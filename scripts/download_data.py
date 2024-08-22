import os
import zipfile
from urllib.request import urlretrieve

# Downlaod Yellow and Green Taxi data
URL_TEMPLATES_TAXI = {
    "yellow": "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_",
    "green": "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_"
}
# CLear the month that we need  
YEAR = ['2023']
MONTH = range(2, 13)
# The dictionary of data
OUTPUT_DIRS_TAXI = {
    "yellow": '../project-1-individual-MuhanChu/data/raw/NYCTLC_data/yellow_taxi',
    "green": '../project-1-individual-MuhanChu/data/raw/NYCTLC_data/green_taxi'
}

# download the data
for color in URL_TEMPLATES_TAXI:
    for year in YEAR:
        for month in MONTH:
            month_str = str(month).zfill(2)
            url = f'{URL_TEMPLATES_TAXI[color]}{year}-{month_str}.parquet'
            output_dir = f'{OUTPUT_DIRS_TAXI[color]}/{year}'
            os.makedirs(output_dir, exist_ok=True)
            output_file = f'{output_dir}/{year}-{month_str}.parquet'
            print(f'Starting download for {color.capitalize()} Taxi {year}-{month_str}')
            urlretrieve(url, output_file)
            print(f'Finished download for {color.capitalize()} Taxi {year}-{month_str}')


# the function use to download the external data
def download_data_url(url, output_dir, filename):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)

    print('Starting download for data...')
    try:
        urlretrieve(url, file_path)
        print(f'Finished download for data, saved to {file_path}')
        return file_path
    except Exception as e:
        print(f'Failed to download the data: {e}')
        return None
    

# Download the New York weather data
URL_TEMPLATES_WEATHER = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=9E8LQXNKLTXT965BD8YPMRU9T&taskId=5180f84aaf1d486a5ecf601410bae267&zip=false'
OUTPUT_DIRS_WEATHER = '../project-1-individual-MuhanChu/data/raw/external_data'
FILENAME = 'weather_raw_data.csv'

downloaded_file = download_data_url(URL_TEMPLATES_WEATHER, OUTPUT_DIRS_WEATHER, FILENAME)


# Download the New York citybike data
URL_TEMPLATES_CITYBIKE = 'https://s3.amazonaws.com/tripdata/2023-citibike-tripdata.zip'
OUTPUT_DIRS_CITYBIKE = '../project-1-individual-MuhanChu/data/raw/external_data/cityBike_data'
FILENAME = '2023-citibike-tripdata.zip'
downloaded_file = download_data_url(URL_TEMPLATES_CITYBIKE, OUTPUT_DIRS_CITYBIKE, FILENAME)

# Download the data of taxi_zone
URL_TEMPLATES_TAXIZONE = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
OUTPUT_DIRS_TAXIZONE = "../project-1-individual-MuhanChu/data/raw/NYCTLC_data"
FILENAME = 'taxi_zone.csv'
downloaded_file = download_data_url(URL_TEMPLATES_TAXIZONE, OUTPUT_DIRS_TAXIZONE, FILENAME)

# Download the data of taxi_zone_shipfile
URL_TEMPLATES_TAXIZONE_SHIPFILE = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zones.zip"
OUTPUT_DIRS_TAXIZONE_SHIPFILE = "../project-1-individual-MuhanChu/data/raw/NYCTLC_data"
FILENAME = 'taxi_zone_shipfile.zip'
downloaded_file = download_data_url(URL_TEMPLATES_TAXIZONE_SHIPFILE, OUTPUT_DIRS_TAXIZONE_SHIPFILE, FILENAME)

# the function use to unzip the data
def unzip_file(zip_file_path, extract_dir):
    os.makedirs(extract_dir, exist_ok=True)
    print(f'Starting to unzip {zip_file_path}...')
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f'Finished unzipping, files extracted to {extract_dir}')


# unzip the data file of 2023
citybike_zip = '../project-1-individual-MuhanChu/data/raw/external_data/cityBike_data/2023-citibike-tripdata.zip'
citybike_unzip = '../project-1-individual-MuhanChu/data/raw/external_data/cityBike_data'
unzip_file(citybike_zip, citybike_unzip)


# get the csv data of 2023
citybike_file_zip = '../project-1-individual-MuhanChu/data/raw/external_data/cityBike_data/2023-citibike-tripdata'
citybike_file_unzip = '../project-1-individual-MuhanChu/data/raw/external_data/cityBike_data/citybike_raw_data'
for month in range(2, 13):
    zip_filename = f'2023{month:02d}-citibike-tripdata.zip'
    zip_file_path = os.path.join(citybike_file_zip, zip_filename)
    os.path.exists(zip_file_path)
    unzip_file(zip_file_path, citybike_file_unzip)

# unzip the data of taxi zone shipfile
taxizone_shipfile_zip = '../project-1-individual-MuhanChu/data/raw/NYCTLC_data/taxi_zone_shipfile.zip'
taxizone_shipfile_unzip = '../project-1-individual-MuhanChu/data/raw/NYCTLC_data/taxi_zone_shipfile'
unzip_file(taxizone_shipfile_zip, taxizone_shipfile_unzip)
