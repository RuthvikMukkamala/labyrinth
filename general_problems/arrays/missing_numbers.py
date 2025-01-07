def missingNumbers(nums):
    if len(nums) == 0:
        return [1, 2]
    if len(nums) == 1:
        if nums[0] == 1:
            return [2, 3]
        if nums[0] == 3:
            return [1, 2]
        else:
            return [1, nums[0] + 1]

    nums.sort()

    min_val = nums[0]
    max_val = nums[-1]

    full_range = set(range(min_val, max_val + 1))

    missing = list(full_range - set(nums))

    while len(missing) < 2:
        if min_val > 1:
            missing.append(min_val - 1)
            min_val -= 1
        else:
            missing.append(max_val + 1)
            max_val += 1

    return sorted(missing)
