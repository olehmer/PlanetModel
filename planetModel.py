import numpy as np
from math import pi, log, exp, sin, cos
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Panel:
    """
    The Panel object will store the coordinates of each panel on the planet, in
    spherical coordinates. 
    """

    def __init__(self, start_phi, end_phi, start_theta, end_theta):
        self.start_phi = start_phi
        self.start_theta = start_theta
        self.end_phi = end_phi
        self.end_theta = end_theta

    def set_albedo(self, albedo):
        """
        Set the albedo of the panel. The passed in albedo array should be 
        broken into wavelength bands.
        """
        self.albedo = [] #TODO: implement this later

    def get_cartesian_coordinates(self,planet_radius):
        """
        Return the x,y,z coordinates of the panel.
        """

        x0 = planet_radius*sin(self.start_phi)*cos(self.start_theta)
        y0 = planet_radius*sin(self.start_phi)*sin(self.start_theta)
        z0 = planet_radius*cos(self.start_phi)

        x1 = planet_radius*sin(self.start_phi)*cos(self.end_theta)
        y1 = planet_radius*sin(self.start_phi)*sin(self.end_theta)
        z1 = planet_radius*cos(self.start_phi)

        x2 = planet_radius*sin(self.end_phi)*cos(self.start_theta)
        y2 = planet_radius*sin(self.end_phi)*sin(self.start_theta)
        z2 = planet_radius*cos(self.end_phi)

        x3 = planet_radius*sin(self.end_phi)*cos(self.end_theta)
        y3 = planet_radius*sin(self.end_phi)*sin(self.end_theta)
        z3 = planet_radius*cos(self.end_phi)

        return [x0,x1,x2,x3], [y0,y1,y2,y3], [z0,z1,z2,z3]

class Planet:
    """
    Create a planet made out of flat panels. 
    """

    def __init__(self, radius, resolution):
        """
        Initialize the planet.

        Inputs:
        radius - the planet radius [m]
        resolution - the number of flat panels for the planet.
        """

        self.radius = radius
        self.resolution = resolution 

        self.generate_panels()


    def generate_panels(self):
        """
        Generate the panels of the planet
        """

        self.panels = []

        phi_steps = np.linspace(0, pi, self.resolution)
        theta_steps = np.linspace(0, 2.0*pi, self.resolution)

        for i in range(0,len(phi_steps)-1):
            for j in range(0,len(theta_steps)-1):
                self.panels.append( Panel(phi_steps[i], phi_steps[i+1], \
                        theta_steps[j], theta_steps[j+1]) )

    def plot_planet(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        count = 0
        for panel in self.panels:
            x,y,z = panel.get_cartesian_coordinates(self.radius)
            print("\n%d:"%(count))
            count += 1
            print(x)
            print(y)
            print(z)
            ax.plot_surface(x,y,z, linewidth=2)
            break

        plt.show()

def test():
    p = Planet(10.0, 10)
    p.plot_planet()

test()

    



























