import os
import requests

from pddiktipy.api import api
from pddiktipy.helper import helper

# Initialize API and Helper
h = helper()
a = api()

# Define program mapping
prodi_mapping = {
    '12': 'Sistem Informasi',
    '93': 'Akuntansi',
    '84': 'Arsitektur',
    '91': 'Ekonomi',
    '85': 'Geografi',
    '95': 'Hubungan Internasional',
    '96': 'Ilmu Komunikasi',
    '94': 'Ilmu Pemerintahan',
    '11': 'Informatika',
    '92': 'Kewirausahaan',
    '86': 'Perancangan Wilayah Kota',
    '83': 'Teknik Komputer',
    '82': 'Teknologi Informasi'
}

# Get user input for angkatan
angkatan = input("Masukkan tahun angkatan (misalnya 20): ").strip()

# Convert angkatan to full year (e.g., 20 -> 2020)
year = "20" + angkatan

# Program code options
print("Pilih kode prodi:")
for index, (code, name) in enumerate(prodi_mapping.items(), start=1):
    print(f"{index}. {name}")

# Get user input for selected program option
prodi_option = input("Masukkan pilihan (1/2/3/...): ").strip()

# Validate the chosen program code
try:
    selected_code = list(prodi_mapping.keys())[int(prodi_option) - 1]
    prodi = prodi_mapping[selected_code]
except (IndexError, ValueError):
    print("Pilihan tidak valid, script dihentikan.")
    exit()

# Get NIM range from user
start_nim = input("Masukkan urutan awal NIM (misalnya 1430): ").strip()
end_nim = input("Masukkan urutan akhir NIM (misalnya 1837): ").strip()

# Create directory for the selected angkatan and prodi
prodi_directory = os.path.join(angkatan, prodi)
os.makedirs(prodi_directory, exist_ok=True)

# Function to fetch data for a given NIM
def fetch_data(nim):
    try:
        # Fetch all matching results from the API
        results = a.search_mahasiswa(nim)
        print(f"API Results for {nim}: {results}")  # Debugging output

        # Normalize the NIM format by removing periods for comparison
        normalized_nim = nim.replace('.', '')
        
        # Filter results for exact NIM match and specific 'nama_pt'
        exact_result = [
            item for item in results 
            if item.get('nim', '').replace('.', '').strip() == normalized_nim and 
               item.get('nama_pt') == 'UNIVERSITAS AMIKOM YOGYAKARTA'
        ]

        if exact_result:
            return exact_result
        else:
            print(f"No exact match found for NIM: {nim} at UNIVERSITAS AMIKOM YOGYAKARTA")
            return None
    except Exception as e:
        print(f"Error fetching data for {nim}: {e}")
        return None

# Download photos and rename them
for i in range(int(start_nim), int(end_nim) + 1):
    nim = f"{angkatan}.{selected_code}.{str(i).zfill(4)}"
    photo_url = f"https://fotomhs.amikom.ac.id/{year}/{angkatan}_{selected_code}_{str(i).zfill(4)}.jpg"
    photo_filename = os.path.join(prodi_directory, f"{angkatan}_{selected_code}_{str(i).zfill(4)}.jpg")

    # Download the photo
    try:
        response = requests.get(photo_url)
        if response.status_code == 200:
            with open(photo_filename, 'wb') as photo_file:
                photo_file.write(response.content)
            print(f"Downloaded: {photo_filename}")
        else:
            print(f"Failed to download {photo_url}, status code: {response.status_code}")
            continue
    except Exception as e:
        print(f"Error downloading {photo_url}: {e}")
        continue

    # Check if the file exists before renaming
    if not os.path.exists(photo_filename):
        print(f"File not found: {photo_filename}")
        continue

    # Fetch name data using the API
    data = fetch_data(nim)
    if not data:
        print(f"No exact match found or data missing for NIM: {nim}")
        continue

    # Rename the file to the student's name
    for item in data:
        nama = item.get('nama', 'Nama Tidak Diketahui')
        new_photo_filename = os.path.join(prodi_directory, f"{nama}.jpg")
        try:
            os.rename(photo_filename, new_photo_filename)
            print(f"Renamed: {photo_filename} to {new_photo_filename}")
        except Exception as e:
            print(f"Error renaming file: {e}")

print("Proses selesai.")
