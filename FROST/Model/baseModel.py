#!/usr/bin/python
class baseModel(object):
	def __init__(self, name):
		super(baseModel, self).__init__()
		self.name = name

# class model(object):
# 	validEvent = QtCore.pyqtSignal(str, str)
# 	physicalSignal = QtCore.pyqtSignal(str, str)

# 	def __init__(self, name):
# 		super(model, self).__init__()
# 		self.name = name
# 		self.parents = []
# 		self.child = []
# 		self.value = []
# 		self.physicalValue = []
# 		self.keys = []
# 		self.physicalSignal.connect(self.physicalUpdate)

# 	def addParent(self, parent):
# 		self.parent.append(parent)

# 	def addChild(self, childName, child):
# 		setattr(self, childName, child)
# 		self.child.append(getattr(self, childName))

# 	def addValue(self, valueName, value):
# 		setattr(self, valueName, value)
# 		self.value.append(getattr(self, valueName))
# 		setattr(self, 't_'+valueName, copy.deepcopy(value))
# 		self.physicalValue.append(getattr(self, 'p_'+valueName))

# 	def g(self, path):
# 		return getattr(self, path)

# 	def s(self, path, value):
# 		if self.validate(path, value):
# 			setattr(self, path, value)
# 			self.validEvent.emit(path, str(value))

# 	def validate(self, path, value):
# 		return True

# 	def physicalUpdate(self, path, value):
# 		setattr(self, 'p_'+path, value)
# 		pass