class Problem1:

    def sum_multiples(self):
        """
        Sums multiples of 3 and 5 below 1000.
        """
        result = 0
        for n in range(1000):
            if n % 3 == 0 or n % 5 == 0:
                result += n
        return result
    
    def main(self):
        print(self.sum_multiples())
        

if __name__ == "__main__":
    Problem1().main()
