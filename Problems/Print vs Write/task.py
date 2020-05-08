numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
file_with_list = open('file_with_list.txt', 'w')
file_with_list.write(str(numbers))
file_with_list.close()
