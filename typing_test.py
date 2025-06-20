from typing import NewType

MyNum = NewType("MyNum", float)


def main() -> None:
    i = MyNum(2.3)
    print(i)


if __name__ == "__main__":
    main()
