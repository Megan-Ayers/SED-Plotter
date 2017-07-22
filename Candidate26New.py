#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 15:18:36 2017

This is the data file for CANDIDATE 26.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    Radio from http://sundog.stsci.edu/cgi-bin/searchfirst **r = 9.6 arcsecs**
    MIR from AllWISE Data Release (Cutri+ 2013)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    UV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (MIS)
    
    ***Missing NIR, x-ray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 26

C26 = {}
C26["ra"] = 351.5679
C26["dec"] = -1.6795
C26["z"] = 1.156 

C26["mag_error_radio"] = 0.178

C26["mag_error_mirw1"] = 0.033
C26["mag_error_mirw2"] = 0.034
C26["mag_error_mirw3"] = 0.121
C26["mag_error_mirw4"] = 0.288
C26["mag_error_nirj"] = "n/a"
C26["mag_error_nirk"] = "n/a"
C26["mag_error_sdss_u"] = 0.023
C26["mag_error_sdss_g"] = 0.009
C26["mag_error_sdss_r"] = 0.009
C26["mag_error_sdss_i"] = 0.012
C26["mag_error_sdss_z"] = 0.037
C26["mag_error_fuv"] = 0.083
C26["mag_error_nuv"] = 0.026

C26["E(B-V)_UKIRT_J"] = 0.043
C26["E(B-V)_UKIRT_K"] = 0.019
C26["E(B-V)_SDSS_u"] = 0.260
C26["E(B-V)_SDSS_g"] = 0.202
C26["E(B-V)_SDSS_r"] = 0.140
C26["E(B-V)_SDSS_i"] = 0.104
C26["E(B-V)_SDSS_z"] = 0.077
C26["E(B-V)_PS1_g"] = 0.194
C26["E(B-V)_PS1_r"] = 0.139
C26["E(B-V)_PS1_i"] = 0.103
C26["E(B-V)_PS1_z"] = 0.081

C26["radio_fdm"] = 31.02 # 25.80 = peak, int. flux = 31.02 mJy
C26["radio_units"] = "mJ"
C26["radio_effective_frequency"] = 1400*10**6
C26["radio_flag"] = 0
C26["radio_source"] = "FIRST"

C26["mirw1_fdm"] = 14.850
C26["mirw1_units"] = "Vega Mag"
C26["mirw1_effective_wavelength"] = 3.35*10**(-4)
C26["mirw1_flag"] = 0
C26["mirw1_source"] = "AllWISE"
C26["mirw1_Vega_0magflux"] = 309.540
C26["mirw2_fdm"] = 13.541
C26["mirw2_units"] = "Vega Mag"
C26["mirw2_effective_wavelength"] = 4.6*(10**-4)
C26["mirw2_flag"] = 0
C26["mirw2_source"] = "AllWISE"
C26["mirw2_Vega_0magflux"] = 171.787
C26["mirw3_fdm"] = 10.672
C26["mirw3_units"] = "Vega Mag"
C26["mirw3_effective_wavelength"] = 11.6*(10**-4)
C26["mirw3_flag"] = 0
C26["mirw3_source"] = "AllWISE"
C26["mirw3_Vega_0magflux"] = 31.674
C26["mirw4_fdm"] = 8.282
C26["mirw4_units"] = "Vega Mag"
C26["mirw4_effective_wavelength"] = 22.1*(10**-4)
C26["mirw4_flag"] = 0
C26["mirw4_source"] = "AllWISE"
C26["mirw4_Vega_0magflux"] = 8.363

C26["nirj_fdm"] = "n/a"
C26["nirj_units"] = "Vega Mag"
C26["nirj_effective_wavelength"] = "n/a" # 1.248*(10**-4)
C26["nirj_flag"] = "n/a"
C26["nirj_source"] = "UKIDSS-DR9"
C26["nirj_Vega_0magflux"] = "n/a" # 1530
C26["nirk_fdm"] = "n/a"
C26["nirk_units"] = "Vega Mag"
C26["nirk_effective_wavelength"] = "n/a" # 2.201*(10**-4)
C26["nirk_flag"] = "n/a"
C26["nirk_source"] = "UKIDSS-DR9"
C26["nirk_Vega_0magflux"] = "n/a" # 631

C26["optu_sdss_fdm"] = 18.997
C26["optu_sdss_units"] = "AB Mag"
C26["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C26["optu_sdss_flag"] = 0
C26["optu_sdss_source"] = "SDSS-DR9"
C26["optg_sdss_fdm"] = 18.923
C26["optg_sdss_units"] = "AB Mag"
C26["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C26["optg_sdss_flag"] = 0
C26["optg_sdss_source"] = "SDSS-DR9"
C26["optr_sdss_fdm"] = 18.571
C26["optr_sdss_units"] = "AB Mag"
C26["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C26["optr_sdss_flag"] = 0
C26["optr_sdss_source"] = "SDSS-DR9"
C26["opti_sdss_fdm"] = 18.595
C26["opti_sdss_units"] = "AB Mag"
C26["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C26["opti_sdss_flag"] = 0
C26["opti_sdss_source"] = "SDSS-DR9"
C26["optz_sdss_fdm"] = 18.652
C26["optz_sdss_units"] = "AB Mag"
C26["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C26["optz_sdss_flag"] = 0
C26["optz_sdss_source"] = "SDSS-DR9"

C26["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C26["optu_cfht_units"] = "AB Mag"
C26["optu_cfht_effective_wavelength"] = 354*(10**-7)
C26["optu_cfht_flag"] = 0
C26["optu_cfht_source"] = "CFHT"
C26["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C26["optg_ps1_units"] = "AB Mag"
C26["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C26["optg_ps1_flag"] = 0
C26["optg_ps1_source"] = "PS1"
C26["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C26["optr_ps1_units"] = "AB Mag"
C26["optr_ps1_effective_wavelength"] = 617*(10**-7)
C26["optr_ps1_flag"] = 0
C26["optr_ps1_source"] = "PS1"
C26["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C26["opti_ps1_units"] = "AB Mag"
C26["opti_ps1_effective_wavelength"] = 752*(10**-7)
C26["opti_ps1_flag"] = 0
C26["opti_ps1_source"] = "PS1"
C26["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C26["optz_ps1_units"] = "AB Mag"
C26["optz_ps1_effective_wavelength"] = 866*(10**-7)
C26["optz_ps1_flag"] = 0
C26["optz_ps1_source"] = "PS1"

C26["fuv_fdm"] = 20.556
C26["fuv_units"] = "AB Mag"
C26["fuv_effective_wavelength"] = 1516*10**-8
C26["fuv_flag"] = 0
C26["fuv_source"] = "GALEX-DR5(MIS)"
C26["nuv_fdm"] = 19.422
C26["nuv_units"] = "AB Mag"
C26["nuv_effective_wavelength"] = 2267*(10**-8)
C26["nuv_flag"] = 0
C26["nuv_source"] = "GALEX-DR5(MIS)"

C26["xray_flux"] = "n/a"
C26["xray_fdm"] = "n/a"
C26["xray_units"] = "erg/cm^2/keV/s"
C26["xray_effective_energy"] = "n/a" # 2
C26["xray_flag"] = "n/a"
C26["xray_source"] = "XMM-Newtwon-DR6"
