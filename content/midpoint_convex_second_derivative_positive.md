title: Positive definite second derivative
date: 2015-02-28
tags: linear algebra, matrix, norm


> Let $f:\mathbb{R}\to\mathbb{R}$ be a twice-differentiable function,
> and let $f$’s second derivative be continuous. Let $f$ be convex with
> the following definition of convexity: for any $a<b \in \mathbb{R}$:
> $$f\left(\frac{a+b}{2}\right) \leq \frac{f(a)+f(b)}{2}$$ Prove that
> $f’’ \geq 0$ everywhere.


## Solution
http://math.stackexchange.com/a/1224986/171836

Given $f$ is a continuous and using the results from [this answer](http://math.stackexchange.com/a/83398/171836), $f$ can be proven to satisfy:
$f(\lambda x_1 + (1-\lambda)x_2) \leq \lambda f(x_1) +  (1-\lambda)f(x_2)\ \forall \  \lambda \in [0,1]$ 


Now, by using Taylor’s expansion, $f’’(x)$ can be written as: 
$$
f’’(x) = \lim_{h \rightarrow 0} \frac{f(x+h)+f(x-h)-2f(x)}{h^2}
$$

$f(\frac{1}{2}(x+h) + \frac{1}{2}(x-h)) \leq \frac{1}{2}f(x+h) + \frac{1}{2}f(x-h) \implies 2f(x) \leq f(x+h)+f(x-h)$ 
or $f(x+h)+f(x-h)-2f(x) \geq 0$. 

Since $h^2 \geq 0$ and $f$ being twice differentiable,  $f’’(x) \geq 0$ follows.



