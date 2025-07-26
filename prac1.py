from collections import defaultdict
def top_k_freq(arr, k):
    # your code
    store=defaultdict(int)
    for i in arr:
        if i in store:
            store[i]+=1
        else:
            store[i]=1
    val = sorted(store.items(),key=lambda x:x[1],reverse=True)[:k]
    return [item[0] for item in val]


print(top_k_freq([1, 1, 1, 2, 2, 3], 2))