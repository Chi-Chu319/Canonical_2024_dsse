import sys
import os
from package_utils import *
from log_utils import *
from dotenv import load_dotenv

load_dotenv()

# variables
content_indices_filename = "Contents-{}"
debian_mirror_url = os.environ['DEBIAN_MIRROR_URL']
download_dir = os.environ['DOWNLOAD_DIR']

# validates the arguments
if len(sys.argv) == 2:
    architecture = sys.argv[1]
    content_indices_filename = content_indices_filename.format(architecture)

    remote = debian_mirror_url + content_indices_filename
    local = download_dir + content_indices_filename

    file_content = download_contents_indices(remote, local)
    package_statistics = get_package_statistics(file_content)
    log_package_statistics(package_statistics)
else:
    # if the argument is not valid, print the usage and exit
    log_usage()
    sys.exit(1)
