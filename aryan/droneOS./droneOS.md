Category: Edge AI & Computer Vision
Difficulty / Points: Easy / 150 pts
Challenge Description:
We intercepted an experimental neural firmware dump named drone_os.npz from an autonomous robotics test rig. According to leaked developer logs, the initial calibration instructions were drawn directly onto the vision layer, and an interactive simulation sandbox was packaged inside the weights to benchmark spatial navigation. Inspect the firmware, boot the calibration environment, and retrieve the root authorization token.
Method to Solve:
Load drone_os.npz in Python and inspect the array keys.
Plot vision_layer using OpenCV or Matplotlib to read the hidden execution command: exec(zlib.decompress(data['sim_code']).decode()).
Run the command to boot the 3D voxel sandbox.
Use the WASD keys and mouse to navigate, and left-click to mine exactly 20 chunks.
Press the 3 key to "forge the pickaxe," which mathematically triggers an XOR decryption of flag_layer and displays the flag.
Files Given to Solver: drone_os.npz (or packaged as drone_os.npz.zip)
Flag: SPIRAL{3dg3_41_4c3_p1l0t}
