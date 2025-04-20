import re
import json
from os import listdir, path
from snowcrypt import snowcrypt
from multiprocessing import Pool
from argparse import ArgumentParser
from pathlib import Path


KEYIV_PATTERN = re.compile(rb'(\{\"(iv|key)\"\: ?\"([a-zA-Z0-9]*)\",\"(iv|key)\"\: ?\"([a-zA-Z0-9]*)\"\})')


def get_keys(path: str) -> dict[str, str]:
    with open(path, "rb") as fd:
        result = KEYIV_PATTERN.search(fd.read())
        if result is None:
            raise Exception("Cannot extract key, iv from file.")
        data = result.group(0).decode('utf-8')
        return json.loads(data)


def derive_target_name(path: str) -> str:
    return path.replace(".AAX", ".m4a")


def convert(source: str) -> None:
    print(f"starting on file {source}")
    target = derive_target_name(source)
    keys = get_keys(source)
    snowcrypt.decrypt_aaxc(source, target, keys["key"], keys["iv"])
    #print(f"Would convert {source} and write output to {target} using key={keys['key']}, iv={keys['iv']}")


def find_all_aax(root_path: str) -> list[str]:
    return [path.join(root_path, x) for x in listdir(root_path) if x.endswith(".AAX")]


def get_opts():
    ap = ArgumentParser()
    ap.add_argument("DIRECTORY", help="The directory to search for AAX files.")
    return ap.parse_args()

def main():

    opts = get_opts()
    source_dir = Path(opts.DIRECTORY)

    if not source_dir.exists():
        print("That directory doesn't exist")
        return 1
    if not source_dir.is_dir():
        print("That path is not a directory.")
        return 1

    with Pool(processes=32) as pool:
        pool.map(convert, find_all_aax(str(source_dir)))


if __name__ == "__main__":
    main()
