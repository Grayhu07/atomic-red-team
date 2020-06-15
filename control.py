import os
import os.path
import sys
sys.path.insert(1,'./execution-frameworks/contrib/python')
import runner

if __name__ == '__main__':
	technique = runner.AtomicRunner()
	technique.execute('T1166',position=0)
	technique.execute('T1156',position=0)
	os.remove('./techniques_hash.db')
