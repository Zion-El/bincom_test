from typing import Tuple

dress_colors = {
    "MONDAY": ("GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"),
    "TUESDAY": ("ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"),
    "WEDNESDAY": ("GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"),
    "THURSDAY": ("BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"),
    "FRIDAY": ("GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"),
}


def get_unique_colors():
    colors = []
    for color in dress_colors.values():
        colors.extend(color)
    return set(colors)

def get_color_frequency(color: str):
    return sum(
        list(colors).count(color)
        for colors in dress_colors.values()
    )

def get_unique_colors_frequencies() -> Tuple[str, int]:
    unique_colors = get_unique_colors()
    return [
        (color, get_color_frequency(color))
        for color in unique_colors
    ]


def to_sql():
    create_statement_statement = """
    CREATE TABLE dress_colors (
        id serial NOT NULL PRIMARY KEY,
        colors varchar NOT NULL,
        frequency int NOT NULL,
    );
    """
    insert_statment = """
    INSERT INTO dress_colors (colors, frequency)
    VALUES {}
    """.format(*get_unique_colors_frequencies())
    return create_statement_statement, insert_statment