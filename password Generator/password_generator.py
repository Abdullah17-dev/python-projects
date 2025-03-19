import string
import random
def password_generator(length):
    characters = string.ascii_letters+string.digits+string.punctuation

    password = "".join(random.choice(characters) for _  in range(length))
    return password
def main():
    try:

        length = int(input("Enter desired password length: "))
        if length <=0:
             
             print("PLease enter a positive number of password length")
             return
    except ValueError:
        print("invalid input please enter number")
        return
    generated_password = password_generator(length)
    print("Generated password:",generated_password)
main()

