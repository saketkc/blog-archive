Title: Expected number of pairings | Jones and Smith Family
Date: 2015-05-17
Tags: expectation, probability, indicator variables

## Problem

4 members of Smith family and 4 of Jones family are pooled
to form all possible pairs, all equally likely. Find $N$, the 
number of smiths which have a smith partner.


## Solution

$X= \sum_{i=1}^4 I_i$

Where $I_i=1$ iff $i^{th}$ meber of smith family has some smith member as it’s partner

Number of ways $i^{th}$ smith member can have a smith partner (Choose 1 from remaining 3 Smiths, form group of the remaining 6 )  $ = \binom{3}{1} \times \frac{6!}{(2!)^3} $

Hence, $P(I_i=1)= \frac{\binom{3}{1}\frac{6!}{(2!)^3}}{\frac{8!}{(2!)^4}} = \frac{3}{14}$ 

The trickery happens because at the next step I am going to over count,
since the wording in the question is a bit ambiguous and we are concerned with
the number of smiths have a partner. I should have multiplied $P(I_i=1)$ by $4$ and then divided by 2, 
but I am going to overcount with ambiguity.

$N = 4 \times \frac{3}{14} = \frac{6}[7]$ which ofcourse is not an integer, but did we expect it to?

