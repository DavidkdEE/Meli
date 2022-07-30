from __future__ import print_function

import os.path
from urllib.error import HTTPError

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from core.exceptions import ConectedFailed
import os


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.metadata.readonly',
        'https://www.googleapis.com/auth/documents.readonly'
        ]

class GoogleDrive:

    def __init__(self):
        self.creds = None

        """Shows basic usage of the Drive v3 API."""

    def get_credentials(self):
        try:
            PROYECT_PATH = os.path.dirname(os.path.abspath(__file__))
            creds = None
            if os.path.exists(PROYECT_PATH+'/token.json'):
                
                creds = Credentials.from_authorized_user_file(PROYECT_PATH+'/token.json', SCOPES)

            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:

                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        PROYECT_PATH+'/credentials.json', SCOPES
                    )
                    creds = flow.run_local_server(port=1234)
                # Save the credentials for the next run
                with open(PROYECT_PATH+'/token.json', 'w') as token:
                    token.write(creds.to_json())
            return creds
        except HTTPError as err:
            raise ConectedFailed(err)
