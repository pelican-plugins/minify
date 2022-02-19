 
# development & release cycle
fullrelease:
	fullrelease

check_setups:
	pyroma .

check_code:
	prospector pelican/plugins/minification/
	check-manifest

sdist:
	python setup.py sdist
