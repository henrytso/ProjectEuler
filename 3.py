class Problem3:

    def largest_prime_factor(self):
        """
        Returns the largest prime factor of 600851475143.
        """
        NUM = 600851475143
        # Prime number has exactly two unique factors: 1 and itself.
        #     2 is prime, with factors = [1,2]
        # i.e. n is prime if for each potential divisor d in [2, n - 1], n % d != 0
        # i.e. OPTIMIZING ON THIS PRINCIPLE:
        #     We only need to check potential divisors in [2, sqrt(n)]
        #     because if a potential divisor d > sqrt(n) exists, it would have been accounted for
        #     when we checked its complementary divisor in [2, sqrt(n)]
        result = -1
        for d in range(2, int(sqrt(NUM)) + 1):
            if NUM % d == 0 and self.is_prime(d):
                result = d
        return result

    def is_prime(self, n):
        if n == 1:
            return False
        for d in range(2, int(sqrt(NUM)) + 1):
            if n % d == 0:
                return False
        return True
    
    def main(self):
        print(self.largest_prime_factor())
        print(self.is_prime(1))
        print(self.is_prime(2))
        print(self.is_prime(3))
        print(self.is_prime(4))
        print(self.is_prime(5))
        print(self.is_prime(6))

if __name__ == "__main__":
    Problem3().main()
