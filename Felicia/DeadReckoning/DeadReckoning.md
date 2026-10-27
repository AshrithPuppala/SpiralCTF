Category: Control Systems / Signals & Systems 						
Difficulty: Medium–Hard 									 
Points: 350

Description:

Our autonomous warehouse rover was supposed to drive a straight diagonal calibration path across the lab floor. According to its primary GPS log (gps_x, gps_y), everything went according to plan.
However, security cameras caught the rover swerving erratically across the floor, and we suspect an attacker spoofed the primary GPS receiver while the rover followed a hidden trajectory. You are given rover_telemetry.csv sampled at fs=20Hz (t=0.05s), containing:
t: Timestamp in seconds
imu_ax, imu_ay: Onboard MEMS accelerometer readings (m/s2), which suffer from unknown constant factory bias and thermal noise.
gps_x, gps_y: Primary position sensor (m) — suspected compromise.
beacon_valid: 1 when the rover passes under an uncompromised ceiling UWB anchor (every 2.5 seconds), 0 otherwise.
beacon_x, beacon_y: Ceiling UWB position measurement (m), valid only when beacon_valid == 1.

Task: The attacker tried to cover their tracks, but the physics don't lie. Reconstruct the true 2D trajectory (x(t),y(t)) of the rover to read the flag it traced on the warehouse floor. 

