from functools import wraps
import os
def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func() #将传进来的函数执行

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

#1
#@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

#1等价于2
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)



