import todoist
import sys

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
currentProjectId = getProjectId('backpack-home')
print currentProjectId
removeAllItemsFromProject(currentProjectId)
setTemplate(currentProjectId, 'backpack-home.csv')


