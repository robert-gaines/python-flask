from werkzeug.security import generate_password_hash,check_password_hash

hashed_password = generate_password_hash("password")

print(hashed_password)

check = check_password_hash(hashed_password,'incorrect_password')

print(check)
