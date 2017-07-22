#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 15:01:48 2017

This is the data file for CANDIDATE 24.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012) (DXS)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    UV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (MIS)
    
    ***Missing FUV, x-ray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 24

C24 = {}
C24["ra"] = 333.9833
C24["dec"] = 1.0242
C24["z"] = 2.234

C24["mag_error_mirw1"] = 0.047
C24["mag_error_mirw2"] = 0.053
C24["mag_error_mirw3"] = 0.264
C24["mag_error_mirw4"] = 0.452
C24["mag_error_nirj"] = 0.008
C24["mag_error_nirk"] = 0.006
C24["mag_error_sdss_u"] = 0.036
C24["mag_error_sdss_g"] = 0.009
C24["mag_error_sdss_r"] = 0.011
C24["mag_error_sdss_i"] = 0.014
C24["mag_error_sdss_z"] = 0.038
C24["mag_error_fuv"] = "n/a"
C24["mag_error_nuv"] = 0.423

C24["E(B-V)_UKIRT_J"] = 0.033
C24["E(B-V)_UKIRT_K"] = 0.014
C24["E(B-V)_SDSS_u"] = 0.198
C24["E(B-V)_SDSS_g"] = 0.155
C24["E(B-V)_SDSS_r"] = 0.107
C24["E(B-V)_SDSS_i"] = 0.079
C24["E(B-V)_SDSS_z"] = 0.059
C24["E(B-V)_PS1_g"] = 0.148
C24["E(B-V)_PS1_r"] = 0.106
C24["E(B-V)_PS1_i"] = 0.079
C24["E(B-V)_PS1_z"] = 0.062

C24["radio_fdm"] = 0.93
C24["radio_units"] = "mJ/beam"
C24["radio_effective_frequency"] = 1400*10**6
C24["radio_flag"] = 1
C24["radio_source"] = "FIRST"

C24["mirw1_fdm"] = 15.723
C24["mirw1_units"] = "Vega Mag"
C24["mirw1_effective_wavelength"] = 3.35*10**(-4)
C24["mirw1_flag"] = 0
C24["mirw1_source"] = "AllWISE"
C24["mirw1_Vega_0magflux"] = 309.540
C24["mirw2_fdm"] = 14.386
C24["mirw2_units"] = "Vega Mag"
C24["mirw2_effective_wavelength"] = 4.6*(10**-4)
C24["mirw2_flag"] = 0
C24["mirw2_source"] = "AllWISE"
C24["mirw2_Vega_0magflux"] = 171.787
C24["mirw3_fdm"] = 11.520
C24["mirw3_units"] = "Vega Mag"
C24["mirw3_effective_wavelength"] = 11.6*(10**-4)
C24["mirw3_flag"] = 0
C24["mirw3_source"] = "AllWISE"
C24["mirw3_Vega_0magflux"] = 31.674
C24["mirw4_fdm"] = 8.893
C24["mirw4_units"] = "Vega Mag"
C24["mirw4_effective_wavelength"] = 22.1*(10**-4)
C24["mirw4_flag"] = 0
C24["mirw4_source"] = "AllWISE"
C24["mirw4_Vega_0magflux"] = 8.363

C24["nirj_fdm"] = 17.676
C24["nirj_units"] = "Vega Mag"
C24["nirj_effective_wavelength"] = 1.248*(10**-4)
C24["nirj_flag"] = 0
C24["nirj_source"] = "UKIDSS-DR9"
C24["nirj_Vega_0magflux"] = 1530
C24["nirk_fdm"] = 16.404
C24["nirk_units"] = "Vega Mag"
C24["nirk_effective_wavelength"] = 2.201*(10**-4)
C24["nirk_flag"] = 0
C24["nirk_source"] = "UKIDSS-DR9"
C24["nirk_Vega_0magflux"] = 631

C24["optu_sdss_fdm"] = 19.869
C24["optu_sdss_units"] = "AB Mag"
C24["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C24["optu_sdss_flag"] = 0
C24["optu_sdss_source"] = "SDSS-DR9"
C24["optg_sdss_fdm"] = 19.064
C24["optg_sdss_units"] = "AB Mag"
C24["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C24["optg_sdss_flag"] = 0
C24["optg_sdss_source"] = "SDSS-DR9"
C24["optr_sdss_fdm"] = 18.830
C24["optr_sdss_units"] = "AB Mag"
C24["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C24["optr_sdss_flag"] = 0
C24["optr_sdss_source"] = "SDSS-DR9"
C24["opti_sdss_fdm"] = 18.736
C24["opti_sdss_units"] = "AB Mag"
C24["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C24["opti_sdss_flag"] = 0
C24["opti_sdss_source"] = "SDSS-DR9"
C24["optz_sdss_fdm"] = 18.523
C24["optz_sdss_units"] = "AB Mag"
C24["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C24["optz_sdss_flag"] = 0
C24["optz_sdss_source"] = "SDSS-DR9"

C24["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C24["optu_cfht_units"] = "AB Mag"
C24["optu_cfht_effective_wavelength"] = 354*(10**-7)
C24["optu_cfht_flag"] = 0
C24["optu_cfht_source"] = "CFHT"
C24["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C24["optg_ps1_units"] = "AB Mag"
C24["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C24["optg_ps1_flag"] = 0
C24["optg_ps1_source"] = "PS1"
C24["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C24["optr_ps1_units"] = "AB Mag"
C24["optr_ps1_effective_wavelength"] = 617*(10**-7)
C24["optr_ps1_flag"] = 0
C24["optr_ps1_source"] = "PS1"
C24["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C24["opti_ps1_units"] = "AB Mag"
C24["opti_ps1_effective_wavelength"] = 752*(10**-7)
C24["opti_ps1_flag"] = 0
C24["opti_ps1_source"] = "PS1"
C24["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C24["optz_ps1_units"] = "AB Mag"
C24["optz_ps1_effective_wavelength"] = 866*(10**-7)
C24["optz_ps1_flag"] = 0
C24["optz_ps1_source"] = "PS1"

C24["fuv_fdm"] = "n/a"
C24["fuv_units"] = "AB Mag"
C24["fuv_effective_wavelength"] = "n/a" # 1516*10**-8
C24["fuv_flag"] = "n/a"
C24["fuv_source"] = "GALEX-DR5(MIS)"
C24["nuv_fdm"] = 24.230
C24["nuv_units"] = "AB Mag"
C24["nuv_effective_wavelength"] = 2267*(10**-8)
C24["nuv_flag"] = 0
C24["nuv_source"] = "GALEX-DR5(MIS)"

C24["xray_flux"] = "n/a"
C24["xray_fdm"] = "n/a"
C24["xray_units"] = "erg/cm^2/keV/s"
C24["xray_effective_energy"] = "n/a" # 2
C24["xray_flag"] = "n/a"
C24["xray_source"] = "XMM-Newtwon-DR6"
