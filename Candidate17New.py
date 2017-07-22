#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:10:56 2017

This is the data file for CANDIDATE 17.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    NUV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (AIS)
 
    ***Missing NIR, FUV, xray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 17

C17 = {}
C17["ra"] = 185.8689
C17["dec"] = 46.9752
C17["z"] = 1.681

C17["mag_error_mirw1"] = 0.085
C17["mag_error_mirw2"] = 0.140
C17["mag_error_mirw3"] = "n/a"
C17["mag_error_mirw4"] = "n/a"
C17["mag_error_nirj"] = "n/a"
C17["mag_error_nirk"] = "n/a"
C17["mag_error_sdss_u"] = 0.064
C17["mag_error_sdss_g"] = 0.024
C17["mag_error_sdss_r"] = 0.034
C17["mag_error_sdss_i"] = 0.033
C17["mag_error_sdss_z"] = 0.113
C17["mag_error_fuv"] = "n/a"
C17["mag_error_nuv"] = 0.217

C17["E(B-V)_UKIRT_J"] = 0.009
C17["E(B-V)_UKIRT_K"] =  0.004
C17["E(B-V)_SDSS_u"] = 0.054
C17["E(B-V)_SDSS_g"] = 0.042
C17["E(B-V)_SDSS_r"] = 0.029
C17["E(B-V)_SDSS_i"] = 0.022
C17["E(B-V)_SDSS_z"] = 0.016
C17["E(B-V)_PS1_g"] = 0.040
C17["E(B-V)_PS1_r"] = 0.029
C17["E(B-V)_PS1_i"] = 0.021
C17["E(B-V)_PS1_z"] = 0.017

C17["radio_fdm"] = 0.96
C17["radio_units"] = "mJ/beam"
C17["radio_effective_frequency"] = 1400*10**6
C17["radio_flag"] = 1
C17["radio_source"] = "FIRST"

C17["mirw1_fdm"] = 16.853
C17["mirw1_units"] = "Vega Mag"
C17["mirw1_effective_wavelength"] = 3.35*10**(-4)
C17["mirw1_flag"] = 0
C17["mirw1_source"] = "AllWISE"
C17["mirw1_Vega_0magflux"] = 309.540
C17["mirw2_fdm"] = 16.047
C17["mirw2_units"] = "Vega Mag"
C17["mirw2_effective_wavelength"] = 4.6*(10**-4)
C17["mirw2_flag"] = 0
C17["mirw2_source"] = "AllWISE"
C17["mirw2_Vega_0magflux"] = 171.787
C17["mirw3_fdm"] = 12.398
C17["mirw3_units"] = "Vega Mag"
C17["mirw3_effective_wavelength"] = 11.6*(10**-4)
C17["mirw3_flag"] = 1
C17["mirw3_source"] = "AllWISE"
C17["mirw3_Vega_0magflux"] = 31.674
C17["mirw4_fdm"] = 9.232
C17["mirw4_units"] = "Vega Mag"
C17["mirw4_effective_wavelength"] = 22.1*(10**-4)
C17["mirw4_flag"] = 1
C17["mirw4_source"] = "AllWISE"
C17["mirw4_Vega_0magflux"] = 8.363

C17["nirj_fdm"] = "n/a"
C17["nirj_units"] = "Vega Mag"
C17["nirj_effective_wavelength"] = "n/a" # 1.248*(10**-4)
C17["nirj_flag"] = "n/a"
C17["nirj_source"] = "UKIDSS-DR9"
C17["nirj_Vega_0magflux"] = "n/a" # 1530
C17["nirk_fdm"] = "n/a"
C17["nirk_units"] = "Vega Mag"
C17["nirk_effective_wavelength"] = "n/a" # 2.201*(10**-4)
C17["nirk_flag"] = "n/a"
C17["nirk_source"] = "UKIDSS-DR9"
C17["nirk_Vega_0magflux"] = "n/a" # 631

C17["optu_sdss_fdm"] = 20.723
C17["optu_sdss_units"] = "AB Mag"
C17["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C17["optu_sdss_flag"] = 0
C17["optu_sdss_source"] = "SDSS-DR9"
C17["optg_sdss_fdm"] = 20.578
C17["optg_sdss_units"] = "AB Mag"
C17["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C17["optg_sdss_flag"] = 0
C17["optg_sdss_source"] = "SDSS-DR9"
C17["optr_sdss_fdm"] = 20.672
C17["optr_sdss_units"] = "AB Mag"
C17["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C17["optr_sdss_flag"] = 0
C17["optr_sdss_source"] = "SDSS-DR9"
C17["opti_sdss_fdm"] = 20.303
C17["opti_sdss_units"] = "AB Mag"
C17["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C17["opti_sdss_flag"] = 0
C17["opti_sdss_source"] = "SDSS-DR9"
C17["optz_sdss_fdm"] = 20.323
C17["optz_sdss_units"] = "AB Mag"
C17["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C17["optz_sdss_flag"] = 0
C17["optz_sdss_source"] = "SDSS-DR9"

C17["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C17["optu_cfht_units"] = "AB Mag"
C17["optu_cfht_effective_wavelength"] = 354*(10**-7)
C17["optu_cfht_flag"] = 0
C17["optu_cfht_source"] = "CFHT"
C17["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C17["optg_ps1_units"] = "AB Mag"
C17["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C17["optg_ps1_flag"] = 0
C17["optg_ps1_source"] = "PS1"
C17["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C17["optr_ps1_units"] = "AB Mag"
C17["optr_ps1_effective_wavelength"] = 617*(10**-7)
C17["optr_ps1_flag"] = 0
C17["optr_ps1_source"] = "PS1"
C17["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C17["opti_ps1_units"] = "AB Mag"
C17["opti_ps1_effective_wavelength"] = 752*(10**-7)
C17["opti_ps1_flag"] = 0
C17["opti_ps1_source"] = "PS1"
C17["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C17["optz_ps1_units"] = "AB Mag"
C17["optz_ps1_effective_wavelength"] = 866*(10**-7)
C17["optz_ps1_flag"] = 0
C17["optz_ps1_source"] = "PS1"

C17["fuv_fdm"] = "n/a"
C17["fuv_units"] = "AB Mag"
C17["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C17["fuv_flag"] = "n/a"
C17["fuv_source"] = "GALEX-DR5(AIS)"
C17["nuv_fdm"] = 21.704
C17["nuv_units"] = "AB Mag"
C17["nuv_effective_wavelength"] = 2267*(10**-8)
C17["nuv_flag"] = 0 
C17["nuv_source"] = "GALEX-DR5(AIS)"

C17["xray_flux"] = "n/a"
C17["xray_fdm"] = "n/a"
C17["xray_units"] = "erg/cm^2/keV/s"
C17["xray_effective_energy"] = "n/a" # 2
C17["xray_flag"] = "n/a"
C17["xray_source"] = "XMM-Newtwon-DR6"

