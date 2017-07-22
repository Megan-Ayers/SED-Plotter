#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:49:37 2017

This is the data file for CANDIDATE 21.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    UV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011)
        MIS (Medium-depth Imaging Survey)
    X-ray from XMM-Newton Serendipitous Source Catalogue 3XMM-DR6
    (XMM-SSC, 2016)

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 21

C21 = {}
C21["ra"] = 242.8039
C21["dec"] = 54.05853
C21["z"] = 0.960

C21["mag_error_mirw1"] = 0.034
C21["mag_error_mirw2"] = 0.035
C21["mag_error_mirw3"] = 0.118
C21["mag_error_mirw4"] = 0.336
C21["mag_error_nirj"] = 0.012
C21["mag_error_nirk"] = 0.012
C21["mag_error_sdss_u"] = 0.046
C21["mag_error_sdss_g"] = 0.017
C21["mag_error_sdss_r"] = 0.018
C21["mag_error_sdss_i"] = 0.024
C21["mag_error_sdss_z"] = 0.090
C21["mag_error_fuv"] = 0.128
C21["mag_error_nuv"] = 0.049
C21["mag_xray_error"] = 1.47e-14

C21["E(B-V)_UKIRT_J"] = 0.008
C21["E(B-V)_UKIRT_K"] = 0.003
C21["E(B-V)_SDSS_u"] = 0.047
C21["E(B-V)_SDSS_g"] = 0.037
C21["E(B-V)_SDSS_r"] = 0.026
C21["E(B-V)_SDSS_i"] = 0.019
C21["E(B-V)_SDSS_z"] = 0.014
C21["E(B-V)_PS1_g"] = 0.035
C21["E(B-V)_PS1_r"] = 0.025
C21["E(B-V)_PS1_i"] = 0.019
C21["E(B-V)_PS1_z"] = 0.015

C21["radio_fdm"] = 0.92
C21["radio_units"] = "mJ/beam"
C21["radio_effective_frequency"] = 1400*10**6
C21["radio_flag"] = 1
C21["radio_source"] = "FIRST"

C21["mirw1_fdm"] = 15.849
C21["mirw1_units"] = "Vega Mag"
C21["mirw1_effective_wavelength"] = 3.35*10**(-4)
C21["mirw1_flag"] = 0 
C21["mirw1_source"] = "AllWISE"
C21["mirw1_Vega_0magflux"] = 309.540
C21["mirw2_fdm"] = 14.623
C21["mirw2_units"] = "Vega Mag"
C21["mirw2_effective_wavelength"] = 4.6*(10**-4)
C21["mirw2_flag"] = 0
C21["mirw2_source"] = "AllWISE"
C21["mirw2_Vega_0magflux"] = 171.787
C21["mirw3_fdm"] = 11.834
C21["mirw3_units"] = "Vega Mag"
C21["mirw3_effective_wavelength"] = 11.6*(10**-4)
C21["mirw3_flag"] = 0
C21["mirw3_source"] = "AllWISE"
C21["mirw3_Vega_0magflux"] = 31.674
C21["mirw4_fdm"] = 9.465
C21["mirw4_units"] = "Vega Mag"
C21["mirw4_effective_wavelength"] = 22.1*(10**-4)
C21["mirw4_flag"] = 0
C21["mirw4_source"] = "AllWISE"
C21["mirw4_Vega_0magflux"] = 8.363

C21["nirj_fdm"] = 18.380
C21["nirj_units"] = "Vega Mag"
C21["nirj_effective_wavelength"] = 1.248*(10**-4)
C21["nirj_flag"] = 0
C21["nirj_source"] = "UKIDSS-DR9"
C21["nirj_Vega_0magflux"] = 1530
C21["nirk_fdm"] = 17.431
C21["nirk_units"] = "Vega Mag"
C21["nirk_effective_wavelength"] = 2.201*(10**-4)
C21["nirk_flag"] = 0
C21["nirk_source"] = "UKIDSS-DR9"
C21["nirk_Vega_0magflux"] = 631

C21["optu_sdss_fdm"] = 20.190
C21["optu_sdss_units"] = "AB Mag"
C21["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C21["optu_sdss_flag"] = 0
C21["optu_sdss_source"] = "SDSS-DR9"
C21["optg_sdss_fdm"] = 19.956
C21["optg_sdss_units"] = "AB Mag"
C21["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C21["optg_sdss_flag"] = 0
C21["optg_sdss_source"] = "SDSS-DR9"
C21["optr_sdss_fdm"] = 19.836
C21["optr_sdss_units"] = "AB Mag"
C21["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C21["optr_sdss_flag"] = 0
C21["optr_sdss_source"] = "SDSS-DR9"
C21["opti_sdss_fdm"] = 19.949
C21["opti_sdss_units"] = "AB Mag"
C21["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C21["opti_sdss_flag"] = 0
C21["opti_sdss_source"] = "SDSS-DR9"
C21["optz_sdss_fdm"] = 20.046
C21["optz_sdss_units"] = "AB Mag"
C21["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C21["optz_sdss_flag"] = 0
C21["optz_sdss_source"] = "SDSS-DR9"

C21["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C21["optu_cfht_units"] = "AB Mag"
C21["optu_cfht_effective_wavelength"] = 354*(10**-7)
C21["optu_cfht_flag"] = 0
C21["optu_cfht_source"] = "CFHT"
C21["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C21["optg_ps1_units"] = "AB Mag"
C21["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C21["optg_ps1_flag"] = 0
C21["optg_ps1_source"] = "PS1"
C21["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C21["optr_ps1_units"] = "AB Mag"
C21["optr_ps1_effective_wavelength"] = 617*(10**-7)
C21["optr_ps1_flag"] = 0
C21["optr_ps1_source"] = "PS1"
C21["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C21["opti_ps1_units"] = "AB Mag"
C21["opti_ps1_effective_wavelength"] = 752*(10**-7)
C21["opti_ps1_flag"] = 0
C21["opti_ps1_source"] = "PS1"
C21["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C21["optz_ps1_units"] = "AB Mag"
C21["optz_ps1_effective_wavelength"] = 866*(10**-7)
C21["optz_ps1_flag"] = 0
C21["optz_ps1_source"] = "PS1"

C21["fuv_fdm"] = 21.519
C21["fuv_units"] = "AB Mag"
C21["fuv_effective_wavelength"] = 1516*10**-8
C21["fuv_flag"] = 0
C21["fuv_source"] = "GALEX-DR5(MIS)"
C21["nuv_fdm"] = 20.526
C21["nuv_units"] = "AB Mag"
C21["nuv_effective_wavelength"] = 2267*(10**-8)
C21["nuv_flag"] = 0
C21["nuv_source"] = "GALEX-DR5(MIS)"

C21["xray_flux"] = 1.0978e-13
C21["xray_fdm"] = 2.681e-14
C21["xray_units"] = "erg/cm^2/keV/s"
C21["xray_effective_energy"] = 2
C21["xray_flag"] = 0
C21["xray_source"] = "XMM-Newtwon-DR6"
