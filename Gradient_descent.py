#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import matplotlib.pyplot as plt
import numpy as np

#variables: F is of the form: F[0][0] + F[0][1]X + F[0][2]X^2 + F[1][1]XY + F[1][0]Y ... etc.
#F should only contain positive integer powers of X and Y with real coefficients. Read the 'ReadMe' file attached for more information.
#learning_coefficient is the iteration step length. It must be below 1, and is usually set as a small value.
#iterations is the number of iterations to be performed from the starting point.
#number of rounds controls the number of starting points.
#starting points are random (within the starting_range) by default but can be added manually as a list of 2-tuples.
#order should be equal to or greater than the highest power appearing in the equation form of F.
#limit is the highest value permitted before classing the gradient descent as divergent.


learning_coefficient = 0.01
iterations = 100
starting_range = 50
limit = 100
number_of_rounds = 100
order = 3
F = np.zeros((order+1)**2).reshape(order+1,order+1)
F[0][2] = 1
F[0][0] = 1
F[2][0] = 4
F[2][1] = 0.1


#Choose a random x,y point. Used for picking points to start the algorithm.
def randompoint(num):
    point = (random.randint(-num,num),random.randint(-num,num))
    return point

#Setup GradF using F. 
def findDeltaF(F,order):
    GradF = np.zeros(2*(order+1)**2).reshape(2,order+1,order+1)
    for i in range(order+1):
        for j in range(order):
            GradF[0,i,j] = F[i,j+1]*(j+1)
    for i in range(order):
        for j in range(order+1):
            GradF[1,i,j] = F[i+1,j]*(i+1)
    return GradF

#Given an x,y point, the gradient of F and the order of the equation, find the gradient at the point. (N.B. code is long because 0**0 returns an error)
def FindGradient(point,GradF,order):
    gradient = np.zeros(2)
    for i in range(2):
        if point[0] == 0 and point[1] == 0:
            gradient[i] = GradF[i,0,0]
        elif point[0] == 0:
            for j in range(order+1):
                gradient[i] += GradF[i,j,0]*(point[1]**j)
        elif point[1] == 0:
            for k in range(order+1):
                gradient[i] += GradF[i,0,k]*(point[0]**k)
        else:
            for j in range(order+1):
                for k in range(order+1):
                    gradient[i] += GradF[i,j,k]*(point[0]**k)*(point[1]**j)
    return gradient
      
#Runs the full Gradient Descent Algorithm and outputs the points and gradients at those points.
def GradientDescent(point,GradF,points_list,grads_list,order,iterations,roundnumber,learning_coefficient,limit):  
    points_list.append(point)
    gradient = FindGradient(point,GradF,order)
    for i in range(iterations):
        if max(point[0],-point[0],point[1],-point[1]) > limit:
            for j in range(i,iterations):
                if not len(points_list) - iterations*roundnumber < 2:
                    points_list[-1] = points_list[-2]
                points_list.append(points_list[-1])
                grads_list.append(gradient)
            break
        gradient = FindGradient(point,GradF,order)
        grads_list.append(gradient)
        point = point - learning_coefficient*gradient
        points_list.append(point)
    grads_list.append("N/A")
    return points_list, grads_list

#plots a point at each starting point, and draws a line following the movements made from that point.
def Plotresults(points_list,number_of_rounds):
    for i in range(number_of_rounds):
        pointsx, pointsy = [], []
        for p in points_list[(iterations+1)*i:(iterations+1)*i+iterations+1]:
            pointsx.append(p[0])
            pointsy.append(p[1])
        plt.plot(pointsx,pointsy)
        plt.plot(pointsx[0],pointsy[0],'ro')
    plt.show()

#setting up variables used by the code.
points_list, grads_list,starting_point = [],[],[]
GradF = findDeltaF(F,order)
for i in range(number_of_rounds):
    starting_point.append(randompoint(starting_range))

#maincode.
for roundnumber in range(number_of_rounds):
    point = starting_point[roundnumber]
    GradientDescent(point,GradF,points_list,grads_list,order,iterations,roundnumber,learning_coefficient,limit)
Plotresults(points_list,number_of_rounds)


# In[ ]:




