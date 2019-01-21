Title: Entropy and Uniform Distribution
Tags: textbook problem, entropy, uniform
Date: 2015-10-18

To show $\sum p_i\log(p_i) = p$

Consider $H = -\sum p_i log(p_i) = log(n)$

Consider weighted AM-GM for $p_i$:

$$
(\prod \frac{1}{p_i}^p_i)^\frac{1}{\sum p_i} \leq \sum \frac{1}{p_i} \times p_i = n
$$

Take log both sides:

$$
\sum p_i \log(\frac{1}{p_i}) \leq \log(n)
$$

And hence euqality holds only if $p_i=p_j=1/n$ 
$$
p_i = 1/n
$$
