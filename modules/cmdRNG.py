import random
class cmdRNG:

    def runCmd(smallnum, largenum):
        # If numbers are wrong way round - don't panic just swap them.
        if (smallnum > largenum):
            swapnum=smallnum
            smallnum=largenum
            largenum=swapnum
        return random.randint(int(smallnum), int(largenum))
