"""Jacob Finger"""

nameTrue = False
while not nameTrue:
    name = input("Please enter your name\n>>> ").strip(' ')

    if name == '':
        print("Please fill in the field")
    else:
        nameTrue = True

for i in range(len(name)):

    if (i % 2) == 1:
        "blah"
    else:
        print('\r '.join(name[i]), end="")

