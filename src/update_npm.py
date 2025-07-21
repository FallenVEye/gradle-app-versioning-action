
import json
import semver
from snapshot_name import get_snapshot_name
from pathlib import Path

def updateNpm(version_type: str, is_snapshot: bool, npm_file: Path):

    with npm_file.open() as file:
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

    new_version = str(version)
    if is_snapshot:
        new_version += "-SNAPSHOT-" + get_snapshot_name()

    package["version"] = new_version

    with npm_file.open("w") as file:
        json.dump(package, file, indent=2)

    return new_version