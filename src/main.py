
import os
from update_gradle import updateGradle
from update_npm import updateNpm
import warnings
import subprocess
import os.path
from pathlib import Path

subprocess.run(["git", "config", "--global", "--add", "safe.directory", "/github/workspace"])

version_type = os.getenv("INPUT_VERSION_TYPE").casefold() 
is_snapshot = os.getenv("INPUT_SNAPSHOT").casefold() == "true"
context = os.getenv("INPUT_CONTEXT").casefold()

new_version = ""

gradle_file = Path(context, "gradle.properties") 
if gradle_file.is_file():
    new_version = updateGradle(version_type, is_snapshot, gradle_file)

npm_file = Path(context, "package.json")
if npm_file.is_file():
    new_version = updateNpm(version_type, is_snapshot, npm_file)

save_to_gh_output = os.getenv("INPUT_SAVE_VERSION_TO_GH_OUTPUT").casefold() == "true"

if (save_to_gh_output):
    path = os.getenv("GITHUB_OUTPUT")
    if path is None:
        warnings.warn("$GITHUB_OUTPUT is null")
    file = open(path, "w")
    file.write("version=" + new_version + "\n")