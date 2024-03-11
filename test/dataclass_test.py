#!/bin/env -S python3 -u


import math
from dataclasses import dataclass
from pretty_cli import PrettyCli


@dataclass
class MyData:
    some_int: int
    some_float: float
    some_string: str


def main():
    cli = PrettyCli()
    cli.main_title("DATACLASS TEST")

    my_data = MyData(
        some_int=42,
        some_float=math.pi,
        some_string="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    )

    cli.print("before")
    cli.print(my_data)
    cli.print("after")


if __name__ == "__main__":
    main()
