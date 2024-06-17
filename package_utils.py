from debian.debian_support import download_file
import os
from typing import List
from log_utils import log_file_exists, log_downloading_file, log_reading_file
import re


def download_contents_indices(remote, local) -> List[str]:
    """Download the contents indices file and return the contents.

    Args:
        remote (str): The remote URL of the file.
        local (str): The local path to save the file.
    """

    # if the file exists, no need to download
    if os.path.exists(local):
        log_file_exists(local)
        with open(local, "rb") as f:
            contents = f.read()
            contents = contents.decode("utf-8")
            contents = contents.split("\n")
            return contents

    log_downloading_file(remote)
    # downloads the file
    download_file(remote, local)

    log_reading_file(local)
    with open(local, "rb") as f:
        contents = f.read()
        contents = contents.decode("utf-8")
        contents = contents.split("\n")
        return contents


def get_package_statistics(content) -> dict:
    """Get the package statistics by parsing the contents.

    Args:
        content (List[str]): The contents of the file.
    """
    package_statistics = {}
    for line in content:
        if line:
            parts = line.split()
            # skip the free form description
            if len(parts) < 2 or re.match(r'^\s*(#|$)', line):
                continue
            # some lines have more than 2 parts, but the package name is always the last part
            package = parts[-1]
            if package in package_statistics:
                package_statistics[package] += 1
            else:
                package_statistics[package] = 1

    return package_statistics

