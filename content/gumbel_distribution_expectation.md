Title: Gumbel distribution expectation
Date: 2015-03-03
tags: stats, distribution, gumbel


## What

 If $X_1,..,X_n$ is a random sample with density $f(x;\theta)=e^{-(x-\theta)}e^{-e^{-(x-\theta)}}$ ($x \in\mathbb{R}$) and $-\infty<\theta<\infty$,
$\quad$i) Find the estimator of $\theta$
## Solution

First let’s confirm if  $f(x;\theta)=e^{-(x-\theta)}e^{-e^{-(x-\theta)}}$ represents a PDF.

Transforming $t=e^{-({x-\theta})}$:

$$\int_{-\infty}^{\infty} e^{-(x-\theta)}e^{-e^{-(x-\theta)}}dx  = \int_{0}^{\infty} e^{-t} dt = 1$$

This is indeed a [known distribution](http://en.wikipedia.org/wiki/Gumbel_distribution)

Now, using similar transformation($t=e^{-(x-\theta)}$) for $$E[X]=\int_{-\infty}^\infty xe^{-(x-\theta)}e^{-e^{-(x-\theta)}}dx$$

we get


$$E[X]=\int_{0}^\infty (\theta-ln (t))e^{-t}dt$$


$$E[X]=\theta - \int_{0}^\infty  ln (t)\ e^{-t}dt$$


Thus, 
$$ E[X] = \theta + \gamma$$

where the second term is [Euler Mascheroni constant](http://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant) $\gamma$ 
