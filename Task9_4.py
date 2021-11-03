class PrintMean(Exception):
    pass


class PrintVar(Exception):
    pass


class PrintNum(Exception):
    pass


def stat_coroutine():
    print("Starting coroutine")
    m = 0
    v = 0
    n = 0
    s = 0
    s_sq = 0
    try:
        while True:
            try:
                x = yield
                m = (m * n + x) / (n + 1)
                s += x
                s_sq += x**2
                n += 1
                v = (s_sq - 2 * m * s + n*m**2)/n
            except PrintMean:
                yield m
            except PrintVar:
                yield v
            except PrintNum:
                yield n
    finally:
        print("Stop coroutine")


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


coroutine = stat_coroutine()
next(coroutine)

while True:
    i = input()
    if i not in ('mean', 'var', 'num', 'close') and not is_number(i):
        raise ValueError('Inmupts can be only commands mean, var, num, close or float numbers')
    if i == 'mean':
        print("Current mean:", coroutine.throw(PrintMean))
        next(coroutine)
    elif i == 'var':
        print("Current varience:", coroutine.throw(PrintVar))
        next(coroutine)
    elif i == 'num':
        print("Current number:", coroutine.throw(PrintNum))
        next(coroutine)
    elif i == 'close':
        coroutine.close()
        break
    else:
        coroutine.send(float(i))

# Starting coroutine
# 0
# 1
# var
# Current varience: 0.25
# 3
# 5
# mean
# Current mean: 2.25
# 6
# num
# Current number: 5
# close
# Stop coroutine
