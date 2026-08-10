def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


n = int(input("Enter the number of elements: "))

arr = []

print("Enter", n, "elements in sorted order:")

for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

result = binary_search(arr, key)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")

print("\nTime Complexity:")
print("Best Case: O(1)")
print("Average Case: O(log n)")
print("Worst Case: O(log n)")
print("Space Complexity: O(1)")
