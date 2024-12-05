# encryption/password_manager.py

encryption = {
  "a": "c", "b": "o", "c": "i", "d": "z", "e": "y", "f": "f", "g": "h", "h": "j", "i": "k", "j": "l", "k": "m", "l": "n", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "a", "w": "b", "x": "d", "y": "e", "z": "g"
}

class PasswordManager:
    def encrypt(self, password, shift=3):
        password_encrypter = ""
        for elem in password:
            password_encrypter += encryption[elem.lower()]
        print(password_encrypter)
        return password

    def check_password(self, encrypted_password, plain_password, shift=3):
        return encrypted_password == self.encrypt(plain_password, shift)
