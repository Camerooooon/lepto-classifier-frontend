from enum import Enum

class Result(Enum):
    POSITIVE = "Postive"
    NEGATIVE = "Negative"
    INVALID = "Invalid"


def from_result_num(result):
    if result == 0:
        return Result.NEGATIVE
    elif result == 1:
        return Result.POSITIVE
    else:
        return Result.INVALID
