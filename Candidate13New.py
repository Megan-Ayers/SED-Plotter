#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:30:25 2017

This is the data file for CANDIDATE 13.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012) (LAS)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    UV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (AIS)
    
    ***Missing xray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 13

C13 = {}
C13["ra"] = 150.9191
C13["dec"] = 3.3880
C13["z"] = 0.719

C13["mag_error_mirw1"] = 0.036
C13["mag_error_mirw2"] = 0.040
C13["mag_error_mirw3"] = 0.354
C13["mag_error_mirw4"] = "n/a"
C13["mag_error_nirj"] = 0.041
C13["mag_error_nirk"] = 0.038
C13["mag_error_sdss_u"] = 0.032
C13["mag_error_sdss_g"] = 0.012
C13["mag_error_sdss_r"] = 0.014
C13["mag_error_sdss_i"] = 0.016
C13["mag_error_sdss_z"] = 0.039
C13["mag_error_fuv"] = 0.181
C13["mag_error_nuv"] = 0.111

C13["E(B-V)_UKIRT_J"] = 0.014
C13["E(B-V)_UKIRT_K"] = 0.006
C13["E(B-V)_SDSS_u"] = 0.083
C13["E(B-V)_SDSS_g"] = 0.065
C13["E(B-V)_SDSS_r"] = 0.045
C13["E(B-V)_SDSS_i"] = 0.033
C13["E(B-V)_SDSS_z"] = 0.025
C13["E(B-V)_PS1_g"] = 0.062
C13["E(B-V)_PS1_r"] = 0.045
C13["E(B-V)_PS1_i"] = 0.033
C13["E(B-V)_PS1_z"] = 0.026

C13["radio_fdm"] = 1.00
C13["radio_units"] = "mJ/beam"
C13["radio_effective_frequency"] = 1400*10**6
C13["radio_flag"] = 1
C13["radio_source"] = "FIRST"

C13["mirw1_fdm"] = 15.107
C13["mirw1_units"] = "Vega Mag"
C13["mirw1_effective_wavelength"] = 3.35*10**(-4)
C13["mirw1_flag"] = 0
C13["mirw1_source"] = "AllWISE"
C13["mirw1_Vega_0magflux"] = 309.540
C13["mirw2_fdm"] = 14.022
C13["mirw2_units"] = "Vega Mag"
C13["mirw2_effective_wavelength"] = 4.6*(10**-4)
C13["mirw2_flag"] = 0
C13["mirw2_source"] = "AllWISE"
C13["mirw2_Vega_0magflux"] = 171.787
C13["mirw3_fdm"] = 12.106
C13["mirw3_units"] = "Vega Mag"
C13["mirw3_effective_wavelength"] = 11.6*(10**-4)
C13["mirw3_flag"] = 0
C13["mirw3_source"] = "AllWISE"
C13["mirw3_Vega_0magflux"] = 31.674
C13["mirw4_fdm"] = 8.448
C13["mirw4_units"] = "Vega Mag"
C13["mirw4_effective_wavelength"] = 22.1*(10**-4)
C13["mirw4_flag"] = 1
C13["mirw4_source"] = "AllWISE"
C13["mirw4_Vega_0magflux"] = 8.363

C13["nirj_fdm"] = 18.139
C13["nirj_units"] = "Vega Mag"
C13["nirj_effective_wavelength"] = 1.248*(10**-4)
C13["nirj_flag"] = 0
C13["nirj_source"] = "UKIDSS-DR9"
C13["nirj_Vega_0magflux"] = 1530
C13["nirk_fdm"] = 16.754
C13["nirk_units"] = "Vega Mag"
C13["nirk_effective_wavelength"] = 2.201*(10**-4)
C13["nirk_flag"] = 0
C13["nirk_source"] = "UKIDSS-DR9"
C13["nirk_Vega_0magflux"] = 631

C13["optu_sdss_fdm"] = 19.680
C13["optu_sdss_units"] = "AB Mag"
C13["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C13["optu_sdss_flag"] = 0
C13["optu_sdss_source"] = "SDSS-DR9"
C13["optg_sdss_fdm"] = 19.392
C13["optg_sdss_units"] = "AB Mag"
C13["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C13["optg_sdss_flag"] = 0
C13["optg_sdss_source"] = "SDSS-DR9"
C13["optr_sdss_fdm"] = 19.243
C13["optr_sdss_units"] = "AB Mag"
C13["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C13["optr_sdss_flag"] = 0
C13["optr_sdss_source"] = "SDSS-DR9"
C13["opti_sdss_fdm"] = 19.152
C13["opti_sdss_units"] = "AB Mag"
C13["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C13["opti_sdss_flag"] = 0
C13["opti_sdss_source"] = "SDSS-DR9"
C13["optz_sdss_fdm"] = 19.010
C13["optz_sdss_units"] = "AB Mag"
C13["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C13["optz_sdss_flag"] = 0
C13["optz_sdss_source"] = "SDSS-DR9"

C13["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C13["optu_cfht_units"] = "AB Mag"
C13["optu_cfht_effective_wavelength"] = 354*(10**-7)
C13["optu_cfht_flag"] = 0
C13["optu_cfht_source"] = "CFHT"
C13["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C13["optg_ps1_units"] = "AB Mag"
C13["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C13["optg_ps1_flag"] = 0
C13["optg_ps1_source"] = "PS1"
C13["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C13["optr_ps1_units"] = "AB Mag"
C13["optr_ps1_effective_wavelength"] = 617*(10**-7)
C13["optr_ps1_flag"] = 0
C13["optr_ps1_source"] = "PS1"
C13["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C13["opti_ps1_units"] = "AB Mag"
C13["opti_ps1_effective_wavelength"] = 752*(10**-7)
C13["opti_ps1_flag"] = 0
C13["opti_ps1_source"] = "PS1"
C13["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C13["optz_ps1_units"] = "AB Mag"
C13["optz_ps1_effective_wavelength"] = 866*(10**-7)
C13["optz_ps1_flag"] = 0
C13["optz_ps1_source"] = "PS1"

C13["fuv_fdm"] = 20.854
C13["fuv_units"] = "AB Mag"
C13["fuv_effective_wavelength"] = 1516*10**-8
C13["fuv_flag"] = 0
C13["fuv_source"] = "GALEX-DR5(AIS)"
C13["nuv_fdm"] = 20.140
C13["nuv_units"] = "AB Mag"
C13["nuv_effective_wavelength"] = 2267*(10**-8)
C13["nuv_flag"] = 0
C13["nuv_source"] = "GALEX-DR5(AIS)"

C13["xray_flux"] = "n/a"
C13["xray_fdm"] = "n/a"
C13["xray_units"] = "erg/cm^2/keV/s"
C13["xray_effective_energy"] = "n/a" # 2
C13["xray_flag"] = "n/a"
C13["xray_source"] = "XMM-Newtwon-DR6"

