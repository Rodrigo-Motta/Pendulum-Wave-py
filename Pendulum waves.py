from math import pi, sqrt
from vpython import rate, sphere, vector
from numpy import arange, array, cos, sin, empty

g = 9.7877                                  # gravity aceleration
theta_o = 50*pi/180                         # angle
comprimento = []                            # string lenght
freq_angular = []                           # angular frequency
esfera = empty(15, sphere)
for i in range(0, 15):                      # Creating the spheres
    L = ((60/(i+51))**2)*g/(4*pi*pi)        # The lenght of the strings that determinate the angular velocity
    cor1 = (1+i/(i+i+1))/2                  # the colours of the spheres
    cor2 = 1-cor1 + i/20
    comprimento.append(L)
    w = sqrt(g/comprimento[i])              # calculating all the frequency
    freq_angular.append(w)
    esfera[i] = sphere(pos=vector(comprimento[i], 0, i/3), radius=0.1)
    esfera[i].color = vector(cor1, 1, cor2)
tmax = 2 * pi * sqrt(comprimento[0]/g)
for t in arange(0, 110, 1/60):             # loop for the movement
    rate(30)
    print(t)
    for i in range(0, 15):                 # moving all the spheres in the xy plane
        freq_angular[i] = array(freq_angular[i], float)
        theta = theta_o * cos(freq_angular[i]*t)
        X = comprimento[i]*sin(theta_o * cos(freq_angular[i]*t))
        Y = comprimento[i]*(-cos(theta_o * cos(freq_angular[i]*t)))
        esfera[i].pos = vector(X, Y, i/3)
