"""
Holds the File reader type object
"""
import yaml
import json


class FileConnector:
    "Class that collects method to update/get/create files"
    ALLOWED_FILE_TYPES = ['json', 'yaml', 'yml']

    def __init__(self, file_path, file_type=None):
        self.file_path = file_path
        if not file_type:
            file_type = self.file_path.split('.')[-1]

        if file_type not in FileConnector.ALLOWED_FILE_TYPES:
            raise Exception('File type {} not supported'.format(file_type))
        else:
            self.file_type = file_type

    def file_reader(self):
        if self.file_type == 'yaml' or self.file_type == 'yml':
            with open(self.file_path, 'r') as f:
                self.raw_data = yaml.load(f.read())

        elif self.file_type == 'json':
            with open(self.file_path, 'r') as f:
                self.raw_data = json.load(f)

        return self.raw_data
