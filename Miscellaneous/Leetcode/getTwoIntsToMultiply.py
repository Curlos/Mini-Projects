def GetTwoIntsMultiplyTo(nums, product):
    nums = set(nums)
    for num in nums:
        if num != 0 and product % num == 0 and product // num in nums:
            return num, product//num

print(GetTwoIntsMultiplyTo([2,4,1,6,5,4,0,-1], 20))