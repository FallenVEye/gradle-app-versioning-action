
import semver
from configobj import ConfigObj
from snapshot_name import get_snapshot_name
from pathlib import Path
def updateGradle(version_type: str, is_snapshot: bool, gradle_file: Path):
    
    config = ConfigObj(str(gradle_file.resolve()))
    version = semver.Version.parse(config["version"])
    
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
        newVersion += "-SNAPSHOT-" + get_snapshot_name()

    config["version"] = newVersion
    config.write()
    
    return newVersion

    
