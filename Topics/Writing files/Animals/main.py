# read animals.txt
file = open('animals.txt', 'r')
animals = file.readlines()
# print(animals)
file.close()

new_file = open('animals_new.txt', 'w')
list_size = len(animals)
count = 1
for animal in animals:
    if count < list_size:
        new_file.write(animal.rstrip('\n') + ' ')
        count += 1
    else:
        new_file.write(animal)
        new_file.close()


