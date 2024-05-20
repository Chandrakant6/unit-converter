from data import data

def main(category :str, value :float, initialUnit: str, finalUnit :str):
	if type(data[category]) is not dict:
		return convert(category, value, initialUnit, finalUnit)
	return dynamicConverter(category, value, initialUnit, finalUnit)

def converter(category :str, value :float, initialUnit: str, finalUnit :str):
	category = data[category]
	return category[initialUnit]/category[finalUnit]
	
def dynamicConverter(category :str, value :float, initialUnit: str, finalUnit :str): #temperature is dynamic 
	return data[category][initialUnit][finalUnit]
