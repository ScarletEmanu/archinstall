from dataclasses import dataclass
from typing import Self, TypedDict, override

from archinstall.lib.models.config import SubConfig
from archinstall.lib.translationhandler import tr


class PacmanConfigSerialization(TypedDict):
	parallel_downloads: int
	color: bool
	verbose_pkg_lists: bool
	i_love_candy: bool


@dataclass
class PacmanConfiguration(SubConfig):
	parallel_downloads: int = 5
	color: bool = True
	verbose_pkg_lists: bool = False
	i_love_candy: bool = False

	@classmethod
	def default(cls) -> Self:
		return cls()

	@override
	def json(self) -> PacmanConfigSerialization:
		return {
			'parallel_downloads': self.parallel_downloads,
			'color': self.color,
			'verbose_pkg_lists': self.verbose_pkg_lists,
			'i_love_candy': self.i_love_candy,
		}

	@override
	def summary(self) -> str | None:
		if self.color:
			return tr('Color enabled')
		return None

	def preview(self, advanced: bool = False) -> str:
		lines = []
		if advanced:
			lines.append('{}: {}'.format(tr('Parallel Downloads'), self.parallel_downloads))
			lines.append('{}: {}'.format(tr('Verbose Package Lists'), self.verbose_pkg_lists))
			lines.append('{}: {}'.format(tr('I Love Candy'), self.i_love_candy))
		lines.append('{}: {}'.format(tr('Color'), self.color))
		return '\n'.join(lines)

	@classmethod
	def parse_arg(cls, args: PacmanConfigSerialization) -> Self:
		config = cls.default()

		if 'parallel_downloads' in args:
			config.parallel_downloads = int(args['parallel_downloads'])
		if 'color' in args:
			config.color = bool(args['color'])
		if 'verbose_pkg_lists' in args:
			config.verbose_pkg_lists = bool(args['verbose_pkg_lists'])
		if 'i_love_candy' in args:
			config.i_love_candy = bool(args['i_love_candy'])

		return config
