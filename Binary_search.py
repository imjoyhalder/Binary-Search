# Binary Search

def B_search(list,n):
    l = 0
    u = len(list)
    global pos
    pos = -1
    while l<u:
        mid = int((l+u)/2)
        if list[mid] == n: 
            pos = mid
            return True
        else:
            if list[mid] <n:
                l = mid
            else:
                u = mid

list = [1,2,46,2213234,3456,456,356,2345,458,3412,215434523,68734652,678346,25675234675,25723346257234]
n = 25675234675
if B_search(list,n):
    print("Found ")
    print(f"Position is {pos}")
else:
    print("Not Found")