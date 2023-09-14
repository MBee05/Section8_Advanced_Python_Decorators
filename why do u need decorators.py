# @classmethod
# @staticmethod

# we going to create @performance decorator 

from time import time

# def performance(fn):
#     def wrapper(*args,**kwargs):
#         t1=time()#will check what time is at the starting
#         result = fn(*args, **kwargs)# will give u the diff btw both time
#         t2=time()#will check end time 
#         print(f'took {t2-t1}s')
#         return result
#     return wrapper

# @performance 
# def long_time():
#     for i in range(10000000):
#         i*5
    
# long_time()
# want to know long it takes in millisecond to permance this code

# took 0.5919280052185059ms



def performance(fn):
    def wrapper(*args,**kwargs):
        t1=time()
        result = fn(*args, **kwargs)
        t2=time()
        print(f'took {t2-t1}s')
        return result
    return wrapper

@performance 
def long_time():
    for i in range(100000000):
        i*5
    
long_time()

# took 4.889807224273682s