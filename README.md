# Python-Kubernetes-Assigment
Python script used to extract the logs from all the pods presented in a particular Namespace, develped using python and Kubernetes module to connect with the K8 cluster, the ouput of the pods logs will be stored in a log file to a better and understandable presentation.

## Dependencies
To run the script we will need only 1 dependency, which is a python module that will connect our python script to the K8 cluster.

```pip3 install Kubernetes ```

## Structure of the Assigment
Here it is a brief description about the purpose of each file of the assigment.

* **nginx-deployment.yaml:** Here we will have our K8 manifest, we will create 3 particular pods, each pod will have running our nginx application specified with the docker image.
* **script.py:** This is the python file will interact with our K8 configuration and structure using the [Kubernetes](https://github.com/kubernetes-client/python) module, basically with this we can execute calls to perform actions in our k8 cluster.
* **nginx-service.yaml:** This is the service file we have created to expose our cluster for our local enviroment, I have been playing around with the ```Publishing Services``` value, that's why we are specifing the NodePort instead of the default(ClusterIp)
* **podlogs.log:** Basically a log file we created at the moment we execute the script, every time the script its executed this file will be wiped out and created with all the old and new logs from all the pods

## Running the script

The manipulation of the script its really straightforward, we only will need 2 specific parameters to know before start its execution.
* **Namespace:** We will need to select the Namespace where our cluster reside, in this case I am using the "default"
* **Pod Name:** We need to specify part of the name of the pods we want to recolect logs from, inside the python file we capture this value with the regex module.

So with that we can execute our script

![image](https://user-images.githubusercontent.com/8351858/168407610-35cfcc23-214e-4f35-8afd-eee67600efd8.png)


Once our script has been sucesfully executed we will see that our podlogs.log will be generated, we can the our log file and see what its the result
```
2022-05-13 20:31:36,095 - POD_NAME: nginx-deployment-9456bbbf9-dfn78 --LOGS CAPTURED: 172.17.0.4 - - [14/May/2022:02:29:51 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.52.1" "-"
172.17.0.4 - - [14/May/2022:02:29:51 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.52.1" "-"

2022-05-13 20:31:36,098 - POD_NAME: nginx-deployment-9456bbbf9-j55wt --LOGS CAPTURED: 172.17.0.3 - - [14/May/2022:02:28:16 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.52.1" "-"
172.17.0.3 - - [14/May/2022:02:28:21 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.52.1" "-"
172.17.0.3 - - [14/May/2022:02:28:22 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.52.1" "-"
172.17.0.3 - - [14/May/2022:02:28:22 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.52.1" "-"
172.17.0.3 - - [14/May/2022:02:28:23 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.52.1" "-"

2022-05-13 20:31:36,101 - POD_NAME: nginx-deployment-9456bbbf9-xh882 -- NO LOG CAPTURED
```

In this example the we have only 3 replicas for our ngixn application, so we will have 3 different pods where we will extract logs from, and for example pod nginx-deployment-9456bbbf9-xh882 did not have any logs recorded basically because we did not generate any GET request to it.


## Some Notes

This was not my first approach, i did not know the existance of a kubernetes module (but thanks god it exist lol) my first idea was to recolect the logs using a request interaction to the cluster API, using the python request module, i think the result could be problably the same but I would definitely have spent more time on this, the exercise was pretty fun, help more to understand the cluster comunication between each node and how we can interact with each pod in a more precise way.
