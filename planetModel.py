import numpy as np
from math import pi, log, exp



class Panel:
    """
    The Panel object will store the coordinates of each panel on the planet, in
    spherical coordinates. 
    """

    def __init__(self, start_phi, end_phi, start_rho, end_rho):
        self.start_phi = start_phi
        self.start_rho = start_rho
        self.end_phi = end_phi
        self.end_rho = end_rho

    def set_albedo(self, albedo):
        """
        Set the albedo of the panel. The passed in albedo array should be 
        broken into wavelength bands.
        """
        self.albedo = [] #TODO: implement this later

    def get_cartesian_coordinates(planet_radius):
        """
        Return the x,y,z coordinates of the panel.
        """
        x,y,z = 0 #TODO: implement
        return [(x,y,z),(x,y,z),(x,y,z),(x,y,z)]

class Planet:
    """
    Create a planet made out of flat panels. 
    """

    def __init__(self, radius, num_panels):
        """
        Initialize the planet.

        Inputs:
        radius - the planet radius [m]
        num_panels - the number of flat panels in each hemisphere of the planet.
        """

        self.radius = radius
        self.num_panels = num_panels

    def generate_panels():
