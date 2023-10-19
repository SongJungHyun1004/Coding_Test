def convert(x):
    x = list(x)
    for i in range(len(x)):
        if x[i] == '#':
            x[i] = ''
            x[i-1] = x[i-1].lower()
    return ''.join(x)
def solution(m, musicinfos):
    answer = '(None)'
    max_play = -1
    m = convert(m)
    for info in musicinfos:
        start, end, title, msheets = info.split(',')
        sh, sm = start.split(":")
        eh, em = end.split(":")
        playtime = int(eh)*60+int(em) - (int(sh)*60+int(sm))
        playmusic = ''
        msheets = convert(msheets)
        if len(msheets) >= playtime:
            playmusic = msheets[:playtime]
        else:
            playmusic = msheets*(playtime//len(msheets))+msheets[:playtime%len(msheets)]   
        if m in playmusic and max_play < playtime:
            answer = title
            max_play = playtime
    return answer