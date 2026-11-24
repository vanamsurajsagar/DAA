def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


n = int(input("Enter the number of elements: "))

arr = []

print("Enter", n, "elements:")

for i in range(n):
    arr.append(int(input()))

quick_sort(arr, 0, n - 1)

print("Sorted array:", end=" ")
for element in arr:
    print(element, end=" ")

print("\n\nTime Complexity:")
print("Best Case: O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case: O(n^2)")
print("Space Complexity: O(log n) average")

