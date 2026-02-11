import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
list_of_elements=[letters,numbers,symbols]
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letters_in_password=nr_letters+nr_symbols+nr_numbers
count=0
print(letters+numbers+symbols)
print("Password Generated: ")
for element in range(0,letters_in_password):

    choose=random.choice(list_of_elements)

    if choose==letters:
        nr_letters-=1
        if nr_letters==0:
            list_to_remove=letters
            list_of_elements.remove(list_to_remove)
    elif choose==numbers:
        nr_numbers-=1
        if nr_letters == 0:
            list_to_remove = numbers
            list_of_elements.remove(list_to_remove)
    else:
        nr_symbols-=1
        if nr_letters == 0:
            list_to_remove = symbols
            list_of_elements.remove(list_to_remove)

    print(random.choice(choose), end=" ")
