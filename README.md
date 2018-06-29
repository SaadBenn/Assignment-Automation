# Web-Automation
This script will automate the turning in of assignments for the courses specified on your local machine. 
The script will look at a main directory that contains all the courses with sub-directories for each course. 
```
.
├── 3170
│   └── assignment.txt
├── 3350
│   └── assignment.txt
└── 3430
    └── assignment.txt

3 directories, 3 files
```

The sub-directories will contain the assignments to submit. The program can be run each time to submit the intended assignment. This script relies on Selenium to automate the submisison process. 

# Note: 
This script is highly customizable as each website is different. Also, there are a few limitations to the way this script works. If the website is upgraded and the elements change then this script won't work and has to be tailored to the
next website layout. 
