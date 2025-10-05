def findDisappearedNumbers(nums):
    set_nums = set(nums)
    res = []
    for n in range(1,len(nums)+1):
        if n not in set_nums:
            res.append(n)

    return res


nums = list(map(int, input().split(",")))
print(findDisappearedNumbers(nums))