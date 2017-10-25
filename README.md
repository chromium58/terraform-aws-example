 ### EXAMPLE. Deploy AWS RDS + AWS Lambda + AWS API Gateway + corresponding VPC, subnets and security group with Terraform
 This example creates
 * VPC
 * subnets in a,b,c availability zones
 * security group
 * aws rds mysql instance
 * lambda function from lambda directory
 * http endpoint for lambda function with AWS API Gateway
 ### Usage
 1. Clone this repo
 2. Put your variables in variables.tf
 3. Run ```terraform init```
 4. Check what terraform going to do with ```terraform plan```
 5. Build infrastructure with ```terraform apply```

After successfully building terraform will output http endpoint url, you can visit it and see that everything builded correctly.

 ### Variables example

 ```
 $ cat variables.tf
variable "account_id" {
  type = "string"
  default = "xxxxxxxxxxxx"
}

variable "region" {
  type = "string"
  default = "us-west-2"
}

variable "credentials_filepath" {
  type = "string"
  default = "/home/username/.aws/credentials"
}
```
