def sorted_lists(list):
    for i in range(len(list) - 1):
        for n in range(i + 1, len(list)):
            if list[i] > list[n]:
                list[n], list[i] = list[i], list[n]
    return list

def merge_sorted_lists(list1, list2):
    list1 = sorted_lists(list1)
    list2 = sorted_lists(list2)
    z = 0
    if len(list1) == 0 or len(list2) == 0:
        list1.extend(list2)
        return list1
    elif list1[len(list1) - 1] > list2[len(list2) - 1]:
        for i in range(len(list2)):
            for n in range(z, len(list1)):
                if list2[i] < list1[n]:
                    list1.insert(n, list2[i])
                    z = n + 1
                    break
        return list1
    else:
        for i in range(len(list1)):
            for n in range(z, len(list2)):
                if list1[i] < list2[n]:
                    list2.insert(n, list1[i])
                    z = n + 1
                    break
        return list2
list1 = [10, 2, 3]
list2 = []
merged = merge_sorted_lists(list1, list2)
print(merged)
