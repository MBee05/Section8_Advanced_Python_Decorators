# def my_decorator(func):
#     def wrap_func():
#         func()
#     return wrap_func


# @my_decorator
# def hello():
#     print('helloooooooooo')

# hello()


# helloooooooooo

# it is same as 
# def hello():
#     print('helloooooooooo')

# hello()

# but decorators we can add some other function

# def my_decorator(func):
#     def wrap_func():
#         print('************')
#         func()
#         print('************')
#     return wrap_func


# @my_decorator
# def hello():
#     print('helloooooooooo')

# hello()

'''
************
helloooooooooo
************
'''


# def my_decorator(func):
#     def wrap_func():
#         print('************')
#         func()
#         print('************')
#     return wrap_func


# @my_decorator
# def hello():
#     print('helloooooooooo')
# def bye():
#     print('see u later')
    
# bye()
# see u later



# def my_decorator(func):
#     def wrap_func():
#         print('************')
#         func()
#         print('************')
#     return wrap_func


# @my_decorator
# def hello():
#     print('helloooooooooo')
    
# @my_decorator
# def bye():
#     print('see u later')
    
# # bye()

'''
************
see u later
************
'''


def my_decorator(func):
    def wrap_func():
        print('************')
        func()
        print('************')
    return wrap_func



def hello():
    print('helloooooooooo')
    

def bye():
    print('see u later')
    
    
hello2 =my_decorator(hello)
hello2()


'''
************
helloooooooooo
************
'''     
# or

my_decorator(hello)()

'''************
helloooooooooo
************'''