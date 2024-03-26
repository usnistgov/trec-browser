# Proceedings - Confusion 1996 

#### Report on the TREC-5 Confusion Track

_Paul B. Kantor, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/confusion_track.ps.gz](http://trec.nist.gov/pubs/trec5/papers/confusion_track.ps.gz)
??? abstract "Abstract"
	
	For TREC-5, retrieval from corrupted data was studied through retrieval of single target documents from a corpus which was corrupted by producing page images, corrupting the bit maps, and applying OCR techniques to the results. In general, methods which attempted a probabilistic estimation of the original clean text fare better than methods which simply accept corrupted versions of the query text.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KantorV96.bib) "
	```
	@inproceedings{DBLP:conf/trec/KantorV96,
		author = {Paul B. Kantor and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Report on the {TREC-5} Confusion Track},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/confusion\_track.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KantorV96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SPIDER Retrieval System at TREC-5

_Jean Paul Ballerini, Marco Büchel, Ruxandra Domenig, Daniel Knaus, Bojidar Mateev, Elke Mittendorf, Peter Schäuble, Paraic Sheridan, Martin Wechsler_

- :fontawesome-solid-user-group: **Participant:** [ETH](./participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz)
- :material-file-search: **Runs:** [ETHD20N](./runs.md#ethd20n) | [ETHD20P](./runs.md#ethd20p) | [ETHD5N](./runs.md#ethd5n) | [ETHFR94](./runs.md#ethfr94) | [ETHD5P](./runs.md#ethd5p)

??? abstract "Abstract"
	
	The ETH group participated in this year's TREC in the following tracks: automatic adhoc (long and short), the manual adhoc, routing, and confusion. We also did some experiments on the chinese data which were not submitted. While for adhoc we relied mainly on methods which were well evaluated in previous TRECs, we successfully tried completely new techniques for the routing task and the confusion task: for routing we found an optimal feature selection method and included co-occurrence data into the retrieval function; for confusion we applied a robust probabilistic technique for estimating feature frequencies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalleriniBDKMMSSW96.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalleriniBDKMMSSW96,
		author = {Jean Paul Ballerini and Marco B{\"{u}}chel and Ruxandra Domenig and Daniel Knaus and Bojidar Mateev and Elke Mittendorf and Peter Sch{\"{a}}uble and Paraic Sheridan and Martin Wechsler},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SPIDER} Retrieval System at {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalleriniBDKMMSSW96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Relevance Feedback within the Relational Model for TREC-5

_David A. Grossman, Carol Lundquist, John Reichart, David O. Holmes, Abdur Chowdhury, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [GMU](./participants.md#gmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz)
- :material-file-search: **Runs:** [gmu96v01](./runs.md#gmu96v01) | [gmu96v02](./runs.md#gmu96v02) | [gmu96v11](./runs.md#gmu96v11) | [gmu96v12](./runs.md#gmu96v12) | [gmu96v21](./runs.md#gmu96v21) | [gmu96v22](./runs.md#gmu96v22)

??? abstract "Abstract"
	
	For TREC-5, we enhanced our existing prototype that implements relevance ranking using the AT&T DBC-1012 Model 4 parallel database machine to include relevance feedback. We identified SQL to compute relevance feedback and ran several experiments to identify good cutoffs for the number of documents that should be assumed to be relevant and the number of terms to add to a query. We also tried to find an optimal weighting scheme such that terms added by relevance feedback are weighted differently from those in the original query. We implemented relevance feedback in our special purpose IR prototype. Additionally, we used relevance feedback as a part of our submissions for English, Spanish, Chinese and corrupted data. Finally, we were a participant in the large data track as well. We used a text merging approach whereby a single Pentium processor was able to implement adhoc retrieval on a 4GB text collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanLRHCF96,
		author = {David A. Grossman and Carol Lundquist and John Reichart and David O. Holmes and Abdur Chowdhury and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Relevance Feedback within the Relational Model for {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ANU/ACSys TREC-5 Experiments

_David Hawking, Paul B. Thistlewaite, Peter Bailey_

- :fontawesome-solid-user-group: **Participant:** [ANU](./participants.md#anu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/anu_t5_paper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/anu_t5_paper.ps.gz)
- :material-file-search: **Runs:** [anu5con0](./runs.md#anu5con0) | [anu5con1](./runs.md#anu5con1)

??? abstract "Abstract"
	
	A number of experiments conducted within the framework of the TREC-5 conference and using the Parallel Document Retrieval Engine (PADRE) are reported. Several of the experiments involve the use of distance-based relevance scoring (spans). This scoring method is shown to be capable of very good precision-recall performance, provided that good queries can be generated. Semi-automatic methods for refining manually-generated span queries are described and evaluated in the context of the adhoc retrieval task. Span queries are also applied to processing a larger (4.5 gigabyte) collection, to retrieval over OCR-corrupted data and to a database merging task. Lightweight probe queries are shown to be an effective method for identifying promising information servers in the context of the latter task. New techniques for automatically generating more conventional weighted-term queries from short topic descriptions have also been devised and are evaluated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingTB96.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingTB96,
		author = {David Hawking and Paul B. Thistlewaite and Peter Bailey},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ANU/ACSys {TREC-5} Experiments},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/anu\_t5\_paper.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingTB96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### OCR Correction and Query Expansion for Retrieval on OCR Data –  CLARIT TREC-5 Confusion Track Report

_Xiang Tong, ChengXiang Zhai, Natasa Milic-Frayling, David A. Evans_

- :fontawesome-solid-user-group: **Participant:** [CLARITECH](./participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/CLARIT-Confusion.ps.gz](http://trec.nist.gov/pubs/trec5/papers/CLARIT-Confusion.ps.gz)
- :material-file-search: **Runs:** [CLCON20](./runs.md#clcon20) | [CLCON20F](./runs.md#clcon20f) | [CLCON5](./runs.md#clcon5) | [CLCON5F](./runs.md#clcon5f) | [CLCONBASE](./runs.md#clconbase)

??? abstract "Abstract"
	
	In CLARIT TREC-5 confusion track experiments, we explored two techniques for improving retrieval performance over corrupted data: (1) OCR word error correction to improve OCR text accuracy, and (2) query expansion by adding query term variants found in the corrupted text. The OCR word correction technique is based on statistical word bigram modeling Tong & Evans 1996]. The variants of a query term are terms similar to the query term, as measured by the edit distance [Wagner 1974]. While the official runs were based on the first approach, in our follow-up experiments we tested the second approach as well. In this report we first give a brief description of the OCR correction and query expansion techniques, and then discuss the results of our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TongZME96a.bib) "
	```
	@inproceedings{DBLP:conf/trec/TongZME96a,
		author = {Xiang Tong and ChengXiang Zhai and Natasa Milic{-}Frayling and David A. Evans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{OCR} Correction and Query Expansion for Retrieval on {OCR} Data -- {CLARIT} {TREC-5} Confusion Track Report},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/CLARIT-Confusion.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TongZME96a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

