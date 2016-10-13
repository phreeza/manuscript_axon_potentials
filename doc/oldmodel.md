

We define the spatial dimension in cylindrical coordinates $\mathbf{r}=(\rho,\varphi,z)$ such that $z$ is the
dorsoventral direction, increasing from dorsal to ventral, and $z=0$ is the dorsal
border of NL. We further define $\hat{\mathbf{e}}_{z}$ as the unit vector in $z$ direction, and
$\hat{\mathbf{e}}_{\rho}$ as an arbitrary unit vector perpendicular to the $z$
direction.

Let us first consider a simple model axon that extends
infinitely on both sides and in a straight line from the dorsal direction into
NL, and at 0 in the remaining coordinates. Furthermore, we consider a single
action potential propagating along this axon. This axon then has a non-zero
current density only at $\rho=0$, which we denote $i_{\infty}(z,t)$, meaning
that in this case $i(\mathbf{r},t)=\delta(\rho)i_{\infty}(z,t)$. Applying this to equation \ref{eqn:basic},
corresponding response $\kappa_{\infty}(\mathbf{r},t)$ of an action potential propagating
through such a line-axon is then 

\begin{align}
\kappa_{\infty}(\mathbf{r},t) & =\frac{1}{4\pi\sigma_{e}}\int_{V}\frac{\delta(\rho')i_{\infty}(z',t)}{|\mathbf{r}-\mathbf{r}'|}\textrm{d}\mathbf{r}'\label{eq:halfline}\\
& =\frac{1}{4\pi\sigma_{e}}\int_{-\infty}^{\infty}\frac{i_{\infty}(z',t)}{|\mathbf{r}-z'\hat{\mathbf{e}}_{z}|}\textrm{d}z'
\end{align}
We will call this response a spike kernel because it will take the
role of an integral kernel in the following.

Due to the rotational symmetry, the kernel at a distance $\rho$ from the axon,
regardless of $\varphi$, can then be described by
\begin{align} \label{eqn:infkern}
\kappa_{\infty}(\mathbf{r},t) & =\frac{1}{4\pi\sigma_{e}}\int_{-\infty}^{\infty}\frac{i_{\infty}(z',t)}{|(z-z')\hat{\mathbf{e}}_{z} + \rho\hat{\mathbf{e}}_{\rho}|}\textrm{d}z' \\
& =\frac{1}{4\pi\sigma_{e}}\int_{-\infty}^{\infty}\frac{i_{\infty}(z',t)}{\sqrt{(z-z')^2 + \rho^2}}\textrm{d}z' 
\end{align}

Equation \ref{eqn:infkern} has the form of a convolution with a weighting
function $w$:
\begin{equation}
  w(\rho,z) = \frac{1}{4\pi\sigma_e}\frac{1}{\sqrt{z^2+\rho^2}}
  \label{eqn:weighting}
\end{equation}

The convolution can then be written as:

\begin{equation}
\kappa_{\infty}(\mathbf{r},t) = \left[i_{\infty}(z,t)\ast w(\rho,z)\right]_z
\end{equation}

with the operator $\left[\cdot\ast\cdot\right]_z$ denoting the convolution with
respect to the variable $z$.

The simplest model of a terminating axon will be a semi-infinite
axon, where the membrane current flow is simply set to zero beyond the
termination point $z_\text{term}$. Using the Heaviside step function $H$ we
find kernel $\kappa_{\text{term}}$ of a spike in a terminating axon:

\begin{equation}
  \kappa_{\text{term}}(\mathbf{r},t) = \left[\left\{H(z_\text{term}-z)\cdot i_{\infty}(z,t)\right\}\ast w(\rho,z)\right]_z
\end{equation}
Similarly, the model of a bifurcating axon would be one in which the current
flow after the bifurcation point $z_\text{bif}$ is double that of the single
infinite fiber.
\begin{equation}
  \kappa_{\text{bif}}(\mathbf{r},t) = \left[\left\{\left(1+H(z-z_\text{bif})\right)\cdot i_{\infty}(z,t)\right\}\ast w(\rho,z)\right]_z
\end{equation}
This places the child branches in superposition at $\rho=0$, which is a useful
approximation for small branching angles.

Approximating terminations and bifurcations in this way disregards the boundary
effects that may appear due to the conservation of charge and the inability of
 charge to flow beyond the termination. However, since the integral over
$i_\infty$ is zero for realistic action potentials, the conservation of charge
is maintained in the long run.

In more general terms, a coherently stimulated axon bundle with terminations
and bifurcations along it's path can be described by the number of individual
fibers $n(z)$ at any depth. The extracellular potential $\kappa_\text{b}$ of
such a bundle in which the action potential is initiated at the same time and
location is then given by
\begin{equation}
  \kappa_{\text{b}}(\mathbf{r},t) = \left[\left\{n(z)\cdot i_{\infty}(z,t)\right\}\ast w(\rho,z)\right]_z
  \label{eqn:bundlekern}
\end{equation}

If we want to calculate the combined field of many axons and action
potentials, we can do so by linearly summing the individual axon fields.

If all axons in the bundle are driven with the same the mean firing rate
$\lambda(t)$, which might be modulated in time, the field potential
$\Phi(\mathbf{r},t)$ in response to this firing rate will be the (temporal)
convolution of the firing rate with the response of the bundle to a coherent
spike in all axons:

\begin{equation}
  \Phi(\mathbf{r},t) = \left[\kappa_\text{b}(\mathbf{r},t) \ast \lambda(t)\right]_t
  \label{eqn:fullpot}
\end{equation}
Substituting equation \ref{eqn:bundlekern} into equation \ref{eqn:fullpot}, and taking advantage of the fact that only $i_\infty$ and $\lambda$ depend on $t$ gives

\begin{align}
  \label{eqn:switchedpot}
  \Phi(\mathbf{r},t) & =  \left[\left[\left\{n(z)\cdot i_{\infty}(z,t)\right\}\ast w(\rho,z)\right]_z \ast \lambda(t)\right]_t \\
  & =  \left[\left\{n(z)\cdot \left[i_{\infty}(z,t)\ast \lambda(t)\right]_t\right\}\ast w(\rho,z)\right]_z
\end{align}
With the average current in a single infinite fiber stimulated with $\lambda$, which we will denote it with $i_\lambda(z,t) := \left[i_{\infty}(z,t)\ast \lambda(t)\right]_t$ this gives us

\begin{align}
  \Phi(\mathbf{r},t) & =  \left[\left\{n(z)\cdot i_\lambda(z,t)\right\}\ast w(a,z)\right]_z
  \label{eqn:switchedpotend}
\end{align}

