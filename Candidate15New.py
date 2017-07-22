#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:49:28 2017

This is the data file for CANDIDATE 15.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)


***Missing UV, xray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 15

C15 = {}
C15["ra"] = 161.2980
C15["dec"] = 57.4038
C15["z"] = 1.799

C15["mag_error_mirw1"] = 0.096
C15["mag_error_mirw2"] = 0.112
C15["mag_error_mirw3"] = "n/a"
C15["mag_error_mirw4"] = "n/a"
C15["mag_error_nirj"] = 0.022
C15["mag_error_nirk"] = 0.021
C15["mag_error_sdss_u"] = 0.036
C15["mag_error_sdss_g"] = 0.016
C15["mag_error_sdss_r"] = 0.021
C15["mag_error_sdss_i"] = 0.023
C15["mag_error_sdss_z"] = 0.079
C15["mag_error_fuv"] = "n/a"
C15["mag_error_nuv"] = "n/a"

C15["E(B-V)_UKIRT_J"] = 0.004
C15["E(B-V)_UKIRT_K"] = 0.002
C15["E(B-V)_SDSS_u"] = 0.026
C15["E(B-V)_SDSS_g"] = 0.020
C15["E(B-V)_SDSS_r"] = 0.014
C15["E(B-V)_SDSS_i"] = 0.010
C15["E(B-V)_SDSS_z"] = 0.008
C15["E(B-V)_PS1_g"] = 0.020
C15["E(B-V)_PS1_r"] = 0.014
C15["E(B-V)_PS1_i"] = 0.010
C15["E(B-V)_PS1_z"] = 0.008

C15["radio_fdm"] = 0.92
C15["radio_units"] = "mJ/beam"
C15["radio_effective_frequency"] = 1400*10**6
C15["radio_flag"] = 1
C15["radio_source"] = "FIRST"

C15["mirw1_fdm"] = 16.988
C15["mirw1_units"] = "Vega Mag"
C15["mirw1_effective_wavelength"] = 3.35*10**(-4)
C15["mirw1_flag"] = 0
C15["mirw1_source"] = "AllWISE"
C15["mirw1_Vega_0magflux"] = 309.540
C15["mirw2_fdm"] = 15.759
C15["mirw2_units"] = "Vega Mag"
C15["mirw2_effective_wavelength"] = 4.6*(10**-4)
C15["mirw2_flag"] = 0
C15["mirw2_source"] = "AllWISE"
C15["mirw2_Vega_0magflux"] = 171.787
C15["mirw3_fdm"] = 12.228
C15["mirw3_units"] = "Vega Mag"
C15["mirw3_effective_wavelength"] = 11.6*(10**-4)
C15["mirw3_flag"] = 1
C15["mirw3_source"] = "AllWISE"
C15["mirw3_Vega_0magflux"] = 31.674
C15["mirw4_fdm"] = 8.576
C15["mirw4_units"] = "Vega Mag"
C15["mirw4_effective_wavelength"] = 22.1*(10**-4)
C15["mirw4_flag"] = 1
C15["mirw4_source"] = "AllWISE"
C15["mirw4_Vega_0magflux"] = 8.363

C15["nirj_fdm"] = 19.307
C15["nirj_units"] = "Vega Mag"
C15["nirj_effective_wavelength"] = 1.248*(10**-4)
C15["nirj_flag"] = 0
C15["nirj_source"] = "UKIDSS-DR9"
C15["nirj_Vega_0magflux"] = 1530
C15["nirk_fdm"] = 18.282
C15["nirk_units"] = "Vega Mag"
C15["nirk_effective_wavelength"] = 2.201*(10**-4)
C15["nirk_flag"] = 0
C15["nirk_source"] = "UKIDSS-DR9"
C15["nirk_Vega_0magflux"] = 631

C15["optu_sdss_fdm"] = 20.031
C15["optu_sdss_units"] = "AB Mag"
C15["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C15["optu_sdss_flag"] = 0
C15["optu_sdss_source"] = "SDSS-DR9"
C15["optg_sdss_fdm"] = 19.886
C15["optg_sdss_units"] = "AB Mag"
C15["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C15["optg_sdss_flag"] = 0
C15["optg_sdss_source"] = "SDSS-DR9"
C15["optr_sdss_fdm"] = 19.953
C15["optr_sdss_units"] = "AB Mag"
C15["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C15["optr_sdss_flag"] = 0
C15["optr_sdss_source"] = "SDSS-DR9"
C15["opti_sdss_fdm"] = 19.795
C15["opti_sdss_units"] = "AB Mag"
C15["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C15["opti_sdss_flag"] = 0
C15["opti_sdss_source"] = "SDSS-DR9"
C15["optz_sdss_fdm"] = 19.760
C15["optz_sdss_units"] = "AB Mag"
C15["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C15["optz_sdss_flag"] = 0
C15["optz_sdss_source"] = "SDSS-DR9"

C15["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C15["optu_cfht_units"] = "AB Mag"
C15["optu_cfht_effective_wavelength"] = 354*(10**-7)
C15["optu_cfht_flag"] = 0
C15["optu_cfht_source"] = "CFHT"
C15["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C15["optg_ps1_units"] = "AB Mag"
C15["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C15["optg_ps1_flag"] = 0
C15["optg_ps1_source"] = "PS1"
C15["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C15["optr_ps1_units"] = "AB Mag"
C15["optr_ps1_effective_wavelength"] = 617*(10**-7)
C15["optr_ps1_flag"] = 0
C15["optr_ps1_source"] = "PS1"
C15["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C15["opti_ps1_units"] = "AB Mag"
C15["opti_ps1_effective_wavelength"] = 752*(10**-7)
C15["opti_ps1_flag"] = 0
C15["opti_ps1_source"] = "PS1"
C15["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C15["optz_ps1_units"] = "AB Mag"
C15["optz_ps1_effective_wavelength"] = 866*(10**-7)
C15["optz_ps1_flag"] = 0
C15["optz_ps1_source"] = "PS1"

C15["fuv_fdm"] = "n/a"
C15["fuv_units"] = "AB Mag"
C15["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C15["fuv_flag"] = "n/a"
C15["fuv_source"] = "GALEX-DR5(MIS)"
C15["nuv_fdm"] = "n/a"
C15["nuv_units"] = "AB Mag"
C15["nuv_effective_wavelength"] = "n/a" # 2267*(10**-8)
C15["nuv_flag"] = "n/a"
C15["nuv_source"] = "GALEX-DR5(MIS)"

C15["xray_flux"] = "n/a"
C15["xray_fdm"] = "n/a"
C15["xray_units"] = "erg/cm^2/keV/s"
C15["xray_effective_energy"] = "n/a" # 2
C15["xray_flag"] = "n/a"
C15["xray_source"] = "XMM-Newtwon-DR6"


