def binary_search(num_list, num):
    first = 0
    last = len(num_list)
    num_found = False
    while first <= last and not num_found:
        middle = int((first+last)/2)
        if num_list[middle] == num:
            num_found = True
        else:
            if num < num_list[middle]:
                last = middle + 1
            else:
                first = middle - 1
    return num_found


print (binary_search([1,2,3,4,5,6,7,8,9,10], 3))