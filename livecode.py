"""l1 = [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
print(len(l1))

#Step 1
print(len(l1) // 2 )  # we get the middle index of l1
print(l1[len(l1)// 2]) # is this higher or lower than my item: 76 > 57
l2 = l1[:len(l1)//2] # we discarded half of our list
print(l2)

#Step2
print(l2[len(l2)//2])
print('NOT FLOOR',len(l2)/2)
print('FLOOR',len(l2)//2)
l3 = l2[:len(l2)//2]
print(l3)

# Step3
print(l3[len(l3)//2]) # Done!

def binary_search(lst_sorted, value):
    step = 0
    while len(lst_sorted) > 1:
        step +=1
        print(step)
        middle = len(lst_sorted) // 2
        if lst_sorted[middle] != value:
            if lst_sorted[middle] > value:
                lst_sorted = lst_sorted[:middle]
            elif lst_sorted[middle] < value:
                lst_sorted = lst_sorted[middle:]
        else:
            return True, step
    return False, step 

print(binary_search(range(1, 101), 100)) #---> tuple binary_search(lst, 57)[1] ---> steps

X = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
Y = [binary_search(range(1, N+1), N) [1] for N in X]

print(Y)

import matplotlib.pylab as plt

plt.plot(X, Y, label='log(N)')
plt.xlabel('Input Size')
plt.ylabel('Number of steps')
plt.legend()
plt.title('Binary Search')
plt.show()"""

# Algorithmic thinking
# Divide and Conquer


print('mod :', 64 % 40)

print('mod :', 104 % 40)

def hcf(a, b):
    remainder = a % b
    if remainder == 0:
        return b
    else:
        return str(remainder) + ' ' + str(hcf(b, remainder))

print(hcf(64, 40))

total_area = 64 * 40
print(total_area)
number_of_squares = total_area/(8**2)

print(number_of_squares)

###################################################



#### Quicksort #####

lst = [33, 15, 10] # we can pick for example 33; 33 will be my pivot element


sorted = [15, 10] + [33] + []

def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[1]
        less = [num for num in lst[:1] + lst[2:] if num <= pivot]
        greater = [num for num in lst[:1] + lst[2:] if num > pivot]
        print('##############')
        print(f"pivot: {pivot}")
        print(f"less: {less}")
        print(f"greater: {greater}")

    return quicksort(less) + [pivot] + quicksort(greater) 

#print(quicksort([10, 5, 2, 3, 4, 4, 20]))

lst = [3, 7, 1, 9, 2, 6, 8, 5]
print(lst)
print(quicksort(lst))


