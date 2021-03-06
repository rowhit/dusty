"""Validates specs to ensure that they're consistent with specifications

Usage:
  validate [<specs-path>]
"""

from docopt import docopt

from ..payload import Payload
from ..commands.validate import validate_specs, validate_specs_from_path

def main(argv):
    args = docopt(__doc__, argv)
    if args.get('<specs-path>'):
        payload = Payload(validate_specs_from_path, args['<specs-path>'])
        payload.run_on_daemon = False
        return payload
    else:
        return Payload(validate_specs)
