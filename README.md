<p align="center">
  <img src="assets/cover.png" alt="Photo Organizer Banner" style="width:100%">
</p>

<div align="center">
  <h1><span style="color: #eeb251ff;">Photo Organizer</span></h1>
  <h2><span style="color: #dece63ff;">Organize your photos by year and month automatically</span></h2>

  <hr style="border:none; height:0.3px; background-color:#777; width:65%; margin:30px auto 35px auto;">

  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python"></a>
    <a href="https://pypi.org/project/Pillow/"><img src="https://img.shields.io/badge/Pillow-F0E68C?style=flat&logo=python&logoColor=white" alt="Pillow"></a>
    <a href="https://git-scm.com/"><img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white" alt="Git"></a>
    <a href="https://github.com/"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" alt="GitHub"></a>
    <a href="https://www.markdownguide.org/"><img src="https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown&logoColor=white" alt="Markdown"></a>
  </p>

  <p>
    <a href="# 📸 Photo Organizer">Context</a> •
    <a href="## 📂 Repository Structure">Structure</a> • 
    <a href="## ⚙️ Requirements">Requirements</a> • 
    <a href="## 💻 Installation">Installation</a> • 
    <a href="## 🚀 Usage">Usage</a> • 
    <a href="## 🎬 Demonstration">Demonstration</a> • 
    <a href="## 📝 Notes">Notes</a> • 
    <a href="## 📌 Optional">Optional</a>
    <a href="## 🔧 License">License</a>
  </p>
</div>








<br>

---

# 📸 Photo Organizer

A simple Python script to organize your photos into **year/month subfolders** based on the photo's **EXIF metadata** (DateTimeOriginal) or, if not available, the file's modification date.  
Duplicates are automatically detected using MD5 hashes, and the script ensures no files are overwritten.






<br>

---

## 📂 Repository Structure

```

photo-organizer/
├── .gitignore             # Files/folders to ignore in Git
├── photo_organizer.py     # Main Python script
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies

```






<br>

---

## ⚙️ Requirements

- Python 3.8 or higher
- [Pillow](https://pypi.org/project/Pillow/) library for image processing

The only external dependency is **Pillow**, all other modules (`os`, `shutil`, `hashlib`, `pathlib`, `datetime`) are included in the Python standard library.






<br>

---

## 💻 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/photo-organizer.git
cd photo-organizer
```

2. **Create a virtual environment (recommended):**

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```






<br>

---

## 🚀 Usage

Run the script:

```bash
python photo_organizer.py
```

The script will prompt you to enter:

```
📁 Please provide the folder paths:
  ⌨️ Enter the source folder path: 
  ⌨️ Enter the destination folder path: 
```

* **Source folder**: the folder containing your photos.
* **Destination folder**: the folder where photos will be organized.
  Subfolders will be created automatically in the format: `YEAR / MM Month / photo.jpg`

**Example:**

```
✅ Moved: Wallpaper56.jpg → 2022/12 December/Wallpaper56.jpg
```

* Duplicate files are skipped automatically.
* Files without EXIF date use the file's modification date.






<br>

---

## 🎬 Demonstration

Below is a visual demonstration of the Photo Organizer in action:

<p align="center">
  <img src="assets/demostration.gif" alt="Demostration Photo Organizer" width="65%">
</p>






<br>

---

## 📝 Notes

* Supports all image formats recognized by Pillow (JPEG, PNG, etc.).
* Automatically handles duplicate file names by appending `_1`, `_2`, etc.
* Make sure **not to include quotes** when entering folder paths; the script automatically strips them if present.






<br>

---

## 📌 Optional

If you want to make the script executable directly (macOS/Linux):

```bash
chmod +x photo_organizer.py
./photo_organizer.py
```






<br>

---

## 🔧 License

This project is open-source under the MIT License. Free to use and modify!
