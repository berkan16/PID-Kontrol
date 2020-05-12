from pidControl import pidController
import matplotlib.pyplot as plt

def main():
   
    # PID gain değerleri
    P = 0.30
    I = 0.0001
    D = 0.00001
    
    sampleTime = 30
    desiredValue = 40
    init_error = 0
    init_value = 0

    system = lambda x : 0.1*(x**2)
    
    pid = pidController(P,I,D,init_error)
   
    pid.setSystem(system) 
    pid.setSampleTime(sampleTime) 
    pid.setDesiredValue(desiredValue)
    
    output = [init_value]
    
    for i in range(sampleTime):
        feedback = output[-1]
        pidResult = pid.pid(feedback)
        output.append(pidResult + feedback)
    
    plt.axhline(desiredValue, color = 'r', label = 'desired-value')
    plt.plot(range(sampleTime+1), output, color = 'g', marker=".", label = 'output value')
    plt.xlabel('time')
    plt.ylabel('output')
    plt.legend()
    plt.show()
    
    pid.errorReset()
    
main()
