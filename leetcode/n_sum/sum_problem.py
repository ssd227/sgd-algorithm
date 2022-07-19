# return min gap between sum of two nums and target
def two_sum_closet(nums, target):
    nums.sort()
    pl = 0
    pr = len(nums) - 1

    min_gap = None
    while pl < pr:
        tmp = nums[pr] + nums[pl]
        gap = abs(tmp - target)

        if gap == 0:
            return 0

        if min_gap is None:
            min_gap = gap
        else:
            min_gap = min(gap, min_gap)

        if tmp < target:
            pl += 1
        if tmp > target:
            pr -= 1

    return min_gap


def two_sum(inums, target):
    '''
    :param inums: sorted nums
    :param target:
    :return: list of result    res2
    '''
    res2 = []
    if inums is None or inums == []:
        return res2

    pl = 0
    pr = len(inums) - 1
    while (pl < pr):
        x = inums[pl] + inums[pr]
        if x == target:
            res2.append([inums[pl], inums[pr]])
        if x < target:
            pl += 1
        else:
            pr -= 1

    return res2

    return res2


def threesum(nums):
    '''
    a+b+c = 0
    :param nums:
    :param target:
    :return:
    '''

    res3 = set()
    nums.sort()

    for i in range(len(nums)):
        x = nums[i]
        res2 = twosum(nums[i + 1:], -x)
        for a, b in res2:
            candi = [x, a, b]
            candi.sort()
            res3.add(tuple(candi))

    return list(res3)


if __name__ == '__main__':
    # res = twosum_closet([-1, 2, 1, -4], 4)
    # print(res)

    res3 = threesum([-1, 0, 1, 2, -1, -4])
    print(res3)
