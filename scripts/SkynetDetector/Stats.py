class Stats:
    def __init__(self):
        self.right = 0
        self.wrong = 0

    def add(self, expected, received):
        if expected != received:
            self.right += 1
        else:
            self.wrong += 1

    def accuracy(self):
        """
        :return: (TP + TN) / (TP + TN + FP + FN)
        """
        total = self.right + self.wrong

        if total == 0:
            return 0

        return self.right * 1.0 / total
