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
def assignLessonsToRoom(lesson, used_colors, rooms, lower_bound_rooms):
	
	#lower_bound do c++, ele faz uma busca binaria direto pro predio em log n
	position = bisect.bisect_left(lower_bound_rooms, lesson.bld, 0, len(lower_bound_rooms))
	
	for x in range(position, len(rooms)):
		room = rooms[x]
		if(room.bld == lesson.bld and room.roomType == lesson.roomType and room.cap >= lesson.vacan): #podemos colocar %
			if(room.uniqueId in used_colors): #verificando se o room já esta sendo usado pelos vizinhos
				continue
			else:
				room.assignClass(int(lesson.day), int(lesson.hour), lesson.uniqueId)
				lesson.setRoom(room.uniqueId)
				break

		elif(room.bld != lesson.bld and room.roomType != lesson.roomType):
			break
