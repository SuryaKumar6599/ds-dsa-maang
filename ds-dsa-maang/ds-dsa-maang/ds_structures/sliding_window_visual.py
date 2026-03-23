def sliding_window_visual(nums, k):
    print(f"Array: {nums}, Window size: {k}\n")

    window_sum = sum(nums[:k])
    print(f"Window {nums[:k]} -> Sum = {window_sum}")

    for i in range(k, len(nums)):
        out_elem = nums[i - k]
        in_elem = nums[i]
        window_sum += in_elem - out_elem

        print(
            f"Slide: remove {out_elem}, add {in_elem} -> "
            f"Window {nums[i-k+1:i+1]} -> Sum = {window_sum}"
        )


if __name__ == "__main__":
    sliding_window_visual([1, 2, 3, 4, 5], 3)