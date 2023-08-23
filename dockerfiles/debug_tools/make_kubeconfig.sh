#/bin/bash

APISERVER=https://kubernetes.default.svc
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
NAMESPACE=default
CLUSTER_NAME=my-cluster
USER_NAME=sa-user
CONTEXT_NAME=my-context
CA_FILE_PATH=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt

# Create a temporary kubeconfig file
KUBECONFIG_PATH=/tmp/kubeconfig

kubectl config --kubeconfig=${KUBECONFIG_PATH} set-cluster ${CLUSTER_NAME} --embed-certs=true --server=${APISERVER} --certificate-authority=${CA_FILE_PATH}
kubectl config --kubeconfig=${KUBECONFIG_PATH} set-credentials ${USER_NAME} --token=${TOKEN}
kubectl config --kubeconfig=${KUBECONFIG_PATH} set-context ${CONTEXT_NAME} --cluster=${CLUSTER_NAME} --namespace=${NAMESPACE} --user=${USER_NAME}
kubectl config --kubeconfig=${KUBECONFIG_PATH} use-context ${CONTEXT_NAME}
