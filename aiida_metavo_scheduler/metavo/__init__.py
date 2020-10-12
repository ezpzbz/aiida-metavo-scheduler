# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida-core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
"""
This is a modified version of PBSPro scheduler plugin and ssh transport plugin.
Both are based on the plugins shipped with AiiDA.
However, in order to use them in MetaVO (Czech Republic), there are few things needed to
be modfied.

PBSPro: MetaVO has three differnt servers associated with different parts of cluster
and therefore, it was needed to declare them in qstat command line to get
the correct job list parsing.
The PBSPro version (pbs_version = 19.0.0) configuration requires -w argument for proper parsin.
The other required change was providing the username so it would not hang in parsing
the job list.

SSH: In this case, the change is minor and related to removal of -l argument from bash commnad.

Related issues:
https://github.com/aiidateam/aiida-core/issues/2978
https://github.com/aiidateam/aiida-core/issues/2977

"""
