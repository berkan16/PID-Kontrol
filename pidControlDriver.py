def main():
   
    # set PID value
    P = 2
    I = 0.001
    D = 0.5
    
    sampleTime = 30
    desiredValue = 50
    init_error = 0
    init_value = 0
    
    # set system
    system = lambda x : 0.2*x + 0.5
    
    pid = pidController(P,I,D,init_error)
   
    pid.setSystem(system) 
    pid.setSampleTime(sampleTime) 
    pid.setDesiredValue(desiredValue)
    
    # define output
    output = [init_value]
    
    # apply PID to the system
    for i in range(sampleTime):
        feedback = output[-1]
        pidResult = pid.pid(feedback)
        output.append(pidResult + feedback)
         
    # plot input and output value
    plt.axhline(desiredValue, color = 'r', label = 'desired-value')
    plt.plot(range(sampleTime+1), output, color = 'b', marker=".", label = 'output value')
    plt.xlabel('time')
    plt.ylabel('output')
    plt.legend()
    plt.show()
    
    # error reset
    pid.errorReset()
    
main()
