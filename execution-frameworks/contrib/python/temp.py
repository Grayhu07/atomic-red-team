import os
import os.path
import ruamel.yaml
import sys
sys.path.insert(1,'./execution-frameworks/contrib/python')
import runner

load_path = '/root/atomic-red-team/atomics'

def all_test(index_list,test_list):
	for i in index_list:
		tmp = []
		relative = os.path.join(load_path,i)
		tmp = os.listdir(relative)
		for j in tmp:
			test_list.append(j)


test_list = []
technique = runner.AtomicRunner()
index_list = ['collection','command&control','discovery','defence_evasion','execution','credential_access','escalation',\
'exfiltration','persistence']
all_test(index_list,test_list)
test_list.append('T1099')
test_list.append('T0000')
print(test_list)
for i in test_list:
	technique.execute(i,position=0)
with open('test_list.txt','a+') as f:
	f.seek(0)
	data = f.read(100)
	if len(data) > 0:
		f.write("\n")
	for item in test_list:
		f.write('%s, '% item)
#technique.execute('T1501', position = 0)
#tmp = '{"temp: temp"}'
#print(tmp)
