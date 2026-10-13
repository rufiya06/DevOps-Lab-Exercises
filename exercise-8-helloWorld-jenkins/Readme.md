# Creating a Hello World Jenkins Job

## 1. Objective

To create and execute a simple Jenkins Freestyle job that retrieves a shell script from GitHub and displays `Hello, Jenkins!` in the build console output.

## 2. Tools and Technologies Used

- **Git:** Version control.
- **GitHub:** Hosting the source code repository.
- **Jenkins:** Automating and executing the job.
- **Docker:** Running Jenkins in a container.
- **Bash Shell:** Executing the shell script.

## 3. GitHub Repository

A public GitHub repository named `devops-sample-code` was created to store the shell script.

Repository URL: https://github.com/rufiya06/devops-sample-code

## 4. Shell Script

The file `hello-world.sh` contains the following code:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

The script prints the message `Hello, Jenkins!` when executed.

## 5. Steps Performed

### Step 1: Create the GitHub Repository
Created the public repository `devops-sample-code` on GitHub.

### Step 2: Create the Shell Script
Created `hello-world.sh` locally with a Bash shebang and an echo command.

### Step 3: Push the Script to GitHub
Initialized a local Git repository, added the script, committed the changes, and pushed it to GitHub.

### Step 4: Create the Jenkins Job
Opened the Jenkins dashboard at `http://localhost:8080/`, selected **New Item**, entered `HelloWorld`, and selected **Freestyle project**.

### Step 5: Configure Source Code Management
Selected Git and configured the following repository:

`https://github.com/rufiya06/devops-sample-code.git`

The branch was set to `*/main`. Since the repository is public, no repository credentials were required.

### Step 6: Configure the Build Step
Added **Execute shell** under Build Steps and entered:

```bash
sh hello-world.sh
```

Saved the job configuration.

### Step 7: Execute the Job
Clicked **Build Now** and opened the build's Console Output to verify the result.

## 6. Expected Output

```text
Hello, Jenkins!
Finished: SUCCESS
```

The successful output confirms that Jenkins retrieved the script and executed the configured build step.

## 7. Result

The Hello World Jenkins Freestyle job was configured and executed successfully. Jenkins retrieved the shell script from GitHub, executed it, and displayed `Hello, Jenkins!` with a successful build status.

## 8. Screenshots

Screenshots of the Jenkins job configuration, job page, and successful Console Output can be stored in the `screenshots` folder as practical evidence.