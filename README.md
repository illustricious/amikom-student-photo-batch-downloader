# amikom-student-photo-batch-downloader
This Python script automates the process of downloading student photos from Universitas Amikom Yogyakarta's server and renaming them to the corresponding student names fetched from the PDDIKTI API. The photos are organized into directories based on the year of enrollment and program of study.


## Features
- **Batch Download**: Downloads student photos based on specified NIM ranges.
- **Rename Photos**: Uses the PDDIKTI API to fetch student names and renames photos accordingly.
- **Organized Output**: Saves photos into directories by year and program (e.g., `24/Sistem Informasi/`).
- **Error Handling**: Handles missing photos, API mismatches, and invalid inputs gracefully.

## Requirements
### System Requirements
- Python 3.7+ installed on your system
- Internet connection to access the photo server and PDDIKTI API

### Python Libraries
Install the necessary Python libraries using pip:
```bash
pip install requests pddiktipy

Usage
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/amikom-student-photo-batch-downloader.git
cd amikom-student-photo-batch-downloader
Run the script:

bash
Copy code
python download.py
Follow the prompts:

Year of Enrollment: Input the year of enrollment (e.g., 20 for 2020).
Program of Study: Select the program from the displayed list.
NIM Range: Specify the starting and ending NIM for the batch download.
The script will:

Download photos from the server using NIMs.
Fetch the student names corresponding to the NIMs using the PDDIKTI API.
Rename the photos to the student names (e.g., 20.12.1550.jpg → HENDRI KURNIAWAN.jpg).
Organize photos into directories structured as {year}/{program}/.
Example
Input
Year of enrollment: 24
Program: Sistem Informasi
NIM range: 3095 to 3100
Output
markdown
Copy code
24/
└── Sistem Informasi/
    ├── FAJARUDDIN.jpg
    ├── KHAIRANI.jpg
    ├── MUHAMMAD RIDHO.jpg
    └── ZOLIARDO.jpg
Directory Structure
download.py: The main script for batch downloading and renaming photos.
requirements.txt: (Optional) A file listing the required Python libraries.
Notes
The script fetches photos from https://fotomhs.amikom.ac.id/ based on the NIM.
Student names are fetched from the PDDIKTI API, ensuring they match the exact NIM and university (UNIVERSITAS AMIKOM YOGYAKARTA).
Known Issues
Missing Photos:
If a photo doesn't exist on the server, the script logs a warning and continues.
API Mismatch:
If the PDDIKTI API returns multiple results or no exact match for a NIM, the photo will not be renamed.
Contribution
Contributions are welcome! If you find a bug or have a feature request, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Disclaimer
This script is intended for academic and personal use only
