def summary(args: list):
    total = 0
    if len(args) == 0:
        return total
    total = args.pop() + summary(args)
    return total


def len_recursive(list: list):
    if list == []:
        return 0
    list.pop()
    return 1 + len_recursive(list)


def recursive_findmax(list: list):
    if len(list) == 1:
        print(list[0])
        return
    if list[0] > list[1]:
        list[0], list[1] = list[1], list[0]
    list.pop(0)
    recursive_findmax(list)


print(summary([1, 2, 9, 1, 23]))
print(len_recursive([1, 2, 3, 2]))
recursive_findmax([23, 3, 33, 3, 1])
