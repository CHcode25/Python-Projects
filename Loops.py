import random
print("Can you name 8 friends of yours:")
f1 = input('Friend one:')
f2 = input('Friend two:')
f3 = input('Friend three:')
f4 = input('Friend four:')
f5 = input('Friend five:')
prompt = [f1,f2,f3,f4,f5]
print("Your 2024 best friend is",random.choice(prompt))



people = []
x = 0
for x in range(0,5):
    person = input(f"Input the name of person { x + 1}:")
    people.append(person)
    add = random.randint(0,5)

random_person = people[add]
print("Your favorite person is", random_person)




 
