def possible_pairs(subh, target):
    '''
    two points problem
     we need to find all pairs b+c > target

    :param subh:  sorted array
    :param target: length of a
    :return:  all candi pairs
    '''
    pairs = []

    pl = 0
    pr = len(subh) - 1

    while (pl < pr):
        b = subh[pl]
        c = subh[pr]
        if b + c > target:
            for bi in range(pl, pr):
                pairs.append([subh[bi], c])
            pr -= 1
        else:
            pl += 1
    return pairs


def triangle_count(h):
    h.sort()

    res = []

    for i in range(len(h)):
        a = h[i]
        candi_pairs = possible_pairs(h[i + 1:], a)
        print(a, candi_pairs)
        for b, c in candi_pairs:
            if a + b > c and b + c > a and a + c > b:
                res.append([a, b, c])

    return len(res)


if __name__ == '__main__':
    h1 = [3, 4, 6, 7]
    print(triangle_count(h1))
