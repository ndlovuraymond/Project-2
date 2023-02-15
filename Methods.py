class Linear_Equations:
    def __init__(self) -> None:
        self.coefficients = []
        self.constants = []

    def Equation_Solver(self):
        # Method for Forward elimination
        number = len(self.constants)
        i = 0
        while i < (number - 1):
            for j in range(i + 1, number):
                try:
                    factor = self.coefficients[j][i] / self.coefficients[i][i]
                    self.coefficients[j] = [
                        x - y * factor
                        for x, y in zip(self.coefficients[j], self.coefficients[i])
                    ]
                    self.constants[j] -= self.constants[i] * factor
                except:
                    print("The coefficient is 0")
                    exit()
            i += 1

        # Method for Back substitution
        solution = [0] * number
        number_record = number - 1
        while number > -1:
            try:
                solution[i] = (
                    self.constants[i]
                    - sum(
                        [
                            self.coefficients[i][j] * solution[j]
                            for j in range(i + 1, number)
                        ]
                    )
                ) / self.coefficientscoefficients[i][i]

            except:
                print("The coefficient is 0")
                exit()
            number += -1

        return solution

    def display_values(self):
        # accepting user inputs
        inputting_value = True
        while inputting_value == True:
            try:
                variables = int(
                    input("Enter the number of variables in the equation system: ")
                )
                inputting_value = False
            except:
                print("Please enter a numerical value e.g. 5")
        coefficients = []
        constants = []
        i = 0
        while i < variables:
            row = input(f"Eq #{i+1}: ").split()
            if len(row) != variables:
                print(
                    "Error: number of coefficients must be equal to number of variables"
                )
                exit()
            current_row = []
            for value in row:
                cur_val = float(value)
                current_row.append(cur_val)
            coefficients.append(current_row)
            constant = float(input(f"Enter the constant d for equation {i+1}: "))
            constants.append(constant)
            i += 1
        self.coefficients = coefficients
        self.constants = constants
        # Displaying the equation system
        print("\nThe equation system is:")
        for i in range(variables):
            equation = ""
            for j in range(variables):
                equation += f"{int(coefficients[i][j])}x{j+1} + "
            equation = equation[:-3] + f"= {constants[i]}"
            print(equation)

        # Solving the equations
        solver = self.Equation_Solver()

        # Displaying the solution
        print("Result is")
        for i, x in enumerate(solver):
            print(f"x{i+1} = {x} \n")
