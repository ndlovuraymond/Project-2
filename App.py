print(
    "Type linear equations in augmented matrix notation: a1 a2... aN d,where a1...N are coefficients and d is constant"
)
print("Type END to finish entering equations.")
my_equation1 = input("Eq #1:")
my_equation2 = input("Eq #2:")
print("Eq #3: END")
print("You have entered the following equations.")
eq = my_equation1.split()
eq1 = my_equation2.split()
print("Eq #1:" + eq[0] + "*x1" + " + " + eq[1] + "*x2" + " = " + eq[2])
print("Eq #1:" + eq1[0] + "*x1" + " + " + eq1[1] + "*x2" + " = " + eq1[2])
