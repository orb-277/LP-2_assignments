# Define the rules
def rule1(symptoms):
    if 'fever' in symptoms and 'cough' in symptoms and 'fatigue' in symptoms:
        return 'You may have the flu.'
    return None

def rule2(symptoms):
    if 'fever' in symptoms and 'rash' in symptoms and 'headache' in symptoms:
        return 'You may have meningitis.'
    return None

def rule3(symptoms):
    if 'pain' in symptoms and 'swelling' in symptoms and 'bruising' in symptoms:
        return 'You may have a fracture.'
    return None

def rule4(symptoms):
    if 'abdominal pain' in symptoms and 'diarrhea' in symptoms and 'nausea' in symptoms:
        return 'You may have food poisoning.'
    return None

def rule5(symptoms):
    if 'shortness of breath' in symptoms and 'chest pain' in symptoms and 'dizziness' in symptoms:
        return 'You may be having a heart attack. Please seek medical attention immediately.'
    return None

# Define the expert system
# def diagnose(symptoms):
#     rules = [rule1, rule2, rule3, rule4, rule5]
#     results = []
#     for rule in rules:
#         result = rule(symptoms)
#         if result:
#             results.append(result)
#     if len(results) == 0:
#         return 'Sorry, we could not diagnose your condition.'
#     elif len(results) == 1:
#         return results[0]
#     else:
#         return 'You may have multiple conditions: ' + ', '.join(results)

# # Test the expert system



def diagonise(symptoms):
    rules = [rule1,rule2,rule3,rule4,rule5]
    results = []
    for i in rules:
        res = i(symptoms)
        if res:
            results.append(res)
    if len(results) == 0:
        return 'Damn bru'
    else:
        return 'You may have '.join(results)

symptoms = ['fever', 'rash', 'headache']
result = diagonise(symptoms)
print(result) # Output: You may have the flu.
    