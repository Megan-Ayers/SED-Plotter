#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 16:57:31 2017

This is a template for creating the data file for CANDIDATE 4.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    NUV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (AIS)
*** Missing NIR, FUV, X-ray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 4

C4 = {}
C4["ra"] = 129.4288
C4["dec"] = 43.8234
C4["z"] = 0.959

C4["mag_error_mirw1"] = 0.038
C4["mag_error_mirw2"] = 0.049
C4["mag_error_mirw3"] = 0.269
C4["mag_error_mirw4"] = "n/a"
C4["mag_error_nirj"] = "n/a"
C4["mag_error_nirk"] = "n/a"
C4["mag_error_sdss_u"] = 0.034
C4["mag_error_sdss_g"] = 0.014
C4["mag_error_sdss_r"] = 0.014
C4["mag_error_sdss_i"] = 0.019
C4["mag_error_sdss_z"] = 0.073
C4["mag_error_fuv"] = "n/a"
C4["mag_error_nuv"] = 0.092

C4["E(B-V)_UKIRT_J"] = 0.019
C4["E(B-V)_UKIRT_K"] = 0.008
C4["E(B-V)_SDSS_u"] = 0.116
C4["E(B-V)_SDSS_g"] = 0.090
C4["E(B-V)_SDSS_r"] = 0.062
C4["E(B-V)_SDSS_i"] = 0.046
C4["E(B-V)_SDSS_z"] = 0.035
C4["E(B-V)_PS1_g"] = 0.087
C4["E(B-V)_PS1_r"] = 0.062
C4["E(B-V)_PS1_i"] = 0.046
C4["E(B-V)_PS1_z"] = 0.036

C4["radio_fdm"] = 0.97
C4["radio_units"] = "mJ/beam"
C4["radio_effective_frequency"] = 1400*10**6
C4["radio_flag"] = 1
C4["radio_source"] = "FIRST"

C4["mirw1_fdm"] = 15.352
C4["mirw1_units"] = "Vega Mag"
C4["mirw1_effective_wavelength"] = 3.35*10**(-4)
C4["mirw1_flag"] = 0
C4["mirw1_source"] = "AllWISE"
C4["mirw1_Vega_0magflux"] = 309.540
C4["mirw2_fdm"] = 14.281
C4["mirw2_units"] = "Vega Mag"
C4["mirw2_effective_wavelength"] = 4.6*(10**-4)
C4["mirw2_flag"] = 0
C4["mirw2_source"] = "AllWISE"
C4["mirw2_Vega_0magflux"] = 171.787
C4["mirw3_fdm"] = 11.926
C4["mirw3_units"] = "Vega Mag"
C4["mirw3_effective_wavelength"] = 11.6*(10**-4)
C4["mirw3_flag"] = 0
C4["mirw3_source"] = "AllWISE"
C4["mirw3_Vega_0magflux"] = 31.674
C4["mirw4_fdm"] = 8.600
C4["mirw4_units"] = "Vega Mag"
C4["mirw4_effective_wavelength"] = 22.1*(10**-4)
C4["mirw4_flag"] = 1
C4["mirw4_source"] = "AllWISE"
C4["mirw4_Vega_0magflux"] = 8.363

C4["nirj_fdm"] = "n/a"
C4["nirj_units"] = "Vega Mag"
C4["nirj_effective_wavelength"] = "n/a" # 1.248*(10**-4)
C4["nirj_flag"] = "n/a"
C4["nirj_source"] = "UKIDSS-DR9"
C4["nirj_Vega_0magflux"] = "n/a" # 1530
C4["nirk_fdm"] = "n/a"
C4["nirk_units"] = "Vega Mag"
C4["nirk_effective_wavelength"] = "n/a" # 2.201*(10**-4)
C4["nirk_flag"] = "n/a"
C4["nirk_source"] = "UKIDSS-DR9"
C4["nirk_Vega_0magflux"] = "n/a" # 631

C4["optu_sdss_fdm"] = 19.670
C4["optu_sdss_units"] = "AB Mag"
C4["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C4["optu_sdss_flag"] = 0
C4["optu_sdss_source"] = "SDSS-DR9"
C4["optg_sdss_fdm"] = 19.451
C4["optg_sdss_units"] = "AB Mag"
C4["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C4["optg_sdss_flag"] = 0
C4["optg_sdss_source"] = "SDSS-DR9"
C4["optr_sdss_fdm"] = 19.246
C4["optr_sdss_units"] = "AB Mag"
C4["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C4["optr_sdss_flag"] = 0
C4["optr_sdss_source"] = "SDSS-DR9"
C4["opti_sdss_fdm"] = 19.276
C4["opti_sdss_units"] = "AB Mag"
C4["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C4["opti_sdss_flag"] = 0
C4["opti_sdss_source"] = "SDSS-DR9"
C4["optz_sdss_fdm"] = 19.344
C4["optz_sdss_units"] = "AB Mag"
C4["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C4["optz_sdss_flag"] = 0
C4["optz_sdss_source"] = "SDSS-DR9"

C4["optu_cfht_fdm"] = cfht_ps1_data_list[4][2]
C4["optu_cfht_units"] = "AB Mag"
C4["optu_cfht_effective_wavelength"] = 354*(10**-7)
C4["optu_cfht_flag"] = 0
C4["optu_cfht_source"] = "CFHT"
C4["optg_ps1_fdm"] = cfht_ps1_data_list[4][3]
C4["optg_ps1_units"] = "AB Mag"
C4["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C4["optg_ps1_flag"] = 0
C4["optg_ps1_source"] = "PS1"
C4["optr_ps1_fdm"] = cfht_ps1_data_list[4][4]
C4["optr_ps1_units"] = "AB Mag"
C4["optr_ps1_effective_wavelength"] = 617*(10**-7)
C4["optr_ps1_flag"] = 0
C4["optr_ps1_source"] = "PS1"
C4["opti_ps1_fdm"] = cfht_ps1_data_list[4][5]
C4["opti_ps1_units"] = "AB Mag"
C4["opti_ps1_effective_wavelength"] = 752*(10**-7)
C4["opti_ps1_flag"] = 0
C4["opti_ps1_source"] = "PS1"
C4["optz_ps1_fdm"] = cfht_ps1_data_list[4][6]
C4["optz_ps1_units"] = "AB Mag"
C4["optz_ps1_effective_wavelength"] = 866*(10**-7)
C4["optz_ps1_flag"] = 0
C4["optz_ps1_source"] = "PS1"

C4["fuv_fdm"] = "n/a"
C4["fuv_units"] = "AB Mag"
C4["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C4["fuv_flag"] = "n/a"
C4["fuv_source"] = "GALEX-DR5(MIS)"
C4["nuv_fdm"] = 19.928
C4["nuv_units"] = "AB Mag"
C4["nuv_effective_wavelength"] = 2267*(10**-8)
C4["nuv_flag"] = 0
C4["nuv_source"] = "GALEX-DR5(MIS)"

C4["xray_flux"] = "n/a"
C4["xray_fdm"] = "n/a"
C4["xray_units"] = "erg/cm^2/keV/s"
C4["xray_effective_energy"] = "n/a" # 2
C4["xray_flag"] = "n/a"
C4["xray_source"] = "XMM-Newtwon-DR6"
