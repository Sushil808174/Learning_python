def max_subarray_sum(nums):
    if not nums:
        return 0

    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

input_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = max_subarray_sum(input_array)
print(output) 
