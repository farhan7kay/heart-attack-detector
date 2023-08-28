from fuzzification import *
from inference import *
from defuzzification import *

chestpain_fuzzification = chestpain_fuzzification()
bloodpressure_fuzzification = bloodpressure_fuzzification()
cholesterol_fuzzification = cholesterol_fuzzification()
bloodsugar_fuzzification = bloodsugar_fuzzification()
ECG_fuzzification  = ECG_fuzzification()
heartrate_fuzzification = heartrate_fuzzification()
exercise_fuzzification = exercise_fuzzification()
oldpeak_fuzzification = oldpeak_fuzzification()
thallium_fuzzification = thallium_fuzzification()
sex_fuzzification = sex_fuzzification()
age_fuzzification = age_fuzzification()

# inferenceLogic = inference.inference()

defuzzification = defuzzify()


class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        age = age_fuzzification.fuzzy_age(int(input_dict['age']))
        chest_pain = chestpain_fuzzification.fuzzy_chestpain(int(input_dict['chest_pain']))
        blood_pressure = bloodpressure_fuzzification.fuzzy_bloodpressure(int(input_dict['blood_pressure']))
        cholesterol = cholesterol_fuzzification.fuzzy_cholesterol(int(input_dict['cholestrol']))
        blood_sugar = bloodsugar_fuzzification.fuzzy_bloodsugar(int(input_dict['blood_sugar']))
        ecg = ECG_fuzzification.fuzzy_ECG(float(input_dict['ecg']))
        heart_rate = heartrate_fuzzification.fuzzy_heartrate(int(input_dict['heart_rate']))
        exercise = exercise_fuzzification.fuzzy_exercise(int(input_dict['exercise']))
        old_peak = oldpeak_fuzzification.fuzzy_oldpeak(float(input_dict['old_peak']))
        thallium = thallium_fuzzification.calc_fuzzy_thallium(int(input_dict['thallium_scan']))
        sex = sex_fuzzification.calc_fuzzy_sex(int(input_dict['sex']))

        fuzzy_data = inference.rules(age, chest_pain, blood_pressure, cholesterol, 
                                     blood_sugar, ecg, heart_rate, exercise, old_peak, 
                                     thallium, sex)
        return defuzzification.defuzzify(fuzzy_data)