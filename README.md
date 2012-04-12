# Spacy
A utility for reading in plain text data files with attached dtypes to numpy.

## Rational and Format
Spacy files are normal numpy style text data files, similar to csv files with
which you would normally import an export with the numpy utilities `loadtxt` and
`savetxt`. However for complex cases you have to know the file's dtype ahead of
time, separating the information from your data and cluttering your code.

Spacy solves this problem by including the dtype as a [yaml][yaml] header in the
data file. A spacy file must begin with `---` and the header must end with a new
line containing only `...`.

## Usage

    spacy.load(file)

> Load and return a numpy from the given spacy formated file. If `file` is a
string, it will try using it as the filename. Otherwise it is treated as a
file object.

    spacy.loads(string)

> Load and return a numpy array from the given spacy formated string.

    spacy.dump(arr, file)

> Dump a numpy array `arr` to the given file. If `file` is a string, it will use
it as a filename. Otherwise it is treated as a file object.

    spacy.dumps(arr)

> Dump and return the numpy array `arr` as a spacy formated string.


[yaml]: http://www.yaml.org/
