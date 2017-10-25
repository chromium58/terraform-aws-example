output "apigw_url" {
  value = "${aws_api_gateway_deployment.dev.invoke_url}${aws_api_gateway_resource.MyDemoResource.path}"
}
