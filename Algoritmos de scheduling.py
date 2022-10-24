n = int(input ("Quantidade de processos: "))
tempoExecucao = []
tempoEntrada = []

for x in range(0, n):
    print('\n')
    print("Processo ", x, ":")
    # print ("Tempo de entrada: ")
    # tempoEntrada.append(float(input()))
    tempoEntrada = float(input ("Tempo de entrada: "))
    print ("Tempo de EXECUCAO do processo ", x, ": ")
    tempoExecucao.append(float(input()))

def fifo ():
	entradas = list(tempoEntrada)
	tempos = list(tempoExecucao)
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
	entradas = list(tempoEntrada) 
	tempos = list(tempoExecucao) 
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
		print ("FIFO - FIST COME FIST SERVED")
		print ("Tempo médio: ", fifo())
		alg = 0
		break
	elif alg == '2':
		quantum = float(input("Valor do quantum: "))
		print ("RR - ROUND ROBIN")
		print ("Tempo medio: ", rr())
		alg = 0
		pass
	else:
		print ("Comando Inválido")
		alg = 0
		pass