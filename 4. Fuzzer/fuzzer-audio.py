#!/usr/bin/python

#Fuzzer for testing rhytmbox audio player

import math
import random
import string
import subprocess
import time
import glob
import os


file_list=glob.glob('audio/*');
print "File list"
print file_list


app = "rhythmbox"


fuzz_output = "fuzzed_audio"

fuzz_factor = 43
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
		subprocess.call('mv '+ fuzz_output, ' crashedaudio/crashed-'+file_choice, shell=True)
		crashes += 1
	else:
		process.terminate()
		os.remove(fuzz_output)

print "Total crashes " + str(crashes)
print "Successful Tests " + str(num_tests - crashes)
