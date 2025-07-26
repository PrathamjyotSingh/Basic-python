def sliding_window_max(nums, k):
    # your code
    l=0
    r=k-1
    store=[]
    while r<len(nums):
        max_val = max(nums[l:r+1])
        store.append(max_val)
        l+=1
        r+=1
    return store


print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))