import os
import os.path
import ruamel.yaml
import sys
sys.path.insert(1,'./execution-frameworks/contrib/python')
import runner

load_path = '/root/atomic-red-team/atomics'

test_list = ['T1132','T1081','T1040','T1139','T1145','T1018','T1033','T1057','T1069','T1082','T1083','T1087','T1135','T1201','T1222','T1217','T1169','T1206','T1064','T1153','T1154','T1136','T1168','T1215','T1501']
technique = runner.AtomicRunner()
for j in range(300):
	for i in test_list:
		technique.execute(i,position=0)
	'''with open('test_list.txt','w') as f:
        for item in test_list:
                f.write('%s, '% item)'''
	os.remove('/root/output/pwd.txt')
print("Did",len(test_list)," tests, you can check those tests in test_list.txt")
#technique.execute('T1501', position = 0)
#tmp = '{"temp: temp"}'
#print(tmp)
