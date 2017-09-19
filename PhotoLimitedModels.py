import numpy as np
import PlanetModel import Planet
from math import exp, pi

H = 6.626E-34 #Planck constant in [J s]
C = 2.99792458E8 #Speed of light [m s-1]                                          
KB = 1.38E-23 #Boltzmann constant in [m2 kg s-2 K-1]
AU = 1.496E11 #1 AU in [m]
SUN_RAD = 6.957E8 #solar radius [m]


def blackbody_flux(T, wvlngth):
    """
    Return the total photon flux in W m-2 s-1 for a blackbody at temperature
    T for the given wavelength, wvlngth. 

    Parameters:
    T - the temperature of the blackbody [K]
    wvlngth - the frequency at which to calculate the photon flux [nm]

    Returns:
    flux - the photon flux at wvlngth [W m-2 s-1 nm-1]
    """

    wvlngth = wvlngth*(1.0E-9) #convert from nm to m
    flux = 2.0*H*C**2.0/wvlngth**5.0*1.0/(exp(H*C/(wvlngth*KB*T))-1.0)
    return flux*pi

def get_blackbody_flux_for_wavelengths(T, wvlngths, \
        star_rad=1.0, orbital_rad=1.0):
    """
    Get the photon fluxes for an array of wavelength values.

    NOTE: this function can be used for calculating the flux a planet receives
          at an orbital distance of orbital_rad. 

    Inputs:
    T - the temperature of the blackbody [K]
    wvlngths - array of wavelengths to calculate fluxes for [nm]
    star_rad - the radius of the star [m]
    orbital_rad - the radius of the orbit [m]

    Returns:
    fluxes - an array of fluxes for the corresponding wavelength values
             in [W m-2 s-1 nm-1]
    """

    fluxes = np.zeros_like(wvlngths)
    for i in range(0,len(wvlngths)):
        fluxes[i] = blackbody_flux(T, wvlngths[i])*(star_rad/orbital_rad)**2

    return fluxes


def total_flux(wvlngths, fluxes):
    """
    This function will take an array of wavelengths and an array of fluxes then
    return the total flux of the fluxes array.

    Inputs:
    wvlngths - the array of wavelength values [nm]
    fluxes - the array of flux values [W m-2 s-1 nm-1]

    Returns:
    t_flux - the summed fluxes from the fluxes array [Photons m-2 s-1]
    """

    t_flux = 0.0

    width = 0.0
    for i in range(0,len(wvlngths)-1):
        width = abs(wvlngths[i]-wvlngths[i+1])*(1.0E-9) #convert from nm to m
        t_flux += width*fluxes[i]

    #add the last flux measurement using the width of the previous freq.
    t_flux += width*fluxes[-1]

    return t_flux



def show_planet_flux(star_temp, orb_dist, planet_radius, albedo):
    plnt = Planet(6.0E6, 20)




def test():
    wavelengths = np.linspace(10,5000,150)
    fluxes = get_blackbody_flux_for_wavelengths(5800.0, wavelengths, star_rad=SUN_RAD,\
            orbital_rad=AU)
    tot = total_flux(wavelengths, fluxes)
    print("Total flux is: %0.2f"%(tot))

test()
