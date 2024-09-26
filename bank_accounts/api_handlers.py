from flask_restful import Resource, reqparse
from datetime import datetime
from psycopg2.errors import UniqueViolation
import logging
from uuid import uuid4
from providers.db import get_postgresql_cursor
from bank_accounts.bank_account import BankAccount, AccountType


class OpenAccount(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('owner', type=str, required=True, help='Owner cannot be blank')
        parser.add_argument('account_type', type=int, required=True, help='Account type is a number and cannot be blank')
        parser.add_argument('initial_balance', type=float, help='Balance must be a number')

        args = parser.parse_args()
        args['account_number'] = account_number = uuid4().__str__()

        initial_balance = args.get('initial_balance') or 0
        args['initial_balance'] = initial_balance

        # todo: No need for the object...
        account = BankAccount(
            account_number=account_number,
            owner=args.get('owner'),
            # account_type=AccountType(args.get('account_type')),
            account_type=args.get('account_type'),
            balance=initial_balance,
            transactions=[]
        )

        query = (f"INSERT INTO bank_accounts (id, owner, account_type, balance, created_at, updated_at) VALUES "
                 f"('{account.account_number}', '{account.owner}', '{account.account_type}', '{account.balance}', "
                 f"'{datetime.utcnow()}', '{datetime.utcnow()}')")
        print(query)
        # todo: Need to handle connection
        cursor = get_postgresql_cursor()
        try:
            cursor.execute(query)
        except UniqueViolation:
            return {
                'message': 'Owner account already exists',
                'owner': account.owner,
            }, 400
        finally:
            cursor.close()

        return {
            'message': 'Account created successfully',
            'account': args
        }, 201





