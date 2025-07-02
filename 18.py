def max_path_sum(arr):
    for i in range(len(arr)-2, -1, -1):
        for j in range(len(arr[i])):
            arr[i][j] += max(arr[i+1][j], arr[i+1][j+1])


filename = "18.txt"
arr = []

with open(filename, 'r') as file:
    for line in file:
        numbers = list(map(int, line.strip().split()))
        arr.append(numbers)

max_path_sum(arr)
print(arr)
