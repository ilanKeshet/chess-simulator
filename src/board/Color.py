from enum import Enum, unique
from random import random
from typing import Iterable


@unique
class Color(Enum):
    BLACK = "Black"
    WHITE = "White"

    @staticmethod
    def getRandomColor() -> 'Color':
        colors = [e for e in Color]
        return random.choice(colors)

    @staticmethod
    def getOpositeColor(color: 'Color') -> 'Color':
        if color == Color.BLACK:
            return Color.WHITE
        elif color == Color.WHITE:
            return Color.BLACK
        else:
            raise Exception('None or Unexpected Color encountered')

    @staticmethod
    def getColorsByPrecedence() -> Iterable['Color']:
        return (Color.WHITE, Color.BLACK)