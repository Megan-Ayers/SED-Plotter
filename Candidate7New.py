#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 13:32:38 2017

This is the data file for CANDIDATE 7.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    NUV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011)
***Missing: NIR, FUV, Xray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 7

C7 = {}
C7["ra"] = 131.7789
C7["dec"] = 45.0939
C7["z"] = 1.233

C7["mag_error_mirw1"] = 0.076
C7["mag_error_mirw2"] = 0.123
C7["mag_error_mirw3"] = "n/a"
C7["mag_error_mirw4"] = "n/a"
C7["mag_error_nirj"] = "n/a"
C7["mag_error_nirk"] = "n/a"
C7["mag_error_sdss_u"] = 0.057
C7["mag_error_sdss_g"] = 0.030
C7["mag_error_sdss_r"] = 0.026
C7["mag_error_sdss_i"] = 0.037
C7["mag_error_sdss_z"] = 0.122
C7["mag_error_fuv"] = "n/a"
C7["mag_error_nuv"] = 0.196

C7["E(B-V)_UKIRT_J"] = 0.020
C7["E(B-V)_UKIRT_K"] = 0.009
C7["E(B-V)_SDSS_u"] = 0.123
C7["E(B-V)_SDSS_g"] = 0.095
C7["E(B-V)_SDSS_r"] = 0.066
C7["E(B-V)_SDSS_i"] = 0.049
C7["E(B-V)_SDSS_z"] = 0.037
C7["E(B-V)_PS1_g"] = 0.092
C7["E(B-V)_PS1_r"] = 0.066
C7["E(B-V)_PS1_i"] = 0.049
C7["E(B-V)_PS1_z"] = 0.038

C7["radio_fdm"] = 0.92
C7["radio_units"] = "mJ/beam"
C7["radio_effective_frequency"] = 1400*10**6
C7["radio_flag"] = 1
C7["radio_source"] = "FIRST"

C7["mirw1_fdm"] = 16.630
C7["mirw1_units"] = "Vega Mag"
C7["mirw1_effective_wavelength"] = 3.35*10**(-4)
C7["mirw1_flag"] = 0
C7["mirw1_source"] = "AllWISE"
C7["mirw1_Vega_0magflux"] = 309.540
C7["mirw2_fdm"] = 15.782
C7["mirw2_units"] = "Vega Mag"
C7["mirw2_effective_wavelength"] = 4.6*(10**-4)
C7["mirw2_flag"] = 0
C7["mirw2_source"] = "AllWISE"
C7["mirw2_Vega_0magflux"] = 171.787
C7["mirw3_fdm"] = 12.452
C7["mirw3_units"] = "Vega Mag"
C7["mirw3_effective_wavelength"] = 11.6*(10**-4)
C7["mirw3_flag"] = 1
C7["mirw3_source"] = "AllWISE"
C7["mirw3_Vega_0magflux"] = 31.674
C7["mirw4_fdm"] = 8.930
C7["mirw4_units"] = "Vega Mag"
C7["mirw4_effective_wavelength"] = 22.1*(10**-4)
C7["mirw4_flag"] = 1
C7["mirw4_source"] = "AllWISE"
C7["mirw4_Vega_0magflux"] = 8.363

C7["nirj_fdm"] = "n/a"
C7["nirj_units"] = "Vega Mag"
C7["nirj_effective_wavelength"] = "n/a" # 1.248*(10**-4)
C7["nirj_flag"] = "n/a"
C7["nirj_source"] = "UKIDSS-DR9"
C7["nirj_Vega_0magflux"] = "n/a" # 1530
C7["nirk_fdm"] = "n/a"
C7["nirk_units"] = "Vega Mag"
C7["nirk_effective_wavelength"] = "n/a" # 2.201*(10**-4)
C7["nirk_flag"] = "n/a"
C7["nirk_source"] = "UKIDSS-DR9"
C7["nirk_Vega_0magflux"] = "n/a" #  631

C7["optu_sdss_fdm"] = 20.567
C7["optu_sdss_units"] = "AB Mag"
C7["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C7["optu_sdss_flag"] = 0
C7["optu_sdss_source"] = "SDSS-DR9"
C7["optg_sdss_fdm"] = 20.588
C7["optg_sdss_units"] = "AB Mag"
C7["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C7["optg_sdss_flag"] = 0
C7["optg_sdss_source"] = "SDSS-DR9"
C7["optr_sdss_fdm"] = 20.236
C7["optr_sdss_units"] = "AB Mag"
C7["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C7["optr_sdss_flag"] = 0
C7["optr_sdss_source"] = "SDSS-DR9"
C7["opti_sdss_fdm"] = 20.297
C7["opti_sdss_units"] = "AB Mag"
C7["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C7["opti_sdss_flag"] = 0
C7["opti_sdss_source"] = "SDSS-DR9"
C7["optz_sdss_fdm"] = 20.080
C7["optz_sdss_units"] = "AB Mag"
C7["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C7["optz_sdss_flag"] = 0
C7["optz_sdss_source"] = "SDSS-DR9"

C7["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C7["optu_cfht_units"] = "AB Mag"
C7["optu_cfht_effective_wavelength"] = 354*(10**-7)
C7["optu_cfht_flag"] = 0
C7["optu_cfht_source"] = "CFHT"
C7["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C7["optg_ps1_units"] = "AB Mag"
C7["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C7["optg_ps1_flag"] = 0
C7["optg_ps1_source"] = "PS1"
C7["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C7["optr_ps1_units"] = "AB Mag"
C7["optr_ps1_effective_wavelength"] = 617*(10**-7)
C7["optr_ps1_flag"] = 0
C7["optr_ps1_source"] = "PS1"
C7["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C7["opti_ps1_units"] = "AB Mag"
C7["opti_ps1_effective_wavelength"] = 752*(10**-7)
C7["opti_ps1_flag"] = 0
C7["opti_ps1_source"] = "PS1"
C7["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C7["optz_ps1_units"] = "AB Mag"
C7["optz_ps1_effective_wavelength"] = 866*(10**-7)
C7["optz_ps1_flag"] = 0
C7["optz_ps1_source"] = "PS1"

C7["fuv_fdm"] = "n/a"
C7["fuv_units"] = "AB Mag"
C7["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C7["fuv_flag"] = "n/a"
C7["fuv_source"] = "GALEX-DR5(MIS)"
C7["nuv_fdm"] = 21.271
C7["nuv_units"] = "AB Mag"
C7["nuv_effective_wavelength"] = 2267*(10**-8)
C7["nuv_flag"] = 0
C7["nuv_source"] = "GALEX-DR5(MIS)"

C7["xray_flux"] = "n/a"
C7["xray_fdm"] = "n/a"
C7["xray_units"] = "erg/cm^2/keV/s"
C7["xray_effective_energy"] = "n/a" # 2
C7["xray_flag"] = "n/a"
C7["xray_source"] = "XMM-Newtwon-DR6"
