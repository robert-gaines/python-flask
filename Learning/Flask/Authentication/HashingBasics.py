from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'password'

hashed_password = bcrypt.generate_password_hash(password)

print(hashed_password)

check = bcrypt.check_password_hash(hashed_password,'incorrect_password')

print(check)
