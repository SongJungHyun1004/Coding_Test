import math
max_time = 23*60+59
def solution(fees, records):
    answer = []
    standard_time, standard_fee, unit_time, unit_fee = fees
    park_info = {}
    parking_time = {}
    for record in records:
        time, number, inout = record.split()
        hour, minute = map(int,time.split(":"))
        time = hour * 60 + minute
        if inout == "IN":
            park_info[number] = time
        else:
            if number in parking_time:
                parking_time[number] += time - park_info[number]
            else:
                parking_time[number] = time - park_info[number]
            del park_info[number]
    for number, time in park_info.items():
        if number in parking_time:
            parking_time[number] += max_time - park_info[number]
        else:
            parking_time[number] = max_time - park_info[number]
    parking_time = sorted(parking_time.items(), key=lambda x: x[0])
    for number, time in parking_time:
        answer.append(standard_fee + max(0, math.ceil((time-standard_time)/unit_time))*unit_fee)
    return answer