import os
from objaverse_dataset_manage.Module.kiuiv2_downloader import Downloader

if __name__ == "__main__":
    dataset_root_folder_path = '/home/chli/chLi/Dataset/'
    csv_file_path = '../objaverse_filter/kiuisobj_v1_merged_80K.csv'
    num_threads = os.cpu_count()

    downloader = Downloader(dataset_root_folder_path)

    downloader.downloadGlbs(csv_file_path, num_threads)