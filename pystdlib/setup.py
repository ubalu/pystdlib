from setuptools import setup

with open("README.md", 'r') as ld:
	ldesc = ld.read()

setup(
	name='pystdlib',
	version='0.0.2',
	description='Personal convenience package.',
	py_modules=["pystdlib", ],
	package_dir={'':'src'},
	classifiers=[
		# "Programming Language :: Python :: 3",
		# "Programming Language :: Python :: 3.6",
		# "Programming Language :: Python :: 3.7",
		# "Programming Language :: Python :: 3.8",
		# "Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
		"Operating System :: OS Independent",
	],
	long_description=ldesc,
	long_description_content_type="text/markdown",
	# install_requires = [
	# 	"camelcase",
	# ],
	# extras_requires = {
	# 	"dev":[
	# 		"pytest>=6.2.5",

	# 	]
	# }
)