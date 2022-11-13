import random

user_name = input("Hi, what is your name? \n")
number = random.randint(1, 20)
print(f"well, {user_name}, I am thinking about number between 1 and 20")


while True:
  guess_number = int(input("take a guess! enter your number: "))
  if guess_number == number:
    print(f"well done, {user_name}! you win!")
  elif 1 <= guess_number <= 20 and guess_number < number:
    print("try bigger number")
  elif 1 <= guess_number <= 20 and guess_number > number:
    print("try smaller number")
  elif not 1 <= guess_number <= 20:
    print("it is out of my range!")