from Cache import Cache
import sys

parameters = sys.argv[1].split(':')
if((parameters[0] == '') and (parameters[1] == '') and (parameters[0] == '')):
	cache = Cache()
else:	
	cache = Cache(nsets=int(parameters[0]),bsize=int(parameters[1]),assoc=int(parameters[2]))
file = open(sys.argv[2], 'r')
in_address = file.readlines()
i = 0
for address in in_address:
	cache.get(address)
	i += 1
	if i % (len(in_address)/4) == 0:
		print('Processing...')
cache.statistic()
file.close()