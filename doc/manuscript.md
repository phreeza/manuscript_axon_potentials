---
geometry: a4paper
documentclass: article
author: 'Thomas McColgan, Hermann Wagner, Richard Kempter'
title: Extracellular potentials of coherently stimulated populations of parallel axons
    
date: \today
...

Introduction
==============

- EFPs have recently been shown to be not only of synaptic origin

- The aim of this study is to understand how the neurophonic EFP is influenced by the anatomical
structure of the axons which are the source of the potential.

- This study is mainly concerned with click responses, which have two main components (Fig 1A&B)

- Low frequency click response shows polarity reversal. (Fig 1C)
    * Similar effect seen in chicken and mamals.
    * Previous models focus on dendrites, but there are no dendrites in high-f NL.


- Basic idea outline
    * interplay of bifurcations and terminations leads to dipole-like behaviour (Fig 1D)

Methods
==============
- Experimental Methods
- Multicompartment Model
- Analytical Model

Results
==============
- Intuitive explanation
    * Single axon tree potentials (Fig 1D)
- Population response has three main characteristics (Fig 2)
    1. The low-frequency component shows a polarity reversal in the center of NL
    2. The low-frequency component exceeds NL in reach, while the high-frequency component is present
mainly inside NL.
    3. The high-frequency component shows a steady increase in latency with depth, while the low-frequency
component is stationary
- Data overview (Fig 3)
    * Shares same characteristics seen in model
- Analytical results
    * decompose response into two components
    * high-pass low-reach/low-pass high-reach (Fig 4)
    * Simulation with fiber bundle also reproduces 3 characteristics (Fig 5)

Discussion
==============

- Relevance of Findings
    * Interpretation of CSD
    * Dipole has far field, ABR response?
- Compare to other auditory systems (Chicken NL, MSO)
    - Speculate on functional relevance of polarity shift (a la Rinzel & Goldwyn)
- compare to other fiber bundle systems


![Introduction Figure](../figs/fig_1.pdf)


![](../../axon_lfp/figures/raw_filt_traces_ipsi_thinned_mod.pdf)


![](../../axon_lfp/figures/sim_filt_traces_mod_n5000.pdf)

![Impulse responses (left column) and frequency responses (right column) of the regular weighting functions $w$ (a-b) and the derivative $w'$ (c-d).](../../axon_lfp/figures/filters.pdf)

![Minimal model of a bifurcating axon bundle. The number of fibers is a piecewise constant function of recording depth, shown on the left hand side. The center and right column show the field potential responses at various depths. The low-frequency component of the response, shown in the right column, shows a characteristic dipole-like behavior. The distance from the bundle was $\rho=200\mu$m, and the velocity $v=5$m/s.](../../axon_lfp/figures/minimal_model.pdf)
