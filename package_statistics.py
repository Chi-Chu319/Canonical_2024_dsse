import sys
from package_utils import *
from log_utils import *
from dotenv import load_dotenv

load_dotenv()

# variables
content_indices_filename = "Contents-{}"
debian_mirror_url = os.getenv("DEBIAN_MIRROR_URL", "http://ftp.uk.debian.org/debian/dists/stable/main/")
download_dir = os.getenv("DOWNLOAD_DIR", "./downloads/")


# validates the arguments
if not len(sys.argv) == 2:
    # if the argument is not valid, print the usage and exit
    log_usage()
    sys.exit(1)

# preparing the variables
architecture = sys.argv[1]
content_indices_filename = content_indices_filename.format(architecture)

remote = debian_mirror_url + content_indices_filename
local = download_dir + content_indices_filename

# downloads the file and get the package statistics
try:
    lines = download_contents_indices(remote, local)
except Exception as e:
    log_contents_indices_not_found(architecture)
    sys.exit(1)

package_statistics = get_package_statistics(lines)
log_package_statistics(package_statistics)

