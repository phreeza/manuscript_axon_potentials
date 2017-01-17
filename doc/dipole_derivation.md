We consider an axon bundle in which identical spikes
with the waveform $V_\text{spike}(t,z)$ propagate as
travelling waves with a velocity $v$:
$V_\text{spike}(t,z) = V_\text{spike}(z/v-t)$. If each
of the fibers is stimulated with an inhomogeneous
Poisson process, with the driving rate $\lambda(t)$
shared among all axons, the average membrane potential
across fibers will be $V_\text{membrane}(z,t) =
V_\text{spike}(z/v-t)\ast \lambda(t)$, where $\ast$
denotes the convolution in time. Plugging this into [@eqn:current], we obtain
\begin{align}
i_m(z,t)& = \frac{\pi a^2}{r_L}\left(\frac{\partial n}{\partial z}(z)\cdot\frac{\partial}{\partial z}(V_\text{spike}(z/v-t)\ast \lambda(t))+n(z)\cdot\frac{\partial ^2}{\partial z^2}(V_\text{spike}(z/v-t)\ast \lambda(t)) \right) \\
& = \frac{\pi a^2}{r_L}\lambda(t)\ast\left(\frac{\partial n}{\partial z}(z)\cdot\frac{\partial}{\partial z}(V_\text{spike}(z/v-t))+n(z)\cdot\frac{\partial ^2}{\partial z^2}(V_\text{spike}(z/v-t)) \right)
\end{align}

Assuming Gaussian shapes for the firing rate pulse $\lambda(t) = \bar\lambda e^{-\frac{t^2}{2\sigma_\text{pulse}}}$, the spike $V_\text{spike}(z/v-t) = \bar{V}_\text{spike} e^{-\frac{(z/v-t)^2}{2\sigma_\text{spike}}}$ and the fiber bundle projection zone $n(z) = \bar{n} e^{-\frac{z^2}{2\sigma_\text{n}}}$, we are able to take advantage of the fact that the product and the convolution of two Gaussians are again Gaussian, and obtain 

\begin{align}\label{eqn:simple_dipole_cur}
i_m(z,t)&=\bar{n} \bar{\lambda }_{\text{pulse}} \bar{V}_{\text{spike}}  \sqrt{2} \pi ^{3/2} a^2  \cdot \exp \left(-\frac{z^2}{2 \sigma _n^2}-\frac{(z-t v)^2}{2 v^2 \left(\sigma _{\text{pulse}}^2+\sigma _{\text{spike}}^2\right)}\right) \\ \nonumber
&\cdot\frac{ \sigma _n^2 \left(-v^2 \sigma _{\text{pulse}}^2-v^2 \sigma _{\text{spike}}^2+(z-t v)^2\right)-v^2 z \left(\sigma _{\text{pulse}}^2+\sigma _{\text{spike}}^2\right) (t v-z)}{v^4 r_L \sigma _n^2 \sqrt{\frac{1}{\sigma _{\text{pulse}}^2}+\frac{1}{\sigma _{\text{spike}}^2}} \left(\sigma _{\text{pulse}}^2+\sigma _{\text{spike}}^2\right){}^2} \end{align}


The dipole moment $p(t)$ is defined as $$p(t) = \int_{-\infty}^{\infty}z\cdot i_m(z,t)\text{d}z$$ into which we can enter Eq. \ref{eqn:simple_dipole_cur} to obtain
$$p(t) =- \bar{n} \bar{\lambda }_{\text{pulse}} \bar{V}_{\text{spike}}\frac{2 \pi ^2 a^2}{r_L }\frac{v^2 \sigma_n \sigma_{\text{pulse}} \sigma_{\text{spike}}}{\left(\sigma _n^2+v^2 \left(\sigma _{\text{pulse}}^2+\sigma _{\text{spike}}^2\right)\right)^{3/2}}\cdot t e^{\frac{t^2 v^2}{2 \left(\sigma _n^2+v^2 \left(\sigma _{\text{pulse}}^2+\sigma _{\text{spike}}^2\right)\right)}}$$

This has its maximum amplitude at $t_\text{max}=\frac{\sqrt{\sigma _n^2+v^2 \left(\sigma _{\text{pulse}}^2+ \sigma _{\text{spike}}^2\right)}}{v}$, when the dipole moment takes the value $$ p_\text{max} = p(t_\text{max}) = \frac{2 a^2 \pi^2}{r_L\sqrt{e}} \cdot
\frac{v \sigma_n \sigma_{\text{pulse}} \sigma_{\text{spike}} \bar{n} \bar{\lambda}_{\text{pulse}} \bar{V}_{\text{spike}}}
{\left(\sigma_n^2+v^2 \left(\sigma_{\text{pulse}}^2+\sigma_{\text{spike}}^2\right)\right)} $$

The dipole moment is maximal whenever the three
(spatial) widths $\sigma_n$, $v\sigma_{\text{pulse}}$
and $v\sigma_{\text{spike}}$ are of the form
$w_1^1=w_2^2+w_3^3$, where $w_1$ is the largest of the
three terms, while $w_2$ and $w_3$ are the other two
terms, regardless of order. The dipole moment is thus
maximal when the widths of the pulses agree. In
particular, if $\sigma_n$ is the widest, then the dipole
moment is maximal if $\sigma_n$ is equal to the width of
$\lambda(t)\ast V_\text{spike}(t,x)$, which is
$v\sqrt{\sigma_{\text{spike}}+\sigma_{\text{pulse}}}$.
