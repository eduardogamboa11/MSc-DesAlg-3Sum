import time

def TripletFinder(SourceFile, DestFile, Length):
    start_time = time.clock()
    Number = []
    PreviousI = 101
    PreviousJ = 101
    PreviousK = 101

    print("searching for triplets in {}".format(SourceFile))

    with open(SourceFile) as File:
        for Index in range(Length):
            line = File.readline()
            Number.append(int(line))
        Number.sort()
        with open(DestFile, "w") as TripletFile:
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
        TripletFile.close()
    File.close()
    print("execution time for file {}: {:.2f} seconds".format(DestFile,time.clock() - start_time))

TripletFinder("1Knums.txt","1Ktriplets.txt", 1000)
TripletFinder("2Knums.txt","2Ktriplets.txt", 2000)
TripletFinder("5Knums.txt","5Ktriplets.txt", 5000)
TripletFinder("10Knums.txt","10Ktriplets.txt", 10000)
TripletFinder("100Knums.txt","100Ktriplets.txt", 100000)
TripletFinder("1Mnums.txt","1Mtriplets.txt", 1000000)

