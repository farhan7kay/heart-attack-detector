import fuzzification as fz

class inference:
    def rules(age, chest_pain, blood_pressure, cholesterol, blood_sugar, ecg, heart_rate, exercise, old_peak, thallium, sex):
        file = open('rules.fcl', 'r')
        line = file.readlines()
        file.close()

        list_sick1,list_sick2,list_sick3,list_sick4,list_healthy = ([] for i in range(5))

        for i in range(len(line)):
            line[i] = line[i].replace('IF', '')
            line[i] = line[i].replace('(', '')
            line[i] = line[i].replace(')', '')
            line[i] = line[i].replace('THEN', '')
            line[i] = line[i].replace(';', '')
            line[i] = line[i].replace('\n', '')
            line[i] = line[i].split()[2:]

        if line[-1] == '':
            del line[-1]

        def append_rule(input, condition):
            key_words = ['age', 'blood_pressure', 'blood_sugar', 'cholestrol',
                         'heart_rate', 'ecg', 'old_peak', 'exercise', 
                         'thallium_scan', 'sex', 'chest_pain']
            if input == key_words[0]:       return age[condition]
            elif input == key_words[1]:     return blood_pressure[condition]
            elif input == key_words[2]:     return blood_sugar[condition]
            elif input == key_words[3]:     return cholesterol[condition]
            elif input == key_words[4]:     return heart_rate[condition]
            elif input == key_words[5]:     return ecg[condition]
            elif input == key_words[6]:     return old_peak[condition]
            elif input == key_words[7]:     return exercise[condition]
            elif input == key_words[8]:     return thallium[condition]
            elif input == key_words[9]:     return sex[condition]
            elif input == key_words[10]:    return chest_pain[condition]

        def update_list(list_num,input1, condition1, input2, condition2, phrase):
            if phrase == 'AND':
                if list_num == 1:
                    list_sick1.append(min(append_rule(input1, condition1), append_rule(input2, condition2)))
                elif list_num == 2:
                    list_sick2.append(min(append_rule(input1, condition1), append_rule(input2, condition2)))
                elif list_num == 3:
                    list_sick3.append(min(append_rule(input1, condition1), append_rule(input2, condition2)))
                elif list_num == 4:
                    list_sick4.append(min(append_rule(input1, condition1), append_rule(input2, condition2)))
                else:
                    list_healthy.append(min(append_rule(input1, condition1), append_rule(input2, condition2)))
            elif phrase == 'OR':
                if list_num == 1:
                    list_sick1.append(max(append_rule(input1, condition1), append_rule(input2, condition2)))
                elif list_num == 2:
                    list_sick2.append(max(append_rule(input1, condition1), append_rule(input2, condition2)))
                elif list_num == 3:
                    list_sick3.append(max(append_rule(input1, condition1), append_rule(input2, condition2)))
                elif list_num == 4:
                    list_sick4.append(max(append_rule(input1, condition1), append_rule(input2, condition2)))
                else:
                    list_healthy.append(max(append_rule(input1, condition1), append_rule(input2, condition2)))

        for i in range(len(line)):
            if len(line[i]) == 10:
                p1, p2 = line[i][0], line[i][2]
                q1, q2 = line[i][4], line[i][6]
                r1, r2 = line[i][7], line[i][9]
                r2 = r2.replace('sick_', '')
                if r2 != 'healthy':
                    r2 = int(r2)
                if line[i][3] == 'AND':
                    update_list(r2, p1, p2, q1, q2, 'AND')
                elif line[i][3] == 'OR':
                    update_list(r2, p1, p2, q1, q2, 'OR')
            elif len(line[i]) == 6:
                p1, p2 = line[i][0], line[i][2]
                q1, q2 = line[i][3], line[i][5]
                q2 = q2.replace('sick_', '')
                if q2 != 'healthy':
                    q2 = int(q2)
                if q2 == 1:
                    list_sick1.append(append_rule(p1, p2))
                elif q2 == 2:
                    list_sick2.append(append_rule(p1, p2))
                elif q2 == 3:
                    list_sick3.append(append_rule(p1, p2))
                elif q2 == 4:
                    list_sick4.append(append_rule(p1, p2))
                else:
                    list_healthy.append(append_rule(p1, p2))

        return dict(
            output_sick1 = max(list_sick1),
            output_sick2 = max(list_sick2),
            output_sick3 = max(list_sick3),
            output_sick4 = max(list_sick4),
            output_healthy = max(list_healthy)
        )