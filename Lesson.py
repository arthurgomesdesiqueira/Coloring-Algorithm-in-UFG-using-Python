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

