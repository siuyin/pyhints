def main() -> None:
    print(greet("Siu Yin"))
    p_greet("Kit Siew")
    print("---")
    greet_all(["Siu Yin", "Kit Siew"])
    print(get_list())


def greet(name: str) -> str:
    return f"Hello {name}!"


def p_greet(name: str) -> None:
    print(f"Hello {name}!")


def greet_all(names: list[str]) -> None:
    for n in names:
        print(f"Hello {n}!")


def get_list() -> list[str]:
    lst = ["a"]
    lst.append(123)
    return [str(x) for x in lst]
    # return lst


if __name__ == "__main__":
    main()
