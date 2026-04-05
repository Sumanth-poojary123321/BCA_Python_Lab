n = int(input("Enter total number of elements: "))

# Create an empty list to store all elements
glist = [10,20,30]

# Loop to take input elements from user
for i in range(n):
    glist.append(input(f"Enter element no {i+1}: "))

# Create an empty list to store unique elements
ulist = []

# Loop through each element in the list
for item in glist:
    # Check if the element appears only once in the list
    if glist.count(item) == 1:
        ulist.append(item)

# Print the given list
print("\nGiven list:", glist)