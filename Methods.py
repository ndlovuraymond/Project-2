# giving the user instructions
print(
    "Type linear equations in augmented matrix notation: a1 a2....aN d, \n         where a1...N are coefficients and d is constant"
)
print("Type END to finish entering equations")
inputting_data = True
equations = []
count = 1
constants = []
variables = 0
# accepting user inputs for the equations
while inputting_data:
    cur_eq = input(f"Eq #{count}:")
    constant = ""
    if count == 1:
        variables = len(cur_eq.split())
    if cur_eq.upper() == "END":
        inputting_data = False
        break
    if len(cur_eq.split()) != (variables) and cur_eq.upper() != "END":
        print("Error, the number of variables entered is incorrect")
        exit()
    values = cur_eq.split()
    eq_values = []
    if cur_eq != "END":
        try:
            for value in range(0, len(values) - 1):
                value = float(values[value])
                eq_values.append(value)
            equations.append(eq_values)
            constant = float(values[len(values) - 1])
            constants.append(constant)
        except:
            print("Please enter data correctly.")
            continue
    count += 1

# displaying the equations
for equation in range(1, len(equations) + 1):
    string = f"Eq #{equation}"
    cur_eq = equations[equation - 1]
    for value in range(0, len(cur_eq)):
        if value == 0:
            string += f" {int(cur_eq[value])}*x{value+1} "
        elif value != 0:
            if int(cur_eq[value]) >= 0:
                string += "+"
                string += f" {int(cur_eq[value])}*x{value+1} "
            elif int(cur_eq[value]) < 0:
                string += "-"
                string += f" {int(cur_eq[value])}*x{value+1} "
    string += f"= {constants[equation-1]}"
    print(string)

# method for forward elimination and backward elimination
def equation_solver(cur_constants, cur_equations):
    # forward elimination
    number = len(cur_constants)
    i = 0
    while i < (number - 1):
        j = i + 1
        while j < number:
            try:
                factor = cur_equations[j][i] / cur_equations[i][i]
                cur_equations[j] = [
                    x - y * factor for x, y in zip(cur_equations[j], cur_equations[i])
                ]
                cur_constants[j] -= cur_constants[i] * factor
            except:
                print("The coefficient is 0")
                exit()
            j += 1
        i += 1

        # Back substitution
        answers = [0] * number
        i = number - 1
        while i > -1:
            try:
                list = []
                for equation in range(i + 1, number):
                    value = cur_equations[i][equation] * answers[equation]
                    list.append(value)
                answers[i] = (cur_constants[i] - sum(list)) / cur_equations[i][i]
            except:
                print("The coefficient is 0")
                exit()
            i -= 1

        return answers


answers = equation_solver(constants, equations)
# showing results
print("\nResult is: ")
i = 1
for answer in answers:
    print(f"x{i} = {answer}")
    i += 1
