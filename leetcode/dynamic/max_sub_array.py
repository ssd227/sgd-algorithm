
# 给定一个数组，求最大加和子数组
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [nums[0]]
    for i in range(1, len(nums)):
        maxi = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
        dp.append(maxi)
    return dp[-1]
