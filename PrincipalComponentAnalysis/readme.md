### PCA explaination

The main idea of principal component analysis (PCA) is to reduce the dimensionality of a data set consisting of many variables correlated with each other,
either heavily or lightly, while retaining the variation present in the dataset, up to the maximum extent. The same is done by transforming 
the variables to a new set of variables, which are known as the principal components (or simply, the PCs) and are orthogonal, ordered such 
that the retention of variation present in the original variables decreases as we move down in the order. So, in this way, 
the 1st principal component retains maximum variation that was present in the original components. The principal components are the
eigenvectors of a covariance matrix, and hence they are orthogonal.

Importantly, the dataset on which PCA technique is to be used must be scaled. The results are also sensitive to 
the relative scaling. As a layman, it is a method of summarizing data. Imagine some wine bottles on a dining table.
Each wine is described by its attributes like colour, strength, age, etc. But redundancy will arise because many of 
them will measure related properties. So what PCA will do in this case is summarize each wine in the stock with less characteristics.           

Intuitively, Principal Component Analysis can supply the user with a lower-dimensional picture, a projection or "shadow"
of this object when viewed from its most informative viewpoint.
