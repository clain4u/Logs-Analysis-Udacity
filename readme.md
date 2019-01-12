# Logs Analysis

This is a python program that generates reports from a website log database.
The reports are:
1. Most popular three articles of all time
2. Most popular article authors of all time
3. Days with more than 1% of requests lead to errors

### Prerequisites

Virtual Box, Vagrant, Python, Postgresql

## Getting Started
To start with you need the virtual box installed.
you can download and install virtual machine from here based on your choice of operating system.

https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

Supported version of Virtual Box to install is version 5.1. 
Newer versions do not work with the current release of Vagrant

==Vagrant==

Download your copy of vagrant from here. 
https://www.vagrantup.com/downloads.html
and install it based on the your choice of operating system.

== Virtual machine [VM]==

Download your copy of virtual machine from here 
https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip

or clone it from here 
https://github.com/udacity/fullstack-nanodegree-vm

Extract the fsnd-virtual-machine.zip

From terminal change directory to "FSND-Virtual-Machine/vagrant"
Start the VM with the command
 
$ vagrant up

this will install the new linux virtual machine.
Once setup you can start vagrant with the following command

$ vagrant ssh

== Database ==

Download the database data from here 
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

and extract the file "newsdata.sql" to vagrant deirectory which is shared with your virtual machine.

== Importing data ==
Change the directory to vagrant and execute 

$ psql -d news -f newsdata.sql

to import the data, this will bring up the psql command-line program that will 
connect to "news" database and import the data by running sql queries from newsdata.sql file

== Python Program ==

Copy this program directory under vagrant folder so that its accessible the to the VM
Change the directory in terminal to program directory 

eg: cd log_analysis

vagrant/log_analysis $

### Executing the Program

Execute using the following command [without quotes] in the terminal

"python log_report.py"

The reports will displayed in pain text format soon after the program is executed.

```
Example:

$ python log_report.py

Most popular three articles of all time.

Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views


Most popular article authors of all time.

Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views


Days when more than 1% of requests lead to errors.

2016-07-17 -- 1276 error requests  -- 56137 total requests -- 2.27% error.

```

## Built With

* [Python](https://www.python.org/)
* [Postgresql] (https://www.postgresql.org/)

## Author

Clain Dsilva - First Udacity Project

## License

This project is licensed only to be used by udacity FSND mentors.

## Acknowledgments

* The Atom editor , without which the coding is a mess.
* The whole udacity batchmates and metors
* The Linux Mint - the OS I work on.
* My wife & kids - the great inspiration.
