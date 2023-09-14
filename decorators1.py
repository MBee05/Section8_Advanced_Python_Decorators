# function are just variable in python

# def hello():
#     print('hellooooo');
    
    
# greet = hello()
# print(greet)
'''hellooooo'''


# greet = hello
# print(greet)

# <function hello at 0x000001D756A30540>  function location in memo then have to call it

# print(greet())
# hellooooo



# if we want to del

# del hello
# hello()
# it delete only the function but not the variable 'greet = hello'



# if want create 

def hello(func):
    func()
    
def greet():
    print('still there!')
    
a=hello(greet)
print(a)

# 'still there!'

# decorators are function that act like variables

