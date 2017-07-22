#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:53:28 2017

This is the data file for CANDIDATE 22.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    NUV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011)
        AIS (All-sky Imaging Survey) (out of 65,266,291 sources)
        
    ***Missing FUV and x-ray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 22

C22 = {}
C22["ra"] = 243.5676
C22["dec"] = 54.9741
C22["z"] = 1.267

C22["mag_error_mirw1"] = 0.036
C22["mag_error_mirw2"] = 0.040
C22["mag_error_mirw3"] = 0.152
C22["mag_error_mirw4"] = 0.251
C22["mag_error_nirj"] = 0.016
C22["mag_error_nirk"] = 0.016
C22["mag_error_sdss_u"] = 0.058
C22["mag_error_sdss_g"] = 0.020
C22["mag_error_sdss_r"] = 0.018
C22["mag_error_sdss_i"] = 0.022
C22["mag_error_sdss_z"] = 0.079
C22["mag_error_fuv"] = "n/a"
C22["mag_error_nuv"] = 0.108

C22["E(B-V)_UKIRT_J"] = 0.006
C22["E(B-V)_UKIRT_K"] = 0.002
C22["E(B-V)_SDSS_u"] = 0.035
C22["E(B-V)_SDSS_g"] = 0.027
C22["E(B-V)_SDSS_r"] = 0.019
C22["E(B-V)_SDSS_i"] = 0.014
C22["E(B-V)_SDSS_z"] = 0.010
C22["E(B-V)_PS1_g"] = 0.026
C22["E(B-V)_PS1_r"] = 0.019
C22["E(B-V)_PS1_i"] = 0.014
C22["E(B-V)_PS1_z"] = 0.011

C22["radio_fdm"] = 0.99
C22["radio_units"] = "mJ/beam"
C22["radio_effective_frequency"] = 1400*10**6
C22["radio_flag"] = 1
C22["radio_source"] = "FIRST"

C22["mirw1_fdm"] = 16.043
C22["mirw1_units"] = "Vega Mag"
C22["mirw1_effective_wavelength"] = 3.35*10**(-4)
C22["mirw1_flag"] = 0
C22["mirw1_source"] = "AllWISE"
C22["mirw1_Vega_0magflux"] = 309.540
C22["mirw2_fdm"] = 14.892
C22["mirw2_units"] = "Vega Mag"
C22["mirw2_effective_wavelength"] = 4.6*(10**-4)
C22["mirw2_flag"] = 0
C22["mirw2_source"] = "AllWISE"
C22["mirw2_Vega_0magflux"] = 171.787
C22["mirw3_fdm"] = 12.176
C22["mirw3_units"] = "Vega Mag"
C22["mirw3_effective_wavelength"] = 11.6*(10**-4)
C22["mirw3_flag"] = 0
C22["mirw3_source"] = "AllWISE"
C22["mirw3_Vega_0magflux"] = 31.674
C22["mirw4_fdm"] = 9.080
C22["mirw4_units"] = "Vega Mag"
C22["mirw4_effective_wavelength"] = 22.1*(10**-4)
C22["mirw4_flag"] = 0
C22["mirw4_source"] = "AllWISE"
C22["mirw4_Vega_0magflux"] = 8.363

C22["nirj_fdm"] = 18.775
C22["nirj_units"] = "Vega Mag"
C22["nirj_effective_wavelength"] = 1.248*(10**-4)
C22["nirj_flag"] = 0
C22["nirj_source"] = "UKIDSS-DR9"
C22["nirj_Vega_0magflux"] = 1530
C22["nirk_fdm"] = 17.611
C22["nirk_units"] = "Vega Mag"
C22["nirk_effective_wavelength"] = 2.201*(10**-4)
C22["nirk_flag"] = 0
C22["nirk_source"] = "UKIDSS-DR9"
C22["nirk_Vega_0magflux"] = 631

C22["optu_sdss_fdm"] = 20.51
C22["optu_sdss_units"] = "AB Mag"
C22["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C22["optu_sdss_flag"] = 0
C22["optu_sdss_source"] = "SDSS-DR9"
C22["optg_sdss_fdm"] = 20.342
C22["optg_sdss_units"] = "AB Mag"
C22["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C22["optg_sdss_flag"] = 0
C22["optg_sdss_source"] = "SDSS-DR9"
C22["optr_sdss_fdm"] = 19.895
C22["optr_sdss_units"] = "AB Mag"
C22["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C22["optr_sdss_flag"] = 0
C22["optr_sdss_source"] = "SDSS-DR9"
C22["opti_sdss_fdm"] = 19.897
C22["opti_sdss_units"] = "AB Mag"
C22["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C22["opti_sdss_flag"] = 0
C22["opti_sdss_source"] = "SDSS-DR9"
C22["optz_sdss_fdm"] = 19.879
C22["optz_sdss_units"] = "AB Mag"
C22["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C22["optz_sdss_flag"] = 0
C22["optz_sdss_source"] = "SDSS-DR9"

C22["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C22["optu_cfht_units"] = "AB Mag"
C22["optu_cfht_effective_wavelength"] = 354*(10**-7)
C22["optu_cfht_flag"] = 0
C22["optu_cfht_source"] = "CFHT"
C22["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C22["optg_ps1_units"] = "AB Mag"
C22["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C22["optg_ps1_flag"] = 0
C22["optg_ps1_source"] = "PS1"
C22["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C22["optr_ps1_units"] = "AB Mag"
C22["optr_ps1_effective_wavelength"] = 617*(10**-7)
C22["optr_ps1_flag"] = 0
C22["optr_ps1_source"] = "PS1"
C22["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C22["opti_ps1_units"] = "AB Mag"
C22["opti_ps1_effective_wavelength"] = 752*(10**-7)
C22["opti_ps1_flag"] = 0
C22["opti_ps1_source"] = "PS1"
C22["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C22["optz_ps1_units"] = "AB Mag"
C22["optz_ps1_effective_wavelength"] = 866*(10**-7)
C22["optz_ps1_flag"] = 0
C22["optz_ps1_source"] = "PS1"

C22["fuv_fdm"] = "n/a"
C22["fuv_units"] = "AB Mag"
C22["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C22["fuv_flag"] = "n/a"
C22["fuv_source"] = "GALEX-DR5(MIS)"
C22["nuv_fdm"] = 20.856
C22["nuv_units"] = "AB Mag"
C22["nuv_effective_wavelength"] = 2267*(10**-8)
C22["nuv_flag"] = 0
C22["nuv_source"] = "GALEX-DR5(MIS)"

C22["xray_flux"] = "n/a"
C22["xray_fdm"] = "n/a"
C22["xray_units"] = "erg/cm^2/keV/s"
C22["xray_effective_energy"] = "n/a" # 2
C22["xray_flag"] = "n/a"
C22["xray_source"] = "XMM-Newtwon-DR6"
