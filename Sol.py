def majorityElement(nums):

        n=len(nums)
        dic={}
        for i in nums:
            dic[i]=nums.count(i) 
        mx_key=max(dic,key=dic.get) 
        mx_val=dic[mx_key]
        if mx_val>(n/2):
            return mx_key
nums = [3,2,3]
print(majorityElement(nums))
