def log_usage():
    print("Usage: python3 package_statistics.py <architecture>")


def log_downloading_file(filename):
    """Log that a file is being downloaded."""
    print("Downloading file: {}".format(filename))


def log_unzipping_file(filename):
    """Log that a file is being unzipped."""
    print("Unzipping file: {}".format(filename))


def log_file_exists(filename):
    """Log that a file already exists."""
    print("File exists: {}".format(filename))


def log_contents_indices_not_found(architecture):
    """Log that the contents file for the given architecture was not found."""
    print("Contents-{} not found".format(architecture))


def log_package_statistics(package_statistics):
    """Log the package statistics."""
    for package, count in package_statistics.items():
        print("{}: {}".format(package, count))
