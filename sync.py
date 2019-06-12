import todoist
import sys
import json

def getProjectId(projectName):
    for proj in api.state['projects']:
        if proj['name'] == projectName:
            print proj
            return proj['id']

def removeAllItemsFromProject(projectId):
    items = api.projects.get_data(projectId)['items']
    print items
    for i in items:
        print 'removing item'
        print i
        realItem = api.items.get_by_id(i['id'])
        print realItem
        realItem.delete()
    api.commit()

def setTemplate(projectId, file):
    print 'Importing file'
    print file
    api.templates.import_into_project(projectId, file)

print 'main'

api = todoist.TodoistAPI(sys.argv[1])
api.sync()

#load projects
with open(sys.argv[2], 'r') as file:
    jdata = json.load(file)

for p in jdata['projects']:
    projectName = p['name']
    projectTemplateFile = p['templateFile']
    currentProjectId = getProjectId(projectName)
    print currentProjectId
    removeAllItemsFromProject(currentProjectId)
    setTemplate(currentProjectId, projectTemplateFile)


