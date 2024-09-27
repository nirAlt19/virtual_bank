from flask_restful import Resource, reqparse
from datetime import datetime
import logging
from uuid import uuid4
from providers.db import get_postgresql_cursor
from psycopg2.errors import UniqueViolation
from users.user import User

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class UserRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('first_name', type=str, required=True, help='First Name cannot be blank')
        parser.add_argument('last_name', type=str, required=True, help='Last Name cannot be blank')
        parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        parser.add_argument('hashed_password', type=str, required=True, help='Password cannot be blank')

        args = parser.parse_args()
        args['user_id'] = uuid4().__str__()  # todo: Using uuid object like this? Any other uses?

        user = User(**args)

        query = (f"INSERT INTO users (id, first_name, last_name, email, password_hash, created_at, updated_at) VALUES "
                 f"('{user.user_id}', '{user.first_name}', '{user.last_name}', '{user.email}', '{user.hashed_password}', "
                 f"'{datetime.utcnow()}', '{datetime.utcnow()}')")
        print(query)
        # todo: Need to handle connection
        cursor = get_postgresql_cursor()

        try:
            cursor.execute(query)
        except UniqueViolation:
            return {
                'message': 'Owner account already exists',
                'owner': user.email,
            }, 400
        finally:
            cursor.close()

        return {
            'message': 'User created successfully',
            'user': args
        }, 201


class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        parser.add_argument('hashed_password', type=str, required=True, help='Password cannot be blank')

        args = parser.parse_args()
        email = args.get('email')

        query = f"SELECT * FROM users WHERE email = '{email}'"
        # todo: Need to handle connection
        cursor = get_postgresql_cursor()
        cursor.execute(query)
        #todo: Can we assume there are no duplicates?
        response = cursor.fetchone()
        cursor.close()

        #todo: What is the appropriate error code to return here?
        if not response:
            return {
                'message': 'User not found'
            }, 404

        password = response.get('password_hash')
        if password != args.get('hashed_password'):
            return {
                'message': 'Incorrect password'
            }, 401

        #todo: Work on the response. Do we need to initialize a user object?
        return {
            'message': f'User {email} logged in successfully',
            'user': args
        }, 201