#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:33:30 2017

This program will plot data on the 26 candidates to create an SED overlayed on
the normalized Elvis et al. (1994) radio loud and radio quiet SEDs.

@author: megan
"""
import math
import numpy as np
np.set_printoptions(threshold=np.nan)
import matplotlib.pyplot as plt
import matplotlib.axes as axes

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
from MEDNormalizer import MED_RQ_normfreq_all, MED_RQ_normlum_all
from MEDNormalizer import MED_RL_normfreq_all, MED_RL_normlum_all
from MEDNormalizer import rq_red_chi_sq_lst, rl_red_chi_sq_lst
from MEDNormalizer import delta_finals_all, log_norm_freq_lums_all 
from MEDNormalizer import log_norm_rest_freqs_all

CandidateList = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14,
                 C15, C16, C17, C18, C19, C20, C21, C22, C23, C24, C25, C26]

candidate_num = 1
for candidate in CandidateList:
    
    # To make referencing the individual candidates' lists easier, I will pull them
    # out of the total lists and rename them here.
    
    plot_nu_rest = all_rest_effective_frequencies[candidate_num]
    plot_ps1_nu_rest = all_ps1_rest_effective_frequencies[candidate_num]
    
    delta_final = delta_finals_all[candidate_num]
    
    plot_rest_lum = all_rest_luminosity[candidate_num]
    plot_ps1_lum = all_ps1_rest_luminosity[candidate_num]
    
    MED_RQ_freq_normalized = MED_RQ_normfreq_all[candidate_num]
    MED_RQ_flux_normalized = MED_RQ_normlum_all[candidate_num]
    
    MED_RL_freq_normalized = MED_RL_normfreq_all[candidate_num]
    MED_RL_flux_normalized = MED_RL_normlum_all[candidate_num]
    
    log_norm_rest_freq = log_norm_rest_freqs_all[candidate_num]
    log_norm_freq_lum = log_norm_freq_lums_all[candidate_num]

    # I want to plot the log of the rest effective frequencies by the log of
    # the rest luminosity times the rest effective frequency. PS1 data will
    # be in open boxes, and the rest in filled boxes.

    plot_x = np.log10(np.array(plot_nu_rest))
    plot_y = np.log10(np.array(plot_nu_rest) * np.array(plot_rest_lum))
    
    plot_ps1_x = np.log10(np.array(plot_ps1_nu_rest))
    plot_ps1_y = np.log10(np.array(plot_ps1_nu_rest) * np.array(plot_ps1_lum))
    
    # And then I plot!
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.scatter(plot_x, plot_y, c='black', marker='s', s = 10, zorder = 10)
    
    
    # ax.scatter(plot_ps1_x, plot_ps1_y, facecolor = 'none', edgecolor = 'black',
    #            marker='s', s = 35, zorder = 5)
    ax.scatter(MED_RL_freq_normalized, MED_RL_flux_normalized, c='dimgray',
               marker='o', s = 5, zorder = 0)
    ax.scatter(MED_RQ_freq_normalized, MED_RQ_flux_normalized, c='darkgray',
               marker='o', s = 5, zorder = 1)
    ax.set_ylabel('log$(\u03BD_{rest} \circ L_{rest})$')
    ax.set_xlabel('log$(\u03BD_{rest})$')
    
    # plt.axvline(x = 15.39, c = 'green')
    
    x_min = min(log_norm_rest_freq) - 0.15
    x_max = max(log_norm_rest_freq) + 0.15
    y_min = min(log_norm_freq_lum) - 0.60
    y_max = max(log_norm_freq_lum) + 0.60
    
    plt.axis([x_min, x_max, y_min, y_max])
    
    ax.errorbar(log_norm_rest_freq, log_norm_freq_lum, yerr=delta_final,
                fmt='none', ecolor='black', zorder = 100)
    
    # I add an arrow for points which are upper limits.
    
    flag_list = [candidate["radio_flag"], candidate["mirw1_flag"],
                 candidate["mirw2_flag"], candidate["mirw3_flag"],
                 candidate["mirw4_flag"], candidate["nirj_flag"],
                 candidate["nirk_flag"], candidate["optu_sdss_flag"],
                 candidate["optg_sdss_flag"], candidate["optr_sdss_flag"],
                 candidate["opti_sdss_flag"], candidate["optz_sdss_flag"],
                 candidate["optu_cfht_flag"], candidate["optg_ps1_flag"],
                 candidate["optr_ps1_flag"], candidate["opti_ps1_flag"],
                 candidate["optz_ps1_flag"], candidate["fuv_flag"],
                 candidate["nuv_flag"], candidate["xray_flag"]]
   
    for flag in flag_list:
        if flag == "n/a":
            flag_list.remove(flag)
    
    """i = 0
    for flag in flag_list:
        if flag == 1:
            plt.text(plot_x[i], plot_y[i], u'\u2193', fontname='STIXGeneral',
                     size=20, va='top', ha='center', clip_on=True, color='k')
        i = i + 1"""
    
    # make shared x axis
    """xaxi = ax.twiny()
    # set limits for shared axis
    xaxi.set_xlim(ax.get_xlim())
    set ticks for shared axis
    wavelength_ticks = ["100 cm", "1.0 cm", "100 $\mu$m","1 $\mu$m",
                        "Ly-$\\alpha$", "100 $\AA$", "1 $\AA$"]
    xaxi.set_xticks([np.log10(3*10**8*(1 + candidate["z"])),
                     np.log10(3*10**10*(1 + candidate["z"])),
                     np.log10(3*10**12*(1 + candidate["z"])),
                     np.log10(3*10**14*(1 + candidate["z"])),
                     np.log10(2.47*10**15*(1 + candidate["z"])),
                     np.log10(3*10**16*(1 + candidate["z"])),
                     np.log10(3*10**18*(1 + candidate["z"]))])
    xaxi.set_xticklabels(wavelength_ticks)
    xaxi.set_xlabel('Wavelength')"""
    fig.tight_layout()
    
    ax.text(x_min + 0.3, y_max - 0.2, r"Candidate %s (%s, %s)"%(candidate_num, 
            candidate["ra"], candidate["dec"]), fontsize=10)
    ax.text(x_min + 0.3, y_max - 0.4, r"RQ $\chi_{red}^2$ = %s"\
            %(int(rq_red_chi_sq_lst[candidate_num])), fontsize=8)
    ax.text(x_min + 0.3, y_max - 0.55, r"RL $\chi_{red}^2$ = %s"\
            %(int(rl_red_chi_sq_lst[candidate_num])), fontsize=8)
    
    # plt.savefig('ErrorBarsCandidate%sJuly20.eps'%(candidate_num), format='eps',
    #             dpi=1000, bbox_inches='tight')
    fig.show()
    
    
    candidate_num = candidate_num + 1
    