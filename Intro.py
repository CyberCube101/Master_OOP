import statistics



class NumberList(list):
    def __init__(self, *numbers):
        for number in numbers:
            if not isinstance(number, (int, float)):
                raise TypeError('Expecting numbers')
        super().__init__(numbers)

    @property
    def mean(self):
        return statistics.mean(self)

    @property
    def length(self):
        return len(self)


fibo = NumberList(1, 1, 2, 3, 5,'a')

for num in fibo:
    print(num)