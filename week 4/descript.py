# class Account:
#     amount = Value()
    
#     def __init__(self, commission):
#         self.commission = commission

class Value:

	def __init__(self):
		self.value = None

	def __set__(self, obj, value):
		self.value = value - value * obj.commission
	def __get__(self, obj, obj_type):
		return self.value  