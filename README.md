# poetry

## Training data

I used poetry from project Gutenberg, you can get the corpus here https://github.com/aparrish/gutenberg-poetry-corpus or by running ``wget http://static.decontextualize.com/gutenberg-poetry-v001.ndjson.gz``

Then you can run convert.py to convert the newline delimited json into a large text file.

An easier method is to just decompress ``poetry.xz`` in the repository.

## Training

first edit ``train.py`` to set the epoch count and size of the dataset.

Then just run ``train.py``. (This model is highly sensitive, if you train it on a CPU then you should use a CPU to sample it, and if you train with a GPU then use a GPU for sampling)

## Generation

just run ``gen.py``.
