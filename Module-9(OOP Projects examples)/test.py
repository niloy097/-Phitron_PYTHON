class Check:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

class Try(Check):
    def __init__(self) -> None:
        pass
    def get_value(self, x, y):
        