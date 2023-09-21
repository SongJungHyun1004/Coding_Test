dir_dict = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}
def in_range(x, y):
    return -5 <= x <=5 and -5 <= y <=5
def solution(dirs):
    lines = set()
    prev = (0, 0)
    for d in dirs:
        x, y = prev
        nx = x+dir_dict[d][0]
        ny = y+dir_dict[d][1]
        if in_range(nx, ny):
            lines.add((x, y, nx, ny))
            lines.add((nx, ny, x, y))
            prev = (nx, ny)
    answer = len(lines)//2
    return answer