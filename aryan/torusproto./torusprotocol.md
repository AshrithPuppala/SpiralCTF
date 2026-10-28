Category: Computer Vision & Image Processing
Difficulty / Points: Medium / 250 pts
Challenge Description:
We intercepted an encrypted transmission file named vortex.png from an adversary's node. Automated scans indicate that the data was scrambled using a basic byte mask hidden somewhere inside the file's raw structure, followed by a continuous dynamical 2D coordinate mapping over a torus. Recover the clean image and extract the flag.
Method to Solve:
Inspect the raw bytes or metadata of vortex.png (using a hex editor or Python script) to find the hidden XOR byte mask.
Apply the XOR mask to the image's pixel data.
The image will still look scrambled because the pixels were spatially shifted wrapping around the edges (a toroidal shift/Arnold's Cat Map).
Write a script to apply the inverse dynamical 2D modulo mapping to unroll the coordinates.
Reconstruct and view the unrolled image to read the flag.
Files Given to Solver: vortex.png
Flag: SPIRAL{t0r01d4l_v0rt3x_unw0und}
