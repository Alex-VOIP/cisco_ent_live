# Cisco Live Screen Viewer

## Purpose

This project provides a simple desktop application to view a live feed of a Cisco IP phone's screen. It's useful for monitoring a phone's display remotely, for testing, or for presentations.

The application continuously fetches screenshots from the phone and displays them in a `tkinter` window.

## Setup

### Prerequisites

- Python 3.x
- `pip` for installing packages

### Dependencies

The script requires the following Python libraries:

- `requests`
- `Pillow` (PIL)

You can install them using `pip`:

```bash
pip install requests Pillow
```

### Configuration

Before running the script, you need to configure the following variables in `cisco_live.py`:

- `PHONE_IP`: The IP address of your Cisco phone.
- `REFRESH_TIME`: The time in seconds between screen refreshes.

You will also need the username and password for your Cisco phone. The script currently uses the default credentials `cisco:cisco`. If your credentials are different, you will need to update the `auth` parameter in the `requests.get` call within the `loop` method.

## Usage

To run the application, simply execute the `cisco_live.py` script from your terminal:

```bash
python cisco_live.py
```

This will open a window on your desktop that displays the live screen of your Cisco phone. To close the application, simply close the window.
