from kubernetes import client, config
import sys
import re
import os


import logging
os.remove("podlogs.log")
logging.basicConfig(format='%(asctime)s - %(message)s',filename="podlogs.log",filemode='a', level=logging.INFO)

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config() #To load our cluster configurations from  .kube/config 
try:
    pod_namespace = sys.argv[1] 
    pod_regex = sys.argv[2] 
except:
    print("+ Please enter a corresponding Namespace and part of the pods name to start ")
    sys.exit()

v1 = client.CoreV1Api()

ret = v1.list_namespaced_pod(pod_namespace)
for i in ret.items:
    #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    pod_name=i.metadata.name
    if re.match(pod_regex, pod_name):#we could have a lot of different pods we don't want to track, so we can apply a regex match to filter only the pods we want
        pod_logs = v1.read_namespaced_pod_log(pod_name,pod_namespace)
        if pod_logs != '':
            logging.info("POD_NAME: "+pod_name+ " --LOG CAPTURED: "+pod_logs)
        else:
            logging.info("POD_NAME: "+pod_name+ " -- NO LOG CAPTURED")


        
     