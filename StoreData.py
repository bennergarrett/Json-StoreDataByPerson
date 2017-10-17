import json
ID = raw_input('What is your name?')
weight = raw_input('What is your weight?')
class storeData(Frame):
    data = {'People': [{'name': ID, 'weight':[weight]}]}

    with open('data.json') as outfile_r:
        try:
            source_data = json.load(outfile_r)
            new_name = True
            for ppl in source_data['People']:
                if ppl['name']==ID:
                    ppl['weight'].append(weight)
                    new_name = False
            if new_name:
                source_data['People'].append({'name': ID, 'weight':[weight]})
            storage = source_data
        except:
            storage = data
    with open('data.json','w') as outfile_w:
        json.dump(storage, outfile_w, sort_keys=True, indent=4)
