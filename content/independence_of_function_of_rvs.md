title: Functions of independent random variables are independent
date: 2015-06-01
tags: independence, random variables

## A textbook problem

Given $X$, $Y$ are two independent random variables,
show that functions $g(X)$ and $h(Y)$ are independent too


## Short Proof

Never took a course on measure theory, so avoiding that route:

Let.

$R = g(X)$

$S = h(Y)$


Also define,

$A_r = \{x: g(X)\leq r\}$ and $B_s = \{y:h(Y) \leq s\}$


$$
F_{RS}(r,s) = P(R\leq r, S \leq s) = P(X \in A_r, Y \in B_s)
$$

Now, since $X$, $Y$ are independent:

$$
P(X \in A_r, Y \in B_s) = P(X \in A_r)P(Y \in B_s) = F_R(r)F_S(s)
$$

Which implies

$$
F_{RS}(r,s) = F_R(r)F_S(s)
$$

and hence

$g(X), h(Y)$ are independent.


