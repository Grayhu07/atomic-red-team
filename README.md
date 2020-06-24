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
pip install -r requirement.txt
```

## Run
Navigate to atomic-red-team directory and use this command to run:

```
python control.py
```

## Result
Everytime a new terminal is started, automatic scripts will run and attack, results will be stored temporarily in ~/output and once it is compressed to ~/output.tar.gz , ~/output will be deleted.
