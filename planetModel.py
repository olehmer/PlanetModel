import numpy as np
import json
from math import pi, sin, cos

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
        self.color = 0
        self.albedo = []

    def set_albedo(self, albedo):
        """
        Set the albedo of the panel. The passed in albedo array should be 
        broken into wavelength bands.
        """
        self.albedo = albedo


    def get_cartesian_coordinates(self,planet_radius, scale = 0):
        """
        Return the x,y,z coordinates of the panel.

        Input:
        planet_radius - the radius of the planet [m]
        scale - the factor by which the planet will be scaled. If set to 0
                the planet will be scaled down by 1/5th the radius for ease of 
                use when plotting (no need to plot huge numbers when smaller 
                ones will work just fine).
        """

        if scale <= 0:
            scale = 5.0/planet_radius

        x0 = planet_radius*sin(self.start_phi)*cos(self.start_theta)/scale
        y0 = planet_radius*sin(self.start_phi)*sin(self.start_theta)/scale
        z0 = planet_radius*cos(self.start_phi)/scale

        x1 = planet_radius*sin(self.start_phi)*cos(self.end_theta)/scale
        y1 = planet_radius*sin(self.start_phi)*sin(self.end_theta)/scale
        z1 = planet_radius*cos(self.start_phi)/scale

        x2 = planet_radius*sin(self.end_phi)*cos(self.end_theta)/scale
        y2 = planet_radius*sin(self.end_phi)*sin(self.end_theta)/scale
        z2 = planet_radius*cos(self.end_phi)/scale

        x3 = planet_radius*sin(self.end_phi)*cos(self.start_theta)/scale
        y3 = planet_radius*sin(self.end_phi)*sin(self.start_theta)/scale
        z3 = planet_radius*cos(self.end_phi)/scale

        #scale down everything by 1/5th the radius so all planets will
        #be the same size when rendered

        return (x0,y0,z0), (x1,y1,z1), (x2,y2,z2), (x3,y3,z3)

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


    def generate_planet_data(self):
        """
        Generate the vertices of the panels and save them to a JSON file for
        use in the WebGL rendering.
        """

        panels = []
        for panel in self.panels:
            panel_verts = panel.get_cartesian_coordinates(self.radius)
            panel_data = panel_verts, panel.color
            panels.append(panel_data)

        #write the panel data out to a JSON file
        output_dict = {}
        output_dict["panels"] = panels
        with open("Web/planet_data.json", "w") as outfile:
            json.dump(output_dict, outfile)#, indent=2)



#def test():
#    p = Planet(10.0, 15)
#    p.generate_planet_data()
#
#test()

    







