class Solution:
    def twosum(self, inums, target):
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

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res3 = set()
        nums.sort()

        map = dict()
        for x in nums:
            if x not in map:
                map[x] =1
            else:
                map[x]+=1

        newli = []
        for k,v in map.items():
            v= min(v,3)
            newli += [k]*v

        newli.sort()
        nums = newli




        for i in range(len(nums)):
            x = nums[i]
            res2 = self.twosum(nums[i + 1:], -x)
            for a, b in res2:
                candi = [x, a, b]
                candi.sort()
                res3.add(tuple(candi))

        return list(res3)