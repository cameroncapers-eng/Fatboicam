class Calculator:

    def addition(self, a, b):
        return a + b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def subtraction(self, a, b):
        return a - b

calc = Calculator()

add_result = calc.addition(11, 3)
multiply_result = calc.multiplication(11, 3)
divide_result = calc.division(11, 3)
subtract_result = calc.subtraction(11, 3)

print("Addition:", add_result)
print("Multiplication:", multiply_result)
print("Division:", divide_result)
print("Subtraction:", subtract_result)