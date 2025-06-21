import asyncio as a


def main() -> None:
    i: int = 5
    print(a.run(countdown(i)))

    print("with runner:")
    with_runner()

    print(i)


def with_runner() -> None:
    with a.Runner() as r:
        i: int = 3
        print(r.run(countdown(i)))
        print("---")
        print(r.run(countdown(i)))


async def countdown(n: int) -> str:
    while n > 0:
        print(str(n))
        await a.sleep(0.3)
        n -= 1
    return "liftoff!"


if __name__ == "__main__":
    main()
