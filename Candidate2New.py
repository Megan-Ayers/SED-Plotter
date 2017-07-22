#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:06:28 2017

This is a data file for CANDIDATE 2.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from  AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012)
    Opt from The SDSS Photometric Catalog, Release 8 (Adelman-McCarthy+, 2011)
    NUV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (AIS)
    XMM-Newton Serendipitous Source Catalogue 3XMM-DR6 (XMM-SSC, 2016) 
        *** r = 1.00 ***

    **Missing  FUV

@author: megan
"""

C2 = {}
C2["ra"] = 35.8704
C2["dec"] = -4.0263
C2["z"] = 1.916

C2["mag_error_mirw1"] = 0.067
C2["mag_error_mirw2"] = 0.076
C2["mag_error_mirw3"] = 0.197
C2["mag_error_mirw4"] = "n/a"
C2["mag_error_nirj"] = 0.022
C2["mag_error_nirk"] = 0.013
C2["mag_error_sdss_u"] = 0.052
C2["mag_error_sdss_g"] = 0.015
C2["mag_error_sdss_r"] = 0.020
C2["mag_error_sdss_i"] = 0.020
C2["mag_error_sdss_z"] = 0.072
C2["mag_error_fuv"] = "n/a"
C2["mag_error_nuv"] = 0.485
C2["mag_xray_error"] = 8.20e-15

C2["E(B-V)_UKIRT_J"] = 0.017
C2["E(B-V)_UKIRT_K"] =  0.007
C2["E(B-V)_SDSS_u"] = 0.104
C2["E(B-V)_SDSS_g"] = 0.081
C2["E(B-V)_SDSS_r"] = 0.056
C2["E(B-V)_SDSS_i"] = 0.042
C2["E(B-V)_SDSS_z"] = 0.031
C2["E(B-V)_PS1_g"] = 0.078
C2["E(B-V)_PS1_r"] = 0.056
C2["E(B-V)_PS1_i"] = 0.041
C2["E(B-V)_PS1_z"] = 0.032

C2["radio_fdm"] = 0.82
C2["radio_units"] = "mJ/beam"
C2["radio_effective_frequency"] = 1400*10**6
C2["radio_flag"] = 1
C2["radio_source"] = "FIRST"

C2["mirw1_fdm"] = 16.483
C2["mirw1_units"] = "Vega Mag"
C2["mirw1_effective_wavelength"] = 3.35*10**(-4)
C2["mirw1_flag"] = 0
C2["mirw1_source"] = "AllWISE"
C2["mirw1_Vega_0magflux"] = 309.540
C2["mirw2_fdm"] = 15.201
C2["mirw2_units"] = "Vega Mag"
C2["mirw2_effective_wavelength"] = 4.6*(10**-4)
C2["mirw2_flag"] = 0
C2["mirw2_source"] = "AllWISE"
C2["mirw2_Vega_0magflux"] = 171.787
C2["mirw3_fdm"] = 11.728
C2["mirw3_units"] = "Vega Mag"
C2["mirw3_effective_wavelength"] = 11.6*(10**-4)
C2["mirw3_flag"] = 0
C2["mirw3_source"] = "AllWISE"
C2["mirw3_Vega_0magflux"] = 31.674
C2["mirw4_fdm"] = 8.492
C2["mirw4_units"] = "Vega Mag"
C2["mirw4_effective_wavelength"] = 22.1*(10**-4)
C2["mirw4_flag"] = 1
C2["mirw4_source"] = "AllWISE"
C2["mirw4_Vega_0magflux"] = 8.363

C2["nirj_fdm"] = 18.388
C2["nirj_units"] = "Vega Mag"
C2["nirj_effective_wavelength"] = 1.248*(10**-4)
C2["nirj_flag"] = 0
C2["nirj_source"] = "UKIDSS-DR9"
C2["nirj_Vega_0magflux"] = 1530
C2["nirk_fdm"] = 17.587
C2["nirk_units"] = "Vega Mag"
C2["nirk_effective_wavelength"] = 2.201*(10**-4)
C2["nirk_flag"] = 0
C2["nirk_source"] = "UKIDSS-DR9"
C2["nirk_Vega_0magflux"] = 631

C2["optu_sdss_fdm"] = 20.077
C2["optu_sdss_units"] = "AB Mag"
C2["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C2["optu_sdss_flag"] = 0
C2["optu_sdss_source"] = "SDSS-DR9"
C2["optg_sdss_fdm"] = 19.869
C2["optg_sdss_units"] = "AB Mag"
C2["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C2["optg_sdss_flag"] = 0
C2["optg_sdss_source"] = "SDSS-DR9"
C2["optr_sdss_fdm"] = 19.788
C2["optr_sdss_units"] = "AB Mag"
C2["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C2["optr_sdss_flag"] = 0
C2["optr_sdss_source"] = "SDSS-DR9"
C2["opti_sdss_fdm"] = 19.526
C2["opti_sdss_units"] = "AB Mag"
C2["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C2["opti_sdss_flag"] = 0
C2["opti_sdss_source"] = "SDSS-DR9"
C2["optz_sdss_fdm"] = 19.372
C2["optz_sdss_units"] = "AB Mag"
C2["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C2["optz_sdss_flag"] = 0
C2["optz_sdss_source"] = "SDSS-DR9"

C2["optu_cfht_fdm"] = 19.96146202
C2["optu_cfht_units"] = "AB Mag"
C2["optu_cfht_effective_wavelength"] = 354*(10**-7)
C2["optu_cfht_flag"] = 0
C2["optu_cfht_source"] = "CFHT"
C2["optg_ps1_fdm"] = 19.42160416
C2["optg_ps1_units"] = "AB Mag"
C2["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C2["optg_ps1_flag"] = 0
C2["optg_ps1_source"] = "PS1"
C2["optr_ps1_fdm"] = 19.38210678
C2["optr_ps1_units"] = "AB Mag"
C2["optr_ps1_effective_wavelength"] = 617*(10**-7)
C2["optr_ps1_flag"] = 0
C2["optr_ps1_source"] = "PS1"
C2["opti_ps1_fdm"] = 19.22444534
C2["opti_ps1_units"] = "AB Mag"
C2["opti_ps1_effective_wavelength"] = 752*(10**-7)
C2["opti_ps1_flag"] = 0
C2["opti_ps1_source"] = "PS1"
C2["optz_ps1_fdm"] = 19.12619972
C2["optz_ps1_units"] = "AB Mag"
C2["optz_ps1_effective_wavelength"] = 866*(10**-7)
C2["optz_ps1_flag"] = 0
C2["optz_ps1_source"] = "PS1"

C2["fuv_fdm"] = "n/a"
C2["fuv_units"] = "AB Mag"
C2["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C2["fuv_flag"] = "n/a"
C2["fuv_source"] = "GALEX-DR5(MIS)"
C2["nuv_fdm"] = 22.228
C2["nuv_units"] = "AB Mag"
C2["nuv_effective_wavelength"] = 2267*(10**-8)
C2["nuv_flag"] = 0
C2["nuv_source"] = "GALEX-DR5(AIS)"

C2["xray_flux"] = 2.9202e-14
C2["xray_fdm"] = 7.132e-15
C2["xray_units"] = "erg/cm^2/keV/s"
C2["xray_effective_energy"] = 2
C2["xray_flag"] = 0
C2["xray_source"] = "XMM-Newtwon-DR6"
