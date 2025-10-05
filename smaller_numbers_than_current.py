def smallerNumbersThanCurrent(nums):
    temp = sorted(nums)
    hash = {}

    for idx, val in enumerate(temp):
        if val not in hash:
            hash[val] = idx

    res = []

    for idx in nums:
        res.append(hash[idx])

    return res


nums = list(map(int, input().split(",")))
print(smallerNumbersThanCurrent(nums))