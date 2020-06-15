import os
import os.path
import ruamel.yaml
import sys
#sys.path.insert(1,'./execution-frameworks/contrib/python')
import runner
import random
import json
import argparse


load_path = '/opt/AtomicRedTeam/atomics'
yaml = ruamel.yaml.YAML()

def parseArguments():
    # Create argument parser
    parser = argparse.ArgumentParser()

    # Optional arguments
    parser.add_argument("-parameter", "--parameter", help="parameter", default=None)

    # Print version
    parser.add_argument("--version", action="version", version='%(prog)s - Version 1.0')

    # Parse arguments
    args = parser.parse_args()

    return args

def load_yaml_file(payload):
	with open(payload) as f:
		list_doc = yaml.load(f)
	return list_doc

def useful_test(atomic_tests, position):
	count = -1
	for data in atomic_tests:
		if data['name']:
			count += 1
		if count == position:
			return data
		else:
			print('out of bound')

def get_payload(list_doc,position=0,new_payload=None):
	if not new_payload:
		test = useful_test(list_doc['atomic_tests'],position)
		out = test['output']
		result = out['file']
		#print(result)
		'''for data in inputs:
			print(data)
			#print(data['output'])'''
		#print(inputs[output])
		'''if len(args) == 0:
			print('no default input arguments')
		for i in range(len(args)):
			temp = inputs[args[i]]
			payload_list.append(temp['file'])'''
	else:
		result = new_payload
	return result

def set_parameter(inputs,arguments,index):
	args = parseArguments()
	parameter = ''
	i = 0
	while i<len(inputs[index]):
		if args.parameter is not None:
			tmp = {inputs[index][i]: args.parameter}
			json_parameter = json.dumps(tmp)
			parameter = json.loads(json_parameter)
		i+=1
	return parameter
		

def random_test(index_list,test_list):
	for i in index_list:
		tmp = []
		relative = os.path.join(load_path,i)
		tmp = os.listdir(relative)
		test_list.append(random.choice(tmp))

if __name__ == '__main__':
	technique = runner.AtomicRunner()
	args = parseArguments()
	inputs = []
	payload_list = []
	test_list = []
	i=0
	flag = False
	#index_list = ['collection','defence_evasion','execution','credential_access','defence_evasion','escalation','persistence']
	#test_list = ['T1113','T1090','T1059','T1139','T1146','T1166','T1156']
	#index_list = ['collection','command&control','credential_access','defence_evasion','final']
	#random_test(index_list,test_list)
	#index_list = ['persistence']
	#test_list = ['T1501']
#for passing file name using parameter, can preload all required name of args and get payload value dynamically. (need implement).
	while flag == False and i<len(index_list):
		relative = os.path.join(load_path,index_list[i])
		test_path = os.path.join(relative,test_list[i],test_list[i]+'.yaml')
		normalize = os.path.normpath(test_path)
		list_doc = load_yaml_file(normalize)
		output = get_payload(list_doc,0)
		#parameter = set_parameter(inputs,payload_list,i)
		#print(parameter)
		#print('running test {}, this test will set specific file uid').format
		flag = technique.execute(test_list[i],position=0)
		if flag:
			print('Success on test ',test_list[i])
			flag = False
		else:
			print('Failed and skip')
		i+=1
	os.remove(os.path.join('/opt/AtomicRedTeam/execution-frameworks/contrib/python/techniques_hash.db'))
	print('Finish test')
