def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


n = int(input("Enter the number of elements: "))

arr = []

print("Enter", n, "elements:")

for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")

print("\nTime Complexity:")
print("Best Case: O(1)")
print("Average Case: O(n)")
print("Worst Case: O(n)")
print("Space Complexity: O(1)")
