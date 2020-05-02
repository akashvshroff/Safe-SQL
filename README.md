# Outline
  * This project uses a Watchdog observer and SQL in order to create a "Safe" in my laptop where I can store and protect sensitive data. A detailed explanation lies below.

# Purpose
  * Not only was this project extremely engaging to code, it helped introduce me to the idea of programming a Watchdog and thereby using Python to automate a large number of my tasks. Moreover, the program helped me solidify my understanding of databases and SQL as well as key foundational ideas in Python. It also helped me understand how to visualise a project and constructively develop a plan to arrive at the visualised goal with the end product an application I use everyday.

# Description
  * There are 2 programs, add_files.py and view_safe.py with add_files.py also convertable to a .exe file using pyinstaller and then run as a background service to create a de facto daemon script.
  * The project used the two python files, one as a Watchdog (add_files) through the PatternMatchingEventHandler that continuously monitored the folder 'Safe' on my desktop and uploaded any files dropped into the directory to an SQL database, converting it into its binary data form and storing using the SQL Blob type. The module send2trash was then used to delete the file from the 'Safe' folder and maintain secrecy.
  * The second program, (view_safe) could be used to access the files in the database via a password which then revealed a simple UI to access the safe, permanently delete a record or quit the application. If a file was accessed, it was converted to its original datatype and displayed on the desktop following which the user could re-add it to the 'Safe' folder in order to secure it again.

# Notes
  * If you use this program, please ensure that you set the filepaths as per your requirements.
  * Since SQLite is used, there are certain concurrency issues and you cannot view the safe being updated real time as it causes the database to lock and an exception. Therefore, if you are viewing any files and access or delete them, close the view_safe program before re-adding the files to the 'Safe' folder.
