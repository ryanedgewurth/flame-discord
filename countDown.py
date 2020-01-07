class countDown(object):
        # Define various interval units
        m = 60
        h = m * 60
        d = h * 24
        w = d * 7
        mo = w *4 #Assume 4 week months = 28 days/4 weeks
        
        ####################################################################################################
        # Initialise object with passed parameters (Number of Units, Units)
        # Some 'sensible' defaults added into constructor
        ####################################################################################################        
        def __init__(self, numbUnits = 1, unit = 'm',user = 'Username not set', name = 'Un-named timer'): 
                # We'll typecast the units just to be safe. Possibly use type hinting later on
                if numbUnits == None:
                        numbUnits = 0
                if int(numbUnits) < 0:
                        numbUnits = 0
                self.numUnits = int(numbUnits)
                self.unitType = unit
                if self.unitType == None:
                        self.unitType = 'm'
                self.name = name # Probably for future expansion
                if self.name == None:
                        self.name='Un-named timer'
                self.timerUser = user
                if self.timerUser == None:
                        self.timerUser='Username not set'

        ####################################################################################################
        # Getter for total number of 'clicks' (normally 1/1000 of a second)
        ####################################################################################################        
        def getTotalTime(self):
                return self.numUnits * self.numTicks() * 1000 
      
        ####################################################################################################
        # Getter and setter for timer name....not yet fully implemented
        ####################################################################################################        
        def setName(self, text):
                self.name = text

        def getName(self):
                return self.name
  
        ####################################################################################################
        # Getter and setter for username (implement as we approach prod)
        ####################################################################################################        
        def setUserName(self, text):
                self.timerUser = text
        def getUserName(self):
                return self.timerUser
       
        ####################################################################################################
        # Handle various unit types 
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
                        

