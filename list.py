def find_special_points(nums):
    if not nums:
        return []

    def is_increasing_from(index):
        for i in range(index, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True

    def is_decreasing_from(index):
        for i in range(index, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                return False
        return True

    special_points = []

    for i in range(1, len(nums) - 1):
        if (nums[i - 1] < nums[i] > nums[i + 1] and is_decreasing_from(i + 1)) or \
           (nums[i - 1] > nums[i] < nums[i + 1] and is_increasing_from(i + 1)):
            special_points.append(nums[i])

    return special_points

def debug_tests():
    outputs = {
        '[1, 2, 3, 4, 3, 2, 1]': find_special_points([1, 2, 3, 4, 3, 2, 1]),
        '[1, 2, 3, 4, 5]': find_special_points([1, 2, 3, 4, 5]),
        '[5, 4, 6, 2, 3, 4, 5]': find_special_points([5, 4, 6, 2, 3, 4, 5]),
        '[5, 4, 3, 2, 1]': find_special_points([5, 4, 3, 2, 1]),
        '[5]': find_special_points([5]),
        '[5, 6, 5, 6, 5]': find_special_points([5, 6, 5, 6, 5])
    }

    for input_data, output in outputs.items():
        print(f"For {input_data}, got: {output}")

debug_tests()





