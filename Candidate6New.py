#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 12:59:20 2017

This is the data file for CANDIDATE 6.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    NUV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (AIS)
    
** Missing NIR, UV, Xray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 6

C6 = {}
C6["ra"] = 131.1273
C6["dec"] = 44.8582
C6["z"] = 2.011

C6["mag_error_mirw1"] = 0.077
C6["mag_error_mirw2"] = 0.097
C6["mag_error_mirw3"] = 0.538
C6["mag_error_mirw4"] = "n/a"
C6["mag_error_nirj"] = "n/a"
C6["mag_error_nirk"] = "n/a"
C6["mag_error_sdss_u"] = 0.071
C6["mag_error_sdss_g"] = 0.027
C6["mag_error_sdss_r"] = 0.033
C6["mag_error_sdss_i"] = 0.032
C6["mag_error_sdss_z"] = 0.090
C6["mag_error_fuv"] = "n/a"
C6["mag_error_nuv"] = "n/a"

C6["E(B-V)_UKIRT_J"] = 0.021
C6["E(B-V)_UKIRT_K"] =  0.009
C6["E(B-V)_SDSS_u"] = 0.127
C6["E(B-V)_SDSS_g"] = 0.099
C6["E(B-V)_SDSS_r"] = 0.068
C6["E(B-V)_SDSS_i"] = 0.051
C6["E(B-V)_SDSS_z"] = 0.038
C6["E(B-V)_PS1_g"] = 0.095
C6["E(B-V)_PS1_r"] = 0.068
C6["E(B-V)_PS1_i"] = 0.050
C6["E(B-V)_PS1_z"] = 0.039

C6["radio_fdm"] = 0.94
C6["radio_units"] = "mJ/beam"
C6["radio_effective_frequency"] = 1400*10**6
C6["radio_flag"] = 1
C6["radio_source"] = "FIRST"

C6["mirw1_fdm"] = 16.556
C6["mirw1_units"] = "Vega Mag"
C6["mirw1_effective_wavelength"] = 3.35*10**(-4)
C6["mirw1_flag"] = 0
C6["mirw1_source"] = "AllWISE"
C6["mirw1_Vega_0magflux"] = 309.540
C6["mirw2_fdm"] = 15.443
C6["mirw2_units"] = "Vega Mag"
C6["mirw2_effective_wavelength"] = 4.6*(10**-4)
C6["mirw2_flag"] = 0
C6["mirw2_source"] = "AllWISE"
C6["mirw2_Vega_0magflux"] = 171.787
C6["mirw3_fdm"] = 12.549
C6["mirw3_units"] = "Vega Mag"
C6["mirw3_effective_wavelength"] = 11.6*(10**-4)
C6["mirw3_flag"] = 0
C6["mirw3_source"] = "AllWISE"
C6["mirw3_Vega_0magflux"] = 31.674
C6["mirw4_fdm"] = 8.342
C6["mirw4_units"] = "Vega Mag"
C6["mirw4_effective_wavelength"] = 22.1*(10**-4)
C6["mirw4_flag"] = 1
C6["mirw4_source"] = "AllWISE"
C6["mirw4_Vega_0magflux"] = 8.363

C6["nirj_fdm"] = "n/a"
C6["nirj_units"] = "Vega Mag"
C6["nirj_effective_wavelength"] = "n/a" # 1.235*(10**-4)
C6["nirj_flag"] = "n/a"
C6["nirj_source"] = "UKIDSS-DR9"
C6["nirj_Vega_0magflux"] = "n/a"
C6["nirk_fdm"] = "n/a"
C6["nirk_units"] = "Vega Mag"
C6["nirk_effective_wavelength"] = "n/a"
C6["nirk_flag"] = "n/a"
C6["nirk_source"] = "UKIDSS-DR9"
C6["nirk_Vega_0magflux"] = "n/a"

C6["optu_sdss_fdm"] = 20.924
C6["optu_sdss_units"] = "AB Mag"
C6["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C6["optu_sdss_flag"] = 0
C6["optu_sdss_source"] = "SDSS-DR9"
C6["optg_sdss_fdm"] = 20.661
C6["optg_sdss_units"] = "AB Mag"
C6["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C6["optg_sdss_flag"] = 0
C6["optg_sdss_source"] = "SDSS-DR9"
C6["optr_sdss_fdm"] = 20.555
C6["optr_sdss_units"] = "AB Mag"
C6["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C6["optr_sdss_flag"] = 0
C6["optr_sdss_source"] = "SDSS-DR9"
C6["opti_sdss_fdm"] = 20.202
C6["opti_sdss_units"] = "AB Mag"
C6["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C6["opti_sdss_flag"] = 0
C6["opti_sdss_source"] = "SDSS-DR9"
C6["optz_sdss_fdm"] = 19.927
C6["optz_sdss_units"] = "AB Mag"
C6["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C6["optz_sdss_flag"] = 0
C6["optz_sdss_source"] = "SDSS-DR9"

C6["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C6["optu_cfht_units"] = "AB Mag"
C6["optu_cfht_effective_wavelength"] = 354*(10**-7)
C6["optu_cfht_flag"] = 0
C6["optu_cfht_source"] = "CFHT"
C6["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C6["optg_ps1_units"] = "AB Mag"
C6["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C6["optg_ps1_flag"] = 0
C6["optg_ps1_source"] = "PS1"
C6["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C6["optr_ps1_units"] = "AB Mag"
C6["optr_ps1_effective_wavelength"] = 617*(10**-7)
C6["optr_ps1_flag"] = 0
C6["optr_ps1_source"] = "PS1"
C6["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C6["opti_ps1_units"] = "AB Mag"
C6["opti_ps1_effective_wavelength"] = 752*(10**-7)
C6["opti_ps1_flag"] = 0
C6["opti_ps1_source"] = "PS1"
C6["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C6["optz_ps1_units"] = "AB Mag"
C6["optz_ps1_effective_wavelength"] = 866*(10**-7)
C6["optz_ps1_flag"] = 0
C6["optz_ps1_source"] = "PS1"

C6["fuv_fdm"] = "n/a"
C6["fuv_units"] = "AB Mag"
C6["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C6["fuv_flag"] = "n/a"
C6["fuv_source"] = "GALEX-DR5(AIS)"
C6["nuv_fdm"] = "n/a"
C6["nuv_units"] = "AB Mag"
C6["nuv_effective_wavelength"] = "n/a"
C6["nuv_flag"] = "n/a"
C6["nuv_source"] = "GALEX-DR5(AIS)"

C6["xray_flux"] = "n/a"
C6["xray_fdm"] = "n/a"
C6["xray_units"] = "erg/cm^2/keV/s"
C6["xray_effective_energy"] = "n/a" # 2
C6["xray_flag"] = "n/a"
C6["xray_source"] = "XMM-Newtwon-DR6"
