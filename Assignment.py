import operator
from Lesson import Lesson
from Room import Room
import Coloring
from visualization import Output
import time #adicionei essa parte

# arquivos
roomsFileName = "DADOS_SIDS/2019.1.Rooms.txt" #esses dados nao estão no github porque sao confidenciais
lessonsFileInputName = "DADOS_SIDS/2019.1.Lessons.txt" #esses dados nao estão no github porque sao confidenciais
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

	#ordenando as salas
	rooms.sort(key=lambda x: (x.bld, x.roomType, x.cap, x.name))
	

	Coloring.create_graph(allLessons)
	
	for lesson in allLessons:
		used_colors = Coloring.neighbor_colors(lesson, allLessons)
		
		Coloring.assignRoomToLesson(lesson, used_colors, rooms, 1)

	for lesson in allLessons:
		
		if(lesson.room == -1):
			used_colors = Coloring.neighbor_colors(lesson, allLessons)
			
			Coloring.assignRoomToLesson(lesson, used_colors, rooms, 0.8)
	
		finalLessons.append(lesson)

		
	writeAllocationToArchive(finalLessons)

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

	for currentLine in file:
		data = currentLine.split()
		
		#testando tamanho
		if(len(data) < 14):
			tamanhoErrado += 1

		#isso aqui é pra todos menos o 2020
		if(len(data) < dataDefaultLen):
			data.insert(3, 0)

		# Se o tamanho não estiver correto ainda, está mal formatado
		# logo não adiciono.
		# TODO: Adicionar logging dos pedidos que estão falhos.
		if(len(data) < dataDefaultLen):
			print("Erro no tamanho do Lesson    id: ", data[0])
			continue
		
		day = int(data[5])

		data[9] = -1

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
