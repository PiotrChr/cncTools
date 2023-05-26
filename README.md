# cncTools
CNC tools


Kafka

Create topic:
/home/kafka/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic Test

Produce:
echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic Test > /dev/null
rec
Consume:
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server cnc:9092 --topic StingFrames


Topics:
Sting


/usr/local/opt/kafka/bin/kafka-console-consumer --bootstrap-server 192.168.2.53:9092 --topic Sting --from-beginning

echo "Hello, World" | /usr/local/opt/kafka/bin/kafka-console-producer --broker-list 192.168.2.53:9092 --topic Sting > /dev/null


Recreate
~/kafka/bin/kafka-topics.sh --delete --topic StingFrames --bootstrap-server cnc:9092 \
&& ~/kafka/bin/kafka-topics.sh --create --bootstrap-server cnc:9092 --replication-factor 1 --partitions 1 --topic StingFrames

~/kafka/bin/kafka-configs.sh --alter --bootstrap-server cnc:9092 --entity-type topics --entity-name StingFrames --add-config retention.ms=60000

~/kafka/bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list cnc:9092 --topic StingFrames --time -2


~/kafka/bin/kafka-topics.sh --delete --topic StingFrames --bootstrap-server cnc:9092 \
&& ~/kafka/bin/kafka-topics.sh --create --bootstrap-server cnc:9092 --replication-factor 1 --partitions 1 --topic StingFrames