# Helmholtz_decomposition
Numerical Helmholtz decomposition in Python.

Ultimately the goal is to numerically decompose into a sum of two fields which are dependent on the curl and gradient of the original vector field.  The field that is dependent on the curl can then be further decomposed into a left and right helical component.

Let's start with a vector field $\Vec{\mathbf{F}}$.  Using Helmholtz theorem, $\Vec{\mathbf{F}}$ can be written as a sum of two other vector fields:
 
$\Vec{\mathbf{F}} = \Vec{\mathbf{A}} + \Vec{\mathbf{B}} = -\nabla U + \nabla \times \Vec{\mathbf{W}}$

where U is a scalar function and $\Vec{\mathbf{W}}$ is a vector function.  U and $\Vec{\mathbf{W}}$ can be found using the Helmholtz decomposition:

$U(\mathbf{r}) = \frac{1}{4\pi} \int \frac{C(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|} d\tau' $

$\Vec{\mathbf{W}}(\mathbf{r}) = \frac{1}{4\pi} \int \frac{\mathbf{D(r')}}{|\mathbf{r}-\mathbf{r}'|} d\tau'$

where

$C = \nabla \cdot \Vec{\mathbf{F}}$
 
$\Vec{\mathbf{D}} = \nabla \times \Vec{\mathbf{F}}$.

Therefore, the first equation becomes:

$\Vec{\mathbf{F}} = \Vec{\mathbf{A}} + \Vec{\mathbf{B}} = -\nabla \bigg( \frac{1}{4\pi} \int \frac{\nabla \cdot \Vec{\mathbf{F}}}{|\mathbf{r}-\mathbf{r}'|} d\tau' \bigg) + \nabla \times \bigg( \frac{1}{4\pi} \int \frac{\nabla \times \Vec{\mathbf{F}}}{|\mathbf{r}-\mathbf{r}'|} d\tau' \bigg) $

and it can be seen that

$\Vec{\mathbf{A}} = -\nabla \bigg( \frac{1}{4\pi} \int \frac{\nabla \cdot \Vec{\mathbf{F}}}{|\mathbf{r}-\mathbf{r}'|} d\tau' \bigg)$

$\Vec{\mathbf{B}} = \nabla \times \bigg( \frac{1}{4\pi} \int \frac{\nabla \times \Vec{\mathbf{F}}}{|\mathbf{r}-\mathbf{r}'|} d\tau' \bigg)$

and that $\Vec{\mathbf{A}}$ and $\Vec{\mathbf{B}}$ are convolutions.

A convolution is defined as:

$g \ast h = \int g(\tau) h(\tau - t) d\tau $. 

Here, $g(\tau) \sim \nabla \cdot \Vec{\mathbf{F}}$ for $\Vec{\mathbf{A}}$ and $g(\tau) \sim \nabla \times \Vec{\mathbf{F}}$ for $\Vec{\mathbf{B}}$, while $h(\tau - t) \sim \frac{1}{|\Vec{r}-\Vec{r'}|}$.  $|\Vec{r} - \Vec{r'}| \sim \tau$ and $d|\Vec{r}-\Vec{r'}| \sim d\tau$ for the dependent variables and spacing.  We also use $|\Vec{r}| = \sqrt{x^2 + y^2 + z^2}$ from our 3D array.


The vector field $\Vec{\mathbf{B}}$ (and by extension $\Vec{\mathbf{W}}$ and $\Vec{\mathbf{D}}$) can be further decomposed into

$\Vec{\mathbf{B}} = \Vec{\mathbf{B_L}} + \Vec{\mathbf{B_R}}$.
