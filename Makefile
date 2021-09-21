.PHONY: venv
venv:
	echo 'layout python3' > .envrc && \
		direnv allow

.PHONY: reqs
reqs:
	pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: docs
docs:
	cd rst && \
		sphinx-build -b html -d _build/doctrees . ../docs

.PHONY: test
test:
	python -m pytest tests

.PHONY: changes
changes:	## create CHANGES file from git logs
	git log --oneline --pretty=format:"* %ad: %s" --date=short > CHANGES

