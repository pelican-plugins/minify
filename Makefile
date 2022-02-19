 
check_setups:
	pyroma .

check_code:
	prospector pelican/plugins/minification/
	check-manifest --ignore Makefile,Pipfile,Pipfile.lock,pyproject.toml
