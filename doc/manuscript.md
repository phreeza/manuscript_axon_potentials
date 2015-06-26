---
geometry: a4paper
documentclass: article
author: 'Thomas McColgan, Hermann Wagner, Richard Kempter'
title: Extracellular potentials of axonal projections including terminations and bifurcations

date: \today
...

Introduction
==============

Extracellular field potentials (EFPs) in the brain were long thought to be
primarily synaptic in origin [@BuzsAki2012Origin]. However, a number of recent
data analysis and modeling studies have shown that active, non-synaptic
membrane currents can play a role in generating EFPs [@Reimann2013Biophysically]. 

It has been shown [@Kuokkanen2010Origin], that with sufficient spatial and temporal
organization purely axonal extracellular fields can reach strengths on the
order of several mV. Here we extend this finding to include more general axon
bundles, including those recieving input with less temporal precision.

The aim of this study is to understand how the EFP is influenced by
the anatomical structure of the axons which are the source of the potential. In
particular, we explain how typical projection patterns in which an axon bundle
widens and then terminates in its projection area affect the EFP.

Such axon bundles exist throughout the peripheral and central nervous system.
(Examples...) The white matter of the brain can be viewed as an aglomeration of
such bundles. (ref) The study of the fields has clinical relevance (motor
nerve, ABR, EEG?)

Based on a forward model of the extracellular field potential
[@Holt1999Electrical,@Gold2006Origin], we characterize three principal effects
of axon bundle structure on the EFP, and demonstrate them using two models of
varying complexity, as well as a set of electrophysiological recordings from
the barn owl brain stem.

- cite: holt&koch, gold&koch, trayanova, gydkov, plonsey, rall, Rinzel, einevol,
  Destexe, Brette, nunez&..., kuokkanen, telenzuk, rattay&danner, cec email ref

Results
==============
- Axonal projections generate a dipole-like field potential (**Fig 1A**)
    - long range
    - low frequency
    - Examples of phenomenology from literature
- General results for axonal projections :
    - The low-frequency (eg population rate pulse) parts are governed by the 
      local density of bifurcations and terminations(**Fig 1B**)
    - The high-frequency (eg individual spikes, 'noise', neurophonic) parts
      are governed by the local fiber density(**Fig 1C**)
    - The low-frequency component exceeds the high-frequency component in reach (**Fig 2**)
- The barn owl neurophonic as an example that shows these properties(**Fig 3**)
    - The high-frequency component shows a steady increase in latency along the
      projections' depth, while the low-frequency can have stationary parts
      caused by sharp increases or decreases of fiber number (bifurcations or
      terminations).
    - These aspects are reflected in the model
- Ways of understanding the effect
    - Single AP along single axon(**Fig 4**)
    - Analytical model(**Fig 5**)

Discussion
==============

- Relevance of Findings
    - Interpretation of CSD
        - Classical CSD: constant fiber density, variable currents
        - Here: variable fiber density, constant currents
    - Dipole has far field, ABR response?
- Compare to other auditory systems (Chicken NL, MSO)
    - Speculate on functional relevance of polarity shift (a la Rinzel & Goldwyn)
- compare to other fiber bundle systems

Methods
==============
- Experimental Methods
- Multicompartment Model
- Analytical Model

![Axonal projections generate a dipole-like extracellular field potential.
Extracellular evoked potential due to a pulse of activity in a generic fiber
bundle. (**A**) shows the structure of the bundle, as well as EFP responses at
various locations, indicated by blue dots. Scaling of traces indicated by
colorbar. Relative strength of high-frequency noise relative to the
low-frequency pulse decays with distance. The low frequency pulse switches
polarity along the nerve bundles termination zone. (**B**) shows the density of
bifurcations and terminations at varying depths, overlayed with the peak
amplitude of the low frequency component. (**C**) shows the fiber density
overlayed with the strength of the high-frequency EFP component.
](../figs/mockups/fig1.pdf)

\clearpage

![Low-frequency component of the axon bundle EFP exceeds high frequency in
reach. (**A**) shows the behaviour of different spectral components (frequency
indicated by colorbar) in a double logarithmic plot. The slope indicates the
scaling coefficient in this frequency band. (**B**) shows this scaling
coefficient for different frequencies. Low frequencies have the least negative
coefficient, indicating the furthest reach.](../figs/mockups/fig2.pdf)

\clearpage

![Data from the barn owl shows the expected behaviour predicted by the model.
(**A**) shows data from the barn owls nucleus laminaris in response to an
auditory click stimulus, compared to a simulation of the axonal structure and
activation in (**B**). The click stimulus induces a pulse of activity in the
afferent axon bundle. The low-frequency components (**Ab** and **Bb**) show the
polarity reversal. The high frequency component (**Ac** and **Bc**, does not
show such a reversal, but rather shows a steady increase in phase with
depth.](../figs/mockups/fig3.pdf)

\clearpage

![The dipolar behaviour can be understood by examining individual action
potentials on a single axon tree. Comparing the low frequency owl data (**A**)
to a single axon and action potential in model (**B**) shows a similar
behaviour. In particular, the potential at a termination and that at a
bifurcation (red and green curves in **B**) are approximately
inverted.](../figs/mockups/fig4.pdf)

\clearpage

![Analytical model of the axon bundle potential explains the effects observed
in the numerical model and example data. (**A**) shows the behaviour of a
simplified fiber bundle with a piecewise constant fiber density (**Aa**). The
high frequency component (**Ab**) shows no polarity reversal, while the
high-frequency component (**Ac**) does, as expected from the data and
modelling. This can be understood by decomposing the signal into two
components. The first component is governed by the bifurcation and termination
density, and is filtered by the regular weighting function (**Ba**), which acts
as a low-pass filter (**Bb**). The second component is governed by the
fiber density, and is filtered by the derivative of the weighting function
(**Bc**), which acts as a high- or band-pass filter
(**Bd**).](../figs/mockups/fig5.pdf)
