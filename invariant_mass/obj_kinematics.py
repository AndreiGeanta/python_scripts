from known_particles import *

import math

class Objects:
    def __init__(self, energy, px, py, pz):
        self.energy = energy
        self.px = px
        self.py = py
        self.pz = pz

    def compute_inv_mass(*obj):
        energy = obj[0].energy+obj[1].energy
        momentum_x = obj[0].px+obj[1].px
        momentum_y  = obj[0].py+obj[1].py
        momentum_z  = obj[0].pz+obj[1].pz
        mass = energy**2-(momentum_x**2  + momentum_y**2  + momentum_z**2)
        if mass >=0:
            print("The invariant mass of the pair is: \nm = {:0.2f} GeV".format(math.sqrt(mass)))
            for particle in particles:
                if (math.sqrt(mass) >= (particle.mass_mean - particle.mass_stat_err)) and (math.sqrt(mass) <= (particle.mass_mean + particle.mass_stat_err)):
                    print("You found the {} {}.\n".format(particle.name, particle.particle_type))
        else:
            print("Particle not on-shell! \nThe particle does not obey the equations of motion. \nIt could be a virtual particle or you might have broken the laws of physics!\n")

def main():
    print("This is the module where the object kinematics is defined... ")

if __name__ == "__main__":
    main()
