import random
import string

def generate_password(length):
    randomshit = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(randomshit) for _ in range(length))
    return pwd

if __name__ == "__main__": 
    l = int(input("Enter the desired password length: "))
    pwd1 = generate_password(l)
    print("Generated password:", pwd1) 
