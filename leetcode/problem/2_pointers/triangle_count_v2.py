def possible_pairs(subh, target):
    '''
    two points problem
     we need to find all pairs a+b > c

    :param subh:  sorted array
    :param target: length of a
    :return:  all candi pairs
    '''
    cc = 0
    pl = 0
    pr = len(subh) - 1

    while (pl < pr):
        a = subh[pl]
        b = subh[pr]


        if a + b > target:
            cc += (pr-pl)
            pr -= 1
        else:
            pl += 1

    return cc


def triangle_count(h):
    h.sort()

    res = 0

    for i in range(len(h)-1, -1, -1):
        c = h[i]
        tmp = possible_pairs(h[:i], c)
        res += tmp

    return res


if __name__ == '__main__':
    h1 = [3, 4, 6, 7]
    print(triangle_count(h1))
