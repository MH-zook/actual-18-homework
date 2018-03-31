#encoding: utf-8

key = 21

nums = [5,13,19,21,37,56,64,75,80,88,92]

min_idx = 0

max_idx = len(nums) - 1


if key in nums:

    while True:

        mid_idx = (min_idx + max_idx)//2

        if nums[mid_idx] > key:
            max_idx = mid_idx
        elif nums[mid_idx] < key:
            min_idx = mid_idx
        else:
            print(str(key)+ '位于第'+str(mid_idx)+'位置')
            break
else:
    print(str(key)+ '没在列表中！')









