from collections import Counter

def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0
    
    for v in arr:
        if v in r3:
            count += r3[v]
        
        if v in r2:
            r3[v*r] += r2[v]
        
        r2[v*r] += 1
        print('k ->', v)
        print('count -> ', count)
        print('v3', r3)
        print('v2', r2)

    return count

arr = [1,3,9,9,27,81]
countTriplets(arr, 3)
