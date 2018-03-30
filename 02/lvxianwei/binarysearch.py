#作业2：二分查找
#输入查找的数字序列（已按从小到大排序）
nums= [0, 1.1, 2, 2.3, 4, 5, 6, 7, 23, 24, 32, 34, 56, 56]
#定义初始变量
start=0
end=len(nums)-1
mid=0
#用户输入查找的数据
check_num=float(input("请输入要查找的号码:"))
#判断查找数据是否在范围内
if nums[0]==check_num:
    print("号码存在,索引位置：",0)
if nums[len(nums)-1]==check_num:
    print("号码存在,索引位置：",len(nums)-1)
if check_num<nums[0] or check_num>nums[len(nums)-1]:
    print("号码不存在")
if check_num>nums[0] and check_num<nums[len(nums)-1]:
    #二分查找
    while True:
        mid=(start+end)//2
        if nums[mid]==check_num:
            print("号码存在,索引位置：",mid)
            break
        if check_num<nums[mid]:
            end=midS
        if check_num>nums[mid]:
            start=mid
        if end-start==1:
            print("号码不存在")
            break
    
