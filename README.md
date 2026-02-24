# 🟢 LEVEL 1 – Python Foundations (Script Writing Only)
# 🎯 Goal: Become extremely comfortable writing clean Python scripts

# Tasks:

1. Write a script to:
- Take user input
- Validate input
- Handle invalid cases
2. Build:
- Password generator
- Random log generator
3. File automation:
- Read file
- Count words
- Extract unique lines
- Replace specific text
4. Build:
- CSV parser
- JSON parser
- YAML reader
5. Exception handling script:
- Simulate failures
- Log errors properly
6. Build your own logging utility module.

# 🟡 LEVEL 2 – Linux & System Automation
# 🎯 Goal: Control Linux using Python

# Scripts to Build:

1. Disk usage monitoring tool
2. Memory usage checker
3. CPU monitoring script
4. Process monitor (auto-restart service)
5. Port scanner
6. Log cleanup automation (older than X days)
7. Cron-compatible script
8. Directory watcher
9. File integrity checker (hash comparison)
10. SSH brute-force detection script

 # 🟠 LEVEL 3 – API & Network Automation
# 🎯 Goal: Automate external systems

# Build:

1. Website uptime monitor
2. REST API caller with:
- Retry logic
- Timeout handling
- Logging
3. Slack alert integration
4. Email alert system
5. API response time tracker
6. Rate limit handler
7. Multi-threaded API caller
8. SSL certificate expiry monitor
9. Load testing mini script
10. CLI-based health check tool

# 🔵 LEVEL 4 – AWS Automation (boto3)
# 🎯 Goal: Infrastructure automation

# Build Scripts For:

1. List EC2 instances
2. Start/Stop EC2 instances
3. Auto shutdown scheduler
4. Upload files to S3
5. Delete unattached EBS volumes
6. Find unused security groups
7. Fetch CloudWatch metrics
8. IAM audit script
9. Cost optimization checker
10. Auto-tag AWS resources

# 🟣 LEVEL 5 – Docker & Kubernetes Automation

# Docker

1. List running containers
2. Restart unhealthy containers
3. Remove unused images
4. Container resource monitor
5. Auto-clean dangling volumes

# Kubernetes

1. List pods in all namespaces
2. Restart CrashLoopBackOff pods
3. Scale deployment automatically
4. Fetch pod logs
5. Validate YAML before deployment
6. Namespace resource usage checker
7. Deployment status monitor
8. Auto-heal pod script

# 🔴 LEVEL 6 – CI/CD Automation

1. Trigger Jenkins job via API
2. Parse Jenkins logs
3. Auto-increment version script
4. Artifact cleanup automation
5. Git commit parser
6. Docker image validation script
7. Automated rollback script
8. Deployment status notifier
9. Pre-deployment validator
10. Build failure analyzer

# 🟤 LEVEL 7 – Monitoring & Reporting

1. Server health report generator (HTML)
2. Log analyzer with summary report
3. Custom monitoring agent
4. Alert system with thresholds
5. Multi-threaded log parser
6. Centralized log summarizer
7. Error rate analyzer
8. CPU spike detector
9. Memory leak detector
10. Daily automated health report (cron-based)

# ⚫ LEVEL 8 – Advanced DevOps Python Projects

# 🔥 Project 1 – Mini Monitoring System

Build a CLI tool that:
- Monitors CPU, memory, disk
- Sends alerts
- Logs results
- Runs continuously

# 🔥 Project 2 – Deployment Automation Tool

Build a Python CLI tool that:
- Pulls latest Git code
- Builds Docker image
- Pushes to registry
- Deploys to Kubernetes
- Verifies deployment
- Rolls back if failed

# 🔥 Project 3 – Auto-Healing System

If:
- Service crashes → restart
- Pod crashes → restart
- CPU high → scale
- Disk full → cleanup
- Send alert

# 🔥 Project 4 – Infrastructure Audit Tool

Check:
- Open security groups
- Public S3 buckets
- Unused resources
- IAM policy risks
- Generate report

# 🧠 Mandatory Engineering Standards

Every script must:

✅ Use logging module
✅ Use proper exception handling
✅ Be modular (functions)
✅ Support CLI arguments (argparse)
✅ Handle failure gracefully
✅ Return proper exit codes
✅ Follow PEP8
✅ Be production-ready

# 🛠 Required Tools

- Python 3.10+
- Virtualenv
- boto3
- requests
- docker SDK
- kubernetes client
- psutil
- paramiko
- PyYAML
