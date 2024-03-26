# Proceedings - Database Merging 1995 

#### Recent Experiments with INQUERY

_James Allan, Lisa Ballesteros, James P. Callan, W. Bruce Croft, Zhihong Lu_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz](http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz)
- :material-file-search: **Runs:** [INQ205](./runs.md#inq205) | [INQ206](./runs.md#inq206) | [INQ207](./runs.md#inq207) | [INQ208](./runs.md#inq208) | [INQ209](./runs.md#inq209)

??? abstract "Abstract"
	
	Past TREC experiments by the University of Massachusetts have focused primarily on ad-hoc query creation. Substantial effort was directed towards automatically translating TREC topics into queries, using a set of simple heuristics and query expansion. Less emphasis was placed on the routing task, although results were generally good. The Spanish experiments in TREC-3 concentrated on simple indexing, sophisticated stemming, and simple methods of creating queries. The TREC-4 experiments were a departure from the past. The ad-hoc experiments involved 'fine tuning' existing approaches, and modifications to the INQUERY term weighting algorithm. However, much of the research focus in TREC-4 was on the routing, Spanish, and collection merging experiments. These tracks more closely match our broader research interests in document routing, document filtering, distributed IR, and multilingual retrieval. The University of Massachusetts' experiments were conducted with version 3.0 of the INQUERY information retrieval system. INQUERY is based on the Bayesian inference network retrieval model. It is described elsewhere [7, 5, 12, 11], so this paper focuses on relevant differences to the previously published algorithms.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanBCCL95.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanBCCL95,
		author = {James Allan and Lisa Ballesteros and James P. Callan and W. Bruce Croft and Zhihong Lu},
		editor = {Donna K. Harman},
		title = {Recent Experiments with {INQUERY}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AllanBCCL95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Siemens TREC-4 Report: Further Experiments with Database Merging

_Ellen M. Voorhees_

- :fontawesome-solid-user-group: **Participant:** [siemens](./participants.md#siemens)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/siemens.ps.gz](http://trec.nist.gov/pubs/trec4/papers/siemens.ps.gz)
- :material-file-search: **Runs:** [siems2](./runs.md#siems2) | [siems3](./runs.md#siems3)

??? abstract "Abstract"
	
	A database merging technique is a strategy for combining the results of multiple, independent searches into a single cohesive response. An isolated database merging technique selects the number of documents to be retrieved from each database without using data from the component databases at run-time. In this paper we investigate the effectiveness of two isolated database merging techniques in the context of the TREC-4 database merging task. The results show that on average a merged result contains about 1 fewer relevant document per query than a comparable single collection run when retrieving up to 100 documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees95,
		author = {Ellen M. Voorhees},
		editor = {Donna K. Harman},
		title = {Siemens {TREC-4} Report: Further Experiments with Database Merging},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/siemens.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Proximity Operators - So Near And Yet So Far

_David Hawking, Paul B. Thistlewaite_

- :fontawesome-solid-user-group: **Participant:** [hawking](./participants.md#hawking)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/anu.ps.gz](http://trec.nist.gov/pubs/trec4/papers/anu.ps.gz)
- :material-file-search: **Runs:** [padreW](./runs.md#padrew)

??? abstract "Abstract"
	
	Testing of the hypothesis that good precision-recall performance can be based entirely on proximity relationships is a focus of current TREC work at ANU. PADRE's 'Z-mode' method (based on proximity spans) of scoring relevance has been shown to produce reasonable results for hand-crafted queries in the Adhoc section. It is capable of producing equally good results in database merging and routing contexts due to its independence from collection statistics. Further work is needed to determine whether Z-mode is capable of achieving top-flight results. A new approach to automatic query generation designed to work with the shorter TREC-4 queries produced reasonable results relative to other groups but fell short of expectations based on training performance. Investigation of causes is still under way.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingT95.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingT95,
		author = {David Hawking and Paul B. Thistlewaite},
		editor = {Donna K. Harman},
		title = {Proximity Operators - So Near And Yet So Far},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/anu.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingT95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

