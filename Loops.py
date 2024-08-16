import random
# print("Can you name 8 friends of yours:")
# f1 = input('Friend one:')
# f2 = input('Friend two:')
# f3 = input('Friend three:')
# f4 = input('Friend four:')
# f5 = input('Friend five:')
# prompt = [f1,f2,f3,f4,f5]
# print("Your 2024 best friend is",random.choice(prompt))



people = []
print(f"Input the names of 5 people:")
for x in range(0,6):
 person = input()
 people.append(person)

index = random.randint(0,5)

random_person = people[index]
print("Here is the random person", random_person)




 
