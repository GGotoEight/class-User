import uuid
import hashlib
import email_validator as ev


class User:
    """Class for a work with users"""

    @staticmethod
    def valid_email(email):
        """Check email on validity"""
        ev.validate_email(email)
        return email

    def __init__(self, username: str, password: str, email: str, is_active=True) -> None:
        self.__username = username
        self.__id = uuid.uuid4()
        self.__password = hashlib.sha256(password.encode()).hexdigest()
        self.__email = self.valid_email(email)
        self.__is_active = is_active

    @property
    def email(self) -> str:
        """Return the user's current email if was not passed, else change email"""
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        self.__email = self.valid_email(email)

    @property
    def username(self) -> str:
        """Return the username if was not passed, else change it"""
        return self.__username

    @username.setter
    def username(self, inp_username: str) -> None:
        self.__username = inp_username

    def get_id(self) -> uuid.UUID:
        """Return user's id"""
        return self.__id

    def change_activate(self) -> None:
        """Change user's active between True and False"""
        self.__is_active = not self.__is_active

    def check_active(self) -> bool:
        """Return the user's current active (True or False)"""
        return self.__is_active

    def verify_password(self, password: str) -> bool:
        """Verifies that the entered password is correct"""
        return hashlib.sha256(password.encode()).hexdigest() == self.__password


if __name__ == '__main__':
    incorrect_email = 'asd@asd@gmail.com'

    user1 = User('Паша', '123321', 'pasha@gmail.com')
    print('First user has been created')

    try:
        user2 = User('Лёва', 'qwerasd', incorrect_email)
        raise Exception("First check on validity of the email has been lost")
    except ev.EmailNotValidError:
        user2 = User('Лёва', 'qwerasd', 'zxc@mail.ru')
        print('First check on validity of the email has been passed\nSecond user has been created')

    print("Printing first's and second's emails:")
    print(user1.email, user2.email, sep='\n')

    try:
        user1.email = incorrect_email
        raise Exception("Second check on validity of the email has been lost")
    except ev.EmailNotValidError:
        print('Second check on validity of the email has been passed')

    print("Printing username and id of first user:")
    print(user1.username, user1.get_id())

    user2.change_activate()
    print('Check method "change_active()" has been passed')

    print("Printing activate of users:")
    print(user1.check_active(), user2.check_active())

    if not user1.verify_password('123') and user2.verify_password('qwerasd'):
        print('"verify_password()" is work')

    user2.username = 'Парк Горького'
    print("Check of change username has been passed")