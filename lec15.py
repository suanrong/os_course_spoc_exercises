#! /usr/bin/env python

import sys
from optparse import OptionParser
import random
parser = OptionParser()
parser.add_option("-s", "--seed", default=0, help="the random seed", 
                  action="store", type="int", dest="seed")
parser.add_option("-j", "--jobs", default=3, help="number of jobs in the system",
                  action="store", type="int", dest="jobs")
parser.add_option("-l", "--jlist", default="", help="instead of random jobs, provide a comma-separated list of run times",
                  action="store", type="string", dest="jlist")
parser.add_option("-m", "--maxlen", default=10, help="max length of job",
                  action="store", type="int", dest="maxlen")
parser.add_option("-p", "--policy", default="priority_inheritance", help="sched policy to use: SJF, FIFO, RR",
                  action="store", type="string", dest="policy")
parser.add_option("-q", "--quantum", help="length of time slice for RR policy", default=1, 
                  action="store", type="int", dest="quantum")
parser.add_option("-c", help="compute answers for me", action="store_true", default=True, dest="solve")

(options, args) = parser.parse_args()

print 'ARG policy', options.policy

import operator

joblist = []
prior = 0 
start_time = 1
run_time = 10
sources_use = [1]
joblist.append([prior,start_time,run_time,sources_use])


prior = 3 
start_time = 3
run_time = 10
sources_use = [1]
joblist.append([prior,start_time,run_time,sources_use])

prior = 2
start_time = 5
run_time = 10
sources_use = []
joblist.append([prior,start_time,run_time,sources_use])

for i in joblist:
    [prior,start_time,run_time,sources_use] = i
    print prior, start_time ,run_time, sources_use
    

if options.solve == True:
    print '** Solutions **\n'
                        
    if options.policy == 'priority_inheritance':
        print 'Execution trace:'
        thetime = 0
        run_id = -1
        ready_list = []
        wait_list = []
        sources_used = {}
        job_finished = 0
        while job_finished < len(joblist):
            thetime += 1
            for jobid in range(len(joblist)):
                tmp = joblist[jobid]
                if tmp[1] == thetime:
                    wait_list.append(jobid)
                for wait_id in wait_list:
                    tmp_wait = joblist[wait_id]
                    can_be_ready = True
                    for source in tmp_wait[3]:
                        if source in sources_used:
                            can_be_ready = False
                            if joblist[sources_used[source]][0]<tmp_wait[0]:
                                joblist[sources_used[source]][0] = tmp_wait[0]                    
                    if can_be_ready:
                        ready_list.append(wait_id)
                        wait_list.remove(wait_id)
            run_id = -1
            for ready_id in ready_list:
                if run_id < 0 or joblist[run_id][0] < joblist[ready_id][0]:
                    run_id = ready_id
            if run_id > -1:                    
                print '  [ time %2d ] Run job %d ,prior is %d' % (thetime, run_id, joblist[run_id][0])
                for source in joblist[run_id][3]:
                    sources_used[source] = run_id
                joblist[run_id][2] -= 1
                if joblist[run_id][2] == 0:
                    ready_list.remove(run_id)
                    for source in joblist[run_id][3]:
                        sources_used.pop(source)
                    job_finished += 1
            else:
                print '  [ time %3d ] no job' % (thetime)
else:
    print 'Compute the turnaround time, response time, and wait time for each job.'
    print 'When you are done, run this program again, with the same arguments,'
    print 'but with -c, which will thus provide you with the answers. You can use'
    print '-s <somenumber> or your own job list (-l 10,15,20 for example)'
    print 'to generate different problems for yourself.'
    print ''
