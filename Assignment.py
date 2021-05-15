import operator
from Lesson import Lesson
from Room import Room
import Coloring
from visualization import Output
import time #adicionei essa parte

# arquivos
roomsFileName = "DADOS_SIDS/2018.1.Rooms.txt"
lessonsFileInputName = "DADOS_SIDS/2018.1.Lessons.txt"
lessonsFileOutputName = "Output/Lessons.txt"
outputLessonsFileName = "Output/UnalocatedLessons.txt"

#valores constantes
dataDefaultLen = 14 #tamanho do dado Lesson
dataRoomLen = 6 #tamanho do dado Room

# Alocacao dos pedidos nas salas
def ColoringAlgorithm():
	rooms = readRoomsFromArchive()
	allLessons = readLessonsFromArchive(rooms)
	finalLessons = [] #imprimir todos os lessons alocados

	'''
	#Para executar esse codigo precisa comentar tudo do #ordenando as salas pra baixo e precisa colocar o data[9] = -1 como comentario tambem
	print("Analise da alocaçao manual: ")
	problemaCap = 0
	#problemaDiscrepancia = 0
	problemaPredio = 0
	problemaNaoAlocados = 0
	
	problemaCap1 = 0
	problemaCap09 = 0
	problemaCap08 = 0
	problemaCap07 = 0
	problemaCap06 = 0
	for lesson in allLessons:		
		if(lesson.room == "0"):
			problemaNaoAlocados += 1
			#print("lesson nao alocado - uniqueId: " + str(lesson.uniqueId) + " day: " + str(lesson.day) + " hour: " + lesson.hour + " bld: " + lesson.bld + " type: " + lesson.roomType + " cap: " + str(lesson.vacan))
		if(lesson.room != "0"):
			for room in rooms:
				if(lesson.room == room.uniqueId):
					room.assignClass(int(lesson.day), int(lesson.hour), lesson.uniqueId)
					
					if(lesson.bld == room.bld and 1 * lesson.vacan > room.cap):
						problemaCap1 += 1
					if(lesson.bld == room.bld and 0.9 * lesson.vacan > room.cap):
						problemaCap09 += 1
					if(lesson.bld == room.bld and 0.8 * lesson.vacan > room.cap):
						problemaCap08 += 1
					if(lesson.bld == room.bld and 0.7 * lesson.vacan > room.cap):
						problemaCap07 += 1
					if(lesson.bld == room.bld and 0.6 * lesson.vacan > room.cap):
						problemaCap06 += 1

					elif(lesson.bld != room.bld):
						problemaPredio += 1
						break

	linhaCap = str(problemaCap1) + " & " + str(problemaCap1) + "/" + str(problemaCap1 - problemaCap1) + " & " + str(problemaCap09) + "/" + str(problemaCap1 - problemaCap09) + " & " + str(problemaCap08) + "/" + str(problemaCap1 - problemaCap08) + " & " + str(problemaCap07) + "/" + str(problemaCap1 - problemaCap07) + " & " + str(problemaCap06) + "/" + str(problemaCap1 - problemaCap06)
	print(linhaCap)

	print("alocados: ", len(allLessons) - problemaNaoAlocados)
	print("problemaNaoAlocados: ", problemaNaoAlocados)
	print("problemaCap:", problemaCap)
	print("problemaPredio:", problemaPredio)
	print("soma dos 3: ", problemaNaoAlocados + problemaCap + problemaPredio)
	print("total de pedidos: ", len(allLessons))
	#print("problemaDiscrepancia: ", problemaDiscrepancia)	
	#Output(rooms)
	'''
	
	
	#ordenando as salas
	rooms.sort(key=lambda x: (x.bld, x.roomType, x.cap, x.name))
	
	'''
	print("ordenaçao dos rooms: ")
	for x, room in enumerate(rooms):
		print(x, room.bld, room.roomType, room.cap, room.name)
	'''

	Coloring.create_graph(allLessons)
	
	#busca binaria do predio pra ir mais rapido
	lower_bound_rooms = [room.bld for room in rooms]

	##########testes##############
	motivoCapacidade = 0
	motivoTipo = 0
	motivoNormal = 0
	motivoTipoLab = 0
	for lesson in allLessons:
		used_colors = Coloring.neighbor_colors(lesson, allLessons)
		
		Coloring.assignLessonsToRoom(lesson, used_colors, rooms, lower_bound_rooms, 1)


	for lesson in allLessons:
		
		if(lesson.room == -1):
			used_colors = Coloring.neighbor_colors(lesson, allLessons)
			
			Coloring.assignLessonsToRoom(lesson, used_colors, rooms, lower_bound_rooms, 0.8)

			#teste com os nao_alocados
			if(lesson.room == -1): #porque nao estao sendo alocados
				value = Coloring.exemplo(lesson, used_colors, rooms, lower_bound_rooms)
				if(value == -1):
					motivoTipo += 1
				if(value == 1):
					motivoCapacidade += 1
				if(value == 0):
					motivoNormal += 1				
				if(value == 2):
					motivoTipoLab += 1					

		finalLessons.append(lesson)


	#so pra colocar no overleaf	
	n_de_pedidos = len(finalLessons)
	pedidos_alocados = len(finalLessons) - (motivoTipo + motivoCapacidade + motivoNormal + motivoTipoLab)
	pedidos_nao_alocados = motivoTipo + motivoCapacidade + motivoNormal + motivoTipoLab

	linhaOverleaf = str(n_de_pedidos) + " & " + str(pedidos_alocados) + " & " + str(pedidos_nao_alocados) + " & " +  str((pedidos_alocados*100)/n_de_pedidos) 
	print(linhaOverleaf)

	print("motivoCapacidade: ", motivoCapacidade)
	print("motivoTipo: ", motivoTipo)
	print("motivoNormal: ", motivoNormal)
	print("motivoTipoLab: ", motivoTipoLab)
	print("soma dos 4 = ", motivoTipo + motivoCapacidade + motivoNormal + motivoTipoLab)

	writeAllocationToArchive(finalLessons)

	#imprimir tudo bonitinho
	#Output(rooms)


# Importante que o arquivo esteja definido como:
# ID Bld Cap Type Special Name
# Pois é acessado diretamente por índice
def readRoomsFromArchive():
	file = open(roomsFileName)
	rooms = []
	# Não precisa ler a primeira linha, apenas definições
	file.readline()
	for currentLine in file:
		data = currentLine.split()

		#verificando o tamanho
		#tem que deixar '<' porque tem alguns que o nome é grande ai acaba passando o tamanho
		if(len(data) < dataRoomLen):
			print("Room com dados faltando")
			print(data)
			continue

		# Junta o nome, caso o de cima separe.
		name = " ".join(data[5:])

		room = Room(data[0], data[1], data[2], data[3], data[4], name)
		rooms.append(room)
	
	file.close()
	return rooms


# Importante que o arquivo esteja definido como:
# ID Group Solicit Course Entity Day Hour Bld Type Room Vacan Matric Priori Special
# Pois é acessado diretamente por índice
def readLessonsFromArchive(rooms):
	file = open(lessonsFileInputName)
	lessons = []
	# Não precisa ler a primeira linha, apenas definições
	file.readline()

	##############testeee##################
	tamanhoErrado = 0

	naoAlocadosManual = 0
	for currentLine in file:
		data = currentLine.split()
		
		#testando tamanho
		if(len(data) < 14):
			#print("Esse lesson esta com tamanho errado: ", lesson.uniqueId, "tamanho: ", len(data))
			tamanhoErrado += 1

		#isso aqui é pra todos menos o 2020
		if(len(data) < dataDefaultLen):
			data.insert(3, 0)

		'''
		# Se estiver faltando um costuma ser room, adiciono ela
		if(len(data) < dataDefaultLen):
			data.insert(9, -1)
		
		
		# Se estiver faltando um costuma ser matric porque tem algumas materias que nenhum aluno se matricula
		if(len(data) < dataDefaultLen):
			data.insert(11, 0)		
		'''


		# Se o tamanho não estiver correto ainda, está mal formatado
		# logo não adiciono.
		# TODO: Adicionar logging dos pedidos que estão falhos.
		if(len(data) < dataDefaultLen):
			print("Erro no tamanho do Lesson    id: ", data[0])
			continue
		
		day = int(data[5])

		data[9] = -1
		#else:
		#	for room in rooms:
		#		if(int(room.uniqueId) == int(data[9])):
		#			room.assignClass(int(data[5]), int(data[6]), int(data[0]))

		lesson = Lesson(data[0], data[1], data[2], data[3], data[4],
				 data[5], data[6], data[7], data[8], data[9], data[10],
				 data[11], data[12], data[13])
		lessons.append(lesson)
	
	print("tamanhoErrado: ", tamanhoErrado)
	file.close()
	return lessons



#passando tudo pro arquivo
def writeAllocationToArchive(finalLessons):
	# Abre pra pegar emprestado o header
	file = open(lessonsFileInputName)
	header = file.readline()
	file.close()

	file = open(lessonsFileOutputName, "w")
	filenoAllocation = open(outputLessonsFileName, "w")	

	file.write(header)
	filenoAllocation.write(header)

	finalLessons.sort(key=operator.attrgetter('uniqueId'))
	naoAlocados = 0
	alocados = 0
	for lesson in finalLessons:
		
		memberList = [lesson.uniqueId, lesson.group, lesson.solicit,
						 lesson.course, lesson.entity, lesson.day, lesson.hour,
						 lesson.bld, lesson.roomType, lesson.room, lesson.vacan,
						 lesson.matric, lesson.priori, lesson.special, "\n"]
		line = " ".join(map(str, memberList))
		
		#coloca os nao alocados
		if (lesson.room == -1): 
			naoAlocados += 1
			filenoAllocation.write(line)
		
		#coloca os alocados
		else:
			alocados += 1
			file.write(line)
		

	print("Qtd alocada: ", alocados)
	print("Qtd nao alocada: ", naoAlocados)
	print("porcentagem de alocação: ", (alocados*100)/(alocados + naoAlocados))
	print("porcentagem de nao alocação: ", (naoAlocados*100)/(alocados + naoAlocados))
	print("N de pedidos: ", alocados + naoAlocados)


init = time.time()
ColoringAlgorithm()

fim = time.time()
print("Tempo gasto: ", fim - init)
