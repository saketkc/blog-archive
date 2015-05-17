title: Prove: No UMVUE exists for $\frac{1}{\theta}$ for Poisson Distribution.
date: 2015-05-16
tags: umvue, poisson, estimator

## Problem

Prove: No UMVUE exists for $\frac{1}{\theta}$ for Poisson Distribution.


## Solution

http://stats.stackexchange.com/a/152660/11668

bservation 1: $\sum X_i$ is complete and sufficient statistic for $\theta$

Observation 2: $\sum X_i \sim Poisson(n\theta)$ 

We need to look for an unbiased estimator of $\frac{1}{\theta}$ in order to utilise [Rao-Blackwell theorem](http://en.wikipedia.org/wiki/Rao%E2%80%93Blackwell_theorem)

Let $\delta(x)$ be such an estimator:

$E[\delta(x)] = \frac{1}{\theta}$ 

Then, $\sum_{k=0}^{\infty}\frac{\delta(k)e^{-\theta}\theta^k}{k!} = \frac{1}{\theta}$ $\implies$ $\sum_{k=0}^{\infty}\frac{\delta(k)\theta^k}{k!} = \frac{e^\theta}{\theta}$

By Taylor expansion:
$e^\theta = \sum_{k=0}^{\infty}\frac{\theta^k}{k!}$ $\implies$ $\frac{e^\theta}{\theta} = \sum_{k=0}^{\infty}\frac{\theta^{k-1}}{k!}$

Thus,
$\sum_{k=0}^{\infty}\frac{\delta(k)\theta^k}{k!}  =\sum_{k=0}^{\infty}\frac{\theta^{k-1}}{k!} $ $\implies$ $\delta(k) = \frac{1}{\theta} $ which is a useless estimator


Since, there is no unbiased estimator, there exists no UMVUE as well.
