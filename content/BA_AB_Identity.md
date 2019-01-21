Title: BA = AB = I
Date: 2015-02-28
Tags: linear algebra, matrix, norm


# To Prove: If $$A_{nxn}$$ and $$B_{nxn}$$ such that AB=I, then BA=I

$$AB=I \implies Rank(A), Rank(B)=n$$

Reason: Rank(AB) $$\leq$$ min(Rank A, Rank B)

so B is a full rank matrix.
Now consider B=BI $$\implies$$ B-B(AB)=0 $$\implies$$ B-(BA)B=0 $$\implies$$ (I-BA)B=0

Since B is full rank so I-BA=0. Q.E.D

