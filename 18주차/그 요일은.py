m1, d1, m2, d2 = map(int, input().split())
A = input()
month, day = m1, d1
elapsed_days = 0

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

while True:
    if month == m2 and day == d2:
        break

    elapsed_days += 1
    day += 1

    if day > num_of_days[month]:
        month += 1
        day = 1
elapsed_days += 1
if week.index(A) <= elapsed_days%7:
    print(elapsed_days//7+1)
else:
    print(elapsed_days//7)