def solution(msg):
    answer = []
    index_list = [i for i in range(1, 27)]
    word_list = [chr(w) for w in range(ord('A'), ord('Z') + 1)]
    lzw_dict = dict(zip(word_list, index_list))
    p = 0
    next_index = 27
    while p < len(msg):
        long_w = ""
        for j in range(p + 1, len(msg)+1):
            w = msg[p:j]
            if w in lzw_dict and len(w) > len(long_w):
                long_w = w
            elif w not in lzw_dict or j == len(msg):
                answer.append(lzw_dict[long_w])
                lzw_dict[w] = next_index
                next_index += 1
                p += len(long_w)
                break
            if p == len(msg) - len(long_w):
                answer.append(lzw_dict[long_w])
                p += len(long_w)
    return answer