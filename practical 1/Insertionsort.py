def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


n = int(input("Enter the number of elements: "))

arr = []

print("Enter", n, "elements:")

for i in range(n):
    arr.append(int(input()))

insertion_sort(arr)

print("Sorted array:", end=" ")

for element in arr:
    print(element, end=" ")
print("\nTime Complexity:")
print("Best Case: O(n)")
print("Average Case: O(n^2)")
print("Worst Case: O(n^2)")
print("Space Complexity: O(1)")