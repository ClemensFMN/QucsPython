# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:19:17 2014

@author: novakc
"""

import subprocess
import parse_result as pr
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt


from string import Template


def minus3dB(x, y):
    for (ind, xval) in enumerate(x):
        if y[ind] < 0.71:
            return x[ind]


def create_NetList(templ_filename, values):

    templ_file = open(templ_filename, 'r')
    templ = Template(templ_file.read())
    netlist = templ.substitute(values)

    f = open('temp.net', 'w')
    f.write(netlist)
    f.close()
    



def runSim():
    netfile = open('temp.net', 'r')
    outfile = open('sim_result.dat', 'w')
        

    process = subprocess.Popen('qucsator', stdin=netfile, stdout=outfile)
    process.wait()

    netfile.close()
    outfile.close()
    

def testOneRun():
    point = {}
    point['Rval'] = 1e3 + 100 * rnd.randn()
    point ['Cval'] = 10e-9

    print point

    templ_filename = 'rc_ac.net'

    create_NetList(templ_filename, point)
    runSim()

    data = pr.parse_file('sim_result.dat')

    x = data['acfrequency']
    y = np.abs(data['out.v'])


    plt.loglog(x, y, '-rx')
    plt.grid()
    plt.show()



# testOneRun()



N = 500

templ_filename = 'rc_ac.net'

freq_array = []

for i in range(N):

    point = {}
    point['Rval'] = 1e3 + 100 * rnd.randn()
    point ['Cval'] = 10e-9

    create_NetList(templ_filename, point)
    runSim()

    data = pr.parse_file('sim_result.dat')

    x = data['acfrequency']
    y = np.abs(data['out.v'])

    freq = minus3dB(x, y)
    print freq

    freq_array.append(freq)


print freq_array



plt.hist(freq_array, 10)
plt.grid()


plt.show()


