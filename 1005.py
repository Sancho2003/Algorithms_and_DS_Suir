from itertools import combinations


def computing(weights):
    total_weights_sum = sum(weights)
    diff = total_weights_sum
    for combination_size in range(0, len(weights)):
        for combination in combinations(weights, combination_size):
            if abs(total_weights_sum - 2 * sum(combination)) < diff:
                diff = abs(total_weights_sum - 2 * sum(combination))
    print(int(diff))


n = int(input())
a = input()
w = a.split()
stone_weights = []
for i in w:
    stone_weights.append(int(i))

computing(stone_weights)
