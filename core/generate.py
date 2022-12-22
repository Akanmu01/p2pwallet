from typing import List


class Main:
    email: List[str]
    password: List[str]

    def __init__(self, email: List[str], password: List[str]) -> None:
        self.email = email
        self.password = password
