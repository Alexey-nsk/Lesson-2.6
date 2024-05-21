import random

list_ = range(3, 21)
ask = random.choice(list_)
print(ask)
answer = ''
for i in range(1, ask):
    for j in range(i + 1, ask + 1):
        if ask % (i + j) == 0:
            answer += str(i) + str(j)

print(answer)
