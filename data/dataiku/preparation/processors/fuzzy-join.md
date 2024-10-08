Fuzzy join with other dataset (memory\-based)[¶](#fuzzy-join-with-other-dataset-memory-based "Permalink to this heading")
=========================================================================================================================


This processor performs a fuzzy left join with another (small) dataset.


‘Fuzzy’ means that the join can match even if the two strings being
matched are not exactly equal, but close.


Since the join is done in memory the main limitation is the dataset size. To overcome this limit there’s a [dedicated fuzzy join recipe](../../other_recipes/fuzzy-join.html) that is a recommended way of using fuzzy join in DSS.



Example use case[¶](#example-use-case "Permalink to this heading")
------------------------------------------------------------------


You are processing a dataset of search queries. Many queries target the
name of a product, but with lots of variations and typos. You also have
a dataset with all your products, and you want to add some product
details info to each query, when we can identify which product it is
about.


Fuzzy join can help you find the correct product, even when the product
name is not exact. \# Behaviour details The processor performs a
deduplicated left join:


* If no rows in the ‘other’ dataset match, joined columns are left
empty
* If multiple rows match in the ‘other’ dataset, the ‘closest’ one in
terms of edit distanceis selected




Requirements and limitations[¶](#requirements-and-limitations "Permalink to this heading")
------------------------------------------------------------------------------------------


The ‘other’ dataset must fit in RAM. A good limit would be that it
should not be more than \~500 000 rows. If this is not the case, you
should use a recipe to join the datasets (for example, a Hive,
Python or SQL recipe).


Both the dataset being processed and the ‘other’ dataset must contain a
column containing the join key. \# Fuzziness and simplification The
processor performs a fuzzy search by computing the ‘distance’ between
two string (roughly speaking, the number of differing characters between
them). In order to increase the recall (ie, the number of times we find
a match), it is generally recommended to first ‘simplify’ the text in
both datasets, to remove some variance. This processor has built\-in
simplification options.


* Normalize text: transforms to lowercase, removes accents and performs
Unicode normalization (Café \-\> cafe)
* Clear stop words: remove so\-called ‘stop words’ (the, I, a, of, …).
This transformation is language\-specific and requires you to enter
the language of your column.
* Stem words: transforms each word into its ‘stem’, ie its grammatical
root. For example, ‘grammatical’ is transformed to ‘grammat’. This
transformation is language\-specific and requires you to enter the
language of your column.
* Sort words alphabetically: sorts all words of the text. For example,
‘the small dog’ is transformed to ‘dog small the’. This allows you to
match together strings that are written with the same words in a
different order.




Parameters[¶](#parameters "Permalink to this heading")
------------------------------------------------------


The processor needs the following parameters:


* Column containing the join key in the current dataset (which may have
been generated by a previous step)
* Name of the dataset to join with. Note that the dataset to join with
must be in the same project.
* Column containing the join key in the joined dataset.
* Columns from the joined dataset that should be copied to the local
dataset, for the matched row.
* Simplification options
* Maximum Damerau\-Levenstein distance between the simplified strings so
that they are considered a match.




Output[¶](#output "Permalink to this heading")
----------------------------------------------


The processor outputs selected columns from the joined dataset. For each
row of the current dataset, the columns will contain the data from the
matching row in the joined dataset.


If no row matched in the joined dataset, the output columns will be left
empty.