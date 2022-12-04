import glob
import zipfile


EXTRACT_TO = './daz_3d_content_extractor'

def find_zip_locations() -> dict:
    print("Locating zip files... ", end="")
    files = glob.glob("*/*.zip")
    print(f"There are {len(files)} archives to extract!")
    return files

def extract_all(archives):
    print(f"\nExtracting {len(archives)} archives...")
    for archive in archives:
        print(f"\tExtracting '{archive}'...", end="")
        with zipfile.ZipFile(archive, 'r') as zip_ref:
            zip_ref.extractall(EXTRACT_TO)
            print(" Done!")

if __name__ == '__main__': 
    print("Tool made by WaWalex :)\nOriginal source: https://github.com/WaWalex/daz3d_content_extractor\n")
    zip_locations = find_zip_locations()
    input(f"Press ENTER to extract them all to '{EXTRACT_TO}'...")
    extract_all(zip_locations)
    print("All archives are been extracted!")