# Proceedings - High-Precision 1997 

#### TREC 6 High-Precision Track

_Chris Buckley_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/hp_track.ps.gz](http://trec.nist.gov/pubs/trec6/papers/hp_track.ps.gz)
??? abstract "Abstract"
	
	The TREC High-Precision (HP) track compares systems on the simple 'Real World' task of having users finding a few relevant documents as quickly as possible. Five groups are participating with each happening to emphasize different aspects of the retrieval process, from visualization to structured queries to relevance feedback. With so few groups participating in this inaugural run of the the track, no decisive conclusions can be reached. However, the indications are that simple approaches work very well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Buckley97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Buckley97,
		author = {Chris Buckley},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC} 6 High-Precision Track},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {69--71},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/hp\_track.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Buckley97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc Retrieval Using Thresholds, WSTs for French Mono-lingual Retrieval,  Document-at-a-Glance for High Precision and Triphone Windows for Spoken  Documents

_Alan F. Smeaton, Fergus Kelledy, Gerard Quinn_

- :fontawesome-solid-user-group: **Participant:** [Dublin](./participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz](http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz)
- :material-file-search: **Runs:** [DCU97HP](./runs.md#dcu97hp)

??? abstract "Abstract"
	
	This paper describes work done by a team from Dublin City University as part of TREC-6. In this TREC exercise we completed series of runs in 4 categories. The first was the mainline ad hoc retrieval task in which we repeated our entry for TREC-5, without modification. This is based on applying various thresholds to processing a query including query term and posting list thresholds, in order to improve retrieval efficiency. As our previous work has shown, this can be done without any loss in retrieval effectiveness. Our second set of submitted runs were as part of the cross-lingual retrieval track where we ran French topics against French texts, effectively mono-lingual retrieval. What is novel about our approach is that it is based upon matching word shape tokens derived from character shape codes, rather than matching word stems or base forms. This technique is useful for retrieving from scanned document images rather than full texts and is something we are currently refining for English texts (and English queries). With those other experiments we have obtained surprisingly effective retrieval and this venture in TREC-6 was to see how effective WST-based retrieval could be for French. The third series of experiments we submitted were based on the high precision track in which we used a graphical representation of a ranked list of documents and the positional occurrences of search terms within those top-ranked documents, relative to each other. Our final experiments were as part of the spoken document retrieval track in which we removed the tags used for story bounds, turned transcripts and topics into a phonetic representation using a phoneme dictionary and we then retrieved story identifiers based on a triphone match between topic and fixed-width windows of triphones in the transcripts. We also applied a weighting function to triphones as they occurred in story 'windows' based on their offset within those windows.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmeatonKQ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmeatonKQ97,
		author = {Alan F. Smeaton and Fergus Kelledy and Gerard Quinn},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ad hoc Retrieval Using Thresholds, WSTs for French Mono-lingual Retrieval, Document-at-a-Glance for High Precision and Triphone Windows for Spoken Documents},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {461--475},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SmeatonKQ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage-Based Refinement (MultiText Experiements for TREC-6)

_Gordon V. Cormack, Charles L. A. Clarke, Christopher R. Palmer, Samuel S. L. To_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz)
- :material-file-search: **Runs:** [uwmt6h0](./runs.md#uwmt6h0) | [uwmt6h1](./runs.md#uwmt6h1) | [uwmt6h2](./runs.md#uwmt6h2)

??? abstract "Abstract"
	
	The MultiText system retrieves passages, rather than entire documents, that are likely to be relevant to a particular topic. For all runs, we used the reciprocal of the length of each passage as an estimate of its likely relevance and ranked accordingly. For the manual adhoc task we explored the limits of user interaction by judging some 13,000 documents based on retrieved passages. For the automatic adhoc task we used retrieved passages as a feedback source for new query terms. For the routing task we estimated probability of relevance from passage length and used this estimate to construct a compound (tiered) query which was used to rank the new data using passage length. For the Chinese track we indexed individual characters rather than segmented words or bigrams and used manually constructed queries and passage-length ranking. For the high precision track we performed judgements on passages using an interface similar to that used for the manual adhoc task. The Very Large Collection run was done on a network of four cheap computers using very simple manually constructed queries and passage-length ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackCPT97.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackCPT97,
		author = {Gordon V. Cormack and Charles L. A. Clarke and Christopher R. Palmer and Samuel S. L. To},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Passage-Based Refinement (MultiText Experiements for {TREC-6)}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {303--319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CormackCPT97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

