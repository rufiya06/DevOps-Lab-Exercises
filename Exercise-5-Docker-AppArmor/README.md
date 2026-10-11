# Exercise 5: Docker Security with AppArmor and Python

## Objective
To understand container security using AppArmor profiles and the Docker SDK for Python.

## Tools Used
- Docker Desktop
- Python
- Flask
- Docker SDK for Python
- VS Code
- PowerShell

## Tasks Completed

1. Created a Flask application in `app.py`.
2. Created a Dockerfile and built the `flask-apparmor` image.
3. Ran the Flask container and tested the application in a browser.
4. Checked Docker Engine security options.
5. Checked AppArmor kernel availability.
6. Prepared Python scripts to inspect Docker security support and run baseline container diagnostics.

## Environment Limitation
The practical was performed on Windows using Docker Desktop. Docker reported `seccomp` but did not report AppArmor in its security options. The AppArmor kernel check returned `N`, indicating AppArmor was not enabled in the checked kernel environment.

Therefore, custom AppArmor profile enforcement and denial of restricted actions were not verified in this environment. These steps require a suitable Linux host or VM with AppArmor enabled and Docker configured to use the loaded profile.

## Result
The Flask application was containerized and tested. Docker security capabilities were inspected, and the environment limitation for AppArmor enforcement was documented.