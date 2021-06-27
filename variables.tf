variable "aws_access_key_id" {
  default = ""
}

variable "aws_secret_access_key" {
  default = ""
}

variable prefix {
  type = string
}

variable terraform_organization {
  default = "awake416"
}

variable region {
  default = "us-east-1"
}

variable env {}

provider tfe {}