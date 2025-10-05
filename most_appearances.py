def findMostAppearances(nums):
    dict = {}
    
    for i in nums:
        dict[i] = dict.get(i,0) + 1

    print(dict.values())
    
    max = 0

    for i in dict.values():
        if i > max:
            max = i
    print(max)

    res = []
    for i,v in dict.items():
        if v == max:
            res.append(i)
    
    return res

nums = list(map(int, input().split()))
print(findMostAppearances(nums))