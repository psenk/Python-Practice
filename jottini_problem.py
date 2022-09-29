# 2.7182818

import random

loop_count, iteration_count, answer, equals_ten = 0, 0, 0, 0

while loop_count < 100000000:
    sum = random.uniform(0.000000000000, 1.000000000000) + random.uniform(0.000000000000, 1.000000000000)
    iteration_count = 2

    while sum < 1:
        sum = sum + random.uniform(0.000000000000, 1.000000000000)
        iteration_count += 1
      
    loop_count += 1
    answer = answer + iteration_count

    if (iteration_count == 10):
        equals_ten = equals_ten + 1

print(float(answer / loop_count))
print(int(loop_count / equals_ten))
