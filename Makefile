.ONESHELL:

SHELL = /bin/bash
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

REPO_ROOT_ = /home/nuc/bb_utils
BB_ROOT_ = $(REPO_ROOT_)
REPO_ROOT_GHA_ = /home/runner/work/bb_utils/bb_utils
BB_ROOT_GHA_ = $(REPO_ROOT_GHA_)


test:
	$(CONDA_ACTIVATE) bb_utils
	cd $(BB_ROOT_)
	pytest

test-gha:
	$(CONDA_ACTIVATE) bb_utils
	cd $(BB_ROOT_GHA_)
	pytest

build:
	cd $(BB_ROOT_)
	conda env update --prefix ./env --file environment.yml  --prune
	echo 'export PYTHONPATH="${PYTHONPATH}:$(BB_ROOT_)"' >> ~/.bashrc

build-gha:
	echo 'PYTHONPATH=$(BB_ROOT_GHA_)' >> $(GITHUB_ENV)
