SHELL = /bin/bash
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

PYPI_PKG_VER_ = $$(poetry search ossr-utils | grep -E 'ossr-utils' | grep -oP '\(\K[^\)]+')
LOCAL_PKG_VER_ = $$(poetry version | grep -Po '(?<=ossr-utils )[^;]+')
PYPI_PKG_VER_ := $(shell echo $(PYPI_PKG_VER_)) # evaluate the cmd
LOCAL_PKG_VER_ := $(shell echo $(LOCAL_PKG_VER_)) # evaluate the cmd

REPO_NAME_ = ossr_utils

REPO_ROOT_ = /home/nuc/$(REPO_NAME_)
BB_ROOT_ = $(REPO_ROOT_)
REPO_ROOT_GHA_ = /home/runner/work/$(REPO_NAME_)/$(REPO_NAME_)
BB_ROOT_GHA_ = $(REPO_ROOT_GHA_)


test:
	$(CONDA_ACTIVATE) $(REPO_NAME_) && \
	cd $(BB_ROOT_) && \
	pytest

test-gha:
	$(CONDA_ACTIVATE) $(REPO_NAME_) && \
	cd $(BB_ROOT_GHA_) && \
	pytest

build:
	cd $(BB_ROOT_)
	conda env update --file environment.yml --prune
	echo 'export PYTHONPATH="${PYTHONPATH}:$(BB_ROOT_)"' >> ~/.bashrc

build-gha:
	echo 'PYTHONPATH=$(BB_ROOT_GHA_)' >> $(GITHUB_ENV)

deploy:
ifneq ($(PYPI_PKG_VER_), $(LOCAL_PKG_VER_))
	@echo Upgrading package from $(PYPI_PKG_VER_) to $(LOCAL_PKG_VER_)
	@poetry build
	@$(CONDA_ACTIVATE) $(REPO_NAME_) && \
	@poetry publish --username=$(USERNAME) --password=$(PASSWORD)
endif