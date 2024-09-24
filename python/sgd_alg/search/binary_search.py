'''
二分查找

todo 可以改写成ST, rank helper function(number of keys < key)
'''

def binary_search(nums, target):
    """ 
        输入
        :param nums: 有序数组
        :param target: 查找值
        
        :return: 
            查找成功, 返回index
            查找失败, 返回-1
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
