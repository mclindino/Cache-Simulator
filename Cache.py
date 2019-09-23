import numpy as np 
import random
import math
import os

class Cache:
	def __init__(self, nsets=256, bsize=4, assoc=1):
		self.nsets = int(nsets)
		self.bsize = int(bsize)
		self.assoc = int(assoc)
		self.size = self.nsets * self.bsize * self.assoc
		self.total_accesses = 0
		self.hits = 0
		self.misses = {'compulsory': 0, 'capacity': 0, 'conflict': 0}
		self.cache = np.zeros(shape=(nsets, assoc), dtype=int) -1

	def find_position(self, address):
		
		###Entrada em Binario
		#n_offset = math.log(self.bsize, 2)
		#n_indice = math.log(self.nsets, 2)
		#n_tag = math.log(32 - n_offset - n_indice)
		#tag = address[0:int(n_tag)-1]
		#position = address[int(n_tag):32-int(n_offset)]
		#return position, dado
		
		#Entrada de inteiros
		address = self.binToDecimal(address)
		if self.assoc == 1:
			return address % self.nsets, address
		else:
			return int(float(address) / float(self.bsize)) % self.nsets, address


	def insert(self, position, address, cache_set=None):
		if cache_set is None:
			cache_set = random.randint(0, self.assoc - 1)
		self.cache[position][cache_set] = address

	def binToDecimal(self, position):
		position = '0b' + position
		return int(position, 2)

	def get(self, address):
		test = False
		position, address = self.find_position(address)
		for cache_set in range(self.assoc):
			
			#Compulsorio
			if(self.cache[position][cache_set] == -1):
				self.insert(position, address, cache_set=cache_set)
				self.misses['compulsory'] += 1
				test = True
			#hit
			elif(self.cache[position][cache_set] == address):
				self.hits += 1
				test = True
				break
		
		if test == False:
			
			#Capacidade
			if self.nsets == 1:
				self.insert(position, address)
				self.misses['capacity'] += 1
			
			#Conflito
			else:
				self.insert(position, address)
				self.misses['conflict'] += 1
		self.total_accesses += 1

	def statistic(self):
		os.system('clear')
		print('__CACHE STATUS__')
		print('NSETS: {}\nBSIZE: {}\nASSOC: {}\n'.format(self.nsets, self.bsize, self.assoc))
		print('\n__CACHE STATISTICS___')
		print('TOTAL_ACCESSES: {}'.format(self.total_accesses))
		print('TOTAL_HITS: {}\nTAXA_HITS: {:.2f}%'.format(self.hits, float(self.hits) / float(self.total_accesses) * 100))
		print('TOTAL_MISSES: {}'.format(self.misses['compulsory'] + self.misses['capacity'] + self.misses['conflict']))
		print('TAXA_MISSES: {:.2f}%'.format((float(self.misses['compulsory']) + float(self.misses['capacity']) + float(self.misses['conflict'])) / float(self.total_accesses) * 100))
		print('MISS_COMPULSORY: {}'.format(self.misses['compulsory']))
		print('MISS_CONFLICT: {}'.format(self.misses['conflict']))
		print('MISS_CAPACITY: {}'.format(self.misses['capacity']))