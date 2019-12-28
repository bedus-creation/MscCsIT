import math


class Lab04:
    def __init__(self):
        self.lists = [3, -1, 5, -8, 10, -2]
        self.maxSum = -math.inf

    def isntall(self):
        answer = ''
        for i, item in enumerate(self.lists):
            for j in range(i, len(self.lists)):
                temp = 0
                for k in range(i, j):
                    temp = temp + self.lists[k]
                    if temp > self.maxSum:
                        self.maxSum = temp
                        answer = (
                            {'start_index': i, 'end_index': k, 'sum': temp})
                        temp = 0

        print(answer)


if __name__ == "__main__":
    Lab04().isntall()
