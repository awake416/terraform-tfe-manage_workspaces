variable aws_access_key_id {}
variable aws_secret_access_key {}
variable oauth_token_id {}
variable env {}

variable prefix {
  type = string
}

variable terraform_organization {
  default = "awake416"
}

variable region {
  default = "us-east-1"
}

variable working_dir {
  default = ""
}