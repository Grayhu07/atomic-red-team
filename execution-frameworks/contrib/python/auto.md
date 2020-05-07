# Install
Please install this according to the original install guid [here](https://github.com/Grayhu07/atomic-red-team/blob/master/execution-frameworks/contrib/python/README.md)

(Note: please download this to /opt/AtomicRedTeam to ensure all hard-coding path can work correctly)
# Introduction
I've created execution.py file which support a single complete attack chain that contains the following attack:
1. T1113 capture desktop screenshot, the default captured image is saved in current working directory (varies by the execution file)
2. T1090 enable traffic redirection, this test may conflict with pre-existing system configuration. (default value is 127.0.0.1:8000)
3. T1059 this test use curl to download and pipe a payload to Bash, upon successful execution, sh will download via curl and wget the specified payload
4. T1139 save credential command from bash_history to a temporary file located in ~/loot.txt. (default search key words are: -p pass ssh)
5. T1146 Clear all bash history
6. T1166 change the privilege of a single file and execute this file.
7. T1156 write the path of generated executable bash file into .bashrc which will execute the bash file every time a new terminal is opened.

I've modified T1113, T1090, T1059, T1139, T1146 such that all the command line these file needed to execute will be write to a new bash file called single.sh located in the /opt/AtomicRedTeam/single.sh
Then, T1166 will make a copy of single.sh and save in /tmp/test.sh, change the privilege of this file and execute.
After this, T1156 will add /tmp/test.sh into .bashrc.

(Note: since I use virtual machine to test these attacks, everytime restart machine will wipe all the /tmp data,
so when restart, new terminal may not execute the test.sh correctly.)

So far execute.py only support a single chain which is hard coded using a list. However, I wrote some funcitons 
leaving certain interface that can be interpret input arguments (the get_payload function). This feature have some 
bugs in it so I comment out the function call. Also, I added user input function such that user can run 
with parameter using command `python3 execution.py -parameter {user input}`

(Note: user input require certain structure, for instance, if user want to add parameter for T1166, the `{user input}`
part need the structure `'{"payload": "your-filepath"}'`
