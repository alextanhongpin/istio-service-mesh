## Installation

```
$ brew install istioctl
$ istioctl version
```

## Installing Demo Profile

```
$ istioctl manifest apply --set profile=demo
```


## Installation with Helm
This does not seem to work as v3 Helm is not supported, and v2 Helm seems to have some issue. Use istioctl to install instead.
```
# NOTE: Helm 3 is not supported.
$ brew search kubernetes-helm

# NOTE: This does not work
# $ brew install kubernetes-helm 2.16.1

# Manual installation
$ curl https://get.helm.sh/helm-v2.16.1-darwin-amd64.tar.gz -o helm.tar.gz
$ tar -zxvf helm.tar.gz
$ mv darwin/helm /usr/local/bin/helm
```

# Viewing dashboard

```bash
$ istioctl dashboard prometheus
```

# Experimental metrics

```bash
$ istioctl experimental metrics <service-name>
```

# Uninstalling Istio

```bash
$ istioctl manifest generate --set profile=demo | kubectl delete -f -
```
## References


https://istio.io/docs/setup/install/istioctl/
