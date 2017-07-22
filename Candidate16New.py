#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:03:20 2017

This is the data file for CANDIDATE 16.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR_K from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012) (DXS)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)

    ***Missing NIR_J, UV, x-ray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 16

C16 = {}
C16["ra"] = 163.2331
C16["dec"] = 58.8626
C16["z"] = 2.169

C16["mag_error_mirw1"] = 0.068
C16["mag_error_mirw2"] = 0.088
C16["mag_error_mirw3"] = 0.303
C16["mag_error_mirw4"] = 0.308
C16["mag_error_nirj"] = "n/a"
C16["mag_error_nirk"] = 0.010
C16["mag_error_sdss_u"] = 0.050
C16["mag_error_sdss_g"] = 0.017
C16["mag_error_sdss_r"] = 0.020
C16["mag_error_sdss_i"] = 0.024
C16["mag_error_sdss_z"] = 0.057
C16["mag_error_fuv"] = "n/a"
C16["mag_error_nuv"] = "n/a"

C16["E(B-V)_UKIRT_J"] = 0.007
C16["E(B-V)_UKIRT_K"] = 0.003
C16["E(B-V)_SDSS_u"] = 0.044
C16["E(B-V)_SDSS_g"] = 0.034
C16["E(B-V)_SDSS_r"] = 0.023
C16["E(B-V)_SDSS_i"] = 0.017
C16["E(B-V)_SDSS_z"] = 0.013
C16["E(B-V)_PS1_g"] = 0.033
C16["E(B-V)_PS1_r"] = 0.023
C16["E(B-V)_PS1_i"] = 0.017
C16["E(B-V)_PS1_z"] = 0.014

C16["radio_fdm"] = 1.03
C16["radio_units"] = "mJ/beam"
C16["radio_effective_frequency"] = 1400*10**6
C16["radio_flag"] = 1
C16["radio_source"] = "FIRST"

C16["mirw1_fdm"] = 16.371
C16["mirw1_units"] = "Vega Mag"
C16["mirw1_effective_wavelength"] = 3.35*10**(-4)
C16["mirw1_flag"] = 0
C16["mirw1_source"] = "AllWISE"
C16["mirw1_Vega_0magflux"] = 309.540
C16["mirw2_fdm"] = 15.263
C16["mirw2_units"] = "Vega Mag"
C16["mirw2_effective_wavelength"] = 4.6*(10**-4)
C16["mirw2_flag"] = 0
C16["mirw2_source"] = "AllWISE"
C16["mirw2_Vega_0magflux"] = 171.787
C16["mirw3_fdm"] = 11.912
C16["mirw3_units"] = "Vega Mag"
C16["mirw3_effective_wavelength"] = 11.6*(10**-4)
C16["mirw3_flag"] = 0
C16["mirw3_source"] = "AllWISE"
C16["mirw3_Vega_0magflux"] = 31.674
C16["mirw4_fdm"] = 8.574
C16["mirw4_units"] = "Vega Mag"
C16["mirw4_effective_wavelength"] = 22.1*(10**-4)
C16["mirw4_flag"] = 0
C16["mirw4_source"] = "AllWISE"
C16["mirw4_Vega_0magflux"] = 8.363

C16["nirj_fdm"] = "n/a"
C16["nirj_units"] = "Vega Mag"
C16["nirj_effective_wavelength"] = "n/a" # 1.248*(10**-4)
C16["nirj_flag"] = "n/a"
C16["nirj_source"] = "UKIDSS-DR9"
C16["nirj_Vega_0magflux"] = "n/a" # 1530
C16["nirk_fdm"] = 17.116
C16["nirk_units"] = "Vega Mag"
C16["nirk_effective_wavelength"] = 2.201*(10**-4)
C16["nirk_flag"] = 0
C16["nirk_source"] = "UKIDSS-DR9"
C16["nirk_Vega_0magflux"] = 631

C16["optu_sdss_fdm"] = 20.095
C16["optu_sdss_units"] = "AB Mag"
C16["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C16["optu_sdss_flag"] = 0
C16["optu_sdss_source"] = "SDSS-DR9"
C16["optg_sdss_fdm"] = 19.849
C16["optg_sdss_units"] = "AB Mag"
C16["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C16["optg_sdss_flag"] = 0
C16["optg_sdss_source"] = "SDSS-DR9"
C16["optr_sdss_fdm"] = 19.770
C16["optr_sdss_units"] = "AB Mag"
C16["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C16["optr_sdss_flag"] = 0
C16["optr_sdss_source"] = "SDSS-DR9"
C16["opti_sdss_fdm"] = 19.604
C16["opti_sdss_units"] = "AB Mag"
C16["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C16["opti_sdss_flag"] = 0
C16["opti_sdss_source"] = "SDSS-DR9"
C16["optz_sdss_fdm"] = 19.265
C16["optz_sdss_units"] = "AB Mag"
C16["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C16["optz_sdss_flag"] = 0
C16["optz_sdss_source"] = "SDSS-DR9"

C16["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C16["optu_cfht_units"] = "AB Mag"
C16["optu_cfht_effective_wavelength"] = 354*(10**-7)
C16["optu_cfht_flag"] = 0
C16["optu_cfht_source"] = "CFHT"
C16["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C16["optg_ps1_units"] = "AB Mag"
C16["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C16["optg_ps1_flag"] = 0
C16["optg_ps1_source"] = "PS1"
C16["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C16["optr_ps1_units"] = "AB Mag"
C16["optr_ps1_effective_wavelength"] = 617*(10**-7)
C16["optr_ps1_flag"] = 0
C16["optr_ps1_source"] = "PS1"
C16["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C16["opti_ps1_units"] = "AB Mag"
C16["opti_ps1_effective_wavelength"] = 752*(10**-7)
C16["opti_ps1_flag"] = 0
C16["opti_ps1_source"] = "PS1"
C16["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C16["optz_ps1_units"] = "AB Mag"
C16["optz_ps1_effective_wavelength"] = 866*(10**-7)
C16["optz_ps1_flag"] = 0
C16["optz_ps1_source"] = "PS1"

C16["fuv_fdm"] = "n/a"
C16["fuv_units"] = "AB Mag"
C16["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C16["fuv_flag"] = "n/a"
C16["fuv_source"] = "GALEX-DR5(MIS)"
C16["nuv_fdm"] = "n/a"
C16["nuv_units"] = "AB Mag"
C16["nuv_effective_wavelength"] = "n/a" # 2267*(10**-8)
C16["nuv_flag"] = "n/a"
C16["nuv_source"] = "GALEX-DR5(MIS)"

C16["xray_flux"] = "n/a"
C16["xray_fdm"] = "n/a"
C16["xray_units"] = "erg/cm^2/keV/s"
C16["xray_effective_energy"] = "n/a" # 2
C16["xray_flag"] = "n/a"
C16["xray_source"] = "XMM-Newtwon-DR6"

