title: A frequent inequality
date: 2015-09-09
tags: stats, pdf, math


$$
\frac{x-1}{x} \leq \ln(x)  \leq x-1 \forall\ x>0
$$

Consider $f(x)=\ln(x)-\frac{x-1}{x}$

$f'(x) = \frac{1}{x} - \frac{1}{x^2} = \frac{x-1}{x^2}$

Now consider the following two cases:

Case A: $0 < x \leq 1$ and Case B: $1 < x < \infty$

Then for Case A: $x-1 \leq 0$ and hence $f'(x)\leq 0$ $\implies$ $f(x)$ is a non-increasing function in $(0,1]$ and hence $f(x)\geq f(1) \forall x \in (0,1]$

So for $x \in (0,1]$, $f(x) \geq f(1)$ $\implies$ $\ln(x)-\frac{x-1}{x} \geq 0$ $\implies$ $\frac{x-1}{x} \leq \ln(x)$


Now for Case B:

$1 < x < \infty$ $\implies$ $x-1>0$

Thus, in this region $f'(x)>0$ and hence $f(x)$ is a strictly increasing function in $(1,\infty)$ 


Thus, for $1 < x < \infty$, $f(x)>f(1)$ and hence  $\ln(x)-\frac{x-1}{x} > 0$ 

Combine results with that in case A for $f(x)$ to conclude: $\frac{x-1}{x} \leq \ln(x)$


Now define $f(x)= \ln(x)-x+1$ $\implies$ $f'(x) = \frac{1}{x}-1 =\frac{1-x}{x}$
Whole story of Case A and Case B again. But it should be simple to see that 
for $0 < x \leq 1$, $g'(x)\geq 0$ and hence $g(x) \leq g(1)$ $\implies$ $\ln(x)-x+1 \leq 0$ 
And for $1 < x < \infty$, $g'(x)<0$ and hence $g(x)<g(1)$ $\implies$ $\ln(x)-x+1 < 0$ 

## TODO

- KL-divergence 
- Entropy