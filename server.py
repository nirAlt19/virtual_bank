from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from users.api_handlers import UserRegistration, UserLogin
from status.api_handlers import DBKeepAlive
from bank_accounts.api_handlers import OpenAccount

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
api = Api(app)


# Add the resources to the API
api.add_resource(UserRegistration, '/users')
api.add_resource(UserLogin, '/users/login')
api.add_resource(DBKeepAlive, '/status')
api.add_resource(OpenAccount, '/accounts') #todo: Not accounts/open? Do i have to add every sub individualy?

#TODO: Only working with host 0.0.0.0?
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')