
import os
from snapshot_name import getSnapshotName
from update_gradle import updateGradle
from update_npm import updateNpm
import warnings
import subprocess
import os.path

subprocess.run(["git", "config", "--global", "--add", "safe.directory", "/github/workspace"])

version_type = os.getenv("INPUT_VERSION_TYPE").casefold() 
is_snapshot = os.getenv("INPUT_SNAPSHOT").casefold() == "true"

if os.path.isfile("gradle.properties"):
    updateGradle(version_type, is_snapshot)

if os.path.isfile("package.json"):
    updateNpm(version_type, is_snapshot)

save_to_gh_output = os.getenv("INPUT_SAVE_VERSION_TO_GH_OUTPUT").casefold() == "true"

if (save_to_gh_output):
    path = os.getenv("GITHUB_OUTPUT")
    if path is None:
        warnings.warn("$GITHUB_OUTPUT is null")
    file = open(path, "w")
    file.write("version=" + newVersion + "\n")