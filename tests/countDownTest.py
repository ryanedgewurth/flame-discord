#
#      Copyright (C) 2019-2020  Edgewurth

#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.

#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import unittest
#import logging
sys.path.append("../modules/")
from countDown import countDown, flameBotTimers



class  CountDownTestCase(unittest.TestCase):

    def test_countDownForFiveMinutes(self):
        units = 'm'
        timer = countDown(5, units)
        assert timer.getTotalTime() == 300

    def testZeroTime(self):
        timer = countDown(0, 'm')
        assert timer.getTotalTime() == 0

    def testNegativeTime(self):
        timer = countDown(-5, 'm')
        assert timer.getTotalTime() == 0

    def testOneHour(self):
        timer = countDown(1, 'h')
        assert timer.getTotalTime() == 3600 # = 60s x 60 m

    def testOneDay(self):
        timer = countDown(1, 'd')
        assert timer.getTotalTime() == 86400 # = h x 24

    def testOneWeek(self):
        timer = countDown(1, 'w')
        assert timer.getTotalTime() == 604800 # = d x 7

    def testOneMonth(self):
        timer = countDown(1, 'mo')
        assert timer.getTotalTime() == 2419200 # = w x 4

    def testIncorrectUnitString(self):
        timer = countDown(1, 'zz')
        assert timer.getTotalTime() == 0


    def testDefaultUserName(self):
        timer = countDown(1, 'w')
        username = 'Freddy'
        assert timer.getUserName() == 'Username not set'
        timer.setUserName(username)
        assert timer.getUserName() == username

    def testTimerName(self):
        timer = countDown(1, 'mo')
        assert timer.getName() == 'Un-named timer'
        timername = 'My Timer'
        timer.setName(timername)
        assert timer.getName() == timername

    def testNamingTimerInConstructor(self):
        timer = countDown(1, 'mo', 'Fred', 'Freds Timer')
        assert timer.getName() == 'Freds Timer'
        assert timer.getUserName() == 'Fred'

    def testPassingNullsToNamesInConstructor(self):
        timer = countDown(1, 'mo', None, None)
        assert timer.getUserName() == 'Username not set'
        assert timer.getName() == 'Un-named timer'
        timer = countDown(1, 'mo', None, 'Fred')
        assert timer.getUserName() == 'Username not set'
        assert timer.getName() == 'Fred'

    def testReminderFlag(self):
        timer = countDown(1, 'm', None, None, 1)
        assert timer.getReminder() == 1
        timer.setReminder(0)
        assert timer.getReminder() == 0


## Test writing timer out to disk - needed for multiple users - just dumping output to stdout for now.
#timer = countDown(1,'d','Test User','My perfect Timer',1)#
##print(timer.jsonOut()) # Commented out as 'eyeball'check ok - put back in for full test output
#
## The below test may seem out of order, but needed to check that we could instantiate countDown with no parameters passed to constructor
##Test with absolutely no parameters passed to check setting of all defaults
#timer=countDown()
##print(timer.jsonOut()) # Passes 'eyeball' check


##############################################################################
## Tests for timer 'stack' or array
##############################################################################
    def testTimerArray(self):
        timers = flameBotTimers('timer.fl')
        assert timers.numTimers() == 0

    def testAddTimerToArray(self):
        timers = flameBotTimers('timer.fl')
        timer = countDown(5, 'm', 'TestUser', 'TestTimer')
        
        timers.addTimer(timer) # This should also save the timer array
        assert timers.numTimers() == 1
        newTimer = flameBotTimers('timer.fl')
        assert newTimer.numTimers() == 1 # Check we can recall the single timer from file


if __name__ == '__main__':
    unittest.main()

