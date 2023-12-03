from dataclasses import dataclass
from typing import Set, Tuple


@dataclass(eq=True, frozen=True)
class PartNumber:
    x_start: int
    x_end: int
    y: int
    value: int

    @property
    def neighbors(self) -> Set[Tuple[int, int]]:
        return {(self.x_start - 1, self.y), (self.x_end + 1, self.y)}.union(
            {
                (x_n, y_n)
                for x_n in range(self.x_start - 1, self.x_end + 2)
                for y_n in [self.y - 1, self.y + 1]
            }
        )


def part_one(filename: str) -> int:
    symbol_coordinates, parts = parse_input(filename)
    return sum(
        part.value
        for part in parts
        if len(symbol_coordinates.intersection(part.neighbors)) > 0
    )


def part_two(filename: str) -> int:
    return 0


def parse_input(filename: str):
    numbers_chars = {str(ch) for ch in range(0, 10)}
    parts = set()

    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    symbol_coordinates = set(
        ch for line in lines for ch in line if ch not in numbers_chars.union({"."})
    )
    for y, line in enumerate(lines):
        for x_start, ch in enumerate(line):
            if line[x_start] in numbers_chars and (
                x_start == 0 or line[x_start - 1] not in numbers_chars
            ):
                x_end = x_start
                while line[x_end] in numbers_chars and x_end < len(line):
                    x_end += 1
                x_end -= 1
                parts.add(
                    PartNumber(
                        x_start=x_start,
                        x_end=x_end,
                        y=y,
                        value=int(line[x_start : x_end + 1]),
                    )
                )

    return symbol_coordinates, parts


if __name__ == "__main__":
    input_path = "./day_03/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
