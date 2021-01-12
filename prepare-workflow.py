import json

with open('./workflow.json') as json_file:
    data = json.load(json_file)
    
processes = data['processes']
    
for process in processes:
    all_args = ''
    executor = process['config']['executor']
    for arg in executor['args']:
        all_args += ' ' + arg
        
    if '>' in all_args or '|' in all_args or '*' in all_args:
        source_exe = executor['executable']
        executor['executable'] = 'sh'
        new_args = []
        new_args.append('-c')
        new_args.append(source_exe + ' ' + all_args)

        executor['args'] = new_args
        
    if 'pipes' in executor:
        del(executor['pipes'])
        del(executor['pipeTo'])
        
data['processes'] = processes

with open('workflow.json', 'w') as result_json:
    data = json.dump(data, result_json, indent=4)
