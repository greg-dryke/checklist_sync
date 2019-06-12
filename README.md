#Overview
Pass in the API Key from profile (super easy to get to on settings page of todoist web, integrations tab).

Also stored in file locally. ex: `.\sync.py (Get-Content -raw .\apitok.secret).Trim() sync_projects.json`

Currently hard coded to one project of mine...

#TODO
- Add JSON/YAML file of projects and their files to sync
- Add code for that :) 


#Docs
* https://developer.todoist.com/sync/v8/?python#import-into-project
* https://todoist-python.readthedocs.io/en/latest/_modules/todoist/managers/projects.html?highlight=get_data
