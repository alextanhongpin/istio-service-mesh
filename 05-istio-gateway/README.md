# Istio Gateway

## Configure Profile

```
$ k label ns istio-app istio-injection=enabled
$ istioctl manifest apply --set profile=demo --set values.global.mtls.auto=true --set values.global.mtls.enabled=false
```

## Deployment
Deploy our application with the gateway.
```
$ k apply -f 05-istio-gateway/
```

## Gateway

Find the istio ingress gateway and the services. The gateway is accessible through `localhost:80` when using Docker Desktop.

```bash
$ k get svc istio-ingressgateway -n istio-system
```


## Curl

To call the service:
```
$ curl localhost:80 -H "Host: webservice.greetings.com"
```

Output:
```
hello world, v5 2019-12-16 13:32:52.552461 v4.0 is so so%
```

We can also `sudo vim /etc/hosts` and add `127.0.0.1 webservice.greetings.com`.

## Generating Certs

Name the Common Name as `*.greetings.com`.

```bash
$ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
$ openssl rsa -in key.pem -out public.pem

# Create.
$ k create -n istio-system secret tls istio-ingressgateway-certs --key public.pem --cert cert.pem

# Validate.
$ k describe secret istio-ingressgateway-certs -n istio-system
```

# Delete

```
$ k delete secret istio-ingressgateway-certs -n istio-system
```


## Calling secure endpoint

```
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].nodePort}')
export INGRESS_HOST=127.0.0.1
```

```
curl -v -HHost:webservice.greetings.com --resolve webservice.greetings.com:$SECURE_INGRESS_PORT:$INGRESS_HOST --cacert cert.pem https://webservice.greetings.com:$SECURE_INGRESS_PORT
```
