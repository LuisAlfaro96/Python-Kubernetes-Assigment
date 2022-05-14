# Python-Kubernetes-Assigment
Python script used to extract the logs from all the pods presented in a particular Namespace, develped using python and Kubernetes module to connect with the K8 cluster, the ouput of the pods logs will be stored in a log file to a better and understandable presentation.
## Structure of the Assigment
Here it is a brief description about the purpose of each file of the assigment.

* **nginx-deployment.yaml:** Here we will have our K8 manifest, we will create 3 particular pods, each pod will have running our nginx application specified with the docker image.
* **script.yaml:** This is the python file will interact with our K8 configuration and structure using the [Kubernetes] (https://github.com/kubernetes-client/python) module, basically with this we can execute calls to perform actions in our k8 cluster.
* **nginx-service.yaml:** This is the service file we have created to expose our cluster for our local enviroment, we have been palaying around with the ```Publishing Services``` value, that's why we are specifing the NodePort instead of the default(ClusterIp)
* **podlogs.log:** Basically a log file we created at the moment we execute the script, every time the script its executed this file will be wiped out and created with all the old and new logs from all the pods

## Running the script

The script its really straightforward, we only will need 2 specific parameters to know to start the recollection of the logs

## Application Output 
