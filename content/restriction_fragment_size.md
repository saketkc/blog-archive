Title: Restriction Fragments Size Distribution
Date: 2015-05-13
Tags: poisson, computational biology, exponential

## Given

The number of restriction sites in a fragment of length $t$ are distributed as:
$$
P(N_t=k)=e^{-\lambda t}\frac{(\lambda t)^k}{k!}
$$

Find the distribution of length of restriction fragments


## Solution

Intuition: If I have a restriction site at some location $z$ and want it to be
atleast $x$ base pairs long, i.e. I have a fragment starting at $z$ and going atleast 
till $z+x$, I need to ensure I do not encounter any other restriction site in between,
which is also equivalent to $P(N_x=0) = e^{-\lambda x}$

Thus, the probability that the restriction site is atleast $x$ bp is given by:
$$
P(X > x) = e^{-\lambda x}
$$

and hence,

$$
P(X < x) = 1-e^{-\lambda x} \implies P(X=x) = \lambda e^{-\lambda x}
$$

Thus, the size of restriction fragments follows an exponential distribution.




