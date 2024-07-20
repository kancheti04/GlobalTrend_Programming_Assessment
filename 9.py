import random
import string
def random_password(length=12):
    if length<4:
        raise ValueError("Password length should atleast 4")
    #Characters to be used in password
    characters=string.ascii_letters+string.digits+string.punctuation
    #password should have atleast one of each character type
    password=[
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    #Fill the password with random choices from all characters
    password+=[random.choice(characters)for _ in range(length-4)]
    #Shuffle the password to mix all character types
    random.shuffle(password)
    #convert list to string
    return''.join(password)
print(random_password(12))