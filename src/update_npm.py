
import json
import semver
from snapshot_name import getSnapshotName

def updateNpm(version_type: str, is_snapshot: bool):

    with open("package.json", "r") as file:
        package = json.load(file)
    
    version = semver.Version.parse(package["version"])
    
    match version_type:
        case "major":
            version = version.bump_major()
        case "minor": 
            version = version.bump_minor()
        case "patch":
            version = version.bump_patch()
        case _:
            raise ValueError("Unknown version type")

    newVersion = str(version)
    if is_snapshot:
        newVersion += "-SNAPSHOT-" + getSnapshotName()

    package["version"] = newVersion

    with open("package.json", "w") as file:
        json.dump(package, file, indent=2)

    return newVersion