from enum import Enum

def from_prediction(prediction):
    if (prediction > 0):
        return Result.POSITIVE
    elif (prediction == 0):
        return Result.NEGATIVE
    else:
            return Result.INVALID
class Result(Enum):
    POSITIVE = 1.0
    NEGATIVE = 0.0
    INVALID = -1.0


    def fmt(self):
        if (self == Result.POSITIVE):
            return "Positive"
        if (self == Result.NEGATIVE):
            return "Negative"
        return "Invalid"
