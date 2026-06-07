#!/usr/bin/env python3

# Imports
import os
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS


# Month dictionary
MONTHS = {
    1: "01 January", 2: "02 February", 3: "03 March", 4: "04 April",
    5: "05 May", 6: "06 June", 7: "07 July", 8: "08 August",
    9: "09 September", 10: "10 October", 11: "11 November", 12: "12 December"
}


# Helper functions
def get_photo_date(file: Path) -> datetime:
    """Try to get the photo date from EXIF data; fallback to file modification date."""
    try:
        image = Image.open(file)
        exif_data = image._getexif()
        if exif_data:
            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                if tag_name == 'DateTimeOriginal':
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass
    return datetime.fromtimestamp(file.stat().st_mtime)

def md5_hash(file: Path) -> str:
    """Compute the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            hash_md5.update(block)
    return hash_md5.hexdigest()

def get_unique_filename(dest: Path, original_name: str, content_hash: str) -> Path | None:
    """Generate a unique filename in the destination folder to avoid duplicates."""
    final_dest = dest / original_name
    if not final_dest.exists():
        return final_dest
    elif md5_hash(final_dest) == content_hash:
        return None  # Same content already exists
    else:
        name_base, ext = os.path.splitext(original_name)
        counter = 1
        while True:
            new_name = f"{name_base}_{counter}{ext}"
            new_dest = dest / new_name
            if not new_dest.exists():
                return new_dest
            elif md5_hash(new_dest) == content_hash:
                return None  # Duplicate with same content
            counter += 1


# Main function
def organize_photos(source: Path, destination: Path):
    """Organize photos into subfolders by year and month."""

    print("")
    print("======================================================================================================================================")
    print("📁 Routes entered by the user:")
    print("======================================================================================================================================")

    if not source.exists():
        print(f"❌ Error: Source path does not exist: {source}")
        return
    if not destination.exists():
        destination.mkdir(parents=True, exist_ok=True)

    print(f"  📸 Organizing photos from: {source}")
    print(f"  📂 Saving into: {destination}")

    print("")
    print("======================================================================================================================================")
    print("🚀 Starting the organization process...")
    print("======================================================================================================================================")

    moved_count = 0
    skipped_count = 0

    for file in source.iterdir():
        if file.is_file():
            date = get_photo_date(file)
            year = str(date.year)
            month = MONTHS[date.month]

            final_folder = destination / year / month
            final_folder.mkdir(parents=True, exist_ok=True)

            file_hash = md5_hash(file)
            final_dest = get_unique_filename(final_folder, file.name, file_hash)

            if final_dest:
                shutil.move(str(file), str(final_dest))
                # Mostrar solo la ruta relativa al destino
                relative_path = final_dest.relative_to(destination)
                print(f"  ✅ Moved: {file.name} → {relative_path}")
                moved_count += 1
            else:
                print(f"  🔁 Already exists (skipped): {file.name}")
                skipped_count += 1

    print("")
    print("======================================================================================================================================")
    print("🏁 Organization process completed:")
    print("======================================================================================================================================")
    print(f"  🎉 Photos organized successfully.")
    print(f"  📦 Moved: {moved_count}")
    print(f"  🚫 Skipped (duplicates): {skipped_count}")
    print("")


# Entry point
if __name__ == "__main__":
    print("")
    print("###########################################################################################################################################################")
    print("                                                                   📸 PHOTO ORGANIZER 📸                                                                   ")
    print("###########################################################################################################################################################")
    print("")
    print("======================================================================================================================================")
    print("📁 Please provide the folder paths:")
    print("======================================================================================================================================")
    source_input = input("  ⌨️ Enter the source folder path: ").strip().strip("'\"")
    destination_input = input("  ⌨️ Enter the destination folder path: ").strip().strip("'\"")

    source_path = Path(source_input).expanduser().resolve()
    destination_path = Path(destination_input).expanduser().resolve()

    organize_photos(source_path, destination_path)
