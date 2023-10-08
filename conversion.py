import pickle


key=23


def encrypt(text):
    encrypted = []
    for char in text:
        encrypted_char = chr(ord(char) ^ key)
        encrypted.append(encrypted_char)
    return ''.join(encrypted)



def decrypt(encrypted_text):
    decrypted = []
    for char in encrypted_text:
        decrypted_char = chr(ord(char) ^ key)
        decrypted.append(decrypted_char)
    return ''.join(decrypted)


def read_file():
    with open("notes.pickle", "rb") as file:
        data = pickle.load(file)

    return eval(decrypt(data))  #decrypting the data and converting it to dictionary


def write_file(data):
    with open("notes.pickle", "wb") as file:
        pickle.dump(encrypt(str(data)),file)

    return True


def read_userfile():
    with open("users.pickle", "rb") as file:
        users_data = pickle.load(file)

    return eval(decrypt(users_data))


def write_userfile(users_data):
    with open("users.pickle", "wb") as users_file:
        pickle.dump(encrypt(str(users_data)), users_file)

    return True
