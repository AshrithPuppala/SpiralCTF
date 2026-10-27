Category: Digital Signal Processing (DSP) 							
Difficulty: Hard 										
Points: 450

Description: We monitored a compromised server rack, but the resulting audio capture (radar_if.wav) is flooded with heavy background noise. It might sound like a standard broadcast, but the attacker hid a dead-drop routing sequence deep within the interference.
To extract the coordinates, look at the big picture. Analyse the entire audio file at once to find the loudest overlapping frequencies dominating the spectrum. Ignore the minor shifts and baseline static; the absolute highest peaks of the whole recording will point you in the right direction. Once you locate the remote drop and recover the final payload, simply decode the remaining data to reveal the attacker's true message.
