# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 15:32:55 2014

@author: cnovak
"""

import subprocess
import parse_result as pr
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt



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


def goal_fun(R):
    point = {}
    point['Rval'] = R
    point ['Cval'] = 10e-9
    
    create_NetList('rc_ac.net', point)
    runSim()
    
    data = pr.parse_file('sim_result.dat')
    
    x = data['acfrequency']
    y = np.abs(data['out.v'])
    
    freq = minus3dB(x, y)
    return abs(freq - 10000.0)


optval = opt.minimize_scalar(goal_fun, bounds=(100, 10000), method='bounded')
print optval

