'''In a previous exercise, you saw that 2 was a reasonable choice for the "intrinsic dimension" of the fish measurements. 
Now use PCA for dimensionality reduction of the fish measurements, retaining only the 2 most important components.

The fish measurements have already been scaled for you, and are available as scaled_samples.'''

#TASK
# Import PCA from sklearn.decomposition.
# Create a PCA instance called pca with n_components=2.
# Use the .fit() method of pca to fit it to the scaled fish measurements scaled_samples.
# Use the .transform() method of pca to transform the scaled_samples. Assign the result to pca_features.

# Import PCA
____

# Create a PCA model with 2 components: pca
pca = ____

# Fit the PCA instance to the scaled samples
____

# Transform the scaled samples: pca_features
pca_features = ____

# Print the shape of pca_features
print(pca_features.shape)




#SOLUTION

# Import PCA
from sklearn.decomposition import PCA

# Create a PCA model with 2 components: pca
pca = PCA(n_components=2)

# Fit the PCA instance to the scaled samples
pca.fit(scaled_samples)

# Transform the scaled samples: pca_features
pca_features = pca.transform(scaled_samples)

# Print the shape of pca_features
print(pca_features.shape)
