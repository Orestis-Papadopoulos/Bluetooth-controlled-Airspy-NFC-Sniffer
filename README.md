# Goal
Sniff NFC traffic at public transport terminals

# Setup
1. airspy mini
2. SMA male cable
3. modified ticket for antenna
4. laptop
5. Serial Bluetooth Terminal app on phone

# Tools
1. 64-bit installer for the Microsoft Visual C++ Redistributable (2010 version and latest version)
2. airspy host tools
3. nfc-lab

# Instructions

1. Install Microsoft Visual C++ Redistributable
   - latest version at https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
   - 2010 version https://www.microsoft.com/en-us/download/details.aspx?id=26999
3. Download "airspy_host_tools_win32_x86_x64_v1_0_10.zip" from: https://github.com/airspy/airspyone_host/releases?utm_source=chatgpt.com#release-v1.0.10
4. Extract the downloaded folder
5. Put the .py files together with the executables
6. Pair phone with laptop
7. Setup Serial Bluetooth Terminal with three buttons; 'Start', 'Stop', 'Shutdown'
8. Run the first .py file to listen for a Bluetooth connection
9. Connect through the phone
10. Start/stop recording or shutdown using the respective buttons
11. Convert the .raw output files to .wav format to open them in nfc-lab
12. Download "nfc-lab-3.4.2-x86_64-installer.exe" from: https://github.com/josevcm/nfc-laboratory/releases/tag/3.4.2
13. Open the .wav on nfc-laboratory
14. Search for a block starting with "1b"; this is the PWD_AUTH command; the four bytes following "1b" are the ticket's password
