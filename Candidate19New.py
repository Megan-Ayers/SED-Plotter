#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:38:31 2017

This is the data file for CANDIDATE 19

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    
    *** Missing NIR, UV, xray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 19

C19 = {}
C19["ra"] = 214.9172
C19["dec"] = 53.8166
C19["z"] = 1.169

C19["mag_error_mirw1"] = 0.053
C19["mag_error_mirw2"] = 0.062
C19["mag_error_mirw3"] = 0.337
C19["mag_error_mirw4"] = "n/a"
C19["mag_error_nirj"] = "n/a"
C19["mag_error_nirk"] = "n/a"
C19["mag_error_sdss_u"] = 0.088
C19["mag_error_sdss_g"] = 0.030
C19["mag_error_sdss_r"] = 0.039
C19["mag_error_sdss_i"] = 0.056
C19["mag_error_sdss_z"] = 0.166
C19["mag_error_fuv"] = "n/a"
C19["mag_error_nuv"] = "n/a"

C19["E(B-V)_UKIRT_J"] = 0.008
C19["E(B-V)_UKIRT_K"] = 0.003
C19["E(B-V)_SDSS_u"] = 0.047
C19["E(B-V)_SDSS_g"] = 0.036
C19["E(B-V)_SDSS_r"] = 0.025
C19["E(B-V)_SDSS_i"] = 0.019
C19["E(B-V)_SDSS_z"] = 0.014
C19["E(B-V)_PS1_g"] = 0.035
C19["E(B-V)_PS1_r"] = 0.025
C19["E(B-V)_PS1_i"] = 0.019
C19["E(B-V)_PS1_z"] = 0.015

C19["radio_fdm"] = 1.00
C19["radio_units"] = "mJ/beam"
C19["radio_effective_frequency"] = 1400*10**6
C19["radio_flag"] = 1
C19["radio_source"] = "FIRST"

C19["mirw1_fdm"] = 16.410
C19["mirw1_units"] = "Vega Mag"
C19["mirw1_effective_wavelength"] = 3.35*10**(-4)
C19["mirw1_flag"] = 0
C19["mirw1_source"] = "AllWISE"
C19["mirw1_Vega_0magflux"] = 309.540
C19["mirw2_fdm"] = 15.214
C19["mirw2_units"] = "Vega Mag"
C19["mirw2_effective_wavelength"] = 4.6*(10**-4)
C19["mirw2_flag"] = 0
C19["mirw2_source"] = "AllWISE"
C19["mirw2_Vega_0magflux"] = 171.787
C19["mirw3_fdm"] = 12.513
C19["mirw3_units"] = "Vega Mag"
C19["mirw3_effective_wavelength"] = 11.6*(10**-4)
C19["mirw3_flag"] = 0
C19["mirw3_source"] = "AllWISE"
C19["mirw3_Vega_0magflux"] = 31.674
C19["mirw4_fdm"] = 9.292
C19["mirw4_units"] = "Vega Mag"
C19["mirw4_effective_wavelength"] = 22.1*(10**-4)
C19["mirw4_flag"] = 1
C19["mirw4_source"] = "AllWISE"
C19["mirw4_Vega_0magflux"] = 8.363

C19["nirj_fdm"] = "n/a"
C19["nirj_units"] = "Vega Mag"
C19["nirj_effective_wavelength"] = "n/a" # 1.248*(10**-4)
C19["nirj_flag"] = "n/a"
C19["nirj_source"] = "UKIDSS-DR9"
C19["nirj_Vega_0magflux"] = "n/a" # 1530
C19["nirk_fdm"] = "n/a"
C19["nirk_units"] = "Vega Mag"
C19["nirk_effective_wavelength"] = "n/a" # 2.201*(10**-4)
C19["nirk_flag"] = "n/a"
C19["nirk_source"] = "UKIDSS-DR9"
C19["nirk_Vega_0magflux"] = "n/a" # 631

C19["optu_sdss_fdm"] = 21.035
C19["optu_sdss_units"] = "AB Mag"
C19["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C19["optu_sdss_flag"] = 0
C19["optu_sdss_source"] = "SDSS-DR9"
C19["optg_sdss_fdm"] = 20.913
C19["optg_sdss_units"] = "AB Mag"
C19["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C19["optg_sdss_flag"] = 0
C19["optg_sdss_source"] = "SDSS-DR9"
C19["optr_sdss_fdm"] = 20.676
C19["optr_sdss_units"] = "AB Mag"
C19["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C19["optr_sdss_flag"] = 0
C19["optr_sdss_source"] = "SDSS-DR9"
C19["opti_sdss_fdm"] = 20.694
C19["opti_sdss_units"] = "AB Mag"
C19["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C19["opti_sdss_flag"] = 0
C19["opti_sdss_source"] = "SDSS-DR9"
C19["optz_sdss_fdm"] = 20.279
C19["optz_sdss_units"] = "AB Mag"
C19["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C19["optz_sdss_flag"] = 0
C19["optz_sdss_source"] = "SDSS-DR9"

C19["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C19["optu_cfht_units"] = "AB Mag"
C19["optu_cfht_effective_wavelength"] = 354*(10**-7)
C19["optu_cfht_flag"] = 0
C19["optu_cfht_source"] = "CFHT"
C19["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C19["optg_ps1_units"] = "AB Mag"
C19["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C19["optg_ps1_flag"] = 0
C19["optg_ps1_source"] = "PS1"
C19["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C19["optr_ps1_units"] = "AB Mag"
C19["optr_ps1_effective_wavelength"] = 617*(10**-7)
C19["optr_ps1_flag"] = 0
C19["optr_ps1_source"] = "PS1"
C19["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C19["opti_ps1_units"] = "AB Mag"
C19["opti_ps1_effective_wavelength"] = 752*(10**-7)
C19["opti_ps1_flag"] = 0
C19["opti_ps1_source"] = "PS1"
C19["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C19["optz_ps1_units"] = "AB Mag"
C19["optz_ps1_effective_wavelength"] = 866*(10**-7)
C19["optz_ps1_flag"] = 0
C19["optz_ps1_source"] = "PS1"

C19["fuv_fdm"] = "n/a"
C19["fuv_units"] = "AB Mag"
C19["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C19["fuv_flag"] = "n/a"
C19["fuv_source"] = "GALEX-DR5(MIS)"
C19["nuv_fdm"] = "n/a"
C19["nuv_units"] = "AB Mag"
C19["nuv_effective_wavelength"] = "n/a" # 2267*(10**-8)
C19["nuv_flag"] = "n/a"
C19["nuv_source"] = "GALEX-DR5(MIS)"

C19["xray_flux"] = "n/a"
C19["xray_fdm"] = "n/a"
C19["xray_units"] = "erg/cm^2/keV/s"
C19["xray_effective_energy"] = "n/a" # 2
C19["xray_flag"] = "n/a"
C19["xray_source"] = "XMM-Newtwon-DR6"
