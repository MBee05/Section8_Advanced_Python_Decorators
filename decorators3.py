
# def my_decorator(func):
#     def wrap_func(x):
#         print('************')
#         func(x)
#         print('************')
#     return wrap_func


# @my_decorator
# def hello(greeting):
#     print(greeting)
    
# hello('hiiiii')
'''
************
hiiiii
************
'''



# def my_decorator(func):
#     def wrap_func(x,y):
#         print('************')
#         func(x,y)
#         print('************')
#     return wrap_func


# @my_decorator
# def hello(greeting, emoji):
#     print(greeting, emoji)
    
# hello('hiiiii', ':)')

'''
************
hiiiii :)
************
'''

# ******decorator pattern******************
# we can pass as many arguments as we want in the func using '*args,**kwargs' and unpacking them ' func(*args,**kwargs)'
def my_decorator(func):
    def wrap_func(*args,**kwargs):
        print('************')
        func(*args,**kwargs)
        print('************')
    return wrap_func


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)
    
hello('hiiiiii')

'''
************
hiiiiii :(
************'''

# these syntax is why decorators are powerful
def my_decorator(func):
    def wrap_func(*args,**kwargs):
        func(*args,**kwargs)
    return wrap_func
