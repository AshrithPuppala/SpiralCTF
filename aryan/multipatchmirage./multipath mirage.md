Category: Signals & Systems
Difficulty / Points: Medium-Hard / 350 pts
Challenge Description:
During an underwater acoustic test inside a reverberant steel tank, a hydrophone recorded a short transmission (multipath_mirage.csv) sampled at Fs=16000Hz. We suspect an external open-water jammer injected a high-power spoofing signal alongside our authentic telemetry burst. Unlike the jammer, our authentic transducer was mounted deep inside a multi-wall cavity—meaning its signal suffered severe discrete multipath reflections. To assist with channel equalization, the authentic transducer fires a short rectangular channel-sounding pulse at t=12.5ms prior to transmitting the payload. Isolate the authentic carrier, invert the LTI multipath channel, and recover the hidden 200bps NRZ payload.
Method to Solve:
Analyze the CSV to find the rectangular channel-sounding pulse at t=12.5ms.
Use the pulse to characterize the acoustic cavity's impulse response h[n].
Apply a zero-forcing or Wiener filter equalizer to invert the LTI multipath channel, effectively canceling the spoofed open-water jammer (which didn't suffer the same multipath distortion).
Isolate the cleaned authentic carrier and demodulate the binary polar NRZ data starting at t=0.15s.
Group the 200bps stream into 8-bit MSB-first blocks and convert to ASCII.
Files Given to Solver: multipath_mirage.csv
Flag: SPIRAL{c0v3rt_4c0ust1c_3qu4l1z4t10n}
