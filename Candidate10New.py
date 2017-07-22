#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:03:53 2017

This is the data file for CANDIDATE 10.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012) (LAS)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    NUV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (AIS)

***Missing FUV, x-ray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 10

C10 = {}
C10["ra"] = 149.2447
C10["dec"] = 3.1393
C10["z"] = 1.859

C10["mag_error_mirw1"] = 0.184
C10["mag_error_mirw2"] = 0.263
C10["mag_error_mirw3"] = "n/a"
C10["mag_error_mirw4"] = "n/a"
C10["mag_error_nirj"] = 0.138
C10["mag_error_nirk"] = 0.184
C10["mag_error_sdss_u"] = 0.075
C10["mag_error_sdss_g"] = 0.029
C10["mag_error_sdss_r"] = 0.050
C10["mag_error_sdss_i"] = 0.059
C10["mag_error_sdss_z"] = 0.183
C10["mag_error_fuv"] = "n/a"
C10["mag_error_nuv"] = 0.436

C10["E(B-V)_UKIRT_J"] = 0.020
C10["E(B-V)_UKIRT_K"] =  0.009
C10["E(B-V)_SDSS_u"] = 0.121
C10["E(B-V)_SDSS_g"] = 0.094
C10["E(B-V)_SDSS_r"] = 0.065
C10["E(B-V)_SDSS_i"] = 0.048
C10["E(B-V)_SDSS_z"] = 0.036
C10["E(B-V)_PS1_g"] = 0.090
C10["E(B-V)_PS1_r"] = 0.065
C10["E(B-V)_PS1_i"] = 0.048
C10["E(B-V)_PS1_z"] = 0.038

C10["radio_fdm"] = 1.16
C10["radio_units"] = "mJ/beam"
C10["radio_effective_frequency"] = 1400*10**6
C10["radio_flag"] = 1
C10["radio_source"] = "FIRST"

C10["mirw1_fdm"] = 17.510
C10["mirw1_units"] = "Vega Mag"
C10["mirw1_effective_wavelength"] = 3.35*10**(-4)
C10["mirw1_flag"] = 0
C10["mirw1_source"] = "AllWISE"
C10["mirw1_Vega_0magflux"] = 309.540
C10["mirw2_fdm"] = 16.388
C10["mirw2_units"] = "Vega Mag"
C10["mirw2_effective_wavelength"] = 4.6*(10**-4)
C10["mirw2_flag"] = 0
C10["mirw2_source"] = "AllWISE"
C10["mirw2_Vega_0magflux"] = 171.787
C10["mirw3_fdm"] = 11.889
C10["mirw3_units"] = "Vega Mag"
C10["mirw3_effective_wavelength"] = 11.6*(10**-4)
C10["mirw3_flag"] = 1
C10["mirw3_source"] = "AllWISE"
C10["mirw3_Vega_0magflux"] = 31.674
C10["mirw4_fdm"] = 8.841
C10["mirw4_units"] = "Vega Mag"
C10["mirw4_effective_wavelength"] = 22.1*(10**-4)
C10["mirw4_flag"] = 1
C10["mirw4_source"] = "AllWISE"
C10["mirw4_Vega_0magflux"] = 8.363

C10["nirj_fdm"] = 19.325
C10["nirj_units"] = "Vega Mag"
C10["nirj_effective_wavelength"] = 1.248*(10**-4)
C10["nirj_flag"] = 0
C10["nirj_source"] = "UKIDSS-DR9"
C10["nirj_Vega_0magflux"] = 1530
C10["nirk_fdm"] = 18.415
C10["nirk_units"] = "Vega Mag"
C10["nirk_effective_wavelength"] = 2.201*(10**-4)
C10["nirk_flag"] = 0
C10["nirk_source"] = "UKIDSS-DR9"
C10["nirk_Vega_0magflux"] = 631

C10["optu_sdss_fdm"] = 20.773
C10["optu_sdss_units"] = "AB Mag"
C10["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C10["optu_sdss_flag"] = 0
C10["optu_sdss_source"] = "SDSS-DR9"
C10["optg_sdss_fdm"] = 20.760
C10["optg_sdss_units"] = "AB Mag"
C10["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C10["optg_sdss_flag"] = 0
C10["optg_sdss_source"] = "SDSS-DR9"
C10["optr_sdss_fdm"] = 20.745
C10["optr_sdss_units"] = "AB Mag"
C10["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C10["optr_sdss_flag"] = 0
C10["optr_sdss_source"] = "SDSS-DR9"
C10["opti_sdss_fdm"] = 20.416
C10["opti_sdss_units"] = "AB Mag"
C10["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C10["opti_sdss_flag"] = 0
C10["opti_sdss_source"] = "SDSS-DR9"
C10["optz_sdss_fdm"] = 20.297
C10["optz_sdss_units"] = "AB Mag"
C10["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C10["optz_sdss_flag"] = 0
C10["optz_sdss_source"] = "SDSS-DR9"

C10["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C10["optu_cfht_units"] = "AB Mag"
C10["optu_cfht_effective_wavelength"] = 354*(10**-7)
C10["optu_cfht_flag"] = 0
C10["optu_cfht_source"] = "CFHT"
C10["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C10["optg_ps1_units"] = "AB Mag"
C10["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C10["optg_ps1_flag"] = 0
C10["optg_ps1_source"] = "PS1"
C10["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C10["optr_ps1_units"] = "AB Mag"
C10["optr_ps1_effective_wavelength"] = 617*(10**-7)
C10["optr_ps1_flag"] = 0
C10["optr_ps1_source"] = "PS1"
C10["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C10["opti_ps1_units"] = "AB Mag"
C10["opti_ps1_effective_wavelength"] = 752*(10**-7)
C10["opti_ps1_flag"] = 0
C10["opti_ps1_source"] = "PS1"
C10["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C10["optz_ps1_units"] = "AB Mag"
C10["optz_ps1_effective_wavelength"] = 866*(10**-7)
C10["optz_ps1_flag"] = 0
C10["optz_ps1_source"] = "PS1"

C10["fuv_fdm"] = "n/a"
C10["fuv_units"] = "AB Mag"
C10["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C10["fuv_flag"] = "n/a"
C10["fuv_source"] = "GALEX-DR5(MIS)"
C10["nuv_fdm"] = 22.610
C10["nuv_units"] = "AB Mag"
C10["nuv_effective_wavelength"] = 2267*(10**-8)
C10["nuv_flag"] = 0
C10["nuv_source"] = "GALEX-DR5(MIS)"

C10["xray_flux"] = "n/a"
C10["xray_fdm"] = "n/a"
C10["xray_units"] = "erg/cm^2/keV/s"
C10["xray_effective_energy"] = "n/a" # 2
C10["xray_flag"] = "n/a"
C10["xray_source"] = "XMM-Newtwon-DR6"
