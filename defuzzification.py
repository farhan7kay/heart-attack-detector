from fuzzification import *
from inference import *
import numpy as np
import math

def result_(x):
        result = ''
        if x < 1.78 :
            result = 'healthy'
        if 1 <= x <= 2.51:
            result = 'sick1'
        if 1.78 <= x < 3.25:
            result = 'sick2'
        if 1.5 <= x <= 4.5:
            result = 'sick3'
        if 3.25 <= x:
            result = 'sick4'
        return result

class defuzzify:
    def defuzzify(self, input):
        points = np.linspace(2, 4, 400)
        out = output_sick(input)
        sum1 = 0
        sum2 = 0
        
        for p in points:
            sum1 += p * out.output_sickk(p)
            sum2 += out.output_sickk(p)
            if math.isnan((sum1/sum2)):
                return 0
            else:
                return result_((sum1/sum2))