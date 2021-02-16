define HELP

Usage:

make create-local-env           - Create skeleton .env file.
make base-requirements          - Install base package requirements and pip upgrade.

endef

export HELP

create-local-env:
	echo "REDDIT_CLIENT_ID" >> .env
	echo "REDDIT_CLIENT_SECRET" >> .env
	echo "REDDIT_USERNAME" >> .env
	echo "REDDIT_PASSWORD" >> .env
	echo "REDDIT_USER_AGENT" >> .env

base-requirements:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
