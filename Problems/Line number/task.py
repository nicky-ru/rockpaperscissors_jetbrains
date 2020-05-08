# read sample.txt and print the number of lines
sample = open('sample.txt', 'r', encoding='utf-8')
print(len(sample.readlines()))
sample.close()
