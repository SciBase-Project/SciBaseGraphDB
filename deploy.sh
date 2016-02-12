#! /bin/bash
WARNING="[WARNING]"
INFO="[INFO]\t"

function hr() {
	printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' $1
}

function print() {
	printf $1;
	printf "\t"
	printf "${@:2}";
	printf "\n";
}

#Check for superuser privileges and branch accordingly!
if (( $EUID != 0 )); then
	echo -e "
____ ____ _ ___  ____ ____ ____    ____ ____ ____ ___  _  _ ___  ___     ____ ___  _ 
[__  |    | |__] |__| [__  |___    | __ |__/ |__| |__] |__| |  \ |__]    |__| |__] | 
___] |___ | |__] |  | ___] |___    |__] |  \ |  | |    |  | |__/ |__]    |  | |    | 
"

	hr "*"
	print $WARNING "Script is called without superuser privileges!";
	print $INFO "Script will now enter superuser mode!";
	hr "*"
	# Execute deploy script with superuser access.
	sudo ./deploy.sh;
else
	hr '-'
	# Set DEPLOY mode.
	mode="[DEPLOY]";
	tab="\t\t"
	print $mode "Seeing if Neo4j service is present."
	#Check if neo4j service exists to determine whether neo4j needs to be installed or not! 
	service neo4j-service status &> /dev/null
	neo4j_service_check=$?
	# echo $neo4j_service_check
	case "$neo4j_service_check" in
		0)	print $tab "Neo4j service is running"
			;;
		1) 	print $tab "Neo4j doesn't exist. Installing NOW!"
			# neo4j installation commands go here
			;;
		3)	print $mode "Neo4j Server exists, but is currently not running! Starting Server NOW!"
			$(sudo service neo4j-service restart)
			;;
	esac
fi
