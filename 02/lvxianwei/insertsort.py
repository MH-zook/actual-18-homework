#作业1：插入排序
nums=[1.1,2.3,4,56,5,6,7,2,0,56,34,23,24]
print("原始序列：",nums)

#对已有序列排序（冒泡）
tmp=nums[0]
for y in range(len(nums)-1):
    for x in range(len(nums)-y-1):
        if nums[x+1]<nums[x]:
            tmp=nums[x]
            nums[x]=nums[x+1]
            nums[x+1]=tmp
print("插入前排序：",nums)

#插入新数字并重新排序
add_num=float(input("你想插入的数字："))
nums.append(add_num)
tmp=nums[0]
for y in range(len(nums)-1):
    for x in range(len(nums)-y-1):
        if nums[x+1]<nums[x]:
            tmp=nums[x]
            nums[x]=nums[x+1]
            nums[x+1]=tmp
print("插入后排序：",nums)
