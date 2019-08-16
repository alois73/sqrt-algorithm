import sys

class squear_root():
	
	def __init__(self, n):
		self.n = n

	def perfect_root_number(self, v):
		i = 1
		tmp = 0
		while (i*i <= v):
			i += 1
			tmp = i
		tmp -= 1 
		return tmp, tmp * tmp

	def addZero(self, d):
		d = d * 100
		return d 

	def createSubNumber(self,left,add):
		return left * add

	def Closest(self,left,right):
		n = 9
		lnumber = self.addLeftnumber(left, n)
		while (lnumber * n > right):
				n -= 1
				lnumber = self.addLeftnumber(left, n)
		return n, lnumber * n

	def addLeftnumber(self, left, add):
		left = (left * 10) + add 
		return left
		
	def cift(self):
		res = []
		n = [int(d) for d in str(self.n)]
		v = n[0]
		n.pop(0)
		v = v * 10 + n[0]
		n.pop(0)
		left, sub = self.perfect_root_number(v) 
		add = left
		right = v - sub
		left += add
		res.append(add)
		for i in range(len(n)):
			if len(n) != 0:
				v = n[0]
				n.pop(0)
				v = v * 10 + n[0]
				n.pop(0)
				right = v
				add, sub = self.Closest(left, right)
				left = self.addLeftnumber(left, add)
				res.append(add)
				left += add
				right -= sub
		while (right != 0):
			if len(res) <= 12:
				right = self.addZero(right)
				add, sub = self.Closest(left, right)
				left = self.addLeftnumber(left, add)
				left += add
				right -= sub
				res.append(add)
			else:
				print(res)
				sys.exit()
		

	def tek(self):
		res = []
		n = [int(d) for d in str(self.n)]
		v = n[0]
		n.pop(0) 
		left, sub = self.perfect_root_number(v) 
		add = left
		right = v - sub
		left += add
		res.append(add)
		for i in range(len(n)):
			if len(n) != 0:
				v = n[0]
				n.pop(0)
				v = v * 10 + n[0]
				n.pop(0)
				right = v
				add, sub = self.Closest(left, right)
				left = self.addLeftnumber(left, add)
				res.append(add)
				left += add
				right -= sub
		while (right != 0):
			if len(res) <= 12:
				right = self.addZero(right)
				add, sub = self.Closest(left, right)
				left = self.addLeftnumber(left, add)
				left += add
				right -= sub
				res.append(add)
			else:
				print(res)
				sys.exit()
		
				
	def singleOdd(self):
		res = []
		v = self.n
		left, sub = self.perfect_root_number(v) 
		add = left
		right = v - sub
		left += add
		res.append(add)
		while (right != 0):
			if len(res) <= 12:
				right = self.addZero(right)
				add, sub = self.Closest(left, right)
				left = self.addLeftnumber(left, add)
				left += add
				right -= sub
				res.append(add)
			else:
				print(res)
				sys.exit()
		

	def singlePair(self):
		res = []
		n = [int(d) for d in str(self.n)]
		v = n[0]
		n.pop(0)
		v = v * 10 + n[0]
		n.pop(0)
		left, sub = self.perfect_root_number(v) 
		add = left
		right = v - sub
		left += add
		res.append(add)
		while (right != 0):
			if len(res) <= 12:
				right = self.addZero(right)
				add, sub = self.Closest(left, right)
				left = self.addLeftnumber(left, add)
				left += add
				right -= sub
				res.append(add)
			else:
				print(res)
				sys.exit()

	def run(self):
		n = self.n 
		n = [int(x) for x in str(n)]
		nl = len(n)
		if nl % 2 == 1 and nl < 3:
			self.singleOdd()
		elif nl % 2 == 1 and nl >=3:
			self.tek()
		if nl % 2 == 0 and nl == 2:		
			self.singlePair()
		elif nl % 2 == 0 and nl > 2:
			self.cift()





obj	= squear_root(63)
obj.singlePair()


