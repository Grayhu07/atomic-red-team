import os
import os.path
import ruamel.yaml
import sys
#sys.path.insert(1,'./execution-frameworks/contrib/python')
import runner
import json
import argparse

load_path = '/root/atomic-red-team/atomics'
yaml = ruamel.yaml.YAML()

def useful_test(atomic_tests, position):
	count = -1
	for data in atomic_tests:
		if data['name']:
			count += 1
		if count == position:
			return data
		else:
			print('out of bound')

def get_payload(list_doc,position=0):
	test = useful_test(list_doc['atomic_tests'],position)
	out = test['description']
	return out

def load_yaml_file(payload):
	with open(payload) as f:
		list_doc = yaml.load(f)
	return list_doc

inputs = []
payload_list = []
technique = runner.AtomicRunner()
test_list = ['T1059','T1166','T1156','T1168','T1027']

for attack in test_list:
	relative = os.path.join(load_path,'demo')
	test_path = os.path.join(relative,attack,attack+'.yaml')
	normalize = os.path.normpath(test_path)
	list_doc = load_yaml_file(normalize)
	output = get_payload(list_doc,0)
	technique.execute(attack, position = 0)
	print(output)
