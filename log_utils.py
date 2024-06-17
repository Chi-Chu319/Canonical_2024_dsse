def log_usage():
    print("Usage: python3 package_statistics.py <architecture>")


def log_contents_indices_not_found(architecture):
    print("Contents-{} not found".format(architecture))


def log_package_statistics(package_statistics):
    for package, count in package_statistics.items():
        print("{}: {}".format(package, count))
