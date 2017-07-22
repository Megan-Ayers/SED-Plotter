#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 10:26:08 2017

This is the data file for CANDIDATE 1.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    NUV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011)
    X-ray from XMM-Newton Serendipitous Source Catalogue 3XMM-DR6 (XMM-SSC,
    2016)

    **Missing FUV

@author: megan
"""

C1 = {}
C1["ra"] = 35.7068
C1["dec"] = -4.23144
C1["z"] = 1.564

C1["mag_error_mirw1"] = 0.070
C1["mag_error_mirw2"] = 0.086
C1["mag_error_mirw3"] = "n/a"
C1["mag_error_mirw4"] = "n/a"
C1["mag_error_nirj"] = 0.017
C1["mag_error_nirk"] = 0.021
C1["mag_error_sdss_u"] = 0.056
C1["mag_error_sdss_g"] = 0.014
C1["mag_error_sdss_r"] = 0.017
C1["mag_error_sdss_i"] = 0.020
C1["mag_error_sdss_z"] = 0.071
C1["mag_error_fuv"] = "n/a"
C1["mag_error_nuv"] = 0.346
C1["mag_xray_error"] = 6.78e-15

C1["E(B-V)_UKIRT_J"] = 0.020
C1["E(B-V)_UKIRT_K"] = 0.008
C1["E(B-V)_SDSS_u"] = 0.117
C1["E(B-V)_SDSS_g"] = 0.091
C1["E(B-V)_SDSS_r"] = 0.063
C1["E(B-V)_SDSS_i"] = 0.047
C1["E(B-V)_SDSS_z"] = 0.035
C1["E(B-V)_PS1_g"] = 0.088
C1["E(B-V)_PS1_r"] = 0.063
C1["E(B-V)_PS1_i"] = 0.046
C1["E(B-V)_PS1_z"] = 0.036

C1["radio_fdm"] = 0.81
C1["radio_units"] = "mJ/beam"
C1["radio_effective_frequency"] = 1400*10**6
C1["radio_flag"] = 1
C1["radio_source"] = "FIRST"

C1["mirw1_fdm"] = 16.496
C1["mirw1_units"] = "Vega Mag"
C1["mirw1_effective_wavelength"] = 3.35*10**(-4)
C1["mirw1_flag"] = 0
C1["mirw1_source"] = "AllWISE"
C1["mirw1_Vega_0magflux"] = 309.540
C1["mirw2_fdm"] = 15.269
C1["mirw2_units"] = "Vega Mag"
C1["mirw2_effective_wavelength"] = 4.6*(10**-4)
C1["mirw2_flag"] = 0
C1["mirw2_source"] = "AllWISE"
C1["mirw2_Vega_0magflux"] = 171.787
C1["mirw3_fdm"] = 12.255
C1["mirw3_units"] = "Vega Mag"
C1["mirw3_effective_wavelength"] = 11.6*(10**-4)
C1["mirw3_flag"] = 1
C1["mirw3_source"] = "AllWISE"
C1["mirw3_Vega_0magflux"] = 31.674
C1["mirw4_fdm"] = 8.891
C1["mirw4_units"] = "Vega Mag"
C1["mirw4_effective_wavelength"] = 22.1*(10**-4)
C1["mirw4_flag"] = 1
C1["mirw4_source"] = "AllWISE"
C1["mirw4_Vega_0magflux"] = 8.363

C1["nirj_fdm"] = 18.876
C1["nirj_units"] = "Vega Mag"
C1["nirj_effective_wavelength"] = 1.248*(10**-4)
C1["nirj_flag"] = 0
C1["nirj_source"] = "UKIDSS-DR9"
C1["nirj_Vega_0magflux"] = 1530
C1["nirk_fdm"] = 17.952
C1["nirk_units"] = "Vega Mag"
C1["nirk_effective_wavelength"] = 2.201*(10**-4)
C1["nirk_flag"] = 0
C1["nirk_source"] = "UKIDSS-DR9"
C1["nirk_Vega_0magflux"] = 631

C1["optu_sdss_fdm"] = 20.033
C1["optu_sdss_units"] = "AB Mag"
C1["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C1["optu_sdss_flag"] = 0
C1["optu_sdss_source"] = "SDSS-DR9"
C1["optg_sdss_fdm"] = 19.620
C1["optg_sdss_units"] = "AB Mag"
C1["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C1["optg_sdss_flag"] = 0
C1["optg_sdss_source"] = "SDSS-DR9"
C1["optr_sdss_fdm"] = 19.664
C1["optr_sdss_units"] = "AB Mag"
C1["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C1["optr_sdss_flag"] = 0
C1["optr_sdss_source"] = "SDSS-DR9"
C1["opti_sdss_fdm"] = 19.509
C1["opti_sdss_units"] = "AB Mag"
C1["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C1["opti_sdss_flag"] = 0
C1["opti_sdss_source"] = "SDSS-DR9"
C1["optz_sdss_fdm"] = 19.519
C1["optz_sdss_units"] = "AB Mag"
C1["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C1["optz_sdss_flag"] = 0
C1["optz_sdss_source"] = "SDSS-DR9"

C1["optu_cfht_fdm"] = 19.85424042
C1["optu_cfht_units"] = "AB Mag"
C1["optu_cfht_effective_wavelength"] = 354*(10**-7)
C1["optu_cfht_flag"] = 0
C1["optu_cfht_source"] = "CFHT"
C1["optg_ps1_fdm"] = 19.56292534
C1["optg_ps1_units"] = "AB Mag"
C1["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C1["optg_ps1_flag"] = 0
C1["optg_ps1_source"] = "PS1"
C1["optr_ps1_fdm"] = 19.58161163
C1["optr_ps1_units"] = "AB Mag"
C1["optr_ps1_effective_wavelength"] = 617*(10**-7)
C1["optr_ps1_flag"] = 0
C1["optr_ps1_source"] = "PS1"
C1["opti_ps1_fdm"] = 19.40238762
C1["opti_ps1_units"] = "AB Mag"
C1["opti_ps1_effective_wavelength"] = 752*(10**-7)
C1["opti_ps1_flag"] = 0
C1["opti_ps1_source"] = "PS1"
C1["optz_ps1_fdm"] = 19.48517799
C1["optz_ps1_units"] = "AB Mag"
C1["optz_ps1_effective_wavelength"] = 866*(10**-7)
C1["optz_ps1_flag"] = 0
C1["optz_ps1_source"] = "PS1"


C1["fuv_fdm"] = "n/a"
C1["fuv_units"] = "AB Mag"
C1["fuv_effective_wavelength"] = "n/a"  # 1516*10**-8
C1["fuv_flag"] = "n/a"
C1["fuv_source"] = "GALEX-DR5(MIS)"
C1["nuv_fdm"] = 21.605
C1["nuv_units"] = "AB Mag"
C1["nuv_effective_wavelength"] = 2267*(10**-8)
C1["nuv_flag"] = 0
C1["nuv_source"] = "GALEX-DR5(MIS)"

C1["xray_flux"] = 5.3153e-14
C1["xray_fdm"] = 1.298e-14
C1["xray_units"] = "erg/cm^2/keV/s"
C1["xray_effective_energy"] = 2
C1["xray_flag"] = 0
C1["xray_source"] = "XMM-Newtwon-DR6"
