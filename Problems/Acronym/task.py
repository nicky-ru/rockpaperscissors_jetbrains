# read test.txt
test = open('test.txt', 'r', encoding='utf-8')
for line in test:
    print(line[0])
test.close()
