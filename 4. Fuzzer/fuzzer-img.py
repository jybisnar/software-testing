#!/usr/bin/python

#Fuzzer for testing shotwell photo manager

import math
import random
import string
import subprocess
import time
import glob;
import os;

file_list=glob.glob('img/*');
print "File list"
print file_list


app = "shotwell"


fuzz_output = "fuzzed_img"

fuzz_factor = 27
num_tests = 1750


crashes = 0
for i in range(num_tests):
	file_choice = random.choice(file_list)
	
	buf= bytearray(open(file_choice, 'rb').read())
	
	#5-line fuzzer from Charlie MIller's "Babysitting an Army of Monkeys"
	#---------------------------------------------------------
	num_writes = random.randrange(math.ceil((float(len(buf)) / fuzz_factor ))) +1
		
	for j in range(num_writes):
		rbyte = random.randrange(256)
		rn = random.randrange(len(buf))
		buf[rn] = "%c"%(rbyte)
		
	#----------------------------------------------------------
	
	open(fuzz_output, 'wb').write(buf)
	
	#open with fuzzed
	process = subprocess.Popen([app,fuzz_output])
	
	time.sleep(1)
	crashed=process.poll()
	
	if crashed:
		print "process crashed with input file " + file_choice
		crashes += 1
	else:
		process.terminate()
		os.remove(fuzz_output)

print "Total crashes " + str(crashes)
print "Successful tests " + str(num_tests - crashes)
