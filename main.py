import sys

from data import data

def main(category :str, value :float, initialUnit: str, finalUnit :str):
	if category not in data:
		return f'Invalid category avilable categories are{data.keys}'
	elif not isinstance(variable, dict):
		return convert(category, value, initialUnit, finalUnit)
	return dynamicConverter(category, value, initialUnit, finalUnit)

def converter(category :str, value :float, initialUnit: str, finalUnit :str):
	category = data[category]
	return value * category[initialUnit]/category[finalUnit]
	
def dynamicConverter(category :str, value :float, initialUnit: str, finalUnit :str): #temperature is dynamic 
	return data[category][initialUnit][finalUnit](value)

if __name__ == '__main__':
	category, value, initialUnit, finalUnit = sys.argv[2:]
	return main(category, value, initialUnit, finalUnit)
