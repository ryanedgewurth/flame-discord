class countDown(object):
        # Define various interval units
        m = 60
        h = m * 60
        d = h * 24
        w = d * 7
        mo = w *4 #Assume 4 week months = 28 days/4 weeks
        ####################################################################################################
        # Initialise object with passed parameters (Number of Units, Units)
        ####################################################################################################        
        def __init__(self, numbUnits, unit):
                if numbUnits < 0:
                        numbUnits = 0
                self.numUnits = numbUnits
                self.unitType = unit
                self.description = "This timer is un-named" # Probably for future expansion
                self.timerUser = "Username not set" # We will need to capture this in the production release
                                                    # Particularly important with multiple users wishing to 
                                                    # use. We don't want to fork n! processes, one or more per user
                                                    # I suspect some form of file holding 'active' countdowns
                                                    # will be needed that can then be 'polled' by means of a 
                                                    # cron job or similar. If so, an entry point will be needed
                                                    # to the class to run.

        ####################################################################################################
        # Getter for total number of 'clicks' (normally 1/1000 of a second)
        ####################################################################################################        
        def getTotalTime(self):
                return self.numUnits * self.numTicks() * 1000 
      
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
                if self.unitType == 'm':
                        return int(self.m) # I'm playing safe by typecasting here
                if self.unitType == 'h':
                        return int(self.h)
                if self.unitType == 'd':
                        return int(self.d)
                if self.unitType == 'w':
                        return int(self.w)
                if self.unitType == 'mo':
                        return int(self.mo)
                return 0          
                        

