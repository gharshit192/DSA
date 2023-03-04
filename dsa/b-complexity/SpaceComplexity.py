def main(list):
    n = len(list)
    res = []
    for i in range(n - 1, -1, -1):
        res.append(list[i])

    return res


for list in [[1, 2, 3, 4]]:
    print(main(list))
