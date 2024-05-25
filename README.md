# Keylogger

This project implements a basic keylogger using Python's `pynput` library to capture keystrokes and periodically send the captured data to a specified server via HTTP POST requests.

## Features

- Captures keystrokes using `pynput`.
- Periodically sends the captured keystrokes to a specified server.
- Configurable IP address, port number, and time interval for sending data.

## Requirements

- Python 3.x
- `pynput` library
- `requests` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/keylogger-project.git
   cd keylogger-project
   ```

2. Install the required libraries:

   ```bash
   pip install pynput requests
   ```

## Configuration

1. Open the `keylogger.py` file.

2. Set the `ip_address` and `port_number` variables to the appropriate values for your server:

   ```python
   ip_address = "your_server_ip_address"
   port_number = "your_server_port_number"
   ```

3. Optionally, adjust the `time_interval` variable to set the desired time interval (in seconds) for sending the captured keystrokes:

   ```python
   time_interval = 10  # Time interval in seconds
   ```

## Usage

1. Run the keylogger script:

   ```bash
   python keylogger.py
   ```

2. The script will start capturing keystrokes and periodically send the data to the specified server.

## Disclaimer

This project is intended for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Use this project responsibly and only on systems where you have explicit permission to do so.

