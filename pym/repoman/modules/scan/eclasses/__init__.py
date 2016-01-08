# Copyright 2015-2016 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

doc = """Eclasses plug-in module for repoman.
Performs an live and ruby eclass checks on ebuilds."""
__doc__ = doc[:]


module_spec = {
	'name': 'eclasses',
	'description': doc,
	'provides':{
		'live-module': {
			'name': "live",
			'class': "LiveEclassChecks",
			'description': doc,
			'functions': ['check'],
			'func_kwargs': {
			},
		},
		'ruby-module': {
			'name': "ruby",
			'class': "RubyEclassChecks",
			'description': doc,
			'functions': ['check'],
			'func_kwargs': {
			},
		},
	}
}

