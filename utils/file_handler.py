import os
import shutil


class FileHandler:

    @staticmethod
    def file_exists(path):
        return os.path.exists(path)

    @staticmethod
    def create_folder(folder):
        os.makedirs(folder, exist_ok=True)

    @staticmethod
    def save_uploaded_file(uploaded_file, folder):

        os.makedirs(folder, exist_ok=True)

        destination = os.path.join(folder, uploaded_file.name)

        with open(destination, "wb") as f:
            f.write(uploaded_file.getbuffer())

        return destination

    @staticmethod
    def delete_file(path):

        if os.path.exists(path):
            os.remove(path)

    @staticmethod
    def copy_file(src, dst):
        shutil.copy(src, dst)