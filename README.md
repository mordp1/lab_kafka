# lab_kafka - Vagrant + Ansible + Minikube + Kafka + Prometheus + Grafana + Kafdrop + Producer and Consumer Python

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
 ```
#### Acces the Systems in your computer: 
 
Kafdrop - To see Messages and other things for Apache Kafka:
 - http://127.0.0.1:30900

Prometheus:
 - http://127.0.0.1:30090

Grafana: 
 - http://127.0.0.1:30300

Kafka Brokers: 
 - 127.0.0.1:30094

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
 
 



