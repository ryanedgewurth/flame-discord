#############################################################################################################################
# Very simple test framework that will exercise various functions within our code. Will only produce output on failure.
#############################################################################################################################

# Set up directory structure - we need to do this because our source code is in the parent directory of this one.
import sys
sys.path.append("../")


# Unit under test
from countDown import countDown

# We're going to use a test-driven development methodolgy, so our tests should reflect what we want the program to do.

# We want to be able to assign a set number of time-period (of a given unit [m h d w mo]) after which the countdown will trigger an alarm....
units = 'm' # lets start with something simple - minutes (we can hard-code the 6000 'ticks' initially)
timer = countDown(5,units)
if timer.getTotalTime() <> 300000: # 60 * 5 * 1000 = 300000
    print(timer.getTotalTime())
    print("Failed in asserting 6000 minutes == 300000 'ticks'")

# Let's stick to minutes, so we can test for example a zero input in terms of units (should return 0 - simple multiplication)
timer = countDown(0,units)
if timer.getTotalTime() <> 0: # Anything multiplied by zero is always zero
    print("Failed in asserting zero units will always give a zero time")
    
# What about a negative value - should we raise an exception? How else should we deal? Assume -ve = zero for our purposes
timer=countDown(-5,units)
if timer.getTotalTime() <> 0: # As per above - set to zero to ignore
    print("Failed handling a negative amount of minutes")
    
    
    
    
# Last line to signal completion of test
print("Tests completed")