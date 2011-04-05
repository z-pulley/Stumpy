#!/usr/bin/env python

# encoding and decoding base62
# based on an example here: http://stackoverflow.com/questions/1119722/base-62-conversion-in-python/1119769#1119769

class encode():
	"""
	Encode a number to Base62 using master string
		encoded_string = base62.encode(4).string
	"""
	def __init__(self,num):
		self.num = num
		self.master = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.make_encode()
	def make_encode(self):
		self.string = ""
		if (self.num == 0):
			self.string = self.master[0]
		self.build_string = []
		self.base = len(self.master)
		while self.num:
			rem = self.num % self.base
			self.num = self.num // self.base
			self.build_string.append(self.master[rem])
		self.build_string.reverse()
		self.string = ''.join(self.build_string)

class decode():
	"""
	Decode a base62 encoded string to a number
		decoded_int = base62.decode("3D").num
	"""
	def __init__(self,string):
		self.string = string	
		self.master = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.make_decode()
	def make_decode(self):
		self.base = len(self.master)
		self.string_length = len(self.string)
		self.num = 0
		self.i = 0
		for char in self.string:
			pow = (self.string_length - (self.i + 1))
			self.num += self.master.index(char) * (self.base ** pow)
			self.i += 1
