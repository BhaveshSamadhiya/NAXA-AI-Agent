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
