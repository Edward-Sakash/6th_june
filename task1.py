
"""Convert this code:
l1 = [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
print(len(l1))

Step 1
print(len(l1) // 2 ) # we get the middle index of l1
print(l1[len(l1)// 2]) # is this higher or lower than my item: 76 > 57
l2 = l1[:len(l1)//2] # we discarded half of our list
print(l2)

Step2
print(l2[len(l2)//2])
print('NOT FLOOR',len(l2)/2)
print('FLOOR',len(l2)//2)
l3 = l2[:len(l2)//2]
print(l3)

Step3
print(l3[len(l3)//2]) # Done!
to a more general function.
The function could start as follows:
def binary_search(lst_sorted, value):
if lst_sorted[len(lst_sorted//2)] == value:
return True
....
....
....
You can use a loop
at each iteration step, check if you have found the value"""
print("_____________________________________________________________")
# Solution 1
def binary_search(lst_sorted, value):
    low = 0
    high = len(lst_sorted) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst_sorted[mid] == value:
            return True
        elif lst_sorted[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return False

# Example usage:
l1 = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
value = 76

mid_index = len(l1) // 2
print(mid_index)

mid_value = l1[mid_index]
print(mid_value)

l2 = l1[:mid_index]
print(l2)

l3_mid_index = len(l2) // 2
print(l2[l3_mid_index])

l3 = l2[:l3_mid_index]
print(l3)

l4_mid_index = len(l3) // 2
print(l3[l4_mid_index])

# Using binary_search function
if binary_search(l1, value):
    print("Value", value, "found in the list.")
else:
    print("Value", value, "not found in the list.")

print("_________________________________________________")



print("_________________________________________________")

def binary_search(lst, value):
    low = 0
    high = len(lst) - 1

    while low <= high:
        middle = (low + high) // 2
        middle_value = lst[middle]

        if middle_value == value:
            return middle
        elif middle_value < value:
            low = middle + 1
        else:
            high = middle - 1

    return -1  # Value not found

# Example usage:
l1 = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
value = 53

index = binary_search(l1, value)
if index != -1:
    print("Value found at index:", index)
else:
    print("Value not found in the list.")
