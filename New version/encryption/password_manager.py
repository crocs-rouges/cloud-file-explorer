# encryption/password_manager.py

class PasswordManager:
    def encrypt(self, password, shift=3):
        return password

    def check_password(self, encrypted_password, plain_password, shift=3):
        return encrypted_password == self.encrypt(plain_password, shift)
