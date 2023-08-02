"""
单调栈
"""

class Monostack:
    # 单调栈定义
    # 输入：
        # compare_func： stack item应该遵循的顺序
    
    # 类函数 append()：
        # 输入: x-待入栈的item
        # 输出: output[List]-所有不满足栈内排序的元素
       
       # 每次往栈内压入数据时，返回当前栈内不满足order的所有items

    def __init__(self, compare_func):
        self.stack = []
        self.order = compare_func
    
    def size(self):
        return len(self.stack)

    def append(self, x):
        output = []

        if self.size() == 0:
            self.stack.append(x)
        else:
            while self.size()>0 and (not self.order(self.stack[-1], x)):
                output.append(self.stack.pop())
            self.stack.append(x)
        return output # 当前时刻所有的出栈pair

# 不使用类的函数写法
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



