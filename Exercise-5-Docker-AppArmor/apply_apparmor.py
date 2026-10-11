
import docker

client = docker.from_env()

# Build the Flask image
print("Building Flask image...")
client.images.build(path=".", tag="flask-apparmor")

# Check whether Docker reports AppArmor support
info = client.info()
security_options = info.get("SecurityOptions", [])

print("Docker security options:", security_options)

if not any("apparmor" in str(option).lower()
           for option in security_options):
    print(
        "AppArmor is not reported by this Docker Engine. "
        "Run this script in a Linux environment with AppArmor enabled "
        "before attempting profile enforcement."
    )
else:
    print(
        "AppArmor is reported by Docker. "
        "Load the custom profile in the Linux host before running "
        "the container with that profile."
    )
