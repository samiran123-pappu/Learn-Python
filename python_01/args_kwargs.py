# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
def func(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

func(1, 2, 3)
func(a=10, b=20)
func(1, 2, a=10, b=20)
