'''
BMI Calculator

Mody Mass Index Calculator

Calculation:
    BMI = (Weight in KG) / (Height in m) ^ 2

Inputs:
    weight: float
    height: float

Returns:
    BMI Value
'''

def bmi(height, weight):
    """
    Purpose:
        Function to calculate BMI.

    Calculation:
        BMI = (Weight in KG) / (Height in m) ^ 2

    :param height: Your height in m
    :param weight: Your weight in kg
    :return: Your BMI Value
    """
    if not isinstance(height, (float, int)) or not isinstance(weight, (float, int)):
        raise TypeError('Height and Weight must be floats.')

    if weight < 6 or weight > 700:
        raise ValueError('Weight must be realistic and in Kilograms')

    if height < 0.2 or height > 3.0:
        raise ValueError('Height must be between 0.2 and 3.0 meters')

    return weight / (height * height)

#test
get_height = float(input('What\'s your height in m => '))
get_weight = float(input('What\'s your weight in kg => '))
print(f'BMI: {bmi(height=get_height, weight=get_weight)}')


def target_weight(bmi, height):
    return bmi  * height * height

print(f'Target Weight: {target_weight(bmi=24, height=1.68)}')