import bcrypt

secret_key = 'mysecretkey'


#   This function is used to add a secret key and rehash an already encrypted (client side) password
def hash_password(password, salt=b'$2b$12$9/zOLTAjZoufnZnCDEMVXO'): #todo: Move to env?
    hashed_password = bcrypt.hashpw((password + secret_key).encode('utf-8'), salt)
    return hashed_password.decode('utf-8')
