#! /bin/bash

# Variables
WARNING="[WARNING]";
INFO="[INFO]\t";

function hr_star() {
	printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' "*";
}

function hr_dash() {
	printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' "-";
}

function print() {
	printf $1;
	printf "\t";
	printf "${@:2}";
	printf "\n";
}

check_python_modules() {
	print $mode "Checking for python modules NOW!";
	
	pip3 --version &> /dev/null;
	pip3_check_status_code=$?;
	case "$pip3_check_status_code" in
		0)	print $tab$tab "pip3 detected!";
			;;
		1) 	print $tab$tab "pip3 not found. Installing NOW!";
			sudo apt-get install python3-pip;
			;;
	esac

	python -c "import numpy" &> /dev/null;
	numpy_check_status_code=$?;
	case "$numpy_check_status_code" in
		0)	print $tab$tab "numpy detected!";
			;;
		1) 	print $tab$tab "numpy not found. Installing NOW!";
			sudo pip3 install numpy;
			;;
	esac

	python -c "import py2neo" &> /dev/null;
	py2neo_check_status_code=$?;
	case "$py2neo_check_status_code" in
		0)	print $tab$tab "py2neo detected!";
			;;
		1) 	print $tab$tab "py2neo not found. Installing NOW!";
			sudo pip3 install py2neo;
			;;
	esac

	python -c "import hug" &> /dev/null;
	hug_check_status_code=$?;
	case "$hug_check_status_code" in
		0)	print $tab$tab "hug detected!";
			;;
		1) 	print $tab$tab "hug not found. Installing NOW!";
			sudo pip3 install hug;
			;;
	esac
}

#Check for superuser privileges and branch accordingly!
if (( $EUID != 0 )); then
	echo -e "
____ ____ _ ___  ____ ____ ____    ____ ____ ____ ___  _  _ ___  ___     ____ ___  _ 
[__  |    | |__] |__| [__  |___    | __ |__/ |__| |__] |__| |  \ |__]    |__| |__] | 
___] |___ | |__] |  | ___] |___    |__] |  \ |  | |    |  | |__/ |__]    |  | |    | 
"

	hr_star;
	print $WARNING "Script is called without superuser privileges!";
	print $INFO "Script will now attempt to enter superuser mode!";
	hr_star;
	# Execute deploy script with superuser access.
	sudo ./deploy.sh;
else
	# **************
	# *   STEP 1   *
	# **************
	hr_dash;
	# Set DEPLOY mode.
	mode="[DEPLOY][1][Neo4j]";
	tab="\t"
	# print $mode "Seeing if Neo4j service is present."
	#Check if neo4j service exists to determine whether neo4j needs to be installed or not! 
	service neo4j-service status &> /dev/null
	neo4j_service_check_status_code=$?
	case "$neo4j_service_check_status_code" in
		0)	print $mode "Neo4j service is running"
			;;
		1) 	print $mode "Neo4j doesn't exist. Installing NOW!"
			# neo4j installation commands go here
			;;
		3)	print $mode "Neo4j Server exists, but is currently not running! Starting Server NOW!";
			sudo service neo4j-service restart;
			;;
	esac
	hr_dash
	printf "\n\n"

	# **************
	# *   STEP 2   *
	# **************
	hr_dash
	# Increment DEPLOY mode.
	mode="[DEPLOY][2][python3]";
	# print $mode "Checking if python3 is installed!"
	#Check if python3 exists! 
	python3_version=`python3 --version`;
	python3_version_check_status_code=$?;
	case "$python3_version_check_status_code" in
		0)	print $mode "$python3_version detected! No need to install."
			;;
		*)	print $mode "python3 not detected. Installing NOW!"
			sudo apt-get install python3
			;;
	esac
	# Since python3 is now available, check for required modules.
	check_python_modules

	hr_dash
	printf "\n\n"	
fi
