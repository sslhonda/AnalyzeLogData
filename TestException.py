def f1(a,b):
    return f2(a) + f2(b)

def f2(x):
    return 1.0 / x

try:
    f1(1.0,0.0)
except:
    import traceback
    traceback.print_exc()
