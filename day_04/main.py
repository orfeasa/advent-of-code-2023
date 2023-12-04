def part_one(filename: str) -> int:
    scratchcards = parse_input(filename)
    return sum(
        2 ** (len(matches) - 1)
        for winning, current in scratchcards.items()
        if (matches := set(winning).intersection(current))
    )


def part_two(filename: str) -> int:
    return 0


def parse_input(filename: str) -> dict[tuple, set]:
    with open(filename, encoding="utf8") as file:
        return {
            tuple(sorted(map(int, line.split(":")[1].split("|")[0].split()))): set(
                map(int, line.split("|")[1].split())
            )
            for line in file
        }


if __name__ == "__main__":
    input_path = "./day_04/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
