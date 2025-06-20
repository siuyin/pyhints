import datetime


class Person:
    name: str
    birthdate: datetime.date

    def __init__(self, name: str, birthdate: datetime.date) -> None:
        self.name = name
        self.birthdate = birthdate

    def string(self) -> str:
        return f"name: {self.name}, birthdate: {self.birthdate}"


def main() -> None:
    q = Person("Kit Siew", datetime.date(1962, 2, 28))
    print(q.string())


if __name__ == "__main__":
    main()
