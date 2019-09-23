import random
import sys

file = open('addresses.txt', 'w')

#Converte o inteiro para uma string com seu valor em binario
def decimalToBinary(n):  
    return bin(n).replace("0b", "")

def generatorRandom(start, stop):
	address = int(random.randrange(start, stop))
	num = decimalToBinary(address)
	for j in range(32 - len(num)):
		num = '0' + num
	file.write(num + '\n')
#A quantidade de enderecos gerados e o argumento passado na chamada do codigo
n = sys.argv[1] 
Range = int(sys.argv[2]), int(sys.argv[3])
for i in range(int(n)):
	generatorRandom(Range[0], Range[1])
file.close()