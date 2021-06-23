# lab_kafka - Virtualbox + Vagrant + Ansible + Minikube + Kafka + Prometheus + Grafana + Kafdrop + Producer and Consumer Python

#### Minimum Requirements :
 - Vagrant 
 - Virtualbox
 - Minimum 6 GB RAM
 - 3 Cores
 
#### To execute all the system :
```
  git clone https://github.com/mordp1/lab_kafka
  cd lab_kafka
  vagrant up
  vagrant ssh
  sudo su -
  cd /vagrant/
  ansible-playbook main.yaml
  kubectl get pods --all-namespaces
 ```
#### The Time to up all the system it's approx 10 min.

#### Acces the Systems in your computer: 
 
Kafdrop - To see Messages and other things for Apache Kafka:
 - http://127.0.0.1:30900
 - Choice the topic input or output
 - So, click the View Message button ( you need to select the number offset message)

Prometheus:
 - http://127.0.0.1:30090

Grafana: 
 - http://127.0.0.1:30300
 - user: admin / pass: admin
 -  On the main screen Grafana, roll down to see the installed dashboard and click strimzi-kafka-exporter to Open Dashboard.

Kafka Brokers: 
 - 127.0.0.1:30094

Kafka Python Producer and Consumer :
- kubectl get pods
- kubectl logs -f POD_NAME ( To see output python)

#### Explain 
2 topics in Kafka called 'input' and 'output'.

Consumer and producer program in python.

Producer continuously writes messages to 'input' topic with epoch timestamp in ms.

The consumer that reads from 'input' topic, transforms input message to date string (must be in RFC 3339) and sends to topic 'output'

Prometheus + Grafana to monitoring Kafka Broker.

Kafdrop to help monitor and see message topic.

All application run in Minikube, 3 Differents Namespaces: Kafka (Kafka and zookeeper cluster/configs), monitoring (Prometheus + Grafana) and Default ( Kafdrop, Producer and Consumer).

#### Details

- Vagrant:
  1. box = mrvantage/centos7-minikube

- Helm: 
  1. https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 

- Kafka:
  1. https://strimzi.io/

- Prometheus:
  1. https://github.com/bitnami/charts/tree/master/bitnami/kube-prometheus

- Grafana:
  1. https://grafana.github.io/helm-charts

- Kafdrop:
  1. https://github.com/obsidiandynamics/kafdrop 
 
 - Producer and Consumer Kafka:
   1. https://hub.docker.com/repository/docker/mordp/producer_kfkpy 
   2. https://hub.docker.com/repository/docker/mordp/consumer_kfkpy
 
 - Ansible: 
   1. Ansible 2.10.5
