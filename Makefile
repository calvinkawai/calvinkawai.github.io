PHONY: clean install build start

SHELL:=/bin/zsh
VIRTUAL_ENV=.venv
PYTHON=${VIRTUAL_ENV}/bin/python

# Colors for echos
ccend = $(shell tput sgr0)
ccbold = $(shell tput bold)
ccgreen = $(shell tput setaf 2)
ccso = $(shell tput smso)

clean: ## >> remove all environment and build files
	@echo ""
	@echo "$(ccso)--> Removing virtual environment $(ccend)"
	rm -rf $(VIRTUAL_ENV)

install: venv requirements.txt ##@main >> update requirements.txt inside the virtual environment
	@echo "$(ccso)--> Updating packages $(ccend)"
	$(PYTHON) -m pip install -r requirements.txt

build:
	$(PYTHON) scripts/format.py

start:
	cd docs
	$(PYTHON) -m http.server
