import json,sys
def logit(name,message):
    datastore = json.load(open('stalkerstuff.json'))
    if type(datastore[name]) == str:
        datastore[name] = []
    datastore[name].append(message)
    with open('stalkerstuff.json', 'w') as outfile:
        json.dump(datastore, outfile)
    return 'ok'
