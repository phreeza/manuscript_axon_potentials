---
geometry: a4paper
documentclass: article
figPrefix:
  - "Figure"
  - "Figures"
header-includes:
    - \usepackage{setspace}
    - \doublespacing
author: 
    - Thomas McColgan
title: Frequency resolved multipole moments
date: \today
...

To analyze the multipole moments in the far field of an idealized axon bundle, we consider the following equations. 

$$I(z,t) = \frac{d}{dz}\left(n(z)\frac{d}{dz}V(z,t)\right)$$

$$\Phi(\mathbf{r},t) = \frac{1}{4\pi\sigma_{e}}\int_{V}\frac{\delta(\rho')I(z',t)}{|\mathbf{r}-\mathbf{r}'|}\textrm{d}\mathbf{r}'\label{eq:halfline}$$

To obtain the frequency resolved power at a given location we consider

$$\tilde{I}(z,\omega) = i\frac{dn}{dz}(z)\cdot\frac{\omega}{v}\tilde{V}(z,\omega)-n(z)\cdot\frac{\omega^2}{v^2}\tilde{V}(z,\omega)$$

and the corresponding 
$$\tilde{\Phi}(\mathbf{r},\omega) = \frac{1}{4\pi\sigma_{e}}\int_{V}\frac{\delta(\rho')\tilde{I}(z,\omega)}{|\mathbf{r}-\mathbf{r}'|}\textrm{d}\mathbf{r}'\label{eq:halfline}$$

Because of the traveling wave nature of $V$ we can write $\tilde{V}(z,\omega)$ as $e^{i\frac{z\omega}{v}}\tilde{V}(0,\omega)$

and 
$$\tilde{\Phi}(\mathbf{r},\omega) = \frac{1}{4\pi\sigma_{e}}\cdot\frac{\omega}{v}\tilde{V}(0,\omega)\int_{-\infty}^\infty e^{i\frac{z'\omega}{v}}\frac{in'(z')-\frac{\omega}{v}n(z)}{\sqrt{(z-z')^2
+ \rho^2}}\textrm{d}z'\label{eq:halfline}$$

Semiinfinite bundle without projection zone
===

In this case we have $n(z) = \Theta(z)$, where $\Theta$ is the Heaviside step function. This gives us $$\tilde{\Phi}(\mathbf{r},\omega) =  \frac{1}{4\pi\sigma_{e}}\cdot\frac{\omega}{v}\tilde{V}(0,\omega)\left(\frac{i}{\sqrt{z^2+ \rho^2}}+\int_{-\infty}^0 e^{i\frac{z'\omega}{v}}\frac{\frac{\omega}{v}}{\sqrt{(z-z')^2
+ \rho^2}}\textrm{d}z'\right)$$

If we consider the potential along the extension of the bundle at $\rho=0$ for $z>0$, this becomes
$$\tilde{\Phi}(\mathbf{r},\omega) =  \frac{1}{4\pi\sigma_{e}}\cdot\frac{\omega}{v}\tilde{V}(0,\omega)\left(\frac{i}{z}+\frac{\omega e^{\frac{i \omega z}{v}} \left(\text{Ei}\left(-\frac{i \omega z}{v}\right)+i \pi \right)}{v}\right)$$

where $\text{Ei}$ is the exponential integral. Using the series expansion of $Ei$ for large $z$ we can approximate $\tilde{\Phi}$ as 
$$\tilde{\Phi}(\mathbf{r},\omega) \approx  \frac{1}{4\pi\sigma_{e}}\cdot\frac{\omega}{v}\tilde{V}(0,\omega)\left(\frac{i \pi  w e^{\frac{i \omega z}{v}}}{v}-\frac{v}{\omega z^2}-\frac{2 i v^2}{\omega^2 z^3} \right)$$

What does this mean?

Gaussian projection zone with neglected trunk
===
In this case we have $n(z) = e^{-\frac{z^2}{a^2}}$ where $a$ determines the
width of the projection zone. Because the current density decreases faster than
any power of $z$ from $z=0$, this case can be evaluated with a classical
multipole analysis.

The monopole charge $q(\omega)=\int \tilde{I}(z,\omega) \textrm{d}z$ is zero, as expected due to the conservation of charge in the system. The dipole moment $\mathbf{p}$ is zero in the radial direction for reasons of symmetry, and $$\tilde{p}_z(\omega)=\int z\tilde{I}(z,\omega)\textrm{d}z= i\tilde{V}(0,\omega)\cdot\sqrt{\pi }\frac{ a \omega}{v}  e^{-\frac{a^2 w^2}{4 v^2}}$$

This means that the relative amount of the signal passed on in a dipolar fashion from the membrane voltage, ie $\frac{\left|\tilde{p}_z(\omega)\right|}{\left|V(0,\omega)\right|}$ is a function of $\omega$ and has its maximum at $\omega_\textrm{dipole}=\sqrt{2}\frac{v}{a}$.

Todos
==

- Double check analytics 
- compare with numerical results
- Find an analytically tractable bundle and projection zone version
