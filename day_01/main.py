def part_one(filename: str) -> int:
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    calibration_sum = 0
    for line in lines:
        first_digit = find_first_digit(line)
        last_digit = find_first_digit(line[::-1])
        calibration_sum += 10 * first_digit + last_digit

    return calibration_sum


def part_two(filename: str) -> int:
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    calibration_sum = 0
    for line in lines:
        for ind, ch in enumerate(line):
            found = False
            if ch in numbers:
                first_digit = int(ch)
                found = True
            else:
                for l in range(min_word_length, max_word_length):
                    if (
                        ind + l < len(line)
                        and (spelled_number := line[ind : ind + l]) in spelled_numbers
                    ):
                        first_digit = spelled_numbers[spelled_number]
                        found = True
            if found:
                break
        for ch in line[::-1]:
            if ch in numbers:
                last_digit = int(ch)
                break
        calibration_sum += 10 * first_digit + last_digit

    return calibration_sum


def find_first_digit(line: list, spelled_digits: bool = False) -> int:
    numbers = {str(ch) for ch in range(0, 10)}
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
    max_word_length = max([len(word) for word in spelled_numbers])
    min_word_length = min([len(word) for word in spelled_numbers])
    for ch in line:
        if ch in numbers:
            return int(ch)
        elif spelled_digits:
            for l in range(min_word_length, max_word_length):
                if (
                    ind + l < len(line)
                    and (substring := line[ind : ind + l]) in spelled_numbers
                ):
                    return spelled_numbers[substring]


if __name__ == "__main__":
    input_path = "./day_01/example2.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
