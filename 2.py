class Problem2:
    
    def __init__(self):
        self.memo = dict()

    def even_fibonacci_sum(self):
        """
        Returns sum of all even fibonacci numbers, not exceeding 4,000,000.
        """
        # Strategy: Starting with 1,2, set n to next fib, while n < 4,000,001, and n is even, add to result
        MAX_TERM = 4000000
        i = 0
        result = 0
        while True:
            term = self.fibonacci(i)
            if term > MAX_TERM:
                break
            if term % 2 == 0:
                result += self.fibonacci(i)
            i += 1
        return result

    def fibonacci(self, i):
        if i == 0:
            return 1
        if i == 1:
            return 2
        if i not in self.memo:
            self.memo[i] = self.fibonacci(i - 2) + self.fibonacci(i - 1)
        return self.memo[i]

    def main(self):
        print(self.even_fibonacci_sum())


if __name__ == "__main__":
    Problem2().main()
