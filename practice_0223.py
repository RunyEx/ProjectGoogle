# function
def awesum(a, b):
    return  a+b
print(awesum(b=200, a=10))
print(awesum(100,300))

def exam_arg(*args):
    print(args)
    print(args[1])
    print(type(args))
exam_arg("test", "print", 123)

def exam_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
exam_kwargs(key="text", word="print", args=123)

def exam_docstring(*args):
    """
    :param args:
    :return:
    """
print(exam_docstring.__doc__)
# print(print.__doc__)
