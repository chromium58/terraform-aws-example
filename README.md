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

After successfully building terraform will output http endpoint url, you can visit it and see that everything built correctly.

 ### Variables example

 ```
 $ cat variables.tf
variable "account_id" {
  type = string
  default = "xxxxxxxxxxxx"
}

variable "region" {
  type = string
  default = "us-west-2"
}

variable "networks" {
  description = "AWS subnets"
  type = map
  default     = {
                  first = {
                    "cidr_block" = "10.0.1.0/24",
                    "availability_zone" = "a"
                  },
                  second = {
                    "cidr_block" = "10.0.2.0/24",
                    "availability_zone" = "b"
                  },
                  third = {
                    "cidr_block" = "10.0.3.0/24",
                    "availability_zone" = "c"
                  }
                }
}

variable "db_username" {
  description = "The username for the DB master user"
  type        = string
  default = "dbmaster"
  sensitive = true
}
variable "db_password" {
  description = "The password for the DB master user"
  type        = string
  default = "Pass1234"
  sensitive = true
}
```
