# HW 1
Set up the environment: 

### 1. Generate a directory on compute called PUI2016_sck408.
In my case the directory was already created

### 2. Create an environmental variable on compute account called PUI2016 that points to the directory PUI2016_sck408.
I opened
	```
	.bashrc
	```
file using the nano editor, typed

	export PUI2016="/home/cusp/sck408/PUI_sck408

and then I saved the file.
Initially I got the syntax wrong giving me a n error msg : not a valid identifier
But then I corrected the syntax to get the variable created. 

![Screenshot 2: create environmental variable ](/HW1_sck408/Create environment variable.png)

### 3. Create an alias that takes me to that directory. 

I opened
	```
	.bashrc
	```
once again to add the alias using the previously made env variable by typing

	alias pui2016='cd $PUI2016'


![Screenshot 3: bashrc profile ](/HW1_sck408/bashrc profile.png)

### 4.Type commands to confirm the new variable and alias work perferctly.

I typed this series

	pwd
	pui2016
	pwd
	
As we can see, my new alias bring me to the PUI2016_sck408 folder, thus, it works.



