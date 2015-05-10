Title: Multidimensional Scaling
Date: 2015-04-14

MDS is a statistical technique to visualize dissimilarity
between points. The distances between two pointsin n-dimensions 
are visualized in 2 dimensions such that it represents
the distance in n-dimensions as far as possible.

It is important to note that, for MDS, we start of with a ‘distance’ matrix
and not the coordinate of points. Dissimilarity is ‘similar’ to distances in most cases(ignoring the scale).
Let $\delta_{i,j}$ represent the distance between $i\ and\ j$

Given $n$ points, the idea is to come up with a set of $n * p$ matrix $X$
such that the distance between two vectors $x_i$ and $x_j$ is given by:


$$
d_{i,j}^2(X) = \sum_{k=1}^{p}(x_{ik}-x_{jk})^2
$$

So if we choose $p=1$, we wish to visualize everything in single dimension.
Let’s restrict to the case $p=2$

## How do you obtain X?

The idea again goes back to the definition of keeping the ‘new’ distance $d_{i,j}(X)$
as the original dissimilarity $\delta_{i,j}$ , this leads to the least square fit kind of regression
where the goal is to minimize the ‘residual’ error. Note, $d_{i,j}$ is an approximation to $\delta_{i,j}$
 The distance matrix could have come from $n$ points having high-dimensions(say $p’>p$), and even though
 these points cannot be visualized (since we cannot draw $p’$ dimensional map) we draw a $p=2$ dimensional map.
The coordinates of original $n$ points in $p’$ need not be known. We can still obtain an ‘equaivalent’
set of $n$ points in $p=2$ dimensions such that the $2D$ distance between two points $i,j$ is 
as close as it can be to the original distance.

$\sigma^2 = \sum_{i=1}^{n}\sum_{j=1}^{i-1}(\delta_{ij}-d_{ij}(X))^2$

This is just one way to define ‘closeness’ of $\delta_{ij}$ with $\d_{ij}$.
$X$ is obtained by minimizing such functions. Imagine doing ordinary least square fit(multidimensional).

## Checking if MDS makes sense

A quick checkt to see if MDS is good enough
is to go back to its definition. The final set of vectors $X_{n*p}$
should be able to communiate the original distance matrix
and hence a plot of the $\frac{n{n+1}}{2}$ points if $d_{ij}$ is
plotted against $X$ acis and $\delta_{ij}$ is plotted along $Y$ axis
then you should get a straight line representing $Y=X$.



