def right_max(h):
    xs = [-1] * len(h)
    tmp_max = h[-1]

    for i in range(len(h) - 2, -1, -1):
        xs[i] = max(tmp_max, h[i + 1])
        tmp_max = xs[i]

    return xs


def left_max(h):
    xs = [-1] * len(h)
    tmp_max = h[0]
    for i in range(1, len(h)):
        xs[i] = max(tmp_max, h[i - 1])
        tmp_max = xs[i]

    return xs


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rm_xs = right_max(height)
        lm_xs = left_max(height)

        print(height)
        print(rm_xs)
        print(lm_xs)

        vol = 0

        for i in range(len(height)):
            if lm_xs[i] == -1 or rm_xs[i] == -1:
                continue

            cv = min(lm_xs[i] - height[i], rm_xs[i] - height[i])
            cv = max(cv, 0)
            print(i, ':', cv, ':', lm_xs[i], rm_xs[i], height[i])
            vol += cv

        return vol


if __name__ == '__main__':
    h1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(h1))
