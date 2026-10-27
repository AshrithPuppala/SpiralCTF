Category: Hardware Security / Forensics 							
Difficulty: Easy 										
Points: 200

Description: We managed to hook a logic analyser up to the internal I2C bus of a recovered embedded device. We know the central microcontroller reads the secure flag directly from an external EEPROM chip on boot, but the capture file is flooded with continuous background noise from the system's real-time clock.
Your objective is to filter through the raw traffic dump to isolate the memory reads. Before extracting the payload, the microcontroller briefly writes a single-byte configuration key to an isolated register. Find that key, apply it to the encrypted EEPROM data, and recover the plaintext flag.
