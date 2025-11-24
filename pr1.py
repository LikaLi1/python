# string - 'hello'
# integer - 42
# float - 3.14
# boolean - true/false
# list - [1, 2, 3]
# tuple - (1, 2, 3)
# set - {1, 2, 3}
# disctionary - {'key': 'value'}
# nontype - none

x = 1
print(type(x)) # смотрит тип данных
print(id(x)) # смотрит id (адрес в памяти)

name = input("Enter your name: ")
patronomic = input("Enter your patronomic: ")
last_name = input("Enter your last name: ")

print("Здравствуйте", name)
print("Здравствуйте, " + name + " " + last_name + " " + patronomic + "!")
print(f'Здравствуйте, {name} {last_name} {patronomic}!')
print(f'{2 + 2}')
print(f'Сумма чисел 2 + 2: {2 + 2}')

name = input("Enter your name: ").tutle()
name = name.title()
print(name)

name = input("Enter your name: ")
print(name)
name = name.capitalize()
print(name)

name = input("Enter your name: ")
print(name)
name = name.replace("!", "").replace("a", "o")
print(name)

number = input("Enter your number: ")
print(number)
print(number.lstrip())
print(number.rstrip())
print(number.strip())
print(number.isdigit()) # проверяет состоит ли строка только из цифр

number = int(number)
print(number + 100)
print(number.isalpha())

name = "VASilisa"
print(name.swapcase())
print(len(name))

print(name.lower())

name_2 = "Eva"
# print(name_2.upper())
name_3 = "Eva"
print(name_2 == name_3)

phone = "+1-234-567-8900"
print(phone.startswith("+"))
print(phone.startswith("-"))
print(phone.startswith("*"))
print(phone.endswith("00"))
print(phone.find("-"))
print(phone[::-1])
