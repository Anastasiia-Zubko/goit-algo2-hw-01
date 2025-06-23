def find_min_max(arr, left, right):
    # one element
    if left == right:
        return arr[left], arr[right]

    # two elements
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]

    # Recursive case
    mid = (left + right) // 2
    min1, max1 = find_min_max(arr, left, mid)
    min2, max2 = find_min_max(arr, mid + 1, right)

    if min1 < min2:
        overall_min = min1
    else:
        overall_min = min2

    if max1 > max2:
        overall_max = max1
    else:
        overall_max = max2

    return overall_min, overall_max

arr = [2, -4, 1, 9, -6, 7, -3, 25, 13, -55, -34, 44]
min_val, max_val = find_min_max(arr, 0, len(arr) - 1)

print(f"Мінімальний елемент: {min_val}")
print(f"Максимальний елемент: {max_val}")