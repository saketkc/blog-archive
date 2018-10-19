Title: SVD v/s MDS v/s PCA
Date: 2015-04-15
tags: math, statistics, ml


Principle Component Analysis(PCA) is a relatively more famous
than Singular Value Decomposition(SVD) or Multidimensional Scaling(MDS).
When I was introduced to the latter two, I was utterly confused
trying to figure out what goes in where.


## SVD

Let $X_{mxn}$ data matrix. For an easy to relate example, from bioinformatics,
let each row represent a gene, and each column represent single patient.

The rows thus give expression profile of gene across patients while the columns
represent the expression levels of different genes in each person.

Without loss of generality we assume $m>n$ and $rank(X)=r <n$

The singular value decomposition of $X_{mxn}$ is then given by:

$$
X_{mxn} = U_{mxr}\sum_{rxr}V_{nxr}^T
$$


$U_{nxr}$ consists of orthornormal eigen vectors of $X^TX$(nxn)

$V_{mxr}$ consists of orthornormal eigen vectors of $XX^T$(mxm)

$\sum_{rxr}$ denotes a diagonal matrix composed of eigen vectors of $X^TX$ arranged with the largest being located
at top left, least at bottom right.$\sum_{ii} = \lambda_i$ and $\lambda_1 \geq \lambda_2 \geq \lambda_3 \geq \ldots \geq \lambda_r$


Facts:

- $\lambda_i \geq 0$ because $X^TX$ is a positive definite matrix: $yX^TXy = (Xy)(Xy)^T > 0$ always [See: http://en.wikipedia.org/wiki/Positive-definite_matrix#Characterizations]


## PCA
 
Let $X_c$ denote the mean centered $X$, i.e. $X_c = I’_{mxm}X_{mxn}$
 where $I’ = I-\frac{1}{m}$ thus from each row we substract the ‘average row’ leading to $X_c4 being zer-mean centerered.

 Def: Gram matrix : $X_cX_c^T$

 Def: Covariance Matrix: $X_c^TX_c$

 Let’s say you are given the original uncente



The most ‘common’ definition of PCA says : For a given set of $n$ dimensional vectors
$x_1, x_2, x_3,x_4, \ldots x_m$ the $p<n$ principal components are those orthogonal
axes onto which the variance retained is maximized

and hence 

Plotting/Running PCA
- Calculate $X_cX_c^T$ and calculate $U$ as the eigen vectors of this matrix. Retain the vectors corresponding
to top $p=2$ eigenvalues
-  Calculate project $Y=U^TX$

Given gram matrix of original data $K$, to obtain gram matrix of mean centered data, cholesky decomposition is not required:


$K_c = (I-\frac{1}{n})K(I-\frac{1}{n}) = K-\frac{I}{n}K -K\frac{1}{n} \frac{I}{n}K\frac{I}{n}$

Also realize:

$X_c = U \sum V^T$

and $UU^T=I$ ; $VV^T=I$

Thus, $K_c=X_cX_c^T = U\sum^2U^T$

PCA is equivalent of doing a SVD: of $X_c = U\sumV^T$ and then using $U\sum$ as the principle components


## MDS
Given distance matrix $D_{ij}$ of pairwise distances, what would PCA result into?
Assuming the distances were euclidean:

$$
D_{ij}^2 = ||x_i-x_j||^2 = ||x_i - \overline{x} + \overline{x} -x_j||^2 = ||x_i-\overline{x}||^2 + ||x_j - \overline{x}|^2 -2\langle x_i-\overline{x}, x_j-\overline{x}\rangle
= ||x_i-\overline{x}||^2 + ||x_j - \overline{x}|^2 + 2[K_c]_{ij}
$$
which can be cleverly rewritten as:
$$K_c = (I-\frac{1}{n})\frac{-D^2}{2}(I-\frac{1}{n}$$

$K_c$ can now undergo SVD to obtain principal components. which is what happens in [MDS](MDS.md) too.
## References

[1] http://stats.stackexchange.com/questions/14002/whats-the-difference-between-principal-components-analysis-and-multidimensional/132731#132731

[2] SVD: http://infolab.stanford.edu/~ullman/mmds/ch11.pdf

[3] SVD in R: http://en.wikibooks.org/wiki/Data_Mining_Algorithms_In_R/Dimensionality_Reduction/Singular_Value_Decomposition

[4] Multidimensional Scaling, Patrick J.F. Groenen∗ Michel van de Velden

[5] SVD and PCA: http://math.stackexchange.com/questions/3869/what-is-the-intuitive-relationship-between-svd-and-pca

[6] Intuitive Explaination of PCA: http://arxiv.org/pdf/1404.1100.pdf

[7] PCA: http://www3.cs.stonybrook.edu/~sael/teaching/cse549/Slides/CSE549_16.pdf

[8] PCA: http://www.math.ucsd.edu/~gptesler/283/slides/pca_f13-handout.pdf

[9] SVD: http://www.cs.wustl.edu/~zhang/teaching/cs517/Spring12/CourseProjects/SVD.pdf

[10] PCA v/s MDS: http://stats.stackexchange.com/questions/14002/whats-the-difference-between-principal-components-analysis-and-multidimensional

[11] Gaussian Lernels: https://shapeofdata.wordpress.com/2013/07/23/gaussian-kernels/

[12] Kernel PCA: http://sebastianraschka.com/Articles/2014_kernel_pca.html
