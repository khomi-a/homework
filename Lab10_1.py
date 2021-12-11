import argparse
from multiprocessing import Pool
from time import time


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


def print_val(val):
    print(str(val)+':', *factorize(val))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Factorization')
    parser.add_argument('-n', '--num_of_processes', nargs=1, type=int,
                        default=[1], help='number of processes')
    parser.add_argument('values', nargs='+', type=int,
                        help='Input values to be factorized')
    args = parser.parse_args()
    pool = Pool(processes=min(len(args.values), args.num_of_processes[0]))
    output = pool.map(print_val, args.values)
