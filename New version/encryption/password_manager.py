# encryption/password_manager.py

encryption = {
  "a": "c", "b": "o", "c": "i", "d": "z", "e": "y", "f": "f", "g": "h", "h": "j", "i": "k", "j": "l", "k": "m", "l": "n", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "a", "w": "b", "x": "d", "y": "e", "z": "g", 
  "#": "1", "!": "5", "?":"8", "/": "3", "," : ";", ";": "9","~": "&", "&" : "+", "%" : "-", "-" : "_", "_": "-",
  "0" : "#", "1" : "!", "2": "3", "3" : "4", "4" : "?", "5" : "6", "6" : "7", "7" : "/", "8": "9", "9" : "0"   
}

class PasswordManager:
    def encrypt(self, password, shift=3):
        password_encrypter = ""
        for elem in password:
            password_encrypter += encryption[elem.lower()]
        # print(password_encrypter)
        return password_encrypter

    def check_password(self, encrypted_password, plain_password, shift=3):
        return encrypted_password == self.encrypt(plain_password, shift)