# higher order function _ HOC

# this is HOC bcz this is a function which accept a function as a parameter 
def greet(func):
    func()
    
# or return a function
def greet2():
    def func():
        return 5
    return func


