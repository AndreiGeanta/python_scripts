class Particle:
    def __init__(self, name, mass_mean, mass_stat_err, particle_type):
        self.name = name
        self.mass_mean = mass_mean
        self.mass_stat_err = mass_stat_err
        self.particle_type = particle_type

particle1 = Particle("Higgs", 125.7, 0.4, "boson")
particle2 = Particle("Z", 91.1876, 0.0021, "boson")
particle3 = Particle("W", 80.379, 0.012, "boson")
particle4 = Particle("charged pi", 0.13957, 0.0, "meson")
particle5 = Particle("neutral pi", 0.13497, 0.0, "meson")

particles = [particle1, particle2, particle3, particle4, particle5]


def main():
    print("This is the module where particle objects are created... ")

if __name__ == "__main__":
    main()
