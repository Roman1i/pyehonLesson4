nums = list(map(int, input().split()))
nums_2 = []

for i in range(len(nums)):
    c = 0
    for j in range(len(nums)):
        if i != j:
            if nums[i] == nums[j]:
                c += 1
    if c == 0:
        nums_2.append(nums[i])

print(nums)
print(nums_2)
