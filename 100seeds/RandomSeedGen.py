import random

def GenerateSeed(FileName,seedNumber):
    random.seed(seedNumber)
    with open(FileName, mode="w") as File:
        for Index in range(100000):
            File.write(str(random.randrange(-100, 101)))
            File.write("\n")
        File.close()

for files in range(100):
    DestFileName = "file"
    DestFileName += str(files+1)
    DestFileName += ".txt"
    print("file {} created".format(files))
    GenerateSeed(DestFileName,files)
