
import random
import names
import wonderwords

def generated_data():

    data = {
        "username": None,
        "email": None,
        "password": None
    }

    # Username generator
    name = ""
    match random.randint(1,7):
        case 1:
            name = names.get_first_name()
        case 2:
            name = names.get_last_name()
        case 3:
            name = names.get_full_name().replace(" ", str(random.randint(0,10)))
        case 4:
            name = names.get_full_name().replace(" ", "")
        case 5:
            name = names.get_full_name().replace(" ", "").lower()
        case 6:
            name = names.get_first_name() + str(random.randint(1, 100))
        case 7:
            name = str(random.randint(10000, 1000001))
    data["username"] = name

    # Email generator
    email = ""
    match random.randint(1,3):
        case 1:
            email += data["username"].replace("_", ".").lower()
        case 2:
            email += data["username"].replace("_", str(random.randint(1, 100))).lower()
        case 3:
            email += data["username"].lower() + "." + wonderwords.RandomWord().word()
    
    email += "@" + random.choice([
        "gmail.com",
        "test.com",
        "mail.com",
        "mail.ua",
        "ukr.net",
        "ukr.ua",
        "mymail.com",
        "box.com",
        "email.com"
    ])
    data["email"] = email

    # Password generatore
    symbols = "".join([
        "".join([chr(n) for n in range(65, 91)]),
        "".join([chr(n) for n in range(97, 123)]),
        "".join(str(n) for n in range(0, 10)),
        "_",
        "-",
        "."
    ])
    password = "".join([random.choice(symbols) for _ in range(8, 21)])
    data["password"] = password
    
    return data

