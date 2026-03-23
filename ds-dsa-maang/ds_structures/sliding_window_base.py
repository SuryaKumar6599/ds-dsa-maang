def sliding_window(nums, k):
    window_sum = sum(nums[:k])
    print(window_sum)

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        print(window_sum)