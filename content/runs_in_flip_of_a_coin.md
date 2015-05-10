Title: Runs in flips of a coin
Date: 2015-04-21
tags: probability, expectation


This problem happened to be in one of the screening examinations
and is my favorite because it demonstrates an application of indicator variables

## Problem
A run is defined as *maximal* subsequence of consecutive tosses all having the same outcome.
So HHHTHHTTH has 5 runs.(HHH,T,HH,TT,H). Let $R_n$ represent the number of runs 
when a coin is flipped $n$ times. Find:

1. $ER_n$
2. $Var(R_n)$
3. Distribution of $R_n-1$

Assume $p,q$ probability of showing H,T respectively.

## Solution

Let $I_i$ be an indicator variable such that $I_i=1$ iff $i^{th}$ and $(i+1)^{th}$ tosses are different(One of {$HT,TH$} ) 
f runs in $n$ flips is given by: $R_n = \sum_{i=1}^{n-1}I_i$

Well, not really. The point to realise is that the first toss is always a run!
Corrected $R_n = \sum_{i=1}^{n-1}I_i + 1$

Now $E[R_n] = 1+\sum_{i=1}^{n-1}P[I_i=1]$

We already know $P[I-i=1] = pq + qp$(Remeber the two possiblites of HT,TH)

and hence
1. $ER_n = 1+ (n-1)2pq$

Check Check!

$ER_1 = 1$ (Straightforward correct)
$ER_2 = 1+2pq$ 
$P(R_2=2) = pq + qp$ and $P(R_2=1) = p^2 + q^2$

Thus $ER_2 = 2(pq+qp) + 1(p^2+q^2) = 1 +2pq$ (Using $p+q=1$)

2. $Var(R_n) = ER_n^2 - (ER_n)^2$

$ER_n^2 = E(1+\sum I_i)^2 = E\sum_{i=1}^{n-1}I_i^2 +1+2\sum_{i=1}^{n-1}I_i = \sum_{i=1}^{n-1}EI_i^2 + 2\sum_{i < j} EI_iI_j + 2E\sum_{i=1}EI_1 = 3\sum E_i + 2\sum_{i < j}EI_iI_j +1$

Now realise that $EI_iI_j=P(I_iI_j)$ is an independent event for $|i-j|>1$ and is equal to $P(I_1)^2$

For $|i-j|=1$ we have $P(I_iI_j)=pqp+qpq = p^2q+qp^2$ and I chose in my summation for $j$ to be less than $i$ so the mod sign is redundant


Alright, skipping too many things here. but:
$Var(R_n) = 4pqn -6pq+2pq(n-2)(n-3) - 4p^2q^2(n-1)^2$

Check for $Var(R_2) = 2pq(1-2pq)$ and $Var(R_1)=0$

3. That should be a straightforward $R_n-1 \approx Binomial(n,2pq)$
