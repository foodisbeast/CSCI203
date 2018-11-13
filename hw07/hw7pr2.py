'''Brian Richardson & Courtney Gutherie
Lab 7
'''
import random
import math

#Area of circle: (pi)r^2
def forPi(n):
    #Variable initialization
    r = 1.0 #radius = 1
    hits = 0 #Darts hit
    estimate = 0 #pi estimate
    for i in range(n):
        x,y = random.uniform(-r,r), random.uniform(-r,r) #Generate random x,y 
        #x^2 + y^2 = r^2
        if (x**2 + y**2) <= r**2: #Check if (x,y) distance from center is within radius
            hits += 1 
        estimate = (4*hits) / (i+1) #4*hits / throws = pi (estiamte)
        #print(x,y)
        print('Darts thrown:', i+1)
        print('Darts inside circle', hits)
        print('Pi estimate:', estimate)
    return estimate

def whilePi(error):
    #Variable initialization
    estimate = 0 #pi estimate
    thrown = 0 #Darts thrown
    hits = 0 #Darts hits
    r =  1.0 #Radius =1.0
    while(abs(math.pi - estimate) > error):
        thrown += 1
        x,y = random.uniform(-r,r), random.uniform(-r,r)
        if (x**2 + y**2) <= r**2:
            hits += 1
        estimate = (4*hits) / thrown
        print('Darts thrown:', thrown)
        print('Darts inside circle:', hits)
        print('Pi estimate:', estimate)
    return thrown
'''
Analysis
Possibility 2 Willl return a more accurate estimate for pi (in certain cases). 
    - The returned estiamte for pi, from forPi(), is the estimate with the generated data
    after 100 throws. Bbecause the throws are random, it is possible to get data that
    possesses a large error in relation to the actual value of pi. In the case with whilePi(),
    although limited to 100 estimation iterations, this function accesses the actual value of
    pi, and instead works backward from this known value to find when the data represents it
    within a given error range. Therefore, if it can be found within 100 iterations, whilePi()
    will produce an estimate faster than forPi(), this is result of whilePi() while-loop
    iteration is dependent on 1) If the calculated estimate is within the desired error range,
    and 2) if it has no more than 100 iterations
'''
    
