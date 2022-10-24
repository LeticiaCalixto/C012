from re import A


n = int(input ("Informe o numero de processos: "))
tmpExe = []
tmpEnt = []

for x in range(0, n):
	print ("Tempo de entrada do processo ", x, ": ")
	tmpEnt.append(float(input()))
	print ("Tempo de execução do processo ", x, ": ")
	tmpExe.append(float(input()))

def fifo ():
	entradas = list(tmpEnt)
	tempos = list(tmpExe)
	for j in range(0,n): 
		for i in range(0,n-1):
			if entradas[i]>entradas[i+1]:
				Aux = entradas[i+1] 
				entradas[i+1] = entradas[i]
				entradas[i] = Aux
				Aux = tempos[i+1] 
				tempos[i+1] = tempos[i]
				tempos[i] = Aux
	soma = 0
	relogio = 0
	for x in range(0,n):
		relogio += tempos[x] 
		soma += relogio - entradas[x] 
		pass
	return float(soma/n);

def rr ():
	entradas = list(tmpEnt) 
	tempos = list(tmpExe) 
	relogio = 0 
	processados = [0]*n  
	entraram = [0]*n  
	fila = [] 
	count = 0 
	soma = 0
	def entra():
		for x in range(0,n): 
			if entradas[x] <= relogio and entraram[x] == 0:
				
				entraram[x] = 1  
				fila.append(x)  
			pass
	entra()
	for processo in fila:
		
		falta = tempos[processo]-processados[processo]  
		if falta > quantum: 
			relogio+=quantum  
			entra() 
			processados[processo]+=quantum 
			fila.append(processo) 
			relogio+=1 
		elif falta <= quantum and falta > 0: 
			relogio+=falta 
			entra() 
			processados[processo]+=falta 
			soma+=relogio-entradas[processo] 
	return float(soma/n) 

alg = input ("Escolha: \n 1 - FIFO \n 2 - RR \n ----->  ")

while alg != 0:
	if alg == '1':
		print('entrou no if')
		print ("============ FIFO ============")
		print ("TURNAROUND MEDIO: ", fifo())
		print ("==============================")
		alg = 0
		pass
	elif alg == '2':
		quantum = float(input("Insira o valor do quantum: "))
		print ("========= ROUND ROBIN ========")
		print ("TURNAROUND MEDIO: ", rr())
		print ("==============================")
		alg = 0
		pass
	else:
		print ("Comando Inválido")
		alg = 0
		pass