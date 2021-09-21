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
