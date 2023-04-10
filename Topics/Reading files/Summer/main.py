#  write your code here 

file = open('data/dataset/input.txt', 'r')

count = 0
for line in file:
    # print(line)
    if line == 'summer\n':
        count += 1

file.close()

print(count)
