''' usado so pro 2020.1
class Lesson:
	def __init__(self, uniqueId, group, solicit, course, entity, day,
				 hour, bld, roomType, room, vacan, matric, priori,
				 special):
		self.uniqueId = int(uniqueId)
		self.group = group
		self.solicit = solicit
		self.course = course
		self.entity = entity
		self.day = day
		self.hour = hour
		self.bld = bld
		self.roomType = roomType
		self.room = room
		self.vacan = int(vacan)
		self.matric = matric
		self.priori = int(priori)
		self.special = special

	def setRoom(self, room):
		self.room = room

'''

#- Para usar isso precisa comentar o codigo anterior, esse de cima no caso
#- precisa trocar o roomsFileName = "SIDS/Rooms.txt", lessonsFileInputName = "SIDS/Lessons.txt" dentro do Assignment.py
#- tem que tirar essa parte aqui
	#if(len(data) < dataDefaultLen):
	#	data.insert(3, 0)


class Lesson:
	def __init__(self, uniqueId, group, solicit, course, entity, day,
				 hour, bld, roomType, room, vacan, matric, priori,
				 special):
		self.uniqueId = int(uniqueId)
		self.group = group
		if(vacan == '-'):
			self.solicit = 0
		else:	
			self.solicit = solicit
		self.course = course
		self.entity = entity
		self.day = day
		self.hour = hour
		self.bld = bld
		self.roomType = roomType
		self.room = room
		if(matric == '-'):
			self.vacan = 0
		else:	
			self.vacan = int(matric)
		self.matric = vacan
		if(priori == '-'):
			self.priori = 0
		else:
			self.priori = int(priori)
		self.special = special

	def setRoom(self, room):
		self.room = room

