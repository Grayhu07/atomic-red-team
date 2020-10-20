import os
import os.path
import ruamel.yaml
import sys
#sys.path.insert(1,'./execution-frameworks/contrib/python')
import runner
import random
import json
import argparse


#load_path = '/root/atomic-red-team/atomics'
load_path = os.path.join("..","..","..","atomics")
home = os.getenv("HOME")
output_file_path = os.path.join(home,'output/')
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

def get_output(list_doc,position=0,new_payload=None):
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

def get_payload(list_doc,position=0):
	payload_list = []
	test = useful_test(list_doc['atomic_tests'],position)
	inputs = test['input_arguments']
	for item in inputs:
		payload_list.append(item)
	return payload_list

def get_description(list_doc,position=0):
	test = useful_test(list_doc['atomic_tests'],position)
	out = test['description']
	return out

def get_command(list_doc,position=0):
	test = useful_test(list_doc['atomic_tests'],position)
	executor = test['executor']
	command = executor['command']
	return command

def set_parameter(inputs,payload,index):
	parameter = ''
	tmp = {payload[index]: inputs}
	json_parameter = json.dumps(tmp)
	parameter = json.loads(json_parameter)
	return parameter

def load_test(test,path,position=0):
	relative = os.path.join(load_path,path)
	test_path = os.path.join(relative,test,test+'.yaml')
	normalize = os.path.normpath(test_path)
	list_doc = load_yaml_file(normalize)
	return list_doc
	

def random_test(index_list,test_list):
	for i in index_list:
		tmp = []
		relative = os.path.join(load_path,i)
		tmp = os.listdir(relative)
		test_list.append(random.choice(tmp))

def read_file():
	files = os.listdir(output_file_path)
	for i in files:
		file_path = os.path.join(output_file_path,i)
		with open(file_path,'r',encoding='utf-8',errors='ignore') as f:
			print('in reading')
			f.read()
	
			

if __name__ == '__main__':
	technique = runner.AtomicRunner()
	args = parseArguments()
	inputs = []
	#payload_list = []
	test_list = []
	download_script = ['T1074','T1027','T1064','T1153']	#tests that need privilege
	#exception_list = ['T1002','T1046','T1049','T1059','T1065','T1071','T1090']
	times=0
	flag = False
	index_list = ['escalation', 'persistence','execution','credential_access','discovery','defence_evasion','lateral_movement',\
'collection','exfiltration']
	#index_list = ['defence_evasion']
	attack_list=index_list+['Include','final']
	while times<1:
		i=0
		#random_test(index_list,test_list)
		test_list =['T1206','T1136','T1153','T1145','T1018','T1070','T1105','T1074','T1048']
		temp_list = ['T1099','T0000']
		test_list = test_list + temp_list
		print(test_list)
		with open('test_list.txt','a+') as f:
                        f.seek(0)
                        data = f.read(100)
                        if len(data) > 0:
                                f.write("\n")
                        f.write('Test list contains: ')
                        for item in test_list:
                                f.write('%s, '% item)
                        f.write('\n')
		#index_list = ['persistence']
		#test_list = ['T1501']
#for passing file name using parameter, can preload all required name of args and get payload value dynamically. (need implement).
		while flag == False and i<len(attack_list):
			relative = os.path.join(load_path,attack_list[i])
			test_path = os.path.join(relative,test_list[i],test_list[i]+'.yaml')
			normalize = os.path.normpath(test_path)
			list_doc = load_yaml_file(normalize)
			output = get_output(list_doc,0)
			#parameter = set_parameter(inputs,payload_list,i)
			flag = technique.execute(test_list[i],position=0)
			if test_list[i] in download_script:
				#Test T1166 perform privilege escalation for necessary test
				test_dict = load_test('T1166','Include',position=0)
				payload_list = get_payload(test_dict,0)
				parameter = set_parameter(output,payload_list,index=0)
				technique.execute('T1166',position=0,parameters=parameter)
			description =  get_description(list_doc,0)
			command = get_command(list_doc,0)
			if flag:
				print('Success on test ',test_list[i])
				flag = False
			else:
				print('Failed and skip')
			print(description)
			print("Command used:")
			print(command)
			with open('test_list.txt','a+') as f:
                                f.seek(0)
                                data = f.read(100)
                                if len(data) > 0:
                                        f.write("\n")
                                f.write(test_list[i])
                                f.write(": ")
                                f.write(description)
                                f.write(command)
                                f.write("\n")

			i+=1
		os.remove(os.path.join('./techniques_hash.db'))
		read_file()
		send_payload=get_payload(load_test('T0003','command&control',position=0))
		#print(send_payload)
		send_input = 'data=@'+home+'/output.tar.gz'
		#Test T0003 perfome a send action to non-operating sever
		technique.execute('T0003',position=0,parameters=set_parameter(send_input,send_payload,index=1))
		test_list=[]
		times+=1
	print('Finish test')
