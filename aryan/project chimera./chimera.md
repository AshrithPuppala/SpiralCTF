Category: Signal Processing & Forensics
Difficulty / Points: Hard / 500 pts
Challenge Description:
An automated listening station on the border was locked down. The terminal dumped an acoustic telemetry stream recorded in a multipath reverberation environment (capture.npz). Engineers left a note stating that a standard calibration chirp was transmitted prior to the payload, a decoy Morse code transmission runs at a low frequency, and the true intelligence payload is an analog-modulated, heavily warped raster image following a 1 kHz to 6 kHz calibration chirp. Can you deconvolve the transmission channel, bypass the decoy, and decode the correct raster image?
Method to Solve:
Load capture.npz.
Cross-correlate the audio with a generated 1 kHz–6 kHz chirp to locate the multipath echo delays.
Apply a frequency-domain Wiener filter to deconvolve the signal and remove the canyon echo distortion.
Ignore the easily visible 2 kHz Morse code signal (which decodes to a fake decoy flag).
Apply AM-demodulation to the 15 kHz high-frequency carrier and filter it to extract the baseband raster signal.
Split the signal using the negative sync pulses, reshape into a 2D matrix, and plot it. Manually read the warped, grid-struck CAPTCHA text that defeats OCR AI.
Files Given to Solver: capture.npz
Flag: SPIRAL{N0_A1_C4N_R34D_TH1S} (Decoy Flag: SPIRAL{3CH0_B41T_LMAO})
