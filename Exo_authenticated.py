# create an authenticated decorator that only allows the function to run is user1 has a 'valid' set to True:

user1 = {
    'name':'Sona',
    'valid': True #changing this will either run or not run the messge_friends function
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result
    return wrapper
    
@authenticated
def message_friends(user):
    print('message has been sent')
    
message_friends(user1)

# message has been sent




# solution
user1 = {
    'name':'Sona',
    'valid': True
}
def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            result = fn(*args, **kwargs)
        return result
    return wrapper
    
@authenticated
def message_friends(user):
    print('message has been sent')
    
message_friends(user1)

# # message has been sent