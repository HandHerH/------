# 传入有序列表
def binary_find(data: list, target):
    if not isinstance(data, list):
        raise TypeError('invalid data type')
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        elif data[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


if __name__ == '__main__':
    my_data = [1, 3, 4, 6, 45, 67, 78, 99]
    print(binary_find(my_data, 100))
