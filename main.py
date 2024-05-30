import sys

from data import data

def main(category :str, value :float, initialUnit: str, finalUnit :str):
	
	notValid = validate(category, value, initialUnit, finalUnit)
	if notValid:
		return notValid
		
	if not isinstance(data[category][initialUnit], dict):
		return converter(category, value, initialUnit, finalUnit)
	return dynamicConverter(category, value, initialUnit, finalUnit)

def converter(category, value, initialUnit, finalUnit):
	return value * data[category][initialUnit]/data[category][finalUnit]
	
def dynamicConverter(category, value, initialUnit, finalUnit): #temperature is dynamic 
	return data[category][initialUnit][finalUnit](value)

def validate(category, value, initialUnit, finalUnit):
	if category not in data: # category validation
		return f'Invalid category avilable categories are{data.keys()}'
		
	if not (isinstance(value, int) or isinstance(value, float)): # value validation
		return f'invalid value datatype avilable datatypes are int or float'

	if not ((initialUnit in data[category]) or (finalUnit in data[category])): # unit validation
		return f'Invalid unit avilable units are{category.keys()}'

if __name__ == '__main__':
	category, value, initialUnit, finalUnit = sys.argv[2:6]
	return main(category, float(value), initialUnit, finalUnit)
