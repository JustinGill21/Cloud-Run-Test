# Cloud-Run-Test
#### This repository is an implementation of deploying a pickled model via API

## Getting Started:
Download the repository, navigate to the directory on your local machine, and from CLI, run:
```bash
docker-compose up
```

Additionally, the `make-request.py` file can be run to test API calls. The file can be run from CLI:
```bash
python3 make-request.py
```

Note: The pickled model for this implementation was downloaded from:
https://storage.googleapis.com/security-analytics-models-public/phish-model-1649995335.cloudpickle
