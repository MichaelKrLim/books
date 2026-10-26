#!/usr/bin/env bash
set -Eeuo pipefail

scp -r -i ~/.ssh/michael_cloud_deployment.pem *.py templates static seeds Dockerfile lib ec2-user@18.130.232.102:~/book_store
ssh -i ~/.ssh/michael_cloud_deployment.pem ec2-user@18.130.232.102
