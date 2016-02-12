#! /bin/bash
echo "[WARNING] Ensure that this script is run with superuser privileges!"

echo "DEPLOY: Seeing if Neo4j service is present."
$(service neo4j-service status)
neo4j_service_check=$?
echo $neo4j_service_check
case "$neo4j_service_check" in
	0)	echo "Neo4j service is running"
		;;
	1) 	echo "Neo4j doesn't exist. Instaling NOW!"
		# neo4j installation commands go here
		;;
	3)	echo "Neo4j Server exists, but is currently not running! Starting Server NOW!"
		$(sudo service neo4j-service restart)
		;;
esac
