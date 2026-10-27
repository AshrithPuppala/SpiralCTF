The Ghost Run | Forensics / Signals | Medium–Hard | 350 pts

The fiber/coax link between the TX board and the capture rig is misbehaving, smearing the signal like the cable remembers things it shouldn't. The payload is buried in a severely distorted digital baseband signal, and you will need to map the physical link's impulse response to clean it up and see what is really there.   

You have been provided with a pre-recorded calibration sweep (reference_recv.wav) to estimate and invert the channel's effects, along with the actual transmission (message_recv.wav). The capture rig's two stereo ADC channels are not sample-locked, and the TX board prepends an untrusted canned preamble. Equalize the channel, phase-align the left and right channels using the 1 kHz calibration tone, bypass the preamble using the 500-4000 Hz chirp, and demodulate the resulting I/Q payload to extract the data.
