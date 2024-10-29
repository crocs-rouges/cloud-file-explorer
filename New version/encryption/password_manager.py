# encryption/password_manager.py

class PasswordManager:
    def encrypt(self, password, shift=3):
        return ''.join(
            chr((ord(char) + shift - 97) % 26 + 97) if char.islower() else char
            for char in password
        )

    def check_password(self, encrypted_password, plain_password, shift=3):
        return encrypted_password == self.encrypt(plain_password, shift)
