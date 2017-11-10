import argparse
import sys

from . import _options_ext
from ._options_ext import SimpleOptions

class ParseOptions(_options_ext.ParseOptions):
    """Command line option parser."""

    def parse_args(self, args=None):
        """Parse arguments and assign them as attributes of a Namespace object.

        Args:
            args (list): List of argument strings. If not provided, the argument
                strings are taken from sys.argv.

        Returns:
            A new Namespace object populated with the parsed arguments.
        """
        self.read(args if args else sys.argv)
        opts = self.get_options()
        arg_dict = {}
        arg_dict.update(opts.bool_map)
        arg_dict.update(opts.int_map)
        arg_dict.update(opts.uint_map)
        arg_dict.update(opts.float_map)
        arg_dict.update(opts.double_map)
        arg_dict.update(opts.str_map)
        return argparse.Namespace(**arg_dict)

################################################################################

_exclude_list = ['argparse', 'sys']

__all__ = [name for name in dir()
           if name[0] != '_'
           and not name.endswith('Base')
           and not name in _exclude_list]
