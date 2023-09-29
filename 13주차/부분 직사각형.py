def two_point(lst, s):
    count = 0
    end = 0
    interval_sum = 0
    for start in range(len(lst)):
        while interval_sum < s and end < len(lst):
            interval_sum += lst[end]
            end += 1
        if interval_sum == s:
            count += 1
        interval_sum -= lst[start]
    return count

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
h, w = map(int, input().split())
print(two_point(a, h)*two_point(b, w))