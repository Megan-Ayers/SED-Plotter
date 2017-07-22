#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 15:08:41 2017

This is the data file for CANDIDATE 25

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    Radio from http://sundog.stsci.edu/cgi-bin/searchfirst
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012) (DXS)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    UV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (MIS)
    
    ***Missing x-ray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 25

C25 = {}
C25["ra"] = 334.2028
C25["dec"] = 1.4075
C25["z"] = 2.070

C25["mag_error_radio"] = 0.143

C25["mag_error_mirw1"] = 0.066
C25["mag_error_mirw2"] = 0.083
C25["mag_error_mirw3"] = 0.261
C25["mag_error_mirw4"] = "n/a"
C25["mag_error_nirj"] = 0.010
C25["mag_error_nirk"] = 0.009
C25["mag_error_sdss_u"] = 0.027
C25["mag_error_sdss_g"] = 0.011
C25["mag_error_sdss_r"] = 0.011
C25["mag_error_sdss_i"] = 0.013
C25["mag_error_sdss_z"] = 0.030
C25["mag_error_fuv"] = 0.103
C25["mag_error_nuv"] = 0.069

C25["E(B-V)_UKIRT_J"] = 0.033
C25["E(B-V)_UKIRT_K"] = 0.014
C25["E(B-V)_SDSS_u"] = 0.199
C25["E(B-V)_SDSS_g"] = 0.155
C25["E(B-V)_SDSS_r"] = 0.107
C25["E(B-V)_SDSS_i"] = 0.080
C25["E(B-V)_SDSS_z"] = 0.059
C25["E(B-V)_PS1_g"] = 0.149
C25["E(B-V)_PS1_r"] = 0.107
C25["E(B-V)_PS1_i"] = 0.079
C25["E(B-V)_PS1_z"] = 0.062

C25["radio_fdm"] = 31.00 # 20.68 = peak, int. flux = 31.00 mJy
C25["radio_units"] = "mJ"
C25["radio_effective_frequency"] = 1400*10**6
C25["radio_flag"] = 0
C25["radio_source"] = "FIRST"

C25["mirw1_fdm"] = 16.124
C25["mirw1_units"] = "Vega Mag"
C25["mirw1_effective_wavelength"] = 3.35*10**(-4)
C25["mirw1_flag"] = 0
C25["mirw1_source"] = "AllWISE"
C25["mirw1_Vega_0magflux"] = 309.540
C25["mirw2_fdm"] = 14.994
C25["mirw2_units"] = "Vega Mag"
C25["mirw2_effective_wavelength"] = 4.6*(10**-4)
C25["mirw2_flag"] = 0
C25["mirw2_source"] = "AllWISE"
C25["mirw2_Vega_0magflux"] = 171.787
C25["mirw3_fdm"] = 11.732
C25["mirw3_units"] = "Vega Mag"
C25["mirw3_effective_wavelength"] = 11.6*(10**-4)
C25["mirw3_flag"] = 0
C25["mirw3_source"] = "AllWISE"
C25["mirw3_Vega_0magflux"] = 31.674
C25["mirw4_fdm"] = 8.552
C25["mirw4_units"] = "Vega Mag"
C25["mirw4_effective_wavelength"] = 22.1*(10**-4)
C25["mirw4_flag"] = 1
C25["mirw4_source"] = "AllWISE"
C25["mirw4_Vega_0magflux"] = 8.363

C25["nirj_fdm"] = 18.108
C25["nirj_units"] = "Vega Mag"
C25["nirj_effective_wavelength"] = 1.248*(10**-4)
C25["nirj_flag"] = 0
C25["nirj_source"] = "UKIDSS-DR9"
C25["nirj_Vega_0magflux"] = 1530
C25["nirk_fdm"] = 17.045
C25["nirk_units"] = "Vega Mag"
C25["nirk_effective_wavelength"] = 2.201*(10**-4)
C25["nirk_flag"] = 0
C25["nirk_source"] = "UKIDSS-DR9"
C25["nirk_Vega_0magflux"] = 631

C25["optu_sdss_fdm"] = 19.405
C25["optu_sdss_units"] = "AB Mag"
C25["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C25["optu_sdss_flag"] = 0
C25["optu_sdss_source"] = "SDSS-DR9"
C25["optg_sdss_fdm"] = 19.262
C25["optg_sdss_units"] = "AB Mag"
C25["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C25["optg_sdss_flag"] = 0
C25["optg_sdss_source"] = "SDSS-DR9"
C25["optr_sdss_fdm"] = 19.144
C25["optr_sdss_units"] = "AB Mag"
C25["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C25["optr_sdss_flag"] = 0
C25["optr_sdss_source"] = "SDSS-DR9"
C25["opti_sdss_fdm"] = 18.976
C25["opti_sdss_units"] = "AB Mag"
C25["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C25["opti_sdss_flag"] = 0
C25["opti_sdss_source"] = "SDSS-DR9"
C25["optz_sdss_fdm"] = 18.772
C25["optz_sdss_units"] = "AB Mag"
C25["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C25["optz_sdss_flag"] = 0
C25["optz_sdss_source"] = "SDSS-DR9"

C25["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C25["optu_cfht_units"] = "AB Mag"
C25["optu_cfht_effective_wavelength"] = 354*(10**-7)
C25["optu_cfht_flag"] = 0
C25["optu_cfht_source"] = "CFHT"
C25["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C25["optg_ps1_units"] = "AB Mag"
C25["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C25["optg_ps1_flag"] = 0
C25["optg_ps1_source"] = "PS1"
C25["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C25["optr_ps1_units"] = "AB Mag"
C25["optr_ps1_effective_wavelength"] = 617*(10**-7)
C25["optr_ps1_flag"] = 0
C25["optr_ps1_source"] = "PS1"
C25["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C25["opti_ps1_units"] = "AB Mag"
C25["opti_ps1_effective_wavelength"] = 752*(10**-7)
C25["opti_ps1_flag"] = 0
C25["opti_ps1_source"] = "PS1"
C25["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C25["optz_ps1_units"] = "AB Mag"
C25["optz_ps1_effective_wavelength"] = 866*(10**-7)
C25["optz_ps1_flag"] = 0
C25["optz_ps1_source"] = "PS1"

C25["fuv_fdm"] = 21.763
C25["fuv_units"] = "AB Mag"
C25["fuv_effective_wavelength"] = 1516*10**-8
C25["fuv_flag"] = 0
C25["fuv_source"] = "GALEX-DR5(MIS)"
C25["nuv_fdm"] = 21.453
C25["nuv_units"] = "AB Mag"
C25["nuv_effective_wavelength"] = 2267*(10**-8)
C25["nuv_flag"] = 0
C25["nuv_source"] = "GALEX-DR5(MIS)"

C25["xray_flux"] = "n/a"
C25["xray_fdm"] = "n/a"
C25["xray_units"] = "erg/cm^2/keV/s"
C25["xray_effective_energy"] = "n/a" # 2
C25["xray_flag"] = "n/a"
C25["xray_source"] = "XMM-Newtwon-DR6"
