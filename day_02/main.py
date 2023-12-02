from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict
import math


class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


text_to_color = {
    "red": Color.RED,
    "green": Color.GREEN,
    "blue": Color.BLUE,
}


@dataclass
class GameData:
    game_id: int
    sets: List[Dict[Color, int]]


def part_one(filename: str) -> int:
    games = parse_input(filename)
    total_cubes = {
        Color.RED: 12,
        Color.GREEN: 13,
        Color.BLUE: 14,
    }
    id_sum = 0
    for game in games:
        game_is_possible = True
        for cube_set in game.sets:
            for color in text_to_color:
                if color in cube_set and cube_set[color] > total_cubes[color]:
                    game_is_possible = False
                    break
        if game_is_possible:
            id_sum += game.game_id
    return id_sum


def part_two(filename: str) -> int:
    games = parse_input(filename)
    return sum(
        math.prod(
            max(cube_set.get(text_to_color[color], 0) for cube_set in game.sets)
            for color in text_to_color
        )
        for game in games
    )


def parse_input(filename: str) -> List[GameData]:
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
    games = []
    for line in lines:
        parts = line.split(": ")
        game_id = int(parts[0].split(" ")[1])
        color_sets = parts[1].split("; ")

        sets = []
        for set in color_sets:
            color_count = {}
            for color_info in set.split(", "):
                count, color_text = color_info.split(" ")
                color_count[text_to_color[color_text]] = int(count)
            sets.append(color_count)

        games.append(GameData(game_id, sets))

    return games


if __name__ == "__main__":
    input_path = "./day_02/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
