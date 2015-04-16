Title: SVD v/s MDS v/s PCA
Date: 2015-04-15
Category: math, statistics, ml


Principle Component Analysis(PCA) is a relatively more famous
than Singular Value Decomposition(SVD) or Multidimensional Scaling(MDS).
When I was introduced to the latter two, I was utterly confused
trying to figure out what goes in where.


## SVD

Let $X__{mxn}$ data matrix. For an easy to relate example, from bioinformatics,
let each row represent a gene, and each column represent single patient.

The rows thus give expression profile of gene across patients while the columns
represent the expression levels of different genes in each person.

Without loss of generality we assume $m>n$ and $rank(X)=r <n$

The singular value decomposition of $X_{mxn}$ is then given by:

$$
X_{mxn} = U__{mxr}\sum_{rxr}V_{nxr}^T
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

