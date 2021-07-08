# manage_workspaces
This is a module to setup workspaces and this maintains a standard for various secrets and common configuration like 
access and secret keys.

## Usage
This module requires setting following env variables in caller module. Ideally these should be part of pipeline
```shell
  export TFE_TOKEN=<Your Token>
  export TF_VAR_oauth_token_id=<Your Token Id> # ideally it should be a data lookup, but that did not work for me
  export TF_VAR_aws_secret_access_key=<aws_secret_access_key>
  export TF_VAR_aws_access_key_id=<aws_access_key>

```

### sample usage
````terraform
module manage_workspaces {
  source  = "app.terraform.io/awake416/manage_workspaces/tfe"
  version="v0.0.1"
  env = "dev"
  prefix = "manage_aws_organizations"
  oauth_token_id = var.oauth_token_id
  aws_access_key_id = var.aws_access_key_id
  aws_secret_access_key = var.aws_secret_access_key
}
````

### workspace exec modes
By default TFC sets execution mode of a workspace to remote and the workspace gets initialized during ``terraform init``
A script has been packaged which can be used to set the exec mode to local 
````shell
Usage - python3 set_local_exec_mode.py <organization> <workspace_name>
$ python3 set_local_exec_mode.py awake416 manage_aws_account_baseline_workspace_setup

````