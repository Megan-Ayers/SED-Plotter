#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:29:15 2017

This is the data file for CANDIDATE 18.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    Radio from http://sundog.stsci.edu/cgi-bin/searchfirst, *** r = 25.8 
    arcsecs***
    MIR from AllWISE Data Release (Cutri+ 2013) *** r = 9.956 arcsecs *** 
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    
    
    ***Missing NIR, UV, xray 

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 18

C18 = {}
C18["ra"] = 213.9985
C18["dec"] = 52.7527
C18["z"] = 1.867

C18["mag_error_radio"] = 0.148

C18["mag_error_mirw1"] = 0.047
C18["mag_error_mirw2"] = 0.088
C18["mag_error_mirw3"] = 0.195
C18["mag_error_mirw4"] = "n/a"
C18["mag_error_nirj"] = "n/a"
C18["mag_error_nirk"] = "n/a"
C18["mag_error_sdss_u"] = 0.075
C18["mag_error_sdss_g"] = 0.032
C18["mag_error_sdss_r"] = 0.059
C18["mag_error_sdss_i"] = 0.056
C18["mag_error_sdss_z"] = 0.166
C18["mag_error_fuv"] = "n/a"
C18["mag_error_nuv"] = "n/a"

C18["E(B-V)_UKIRT_J"] = 0.007
C18["E(B-V)_UKIRT_K"] =  0.003
C18["E(B-V)_SDSS_u"] = 0.044
C18["E(B-V)_SDSS_g"] = 0.034
C18["E(B-V)_SDSS_r"] = 0.024
C18["E(B-V)_SDSS_i"] = 0.017
C18["E(B-V)_SDSS_z"] = 0.013
C18["E(B-V)_PS1_g"] = 0.033
C18["E(B-V)_PS1_r"] = 0.023
C18["E(B-V)_PS1_i"] = 0.017
C18["E(B-V)_PS1_z"] = 0.014

C18["radio_fdm"] = 2.04 # 1.96 = peak, int. flux is 2.04 in mJy.
C18["radio_units"] = "mJ"
C18["radio_effective_frequency"] = 1400*10**6
C18["radio_flag"] = 0
C18["radio_source"] = "FIRST"

C18["mirw1_fdm"] = 16.179
C18["mirw1_units"] = "Vega Mag"
C18["mirw1_effective_wavelength"] = 3.35*10**(-4)
C18["mirw1_flag"] = 0
C18["mirw1_source"] = "AllWISE"
C18["mirw1_Vega_0magflux"] = 309.540
C18["mirw2_fdm"] = 15.598
C18["mirw2_units"] = "Vega Mag"
C18["mirw2_effective_wavelength"] = 4.6*(10**-4)
C18["mirw2_flag"] = 0
C18["mirw2_source"] = "AllWISE"
C18["mirw2_Vega_0magflux"] = 171.787
C18["mirw3_fdm"] = 11.905
C18["mirw3_units"] = "Vega Mag"
C18["mirw3_effective_wavelength"] = 11.6*(10**-4)
C18["mirw3_flag"] = 0
C18["mirw3_source"] = "AllWISE"
C18["mirw3_Vega_0magflux"] = 31.674
C18["mirw4_fdm"] = 9.425
C18["mirw4_units"] = "Vega Mag"
C18["mirw4_effective_wavelength"] = 22.1*(10**-4)
C18["mirw4_flag"] = 1
C18["mirw4_source"] = "AllWISE"
C18["mirw4_Vega_0magflux"] = 8.363

C18["nirj_fdm"] = "n/a"
C18["nirj_units"] = "Vega Mag"
C18["nirj_effective_wavelength"] = "n/a" # 1.248*(10**-4)
C18["nirj_flag"] = "n/a"
C18["nirj_source"] = "UKIDSS-DR9"
C18["nirj_Vega_0magflux"] = "n/a" # 1530
C18["nirk_fdm"] = "n/a"
C18["nirk_units"] = "Vega Mag"
C18["nirk_effective_wavelength"] = "n/a" # 2.201*(10**-4)
C18["nirk_flag"] = "n/a"
C18["nirk_source"] = "UKIDSS-DR9"
C18["nirk_Vega_0magflux"] = "n/a" # 631

C18["optu_sdss_fdm"] = 20.818
C18["optu_sdss_units"] = "AB Mag"
C18["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C18["optu_sdss_flag"] = 0
C18["optu_sdss_source"] = "SDSS-DR9"
C18["optg_sdss_fdm"] = 20.786
C18["optg_sdss_units"] = "AB Mag"
C18["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C18["optg_sdss_flag"] = 0
C18["optg_sdss_source"] = "SDSS-DR9"
C18["optr_sdss_fdm"] = 21.005
C18["optr_sdss_units"] = "AB Mag"
C18["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C18["optr_sdss_flag"] = 0
C18["optr_sdss_source"] = "SDSS-DR9"
C18["opti_sdss_fdm"] = 20.493
C18["opti_sdss_units"] = "AB Mag"
C18["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C18["opti_sdss_flag"] = 0
C18["opti_sdss_source"] = "SDSS-DR9"
C18["optz_sdss_fdm"] = 20.371
C18["optz_sdss_units"] = "AB Mag"
C18["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C18["optz_sdss_flag"] = 0
C18["optz_sdss_source"] = "SDSS-DR9"

C18["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C18["optu_cfht_units"] = "AB Mag"
C18["optu_cfht_effective_wavelength"] = 354*(10**-7)
C18["optu_cfht_flag"] = 0
C18["optu_cfht_source"] = "CFHT"
C18["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C18["optg_ps1_units"] = "AB Mag"
C18["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C18["optg_ps1_flag"] = 0
C18["optg_ps1_source"] = "PS1"
C18["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C18["optr_ps1_units"] = "AB Mag"
C18["optr_ps1_effective_wavelength"] = 617*(10**-7)
C18["optr_ps1_flag"] = 0
C18["optr_ps1_source"] = "PS1"
C18["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C18["opti_ps1_units"] = "AB Mag"
C18["opti_ps1_effective_wavelength"] = 752*(10**-7)
C18["opti_ps1_flag"] = 0
C18["opti_ps1_source"] = "PS1"
C18["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C18["optz_ps1_units"] = "AB Mag"
C18["optz_ps1_effective_wavelength"] = 866*(10**-7)
C18["optz_ps1_flag"] = 0
C18["optz_ps1_source"] = "PS1"

C18["fuv_fdm"] = "n/a"
C18["fuv_units"] = "AB Mag"
C18["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C18["fuv_flag"] = "n/a"
C18["fuv_source"] = "GALEX-DR5(MIS)"
C18["nuv_fdm"] = "n/a"
C18["nuv_units"] = "AB Mag"
C18["nuv_effective_wavelength"] = "n/a" # 2267*(10**-8)
C18["nuv_flag"] = "n/a"
C18["nuv_source"] = "GALEX-DR5(MIS)"

C18["xray_flux"] = "n/a"
C18["xray_fdm"] = "n/a"
C18["xray_units"] = "erg/cm^2/keV/s"
C18["xray_effective_energy"] = "n/a" # 2
C18["xray_flag"] = "n/a"
C18["xray_source"] = "XMM-Newtwon-DR6"
