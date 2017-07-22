#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:11:01 2017

This is the data file for CANDIDATE 11.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012) (LAS)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    UV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (MIS)
        ** r = 1.313 **
        
***Missing x-ray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 11

C11 = {}
C11["ra"] = 149.9400
C11["dec"] = 1.5090
C11["z"] = 1.106

C11["mag_error_mirw1"] = 0.055
C11["mag_error_mirw2"] = 0.075
C11["mag_error_mirw3"] = 0.364
C11["mag_error_mirw4"] = 0.518
C11["mag_error_nirj"] = 0.116
C11["mag_error_nirk"] = 0.091
C11["mag_error_sdss_u"] = 0.060
C11["mag_error_sdss_g"] = 0.022
C11["mag_error_sdss_r"] = 0.026
C11["mag_error_sdss_i"] = 0.037
C11["mag_error_sdss_z"] = 0.114
C11["mag_error_fuv"] = 0.403
C11["mag_error_nuv"] = 0.180

C11["E(B-V)_UKIRT_J"] = 0.014
C11["E(B-V)_UKIRT_K"] = 0.006
C11["E(B-V)_SDSS_u"] = 0.084
C11["E(B-V)_SDSS_g"] = 0.065
C11["E(B-V)_SDSS_r"] = 0.045
C11["E(B-V)_SDSS_i"] = 0.034
C11["E(B-V)_SDSS_z"] = 0.025
C11["E(B-V)_PS1_g"] = 0.063
C11["E(B-V)_PS1_r"] = 0.045
C11["E(B-V)_PS1_i"] = 0.033
C11["E(B-V)_PS1_z"] = 0.026

C11["radio_fdm"] = 1.03
C11["radio_units"] = "mJ/beam"
C11["radio_effective_frequency"] = 1400*10**6
C11["radio_flag"] = 1
C11["radio_source"] = "FIRST"

C11["mirw1_fdm"] = 15.901
C11["mirw1_units"] = "Vega Mag"
C11["mirw1_effective_wavelength"] = 3.35*10**(-4)
C11["mirw1_flag"] = 0
C11["mirw1_source"] = "AllWISE"
C11["mirw1_Vega_0magflux"] = 309.540
C11["mirw2_fdm"] = 14.907
C11["mirw2_units"] = "Vega Mag"
C11["mirw2_effective_wavelength"] = 4.6*(10**-4)
C11["mirw2_flag"] = 0
C11["mirw2_source"] = "AllWISE"
C11["mirw2_Vega_0magflux"] = 171.787
C11["mirw3_fdm"] = 12.027
C11["mirw3_units"] = "Vega Mag"
C11["mirw3_effective_wavelength"] = 11.6*(10**-4)
C11["mirw3_flag"] = 0
C11["mirw3_source"] = "AllWISE"
C11["mirw3_Vega_0magflux"] = 31.674
C11["mirw4_fdm"] = 8.949
C11["mirw4_units"] = "Vega Mag"
C11["mirw4_effective_wavelength"] = 22.1*(10**-4)
C11["mirw4_flag"] = 0
C11["mirw4_source"] = "AllWISE"
C11["mirw4_Vega_0magflux"] = 8.363

C11["nirj_fdm"] = 18.923
C11["nirj_units"] = "Vega Mag"
C11["nirj_effective_wavelength"] = 1.248*(10**-4)
C11["nirj_flag"] = 0
C11["nirj_source"] = "UKIDSS-DR9"
C11["nirj_Vega_0magflux"] = 1530
C11["nirk_fdm"] = 17.371
C11["nirk_units"] = "Vega Mag"
C11["nirk_effective_wavelength"] = 2.201*(10**-4)
C11["nirk_flag"] = 0
C11["nirk_source"] = "UKIDSS-DR9"
C11["nirk_Vega_0magflux"] = 631

C11["optu_sdss_fdm"] = 20.726
C11["optu_sdss_units"] = "AB Mag"
C11["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C11["optu_sdss_flag"] = 0
C11["optu_sdss_source"] = "SDSS-DR9"
C11["optg_sdss_fdm"] = 20.421
C11["optg_sdss_units"] = "AB Mag"
C11["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C11["optg_sdss_flag"] = 0
C11["optg_sdss_source"] = "SDSS-DR9"
C11["optr_sdss_fdm"] = 19.983
C11["optr_sdss_units"] = "AB Mag"
C11["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C11["optr_sdss_flag"] = 0
C11["optr_sdss_source"] = "SDSS-DR9"
C11["opti_sdss_fdm"] = 20.062
C11["opti_sdss_units"] = "AB Mag"
C11["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C11["opti_sdss_flag"] = 0
C11["opti_sdss_source"] = "SDSS-DR9"
C11["optz_sdss_fdm"] = 20.023
C11["optz_sdss_units"] = "AB Mag"
C11["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C11["optz_sdss_flag"] = 0
C11["optz_sdss_source"] = "SDSS-DR9"

C11["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C11["optu_cfht_units"] = "AB Mag"
C11["optu_cfht_effective_wavelength"] = 354*(10**-7)
C11["optu_cfht_flag"] = 0
C11["optu_cfht_source"] = "CFHT"
C11["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C11["optg_ps1_units"] = "AB Mag"
C11["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C11["optg_ps1_flag"] = 0
C11["optg_ps1_source"] = "PS1"
C11["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C11["optr_ps1_units"] = "AB Mag"
C11["optr_ps1_effective_wavelength"] = 617*(10**-7)
C11["optr_ps1_flag"] = 0
C11["optr_ps1_source"] = "PS1"
C11["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C11["opti_ps1_units"] = "AB Mag"
C11["opti_ps1_effective_wavelength"] = 752*(10**-7)
C11["opti_ps1_flag"] = 0
C11["opti_ps1_source"] = "PS1"
C11["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C11["optz_ps1_units"] = "AB Mag"
C11["optz_ps1_effective_wavelength"] = 866*(10**-7)
C11["optz_ps1_flag"] = 0
C11["optz_ps1_source"] = "PS1"

C11["fuv_fdm"] = 23.740
C11["fuv_units"] = "AB Mag"
C11["fuv_effective_wavelength"] = 1516*10**-8
C11["fuv_flag"] = 0
C11["fuv_source"] = "GALEX-DR5(MIS)"
C11["nuv_fdm"] = 21.368
C11["nuv_units"] = "AB Mag"
C11["nuv_effective_wavelength"] = 2267*(10**-8)
C11["nuv_flag"] = 0
C11["nuv_source"] = "GALEX-DR5(MIS)"

C11["xray_flux"] = "n/a"
C11["xray_fdm"] = "n/a"
C11["xray_units"] = "erg/cm^2/keV/s"
C11["xray_effective_energy"] = "n/a" # 2
C11["xray_flag"] = "n/a"
C11["xray_source"] = "XMM-Newtwon-DR6"

