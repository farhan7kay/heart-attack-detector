def membership_function(first, last, x):
    return (x-first)/(last-first)

class age_fuzzification:
    def __init__(self):
        pass 

    def age_young(self, age):
        if 0 < age <= 29:
            return 1
        elif 29 < age <= 38:
            return membership_function(38, 29, age)
        else:
            return 0
    
    def age_mild(self, age):
        if 33 < age <= 38:
            return membership_function(33, 38, age)
        elif 38 < age <= 45:
            return membership_function(45, 38, age)
        else:
            return 0

    def age_old(self, age):
        if 40 < age <= 48:
            return membership_function(40, 48, age)
        elif 48 < age <= 58:
            return membership_function(58, 48, age)
        else: 
            return 0

    def age_veryold(self, age):
        if 0 <= age <= 52:
            return 0
        elif 52 < age <= 60:
            return membership_function(52, 60, age)
        else:
            return 1

    def fuzzy_age(self,age):
        return dict (
            young = self.age_young(age),
            mild = self.age_mild(age),
            old = self.age_old(age),
            very_old = self.age_veryold(age)
        )

        
        

class bloodpressure_fuzzification:
    def __init__(self):
        pass

    def bloodpressure_low(self, pressure):
        if 0 <= pressure <= 111:
            return 1
        elif 111 < pressure <= 134:
            return membership_function(134, 111, pressure)
        else:
            return 0

    def bloodpressure_medium(self, pressure):
        if 127 < pressure <= 139:
            return membership_function(127, 139, pressure)
        elif 139 < pressure <= 153:
            return membership_function(153, 139, pressure)
        else:
            return 0

    def bloodpressure_high(self, pressure):
        if 142 < pressure <= 157:
            return membership_function(142, 157, pressure)
        elif 157 < pressure <= 172:
            return membership_function(172, 157, pressure)
        else:
            return 0
    
    def bloodpressure_veryhigh(self, pressure):
        if 0 <= pressure <= 154:
            return 0
        elif 154 < pressure <= 171:
            return membership_function(154, 171, pressure)
        else:
            return 1

    def fuzzy_bloodpressure(self, pressure):
        return dict (
            low = self.bloodpressure_low(pressure),
            medium = self.bloodpressure_medium(pressure),
            high = self.bloodpressure_high(pressure),
            very_high = self.bloodpressure_veryhigh(pressure)
        )


class bloodsugar_fuzzification:
    def __init__(self):
        pass

    def bloodsugar_veryhigh(self, sugar):
        if 0 <= sugar <= 105:
            return 0
        elif 105 < sugar <= 120:
            return membership_function(105, 120, sugar)
        else:
            return 1

    def fuzzy_bloodsugar(self,sugar):
        return dict (
           true = self.bloodsugar_veryhigh(sugar),
           false = 1 - self.bloodsugar_veryhigh(sugar)
        )


class cholesterol_fuzzification:
    def __init__(self):
        pass
    
    def cholesterol_low(self, cholesterol):
        if 0 <= cholesterol <= 151:
            return 1
        elif 151 < cholesterol <= 197:
            return membership_function(197, 151, cholesterol)
        else:
            return 0

    def cholesterol_medium(self, cholesterol):
        if 188 < cholesterol <= 215:
            return membership_function(188, 215, cholesterol)
        elif 215 < cholesterol <= 250:
            return membership_function(250, 215, cholesterol)
        else:
            return 0

    def cholesterol_high(self, cholesterol):
        if 217 < cholesterol <= 263:
            return membership_function(217, 263, cholesterol)
        elif 263 < cholesterol <= 307:
            return membership_function(307, 263, cholesterol)
        else:
            return 0
    
    def cholesterol_veryhigh(self, cholesterol):
        if 0 <= cholesterol <= 281:
            return 0
        elif 281 < cholesterol <= 347:
            return membership_function(281, 347, cholesterol)
        else:
            return 1

    def fuzzy_cholesterol(self, cholesterol):
        return dict (
            low = self.cholesterol_low(cholesterol),
            medium = self.cholesterol_medium(cholesterol),
            high = self.cholesterol_high(cholesterol),
            very_high = self.cholesterol_veryhigh(cholesterol)
        )


class heartrate_fuzzification:
    def __init__(self):
        pass

    def heartrate_low(self, heartrate):
        if 0 <= heartrate <= 100:
            return 1
        elif 100 < heartrate <= 141:
            return membership_function(141, 100, heartrate)
        else :
            return 0

    def heartrate_medium(self, heartrate):
        if 111 < heartrate <= 152:
            return membership_function(111, 152, heartrate)
        elif 152 < heartrate <= 194:
            return membership_function(194, 152, heartrate)
        else:
            return 0

    def heartrate_high(self, heartrate):
        if 0 <= heartrate <= 152:
            return 0
        elif 152 < heartrate <= 210:
            return membership_function(152, 210, heartrate)
        else:
            return 1

    def fuzzy_heartrate(self, heartrate):
        return dict (
            low = self.heartrate_low(heartrate),
            medium = self.heartrate_medium(heartrate),
            high = self.heartrate_high(heartrate)
        )


class ECG_fuzzification:
    def __init__(self):
        pass

    def ECG_normal(self, ECG):
        if -0.5 <= ECG <= 0:
            return 1
        elif 0 <= ECG <= 0.4:
            return membership_function(0.4, 0, ECG)
        else:
            return 0

    def ECG_abnormal(self, ECG):
        if 0.2 <= ECG <= 1:
            return membership_function(0.2, 1, ECG)
        elif 1 < ECG <= 1.8:
            return membership_function(1.8, 1, ECG)
        else:
            return 0

    def ECG_hypertrophy(self, ECG):
        if -0.5 <= ECG <= 1.4:
            return 0
        elif 1.4 < ECG <= 1.9:
            return membership_function(1.4, 1.9, ECG)
        else:
            return 1

    def fuzzy_ECG(self,ECG):
        return dict (
            normal = self.ECG_normal(ECG),
            abnormal = self.ECG_abnormal(ECG),
            hypertrophy = self.ECG_hypertrophy(ECG),
        )


class oldpeak_fuzzification:
    def __init__(self):
        pass

    def oldpeak_low(self, oldpeak):
        if 0 <= oldpeak <= 1:
            return 1
        elif 1 < oldpeak <= 2:
            return membership_function(2, 1, oldpeak)
        else:
            return 0

    def oldpeak_risk(self, oldpeak):
        if 1.5 < oldpeak <= 2.8:
            return membership_function(1.5, 2.8)
        elif 2.8 < oldpeak <= 4.2:
            return membership_function(4.2, 2.8)
        else:
            return 0

    def oldpeak_terrible(self, oldpeak):
        if 0 <= oldpeak <= 2.5:
            return 0
        elif 2.5 < oldpeak <= 4:
            return membership_function(2.5, 4, oldpeak)
        else:
            return 1

    def fuzzy_oldpeak(self,oldpeak):
        return dict (
            low = self.oldpeak_low(oldpeak),
            risk = self.oldpeak_risk(oldpeak),
            terrible = self.oldpeak_terrible(oldpeak),
        )

    
class chestpain_fuzzification:
    def __init__(self):
        pass

    def typical_angina(self, chestpain):
        if chestpain == 1 :
            return 1
        else:
            return  0

    def atypical_angina(self, chestpain):
        if chestpain == 2 :
            return 1
        else:
            return  0

    def non_anginal(self, chestpain):
        if chestpain == 3 :
            return 1
        else:
            return  0

    def asymptomatic(self, chestpain):
        if chestpain == 4 :
            return 1
        else:
            return  0

    def fuzzy_chestpain(self, chestpain):
        return dict(
            typical_anginal = self.typical_angina(chestpain),
            atypical_anginal = self.atypical_angina(chestpain),
            non_aginal_pain = self.non_anginal(chestpain),
            asymptomatic = self.asymptomatic(chestpain)
        )


class exercise_fuzzification:
    def __init__(self):
        pass

    def true(self, exercise):
        if exercise == 1:
            return 1
        else: 
            return 0

    def false(self, exercise):
        if exercise == 0:
            return 1
        else: 
            return 0

    def fuzzy_exercise(self, exercise):
        return dict(
            true = self.true(exercise),
            false = self.false(exercise)
        )


class thallium_fuzzification:
    def __init__(self):
        pass

    def normal(self, thallium):
        if thallium == 3 :
            return 1
        else: 
            return 0

    def medium(self, thallium):
        if thallium == 6 :
            return 1
        else: 
            return 0

    def high(self, thallium):
        if thallium == 7 :
            return 1
        else: 
            return 0

    def calc_fuzzy_thallium(self, thallium):
       return dict(
           normal = self.normal(thallium),
           medium = self.medium(thallium),
           high = self.high(thallium)
       )


class sex_fuzzification:
    def __init__(self):
        pass

    def male(self, sex):
        if sex == 0:
            return 1
        else: 
            return 0

    def female(self, sex):
        if sex == 1:
            return 1
        else: 
            return 0

    def calc_fuzzy_sex(self, sex):
        return dict(
            male = self.male(sex),
            female = self.female(sex)
        )

class output_sick:
    def __init__(self, x):
        self.x = x

    def output_healthy(self, output):
        alpha = self.x['output_healthy']
        if alpha == 0:
            return 0
        if 0 <= output <= 0.25:
            return alpha
        elif 0.25 < output <= 1:
            return min(alpha, membership_function(1, 0.25, output))
        else:
            return 0

    def output_sick1(self, output):
        alpha = self.x['output_sick1']
        if alpha == 0:
            return 0
        if 0 <= output <= 1:
            return min(alpha, membership_function(0, 1, output))
        elif 1 < output <= 2:
            return min(alpha, membership_function(2, 1, output))
        else:
            return 0

    def output_sick2(self, output):
        alpha = self.x['output_sick2']
        if alpha == 0:
            return 0
        if 1 <= output <= 2:
            return min(alpha, membership_function(1, 2, output))
        elif 2 < output <= 3:
            return min(alpha, membership_function(3, 2, output))
        else:
            return 0

    def output_sick3(self, output):
        alpha = self.x['output_sick3']
        if alpha == 0:
            return 0
        if 2 <= output <= 3:
            return min(alpha, membership_function(2, 3, output))
        elif 3 < output <= 4:
            return min(alpha, membership_function(4, 3, output))
        else:
            return 0

    def output_sick4(self, output):
        alpha = self.x['output_sick4']
        if alpha == 0:
            return 0
        if 0 <= output <= 3:
            return alpha
        elif 3 < output <= 3.75:
            return min(alpha, membership_function(3, 3,75))
        else:
            return 1

    def output_sickk(self, output):
        return max(self.output_sick1(output), 
                   self.output_sick2(output), 
                   self.output_sick3(output), 
                   self.output_sick4(output), 
                   self.output_healthy(output))