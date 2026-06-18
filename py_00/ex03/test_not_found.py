import inspect
def fun(var)
 f1 = inspect.currentframe()
 try:
 	f2 = f1.f_back.f_locals
    v1 = [name for name, value in f2.items() if value is var][0]
    print(f"variable name: {v1}")
    finally:
        del f1
