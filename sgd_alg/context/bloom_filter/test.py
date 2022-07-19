import string
import random
from pybloom import BloomFilter


def get_string(N):
    str_list = [''.join(random.sample(string.ascii_letters + string.digits, random.randint(5, 20))) for x in
                range(int(N))]
    return str_list


if __name__ == '__main__':
    import time

    tic = time.time()

    inners = get_string(1e6)
    outers = get_string(1e4)
    print(len(inners))
    # print(inners)

    tic = time.time()
    f = BloomFilter(capacity=1e6, error_rate=1e-5)

    [f.add(x) for x in inners]


    c = 0
    for x in outers:
        if x in f:
            c += 1
    print(c, len(outers), 1.0 * c / len(outers))

    toc = time.time()
    print(toc - tic)
