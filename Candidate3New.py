#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 21:31:25 2017

This is a test template for creating the data file for CANDIDATE 3.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013) *** r = 1.009 arcsec ***
    Opt from PS1 data sheet
    
    *** Missing radio, NIR, UV, xray

@author: megan
"""

C3 = {}
C3["ra"] = 52.6172
C3["dec"] = -27.6268
C3["z"] = 2.134

C3["mag_error_mirw1"] = 0.062
C3["mag_error_mirw2"] = 0.094
C3["mag_error_mirw3"] = 0.251
C3["mag_error_mirw4"] = 0.433
C3["mag_error_nirj"] = "n/a"
C3["mag_error_nirk"] = "n/a"
C3["mag_error_sdss_u"] = "n/a"
C3["mag_error_sdss_g"] = "n/a"
C3["mag_error_sdss_r"] = "n/a"
C3["mag_error_sdss_i"] = "n/a"
C3["mag_error_sdss_z"] = "n/a"
C3["mag_error_fuv"] = "n/a"
C3["mag_error_nuv"] = "n/a"

C3["E(B-V)_UKIRT_J"] = 0.006
C3["E(B-V)_UKIRT_K"] =  0.003
C3["E(B-V)_SDSS_u"] = 0.037
C3["E(B-V)_SDSS_g"] = 0.029
C3["E(B-V)_SDSS_r"] = 0.020
C3["E(B-V)_SDSS_i"] = 0.015
C3["E(B-V)_SDSS_z"] = 0.011
C3["E(B-V)_PS1_g"] = 0.028
C3["E(B-V)_PS1_r"] = 0.020
C3["E(B-V)_PS1_i"] = 0.015
C3["E(B-V)_PS1_z"] = 0.011

C3["radio_fdm"] = "n/a"
C3["radio_units"] = "mJ"
C3["radio_effective_frequency"] = "n/a"
C3["radio_flag"] = "n/a"
C3["radio_source"] = "FIRST"

C3["mirw1_fdm"] = 16.753
C3["mirw1_units"] = "Vega Mag"
C3["mirw1_effective_wavelength"] = 3.35*10**(-4)
C3["mirw1_flag"] = 0
C3["mirw1_source"] = "AllWISE"
C3["mirw1_Vega_0magflux"] = 309.540
C3["mirw2_fdm"] = 15.808
C3["mirw2_units"] = "Vega Mag"
C3["mirw2_effective_wavelength"] = 4.6*(10**-4)
C3["mirw2_flag"] = 0
C3["mirw2_source"] = "AllWISE"
C3["mirw2_Vega_0magflux"] = 171.787
C3["mirw3_fdm"] = 12.459
C3["mirw3_units"] = "Vega Mag"
C3["mirw3_effective_wavelength"] = 11.6*(10**-4)
C3["mirw3_flag"] = 0
C3["mirw3_source"] = "AllWISE"
C3["mirw3_Vega_0magflux"] = 31.674
C3["mirw4_fdm"] = 9.473
C3["mirw4_units"] = "Vega Mag"
C3["mirw4_effective_wavelength"] = 22.1*(10**-4)
C3["mirw4_flag"] = 0
C3["mirw4_source"] = "AllWISE"
C3["mirw4_Vega_0magflux"] = 8.363

C3["nirj_fdm"] = "n/a"
C3["nirj_units"] = "Vega Mag"
C3["nirj_effective_wavelength"] = "n/a" # 1.248*(10**-4)
C3["nirj_flag"] = "n/a"
C3["nirj_source"] = "UKIDSS-DR9"
C3["nirj_Vega_0magflux"] = 1530
C3["nirk_fdm"] = "n/a"
C3["nirk_units"] = "Vega Mag"
C3["nirk_effective_wavelength"] = "n/a" # 2.201*(10**-4)
C3["nirk_flag"] = "n/a"
C3["nirk_source"] = "UKIDSS-DR9"
C3["nirk_Vega_0magflux"] = 631

C3["optu_sdss_fdm"] = "n/a"
C3["optu_sdss_units"] = "AB Mag"
C3["optu_sdss_effective_wavelength"] = "n/a" # 354.3*(10**-7)
C3["optu_sdss_flag"] = "n/a"
C3["optu_sdss_source"] = "SDSS-DR9"
C3["optg_sdss_fdm"] = "n/a"
C3["optg_sdss_units"] = "AB Mag"
C3["optg_sdss_effective_wavelength"] = "n/a" # 477.0*(10**-7)
C3["optg_sdss_flag"] = "n/a"
C3["optg_sdss_source"] = "SDSS-DR9"
C3["optr_sdss_fdm"] = "n/a"
C3["optr_sdss_units"] = "AB Mag"
C3["optr_sdss_effective_wavelength"] = "n/a" # 623.1*(10**-7)
C3["optr_sdss_flag"] = "n/a"
C3["optr_sdss_source"] = "SDSS-DR9"
C3["opti_sdss_fdm"] = "n/a"
C3["opti_sdss_units"] = "AB Mag"
C3["opti_sdss_effective_wavelength"] = "n/a" # 762.5*(10**-7)
C3["opti_sdss_flag"] = "n/a"
C3["opti_sdss_source"] = "SDSS-DR9"
C3["optz_sdss_fdm"] = "n/a"
C3["optz_sdss_units"] = "AB Mag"
C3["optz_sdss_effective_wavelength"] = "n/a" #  913.4*(10**-7)
C3["optz_sdss_flag"] = "n/a"
C3["optz_sdss_source"] = "SDSS-DR9"

C3["optu_cfht_fdm"] = 20.47489357
C3["optu_cfht_units"] = "AB Mag"
C3["optu_cfht_effective_wavelength"] = 354*(10**-7)
C3["optu_cfht_flag"] = 0
C3["optu_cfht_source"] = "CFHT"
C3["optg_ps1_fdm"] = 20.40201569
C3["optg_ps1_units"] = "AB Mag"
C3["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C3["optg_ps1_flag"] = 0
C3["optg_ps1_source"] = "PS1"
C3["optr_ps1_fdm"] = 20.04507256
C3["optr_ps1_units"] = "AB Mag"
C3["optr_ps1_effective_wavelength"] = 617*(10**-7)
C3["optr_ps1_flag"] = 0
C3["optr_ps1_source"] = "PS1"
C3["opti_ps1_fdm"] = 20.07183647
C3["opti_ps1_units"] = "AB Mag"
C3["opti_ps1_effective_wavelength"] = 752*(10**-7)
C3["opti_ps1_flag"] = 0
C3["opti_ps1_source"] = "PS1"
C3["optz_ps1_fdm"] = 19.84422493
C3["optz_ps1_units"] = "AB Mag"
C3["optz_ps1_effective_wavelength"] = 866*(10**-7)
C3["optz_ps1_flag"] = 0
C3["optz_ps1_source"] = "PS1"

C3["fuv_fdm"] = "n/a"
C3["fuv_units"] = "AB Mag"
C3["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C3["fuv_flag"] = "n/a"
C3["fuv_source"] = "GALEX-DR5(MIS)"
C3["nuv_fdm"] = "n/a"
C3["nuv_units"] = "AB Mag"
C3["nuv_effective_wavelength"] = "n/a" # 2267*(10**-8)
C3["nuv_flag"] = "n/a"
C3["nuv_source"] = "GALEX-DR5(AIS)"

C3["xray_flux"] = "n/a"
C3["xray_fdm"] = "n/a"
C3["xray_units"] = "erg/cm^2/keV/s"
C3["xray_effective_energy"] = "n/a" # 2
C3["xray_flag"] = "n/a"
C3["xray_source"] = "XMM-Newtwon-DR6"
