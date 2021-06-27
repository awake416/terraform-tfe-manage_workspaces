locals {
  prefix = var.prefix
  workspace_name = join("", [
    local.prefix,
    "-",
    var.env])
  working_directory = var.working_dir == "" ? "./" : var.working_dir
  execution_mode = var.env == "dev" ? "local" : "remote"
}

resource tfe_workspace workspace {
  organization = var.terraform_organization
  name = local.workspace_name
  auto_apply = true
  terraform_version = "0.15.3"
  working_directory = local.working_directory
  execution_mode = local.execution_mode
  vcs_repo {
    identifier = join("/", [var.terraform_organization, var.prefix])
    oauth_token_id = var.oauth_token_id
  }
}

resource tfe_variable aws_access_key_id {
  key = "AWS_ACCESS_KEY_ID"
  value = var.aws_access_key_id
  category = "terraform"
  description = "aws access key id "
  workspace_id = tfe_workspace.workspace.id
  sensitive = true
}

resource tfe_variable aws_secret_access_key {
  key = "AWS_SECRET_ACCESS_KEY"
  value = var.aws_secret_access_key
  category = "terraform"
  description = "aws access key id "
  workspace_id = tfe_workspace.workspace.id
  sensitive = true
}
