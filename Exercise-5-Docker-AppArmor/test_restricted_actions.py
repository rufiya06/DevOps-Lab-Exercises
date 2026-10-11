
import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    ports={"5000/tcp": None},
    detach=True
)

try:
    print("Container started:", container.short_id)

    # Baseline diagnostic only. These tests do not prove AppArmor denial.
    for command in [
        ["sh", "-c", "cat /etc/passwd"],
        ["sh", "-c", "command -v bash"]
    ]:
        result = container.exec_run(command)
        print("Command:", command)
        print("Exit code:", result.exit_code)
        print("Output:", result.output.decode(errors="replace"))

    print(
        "Note: these are baseline tests without a custom AppArmor profile. "
        "Successful or failed commands do not demonstrate AppArmor enforcement."
    )
finally:
    container.stop()
    container.remove()
    print("Container stopped and removed.")
