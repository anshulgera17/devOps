# Terraform Learning and commands to use 

- Q1. What is Terraform ?

#### Answer

- Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions. Configuration files describe to Terraform the components needed to run a single application or your entire datacenter

- `sudo curl -O https://releases.hashicorp.com/terraform/0.11.5/terraform_0.11.5_linux_amd64.zip`
- `sudo apt-get install unzip`
- `sudo mkdir /bin/terraform`
- `sudo unzip terraform_0.11.5_linux_amd64.zip -d /usr/local/bin/`
- `terraform init`
- `vi main.tf`

## Download the latest Ghost image

```
resource "docker_image" "image_id" {
 name = "ghost:latest"
}
```

## Terraform commands to use

- `terraform init`
- `terraform plan`
- `terraform apply`
- `terraform show`
- `terraform destroy`
- `terraform taint`
- `terraform show`
- `terraform console`
- `terraform state list`
- `terraform state show`
- `terraform graph`
- `terraform apply -auto-approve`
- `terraform plan -destroy`

## variable in terraform

- while apply terraform it will ask you to use what or we can set default value as well
- terraform modules
- maps and lookups
- terraform workspaces `terraform workspace new dev`, `terraform workspace select dev`, `terraform workspace select default`
- null resource and local-exec

## Terraform Components

- Terraform does this with a few different components: Configurations: A Terraform configuration is the text file that contains the infrastructure resource definitions, When you define a configuration, you are defining one or more (typically more) resources

## Creating Modules

- A module is a container for multiple resources that are used together. Modules can be used to create lightweight abstractions, so that you can describe your infrastructure in terms of its architecture, rather than directly in terms of physical objects.
The .tf files in your working directory when you run terraform plan or terraform apply together form the rootmodule. That module may call other modules and connect them together by passing output values from one to input values of another.

- Interpolation Syntax `{docker_image.image_id.latest}`

## Start the Container

```
resource "docker_container" "container_id" {
  name  = "blog"
  image = "${docker_image.image_id.latest}"
  ports {
    internal = "2368"
    external = "80"
  }
}
```

- For destroy the infrastructure `terraform destroy`

## Tainting and updating resources

- `terraform taint docker_container.container_id`, `terraform untaint docker_container.container_id`

## Terraform console and output

- `terraform show`, `terraform console` 
- `> docker_container.container_id.name`

## Output the IP Address of the Container

```
output "IP Address" {
  value = "${docker_container.container_id.ip_address}"
}

output "container_name" {
  value = "${docker_container.container_id.name}"
}
```

## Terraform variables

```
variable "container_name" {
  description = "Name of container"
  default = "blog"
}
variable "image" {
  description = "image for container"
  default = "ghost:latest"
}
variable "int_port" {
  description = "internal port for container"
  default = "2368"
}
variable "ext_port" {
  description = "external port for container"
  default = "80"
}
```

## Download the latest Ghost Image

```
resource "docker_image" "image_id" {
  name = "${var.image}"
}
```

## Start the Container

```
resource "docker_container" "container_id" {
  name  = "${var.container_name}"
  image = "${docker_image.image_id.latest}"
  ports {
    internal = "${var.int_port}"
    external = "${var.ext_port}"
  }
}
```

- main.tf , variables.tf, outputs.tf

## Modules

- Create folders like image and containers and create files inside the folders 
- main.tf , variables.tf, outputs.tf
- `terraform init` (inside the image folder)
- `terraform plan`
- `terraform apply`
- For connecting modules need to write something in root module `main.tf`

```
module “image”
{
Source =  “./image”
Image = “${var.image}”
}
module “container”
{
Source =  “./container”
Image = “${module.image.image_out}”
Name = “${var.container_name}”
Int_port = “${var.int_port}”
ext_port = “${var.ext_port}”
}
```

- And in the outputs.tf in root folder

```
output   “IP Address”
{
value = “${module.container.ip}”
}
output “container_name”
{
value = “${module.container.container_name}”
}
```

```
resources
provider "aws"{
profile = "default"
region = "us-west-2"
}

resource "aws_s3_bucket" "tf-course"{
bucket = "buncket name---"
acl = "private"
}
```
