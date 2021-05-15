
#file constantes
lessonsFileName = "Output/Lessons.txt"
buildingsFileName = "SIDS/Buildings.txt"
hoursFileName = "SIDS/Hours.txt"
reservationsFileName = "SIDS/Reservations.txt"
output = "Output/Room.txt"

diasDaSemana = {
	1: "Segunda",
	2: "Terca",
	3: "Quarta",
	4: "Quinta",
	5: "Sexta",
	6: "Sabado"	
}
tipo = {
	1: "Sala", 
	2: "Lab", 
	3: "Ateliê"
}
	

def Output(rooms):

	buildings = readBuildings()
	hours = readHours()
	reservations = readReservations()
	lessons = readLessons()

	file = open(output, "w")
		
	for room in rooms:		
		if(room.bld == '0'):
			continue
		line = "Predio: " + buildings[int(room.bld)] + "\n"
		file.write(line)
		line = "Sala: " + room.name + ", Capacidade: " + str(room.cap) + ", Tipo da Sala: " + tipo[int(room.roomType)] + "\n"
		file.write(line)
		for week in range(1, 7):
			line = diasDaSemana[week] + "\n"
			file.write(line)
			for hour in range(1,18):
				if(room.isRoomFullDayHour(week, hour) == True):
					#retornei uma lista do lessons
					#variavel = lessons[int(room.dayHour[week][hour])]
					line = hours[hour] + ": " + " Temos uma materia aqui " + "\n"
					file.write(line)
				else:
					line = hours[hour] + ": \n"
					file.write(line)
		
	file.close()

'''
def Output(rooms):

	buildings = readBuildings()
	hours = readHours()
	reservations = readReservations()
	lessons = readLessons()

	file = open(output, "w")
		
	for room in rooms:		
			
		line = "Predio: " + buildings[int(room.bld)] + "\n"
		file.write(line)
		line = "Sala: " + room.name + ", Capacidade: " + str(room.cap) + ", Tipo da Sala: " + tipo[int(room.roomType)] + "\n"
		file.write(line)
		for week in range(1, 7):
			line = diasDaSemana[week] + "\n"
			file.write(line)
			for hour in range(1,18):
				if(room.isRoomFullDayHour(week, hour) == True):
					#retornei uma lista do lessons
					variavel = lessons[int(room.dayHour[week][hour])]
					line = hours[hour] + ": " + reservations[int(variavel[1])] + "   cap: " + variavel[9] + "\n"
					file.write(line)
				else:
					line = hours[hour] + ": \n"
					file.write(line)
		
	file.close()
'''

def readLessons():
	file = open(lessonsFileName)
	file.readline()
	lessons = {}
	for currentLine in file:
		data = currentLine.split()
		lessons[int(data[0])] = [data[1], data[2], data[3], 
								data[4], data[5], data[6], 
								data[7], data[8], data[9], 
								data[10], data[11], data[12], data[13]]
		
	file.close()
	return lessons


def readBuildings():
	file = open(buildingsFileName)
	file.readline()
	buildings = {}
	for currentLine in file:
		data = currentLine.split()
		buildings[int(data[0])] = data[2]
	
	file.close()
	return buildings

def readHours():
	file = open(hoursFileName)
	file.readline()
	hours = {}
	for currentLine in file:
		data = currentLine.split()
		line = [data[1], "-", data[2]]
		hours[int(data[0])] = " ".join(line)

	file.close()
	return hours	

def readReservations():
	file = open(reservationsFileName)
	file.readline()
	reservations = {}
	for currentLine in file:
		data = currentLine.split()
		if(len(data) < 8):
			continue
		
		name = " ".join(data[7:])
		reservations[int(data[0])] = name
	
	file.close()
	return reservations	
