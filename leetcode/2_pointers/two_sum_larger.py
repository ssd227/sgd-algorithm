def count_pairs(nums, target):
    N = len(nums)
    nums.sort()

    p1 = 0
    p2 = N - 1
    cc = 0
    while(p1<p2):
        if nums[p1]+nums[p2] >= target:
            cc += (p2-p1)
            p2-=1
        else:
            p1+=1

    return cc



if __name__ == '__main__':
    h1 = [2, 7, 11, 15, 20]
    target = 24
    res =count_pairs(h1, target)
    print(res)