#
# Make File for bttf
#
# Use this make file to install the project and run convenience methods. For example:
#
# 	make develop
# 	make syncdb
# 	make run_django
#

remove_egg:
	rm -rf ./src/bttf.egg-info

install_develop_dependencies:
	pip install "file://`pwd`#egg=bttf[develop]" --use-mirrors

install_test_dependencies:
	pip install "file://`pwd`#egg=bttf[test]" --use-mirrors

develop: install_develop_dependencies remove_egg

test: install_test_dependencies remove_egg

syncdb:
	django-admin.py syncdb
	django-admin.py migrate

run_django:
	django-admin.py runserver 0.0.0.0:9000
