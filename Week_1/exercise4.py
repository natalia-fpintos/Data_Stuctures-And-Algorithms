"""Recursion"""


class IOObject:
    def display_int_less_than(self, n):
        n -= 1
        if n > 0:
            self.display_int_less_than(n)
        print(n)

    def factorial(self, n):
        result = 1
        for t in range(1, n+1):
            result *= t
        return result

    def factorial_recursive(self, n):
        if n > 1:
            return n * self.factorial_recursive(n - 1)
        return n


if __name__ == "__main__":
    io = IOObject()
    io.display_int_less_than(20)

    print("Factorial of 4: {}".format(io.factorial(4)))
    print("Recursive Factorial of 4: {}".format(io.factorial_recursive(4)))

