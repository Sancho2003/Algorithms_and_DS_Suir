def computing():
    global result
    n, k = [int(i) for i in input().split()]
    all_fights = n * (n - 1) / 2
    n_in_team_min = n // k
    n_in_team_max = n_in_team_min + 1
    teams_with_max_num = n % k
    teams_witn_min_num = k - teams_with_max_num
    excepted_fights = teams_witn_min_num * (n_in_team_min * (n_in_team_min - 1) / 2) + teams_with_max_num * (n_in_team_max * (n_in_team_max - 1) / 2)
    answer = all_fights - excepted_fights
    result.append(answer)


tests = int(input())
result = []
for test in range(tests):
    computing()
for i in result:
    print(int(i))
