# google
# googl
# aaoab
# aaoac

def get_position_next_value(s, position):  # 计算第position个元素的最小公共前后缀
    s_head = s[:position]
    j = 1
    while j <= len(s_head):
        if s_head[0:j] == s_head[-j:]:
            j = j + 1
            continue
        else:
            return j - 1
    return 0

def get_next(s):
    s = str(s)
    next_list = [None, 0]
    length = len(s)
    for i in range(2, length):
        next_list.append(get_position_next_value(s, i))

    return next_list

def kmp_search(s, target, next_list=None):
    s = str(s)
    if next_list is None:
        next_list = get_next(target)
    i = 0
    j = 0
    while (i < len(s)) and (j < len(target)):
        if s[i] == target[j]:
            i = i + 1
            j = j + 1
        else:
            if next_list[j] is None:
                i = i + 1
                j = j + 1
            else:
                j = next_list[j]
    if j == len(target):
        return i - j
    return None


if __name__ == '__main__':
    s1 = 'abcd999googlejjjd'
    print(kmp_search(s1, 'google'))
