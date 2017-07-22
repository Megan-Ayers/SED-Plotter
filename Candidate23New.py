#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:58:30 2017

This is the data file for CANDIDATE 23.

Assume that all effective wavelengths are in cm, all effective
frequencies are in hz, and the effective energies for xray is in keV.

Notes:
    MIR from AllWISE Data Release (Cutri+ 2013)
    NIR from UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012)
    Opt from The SDSS Photometric Catalog, Release 9 (Adelman-McCarthy+, 2012)
    UV from GALEX-DR5 (GR5) sources from AIS and MIS (Bianchi+ 2011) (MIS)
    
    ***Missing x-ray

@author: megan
"""

from CFHT_PS1Readin import cfht_ps1_data_list

candidate_num = 23

C23 = {}
C23["ra"] = 333.0298
C23["dec"] = 0.9687
C23["z"] = 1.284

C23["mag_error_mirw1"] = 0.117
C23["mag_error_mirw2"] = 0.131
C23["mag_error_mirw3"] = "n/a"
C23["mag_error_mirw4"] = "n/a"
C23["mag_error_nirj"] = 0.036
C23["mag_error_nirk"] = 0.022
C23["mag_error_sdss_u"] = 0.169
C23["mag_error_sdss_g"] = 0.074
C23["mag_error_sdss_r"] = 0.057
C23["mag_error_sdss_i"] = 0.101
C23["mag_error_sdss_z"] = 0.528
C23["mag_error_fuv"] = 0.341
C23["mag_error_nuv"] = 0.110

C23["E(B-V)_UKIRT_J"] = 0.030
C23["E(B-V)_UKIRT_K"] = 0.013
C23["E(B-V)_SDSS_u"] = 0.178
C23["E(B-V)_SDSS_g"] = 0.139
C23["E(B-V)_SDSS_r"] = 0.096
C23["E(B-V)_SDSS_i"] = 0.071
C23["E(B-V)_SDSS_z"] = 0.053
C23["E(B-V)_PS1_g"] = 0.133
C23["E(B-V)_PS1_r"] = 0.095
C23["E(B-V)_PS1_i"] = 0.071
C23["E(B-V)_PS1_z"] = 0.056

C23["radio_fdm"] = 0.79
C23["radio_units"] = "mJ/beam"
C23["radio_effective_frequency"] = 1400*10**6
C23["radio_flag"] = 1
C23["radio_source"] = "FIRST"

C23["mirw1_fdm"] = 16.946
C23["mirw1_units"] = "Vega Mag"
C23["mirw1_effective_wavelength"] = 3.35*10**(-4)
C23["mirw1_flag"] = 0
C23["mirw1_source"] = "AllWISE"
C23["mirw1_Vega_0magflux"] = 309.540
C23["mirw2_fdm"] = 15.676
C23["mirw2_units"] = "Vega Mag"
C23["mirw2_effective_wavelength"] = 4.6*(10**-4)
C23["mirw2_flag"] = 0
C23["mirw2_source"] = "AllWISE"
C23["mirw2_Vega_0magflux"] = 171.787
C23["mirw3_fdm"] = 12.566
C23["mirw3_units"] = "Vega Mag"
C23["mirw3_effective_wavelength"] = 11.6*(10**-4)
C23["mirw3_flag"] = 1
C23["mirw3_source"] = "AllWISE"
C23["mirw3_Vega_0magflux"] = 31.674
C23["mirw4_fdm"] = 8.835
C23["mirw4_units"] = "Vega Mag"
C23["mirw4_effective_wavelength"] = 22.1*(10**-4)
C23["mirw4_flag"] = 1
C23["mirw4_source"] = "AllWISE"
C23["mirw4_Vega_0magflux"] = 8.363

C23["nirj_fdm"] = 20.114
C23["nirj_units"] = "Vega Mag"
C23["nirj_effective_wavelength"] = 1.248*(10**-4)
C23["nirj_flag"] = 0
C23["nirj_source"] = "UKIDSS-DR9"
C23["nirj_Vega_0magflux"] = 1530
C23["nirk_fdm"] = 18.309
C23["nirk_units"] = "Vega Mag"
C23["nirk_effective_wavelength"] = 2.201*(10**-4)
C23["nirk_flag"] = 0
C23["nirk_source"] = "UKIDSS-DR9"
C23["nirk_Vega_0magflux"] = 631

C23["optu_sdss_fdm"] = 21.898
C23["optu_sdss_units"] = "AB Mag"
C23["optu_sdss_effective_wavelength"] = 354.3*(10**-7)
C23["optu_sdss_flag"] = 0
C23["optu_sdss_source"] = "SDSS-DR9"
C23["optg_sdss_fdm"] = 22.003
C23["optg_sdss_units"] = "AB Mag"
C23["optg_sdss_effective_wavelength"] = 477.0*(10**-7)
C23["optg_sdss_flag"] = 0
C23["optg_sdss_source"] = "SDSS-DR9"
C23["optr_sdss_fdm"] = 21.307
C23["optr_sdss_units"] = "AB Mag"
C23["optr_sdss_effective_wavelength"] = 623.1*(10**-7)
C23["optr_sdss_flag"] = 0
C23["optr_sdss_source"] = "SDSS-DR9"
C23["opti_sdss_fdm"] = 21.398
C23["opti_sdss_units"] = "AB Mag"
C23["opti_sdss_effective_wavelength"] = 762.5*(10**-7)
C23["opti_sdss_flag"] = 0
C23["opti_sdss_source"] = "SDSS-DR9"
C23["optz_sdss_fdm"] = 21.871
C23["optz_sdss_units"] = "AB Mag"
C23["optz_sdss_effective_wavelength"] = 913.4*(10**-7)
C23["optz_sdss_flag"] = 0
C23["optz_sdss_source"] = "SDSS-DR9"

C23["optu_cfht_fdm"] = cfht_ps1_data_list[candidate_num][2]
C23["optu_cfht_units"] = "AB Mag"
C23["optu_cfht_effective_wavelength"] = 354*(10**-7)
C23["optu_cfht_flag"] = 0
C23["optu_cfht_source"] = "CFHT"
C23["optg_ps1_fdm"] = cfht_ps1_data_list[candidate_num][3]
C23["optg_ps1_units"] = "AB Mag"
C23["optg_ps1_effective_wavelength"] = 481.0*(10**-7)
C23["optg_ps1_flag"] = 0
C23["optg_ps1_source"] = "PS1"
C23["optr_ps1_fdm"] = cfht_ps1_data_list[candidate_num][4]
C23["optr_ps1_units"] = "AB Mag"
C23["optr_ps1_effective_wavelength"] = 617*(10**-7)
C23["optr_ps1_flag"] = 0
C23["optr_ps1_source"] = "PS1"
C23["opti_ps1_fdm"] = cfht_ps1_data_list[candidate_num][5]
C23["opti_ps1_units"] = "AB Mag"
C23["opti_ps1_effective_wavelength"] = 752*(10**-7)
C23["opti_ps1_flag"] = 0
C23["opti_ps1_source"] = "PS1"
C23["optz_ps1_fdm"] = cfht_ps1_data_list[candidate_num][6]
C23["optz_ps1_units"] = "AB Mag"
C23["optz_ps1_effective_wavelength"] = 866*(10**-7)
C23["optz_ps1_flag"] = 0
C23["optz_ps1_source"] = "PS1"

C23["fuv_fdm"] = 23.622
C23["fuv_units"] = "AB Mag"
C23["fuv_effective_wavelength"] = 1516*10**-8
C23["fuv_flag"] = 0
C23["fuv_source"] = "GALEX-DR5(MIS)"
C23["nuv_fdm"] = 21.962
C23["nuv_units"] = "AB Mag"
C23["nuv_effective_wavelength"] = 2267*(10**-8)
C23["nuv_flag"] = 0
C23["nuv_source"] = "GALEX-DR5(MIS)"

C23["xray_flux"] = "n/a"
C23["xray_fdm"] = "n/a"
C23["xray_units"] = "erg/cm^2/keV/s"
C23["xray_effective_energy"] = "n/a" # 2
C23["xray_flag"] = "n/a"
C23["xray_source"] = "XMM-Newtwon-DR6"

