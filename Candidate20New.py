#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:44:39 2017

This is the data file for CANDIDATE 20.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012) (DXS)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    
    ***Missing UV and xray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 20

C20 = {}
C20["ra"] = 242.5040
C20["dec"] = 55.4391
C20["z"] = 1.794

C20["mag_error_mirw1"] = 0.053
C20["mag_error_mirw2"] = 0.066
C20["mag_error_mirw3"] = 0.453
C20["mag_error_mirw4"] = "n/a"
C20["mag_error_nirj"] = 0.019
C20["mag_error_nirk"] = 0.022
C20["mag_error_sdss_u"] = 0.067
C20["mag_error_sdss_g"] = 0.026
C20["mag_error_sdss_r"] = 0.036
C20["mag_error_sdss_i"] = 0.039
C20["mag_error_sdss_z"] = 0.194
C20["mag_error_fuv"] = "n/a"
C20["mag_error_nuv"] = "n/a"

C20["E(B-V)_UKIRT_J"] = 0.006
C20["E(B-V)_UKIRT_K"] = 0.002
C20["E(B-V)_SDSS_u"] = 0.034
C20["E(B-V)_SDSS_g"] = 0.027
C20["E(B-V)_SDSS_r"] = 0.018
C20["E(B-V)_SDSS_i"] = 0.014
C20["E(B-V)_SDSS_z"] = 0.010
C20["E(B-V)_PS1_g"] = 0.026
C20["E(B-V)_PS1_r"] = 0.018
C20["E(B-V)_PS1_i"] = 0.014
C20["E(B-V)_PS1_z"] = 0.011

C20["radio_fdm"] = 0.96
C20["radio_units"] = "mJ/beam"
C20["radio_effective_frequency"] = 1400*10**6
C20["radio_flag"] = 1
C20["radio_source"] = "FIRST"

C20["mirw1_fdm"] = 16.801
C20["mirw1_units"] = "Vega Mag"
C20["mirw1_effective_wavelength"] = 3.35*10**(-4)
C20["mirw1_flag"] = 0
C20["mirw1_source"] = "AllWISE"
C20["mirw1_Vega_0magflux"] = 309.540
C20["mirw2_fdm"] = 15.612
C20["mirw2_units"] = "Vega Mag"
C20["mirw2_effective_wavelength"] = 4.6*(10**-4)
C20["mirw2_flag"] = 0
C20["mirw2_source"] = "AllWISE"
C20["mirw2_Vega_0magflux"] = 171.787
C20["mirw3_fdm"] = 13.274
C20["mirw3_units"] = "Vega Mag"
C20["mirw3_effective_wavelength"] = 11.6*(10**-4)
C20["mirw3_flag"] = 0
C20["mirw3_source"] = "AllWISE"
C20["mirw3_Vega_0magflux"] = 31.674
C20["mirw4_fdm"] = 9.892
C20["mirw4_units"] = "Vega Mag"
C20["mirw4_effective_wavelength"] = 22.1*(10**-4)
C20["mirw4_flag"] = 1
C20["mirw4_source"] = "AllWISE"
C20["mirw4_Vega_0magflux"] = 8.363

C20["nirj_fdm"] = 19.257
C20["nirj_units"] = "Vega Mag"
C20["nirj_effective_wavelength"] = 1.248*(10**-4)
C20["nirj_flag"] = 0
C20["nirj_source"] = "UKIDSS-DR9"
C20["nirj_Vega_0magflux"] = 1530
C20["nirk_fdm"] = 18.178
C20["nirk_units"] = "Vega Mag"
C20["nirk_effective_wavelength"] = 2.201*(10**-4)
C20["nirk_flag"] = 0
C20["nirk_source"] = "UKIDSS-DR9"
C20["nirk_Vega_0magflux"] = 631

C20["optu_sdss_fdm"] = 20.482
C20["optu_sdss_units"] = "AB Mag"
C20["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C20["optu_sdss_flag"] = 0
C20["optu_sdss_source"] = "SDSS-DR9"
C20["optg_sdss_fdm"] = 20.502
C20["optg_sdss_units"] = "AB Mag"
C20["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C20["optg_sdss_flag"] = 0
C20["optg_sdss_source"] = "SDSS-DR9"
C20["optr_sdss_fdm"] = 20.557
C20["optr_sdss_units"] = "AB Mag"
C20["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C20["optr_sdss_flag"] = 0
C20["optr_sdss_source"] = "SDSS-DR9"
C20["opti_sdss_fdm"] = 20.298
C20["opti_sdss_units"] = "AB Mag"
C20["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C20["opti_sdss_flag"] = 0
C20["opti_sdss_source"] = "SDSS-DR9"
C20["optz_sdss_fdm"] = 20.416
C20["optz_sdss_units"] = "AB Mag"
C20["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C20["optz_sdss_flag"] = 0
C20["optz_sdss_source"] = "SDSS-DR9"

C20["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C20["optu_cfht_units"] = "AB Mag"
C20["optu_cfht_effective_wavelength"] = 354*(10**-7)
C20["optu_cfht_flag"] = 0
C20["optu_cfht_source"] = "CFHT"
C20["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C20["optg_ps1_units"] = "AB Mag"
C20["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C20["optg_ps1_flag"] = 0
C20["optg_ps1_source"] = "PS1"
C20["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C20["optr_ps1_units"] = "AB Mag"
C20["optr_ps1_effective_wavelength"] = 617*(10**-7)
C20["optr_ps1_flag"] = 0
C20["optr_ps1_source"] = "PS1"
C20["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C20["opti_ps1_units"] = "AB Mag"
C20["opti_ps1_effective_wavelength"] = 752*(10**-7)
C20["opti_ps1_flag"] = 0
C20["opti_ps1_source"] = "PS1"
C20["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C20["optz_ps1_units"] = "AB Mag"
C20["optz_ps1_effective_wavelength"] = 866*(10**-7)
C20["optz_ps1_flag"] = 0
C20["optz_ps1_source"] = "PS1"

C20["fuv_fdm"] = "n/a"
C20["fuv_units"] = "AB Mag"
C20["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C20["fuv_flag"] = "n/a"
C20["fuv_source"] = "GALEX-DR5(MIS)"
C20["nuv_fdm"] = "n/a"
C20["nuv_units"] = "AB Mag"
C20["nuv_effective_wavelength"] = "n/a" # 2267*(10**-8)
C20["nuv_flag"] = "n/a"
C20["nuv_source"] = "GALEX-DR5(MIS)"

C20["xray_flux"] = "n/a"
C20["xray_fdm"] = "n/a"
C20["xray_units"] = "erg/cm^2/keV/s"
C20["xray_effective_energy"] = "n/a" # 2
C20["xray_flag"] = "n/a"
C20["xray_source"] = "XMM-Newtwon-DR6"

