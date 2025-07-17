# class-User
#### Class for a work with user
You can create and customize user

#### Attributes
- username (str)
- password (str)
- email (str)
- is_active (opt., bool)

#### Properties
- username
- email

#### Methods
- valid_email(email: str) -> str: Check email on validity
- get_id(self) -> uuid.UUID: Return user's id
- change_activate(self) -> None: Change user's active between True and False
- check_active(self) -> bool: Return the user's current active (True or False)
- verify_password(self, password: str) -> bool: Verifies that the entered password is correct
