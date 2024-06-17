# Package Statistics Command Line Tool

This Python 3 command line tool downloads and analyzes Debian package Contents files. It takes an architecture type (e.g., amd64, arm64, mips) as an argument, downloads the corresponding compressed Contents file from a Debian mirror, parses the file, and outputs statistics of the top 10 packages with the most files.

## Prerequisites

- Python 3.6+
- `virtualenv` for virtual environment management

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set up the virtual environment:**

    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies from `requirements.txt`:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Set the environment variables:**

    ```bash
    export DEBIAN_MIRROR_URL=http://ftp.uk.debian.org/debian/dists/stable/main/
    export DOWNLOAD_DIR=./downloads/
    ```

2. **Run the program:**

    ```bash
    python package_statistics.py <architecture>
    ```

    Replace `<architecture>` with the desired architecture type (e.g., `amd64`, `arm64`, `mips`).

## Example

```bash
$ python package_statistics.py amd64
1. <package name 1>         <number of files>
2. <package name 2>         <number of files>
......
10. <package name 10>         <number of files>
```

## Notes

- Ensure the environment variables `DEBIAN_MIRROR_URL` and `DOWNLOAD_DIR` are set correctly before running the script.
- The `DOWNLOAD_DIR` should be a writable directory where the compressed Contents files will be downloaded.

## Acknowledgements

- The Debian Project for their detailed documentation on repository formats.
- All contributors to this project.

---

For more information on Debian repository formats, refer to the [Debian Wiki](https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices).
