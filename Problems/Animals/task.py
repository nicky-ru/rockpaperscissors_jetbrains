# read animals.txt
animals = open('animals.txt', 'r')
# and write animals_new.txt
animals_new = open('animals_new.txt', 'w')
for animal in animals:
    animals_new.write(animal.strip() + ' ')
animals_new.close()
animals.close()
