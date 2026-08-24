from traceback import format_list

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

#3. Write a script that checks if a `.env` file exists in the current directory; if not, create one with a placeholder `API_KEY=changeme`.

from pathlib import Path
env_f = Path(".env")
if env_f.exists():
    print(".env exist")
else:
    env_f.write_text("AP_KEY=name")
    print(".env created")

#count lines of code in py file

import os
totallines = 0
for file in os.listdir("."):
    if file.endswith((".py")):
        with open (file,"r") as f:
            lines = f.readlines()
        print(len(lines))
        totallines += len(lines)
print(totallines)

#Write a function that checks whether a given package name is installed, returning `True`/`False` (don't just try/except an import blindly — think about how to do this properly using `importlib.metadata`).


from importlib.metadata import PackageNotFoundError,version

def isavailable(packname):
    try:
        version(packname)
        return True
    except PackageNotFoundError:
        return False

print(isavailable("pytorch"))

#Write a script that creates the `week01`–`week22` folder structure programmatically (don't do it by hand).

# for week in range(1,23):
#     folder = Path(f"Week{week:02d}")
#     folder.mkdir()
#
# print("Week created")


# to dlete

from pathlib import Path
import shutil

for week in range(1, 23):
    folder = Path(f"week{week:01d}")

    if folder.exists():
        shutil.rmtree(folder)
        print(f"Deleted {folder}")

print("All week folders deleted.")

#COUNT OF COMMIT HAPPEN  git rev-list --count HEAD






