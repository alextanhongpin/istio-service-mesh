# Quick Tour

Build the docker image in the folder `python-container`.

```
# Alias to reduce typing.
$ alias k=kubectl

# Deploy the container.
$ k apply -f 01-quick-tour

# View the created container.
$ k get po
```

Output:

```
NAME                                 READY   STATUS    RESTARTS   AGE
webapp-deployment-7f8fbc856f-xcz6s   1/1     Running   0          69s
```

## To access service

Port-forward the service in order to access them.

```bash
$ k port-forward webapp-deployment-7f8fbc856f-xcz6s 8000:8000
```

Output:

```
Forwarding from 127.0.0.1:8000 -> 8000
Forwarding from [::1]:8000 -> 8000
Handling connection for 8000
```

Validate the endpoint is exposed:

```bash
$ curl localhost:8000
```

Output:

```
hello world%
```

## ExternalName

Maps a Service to a DNS name.

```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: db1
  namespace: prod
spec:
  type: ExternalName
  externalName: my.database.example.com
```

## External IP

```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: externalIpAssignedService
spec:
  selector:
    app: externalIpService
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9000
  externalIPs:
    - 70.34.1.23
```


## LoadBalancer vs NodePort

When running Docker Desktop, we can use either `NodePort` or `LoadBalancer` to expose services.

Using `LoadBalancer`, we can make a call to `localhost:5000` directly (call the port on the left).
Using `NodePort`, we can make a call to `localhost:32622` (call the port on the right).

```
$ k get svc
NAME                  TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes            ClusterIP      10.96.0.1       <none>        443/TCP          3m13s
webapp-loadbalancer   LoadBalancer   10.97.95.156    localhost     5000:32089/TCP   2m52s
webapp-service        NodePort       10.103.74.128   <none>        80:32622/TCP     2m51s
```


## Reset

If there are issues running on Docker-Deskop, just go to Preferences > Kubernetes > Reset.
