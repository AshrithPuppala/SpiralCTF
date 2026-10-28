Category: AI/ML & Image Processing
Difficulty / Points: Hard / 500 pts
Challenge Description:
BouncerBot 9000 is guarding the VIP node at an underground club. We tapped into its optical feed and dumped bouncer_eye.png, along with an encrypted memory dump from its perceptual core, bouncer_brain.npz. Leaked hardware logs suggest BouncerBot filters visual noise in the frequency domain before verifying credentials, but its raw memory banks are heavily corrupted with impulse interference. Solvers who feed noisy data directly to its cortex are known to be mocked. Can you bypass the bouncer and reconstruct the VIP pass?
Method to Solve:
Load bouncer_eye.png, which is obscured by heavy periodic noise.
Apply a 2D Fast Fourier Transform (FFT) to the image and identify the high-frequency anomaly spikes in the magnitude spectrum.
Mask/Zero-out these specific frequency anomalies and apply the Inverse FFT (IFFT) to reconstruct a clean image, revealing a decryption key or matrix.
Use the extracted key to decrypt the neural weights inside bouncer_brain.npz.
Run the neural network forward pass with the cleaned image data to generate the final output array, which renders the VIP flag.
Files Given to Solver: bouncer_eye.png, bouncer_brain.npz
Flag: SPIRAL{fr3qu3ncy_d0m41n_b0unc3r}
