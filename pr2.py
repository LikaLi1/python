# if elif else
# if условие:
#   блок кода - выполняется если условие True

temperature = 25

if temperature >= 30:
  print("Temperature is ok for walk")
elif temperature >= 25:
  print("Temperature is good")
else:
  print("Temperature is bad")

# and or

if temperature > 30 or temperature > 25:
    print("Temperature must be between 30 and 25")

has_license = True
age = 20

if has_license and age >= 21:
  print("Ok")
else:
  print("Oops")

age = 17 
status = "Совершенолетний" if age >= 18 else "Несовершенолетний"
print(status)

for i in range(10):
  print(i)

even_number = [i for i in range(10) if i % 2 == 0]
print(even_number)

for i in range(10, -1, -1):
  if i % 2 == 0: 
    print(i)

while age < 18:
  age += 1
print(age)
