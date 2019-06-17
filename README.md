#Overview
Pass in the API Key from profile (super easy to get to on settings page of todoist web, integrations tab).

Also stored in file locally. ex: `.\sync.py (Get-Content -raw .\apitok.secret).Trim() sync_projects.json`

#TODO
- add example for supervisor scheduling

#Docs
* https://developer.todoist.com/sync/v8/?python#import-into-project
* https://todoist-python.readthedocs.io/en/latest/_modules/todoist/managers/projects.html?highlight=get_data
