class Calculator:

    def sum(self, a, b):
        result = a + b
        return result

    def sub(self, a, b):
        result = a - b
        return result

    def mul(self, a, b):
        result = a * b
        return result

    def div(self, a, b):
        if b == 0:
            raise ArithmeticError("На ноль делить нельзя")
        result = a / b
        return result

    def pow(self, a, b=2):
        result = a ** b
        return result

    def avg(self, nums):
        if len(nums) == 0:
            return 0
        s = 0
        for num in nums:
            s = self.sum(s, num)
        le = len(nums)
        return self.div(s, le)
