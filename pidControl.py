
class pidController():
    
    def __init__(self,Kp,Ki,Kd,error):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.error = error
        
    def errorReset(self):
        self.error=0  
        
    def getSampleTime(self):
        return self.sampleTime
        
    def getDesiredValue(self):
        return self.desiredValue
    
    def getSystem(self):
        return self.system
    
    # sistemin işlem süresini giriyouz
    def setSampleTime(self,sampleTime):
        self.sampleTime = sampleTime
    
    # istenilen değerimiz (değerimiz)
    def setDesiredValue(self,desiredValue):
        self.desiredValue = desiredValue
    
    def setSystem(self,system):
        self.system = system
    
    # feedback and system output
    def systemOutput(self,processOutput):
        self.output = self.system(processOutput)
        return self.output 
    
    def errorCalculate(self,feedback):
        self.error = self.desiredValue - feedback
        return self.error
    
    def pid(self,feedback):
        
        self.last_err = 0
        
        errorI = 0
        errorD = self.errorCalculate(feedback) - self.last_err / self.getSampleTime() 
        errorI += (self.getSampleTime() * (self.errorCalculate(feedback) / 2 ))
        
        P = self.Kp * self.error
        I = self.Ki * errorI
        D = self.Kd * errorD
        
        output = P + I + D
        self.last_err = self.error
        return self.systemOutput(output)
