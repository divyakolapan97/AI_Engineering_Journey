print("Hello")
print("Hello Divya")
import sys
# print(sys.version)
# print(sys.prefix)

# Write a script that prints your current Python version and exits with an error if it's below 3.10.

ver = sys.version_info

if ver <= (3,13):
    print("Error")
else:
    print("All good")

# Write a script that lists all installed packages in your current virtual environment, sorted alphabetically.

import subprocess

result = subprocess.run(
    ["pip", "list", "--format=freeze"],
    capture_output=True,
    text=True,
    check=True
)

packages = result.stdout.strip().split("\n")

for package in sorted(packages, key=str.lower):
    print(package)

