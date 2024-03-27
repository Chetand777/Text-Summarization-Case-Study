# Create Components
import os
import urllib.request as request
import zipfile
from textsummarizer.logging import logger
from textsummarizer.utils.common import get_size
from textsummarizer.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
  def __init__(self, config: DataIngestionConfig):
    self.config = config

# Downlading the data file from url to artifacts location
  def download_file(self):
    if not os.path.exists(self.config.local_data_file):
      filename, headers = request.urlretrieve(
        url = self.config.source_url,
        filename = self.config.local_data_file
      )
      logger.info(f"{filename} downloaded! with follwing info: \n{headers}")
    else:
      logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")


# Extracting zip file(local data file) and unzipping it to unzip file
  def extract_zip_file(self):
    unzip_path = self.config.unzip_dir
    os.makedirs(unzip_path, exist_ok=True)
    with zipfile.ZipFile(self.config.local_data_file, 'r') as zipref:
      zipref.extractall(unzip_path)
      logger.info(f"Unzipped file to {unzip_path}")