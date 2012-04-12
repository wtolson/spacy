#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       spacy.py
#
#       Copyright 2011 William Trevor Olson <wtolson@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

"""A utility for reading in plain text data files with attached dtypes to numpy."""

from StringIO import StringIO
import yaml
import numpy as np


def _parse_header(stream):
    """Extract the header from the stream."""
    magic = stream.read(3)
    if magic != '---':
        raise Exception('Header must begin with "---"')

    header = []
    while 1:
        # Read the next line from the stream
        line = stream.readline()

        # Throw an error if we reach the end of the file
        if not line:
            raise Exception('Header never ended!')

        # Check for the end of the header and break
        if line.strip() == '...':
            break

        # Append this line to the buffer
        header.append(line)

    header = '\n'.join(header)
    return yaml.safe_load(header)


def load(stream, **kwargs):
    """ Load a spacy file.

    Arguments:
        stream: Either the filename or spacy file to load data from.

    Returns:
        The array loaded from the spacy file
    """
    if isinstance(stream, basestring):
        with open(stream, 'r+') as f:
            return load(f, **kwargs)

    dtype = _parse_header(stream)
    return np.loadtxt(stream, dtype=dtype, **kwargs)


def loads(string, **kwargs):
    """ Load a spacy file from a string.

    Arguments:
        string: The string to parse as a spacy file

    Returns:
        The array loaded from the spacy string
    """
    return load(StringIO(string), **kwargs)


def dump(arr, stream, **kwargs):
    """ Dump an array to a spacy file.

    Arguments:
        arr: The 1D or 2D numpy array to dump
        stream: The file or filename to write the array to
    """
    if isinstance(stream, basestring):
        with open(stream, 'w') as f:
            return dump(arr, f, **kwargs)

    if arr.dtype.names is None:
        dtype = arr.dtype.name

    else:
        names = list(arr.dtype.names)
        formats = [arr.dtype.fields[name][0].name for name in names]
        dtype = {'names': names, 'formats': formats}

    yaml.dump(dtype, stream, explicit_start=True, explicit_end=True)
    np.savetxt(stream, arr, fmt='%s', **kwargs)


def dumps(arr, **kwargs):
    """ Dump an array to a spacy file.

    Arguments:
        arr: The 1D or 2D numpy array to dump

    Returns:
        A spacy string representation of the array.
    """
    stream = StringIO()
    dump(arr, stream, **kwargs)
    return stream.getvalue()

