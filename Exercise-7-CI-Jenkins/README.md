# Exercise 7: Introduction to Continuous Integration (CI) and Jenkins Installation

## 1. Objective
To understand Continuous Integration (CI), learn its features and benefits, explore different CI tools, and install and access Jenkins using Docker.

## 2. What is Continuous Integration?
Continuous Integration is a software development practice in which developers frequently integrate their code changes into a shared repository. Automated builds and tests help identify errors early and improve software quality.

## 3. Key Features of CI
1. **Frequent Code Integration:** Developers regularly push code to a shared repository.
2. **Automated Builds:** Code changes trigger automated build processes.
3. **Automated Testing:** Tests check whether code changes work correctly.
4. **Immediate Feedback:** Developers receive results quickly and can fix errors.

## 4. Benefits of CI
- Early detection of bugs.
- Improved collaboration among developers.
- Faster development cycles.
- Better software quality.
- Reduced integration problems.

## 5. How CI Works
1. A developer writes and commits code.
2. The code is pushed to a version control repository.
3. A CI server detects the changes and triggers a pipeline.
4. The pipeline builds the application and runs tests.
5. The results are reported to the developer.

## 6. Examples of CI/CD Tools
- GitLab CI/CD
- CircleCI
- Travis CI
- Bamboo
- TeamCity
- Azure DevOps Pipelines
- GitHub Actions
- Spinnaker
- Buildkite
- Drone

## 7. Introduction to Jenkins
Jenkins is an open-source automation server used to automate software building, testing, and deployment. It supports Continuous Integration and Continuous Delivery through pipelines and plugins.

### Why Use Jenkins?
- Automates repetitive tasks.
- Supports CI workflows.
- Provides plugins for different tools.
- Supports distributed builds using agents.

### Key Jenkins Concepts
1. **Job:** A task configured in Jenkins.
2. **Build:** An execution of a job or pipeline.
3. **Pipeline:** A sequence of automated stages.
4. **Plugins:** Extensions that add functionality.
5. **Nodes:** Machines that execute Jenkins tasks.

## 8. Jenkins Installation Using Docker

Jenkins was installed using Docker with the following command:

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

**Note:** The existing Jenkins container and persistent volume from the previous exercise were reused.

### Verify the Container

```bash
docker ps
```

### Access Jenkins

Open the following address in a browser:

`http://localhost:8080/`

### Initial Setup
1. Retrieve the initial administrator password if required.
2. Unlock Jenkins.
3. Install the suggested plugins.
4. Create the administrator account.
5. Open the Jenkins dashboard.

## 9. Result
Continuous Integration concepts, features, benefits, and tools were reviewed. Jenkins was installed and accessed through Docker, and its initial setup was completed.