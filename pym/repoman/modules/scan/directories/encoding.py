
import io

from portage import _encodings
from portage import _unicode_encode

from repoman.checks.ebuilds.checks import run_checks


class EncodingCheck(object):

	def __init__(self, **kwargs):
		self.qatracker = kwargs.get('qatracker')

	def check(self, **kwargs):
		ebuild = kwargs.get('ebuild')
		pkg = kwargs.get('pkg')
		try:
			# All ebuilds should have utf_8 encoding.
			f = io.open(
				_unicode_encode(ebuild.full_path, encoding=_encodings['fs'],
					errors='strict'),
				mode='r', encoding=_encodings['repo.content'])
			try:
				for check_name, e in run_checks(f, pkg):
					self.qatracker.add_error(
						check_name, ebuild.relative_path + ': %s' % e)
			finally:
				f.close()
		except UnicodeDecodeError:
			# A file.UTF8 failure will have already been recorded.
			pass
		return {'continue': False}

	@property
	def runInPkgs(self):
		return (False, [])

	@property
	def runInEbuilds(self):
		return (True, [self.check])
