from googleapiclient.discovery import build

from core.exceptions import ConectedFailed


class GoogleDriveService():

    def __init__(self):
        pass

    def list_files(self, google_creds):
        try:
            service = build('drive', 'v3', credentials=google_creds)
            results = service.files().list(
                pageSize=20, fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])
            return items
        except Exception:
            raise ConectedFailed()

    def create_file(self, title, google_creds):
        """Create a file and return id of the file."""
        try:
            service = build('docs', 'v1', credentials=google_creds)
            doc = {'title': title}
            response = service.documents().create(body=doc).execute()
            return response.get('documentId')
        except Exception:
            raise ConectedFailed()

    def update_file(self, id_document, description, google_creds):
        """Update file."""
        try:
            service = build('docs', 'v1', credentials=google_creds)
            requests = [
                    {
                        "insertText": {
                            "text": description,
                            "location": {
                                "index": 1
                            }
                        }
                    }
                ]
            result = service.documents().batchUpdate(documentId=id_document, body={'requests': requests}).execute()
            return result
        except Exception:
            raise ConectedFailed()

    def delete_file(self, id_document, google_creds):
        """Delete file trough id."""
        try:
            service = build('drive', 'v3', credentials=google_creds)
            response = service.files().delete(fileId=id_document).execute()
            return response
        except Exception:
            raise ConectedFailed()

    def get_content_in_file(self, id_document, google_creds):
        """Get content in file."""
        try:
            service = build('docs', 'v1', credentials=google_creds)
            doc = service.documents().get(documentId=id_document).execute()
            doc_content = doc.get('body').get('content')
            return doc_content
        except Exception:
            raise ConectedFailed()
