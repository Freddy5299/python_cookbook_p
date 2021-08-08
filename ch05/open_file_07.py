import gzip
import bz2

text = open('sample.txt', 'rt', encoding='ascii', errors='ignore')

with gzip.open('somefile.gz', 'wt+') as f:
    f.write(text)

with bz2.open('somefile.bz2', 'wt+') as f:
    f.write(text)

