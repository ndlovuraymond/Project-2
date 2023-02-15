def Equation_Solver(coefficients, constants_d):
    # Method for Forward elimination
    number = len(constants_d)
    for i in range(number - 1):
        for j in range(i + 1, number):
            try:
                factor = coefficients[j][i] / coefficients[i][i]
                coefficients[j] = [
                    x - y * factor for x, y in zip(coefficients[j], coefficients[i])
                ]
                constants_d[j] -= constants_d[i] * factor
            except:
                print("The coefficient is 0")
                exit()

    # Method for Back substitution
    solution = [0] * number
    for i in range(number - 1, -1, -1):
        try:
            solution[i] = (
                constants_d[i]
                - sum([coefficients[i][j] * solution[j] for j in range(i + 1, number)])
            ) / coefficients[i][i]

        except:
            print("The coefficient is 0")
            exit()

    return solution


# accepting user inputs
variables = int(input("Enter the number of variables in the system: "))
coefficients = []
constants = []
for i in range(variables):
    row = input(f"Eq #{i+1}: ").split()
    if len(row) != variables:
        print("Error: number of coefficients must be equal to number of variables")
        exit()
    current_row = []
    for value in row:
        cur_val = float(value)
        current_row.append(cur_val)
    coefficients.append(current_row)
    constant = float(input(f"Enter the constant d for equation {i+1}: "))
    constants.append(constant)

# Displaying the equation system
print("\nThe equation system is:")
for i in range(variables):
    equation = ""
    for j in range(variables):
        equation += f"{coefficients[i][j]}x{j+1} + "
    equation = equation[:-3] + f"= {constants[i]}"
    print(equation)

# Solving the equations
solver = Equation_Solver(coefficients, constants)

# Displaying the solution
solution = " ".join([f"x{i+1} = {x} \n" for i, x in enumerate(solver)])
print(f"\nResult is: \n {solution}")
