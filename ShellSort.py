from InsertionSort import *


# 1 2 3 4 5 6 7 8 9
def shell_sort(target_list):
    length = len(target_list)
    step = length // 2
    while step > 0:
        for i in range(step):
            temp_list = [target_list[j] for j in range(i, length, step)]
            temp_list = half_insertion_sort(temp_list)
            for m in range(len(temp_list)):
                target_list[i + (m * step)] = temp_list[m]
        step = step // 2
    return target_list


if __name__ == '__main__':
    l = [random.randint(0, 10000) for i in range(0, 100000)]

    now = int(time.time())
    print(f'第一次执行开始: {now}')
    half_insertion_sort(l)
    print(time.time() - now)

    now = int(time.time())
    print(f'第二次执行开始: {now}')
    shell_sort(l)
    print(time.time() - now)

    now = int(time.time())
    print(f'第三次执行开始: {now}')
    direct_insertion_sort(l)
    print(time.time() - now)