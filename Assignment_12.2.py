def suppress_exception(exceptions, result=None):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                return result
        return inner
    return decorator

@suppress_exception(KeyError, result=False)
def authenticate(users, user, password):
    print(f'Authenticating user: {user}')
    return users[user] == password


users = {'harika': '123', 'jahnavi': '456','indu': '789'}

print(authenticate(users, 'harika', '123'))  # True
print(authenticate(users, 'jahnavi', '123'))  # False
print(authenticate(users, 'ravi', '123'))  # False