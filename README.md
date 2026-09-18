# NAXA AI Agent

A Python-based automation and watchdog system designed to automate application launching and monitor running processes.

## Features

- Automatically launches Chrome and web applications
- Opens Google, YouTube and WhatsApp Web
- Automatically starts the Python test process
- Monitors whether `test.py` is running
- Automatically restarts `test.py` if it stops
- Uses process monitoring for continuous execution
- Supports Windows-based automation

## Technologies Used

- Python
- psutil
- subprocess
- os
- time
- Windows Batch Script

## Project Files

- `service_v2.py` — Main watchdog and automation script
- `test.py` — Test process monitored by the watchdog
- `run.bat` — Batch file used to start the project

## How It Works

1. The watchdog service starts.
2. Required applications and websites are opened.
3. `test.py` is started automatically.
4. The service continuously checks whether `test.py` is running.
5. If `test.py` stops, the service automatically starts it again.

## Purpose

This project demonstrates Python automation, process monitoring, subprocess management and continuous task execution on Windows.

## Author

Bhavesh Samadhiya

## Requirements

- Python 3.x
- Windows OS
- psutil
- pyautogui
- Microsoft Visual Studio Code

## Installation

Install the required Python libraries:

```bash
pip install psutil pyautogui

## How to Run

1. Open the project folder.
2. Make sure `timer.txt` is available.
3. Run:

```bash
python service_v2.py

You can also use `run.bat`.

## Note

This project is currently configured for a specific Windows environment and uses a local VS Code installation path.
