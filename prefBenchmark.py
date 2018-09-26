#!/usr/bin/env python3

import alias
import sys
import time
import signal

def write_to_file(text):
    with open('/home/szczocik/Workspaces/benchmarkScript/alias/results/20180924_preferred_results.csv', 'a') as file:
        file.write(text)

def signal_handler(signum, frame):
    raise Exception("Timed out!")

print('Reading file\n')
start_r = time.time()
af = alias.read_tgf(sys.argv[1])
end_r = time.time()
print('Finished reading file\n')

signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(1200)

print('Start computing preferred extension')
start = time.time()
try:
    stable = af.get_preferred_extension()
    end = time.time()
    print('End computing preferred extension')
except Exception as e:
    end = time.time()
    stable = e
    print('exception thrown: now writing to file')
    write_to_file(sys.argv[1] + ';' + str(af.get_args_count()) + ';' + str(af.get_attacks_count()) + ';' + str(end_r - start_r) + ';' + str(end - start) + ';' + str(stable) + '\n')
    print(str(end - start) + 's: exception thrown: finished writing to file')
    sys.exit()

print('starting writing to file')
write_to_file(sys.argv[1] + ';' + str(af.get_args_count()) + ';' + str(af.get_attacks_count()) + ';' + str(end_r - start_r) + ';' + str(end - start) + ';' + str(stable) + '\n')
print('finished writing to file')