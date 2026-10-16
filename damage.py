from enum import Enum

class DamageType(Enum):
	MAGIC = 1
	PHYSIC = 2
	TRUE = 3


class DamageSourceType(Enum):
	AUTO_ATTACK = 1
	SPELL = 2
	ITEM = 3

class Damage:
	def __init__(self, damage_type, damage_source_type, damage_source, damage_amount):
		self.damage_type = damage_type
		self.damage_source = damage_source
		self.damage_source_type = damage_source_type
		self.damage_amount = damage_amount