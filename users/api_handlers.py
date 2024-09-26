from flask_restful import Resource, reqparse
from datetime import datetime
import logging
from uuid import uuid4
from providers.db import get_postgresql_cursor
from users.user import User
from users.auth_service import hash_password, verify_password

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class UserRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('first_name', type=str, required=True, help='First Name cannot be blank')
        parser.add_argument('last_name', type=str, required=True, help='Last Name cannot be blank')
        parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        parser.add_argument('password', type=str, required=True, help='Password cannot be blank')

        args = parser.parse_args()
        # Generate UUID
        args['user_id'] = uuid4().__str__()  # todo: Using uuid object like this? Any other uses?
        # Hash password - comes un-hashed from client
        args['password'] = hash_password(args['password'])

        user = User(**args)

        query = (f"INSERT INTO users (id, first_name, last_name, email, password_hash, created_at, updated_at) VALUES "
                 f"('{user.user_id}', '{user.first_name}', '{user.last_name}', '{user.email}', '{user.password}', "
                 f"'{datetime.utcnow()}', '{datetime.utcnow()}')")
        print(query)
        # todo: Need to handle connection
        cursor = get_postgresql_cursor()
        cursor.execute(query)
        cursor.close()

        return {
            'message': 'User created successfully',
            'user': args
        }, 201


class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        parser.add_argument('password', type=str, required=True, help='Password cannot be blank')

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
        if not len(response):
            return {
                'message': 'User not found'
            }, 404

        if not verify_password(args.get('password'), response.get('password_hash')):
            return {
                'message': 'Incorrect password'
            }, 401

        #todo: Work on the response. Do we need to initialize a user object?
        return {
            'message': f'User {email} logged in successfully',
            'user': {
                'id': response.get('id'),
                'email': response.get('email'),
                'last_updated_at': str(response.get('updated_at'))
            }
        }, 201