#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:00:32 2017

This program will read in the data from each candidate's data file, manipulate
it, and store it in different lists to make statistical and plotting work
simpler in their programs. 

First I import the different packages necessary for these calculations and the
candidate files.

@author: megan
"""
import math
import numpy as np
from astropy import units as u
from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)

from Candidate1New import C1
from Candidate2New import C2
from Candidate3New import C3
from Candidate4New import C4
from Candidate5New import C5
from Candidate6New import C6
from Candidate7New import C7
from Candidate8New import C8
from Candidate9New import C9
from Candidate10New import C10
from Candidate11New import C11
from Candidate12New import C12
from Candidate13New import C13
from Candidate14New import C14
from Candidate15New import C15
from Candidate16New import C16
from Candidate17New import C17
from Candidate18New import C18
from Candidate19New import C19
from Candidate20New import C20
from Candidate21New import C21
from Candidate22New import C22
from Candidate23New import C23
from Candidate24New import C24
from Candidate25New import C25
from Candidate26New import C26

from CFHT_PS1Readin import cfht_ps1_data_list
from ElvisMEDReadin import MED_RL_nu, MED_RL_flux, MED_RQ_nu, MED_RQ_flux

CandidateList = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14,
                 C15, C16, C17, C18, C19, C20, C21, C22, C23, C24, C25, C26]

# These lists will get filled with individual lists of data for each candidate.

all_rest_effective_frequencies = [0]

all_mir_rest_effective_frequencies = [0]
all_nir_rest_effective_frequencies = [0]
all_sdss_rest_effective_frequencies = [0]
all_ps1_rest_effective_frequencies = [0]
all_uv_rest_effective_frequencies = [0]

all_mir_mag = [0]
all_nir_mag = [0]
all_sdss_mag = [0]
all_uv_mag = [0]

all_mir_flux = [0]
all_nir_flux = [0]
all_sdss_flux = [0]
all_uv_flux = [0]

all_rest_luminosity = [0]

all_mir_rest_luminosity = [0]
all_nir_rest_luminosity = [0]
all_sdss_rest_luminosity = [0]
all_ps1_rest_luminosity = [0]
all_uv_rest_luminosity = [0]

candidate_num = 1
for candidate in CandidateList:

# First I convert all effective frequencies/wavelengths/energies into rest
# frequencies in hz. To start, I will compile the lists all of of the
# different types of effective "things", since they require different
# processes for conversion. I also break the lists up by the type of
# the range/survey, since this will make normalization and statistical
# analysis easier later on. The lists will be named by 
# section_units_effectives. The x-ray float is from ROSAT's upper limit.

    radio_hz_effectives = [candidate["radio_effective_frequency"]]
    mir_cm_effectives = [candidate["mirw1_effective_wavelength"],
                         candidate["mirw2_effective_wavelength"],
                         candidate["mirw3_effective_wavelength"],
                         candidate["mirw4_effective_wavelength"]]
    nir_cm_effectives = [candidate["nirj_effective_wavelength"],
                         candidate["nirk_effective_wavelength"]]
    sdss_cm_effectives = [candidate["optu_sdss_effective_wavelength"],
                          candidate["optg_sdss_effective_wavelength"],
                          candidate["optr_sdss_effective_wavelength"],
                          candidate["opti_sdss_effective_wavelength"],
                          candidate["optz_sdss_effective_wavelength"]]
    ps1_cm_effectives = [candidate["optu_cfht_effective_wavelength"],
                         candidate["optg_ps1_effective_wavelength"],
                         candidate["optr_ps1_effective_wavelength"],
                         candidate["opti_ps1_effective_wavelength"],
                         candidate["optz_ps1_effective_wavelength"]]
    uv_cm_effectives = [candidate["fuv_effective_wavelength"],
                        candidate["nuv_effective_wavelength"]]
    xray_keV_effectives = [candidate["xray_effective_energy"], 1.5]

# Next, I create empty lists that will be filled as the rest frequencies
# are calculated to serve various purposes. rest_effective_frequencies will
# have all of the data except from PS1, and the other lists are the
# frequencies broken up by range/survey to make compiling specific sections of
# the SED easier.

    rest_effective_frequencies = []

    mir_rest_effective_frequencies = []
    nir_rest_effective_frequencies = []
    sdss_rest_effective_frequencies = []
    ps1_rest_effective_frequencies = []
    uv_rest_effective_frequencies = []

# I now calculate the rest frequencies for each range using:
# nu = c/lambda, 1 keV = 2.417 * 10**17 hz, and finally,
# nu_rest = nu_obs * (1 + z). Each loop first checks if data exists before
# starting these processes.

    for item in radio_hz_effectives:
        if item != "n/a":
            nu_rest = item * (1 + candidate["z"]) # already in hz, convert to
            # rest frame.
            rest_effective_frequencies.append(nu_rest)
    for item in mir_cm_effectives:
        if item != "n/a":
            nu_obs = 3 * 10**10/item  # c / lambda = nu
            nu_rest = nu_obs * (1 + candidate["z"])
            rest_effective_frequencies.append(nu_rest)
            mir_rest_effective_frequencies.append(nu_rest)
    for item in nir_cm_effectives:
        if item != "n/a":
            nu_obs = 3 * 10**10/item
            nu_rest = nu_obs * (1 + candidate["z"])
            rest_effective_frequencies.append(nu_rest)
            nir_rest_effective_frequencies.append(nu_rest)
    for item in sdss_cm_effectives:
        if item != "n/a":
            nu_obs = 3 * 10**10/item
            nu_rest = nu_obs * (1 + candidate["z"])
            rest_effective_frequencies.append(nu_rest)
            sdss_rest_effective_frequencies.append(nu_rest)
    for item in ps1_cm_effectives:
        if item != "n/a":
            nu_obs = 3 * 10**10/item
            nu_rest = nu_obs * (1 + candidate["z"])
            ps1_rest_effective_frequencies.append(nu_rest)
    for item in uv_cm_effectives:
        if item != "n/a":
            nu_obs = 3 * 10**10/item
            nu_rest = nu_obs * (1 + candidate["z"])
            rest_effective_frequencies.append(nu_rest)
            uv_rest_effective_frequencies.append(nu_rest)
    for item in xray_keV_effectives:
        if item != "n/a":
            nu_obs = item * 2.417 * 10**17
            nu_rest = nu_obs * (1 + candidate["z"])
            rest_effective_frequencies.append(nu_rest)

# Next I prepare to convert from different magnitudes/flux densities to the
# same units of flux density (erg/cm^2/hz/s), and then to rest luminosity.
# I compile the lists of the different types of units and ranges/surveys, as
# well as the zero magnitude flux and galactic extinction constants needed for
# calculating from vega magnitude to flux and for correcting for galactic
# extinction, respectively. The lists with flux density/magnitude data will be
# named range/survey_units_fdm, and the lists with constants will be named
# range/survey_constantname. The x-ray float is from ROSAT's upper limit.

    radio_jy_fdm = [candidate["radio_fdm"]]
    mir_vega_fdm = [candidate["mirw1_fdm"], candidate["mirw2_fdm"],
                    candidate["mirw3_fdm"], candidate["mirw4_fdm"]]
    nir_vega_fdm = [candidate["nirj_fdm"], candidate["nirk_fdm"]]
    sdss_ab_fdm = [candidate["optu_sdss_fdm"], candidate["optg_sdss_fdm"],
                   candidate["optr_sdss_fdm"], candidate["opti_sdss_fdm"],
                   candidate["optz_sdss_fdm"]]
    ps1_ab_fdm = [candidate["optu_cfht_fdm"], candidate["optg_ps1_fdm"],
                  candidate["optr_ps1_fdm"], candidate["opti_ps1_fdm"],
                  candidate["optz_ps1_fdm"]]
    uv_ab_fdm = [candidate["fuv_fdm"], candidate["nuv_fdm"]]
    xray_keVfd_fdm = [candidate["xray_fdm"], 2.993e-13]

    mir_0magflux = [candidate["mirw1_Vega_0magflux"],
                    candidate["mirw2_Vega_0magflux"],
                    candidate["mirw3_Vega_0magflux"],
                    candidate["mirw4_Vega_0magflux"]]
    nir_0magflux = [candidate["nirj_Vega_0magflux"],
                    candidate["nirk_Vega_0magflux"]]

    nir_galextfact = [candidate["E(B-V)_UKIRT_J"], candidate["E(B-V)_UKIRT_K"]]
    nir_reddening = [0.709, 0.302]  # [UKIRT J, UKIRT K], same for all

    sdss_galextfact = [candidate["E(B-V)_SDSS_u"], candidate["E(B-V)_SDSS_g"],
                       candidate["E(B-V)_SDSS_r"], candidate["E(B-V)_SDSS_i"],
                       candidate["E(B-V)_SDSS_z"]]
    sdss_reddening = [4.239, 3.303, 2.285, 1.698, 1.263]  # [sdss u, g, r , z]

    ps1_galextfact = [0, candidate["E(B-V)_PS1_g"], candidate["E(B-V)_PS1_r"],
                      candidate["E(B-V)_PS1_i"], candidate["E(B-V)_PS1_z"]]
    ps1_reddening = [0, 3.172, 2.271, 1.682, 1.322]  # [g, r, i, z]

# Here I make use of the astropy package to calculate the luminosity distance.
# The multiplication by the constant converts the units from mega parsecs to
# centimeters.

    d_L_units = cosmo.luminosity_distance(candidate["z"])*3.068e24
    d_L = d_L_units.value

# Now that all the lists and constants are set up, I create empty lists that
# will be filled as different conversions are applied to the data.
# The flux lists record the flux density to be used for chi^2, and all
# luminosities except for those for PS1 are recorded in rest_luminosity and
# are also broken up by range in the lists range/survey_rest_lumionsity for use
# in normalization/plotting.

    mir_flux = []
    nir_flux = []
    sdss_flux = []
    uv_flux = []

    rest_luminosity = []

    mir_rest_luminosity = []
    nir_rest_luminosity = []
    sdss_rest_luminosity = []
    ps1_rest_luminosity = []
    uv_rest_luminosity = []

# Next, all data is converted to the proper flux density units, then to
# rest luminosity. For data from NIR, SDSS, and PS1, the magnitudes are
# corrected for galactic extinction using m_corr = m_obs - E(B-V)*R_v.
# E(B-V) values were taken from
# https://ned.ipac.caltech.edu/forms/calculator.html. R_v values were taken
# from Schlafay et al. 2011.

    for item in radio_jy_fdm:
        if item != "n/a":
            f_nu = item * 10**(-3) * 10**-23  # Convert from mJy to Jy then
            # erg/s/cm^2/hz
            L_rest = (f_nu * 4 * math.pi * (d_L)**2)/(1 + candidate["z"])
            rest_luminosity.append(L_rest)
    for item in mir_vega_fdm:
        if item != "n/a":
            f_nu = mir_0magflux[mir_vega_fdm.index(item)] * \
                   10**(-(item / 2.5)) * 10**-23
            mir_flux.append(f_nu)
            L_rest = (f_nu * 4 * math.pi * (d_L)**2)/(1 + candidate["z"])
            rest_luminosity.append(L_rest)
            mir_rest_luminosity.append(L_rest)
    for item in nir_vega_fdm:
        if item != "n/a":
            f_nu_obs = nir_0magflux[nir_vega_fdm.index(item)] * \
                       10**(-(item / 2.5)) * 10**-23
            m_ab_obs = -2.5 * np.log10(f_nu_obs) - 48.6  # Go back to AB for
            # galactic extinction correction due to assumption that these
            # constants are given assuming AB magnitude scale.
            m_ab_corr = m_ab_obs - nir_galextfact[nir_vega_fdm.index(item)] \
                        * nir_reddening[nir_vega_fdm.index(item)]
            f_nu_corr = 10**(-(m_ab_corr + 48.6)/2.5)
            nir_flux.append(f_nu_corr)
            L_rest = (f_nu_corr * 4 * math.pi * (d_L)**2)/(1 + candidate["z"])
            rest_luminosity.append(L_rest)
            nir_rest_luminosity.append(L_rest)
    for item in sdss_ab_fdm:
        if item != "n/a":
            m_corr = item - sdss_galextfact[sdss_ab_fdm.index(item)] * \
                     sdss_reddening[sdss_ab_fdm.index(item)]
            f_nu = 10**(-((m_corr + 48.6) / 2.5))
            sdss_flux.append(f_nu)
            L_rest = (f_nu * 4 * math.pi * (d_L)**2)/(1 + candidate["z"])
            rest_luminosity.append(L_rest)
            sdss_rest_luminosity.append(L_rest)
    for item in ps1_ab_fdm:
        if item != "n/a":
            m_corr = item - ps1_galextfact[ps1_ab_fdm.index(item)] * \
                     ps1_reddening[ps1_ab_fdm.index(item)]
            f_nu = 10**(-((m_corr + 48.6) / 2.5))
            L_rest = (f_nu * 4 * math.pi * (d_L)**2)/(1 + candidate["z"])
            ps1_rest_luminosity.append(L_rest)
    for item in uv_ab_fdm:
        if item != "n/a":
            f_nu = 10**(-((item + 48.6) / 2.5))
            uv_flux.append(f_nu)
            L_rest = (f_nu * 4 * math.pi * (d_L)**2)/(1 + candidate["z"])
            rest_luminosity.append(L_rest)
            uv_rest_luminosity.append(L_rest)
    for item in xray_keVfd_fdm:
        if item != "n/a":
            L_rest = (item * 2.417 * 10**-17 * 4 * math.pi * (d_L)**2) / (1 +
                      candidate["z"])
            rest_luminosity.append(L_rest)

# I want to save all of these for each individual candidate to read into other
# functions, so I  save them to a list of these lists. I start these with a 0
# so that the index corresponds to the candidate number (see them at top).

    all_rest_effective_frequencies.append(rest_effective_frequencies)

    all_mir_rest_effective_frequencies.append(mir_rest_effective_frequencies)
    all_nir_rest_effective_frequencies.append(nir_rest_effective_frequencies)
    all_sdss_rest_effective_frequencies.append(sdss_rest_effective_frequencies)
    all_ps1_rest_effective_frequencies.append(ps1_rest_effective_frequencies)
    all_uv_rest_effective_frequencies.append(uv_rest_effective_frequencies)

    all_mir_flux.append(mir_flux)
    all_nir_flux.append(nir_flux)
    all_sdss_flux.append(sdss_flux)
    all_uv_flux.append(uv_flux)

    all_rest_luminosity.append(rest_luminosity)

    all_mir_rest_luminosity.append(mir_rest_luminosity)
    all_nir_rest_luminosity.append(nir_rest_luminosity)
    all_sdss_rest_luminosity.append(sdss_rest_luminosity)
    all_ps1_rest_luminosity.append(ps1_rest_luminosity)
    all_uv_rest_luminosity.append(uv_rest_luminosity)

# Finally, I increase the index of the candidate_num for the loop.

    candidate_num = candidate_num + 1

# Saying a prayer that I did all of this correctly!
