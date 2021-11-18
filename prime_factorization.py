import threading
import sys
import argparse
import time


def factorize(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans


def thread_job(val):
    with lock:
        print(str(val)+':', *factorize(val))


parser = argparse.ArgumentParser(description='Factorization')
parser.add_argument('values', nargs='+', type=int,
                    help='Input values to be factorized')
args = parser.parse_args()

lock = threading.Lock()
threads = [threading.Thread(target=thread_job, args=(value, ))
           for value in args.values]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

