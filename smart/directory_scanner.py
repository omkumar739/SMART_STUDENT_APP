import os
class MissingFileOrFolderError(Exception): pass

def scan_directory(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid path: {path}")
        for root, dirs, files in os.walk(path):
            print(f"Directory: {root}")
            for f in files: print(f" File: {f}")
            if not files and not dirs:
                raise MissingFileOrFolderError(f"Empty folder: {root}")
    except Exception as e:
        print(f"Error: {e}")

# Usage: scan_directory("path_to_scan")