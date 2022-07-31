from api_google.credentials import google_creds
from api_google.google_drive import GoogleDriveService
from core.exceptions import WordNotFound

class FileService():
    def __init__(self):
        self.drive_service = GoogleDriveService()
        self.google_creds = google_creds.get_credentials()
    
    def get_files(self):
        items = self.drive_service.list_files(self.google_creds)
        return items

    def create_file(self, title, description):
        file_id = self.drive_service.create_file(title, self.google_creds)
        self.drive_service.update_file(file_id, description, self.google_creds)
        data = {
            'id': file_id,
            'titulo': title,
            'descripcion': description
        }
        return data
    
    def delete_file(self, file_id):
        delete_file = self.drive_service.delete_file(file_id, self.google_creds)
        return delete_file
    
    def get_content_file(self, file_id, word):
        doc_content = self.drive_service.get_content_in_file(file_id, self.google_creds)
        return doc_content

    def search_word(self, file_id, word):
        doc_content = self.get_content_file(file_id, word)
        text = []
        for paragraph in doc_content:
            if paragraph.get('paragraph'):
                content = paragraph.get('paragraph').get('elements')[0].get('textRun').get('content')
                list_word = content.split(' ')
                for _word in list_word:
                    if _word == '\n':
                        continue
                    __word = _word.rstrip()
                    text.append(__word.lower())
        if not word.lower() in text:
            raise WordNotFound()
        return {'message': 'La palabra SI se encuentra en el texto'}
