Category: Edge AI / Reverse Engineering 							
Difficulty: Hard										
Points: 400

Description: We intercepted a rogue autonomous drone and recovered its compiled flight controller executable (uplink.exe). The drone's true origin coordinates (the flag) are AES-encrypted inside the binary, but the decryption sequence is locked behind a strict Edge AI calibration protocol.
The terminal requires exactly 5 rotor voltage inputs. Any deviation from the optimal flight metrics triggers a catastrophic rotor stall sequence that instantly terminates the telemetry connection, leaving zero margin for brute-force attacks. To bypass the calibration gate, you must extract the drone's internal neural network (firmware.tflite), analyse its topology, and mathematically derive the exact input vector that produces the required target output.

Note: There are two paths to the flag. You can reverse the mathematics of the Edge TPU, or you can dissect the executable's memory architecture and rip the cryptography variables out by the roots.
