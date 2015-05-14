title: Restriction Fragments, MLE,  and Mixed Random Variables
date: 2015-05-13
tags: indicator variable, computational biology, exponential, mle, likelihood


Let $X_1, X_2, \dots , X_n$ be the lengths of $n$ restriction fragments. Suppose that a
biotechnique can measure fragment lengths accurately up to a given length c.
That is, if $X_i < c$, then the technique gives correct value $X_i$
Show that MLE of $\lambda = \frac{n-T_n}{S_n+cT_n}$ where $S_n= \sum_{j=1}^n X_jI(X_j < c)$ and $T_n = \sum_{j=1}^n I(X_j \geq c)$




## Solution

This is another of my favorite problems that requires clever use of exponential variables.
I also answered a similar  question on [Mathematics stackexchange](http://math.stackexchange.com/a/1281204/171836)

Few observations:

$P(X_i < x)  = 1 - \lambda e^{-x}$ if $ 0 \leq x < c$

$P(X_i = c) = P(X_i \geq c) = e^{-\lambda c}$ (This one looks counter intuitive at first look, but that is what the $X_i=c$ if $X_i \geq c$ returns)

Now,

$\begin{align}L( \lambda| x_i) &= \prod_{i=1}^{n}  (\lambda e^{-\lambda x_i}) I(0 \leq x_i < c) \times (e^{-\lambda c})I( x_i \geq c) \\&= \lambda^{\sum_{i=1}^n I(0 \leq x_i < c)}e^{-\lambda(\sum_{i=1}^n x_iI(0 \leq x_i < c)} \times e^{-\lambda c \sum_{i=1}^n I(x_i \geq c)} \\&= \lambda^{n-T_n}e^{-\lambda S_n} \times e^{-\lambda c T_n}\end{align}$ 

$\log L= (n-T_n) \log \lambda -\lambda(S_n+cT_n)$

$\frac{\partial \log L}{\partial \lambda} = \frac{n-T_n}{\lambda}-(S_n+cT_n)$

which gives $\hat \lambda = \frac{n-T_n}{S_n+cT_n}$
