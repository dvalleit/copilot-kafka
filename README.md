## INSTALL kafka:
brew install kafka

## Info kafka
brew info kafka

## Start zookeper
brew services start zookeeper

## Start kafka
kafka-server-start /opt/homebrew/etc/kafka/server.properties

## Create venv
python -m venv kafka

## Activate venv
source kafka/bin/activate

## Start producer
python producer.py

## Start consumer
python consumer.py


## Stop Zookeeper
brew services stop zookeeper

## Conf files
/opt/homebrew/etc/kafka/
