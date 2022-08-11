# Helmholtz_decomposition
Numerical Helmholtz decomposition in Python.

Ultimately the goal is to numerically decompose into a sum of two fields which are dependent on the curl and gradient of the original vector field.  The field that is dependent on the curl can then be further decomposed into a left and right helical component.

Let's start with a vector field $\mathbf{F}$.  Using Helmholtz theorem, $\mathbf{F}$ can be written as a sum of two other vector fields:
 
$\mathbf{F} = \mathbf{A} + \mathbf{B} = -\nabla U + \nabla \times \mathbf{W}$

where U is a scalar function and $\mathbf{W}$ is a vector function.  U and $\mathbf{W}$ can be found using the Helmholtz decomposition:

$U(\mathbf{r}) = \frac{1}{4\pi} \int \frac{C(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|} d\tau' $

$\mathbf{W}(\mathbf{r}) = \frac{1}{4\pi} \int \frac{\mathbf{D(r')}}{|\mathbf{r}-\mathbf{r}'|} d\tau'$

where

$C = \nabla \cdot \mathbf{F}$
 
$\mathbf{D} = \nabla \times \mathbf{F}$.

Therefore, the first equation becomes:

$\mathbf{F} = \mathbf{A} + \mathbf{B} = -\nabla \bigg( \frac{1}{4\pi} \int \frac{\nabla \cdot \mathbf{F}}{|\mathbf{r}-\mathbf{r}'|} d\tau' \bigg) + \nabla \times \bigg( \frac{1}{4\pi} \int \frac{\nabla \times \mathbf{F}}{|\mathbf{r}-\mathbf{r}'|} d\tau' \bigg) $

and it can be seen that

$\mathbf{A} = -\nabla \bigg( \frac{1}{4\pi} \int \frac{\nabla \cdot \mathbf{F}}{|\mathbf{r}-\mathbf{r}'|} d\tau' \bigg)$

$\mathbf{B} = \nabla \times \bigg( \frac{1}{4\pi} \int \frac{\nabla \times \mathbf{F}}{|\mathbf{r}-\mathbf{r}'|} d\tau' \bigg)$

and that $\mathbf{A}$ and $\mathbf{B}$ are convolutions.

A convolution is defined as:

$g \ast h = \int g(\tau) h(\tau - t) d\tau $. 

Here, $g(\tau) \sim \nabla \cdot \mathbf{F}$ for $\mathbf{A}$ and $g(\tau) \sim \nabla \times \mathbf{F}$ for $\mathbf{B}$, while $h(\tau - t) \sim \frac{1}{|\mathbf{r}-\mathbf{r'}|}$.  $|\mathbf{r} - \mathbf{r'}| \sim \tau$ and $d|\mathbf{r}-\mathbf{r'}| \sim d\tau$ for the dependent variables and spacing.  We also use $|\mathbf{r}| = \sqrt{x^2 + y^2 + z^2}$ from our 3D array.


The vector field $\mathbf{B}$ (and by extension $\mathbf{W}$ and $\mathbf{D}$) can be further decomposed into

$\mathbf{B} = \mathbf{B_L} + \mathbf{B_R}$.
