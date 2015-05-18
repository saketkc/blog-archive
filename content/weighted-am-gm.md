title: [Proof]Weighted AM-GM
date: 2015-05-18
tags: inequalities


We make use of [Jensen’s Inequality](http://en.wikipedia.org/wiki/Jensen%27s_inequality)
and the fact that $log(x)$ is a concave function:

For concave f:
$f(\frac{\sum a_ix_i}{\sum a_i}) \geq \frac{\sum a_i f(x_i)}{\sum a_i}$

$f=log(X)$

$log(\frac{\sum a_ix_i}{\sum a_i}) \geq \frac{\sum a_i log(x_i)}{\sum a_i}$
$\implies$ 
$log(\frac{\sum a_ix_i}{\sum a_i}) \geq log(\prod (x_i)^{\frac{1}{a_i}})$


Thus,
 $\frac{\sum_i a_i x_i}{\sum_i a_i}  \geq (\Pi x_i^{a_i})^{\frac{1}{\sum_i a_i}}$
