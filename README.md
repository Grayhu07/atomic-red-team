# Atomic Red Team
[![CircleCI](https://circleci.com/gh/redcanaryco/atomic-red-team.svg?style=svg)](https://circleci.com/gh/redcanaryco/atomic-red-team)

Atomic Red Team allows every security team to test their controls by executing simple
"atomic tests" that exercise the same techniques used by adversaries (all mapped to
[Mitre's ATT&CK](https://attack.mitre.org/wiki/Main_Page)).

# About what I've done:
I wrote some script that randomly choose attack scripts from each categories (collection, commmand and control, credential access, defence evasion, discovery, escalation, execution, exfiltration, lateral movement and persistence) to run and pack the result in ~/output to ~/output.tar.gz

## Structure

```bash
                                                |── collection
                                                |── command and control
                                                |── credential access
                                                |── defence evasion
                                                |── discovery
├── control.py ── control.sh ── execution.py ── |── privilege escalation
                                                |── execution
                                                |── exfiltration
                                                |── lateral movement
                                                |── persistence
                                                |── final (pack output and send)
```
Once control.py file is executed, it will give control.sh necessary privilege and add control.sh to .bashrc file. When new terminal is started, execution.py will executed and randomly choose attack script from each category listed above to form an attack chain (the order of the category is not important and I'm going to change the order into random select). Nearly all the output will be saved into ~/output directory and once it is packed, it will be deleted and leave the ~/output.tar.gz file.

## Install
Simply clone the repository to home and install dependency package listed in execution-frameworks/contrib/python/requirement.txt:

```
pip3 install -r requirement.txt
```

## Run
Navigate to ```atomic-red-team/execution-framework/contrib/python``` directory and use this command to run:

```
python3 execution.py
```
## Implement your own attack script
Please use this example and follow the structure to implement your ```.yaml``` file:
```
---
attack_technique: T0001
display_name: executing and save result

atomic_tests:
- name: executing and save result
  description: |
    executing and save result
  supported_platforms:
    - linux

  input_arguments:
    payload:
      description: hello.c payload
      type: path
      default: ~/hello.sh
  output:
    file: ~/output/script_out.txt
  executor:
    name: sh
    elevation_required: false
    command: |
      #{payload} >> ~/output/script_out.txt
    cleanup_command: |
      sudo rm ./hello
```
```attack_technique``` is used to distinct the attack methods and each attack script should have it's unique value. For now, any number from ```T0004``` to ```T0999``` is usable for implementing. ```supported_platforms``` is also needed for your attack script to work. Other parameters are recommanded but not necessary for your attack script to work. ```output``` is used to pass data flow like privilege escalation or other information, it can accept the value ```null``` if you don't want to pass anything to other attack script.

After you implement the ```.yaml``` file, please also write a ```.md``` file to explain your attack and put these two file in a folder named ```T###``` (and place this folder in ```atomic-red-team/atomics/{which category should this attack belone}```. Then it should be loaded once you run the ```execution.py``` file.

For adding new load path(directories) to ```execution.py``` file, please nevigate to ```runner.py``` in the function ```load_techniques``` line 77-78 (line number may change in the future) ```load_list``` in the same directory and add your folder name, it should be loaded once you rerun the program. It should follow the structure of other folders that store attack scripts.

## Result
Everytime a new terminal is started, automatic scripts will run and attack, results will be stored temporarily in ~/output and once it is compressed to ~/output.tar.gz , ~/output will be deleted.
