def pgcd(x,y):
	n = x
	m = y
	if x < y:
		x,y = y,x
	while y!=0:
		print(x,'=',y,'x',x//y,'+',x%y)
		y,x=x%y,y
		print(f'pgcd({n},{m})={x}')
pgcd(20625260,156262500)
		
		
	
