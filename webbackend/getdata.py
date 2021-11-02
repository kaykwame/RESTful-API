from googleapiclient.discovery import build

# from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = "datakeys.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1Wwbkw9zYuvEZVf4fakY16UvVMXtIn9zjq2PqgPXE7gQ"
service = build("sheets", "v4", credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = (
    sheet.values()
    .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="test_application_data!A1:C26")
    .execute()
)
values = result.get("values", [])
