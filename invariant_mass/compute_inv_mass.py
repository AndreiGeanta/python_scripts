'''
Two objects with their 4-momentum are given. The structure is as follows:
object = (E, px, py, pz)

These objects are the decay product of a particle decay.
By calculating the invariant mass of the pair, we can in fact get the invariant mass of the original particle.

The invariant mass is given by the energy-momentum equation:
m^2 = E^2 - p^2

This script computes the invariant mass of a pair of particles with a given energy and momentum.
'''

from known_particles import *
from obj_kinematics import *

#object definition
object1 = Objects(109.38, -41.85, -9.29, -100.74)
object2 = Objects(40.21, 34.10, 8.35, 19.49)

object3 = Objects(100, 89.99, 0, 0)
object4 = Objects(100.086, 88.11, 0, 0)

object5 = Objects(0, 178, 0, 0)
object6 = Objects(0, 0.1, 0, 0)

object7 = Objects(100, 80, 0, 0)
object8 = Objects(30, 22.18, 0, 0)

object9 = Objects(0.13957/2, (0.13957/2)*math.sin(10), 0, (0.13957/2)*math.cos(10))
object10 = Objects(0.13957/2, (-0.13957/2)*math.sin(10), 0, -(0.13957/2)*math.cos(10))

object11 = Objects(0.13497/2, (0.13497/2)*math.sin(20), 0, (0.13497/2)*math.cos(20))
object12 = Objects(0.13497/2, (-0.13497/2)*math.sin(20), 0, -(0.13497/2)*math.cos(20))

def main():
#compute the invariant mass for pairs of objects
    mass = Objects.compute_inv_mass(object1, object2)
    mass = Objects.compute_inv_mass(object3, object4)
    mass = Objects.compute_inv_mass(object5, object6)
    mass = Objects.compute_inv_mass(object7, object8)
    mass = Objects.compute_inv_mass(object9, object10)
    mass = Objects.compute_inv_mass(object11, object12)

if __name__ == '__main__':
    main()
