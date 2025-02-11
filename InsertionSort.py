import random
import time

def direct_insertion_sort(target: list, reverse=False) -> list:
    result = target[:1]
    for i in range(1, len(target)):
        value = target[i]
        for j in range(len(result)):
            if result[j] >= value:
                result.insert(j, value)
                break
            else:
                if j == len(result) - 1:
                    result.append(value)
    if reverse:
        result = list(reversed(result))
    return result


def half_search(target_list: list, target) -> int:
    left, right = 0, len(target_list) - 1
    if right < 0:
        return 0
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if target_list[mid] == target:
            return mid
        elif target_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if target_list[mid] > target:
        return mid
    else:
        return mid + 1



def half_insertion_sort(target: list, reverse=False) -> list:
    result = target[:1]
    for i in range(1, len(target)):
        value = target[i]
        position = half_search(result, value)
        result.insert(position, value)
    if reverse:
        result = list(reversed(result))
    return result


if __name__ == '__main__':
    l = [random.randint(0, 10000) for i in range(0, 50000)]
    now = int(time.time())
    print(f'第一次执行开始: {now}')
    half_insertion_sort(l)
    print(time.time() - now)
    now = int(time.time())
    print(f'第二次执行开始: {now}')
    direct_insertion_sort(l)
    print(time.time() - now)