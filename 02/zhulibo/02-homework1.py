#encoding: utf-8
nums = [24,13,34,76,56,98,45,43,13,8]


for i in range(1,len(nums)):

    idx = i

    for j in range(i,0,-1):

        if nums[i] < nums[j-1]:

            idx = j-1
        else:
            break
    if idx == i:
        continue
    else:
        nums.insert(idx,nums.pop(i))

print(nums)



