<p align="center">
  <img src="assets/cover.png" alt="Photo Organizer Banner" style="width:100%">
</p>

<div align="center">
  <h1><span style="color: #dece63ff;">Organize your photos by year and month automatically</span></h1>

  <hr style="border:none; height:0.3px; background-color:#777; width:65%; margin:30px auto 35px auto;">

  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python"></a>
    <a href="https://pypi.org/project/Pillow/"><img src="https://img.shields.io/badge/Pillow-F0E68C?style=flat&logo=python&logoColor=white" alt="Pillow"></a>
    <a href="https://git-scm.com/"><img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white" alt="Git"></a>
    <a href="https://github.com/"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" alt="GitHub"></a>
    <a href="https://www.markdownguide.org/"><img src="https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown&logoColor=white" alt="Markdown"></a>
  </p>

  <p>
    <a href="## 📄 Description">Description</a> •
    <a href="## 📂 Repository Structure">Structure</a> • 
    <a href="## ⚙️ Requirements">Requirements</a> • 
    <a href="## 💻 Installation">Installation</a> • 
    <a href="## 🚀 Usage">Usage</a> • 
    <a href="## 🎬 Demonstration">Demonstration</a> • 
    <a href="## 📝 Notes">Notes</a> • 
    <a href="## 📌 Optional">Optional</a> •
    <a href="## 📬 Contacto">Contacto</a>
  </p>
</div>








<br>

---

## 📄 Description

A simple Python script to organize your photos into **year/month subfolders** based on the photo's **EXIF metadata** (DateTimeOriginal) or, if not available, the file's modification date.  
Duplicates are automatically detected using MD5 hashes, and the script ensures no files are overwritten.






<br>

---

## 📂 Repository Structure

```plaintext
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

You can install and run the project using a **Python virtual environment** or **Conda**.  
Choose the method you prefer.




### 🔹 Option 1: Install using Python virtual environment (recommended)

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/photo-organizer.git
cd photo-organizer
```

2. **Create a virtual environment:**

```bash
python3 -m venv venv
```

3. **Activate the environment:**

```bash
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

4. **Install dependencies:**

```bash
pip install -r requirements.txt
```




### 🔹 Option 2: Install using Conda

1. **Create a Conda environment:**

```bash
conda create -n photo-organizer python=3.12
```

2. **Activate the environment:**

```bash
conda activate photo-organizer
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

Once the environment is set up, you can run the main script:

```bash
python photo_organizer.py
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

## 📬 Contact

If you would like to get in touch with me:  

- 📧 Email: [asanca33@gmail.com](mailto:asanca33@gmail.com)  
- 📞 Phone: [+34 673 49 99 51](tel:+34673499951)  
- 📍 Location: Granada, Spain.

I will be more than happy to help you with any questions or suggestions! 😊
