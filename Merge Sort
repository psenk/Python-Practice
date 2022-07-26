import random

rand_list = []

# for loop to add random numbers into list of size 100
# adding random ints between 0 - 999 to list
for i in range(0,1000):
    list_add = random.randint(0,1000)
    rand_list.append(list_add)

print("Bubble sort!\n")

# printing unsorted list first
print(f"Unsorted list:\n{rand_list}\n")

# delaring temp storage variable and flag to stop loop
temp_store = None
swapped = True

# while flag is true, keep going
while(swapped):
    swapped = False
# for loop for iterating through random list
# num = index of list iterator (minus one to prevent out of range exception)
    for num in range(len(rand_list) - 1):
    # sorting list values
        if rand_list[num] > rand_list[num + 1]:
            temp_store = rand_list[num + 1]
            rand_list[num + 1] = rand_list[num]
            rand_list[num] = temp_store
            # flag a swap as true to restart sort once iterator is over
            swapped = True

# printing sorted list
print(f"Sorted list:\n{rand_list}")
