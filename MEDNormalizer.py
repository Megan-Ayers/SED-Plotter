#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 18:42:19 2017

This program will normalize the Elvis et al. (1994) radio quiet and radio loud
MEDs to data from SMBHB candidates. It will also calculate the reduced chi
squared value for each fit along with different bolometric luminosities.

@author: megan
"""
import math
from astropy import units as u
import numpy as np
np.set_printoptions(threshold=np.nan)
from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)

from Candidate1New import C1
from Candidate2New import C2
from Candidate3New import C3
from Candidate4New import C4
from Candidate5New import C5
from Candidate6New import C6
from Candidate7New import C7
from Candidate8New import C8
from Candidate9New import C9
from Candidate10New import C10
from Candidate11New import C11
from Candidate12New import C12
from Candidate13New import C13
from Candidate14New import C14
from Candidate15New import C15
from Candidate16New import C16
from Candidate17New import C17
from Candidate18New import C18
from Candidate19New import C19
from Candidate20New import C20
from Candidate21New import C21
from Candidate22New import C22
from Candidate23New import C23
from Candidate24New import C24
from Candidate25New import C25
from Candidate26New import C26

from CFHT_PS1Readin import cfht_ps1_data_list
from ElvisMEDReadin import MED_RL_nu, MED_RL_flux, MED_RQ_nu, MED_RQ_flux

from SEDDataManip import *

CandidateList = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14,
                 C15, C16, C17, C18, C19, C20, C21, C22, C23, C24, C25, C26]

# I create lists that will be filled with individual lists of information or
# values for each candidate. The index of the data will correspond to the
# candidate number, which is why each list initially has a 0 in the 0th index.

log_norm_rest_freqs_all = [0]
log_norm_freq_lums_all = [0]

MED_RQ_normfreq_all = [0]
MED_RQ_normlum_all = [0]

MED_RL_normfreq_all = [0]
MED_RL_normlum_all = [0]

rq_red_chi_sq_lst = [0]
rl_red_chi_sq_lst = [0]

delta_finals_all = [0]

L_bol_data_all = [0]
L_bol_rq_all = [0]
L_bol_rl_all = [0]

candidate_num = 1
for candidate in CandidateList:

    # I use astropy to calculate the luminosity distance.
    
    d_L_units = cosmo.luminosity_distance(candidate["z"])*3.068e24
    d_L = d_L_units.value

    # To make referencing the individual candidates' lists easier, I will pull
    # them out of the compiled lists and rename them here.

    nu_rest = all_rest_effective_frequencies[candidate_num]
    mir_nu_rest = all_mir_rest_effective_frequencies[candidate_num]
    nir_nu_rest = all_nir_rest_effective_frequencies[candidate_num]
    sdss_nu_rest = all_sdss_rest_effective_frequencies[candidate_num]
    ps1_nu_rest = all_ps1_rest_effective_frequencies[candidate_num]
    uv_nu_rest = all_uv_rest_effective_frequencies[candidate_num]

    mir_fd = all_mir_flux[candidate_num]
    nir_fd = all_nir_flux[candidate_num]
    sdss_fd = all_sdss_flux[candidate_num]
    uv_fd = all_uv_flux[candidate_num]

    rest_lum = all_rest_luminosity[candidate_num]
    mir_lum = all_mir_rest_luminosity[candidate_num]
    nir_lum = all_nir_rest_luminosity[candidate_num]
    sdss_lum = all_sdss_rest_luminosity[candidate_num]
    ps1_lum = all_ps1_rest_luminosity[candidate_num]
    uv_lum = all_uv_rest_luminosity[candidate_num]

    # The first concern in normalization is making sure that I don't include
    # any upper limits in my calculation. I will search through the flags of
    # the candidates and eliminate those that have flag = 1. Those with flag =
    # n/a have already been eliminated in the data manipulation. This is only a
    # concern in the MIR since I am not including radio data in the
    # normalization. If the data is not flagged, I add it to a new list to use.
    
    # I also want to check UV data to see if it is past the ly-alpha break
    # wavelength. If so, I disregard these values in normalization.

    flag_list = [candidate["mirw1_flag"], candidate["mirw2_flag"],
                 candidate["mirw3_flag"], candidate["mirw4_flag"]]

    mir_nu_rest_ok = []
    mir_fd_ok = []
    mir_lum_ok = []
    i = 0
    for flag in flag_list:
        if flag == 0:
            mir_nu_rest_ok.append(mir_nu_rest[i])
            mir_fd_ok.append(mir_fd[i])
            mir_lum_ok.append(mir_lum[i])
        i = i + 1
    
    uv_nu_rest_ok = []
    uv_fd_ok = []
    uv_lum_ok = []
    uv_count = 0  # Counts how many UV points the candidate has.
    uv_error_flag = 0  # This will count if I have removed a uv point, so that
    # later I know to also remove the error value from the delta_m list. If
    # the candidate has two points and one flag, I know it is the FUV since it
    # is closer to ly-alpha. If there are two points and two flags, I remove
    # both, and if there is one flag and one point, I remove that point (this
    # all occurs in a function below).
    i = 0
    for item in uv_nu_rest:
        if np.log10(item) <= 15.39:
            uv_nu_rest_ok.append(uv_nu_rest[i])
            uv_fd_ok.append(uv_fd[i])
            uv_lum_ok.append(uv_lum[i])
        if np.log10(item) > 15.39:
            uv_error_flag = uv_error_flag + 1
        uv_count = uv_count + 1
        i = i + 1

    # Now that I have gotten rid of any upper limits, I recompile a list
    # of all the log(nu_rest) and log(nu_rest*L_rest) points that I will be
    # using to interpolate and normalize the Elvis MEDs.

    norm_rest_freqs = mir_nu_rest_ok + nir_nu_rest + sdss_nu_rest + \
                      uv_nu_rest_ok
    norm_lums = mir_lum_ok + nir_lum + sdss_lum + uv_lum_ok

    log_norm_rest_freqs = np.log10(norm_rest_freqs)
    log_norm_rest_freqs_all.append(log_norm_rest_freqs)  # Save list for
    # plotting all the candidates later.
    
    log_norm_freq_lums = np.log10(np.array(norm_rest_freqs) *
                         np.array(norm_lums))
    log_norm_freq_lums_all.append(log_norm_freq_lums)  # Save list for
    # plotting all the candidates later.

    # For each of the "frequency" points for which I have data, I interpolate
    # the Elvis MED value onto it. The code below searches through the Elvis
    # "frequency" list, finds the closest two flanking points to my data point,
    # and interpolates the y-axis value at that point. I do this first for the
    # RQ MED and will repeat for the RL MED. Note: I decided not to include PS1
    # in the fitting since I have no error data for it - can easily reinsert
    # later if Suvi wants.

    rq_interpolated_values = []

    for freq in log_norm_rest_freqs:  # Loop through data frequencies
        i = 0
        count = 0
        for item in MED_RQ_nu:  # For each data point, loop through Elvis freq
            diff = abs(freq - item)  # Find difference between the two
            if diff < 0.02:  # If difference is less than incrementation . . .
                if count == 0:  # And if this is the first detection . . .
                    x_a = item  # Save this freq as first x value . . .
                    y_a = MED_RQ_flux[i]   # And save corresponding flux as y.
                    count = 1  # Record that one flanking point is found
                else:
                    x_b = item  # Record as second x value . . .
                    y_b = MED_RQ_flux[i]  # Record as second y value.
            i = i + 1
        interp_pt = y_a + (y_b - y_a) / (x_b - x_a) * (freq - x_a)  # Int. flux
        rq_interpolated_values.append(interp_pt)  # Save interpolated flux
        # values to a list.
    
    # I want to find a normalization factor to multiply the MEDs by that
    # minimizes the least square value. To do this, I iteratively loop through
    # normalization factors starting from 0.985 and increasing to 1.015 by
    # increments of 0.0000001, find the resulting least square sums between the
    # normalized MED and the data, and find the minimum of those and the
    # corresponding minimizing normalization factor.
    
    rq_least_square_sums = []
    rq_normtracker = []
    rq_normfactor = 0.985
    while rq_normfactor <= 1.015:
        rq_normalized_lum = np.array(rq_interpolated_values) * rq_normfactor  
        # Create list of the residuals between this normalization and the data.
        rq_norm_residuals = []
        i = 0
        for item in rq_normalized_lum:
            residual = item - log_norm_freq_lums[i]  # Find residual between
            # normalized MED and data at each point
            rq_norm_residuals.append(residual)  # Record the residual
            i = i + 1
        rq_sum_residuals_sq = 0
        for item in rq_norm_residuals:
            rq_sum_residuals_sq = rq_sum_residuals_sq + item**2  # Add the 
            # squared residuals
        rq_least_square_sums.append(rq_sum_residuals_sq)  # Add resulting
        # sum to list of sums at different normalizations
        rq_normtracker.append(rq_normfactor)  # Record normalization factor
        # at same index as the sum to be able to find when minimizing
        rq_normfactor = rq_normfactor + 0.0000001  # Increase normfactor 
        # to loop through again.
    rq_bestnorm = min(float(item) for item in rq_least_square_sums)  # Find
    # least S
    rq_bestfactor = rq_normtracker[rq_least_square_sums.index(rq_bestnorm)]
    # Find corresponding minimizing normalization factor.
    
    # Now I repeat the process for the radio loud MED.
    
    rl_interpolated_values = []

    for freq in log_norm_rest_freqs:
        i = 0
        count = 0
        for item in MED_RL_nu:
            diff = abs(freq - item)
            if diff < 0.02:
                if count == 0:
                    x_a = item
                    y_a = MED_RL_flux[i]
                    count = 1
                else:
                    x_b = item
                    y_b = MED_RL_flux[i]
            i = i + 1
        interp_pt = y_a + (y_b - y_a) / (x_b - x_a) * (freq - x_a)
        rl_interpolated_values.append(interp_pt)

    
    rl_least_square_sums = []
    rl_normtracker = []
    rl_normfactor = 0.985
    while rl_normfactor <= 1.015:
        rl_normalized_lum = np.array(rl_interpolated_values) * rl_normfactor  
        rl_norm_residuals = []
        i = 0
        for item in rl_normalized_lum:
            residual = item - log_norm_freq_lums[i]
            rl_norm_residuals.append(residual)
            i = i + 1
        rl_sum_residuals_sq = 0
        for item in rl_norm_residuals:
            rl_sum_residuals_sq = rl_sum_residuals_sq + item**2
        rl_least_square_sums.append(rl_sum_residuals_sq)
        rl_normtracker.append(rl_normfactor)
        rl_normfactor = rl_normfactor + 0.0000001
    rl_bestnorm = min(float(item) for item in rl_least_square_sums)
    rl_bestfactor = rl_normtracker[rl_least_square_sums.index(rl_bestnorm)]
    
    # Now that I know the best normalization factor for minimizing the
    # difference between the MEDs and the data for each candidate, I will
    # multiply all of the Elvis MED data (NOT including the interpolated
    # points) by this factor for RQ and RL to have a fully fitted curve. 
    
    MED_RQ_flux_normalized = []
    for item in MED_RQ_flux:
        item = item * rq_bestfactor
        MED_RQ_flux_normalized.append(item)
    MED_RQ_normlum_all.append(MED_RQ_flux_normalized)
        
    MED_RQ_freq_normalized = []
    for item in MED_RQ_nu:
        MED_RQ_freq_normalized.append(item)
    MED_RQ_normfreq_all.append(MED_RQ_freq_normalized)
        
    # I repeat for the RL MED. . .
    
    MED_RL_flux_normalized = []
    for item in MED_RL_flux:
        item = item * rl_bestfactor
        MED_RL_flux_normalized.append(item)
    MED_RL_normlum_all.append(MED_RL_flux_normalized)
    
    MED_RL_freq_normalized = []
    for item in MED_RL_nu:
        MED_RL_freq_normalized.append(item)
    MED_RL_normfreq_all.append(MED_RL_freq_normalized)    
    
    # The four lists above can now be plotted as the normalized Elvis MED
    # curves. 
    
    """***************REDUCED CHI SQUARED**********************"""
    
    # Now I want to calculate the reduced chi squared value that corresponds
    # to each of these fits. A lot of work actually has to go into finding
    # the variance for each point, which is a result of propagating the mean
    # magnitude error on each VizieR measurement through the calculations that
    # I do for changing magnitudes into rest luminosity. This value should
    # correspond with all of the data points used in normalization, but since I
    # don't (yet) have PS1 error data, those points are excluded. Another note
    # is that in propagating the error for IR from vega mag to L_rest, I
    # multiply by 10**-23 to change from Jy to erg/hz/cm^2/s. In propagation,
    # this results in an irrationally small error value, which is not an
    # accurate comparison to the ab conversion since that flux density value
    # becomes small from the 10^(m + 48.6) addition in the exponent, something
    # not reflected in that error propagation calculation. Therefore, for now
    # I will convert the vega magnitude error to ab magnitude error using
    # addition of offsets provided by ALLWise and UKIDSS, which results in
    # errors comparable to those produced by the ab -> L_rest propagation.
    # I also ignore the calculations leading to galactic extinction, since
    # that involved only addition of a constant, which doesn't affect the
    # error of the original measurement.
    
    # Update to above discussion on Vega propagation: I consider the 10^-23
    # absorbed into the other 10^... used to go to flux density, but however,
    # now account for multiplication by the zero magnitude flux constant. This
    # makes the errors very large, though, so I'm unsure if we want to keep
    # this change.

    # I first create lists of the errors, divided into vega and ab magnitudes,
    # as well as a list of the zero magnitude flux constants.

    delta_m_v_all = [candidate["mag_error_mirw1"],
                     candidate["mag_error_mirw2"],
                     candidate["mag_error_mirw3"],
                     candidate["mag_error_mirw4"],
                     candidate["mag_error_nirj"],
                     candidate["mag_error_nirk"]]
    
    zero_mag_flux_all = [candidate["mirw1_Vega_0magflux"],
                         candidate["mirw2_Vega_0magflux"],
                         candidate["mirw3_Vega_0magflux"],
                         candidate["mirw4_Vega_0magflux"],
                         candidate["nirj_Vega_0magflux"],
                         candidate["nirk_Vega_0magflux"]]

    delta_m_ab_all = [candidate["mag_error_sdss_u"],
                      candidate["mag_error_sdss_g"],
                      candidate["mag_error_sdss_r"],
                      candidate["mag_error_sdss_i"],
                      candidate["mag_error_sdss_z"],
                      candidate["mag_error_fuv"],
                      candidate["mag_error_nuv"]]

    # ir_offsets = [2.699, 3.339, 5.174, 6.620, 0.938, 1.900]
    # W1, W2, W3, W4, NIR J, NIR K. These are actually irrelevant for the error
    # prop calculation though, since it is just an addition of a constant.
    # Therefore all error propagation calculations end up being the same.

    # I want to eliminate upper limit values, because their errors don't exist.
    # I also eliminate the items for which there is no data at all. I create a
    # new list for data that doesn't include upper limits.

    delta_m_v = []
    zero_mag_flux = []
    i = 0
    for item in delta_m_v_all:
        if type(item) == float:  # Since upper limits will have "n/a" here this
        # only accepts normal data.
            delta_m_v.append(item)
            zero_mag_flux.append(zero_mag_flux_all[i])
        i = i + 1
        
    delta_m_ab = []
    for item in delta_m_ab_all:
        if type(item) == float: # If data doesn't exist, will be "n/a" also.
            delta_m_ab.append(item)

    if uv_error_flag == 1: 
        if uv_count == 1: # If there is 1 point and 1 flag, remove the last
        # point from the list since it will be the UV point.
            delta_m_ab.remove(delta_m_ab[len(delta_m_ab) - 1])
        if uv_count == 2: # If 2 points, it is the FUV point, whicih is second
        # to last always.
            delta_m_ab.remove(delta_m_ab[len(delta_m_ab) - 2])
    if uv_error_flag == 2: # If both, remove both.
        delta_m_ab.remove(delta_m_ab[len(delta_m_ab) - 1])
        delta_m_ab.remove(delta_m_ab[len(delta_m_ab) - 2])
    
    # Now I begin calculating how the error propagates, and record the final
    # error value in the list delta_finals. Before the function I collect
    # the fluxes, frequencies, and luminosities into lists for vega and ab
    # types of magnitude.

    frequencies_v = mir_nu_rest_ok + nir_nu_rest
    fluxes_v = mir_fd_ok + nir_fd
    luminosities_v = mir_lum_ok + nir_lum

    frequencies_ab = sdss_nu_rest + uv_nu_rest_ok
    fluxes_ab = sdss_fd + uv_fd_ok
    luminosities_ab = sdss_lum + uv_lum_ok

    delta_finals = []  # This list will contain the final errors for the points
    j = 0
    # !!! Taking out zero_mag_flux[j] * stuff in delta_f, distracting
    for error in delta_m_v:
        delta_f = (fluxes_v[j] * math.log(10) * error) / 2.5
        # First propagation follows rule: if log_10(a) = x, then
        # delta_x = 1/ln(10)*delta_a/a.
        delta_L = (delta_f * 4 * math.pi * (d_L)**2) / (1 + candidate["z"])
        # Second propagation follows rule of multiplication by constant 'c':
        # x = a * C -> delta_x = delta_a * C
        delta_Lnu = delta_L * frequencies_v[j]
        # Third propagation is another multiplication by constant
        delta_logLnu = delta_Lnu / (math.log(10) * luminosities_v[j] *
                                    frequencies_v[j])
        # Fourth propagation is another log rule.
        delta_finals.append(delta_logLnu)
        j = j + 1
    j = 0
    for error in delta_m_ab:
        delta_f = (fluxes_ab[j] * math.log(10) * error) / 2.5
        # First propagation follows rule: if log_10(a) = x, then
        # delta_x = 1/ln(10)*delta_a/a.
        delta_L = (delta_f * 4 * math.pi * (d_L)**2) / (1 + candidate["z"])
        # Second propagation follows rule of multiplication by constant 'c':
        # x = a * C -> delta_x = delta_a * C
        delta_Lnu = delta_L * frequencies_ab[j]
        # Third propagation is another multiplication by constant
        delta_logLnu = delta_Lnu / (math.log(10) * luminosities_ab[j] *
                                    frequencies_ab[j])
        # Fourth propagation is another log rule.
        delta_finals.append(delta_logLnu)
        j = j + 1
    
    delta_finals_all.append(delta_finals)

    # Now that I have my "variances", I calculate the reduced chi^2 value
    # using chi^2_red = 1/nu * sum[(obs - expected)^2/variance^2], where
    # nu is the degrees of freedom which I am considering to be the number
    # of data points - 2, since nu = N-n-1 where N is the # of observations
    # and n is the number of fitted parameters. I do the same for RQ and RL.

    rq_chi_sq = 0
    i = 0
    for delta in delta_finals:
        rq_value = (log_norm_freq_lums[i] - rq_interpolated_values[i])**2 * \
        delta**-2  # Find individual values 
        rq_chi_sq = rq_chi_sq + rq_value  # Add them together in loop
        i = i + 1
    rq_red_chi_sq = rq_chi_sq/(len(log_norm_freq_lums) - 2)  # Divide by nu
    rq_red_chi_sq_lst.append(rq_red_chi_sq)
    
    rl_chi_sq = 0
    i = 0
    for delta in delta_finals:
        rl_value = (log_norm_freq_lums[i] - rl_interpolated_values[i])**2 / \
                delta**2
        rl_chi_sq = rl_chi_sq + rl_value
        i = i + 1
    rl_red_chi_sq = rl_chi_sq/(len(log_norm_freq_lums) - 2)
    rl_red_chi_sq_lst.append(rl_red_chi_sq)
    
    """***************BOLOMETRIC LUMINOSITY******************"""
    
    # The next statistic that I am interested in is the bolometric luminosity
    # of each candidate. I find this by using trapezoidal integration
    # under the luminosity values that I used for normalization (no upper
    # limits, exist between IR and UV). 
                                                                 
    # First I go through and order the lists in terms of increasing frequency,
    # which is necessary for making a loop for trapezoidal integration since
    # each area is dependent on the data point plotted next to it.
    
    copy_rest_freqs = []
    
    for item in norm_rest_freqs:
        copy_rest_freqs.append(item)  # I do this so that the original list
        # is not altered.
    
    ordered_freqs = []
    ordered_lums = []
    
    while len(ordered_freqs) < len(norm_lums):
        lowest_freq = min(copy_rest_freqs)
        ordered_freqs.append(lowest_freq)
        ordered_lums.append(norm_lums[norm_rest_freqs.index(lowest_freq)])
        copy_rest_freqs.remove(lowest_freq)
        # I remove the minimum frequency from the list and add it to the
        # ordered list along with its corresponding lum value until all are
        # gone. 
        
    # Now that the lists are properly ordered, I find L_bol for the data.
                     
    L_bol_data = 0
    i = 0
    for item in ordered_freqs[1:]:
        trap_area = 1/2 * (item - ordered_freqs[i]) * (ordered_lums[i + 1] +
                          ordered_lums[i])
        L_bol_data = L_bol_data + trap_area
        i = i + 1
    L_bol_data_all.append(L_bol_data)
    
    # Now I find L_bol for the MEDs under the same frequency range. Since the
    # MED data is only given in log(freq*lum) I need to undo the
    # log and divide the y values by their respective frequencies. First I
    # use the same process above to reorder the lists.
    
    copy_rest_freqs = []
    for item in norm_rest_freqs:
        copy_rest_freqs.append(item)  # I do this so that the original list
        # is not altered.

    ordered_freqs = []
    ordered_log_lums_rq = []
    ordered_log_lums_rl = []

    while len(ordered_freqs) < len(rq_interpolated_values):
        lowest_freq = min(copy_rest_freqs)
        ordered_freqs.append(lowest_freq)
        ordered_log_lums_rq.append(rq_interpolated_values[norm_rest_freqs.index(lowest_freq)])
        ordered_log_lums_rl.append(rl_interpolated_values[norm_rest_freqs.index(lowest_freq)])
        copy_rest_freqs.remove(lowest_freq)    
    
    ordered_lums_rq = []
    ordered_lums_rl = []
    i = 0
    for item in ordered_log_lums_rq:
        lum = 10**(item) / ordered_freqs[i]  # Undo the log, multiply by
        # appropriate frequency.
        ordered_lums_rq.append(lum)
        i = i + 1
    i = 0
    for item in ordered_log_lums_rl:
        lum = 10**(item) / ordered_freqs[i]  # Undo the log, multiply by
        # appropriate frequency.
        ordered_lums_rl.append(lum)
        i = i + 1
    
    # Now that the lists are ordered and in the right units, I find L_bol for
    # the MEDs for the same range.
    
    L_bol_rq = 0
    L_bol_rl = 0
    i = 0
    for item in ordered_freqs[1:]:
        trap_area_rq = 1/2 * (item - ordered_freqs[i]) * \
                       (ordered_lums_rq[i + 1] + ordered_lums_rq[i])
        trap_area_rl = 1/2 * (item - ordered_freqs[i]) * \
                       (ordered_lums_rl[i + 1] + ordered_lums_rl[i])
        L_bol_rq = L_bol_rq + trap_area_rq
        L_bol_rl = L_bol_rl + trap_area_rl
        i = i + 1
    L_bol_rq_all.append(L_bol_rq)
    L_bol_rl_all.append(L_bol_rl)
    
    # I now find L_bol for the entire MEDs. Luckily the Elvis data is already
    # ordered, so I just need to undo the logs and multiply the y-values then
    # by the derived effective frequencies.

    effective_freq_rq = []
    for item in MED_RQ_nu:
        freq = 10**item  #undo the log
        effective_freq_rq.append(freq)
    effective_freq_rl = []
    for item in MED_RL_nu:
        freq = 10**item  #undo the log
        effective_freq_rl.append(freq)
    
    lum_rq = []
    i = 0
    for item in MED_RQ_flux:
        lum = 10**item / effective_freq_rq[i]  # undo log and multiply by
        # appropriate effective frequency.
        lum_rq.append(lum)
        i = i + 1   
    lum_rl = []
    i = 0
    for item in MED_RL_flux:
        lum = 10**item / effective_freq_rl[i]  # undo log and multiply by
        # appropriate effective frequency.
        lum_rl.append(lum)
        i = i + 1

    # Now that everything is in the right units, I find L_bol using the
    # same process as above.

    """total_L_bol_rq = 0
    total_L_bol_rl = 0
    i = 0
    for item in effective_freq_rq[1:]:
        trap_area_rq = 1/2 * (item - ordered_freqs[i]) * \
                       (ordered_lums_rq[i + 1] + ordered_lums_rq[i])
        trap_area_rl = 1/2 * (item - ordered_freqs[i]) * \
                       (ordered_lums_rl[i + 1] + ordered_lums_rl[i])
        L_bol_rq = L_bol_rq + trap_area_rq
        L_bol_rl = L_bol_rl + trap_area_rl
        i = i + 1
    L_bol_rq_all.append(L_bol_rq)
    L_bol_rl_all.append(L_bol_rl)"""
    
    
    candidate_num = candidate_num + 1
