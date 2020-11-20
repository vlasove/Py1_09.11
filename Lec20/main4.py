"""
Передача функции как параметра.
"""

def hello():
    print("Hello!")

def foo(f):
    print("Before argument call")
    f()
    print("After argument call")



foo(hello)