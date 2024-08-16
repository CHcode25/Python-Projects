person = {"name":"john doe", "age": 33,
          "country": "US", "address": "Delaware"}
key = input('What information do you want to know about the person?').lower()
user = person.get(key)
print(user)

num1 = int(input('What is your age?'))
num2 = int(input('What is your sisters age?'))
if (num1 > num2):
    print("She's younger than you")
elif (num1 < num2):
    print("She's older than you")
elif (num1 == num2):
    print("You two are the same age!")
else:
    print('Statement ran successfully')
