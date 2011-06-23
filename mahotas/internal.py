# Copyright (C) 2011, Luis Pedro Coelho <luis@luispedro.org>
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 2 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
import numpy as np

def _get_output(array, output, fname):
    '''
    output = _get_output(array, output, fname)

    Implements the mahotas output convention:
        (1) if `output` is None, return np.empty(array.shape, array.dtype)
        (2) else verify that output is of right size, shape, and contiguous

    Parameters
    ----------
    array : ndarray
    output : ndarray or None
    fname : str
        Function name. Used in error messages

    Returns
    -------
    output : ndarray
    '''
    if output is None:
        return np.empty(array.shape, array.dtype)
    if output.dtype != array.dtype:
        raise ValueError('mahotas.%s: `output` has wrong type' % fname)
    if output.shape != array.shape:
        raise ValueError('mahotas.%s: `output` has wrong shape' % fname)
    if not output.flags.contiguous:
        raise ValueError('mahotas.%s: `output` is not c-array' % fname)
    return output