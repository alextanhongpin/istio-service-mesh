## Istio

Create a namespace to host all istio-enabled applications:
```
$ k create ns istio-app
$ k label ns istio-app istio-injection=enabled
```

Validate namespace:

```
$ k describe ns istio-app
Name:         istio-app
Labels:       istio-injection=enabled
Annotations:  <none>
Status:       Active
```


## Creating applications

Deploy the application to the namespace `istio-app`:

```bash
$ k create -n istio-app -f 04-istio-virtual-service
$ k get vs
```

## View Application Dashboards

```bash
$ istioctl dashboard jaeger

# Default username and password is admin/admin.
$ istioctl dashboard kiali 
```

## Viewing destination rules

```bash
$ k get -n istio-app destinationrules
$ k get dr
```

## Working Namespace


To avoid switching namespace too often (or adding the -n tag), set the default namespace to `istio-app`:
```
$ k config set-context --current --namespace=istio-app

# To view the current namespace.
$ k config view | grep namespace
```


## Testing HTTP Lookup

NOTE: Remove other VirtualServices and just deploy the `webapp-httplookup-vs.yaml`.

The command `wget -O -` prints the result to stdout, the `-` stands for stdout.

Calling v4:
```
$ k exec pod/webapp-deployment-4.0-554f44f5d6-rrbqw -- wget -O - http://webservice/
Defaulting container name to webapp.
Use 'kubectl describe pod/webapp-deployment-4.0-554f44f5d6-rrbqw -n istio-app' to see all of the containers in this pod.
Connecting to webservice (10.103.195.242:80)
hello world, v5 2019-12-15 15:00:39.788060 v4.0 is so so-                    100% |********************************|    56  0:00:00 ETA
```


Calling v5:
```
$ k exec pod/webapp-deployment-4.0-554f44f5d6-rrbqw -- wget -O - http://webservice/ -O - http://webservice --header='x-upgrade: TRUE'
$ k exec pod/webapp-deployment-4.0-554f44f5d6-rrbqw -- wget -O - http://webservice/ -O - http://webservice/?ver=v1
Defaulting container name to webapp.
Use 'kubectl describe pod/webapp-deployment-4.0-554f44f5d6-rrbqw -n istio-app' to see all of the containers in this pod.
Connecting to webservice (10.103.195.242:80)
hello world, v5 2019-12-15 15:01:47.598353 v5.0 is great-                    100% |********************************|    56  0:00:00 ETA
Connecting to webservice (10.103.195.242:80)
-                    100% |********************************|    56  0:00:00 ETA
hello world, v5 2019-12-15 15:01:47.612960 v5.0 is great%
```
