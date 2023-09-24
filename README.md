# Wi-Fi Profile Extractor Readme

## Overview
The Wi-Fi Profile Extractor is a Python script that allows you to extract saved Wi-Fi profiles and their associated passwords from Windows and Linux machines. It uses system-specific commands and file structures to retrieve this information.

## Features
- Extracts saved Wi-Fi SSIDs and their associated security details.
- Supports both Windows and Linux operating systems.
- Provides an option to print the extracted profiles in a tabular format.

## Prerequisites
Before using the Wi-Fi Profile Extractor, make sure you have the following prerequisites in place:

1. Python: The script is written in Python, so you need to have Python installed on your system.

2. Dependencies: The script uses the following Python libraries, which should be installed:
   - `subprocess`
   - `os`
   - `re`
   - `collections.namedtuple`
   - `configparser`

## Usage

### Running the Script
1. Clone or download the script to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is located.

4. Run the script using the following command:
   ```
   python wifi_profile_extractor.py
   ```

### Output
- When you run the script, it will display the saved Wi-Fi profiles and their associated information in a tabular format.

- For Windows, it will show SSID, Ciphers, and Key (password).
- For Linux, it will show SSID, Authentication Algorithm, Key Management, and PSK (password).

## Configuration
The script does not require any specific configuration. However, you can customize the following:

- **Verbosity**: You can control the verbosity of the output by changing the `verbose` parameter when calling the `print_profiles()` function. A higher verbosity level (e.g., `verbose=1`) will display more detailed information about each profile.

## Compatibility
The Wi-Fi Profile Extractor is compatible with both Windows and Linux operating systems. The script automatically detects the operating system and extracts profiles accordingly.

## Important Notes
- For Linux, the script extracts profiles from the `/etc/NetworkManager/system-connections/` directory, which requires administrative privileges.

- Ensure that the script is executed with the necessary permissions to access the Wi-Fi profile information.

- The script may not work on operating systems other than Windows and Linux.

## License
This script is provided under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.

## Author
This script was created by  TheODDYSEY.

Feel free to reach out if you have any questions or encounter any issues while using this script.
