print('Create account now')
username = input('Enter username: ')
password = input('Enter Password: ')

print('Account created successfully')
print('Login Now')

username2 = input('Enter username: ')
password2 = input('Enter password: ')

if username == username2 and password == password2:
    print('Logged in successfully')
else:
    print('Invalid credentials')
