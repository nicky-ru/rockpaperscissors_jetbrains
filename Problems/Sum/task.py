# read sums.txt
sums = open('sums.txt', 'r', encoding='utf-8')
for line in sums:
    numbers = line.split()
    print(int(numbers[0]) + int(numbers[1]))
sums.close()
