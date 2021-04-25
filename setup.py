# vim:fileencoding=utf-8:noet:tabstop=4:softtabstop=4:shiftwidth=4:
from setuptools import setup

setup(
	name             = 'powerline-k8s',
	description      = 'A Powerline segment to show Kubernetes context',
	long_description = 'A Powerline segment to show Kubernetes context fast',
	long_description_content_type="text/markdown",
	version          = '0.0.1',
	keywords         = 'powerline kubernetes context',
	license          = 'MIT',
	author           = 'Francesco Della Coletta',
	author_email     = 'francesco@dellacoletta.org',
	url              = 'https://github.com/dellacf/powerline-k8s',
	packages         = ['powerline-k8s'],
	install_requires = ['powerline-status', 'kubernetes'],
	classifiers      = [
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Terminals'
	]
)
