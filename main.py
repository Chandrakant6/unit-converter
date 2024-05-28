import sys

from data import data

def main(category :str, value :float, initialUnit: str, finalUnit :str):
	valid = validate(category, value, initialUnit, finalUnit)
	if valid:
		return valid
	if not isinstance(data[category][initialUnit], dict):
		return converter(category, value, initialUnit, finalUnit)
	return dynamicConverter(category, value, initialUnit, finalUnit)

def converter(category :str, value :float, initialUnit: str, finalUnit :str):
	category = data[category]
	return value * category[initialUnit]/category[finalUnit]
	
def dynamicConverter(category :str, value :float, initialUnit: str, finalUnit :str): #temperature is dynamic 
	return data[category][initialUnit][finalUnit](value)

def validate(category, value, initialUnit, finalUnit):
	# category validation
	if category not in data:
		return f'Invalid category avilable categories are{data.keys()}'
		
	# value validation
	if not (isinstance(value, int) or isinstance(value, float)):
		return f'invalid value datatype avilable datatypes are int or float' 

	# unit validation
	category = data[category]
	if not ((initialUnit in category) or (finalUnit in category)):
		return f'Invalid unit avilable units are{category.keys()}'
	

if __name__ == '__main__':
	category, value, initialUnit, finalUnit = sys.argv[2:6]
	return main(category, float(value), initialUnit, finalUnit)
