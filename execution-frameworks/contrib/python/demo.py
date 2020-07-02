import os
import os.path
import ruamel.yaml
import sys
#sys.path.insert(1,'./execution-frameworks/contrib/python')
import runner

technique = runner.AtomicRunner()
test_list = ['T1059','T1166','T1156','T1168','T1027']
for attack in test_list:
	technique.execute(attack, position = 0)
