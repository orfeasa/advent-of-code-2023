import math
from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class PartNumber:
    x_start: int
    x_end: int
    y: int
    value: int

    @property
    def neighbors(self) -> set[tuple[int, int]]:
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
        if len(set(symbol_coordinates).intersection(part.neighbors)) > 0
    )


def part_two(filename: str) -> int:
    symbol_coordinates, parts = parse_input(filename)
    gear_to_parts = {
        (x, y): {part for part in parts if (x, y) in part.neighbors}
        for (x, y), ch in symbol_coordinates.items()
        if ch == "*"
    }
    return sum(
        math.prod(part.value for part in gear_parts)
        for gear_parts in gear_to_parts.values()
        if len(gear_parts) == 2
    )


def parse_input(
    filename: str,
) -> tuple[set[tuple[int, int]], dict[tuple[int, int], str]]:
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    numbers_chars = {str(ch) for ch in range(0, 10)}
    symbol_coordinates = {
        (x, y): ch
        for y, line in enumerate(lines)
        for x, ch in enumerate(line)
        if ch not in numbers_chars.union({"."})
    }
    parts = set()
    for y, line in enumerate(lines):
        x = 0
        while x < len(line):
            if line[x] in numbers_chars:
                x_start = x
                while x + 1 < len(line) and line[x + 1] in numbers_chars:
                    x += 1
                parts.add(
                    PartNumber(
                        x_start=x_start,
                        x_end=x,
                        y=y,
                        value=int(line[x_start : x + 1]),
                    )
                )
            x += 1

    return symbol_coordinates, parts


if __name__ == "__main__":
    input_path = "./day_03/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
