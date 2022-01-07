def fibonacci(veces):
	lista = [1,1]
	i = 1
	while i < veces:
		n = lista[-2] + lista[-1]
		lista.append(n)	
		i += 1
	return lista 
bandera = True
while bandera:
	r = fibonacci(int(input("¿Cuántos números de Fibonacci quieres? Marca 1 para salir: ")))
	if r == [1, 1]:
		break
	else:
		print(r)
