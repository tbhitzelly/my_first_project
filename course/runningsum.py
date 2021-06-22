

nums = [1, 2, 3, 4]
result = []

for i, el in enumerate(nums):
    if i == 0:
        result.append(el)
    else:
        s = el + result[i-1]
        result.append(s)

print(result)