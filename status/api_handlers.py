from flask_restful import Resource
from providers.db import connect_db

#todo: Just exposed like that? Is connecting and closing enough?
class DBKeepAlive(Resource):
    def post(self):
        try:
            connection = connect_db()
            connection.close()

            return {
                'message': 'DB connected successfully',
            }, 201
        except Exception as e:
            return {
                'message': 'Database unavailable',
            }, 503

