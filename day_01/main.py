def part_one(filename: str) -> int:
    lines = parse_input(filename)
    return sum(
        find_first_digit(line) * 10 + find_first_digit(line, start_from_end=True)
        for line in lines
    )


def part_two(filename: str) -> int:
    lines = parse_input(filename)
    return sum(
        find_first_digit(line, spelled_digits=True) * 10
        + find_first_digit(line, spelled_digits=True, start_from_end=True)
        for line in lines
    )


def find_first_digit(
    line: list, spelled_digits: bool = False, start_from_end=False
) -> int | None:
    spelled_numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    numbers = {str(ch) for ch in range(0, 10)}
    if not start_from_end:
        for ind, ch in enumerate(line):
            if ch in numbers:
                return int(ch)
            if spelled_digits:
                for word, num in spelled_numbers.items():
                    if line.startswith(word, ind):
                        return num
    else:
        for ind in range(len(line) - 1, -1, -1):
            if (ch := line[ind]) in numbers:
                return int(ch)
            if spelled_digits:
                for word, num in spelled_numbers.items():
                    if line.startswith(word, ind):
                        return num
    return None


def parse_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    input_path = "./day_01/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
