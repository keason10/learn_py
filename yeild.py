import contextlib


def fun1():
    yield 1
    yield 2
    yield 3
    return 44


def fun2():
    yield 21
    ret = yield from fun1()
    print(ret)
    yield 22
    return 33


class MTest():
    def __init__(self, fn):
        self.fn = fn

    def __enter__(self):
        print('MTest Class open file')
        return self.fn

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('close')

    def __call__(self, *args, **kwargs):
        self.fn(*args)


@contextlib.contextmanager
def mtest(f1):
    print('contextmanager open file')
    try:
        yield f1
    except Exception as exp:
        print('exp')
    finally:
        print('close')


def fn1(*args):
    print("list:", args)
    return args


def say_hello():
    with mtest(fn1) as a:
        print("say  hello")
        print(a(*[1, 2]))
    print("\r\n")
    with MTest(fn1) as bb:
        print("say  hello")
        print(bb(*[1, 2]))


if __name__ == '__main__':
    ret = fun2()
    print('ret:', ret)
    l1 = list(x for x in ret)
    print(l1, '\r\n\r\n\r\n')

    i1 = iter(fun2())
    while True:
        try:
            print(next(i1))
        except StopIteration as se:
            print(se)
            break
    print('\r\n\r\n\r\n')

    say_hello()
