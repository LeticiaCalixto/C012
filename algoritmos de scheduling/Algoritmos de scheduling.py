n = int(input ("Quantidade de processos: "))
tempoExecucao = []
tempoEntrada = []

for x in range(0, n):
    print("Processo ", x, ":")
    tempoEntrada.append(float(input("    Tempo de entrada: ")))
    tempoExecucao.append(float(input("    Tempo de execucao:")))
    
alg = input ("Escolha: \n 1 - FIFO \n 2 - RR \n ----->  ")

def fifo ():
	tEntrada = list(tempoEntrada)
	tExecucao = list(tempoExecucao)
	for i in range(0,n-1):
		if tEntrada[i]>tEntrada[i+1]:
			aux = tEntrada[i+1] 
			tEntrada[i+1] = tEntrada[i]
			tEntrada[i] = aux
			aux = tExecucao[i+1] 
			tExecucao[i+1] = tExecucao[i]
			tExecucao[i] = aux
	soma = 0
	relogio = 0
	for x in range(0,n):
		relogio += tExecucao[x] 
		soma += relogio - tEntrada[x] 
		pass
	return float(soma/n);

def rr ():
	tEntrada = list(tempoEntrada) 
	tExecucao = list(tempoExecucao) 
	relogio = 0 
	processados = [0]*n  
	entraram = [0]*n  
	fila = [] 
	soma = 0
	def entra():
		for x in range(0,n): 
			if tEntrada[x] <= relogio and entraram[x] == 0:
				
				entraram[x] = 1  
				fila.append(x)  
			pass
	entra()
	for processo in fila:
		
		falta = tExecucao[processo]-processados[processo]  
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
			soma+=relogio-tEntrada[processo] 
	return float(soma/n) 

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