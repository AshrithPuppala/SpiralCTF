Difficulty / Points: Easy-Medium / 150 pts
Challenge Description:
We intercepted a massive dataset of 1,000 corrupted transmission frames (transmissions.npy). Each frame is an array of 16,384 floating-point numbers. At first glance, plotting any individual frame just looks like random TV static. However, our analysts suspect that a static hidden image is being broadcast at varying signal strengths across the dataset, buried underneath heavy Gaussian noise. You don't need a neural network for this. Sometimes, the direction of maximum variance is all you need to see the truth.
Method to Solve:
Load the dataset of 1,000 frames (shape 1000 x 16384).
Recognize the hint regarding "direction of maximum variance," which points directly to Principal Component Analysis (PCA).
Compute the first principal component (or simply average the frames to cancel out the zero-mean Gaussian noise).
Reshape the resulting 16,384-length vector into a 128x128 2D matrix.
Plot the matrix as an image using matplotlib to reveal the hidden flag.
Files Given to Solver: transmissions.npy
Flag: SPIRAL{pr1nc1p4l_c0mp0n3nt_4n4lys1s}

