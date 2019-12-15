start:
	@# NOTE: Volume path must be absolute!
	@docker run -v /Users/alextanhongpin/Documents/devops/istio/02-introduction-to-service-mesh/service-envoy.yaml:/etc/envoy/envoy.yaml -p 9000:80 -p 8081:8081 -it envoyproxy/envoy-alpine envoy -c /etc/envoy/envoy.yaml
