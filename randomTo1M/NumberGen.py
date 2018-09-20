import random

Number = []
for Index in range(1000000):
    Number.append(str(random.randrange(-100,101)))

with open("1Knums.txt", mode="w") as File:
    for Index in range(1000):
        File.write(Number[Index])
        File.write("\n")
    File.close()

with open("2Knums.txt", mode="w") as File:
    for Index in range(2000):
        File.write(Number[Index])
        File.write("\n")
    File.close()

with open("5Knums.txt", mode="w") as File:
    for Index in range(5000):
        File.write(Number[Index])
        File.write("\n")
    File.close()

with open("10Knums.txt", mode="w") as File:
    for Index in range(10000):
        File.write(Number[Index])
        File.write("\n")
    File.close()

with open("100Knums.txt", mode="w") as File:
    for Index in range(100000):
        File.write(Number[Index])
        File.write("\n")
    File.close()

with open("1Mnums.txt", mode="w") as File:
    for Index in range(1000000):
        File.write(Number[Index])
        File.write("\n")
    File.close()

print("files created")

