__all__ = ['A', 'test1']


class A:
    def __init__(self):
        pass


def test1():
    print('----test1')


def test2():
    print('----test2')


print('__name__:', __name__)
if __name__ == '__main__':
    test2()
