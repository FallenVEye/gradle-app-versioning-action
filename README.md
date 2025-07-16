# FallenVEye/versioning-action
This action is used to update version property of project according to semver

# Support
 - Gradle 
 - NPM

# Explanation
## Gradle
Updates ```version``` entry in ```gradle.properties``` file
## NPM
Updates ```version``` entry in ```package.json``` file

# Usage
``` yaml
uses: FallenVEye/versioning-action@master
  with:
    # Used to determine if a version is a snapshot
    # Not required
    # Accepted values(case insensitive): True|False
    # Default: False
    snapshot: ''

    # What next version shoud be? major|minor|patch
    # Required
    # Accepted values(case insensitive): major|minor|patch
    version_type: ''

    # Shoud the snapshot version include some uniqueness?
    # Not required
    # Accepted values(case insensitive): none|commit|date-time
    #   none - generated version is not unique
    #   commit - unique by commit hash
    #   date-time - unique by date-time of action run 
    # Default: false
    unique_snapshot: ''

    # Optionally store generated version in GH_OUTPUT
    # Not required
    # Accepted values(case insensitive): True|False
    # Default: False
    save_version_to_gh_output: ''   
```

# Outputs
| Name    | Description      | Example                                  |
|---------|------------------|------------------------------------------|
| version | Generated version| 1.6.3-SNAPSHOT-add-endpoints-10-07-22-30 |
    
# Scenarios

## Generate new minor release version
``` yaml
- uses: FallenVEye/versioning-action@master
  with:
    version_type: minor
```

## Generate new minor snapshot version with unique by date-time and write to GH_OUTPUT
``` yaml
- uses: FallenVEye/versioning-action@master
  with:
    version_type: minor
    snapshot: true
    unique_snapshot: date-time
    save_version_to_gh_output: true
```