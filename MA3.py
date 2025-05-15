""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""

import random
#import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
import numpy as np
import functools as ft
import multiprocessing as mp 

def approximate_pi(n): # Ex1
    sample = np.zeros((n, 2))


    for i in range(len(sample)):
        sample[i][0] = np.random.uniform(-1, 1)
        sample[i][1] = np.random.uniform(-1, 1)
        
    inside = 0
    

    for i in sample:
        if i[0]**2 + i[1]**2 <= 1:
            inside += 1
    
    return 4*inside/n



def sphere_volume(n, d): #Ex2, approximation
    radius = lambda x: sum(i**2 for i in x) #define a function that determines wether each point is within the spherical boundary    
    cube_vol = 2**d #This is the volume of a hypercube of side length 2 in d dimensions
    samples = [[np.random.uniform(-1, 1) for i in range (d)] for i in range(n)] # construct a list of uniformly sampled numbers
    inside = list(filter(lambda x: x <= 1, [radius(i) for i in samples])) #determine which points are within the radius and filter the others out
    
    
    
    

    return len(inside)/n*cube_vol # this is the ratio of the spheres volume to the cubes, times the volume of the cube.

def hypersphere_exact(d): #Ex2, real value
    # d is the number of dimensions of the sphere
    return np.sqrt(np.pi)**d/(m.gamma(d/2+1))


#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
    start = pc()
    with future.ProcessPoolExecutor() as ex:
        nlist = [n for i in range(np)]
        dlist = [d for i in range(np)]
        result = ex.map(sphere_volume, nlist, dlist)
        result = list(result)
        
    end = pc()
    print(f'den parallella processen tog {end-start} sekunder')
    return sum(result)/len(result)



#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    start = pc()
    value = sphere_volume_parallel1(int(n/np), d)
    end = pc()
    
    return [value, end-start]
    
 
    
def main():
#     #Ex1
#     dots = [1000, 10000, 100000]
#     for n in dots:
#         approximate_pi(n)
#     #Ex2
#     n = 100000
#     d = 2
#     sphere_volume(n,d)
#     print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")
# 
#     n = 100000
#     d = 11
#     sphere_volume(n,d)
#     print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")
# 
#     #Ex3
#     n = 100000
#     d = 11
#     start = pc()
#     for y in range (10):
#         sphere_volume(n,d)
#     stop = pc()
#     print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
#     print("What is parallel time?")
# 
#     #Ex4
#     n = 1000000
#     d = 11
#     start = pc()
#     sphere_volume(n,d)
#     stop = pc()
#     print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
#     print("What is parallel time?")
# 
#     
#     
#     start = pc()
#     resultlst = []
#     for i in range(10):
#         resultlst.append(sphere_volume(int(10e5), 11))
#     print(sum(resultlst)/len(resultlst))
#     end = pc()
#     print(round(end-start, 2))
     start = pc()
     print(sphere_volume(int(10e6), 11))
     end = pc()
     print(f'linjär metod tog', start-end, 'sekunder')
     
     start = pc()
     print(sphere_volume_parallel2(10**6,11))
     end = pc()
     
     print('den parallella metoden tog', start-end, 'sekunder')
     
if __name__ == '__main__':
    main()


