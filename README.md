# Overview
This simple Python code generates a html file showing geographical location of each person found in the Google Sheet document (known as the Location File below). 

After downloading the source code
# Setup your Python environment
Create a virtual venv to run your Python code, then activate it
```sh
tiger@mbp0022 x-unsw-whereabouts % python -m venv venv 
tiger@mbp0022 x-unsw-whereabouts % source venv/bin/activate
```
Install all necessary libraries
```sh
(venv) tiger@mbp0022 x-unsw-whereabouts % pip install -r requirements.txt  
```

Google Sheets File URL
Please create a local file on with the following name
google_sheets_url.txt
And put the URL of your Google Sheets in the file.

Run it
```sh
(venv) tiger@mbp0022 x-unsw-whereabouts % python gsmap.py  
```

# For the local array version map.py
no Set up required

# For Google Sheets Version gsmap.py
## Set up GCP to enable reading your public Google Doc
1. Go to the Google Cloud Console (https://console.cloud.google.com/)
2. Create a new project or select an existing project.
3. In the sidebar, click on "APIs & Services" > "Dashboard."
4. Click on "+ CREATE CREDENTIALS" and select "Service account."
5. Fill in the required information for the service account, and make sure to grant the necessary permissions (e.g., Google Sheets API access).
6. After creating the service account, click on the "Manage keys" tab, then click on "Add key" > "Create new key."
7. Choose the JSON format and click "Create." This will download the service_account.json file.
8. Place the service_account.json file in the same directory as your Python script or specify the correct path to it in the ServiceAccountCredentials.from_json_keyfile_name() function
9. Go to the following link to enable Google Sheets API
https://console.developers.google.com/apis/api/sheets.googleapis.com/overview?project=<GCP_PROJECT_ID>

NOTE: Replace <GCP_PROJECT_ID> with your Google Cloud Platform project id

## The location file
https://docs.google.com/spreadsheets/d/<GOOGLE_DOC_FILE_ID>/edit?usp=sharing

NOTE: Replace <GOOGLE_DOC_FILE_ID> with your Google Sheets' file id
