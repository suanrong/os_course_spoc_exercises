#! /usr/bin/env python

import sys
from optparse import OptionParser
import random
import math

def hfunc(index):
    if index == -1:
        return 'MISS'
    else:
        return 'HIT '

def vfunc(victim):
    if victim == -1:
        return '-'
    else:
        return str(victim)

#
# main program
#
parser = OptionParser()
parser.add_option('-a', '--addresses', default='-1',   help='a set of comma-separated pages to access; -1 means randomly generate',  action='store', type='string', dest='addresses')
parser.add_option('-f', '--pageframesize', default='3',    help='size of the physical page frame, in pages',                                  action='store', type='string', dest='pageframesize')

(options, args) = parser.parse_args()

print 'ARG addresses', options.addresses
print 'ARG pageframesize', options.pageframesize


addresses   = str(options.addresses)
pageframesize   = int(options.pageframesize)




addrList = []
addrList = addresses.split(',')

# init memory structure
count = 0
memory = []
hits = 0
miss = 0

# track reference bits for clock
ref   = {}

cdebug = False
leftStr = 'LRU'
riteStr = 'MRU'
# need to generate addresses
addrIndex = 0
for nStr in addrList:
    # first, lookup
    n = int(nStr)
    try:
        idx = memory.index(n)
        hits = hits + 1
        update = memory.remove(n)
        memory.append(n) # puts it on MRU side
    except:
        idx = -1
        miss = miss + 1

    victim = -1        
    if idx == -1:
        # miss, replace?
        # print 'BUG count, pageframesize:', count, pageframesize
        if count == pageframesize:
            victim = memory.pop(0)
        else:
            # miss, but no replacement needed (page frame not full)
            victim = -1
            count = count + 1

        # now add to memory
        memory.append(n)
        if cdebug:
            print 'LEN (a)', len(memory)
        if victim != -1:
            assert(victim not in memory)

    # after miss processing, update reference bit
    if n not in ref:
        ref[n] = 1
    else:
        ref[n] += 1
    
    if cdebug:
        print 'REF (a)', ref

    print 'Access: %d  %s %s -> %12s <- %s Replaced:%s [Hits:%d Misses:%d]' % (n, hfunc(idx), leftStr, memory, riteStr, vfunc(victim), hits, miss)
    addrIndex = addrIndex + 1
    
print ''
print 'FINALSTATS hits %d   misses %d   hitrate %.2f' % (hits, miss, (100.0*float(hits))/(float(hits)+float(miss)))
print ''

    
    
    






