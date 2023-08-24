def solution(id_list, report, k):
    report = list(set(report))
    report_dict = dict(zip(id_list, [[] for _ in range(len(id_list))]))
    for r in report:
        reporter, reported = r.split()
        report_dict[reported].append(reporter)
    answer = dict(zip(id_list, [0 for _ in range(len(id_list))]))
    for r in report_dict:
        if len(report_dict[r]) >= k:
            for r2 in report_dict[r]:
                answer[r2] += 1

    return list(answer.values())