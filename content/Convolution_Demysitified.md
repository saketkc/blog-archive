title: Convolution Demysitifed
date: 2015-05-09
tags: stats, pdf, math

## Problem

Given $f(x) = \frac{x}{2}$ for $0 \leq x \leq 2$. Find the pdf of $x_1+x_2$
for $x_1,x_2$ which are i.i.d.

## Wrong solution


$$ 
f*g(t) = \int_{-\infty}^{\infty} f(w)g(t-w)dw
$$

Thus, blindly,

$f_S(s) = \int_{0}^s \frac{x(s-x)}{4}dx = \frac{s^3}{24}$ and $0 \leq s \leq 4$

But is $f_S(s)$ a PDF? 

No.

$\int_0^4 f_S(s)ds = \frac{4^4}{96} \neq 1$

## Respecting the bounds.

$f_S(s) = \int_{0}^s \frac{x}{2}{s-x}{2}dx $ for :

$$
0 \leq x \leq 2
$$
and

$$
0 \leq s-x \leq 2
$$

Which gives us, these bounds:

$s-2 \leq x \leq s$ and $0 \leq x \leq 2$

In order to respect the above bounds,

$f*g(s) = \int_{-\infty}^{\infty}f(x)f(s-x)dx$

But, $f(x) \neq 0$ for $0 \leq x \leq 2$

and $f(x-w)\neq 0 $ for $s-2 \leq x \leq s$

thus, $f(x)f(x-w) \neq 0 $ for $max(0,s-2) \leq x \leq min(s,2)$

And thus,i


Range of s: $[0,4]$


$f*g(s) = \int_{max(0,s-2)}^{min(s,2)}f(x)f(s-x)dx$

For $0 \leq s \leq 2$ :  $min(s,2)=s$ and $max(0,s-2)=0$

For $2 \leq s \leq 4$ : $min(s,2)=2$ and $max(0,s-2)=s-2$


Now,

$$
f_S(s) = \begin{cases}
\int_{0}^{s}\frac{x}{2}\frac{s-x}{2}dx = \frac{s^3}{24}  & 0 \leq s \leq 2\\
\int_{s-2}^{2}\frac{x}{2}\frac{s-x}{2}dx = \frac{1}{4}(\frac{s(2^2-(s-2)^2)}{2}-\frac{2^3-(s-2)^3}{3})  & 0 \leq s \leq 2\\
\end{cases}
$$
