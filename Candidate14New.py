#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:42:04 2017

This isthe data file for CANDIDATE 14.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    
    
    ***Missing NIR, UV, x-ray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 14

C14 = {}
C14["ra"] = 160.6037
C14["dec"] = 56.9160
C14["z"] = 1.445

C14["mag_error_mirw1"] = 0.049
C14["mag_error_mirw2"] = 0.053
C14["mag_error_mirw3"] = 0.204
C14["mag_error_mirw4"] = "n/a"
C14["mag_error_nirj"] = "n/a"
C14["mag_error_nirk"] = "n/a"
C14["mag_error_sdss_u"] = 0.037
C14["mag_error_sdss_g"] = 0.016
C14["mag_error_sdss_r"] = 0.019
C14["mag_error_sdss_i"] = 0.022
C14["mag_error_sdss_z"] = 0.083
C14["mag_error_fuv"] = "n/a"
C14["mag_error_nuv"] = "n/a"

C14["E(B-V)_UKIRT_J"] = 0.003
C14["E(B-V)_UKIRT_K"] =  0.001
C14["E(B-V)_SDSS_u"] = 0.019
C14["E(B-V)_SDSS_g"] = 0.014
C14["E(B-V)_SDSS_r"] = 0.010
C14["E(B-V)_SDSS_i"] = 0.007
C14["E(B-V)_SDSS_z"] = 0.006
C14["E(B-V)_PS1_g"] = 0.014
C14["E(B-V)_PS1_r"] = 0.010
C14["E(B-V)_PS1_i"] = 0.007
C14["E(B-V)_PS1_z"] = 0.006

C14["radio_fdm"] = 1.02
C14["radio_units"] = "mJ/beam"
C14["radio_effective_frequency"] = 1400*10**6
C14["radio_flag"] = 1
C14["radio_source"] = "FIRST"

C14["mirw1_fdm"] = 16.008
C14["mirw1_units"] = "Vega Mag"
C14["mirw1_effective_wavelength"] = 3.35*10**(-4)
C14["mirw1_flag"] = 0
C14["mirw1_source"] = "AllWISE"
C14["mirw1_Vega_0magflux"] = 309.540
C14["mirw2_fdm"] = 14.750
C14["mirw2_units"] = "Vega Mag"
C14["mirw2_effective_wavelength"] = 4.6*(10**-4)
C14["mirw2_flag"] = 0
C14["mirw2_source"] = "AllWISE"
C14["mirw2_Vega_0magflux"] = 171.787
C14["mirw3_fdm"] = 11.720
C14["mirw3_units"] = "Vega Mag"
C14["mirw3_effective_wavelength"] = 11.6*(10**-4)
C14["mirw3_flag"] = 0
C14["mirw3_source"] = "AllWISE"
C14["mirw3_Vega_0magflux"] = 31.674
C14["mirw4_fdm"] = 8.793
C14["mirw4_units"] = "Vega Mag"
C14["mirw4_effective_wavelength"] = 22.1*(10**-4)
C14["mirw4_flag"] = 1
C14["mirw4_source"] = "AllWISE"
C14["mirw4_Vega_0magflux"] = 8.363

C14["nirj_fdm"] = "n/a"
C14["nirj_units"] = "Vega Mag"
C14["nirj_effective_wavelength"] = "n/a" # 1.248*(10**-4)
C14["nirj_flag"] = "n/a"
C14["nirj_source"] = "UKIDSS-DR9"
C14["nirj_Vega_0magflux"] = "n/a" # 1530
C14["nirk_fdm"] = "n/a"
C14["nirk_units"] = "Vega Mag"
C14["nirk_effective_wavelength"] = "n/a" # 2.201*(10**-4)
C14["nirk_flag"] = "n/a"
C14["nirk_source"] = "UKIDSS-DR9"
C14["nirk_Vega_0magflux"] = "n/a" # 631

C14["optu_sdss_fdm"] = 19.963
C14["optu_sdss_units"] = "AB Mag"
C14["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C14["optu_sdss_flag"] = 0
C14["optu_sdss_source"] = "SDSS-DR9"
C14["optg_sdss_fdm"] = 19.840
C14["optg_sdss_units"] = "AB Mag"
C14["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C14["optg_sdss_flag"] = 0
C14["optg_sdss_source"] = "SDSS-DR9"
C14["optr_sdss_fdm"] = 19.750
C14["optr_sdss_units"] = "AB Mag"
C14["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C14["optr_sdss_flag"] = 0
C14["optr_sdss_source"] = "SDSS-DR9"
C14["opti_sdss_fdm"] = 19.651
C14["opti_sdss_units"] = "AB Mag"
C14["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C14["opti_sdss_flag"] = 0
C14["opti_sdss_source"] = "SDSS-DR9"
C14["optz_sdss_fdm"] = 19.856
C14["optz_sdss_units"] = "AB Mag"
C14["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C14["optz_sdss_flag"] = 0
C14["optz_sdss_source"] = "SDSS-DR9"

C14["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C14["optu_cfht_units"] = "AB Mag"
C14["optu_cfht_effective_wavelength"] = 354*(10**-7)
C14["optu_cfht_flag"] = 0
C14["optu_cfht_source"] = "CFHT"
C14["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C14["optg_ps1_units"] = "AB Mag"
C14["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C14["optg_ps1_flag"] = 0
C14["optg_ps1_source"] = "PS1"
C14["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C14["optr_ps1_units"] = "AB Mag"
C14["optr_ps1_effective_wavelength"] = 617*(10**-7)
C14["optr_ps1_flag"] = 0
C14["optr_ps1_source"] = "PS1"
C14["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C14["opti_ps1_units"] = "AB Mag"
C14["opti_ps1_effective_wavelength"] = 752*(10**-7)
C14["opti_ps1_flag"] = 0
C14["opti_ps1_source"] = "PS1"
C14["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C14["optz_ps1_units"] = "AB Mag"
C14["optz_ps1_effective_wavelength"] = 866*(10**-7)
C14["optz_ps1_flag"] = 0
C14["optz_ps1_source"] = "PS1"

C14["fuv_fdm"] = "n/a"
C14["fuv_units"] = "AB Mag"
C14["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C14["fuv_flag"] = "n/a"
C14["fuv_source"] = "GALEX-DR5(MIS)"
C14["nuv_fdm"] = "n/a"
C14["nuv_units"] = "AB Mag"
C14["nuv_effective_wavelength"] = "n/a" # 2267*(10**-8)
C14["nuv_flag"] = "n/a"
C14["nuv_source"] = "GALEX-DR5(MIS)"

C14["xray_flux"] = "n/a"
C14["xray_fdm"] = "n/a"
C14["xray_units"] = "erg/cm^2/keV/s"
C14["xray_effective_energy"] = "n/a" # 2
C14["xray_flag"] = "n/a"
C14["xray_source"] = "XMM-Newtwon-DR6"

