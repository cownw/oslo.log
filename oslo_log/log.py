"""OpenStack logging handler

This module adds to logging functionality by adding the option to specify
a context object when calling the various log methods. If the context object
is not specified, default formatting is used. Additionally, an instance uuid
may be passed as part of the log message, which is intended to make it easier
for admins to find messages related to a specific instance.

It also allows settings of formatting information through conf.

"""

