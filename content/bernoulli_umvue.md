Title: Bernoulli random varlable and UMVUE
Tags: bernoulli, umvue
Date: 2015-05-21

## Problem

Let $X_1,...,X_n$ random sample $X$~$Bernoulli(p)$.
For $n\geq 4$ show that the product $X_1X_2X_3X_4$ is a unbiased estimator for $p^4$, 
and use this fact for find the best unbiased estimator of $p^4$


## Solution

As posted on [stackexchange](http://stats.stackexchange.com/a/153315/11668)

[ToDo: Add variance, prove $E[\phi(T)]=0$]

T is a complete sufficient statistic for $p$. 

Now, consider indicator $I_{X_1=1,X_2=1,X_3=1,X_4=1}$ which is an unbiased estimator of $p^4$

Rao-Blackwellising:

$\begin{align}\phi(T) &= E[I_{X_1=1,X_2=1,X_3=1,X_4=1}|T]  \\&=P(X_1=1,X_2=1,X_3=1,X_4=1|T=t) \\&=\frac{P(X_1=1,X_2=1,X_3=1,X_4=1,X_1+X_2+X_3+X_4+\dots X_n=t)}{P(X_1+X_2+\dots +X_n=t)}  \\&= \frac{P(X_1=1,X_2=1,X_3=1,X_4=1)\times P(X_5+X_6+\dots X_n=t-4)}{P(X_1+X_2+\dots +X_n=t)} 
\\&= \frac{p^4\times \binom{n-4}{t-4}p^{t-4}(1-p)^{n-t}}{\binom{n}{t}p^{t}(1-p)^{n-t}}
\\&= \frac{\binom{n-4}{t-4}}{\binom{n}{t}} 
\\&=\frac{t(t-1)(t-2)(t-3)}{n(n-1)(n-2)(n-3)} \end{align}$


Check:

$E[\phi(T)] = 0 $ using moments from [here](http://mathworld.wolfram.com/BinomialDistribution.html)



