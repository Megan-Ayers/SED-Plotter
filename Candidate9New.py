#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 11:54:19 2017

This is the data file for CANDIDATE 9.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013) *** r = 8.110 arcsecs ***
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012) (LAS)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    UV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (AIS)
    X-ray from XMM-Newton Serendipitous Source Catalogue 3XMM-DR6 
    (XMM-SSC, 2016) *** r = 2.34 ***

***Missing FUV

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 9

C9 = {}
C9["ra"] = 149.4989
C9["dec"] = 2.7827
C9["z"] = 2.376

C9["mag_error_mirw1"] = 0.033
C9["mag_error_mirw2"] = 0.047
C9["mag_error_mirw3"] = 0.143
C9["mag_error_mirw4"] = 0.470
C9["mag_error_nirj"] = 0.177
C9["mag_error_nirk"] = 0.101
C9["mag_error_sdss_u"] = 0.058
C9["mag_error_sdss_g"] = 0.019
C9["mag_error_sdss_r"] = 0.026
C9["mag_error_sdss_i"] = 0.039
C9["mag_error_sdss_z"] = 0.080
C9["mag_error_fuv"] = "n/a"
C9["mag_error_nuv"] = 0.239
C9["mag_xray_error"] = 6.43e-15

C9["E(B-V)_UKIRT_J"] = 0.014
C9["E(B-V)_UKIRT_K"] =  0.006
C9["E(B-V)_SDSS_u"] = 0.083
C9["E(B-V)_SDSS_g"] = 0.064
C9["E(B-V)_SDSS_r"] = 0.045
C9["E(B-V)_SDSS_i"] = 0.033
C9["E(B-V)_SDSS_z"] = 0.025
C9["E(B-V)_PS1_g"] = 0.062
C9["E(B-V)_PS1_r"] = 0.044
C9["E(B-V)_PS1_i"] = 0.033
C9["E(B-V)_PS1_z"] = 0.026


C9["radio_fdm"] = 1.12
C9["radio_units"] = "mJ/beam"
C9["radio_effective_frequency"] = 1400*10**6
C9["radio_flag"] = 1
C9["radio_source"] = "FIRST"

C9["mirw1_fdm"] = 14.686
C9["mirw1_units"] = "Vega Mag"
C9["mirw1_effective_wavelength"] = 3.35*10**(-4)
C9["mirw1_flag"] = 0
C9["mirw1_source"] = "AllWISE"
C9["mirw1_Vega_0magflux"] = 309.540
C9["mirw2_fdm"] = 14.111
C9["mirw2_units"] = "Vega Mag"
C9["mirw2_effective_wavelength"] = 4.6*(10**-4)
C9["mirw2_flag"] = 0
C9["mirw2_source"] = "AllWISE"
C9["mirw2_Vega_0magflux"] = 171.787
C9["mirw3_fdm"] = 11.134
C9["mirw3_units"] = "Vega Mag"
C9["mirw3_effective_wavelength"] = 11.6*(10**-4)
C9["mirw3_flag"] = 0
C9["mirw3_source"] = "AllWISE"
C9["mirw3_Vega_0magflux"] = 31.674
C9["mirw4_fdm"] = 8.761
C9["mirw4_units"] = "Vega Mag"
C9["mirw4_effective_wavelength"] = 22.1*(10**-4)
C9["mirw4_flag"] = 0
C9["mirw4_source"] = "AllWISE"
C9["mirw4_Vega_0magflux"] = 8.363

C9["nirj_fdm"] = 19.303
C9["nirj_units"] = "Vega Mag"
C9["nirj_effective_wavelength"] = 1.248*(10**-4)
C9["nirj_flag"] = 0
C9["nirj_source"] = "UKIDSS-DR9"
C9["nirj_Vega_0magflux"] = 1530
C9["nirk_fdm"] = 17.443
C9["nirk_units"] = "Vega Mag"
C9["nirk_effective_wavelength"] = 2.201*(10**-4)
C9["nirk_flag"] = 0
C9["nirk_source"] = "UKIDSS-DR9"
C9["nirk_Vega_0magflux"] = 631

C9["optu_sdss_fdm"] = 20.671
C9["optu_sdss_units"] = "AB Mag"
C9["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C9["optu_sdss_flag"] = 0
C9["optu_sdss_source"] = "SDSS-DR9"
C9["optg_sdss_fdm"] = 20.183
C9["optg_sdss_units"] = "AB Mag"
C9["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C9["optg_sdss_flag"] = 0
C9["optg_sdss_source"] = "SDSS-DR9"
C9["optr_sdss_fdm"] = 20.067
C9["optr_sdss_units"] = "AB Mag"
C9["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C9["optr_sdss_flag"] = 0
C9["optr_sdss_source"] = "SDSS-DR9"
C9["opti_sdss_fdm"] = 20.020
C9["opti_sdss_units"] = "AB Mag"
C9["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C9["opti_sdss_flag"] = 0
C9["opti_sdss_source"] = "SDSS-DR9"
C9["optz_sdss_fdm"] = 19.562
C9["optz_sdss_units"] = "AB Mag"
C9["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C9["optz_sdss_flag"] = 0
C9["optz_sdss_source"] = "SDSS-DR9"

C9["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C9["optu_cfht_units"] = "AB Mag"
C9["optu_cfht_effective_wavelength"] = 354*(10**-7)
C9["optu_cfht_flag"] = 0
C9["optu_cfht_source"] = "CFHT"
C9["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C9["optg_ps1_units"] = "AB Mag"
C9["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C9["optg_ps1_flag"] = 0
C9["optg_ps1_source"] = "PS1"
C9["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C9["optr_ps1_units"] = "AB Mag"
C9["optr_ps1_effective_wavelength"] = 617*(10**-7)
C9["optr_ps1_flag"] = 0
C9["optr_ps1_source"] = "PS1"
C9["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C9["opti_ps1_units"] = "AB Mag"
C9["opti_ps1_effective_wavelength"] = 752*(10**-7)
C9["opti_ps1_flag"] = 0
C9["opti_ps1_source"] = "PS1"
C9["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C9["optz_ps1_units"] = "AB Mag"
C9["optz_ps1_effective_wavelength"] = 866*(10**-7)
C9["optz_ps1_flag"] = 0
C9["optz_ps1_source"] = "PS1"

C9["fuv_fdm"] = "n/a"
C9["fuv_units"] = "AB Mag"
C9["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C9["fuv_flag"] = "n/a"
C9["fuv_source"] = "GALEX-DR5(MIS)"
C9["nuv_fdm"] = 21.221
C9["nuv_units"] = "AB Mag"
C9["nuv_effective_wavelength"] = 2267*(10**-8)
C9["nuv_flag"] = 0
C9["nuv_source"] = "GALEX-DR5(MIS)"

C9["xray_flux"] = 5.1961e-14
C9["xray_fdm"] = 1.269e-14
C9["xray_units"] = "erg/cm^2/keV/s"
C9["xray_effective_energy"] = 2
C9["xray_flag"] = 0
C9["xray_source"] = "XMM-Newtwon-DR6"
