class countDown(object):
        ####################################################################################################
        # Initialise object with passed parameters (Number of Units, Units)
        ####################################################################################################        
        def __init__(self, numbUnits, unit):
                self.numUnits = numbUnits
                self.unitType = unit
                self.description = "This timer is un-named" # Probably for future expansion
                self.timerUser = "Username not set" # We wil need to capture this in the production release

        ####################################################################################################
        # Getter for total number of 'clicks' (normally 1/1000 of a second)
        ####################################################################################################        
        def getTotalTime(self):
                return self.numUnits * 60 * 1000 # Hard coded to minutes for now. (See ./tests/countDownTest.py)
      
        ####################################################################################################
        # Getter and setter for timer description....not yet fully implemented
        ####################################################################################################        
        def setDescription(self, text):
                self.description = text

        def getDescription(self, text):
                return self.description
  
        ####################################################################################################
        # Getter and setter for username (implement as we approach prod)
        ####################################################################################################        
        def setUserName(self, text):
                self.timerUser = text
        def getUserName(self):
                return self.timerUser
       
        ####################################################################################################
        # Handle various unit types - not yet implemented
        ####################################################################################################                
        def numTicks(self):
                print("in numTicks")
                if self._timeFormat == 'm':
                        return int(m)*int(self._numberOfIntervals) # I'm playing safe by typecasting here
                if self._timeFormat == 'h':
                        return int(m)*int(self._numberOfIntervals)
                if self._timeFormat == 'd':
                        return int(m)*int(self._numberOfIntervals)
                if self._timeFormat == 'w':
                        return int(w)*int(self._numberOfIntervals)
                if self._timeFormat == 'mo':
                        return int(mo)*int(self._numberOfIntervals)
                return 0          
                        

