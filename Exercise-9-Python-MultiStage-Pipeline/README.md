# Exercise 9: Python Multi-Stage Jenkins Pipeline
## Objective
Build, test, deploy, run, and verify a Python Flask application using a Jenkins multi-stage pipeline.
## Tools Used
- Jenkins
- Docker
- Python 3
- Flask
- Git and GitHub
- PowerShell
## Application
The Flask application responds to requests at `/` with:
`Hello, Jenkins Multi-Stage Pipeline!`
## Pipeline Stages
1. **Build:** Creates a Python virtual environment and installs dependencies from `requirements.txt`.
2. **Test:** Runs unit tests using Python unittest.
3. **Deploy:** Copies the application and test files into `python-app-deploy`.
4. **Run Application:** Starts the Flask application in the background.
5. **Test Application:** Checks the deployed HTTP endpoint and runs the unit tests again.
## Project Files
- `app.py`: Flask application.
- `requirements.txt`: Python dependencies.
- `test_app.py`: Unit tests.
- `Jenkinsfile`: Defines the five pipeline stages.
- `hello-world.sh`: Previous Jenkins Hello World exercise.
## Jenkins Configuration
- Job: `Python-MultiStage-Pipeline`
- Repository: https://github.com/rufiya06/devops-sample-code
- Branch: `main`
- Pipeline script: `Jenkinsfile`
## Result
The Jenkins build completed successfully with `Finished: SUCCESS`.
## Screenshots
Evidence for this exercise is stored in the `screenshots` folder.
