"""
单调栈
"""

def mono_stack(inums, get_left_min=True):
    """
    找到左边第一个比当前值小的id   复杂度为 O(n)
    :param inums:
    :param get_left_min:
    :return: index
    """

    def larger(a, b):
        return a > b

    def less(a, b):
        return a < b

    if get_left_min:
        compare = larger
    else:
        compare = less

    stack = []
    result = [0] * len(inums)
    for i in range(len(inums)):
        x = inums[i]
        if not stack:  # empty
            stack.append(i)
            result[i] = -1
        else:
            while stack and compare(inums[stack[-1]], x):
                stack = stack[:-1]
            if not stack:
                stack.append(i)
                result[i] = -1
            else:
                result[i] = stack[-1]
                stack.append(i)
    return result


def left_min(li):
    return mono_stack(li, True)


def left_max(li):
    return mono_stack(li, False)


def right_min(li, type=True):
    reli = li[::-1]
    re_res = mono_stack(reli, type)
    res = [len(li) - 1 - id if not id == -1 else -1 for id in re_res]

    return res[::-1]


def right_max(li):
    return right_min(li, False)


if __name__ == '__main__':
    h1 = [2, 3, 7, 2, 3, 7, 1, 657, 347, 233, 46, 8]
    h2 = right_max(h1)

    h3 = [h1[i] if not i == -1 else 'Null' for i in h2]
    print(h1)
    print(h3)
    print(h2)
