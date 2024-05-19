from maths import pi
data = {
	'time' : {
		'second' : 1,
		'minute' : 60,
		'hour' : pow(60, 2),
		'day' : 24 * pow(60, 2),
		'week' : 7 * 24 * pow(60, 2),
		'month' : 30 * 24 * pow(60, 2),
		'year' : 365 * 24 * pow(60, 2),
		'decade' : 10 * 365 * 24 * pow(60, 2),
		},
	'storage-space' : {
		'bit' : 1/8,
		'nibble' : 1/2,
		'byte' : 1,
		'kilo-byte' : pow(2,10) ,
		'mega-byte' : pow(2,20) ,
		'giga-byte' : pow(2,30) ,
		'tera-byte' : pow(2,40) ,
		'peta-byte' : pow(2,50) ,
		},
	'angle' : {
		'degree' : 1,
		'radian' : pi()/180 ,
		},
	'length' : {
		'mili-metre' : pow(10,-3),
		'centi-metre' : pow(10,-2),
		'metre' : 1,
		'kilo-metre' : pow(10,3),

		'inch' : 0.0254 ,
		'foot' : 12 * 0.0254 ,
		'yard' : 3 * 12 * 0.0254 ,
		'mile' : 1760 * 3 * 12 * 0.0254 ,
		},
	}
