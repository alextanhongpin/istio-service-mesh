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
