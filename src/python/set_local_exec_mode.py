#!/usr/bin/env python3
import argparse
import os
import re
import sys
import requests

PAYLOAD = {"data": {"type": "workspaces", "attributes": {"operations": False}}}
HEADERS = {"Content-Type": "application/vnd.api+json"}


def load_api_credentials(rc_path="~/.terraform.d/credentials.tfrc.json"):
    with open(os.path.expanduser(rc_path)) as f:
        m = re.findall(r'"token": "([^"]+)"', f.read(), re.MULTILINE)

    if not m:
        raise RuntimeError(f"Unable to load credentials from {rc_path}")
    else:
        HEADERS["Authorization"] = f"Bearer {m[0]}"


def configure_workspace(workspace_id):
    requests.patch(
        f"https://app.terraform.io/api/v2/workspaces/{workspace_id}",
        json=PAYLOAD,
        headers=HEADERS,
    ).raise_for_status()


def configure_all_workspaces(org, workspace):
    next_page = "https://app.terraform.io/api/v2/organizations/{}/workspaces/{}".format(org, workspace)

    page = requests.get(next_page, headers=HEADERS).json()

    ws_id = page["data"]["id"]
    ws_name = page["data"]["attributes"]["name"]

    print(f"Updating {ws_name} to local exec_mode")
    try:
        configure_workspace(ws_id)
    except requests.exceptions.HTTPError as exc:
        print(f"Error updating {ws_id} {ws_name}: {exc}", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='read the workspace name')
    parser.add_argument('org', metavar='org', type=str, help='organization name, where workspace lives')
    parser.add_argument('workspace', metavar='workspace', type=str, help='name of workspace')
    args = parser.parse_args()

    load_api_credentials()
    configure_all_workspaces(args.org, args.workspace)
