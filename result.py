from enum import Enum

class Result(Enum):
    POSITIVE = 1
    NEGATIVE = 0
    INVALID = -1

    def fmt(self):
        if (self == Result.POSITIVE):
            return "Positive"
        if (self == Result.NEGATIVE):
            return "Negative"
        return "Invalid"
