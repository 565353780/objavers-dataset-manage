import os
from time import sleep


def unzipGlbs(glbs_zip_folder_path: str, objaverse_glbs_folder_path: str) -> bool:
    if not os.path.exists(glbs_zip_folder_path):
        print("[ERROR][unzip_glbs::unzipGlbs]")
        print("\t glbs zip folder not exist!")
        print("\t glbs_zip_folder_path:", glbs_zip_folder_path)

        return False

    glbs_zip_filename_list = os.listdir(glbs_zip_folder_path)
    glbs_zip_filename_list.sort()

    for glbs_zip_filename in glbs_zip_filename_list:
        if glbs_zip_filename[:4] != "000-" or glbs_zip_filename[-4:] != ".zip":
            continue

        """
        zip_id = int(glbs_zip_filename[4:7])

        if not 140 <= zip_id <= 141:
            continue
        """

        glbs_zip_file_path = glbs_zip_folder_path + glbs_zip_filename

        print('[INFO][unzip_glbs::unzipGlbs]')
        print('\t start unzip file:', glbs_zip_filename, '...')
        command = 'unzip -u ' + glbs_zip_file_path + ' -d ' + objaverse_glbs_folder_path
        valid_command = command.replace('\\', '\\\\')

        os.system(valid_command)

    return True


if __name__ == "__main__":
    root_list = [
        '/mnt/d/chLi/Dataset/',
        os.environ['HOME'] + '/chLi/Dataset/',
    ]

    root_folder_path = None
    for root in root_list:
        if os.path.exists(root):
            root_folder_path = root
            break
    if root_folder_path is None:
        print("[ERROR][unzip_glbs::__main__]")
        print("\t dataset not found!")
        exit()

    glbs_zip_folder_path = os.environ['HOME'] + '/chLi/Downloads/D:\\/'
    objaverse_glbs_folder_path = root_folder_path + 'Objaverse_82K/glbs/'

    while True:
        unzipGlbs(glbs_zip_folder_path, objaverse_glbs_folder_path)
        sleep(60)
