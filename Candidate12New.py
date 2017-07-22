#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:19:44 2017

This is the data file for CANDIDATE 12.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012) (LAS)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    NUV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (AIS)
    Xray from XMM-Newton Serendipitous Source Catalogue 3XMM-DR6 (XMM-SSC,2016)

    ***Missing FUV

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 12

C12 = {}
C12["ra"] = 149.6873
C12["dec"] = 1.7192
C12["z"] = 1.350

C12["mag_error_mirw1"] = 0.138
C12["mag_error_mirw2"] = 0.136
C12["mag_error_mirw3"] = "n/a"
C12["mag_error_mirw4"] = "n/a"
C12["mag_error_nirj"] = 0.118
C12["mag_error_nirk"] = 0.197
C12["mag_error_sdss_u"] = 0.064
C12["mag_error_sdss_g"] = 0.025
C12["mag_error_sdss_r"] = 0.026
C12["mag_error_sdss_i"] = 0.033
C12["mag_error_sdss_z"] = 0.110
C12["mag_error_fuv"] = "n/a"
C12["mag_error_nuv"] = 0.205
C12["mag_xray_error"] = 3.31e-15

C12["E(B-V)_UKIRT_J"] = 0.014
C12["E(B-V)_UKIRT_K"] = 0.006
C12["E(B-V)_SDSS_u"] = 0.086
C12["E(B-V)_SDSS_g"] = 0.067
C12["E(B-V)_SDSS_r"] = 0.047
C12["E(B-V)_SDSS_i"] = 0.035
C12["E(B-V)_SDSS_z"] = 0.026
C12["E(B-V)_PS1_g"] = 0.065
C12["E(B-V)_PS1_r"] = 0.046
C12["E(B-V)_PS1_i"] = 0.034
C12["E(B-V)_PS1_z"] = 0.027

C12["radio_fdm"] = 1.02
C12["radio_units"] = "mJ/beam"
C12["radio_effective_frequency"] = 1400*10**6
C12["radio_flag"] = 1
C12["radio_source"] = "FIRST"

C12["mirw1_fdm"] = 17.145
C12["mirw1_units"] = "Vega Mag"
C12["mirw1_effective_wavelength"] = 3.35*10**(-4)
C12["mirw1_flag"] = 0
C12["mirw1_source"] = "AllWISE"
C12["mirw1_Vega_0magflux"] = 309.540
C12["mirw2_fdm"] = 15.674
C12["mirw2_units"] = "Vega Mag"
C12["mirw2_effective_wavelength"] = 4.6*(10**-4)
C12["mirw2_flag"] = 0
C12["mirw2_source"] = "AllWISE"
C12["mirw2_Vega_0magflux"] = 171.787
C12["mirw3_fdm"] = 12.227
C12["mirw3_units"] = "Vega Mag"
C12["mirw3_effective_wavelength"] = 11.6*(10**-4)
C12["mirw3_flag"] = 1
C12["mirw3_source"] = "AllWISE"
C12["mirw3_Vega_0magflux"] = 31.674
C12["mirw4_fdm"] = 8.900
C12["mirw4_units"] = "Vega Mag"
C12["mirw4_effective_wavelength"] = 22.1*(10**-4)
C12["mirw4_flag"] = 1
C12["mirw4_source"] = "AllWISE"
C12["mirw4_Vega_0magflux"] = 8.363

C12["nirj_fdm"] = 19.127
C12["nirj_units"] = "Vega Mag"
C12["nirj_effective_wavelength"] = 1.248*(10**-4)
C12["nirj_flag"] = 0
C12["nirj_source"] = "UKIDSS-DR9"
C12["nirj_Vega_0magflux"] = 1530
C12["nirk_fdm"] = 18.319
C12["nirk_units"] = "Vega Mag"
C12["nirk_effective_wavelength"] = 2.201*(10**-4)
C12["nirk_flag"] = 0
C12["nirk_source"] = "UKIDSS-DR9"
C12["nirk_Vega_0magflux"] = 631

C12["optu_sdss_fdm"] = 20.559
C12["optu_sdss_units"] = "AB Mag"
C12["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C12["optu_sdss_flag"] = 0
C12["optu_sdss_source"] = "SDSS-DR9"
C12["optg_sdss_fdm"] = 20.432
C12["optg_sdss_units"] = "AB Mag"
C12["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C12["optg_sdss_flag"] = 0
C12["optg_sdss_source"] = "SDSS-DR9"
C12["optr_sdss_fdm"] = 20.095
C12["optr_sdss_units"] = "AB Mag"
C12["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C12["optr_sdss_flag"] = 0
C12["optr_sdss_source"] = "SDSS-DR9"
C12["opti_sdss_fdm"] = 20.054
C12["opti_sdss_units"] = "AB Mag"
C12["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C12["opti_sdss_flag"] = 0
C12["opti_sdss_source"] = "SDSS-DR9"
C12["optz_sdss_fdm"] = 19.813 
C12["optz_sdss_units"] = "AB Mag"
C12["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C12["optz_sdss_flag"] = 0
C12["optz_sdss_source"] = "SDSS-DR9"

C12["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C12["optu_cfht_units"] = "AB Mag"
C12["optu_cfht_effective_wavelength"] = 354*(10**-7)
C12["optu_cfht_flag"] = 0
C12["optu_cfht_source"] = "CFHT"
C12["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C12["optg_ps1_units"] = "AB Mag"
C12["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C12["optg_ps1_flag"] = 0
C12["optg_ps1_source"] = "PS1"
C12["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C12["optr_ps1_units"] = "AB Mag"
C12["optr_ps1_effective_wavelength"] = 617*(10**-7)
C12["optr_ps1_flag"] = 0
C12["optr_ps1_source"] = "PS1"
C12["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C12["opti_ps1_units"] = "AB Mag"
C12["opti_ps1_effective_wavelength"] = 752*(10**-7)
C12["opti_ps1_flag"] = 0
C12["opti_ps1_source"] = "PS1"
C12["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C12["optz_ps1_units"] = "AB Mag"
C12["optz_ps1_effective_wavelength"] = 866*(10**-7)
C12["optz_ps1_flag"] = 0
C12["optz_ps1_source"] = "PS1"

C12["fuv_fdm"] = "n/a"
C12["fuv_units"] = "AB Mag"
C12["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C12["fuv_flag"] = "n/a"
C12["fuv_source"] = "GALEX-DR5(MIS)"
C12["nuv_fdm"] = 21.460
C12["nuv_units"] = "AB Mag"
C12["nuv_effective_wavelength"] = 2267*(10**-8)
C12["nuv_flag"] = 0
C12["nuv_source"] = "GALEX-DR5(MIS)"

C12["xray_flux"] = 2.3964e-14
C12["xray_fdm"] = 5.853e-15
C12["xray_units"] = "erg/cm^2/keV/s"
C12["xray_effective_energy"] = 2
C12["xray_flag"] = 0
C12["xray_source"] = "XMM-Newtwon-DR6"
