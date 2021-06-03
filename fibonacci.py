class Fibonacci:

    def __init__(self, num_of_items):

        try:
            self.num_of_items = int(num_of_items)
        except ValueError:

            raise ValueError('ValueError')

    def __iter__(self):
        self.n_fibonnacci = 0  # nth of fibonacci
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        if self.n_fibonnacci > self.num_of_items:
            raise StopIteration
        elif self.n_fibonnacci == 0:
            self.n_fibonnacci += 1
            return self.a
        elif self.n_fibonnacci == 1:
            self.n_fibonnacci += 1
            return self.b
        else:
            result = self.a + self.b
            self.a = self.b  # mutating
            self.b = result
            self.n_fibonnacci += 1
            return result
