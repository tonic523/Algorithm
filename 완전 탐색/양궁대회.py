import sys

input = sys.stdin.readline


def solution(n, info):
    answer = [0] * 11
    max_point = 0
    apeach_total_point = 0
    for i in range(11):
        if info[i]:
            apeach_total_point += 10 - i
    for i in range(2047, -1, -1):
        t_rion_points = list(map(int, bin(i)[2:].zfill(11)))
        t_rion_arrow_count = 0
        t_rion_total_point = 0
        t_apeach_total_point = apeach_total_point
        for j in range(11):
            if t_rion_points[j] == 1:
                t_rion_arrow_count += info[j] + 1
                t_rion_total_point += 10 - j
                if info[j] > 0:
                    t_apeach_total_point -= 10 - j

        print(t_rion_points, t_rion_arrow_count, t_rion_total_point, t_apeach_total_point)
        if t_rion_arrow_count != n or t_rion_total_point <= t_apeach_total_point:
            continue

        if t_rion_total_point - t_apeach_total_point >= max_point:
            # print(t_rion_points, answer)
            if t_rion_total_point - t_apeach_total_point == max_point:
                # print(t_rion_points, answer)
                for k in range(10, -1, -1):
                    if answer[k] < t_rion_points[k]:
                        answer = t_rion_points
                        break
            else:
                answer = t_rion_points
            max_point = t_rion_total_point - t_apeach_total_point
    if max_point == 0:
        return [-1]
    else:
        for i in range(11):
            if answer[i]:
                answer[i] = info[i] + 1
    return answer


print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))