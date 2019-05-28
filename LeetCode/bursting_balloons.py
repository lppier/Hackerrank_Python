def maxCoins(iNums):
    nums = [1] + [i for i in iNums if i > 0] + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]

    for k in range(2, n):
        print(f"k = {k}")
        for left in range(0, n - k):
            print(f"  left = {left}")
            right = left + k
            print(f"  right = {right}")
            for i in range(left + 1,right):
                print(f"    i = {i}")
                dp[left][right] = max(dp[left][right],
                       nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
                print(f"dp[{left}][{right}] = max(dp[{left}][{right}],, nums[{left}] * nums[{i}] * nums[{right}] + dp[{left}][{i}] + dp[{i}][{right}]")
                
    return dp[0][n - 1]

maxCoins([3, 1, 5])