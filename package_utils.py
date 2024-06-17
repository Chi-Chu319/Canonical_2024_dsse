from debian.debian_support import download_file


# download the file and unzip and return the contents
def download_contents_indices(remote, local):
    # download the file
    download_file(remote, local)

    # unzip the file
    with open(local, "rb") as f:
        contents = f.read()
        contents = contents.decode("utf-8")
        contents = contents.split("\n")
        return contents


# get the package statistics by parsing the contents
def get_package_statistics(content):
    package_statistics = {}
    for line in content:
        if line:
            parts = line.split()
            if len(parts) < 2:
                continue
            package = parts[-1]
            if package in package_statistics:
                package_statistics[package] += 1
            else:
                package_statistics[package] = 1

    return package_statistics

