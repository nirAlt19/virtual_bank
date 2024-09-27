import bcrypt

secret_key = 'mysecretkey'


#   This function is used to add a secret key and rehash an already encrypted (client side) password
def hash_password(password):
    hashed_password = bcrypt.hashpw((password + secret_key).encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def verify_password(password, hashed_password):
    return bcrypt.checkpw((password + secret_key).encode('utf-8'), hashed_password.encode('utf-8'))
