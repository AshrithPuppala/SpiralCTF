Category: Signals, Control Systems & AI/ML
Difficulty / Points: Medium-High / 350 pts
Challenge Description:
Hackers compromised our magnetic levitation system. We recorded the raw sensor bus and saved it as phantom_hack.npz. This file contains the recording (rf_bus), the system matrices (A, B, C), and the weights of an onboard neural network (W1, b1, W2, b2). The system pinged an acoustic impulse, followed by a 16,000 Hz data transmission of control commands and sensor readings mixed onto a 2000 Hz carrier wave. The system doesn't start at rest, and after 3 calibration steps, a secret error was injected for 128 steps. Deconvolve the signal, calculate the initial state, extract the true error, and pass the attack phase through the network to decode the 128-bit payload.
Method to Solve:
Use the first 64 samples (the ping) to determine the impulse response h[n] and deconvolve rf_bus.
Demodulate the 2000 Hz carrier (In-Phase for u[k], Quadrature for y[k]) and downsample by 16 to match the control steps.
Use the first 3 uncompromised steps (k=0,1,2 where e[k]=0) to algebraically solve for the unknown initial state x[0] using the observability matrix.
Iterate the state-space equations for steps 3 to 130 to isolate the injected error e[k].
Feed z[k]=[x1[k],x2[k],x3[k],e[k]] into the 2-layer Neural Network. Threshold the output at 0.5 to get binary 1s and 0s, and convert the resulting 128 bits to ASCII.
Files Given to Solver: phantom_hack.npz
Flag: SPIRAL{st4t3_sp4c3_0bs3rv3r}

