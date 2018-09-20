import time
import sys

def TripletFinder(SourceFile):
    Number = []
    Length = 100000

    PreviousI = 101
    PreviousJ = 101
    PreviousK = 101

    with open(SourceFile) as File:
        for Index in range(Length):
            Line = File.readline()
            Number.append(int(Line))
        Number.sort()
        for i in range(Length-2):
            if Number[i] != PreviousI:
                j = i + 1
                k = Length - 1
                while j <= k:
                    if (PreviousJ == Number[j]) & (PreviousK == Number[k]):
                        k -= 1
                    else:
                        if Number[i] + Number[j] + Number[k] > 0:
                            k -= 1
                        elif Number[i] + Number[j] + Number[k] < 0:
                            j += 1
                        else:
                            TripletFile.write("{} {} {}\n".format(str(Number[i]),
                                str(Number[j]), str(Number[k])))
                            j += 1
                            PreviousJ = Number[j]
                            PreviousK = Number[k]
            PreviousI = Number[i]
    File.close()

start_time = time.clock()
with open("Triplets.txt", "w") as TripletFile:
    for files in range(100):
        Source = "file"
        Source += str(files+1)
        Source += ".txt"
        TripletFinder(Source)
        sys.stdout.write("\r" + str(files+1) + "%")
        sys.stdout.flush()
    TripletFile.close()
print()
print("execution time: {:.2f} seconds".format(time.clock() - start_time))