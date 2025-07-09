
import os
from configobj import ConfigObj
from pystreamapi import Stream
from snapshot_name import getSnapshotName

version_type = os.getenv("INPUT_VERSION_TYPE").casefold() 
is_snapshot = os.getenv("INPUT_SNAPSHOT").casefold() == "true"

config = ConfigObj("gradle.properties")
version = list(map(int, str(config["version"]).split(".")))

match version_type:
    case "major":
        version[0] += 1
        version[1] = 0
        version[2] = 0
    case "minor": 
        version[1] += 1
        version[2] = 0
    case "patch":
        version[2] += 1
    case _:
        raise ValueError("Unknown version type")

newVersion = ".".join(list(map(str, version)))
if is_snapshot:
    newVersion += "-SNAPSHOT-" + getSnapshotName()

config["version"] = newVersion
config.write()

print(newVersion)