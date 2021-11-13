def median(li):
    li.sort()
    count = len(li)
    
    if count == 0:
        return None
    if count % 2 == 1:
        mid = count // 2
        return li[mid]
    else:
        mid2 = count // 2
        mid1 = mid2 - 1
        return (li[mid1] + li[mid2]) / 2

run_robin = [95, 88, 47, 0, 10, 1, 5, 12, 0, 3]
run_shomit = [10, 40, 20, 37, 0, 1, 25, 35, 30, 33]

median_robin = median(run_robin)
median_shomit = median(run_shomit)

print("Median run for Robin", median_robin)
print("Median run for Shomit", median_shomit)