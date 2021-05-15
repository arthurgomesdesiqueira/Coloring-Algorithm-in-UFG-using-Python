import bisect

#criando o grafo de coloracao
#ligando todos os pedidos que tem choque de horario	
def create_graph(allLessons):
	
	for lesson in allLessons:
		lesson.connect = []
		for i, lesson2 in enumerate(allLessons):

			if(lesson.uniqueId == lesson2.uniqueId):
				continue

			if(lesson.roomType == lesson2.roomType and lesson.bld == lesson2.bld and lesson.day == lesson2.day 
			and lesson.hour == lesson2.hour):
				lesson.connect.append(i)

#pegando todas as cores(rooms) dos vizinhos 
def neighbor_colors(lesson, allLessons):

	used_colors = set()
	for viz in lesson.connect:
		if(allLessons[viz].room != -1):
			used_colors.add(allLessons[viz].room) #pega o id da sala

	return used_colors


#alocar os pedidos nas salas
def assignLessonsToRoom(lesson, used_colors, rooms, lower_bound_rooms, porcentagem_discrepancia):
	
	'''
	for room in rooms:
		if(room.bld == lesson.bld and room.roomType == lesson.roomType and room.cap >= lesson.vacan): #podemos colocar %
			
				if(room.name in used_colors): #verificando se o room já esta sendo usado pelos vizinhos
					continue
				else:
					#no codigo de coloraçao nao necessita dessa funçao, se fosse guloso precisaria
					#if(isRoomFullDayHour(lesson.day, lesson.hour) == True):

					#pode ser que eu tenha que trocar o lesson.uniqueId
					#pela posicao dentro do allLessons, no caso o indice

					room.assignClass(int(lesson.day), int(lesson.hour), lesson.uniqueId)
					lesson.setRoom(room.uniqueId)
		
	'''
	#lower_bound do c++, ele faz uma busca binaria direto pro predio em log n
	position = bisect.bisect_left(lower_bound_rooms, lesson.bld, 0, len(lower_bound_rooms))
	#print("lesson.bld: ", lesson.bld, " - position: ", position)
	for x in range(position, len(rooms)):
		room = rooms[x]
		if(room.bld == lesson.bld and room.roomType == lesson.roomType and room.cap >= porcentagem_discrepancia * lesson.vacan): #podemos colocar %
			if(room.uniqueId in used_colors): #verificando se o room já esta sendo usado pelos vizinhos
				continue
			else:
				#no codigo de coloraçao nao necessita dessa funçao, se fosse guloso precisaria
				#if(isRoomFullDayHour(lesson.day, lesson.hour) == True):

				#pode ser que eu tenha que trocar o lesson.uniqueId
				#pela posicao dentro do allLessons, no caso o indice

				room.assignClass(int(lesson.day), int(lesson.hour), lesson.uniqueId)
				lesson.setRoom(room.uniqueId)
				break

		elif(room.bld != lesson.bld):
			break

		#elif(room.bld != lesson.bld and room.roomType != lesson.roomType):
		#	break


def exemplo(lesson, used_colors, rooms, lower_bound_rooms):
	
	position = bisect.bisect_left(lower_bound_rooms, lesson.bld, 0, len(lower_bound_rooms))
	
	verificarCap = True
	verificarTipo = True
	auxRoom = rooms[len(rooms) - 1]
	for x in range(position, len(rooms)):
		room = rooms[x]			

		if(room.bld != lesson.bld):
			break

		if(room.bld == lesson.bld and room.roomType == lesson.roomType and room.cap >= 0.8*lesson.vacan): #podemos colocar %
			verificarCap = False

		if(lesson.bld == room.bld and lesson.roomType == room.roomType):
			auxRoom = room
			verificarTipo = False

	if(verificarTipo == True):
		#print("Problema com o tipo")
		#line = "lesson: bld: " + lesson.bld + " tipo: " + lesson.roomType + " cap: " + str(lesson.vacan) + " id: " + str(lesson.uniqueId)
		#print(line)

		return -1

	elif(verificarCap == True):
		'''print("Problema com capacidade")
		line = "lesson: bld: " + lesson.bld + " tipo: " + lesson.roomType + " cap: " + str(lesson.vacan) + " id: " + str(lesson.uniqueId)
		print(line)
		#se imprimir isso: room: bld: 8 tipo: 1 cap: 60, algo nao esta certo
		line = "room: bld: " + auxRoom.bld + " tipo: " + auxRoom.roomType + " cap: " + str(auxRoom.cap)
		print(line)
		'''
		if(lesson.roomType == '2'):
			return 2;

		return 1;
	

	#sao os normais, que nao conseguimos alocar
	#line = "room: bld: " + auxRoom.bld + " tipo: " + auxRoom.roomType + " cap: " + str(auxRoom.cap)
	#print(line)
	#line = "lesson: bld: " + lesson.bld + " tipo: " + lesson.roomType + " cap: " + str(lesson.vacan) + " id: " + str(lesson.uniqueId)
	#print(line)

	return 0;