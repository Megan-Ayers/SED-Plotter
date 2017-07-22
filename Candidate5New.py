#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 17:47:21 2017

This the data file for CANDIDATE 5.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    *** Missing NIR, NUV, FUV, X-ray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 5

C5 = {}
C5["ra"] = 130.9953
C5["dec"] = 43.7685
C5["z"] = 0.986

C5["mag_error_mirw1"] = 0.046
C5["mag_error_mirw2"] = 0.050
C5["mag_error_mirw3"] = "n/a"
C5["mag_error_mirw4"] = "n/a"
C5["mag_error_nirj"] = "n/a"
C5["mag_error_nirk"] = "n/a"
C5["mag_error_sdss_u"] = 0.062
C5["mag_error_sdss_g"] = 0.023
C5["mag_error_sdss_r"] = 0.022
C5["mag_error_sdss_i"] = 0.037
C5["mag_error_sdss_z"] = 0.125
C5["mag_error_fuv"] = "n/a"
C5["mag_error_nuv"] = "n/a"

C5["E(B-V)_UKIRT_J"] = 0.021
C5["E(B-V)_UKIRT_K"] =  0.009
C5["E(B-V)_SDSS_u"] = 0.128
C5["E(B-V)_SDSS_g"] = 0.099
C5["E(B-V)_SDSS_r"] = 0.069
C5["E(B-V)_SDSS_i"] = 0.051
C5["E(B-V)_SDSS_z"] = 0.038
C5["E(B-V)_PS1_g"] = 0.095
C5["E(B-V)_PS1_r"] = 0.068
C5["E(B-V)_PS1_i"] = 0.051
C5["E(B-V)_PS1_z"] = 0.040

C5["radio_fdm"] = 0.92
C5["radio_units"] = "mJ/beam"
C5["radio_effective_frequency"] = 1400*10**6
C5["radio_flag"] = 1
C5["radio_source"] = "FIRST"

C5["mirw1_fdm"] = 15.740
C5["mirw1_units"] = "Vega Mag"
C5["mirw1_effective_wavelength"] = 3.35*10**(-4)
C5["mirw1_flag"] = 0
C5["mirw1_source"] = "AllWISE"
C5["mirw1_Vega_0magflux"] = 309.540
C5["mirw2_fdm"] = 14.491
C5["mirw2_units"] = "Vega Mag"
C5["mirw2_effective_wavelength"] = 4.6*(10**-4)
C5["mirw2_flag"] = 0
C5["mirw2_source"] = "AllWISE"
C5["mirw2_Vega_0magflux"] = 171.787
C5["mirw3_fdm"] = 12.144
C5["mirw3_units"] = "Vega Mag"
C5["mirw3_effective_wavelength"] = 11.6*(10**-4)
C5["mirw3_flag"] = 1
C5["mirw3_source"] = "AllWISE"
C5["mirw3_Vega_0magflux"] = 31.674
C5["mirw4_fdm"] = 8.675
C5["mirw4_units"] = "Vega Mag"
C5["mirw4_effective_wavelength"] = 22.1*(10**-4)
C5["mirw4_flag"] = 1
C5["mirw4_source"] = "AllWISE"
C5["mirw4_Vega_0magflux"] = 8.363

C5["nirj_fdm"] = "n/a"
C5["nirj_units"] = "Vega Mag"
C5["nirj_effective_wavelength"] = "n/a" # 1.248*(10**-4)
C5["nirj_flag"] = "n/a"
C5["nirj_source"] = "UKIDSS-DR9"
C5["nirj_Vega_0magflux"] = "n/a" # 1530
C5["nirk_fdm"] = "n/a"
C5["nirk_units"] = "Vega Mag"
C5["nirk_effective_wavelength"] = "n/a" # 2.201*(10**-4)
C5["nirk_flag"] = "n/a"
C5["nirk_source"] = "UKIDSS-DR9"
C5["nirk_Vega_0magflux"] = "n/a" # 631

C5["optu_sdss_fdm"] = 20.852
C5["optu_sdss_units"] = "AB Mag"
C5["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C5["optu_sdss_flag"] = 0
C5["optu_sdss_source"] = "SDSS-DR9"
C5["optg_sdss_fdm"] = 20.427
C5["optg_sdss_units"] = "AB Mag"
C5["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C5["optg_sdss_flag"] = 0
C5["optg_sdss_source"] = "SDSS-DR9"
C5["optr_sdss_fdm"] = 20.124
C5["optr_sdss_units"] = "AB Mag"
C5["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C5["optr_sdss_flag"] = 0
C5["optr_sdss_source"] = "SDSS-DR9"
C5["opti_sdss_fdm"] = 20.276
C5["opti_sdss_units"] = "AB Mag"
C5["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C5["opti_sdss_flag"] = 0
C5["opti_sdss_source"] = "SDSS-DR9"
C5["optz_sdss_fdm"] = 20.218
C5["optz_sdss_units"] = "AB Mag"
C5["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C5["optz_sdss_flag"] = 0
C5["optz_sdss_source"] = "SDSS-DR9"

C5["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C5["optu_cfht_units"] = "AB Mag"
C5["optu_cfht_effective_wavelength"] = 354*(10**-7)
C5["optu_cfht_flag"] = 0
C5["optu_cfht_source"] = "CFHT"
C5["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C5["optg_ps1_units"] = "AB Mag"
C5["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C5["optg_ps1_flag"] = 0
C5["optg_ps1_source"] = "PS1"
C5["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C5["optr_ps1_units"] = "AB Mag"
C5["optr_ps1_effective_wavelength"] = 617*(10**-7)
C5["optr_ps1_flag"] = 0
C5["optr_ps1_source"] = "PS1"
C5["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C5["opti_ps1_units"] = "AB Mag"
C5["opti_ps1_effective_wavelength"] = 752*(10**-7)
C5["opti_ps1_flag"] = 0
C5["opti_ps1_source"] = "PS1"
C5["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C5["optz_ps1_units"] = "AB Mag"
C5["optz_ps1_effective_wavelength"] = 866*(10**-7)
C5["optz_ps1_flag"] = 0
C5["optz_ps1_source"] = "PS1"

C5["fuv_fdm"] = "n/a"
C5["fuv_units"] = "AB Mag"
C5["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C5["fuv_flag"] = "n/a"
C5["fuv_source"] = "GALEX-DR5(MIS)"
C5["nuv_fdm"] = "n/a"
C5["nuv_units"] = "AB Mag"
C5["nuv_effective_wavelength"] = "n/a" # 2267*(10**-8)
C5["nuv_flag"] = "n/a"
C5["nuv_source"] = "GALEX-DR5(MIS)"

C5["xray_flux"] = "n/a"
C5["xray_fdm"] = "n/a"
C5["xray_units"] = "erg/cm^2/keV/s"
C5["xray_effective_energy"] = "n/a" # 2
C5["xray_flag"] = "n/a"
C5["xray_source"] = "XMM-Newtwon-DR6"
