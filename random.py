import random

student="xyz"

physics=random.uniform(0,100)

maths=random.uniform(0,100)

chemistry=random.uniform (0,100)

english=random.uniform(0,100)

computer_science=random.uniform(0,100)

gpa=(physics+maths+chemistry+english+computer_science)/5/10

print("student name", student)

print("maths marks{:.2f}".format(maths))

print("chemistry marks{:.2f}".format(chemistry))

print("physics marks{:.2f}".format(physics))

print("english marks{:.2f}".format(english))

print("computer_science marks{:.2f}".format(computer_science))

print("GPA is{:.2f}".format(gpa))
