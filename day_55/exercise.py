# class User:
#     def __init__(self,name):
#         self.name=name
#         self.is_logged_in= False  
# def is_authenticated_decorator(function):
#     def wrapper(*args,**kwargs):
#         if args[0].is_logged_in==True:
#             function(args[0])
#     return wrapper
# def creat_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")

# new_user=User('George')
# new_user.is_logged_in=True
# creat_blog_post(new_user)


########################### TODO: Create the logging_decorator() function 👇

# Create a logging_decorator() which is going to print the name of the function that was called, the arguments it was given and finally the returned output: 

# You called a_function(1,2,3) 
# It returned: 6 
# The value 6 is the return value of the function.



# Don't change the body of a_function. 



# IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise. 

# TODO: Use the decorator 👇

def logging_decorator(func):
    def wrapp(*args):
        name=func.__name__
        arguments=args
        result=func(*args)
        print(f"You called {name}{arguments}")
        print(f"It returned: {result}")
        print(f"The value {result} is the return value of the function.")
    return wrapp

@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)
###########################################################################
def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
        return result
    return wrapper
 
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)