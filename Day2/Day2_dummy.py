
def f():
    raise IndexError

def g():
    try:
        print('#1')
        f()
        print('#2')
    finally:
        print('Finally')

g()