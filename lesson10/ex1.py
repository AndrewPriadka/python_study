import random
# https://wit.ai/
# pathlib

with open('qtest.txt') as file:

    arr = [int(line.strip())for line in file]
    # for line in file:
    #     a = int(line.strip())
    #     arr.append(a)

    sr = sum(arr)/len(arr)
    print(sr)



arr1 = []
for namber in range(1, 10):
    arr1.append(random.randint(1, 100))

print(arr1)