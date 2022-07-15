list_house = [0, 4, 0, 9, 6]
length = 10
indices = [i + 1 for i, x in enumerate(list_house) if x == 0]
print(indices)
b = 1
tmp = []
result = []
for i in indices:
    # if i :
    #     result.append(0)
    #     if (len(range(1, indices[1])) % 2) == 1:
    #         tmp = list(range(1, (indices[1] // 2)))
    #         result.extend(tmp)
    #         result.append((indices[1] // 2))
    #         result.extend(tmp[::-1])
    #     else:
    #         tmp = list(range(1, ((indices[1] // 2) + 1)))
    #         result.extend(tmp)
    #         result.extend(tmp[::-1])
    #     tmp.clear()
    #     b = indices[1]
    # else:
    print(b)
    if (len(range(b, i)) % 2) == 1:
        tmp = list(range(1, (i // 2)))
        result.extend(tmp)
        result.append((i // 2))
        result.extend(tmp[::-1])
        result.append(0)
    else:
        tmp = list(range(b, ((i // 2) + 1)))
        result.extend(tmp)
        result.extend(tmp[::-1])
        result.append(0)
    b = i
    tmp.clear()

print(result)
