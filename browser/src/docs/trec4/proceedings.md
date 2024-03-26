# Proceedings 1995 

## Overview of the Fourth Text REtrieval Conference (TREC-4)

_Donna Harman_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/overview.ps.gz](http://trec.nist.gov/pubs/trec4/overview.ps.gz)
??? abstract "Abstract"
	
	The fourth Text REtrieval Conference (TREC-4) was held at the National Institute of Standards and Technology (NIST) in November 1995. The conference, co-sponsored by DARPA and NIST, is run as a workshop for participating groups to discuss their system results on the retrieval tasks done using the TIPSTER/TREC collection. As with the first three TRECs, the goals of this workshop are: To encourage research in text retrieval based on large-scale test collections To increase communication among industry, academia and government by creating an open forum for exchange of research ideas To speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems To increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current systems The number of participating systems has grown from 25 in TREC-1 to 36 in TREC-4 (see Table 1), including most of the major text retrieval software companies and most of the universities doing research in text retrieval. The diversity of the participating groups has ensured that TREC represents many different approaches to text re-trieval, while the emphasis on individual experiments evaluated within a common setting has proven to be a major strength of TREC. The research done by the participating groups in the four TREC conferences has varied, but has followed a general pattern. TREC-1 (1992) required significant system rebuilding by most groups due to the huge increase in the size of the document collection from a traditional test collection of several megabytes in size to the 2 gigabyte TIPSTER collection. The second TREC conference (TREC-2) occurred in August of 1993, less than 10 months after the first conference. The results (using new test topics) showed significant improvements over the TREC-1 results, but should be viewed as an appropriate baseline representing the 1993 state-of-the-art retrieval techniques as scaled up to a 2 gigabyte collection. TREC-3 [Harman 1994] provided an opportunity for more complex experimentation. The experiments included the development of automatic query expansion tech-niques, the use of passages or subdocuments to increase the precision of retrieval results, and the use of training information to select only the best terms for queries. Some groups explored hybrid approaches (such as the use of the Rocchio methodology in systems not using a vector space model), and others tried approaches that were radically different from their original approaches. For exam-ple, experiments in manual query expansion were done by the University of California at Berkeley and experiments in combining information from three very different retrieval techniques were done by the Swiss Federal Institute of Technology (ETH). TREC-4 represented a continuation of many of these complex experiments, and also included a set of five fo-cussed tasks, called tracks. This paper provides a review of the TREC-4 tasks, a very brief description of the test collection being used, and an overview of the results. The papers from the individual groups should be referred to for more details on specific system approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Harman95.bib)"
	```
	@inproceedings{DBLP:conf/trec/Harman95,
		author = {Donna Harman},
		editor = {Donna K. Harman},
		title = {Overview of the Fourth Text REtrieval Conference {(TREC-4)}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/overview.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Harman95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Adhoc 

#### The Troubles with Using a Logical Model of IR on a Large Collection  of Documents

_Fabio Crestani, Ian Ruthven, Mark Sanderson, C. J. van Rijsbergen_

- :fontawesome-solid-user-group: **Participant:** [glasgow](./adhoc/participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/glasgow.ps.gz](http://trec.nist.gov/pubs/trec4/papers/glasgow.ps.gz)
- :material-file-search: **Runs:** [glair1](./adhoc/runs.md#glair1)

??? abstract "Abstract"
	
	The evaluation of an implication by Imaging is a logical technique developed in the framework of Conditional Logics. In 1993 a logical model of IR called 'Retrieval by Logical Imaging' was proposed by some of the authors of this paper and tested using some classical IR test collections. In this paper we report on the challenges posed by trying to apply such a model to a large test collection of the size of TREC-B. The problems we found and the way we put together ideas and efforts to solve them are indicative of the troubles one might find in trying to implement and experiment with a 'complex' logical model of IR. We believe our efforts could set an example for other researchers working on logical models of IR to try to implement their models in such a way that they can cope with the size of real life collections, though preserving the formal 'beauty' of their logical models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CrestaniRSR95.bib) "
	```
	@inproceedings{DBLP:conf/trec/CrestaniRSR95,
		author = {Fabio Crestani and Ian Ruthven and Mark Sanderson and C. J. van Rijsbergen},
		editor = {Donna K. Harman},
		title = {The Troubles with Using a Logical Model of {IR} on a Large Collection of Documents},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/glasgow.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CrestaniRSR95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Shortest Substring Ranking (MultiText Experiments for TREC-4)

_Charles L. A. Clarke, Gordon V. Cormack, Forbes J. Burkowski_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo](./adhoc/participants.md#uwaterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/uwaterloo.ps.gz](http://trec.nist.gov/pubs/trec4/papers/uwaterloo.ps.gz)
- :material-file-search: **Runs:** [uwgcl1](./adhoc/runs.md#uwgcl1)

??? abstract "Abstract"
	
	To address the TREC-4 topics, we used a precise query language that yields and combines arbitrary intervals of text rather than pre-defined units like words and documents. Each solution was scored in inverse proportion to the length of the shortest interval containing it. Each document was scored by the sum of the scores of solutions within it. Whenever the above strategy yielded less than 1000 documents, documents satisfying successively weaker queries were added with lower rank. Our results for the ad-hoc topics compare favourably with the median average precision for all groups.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCB95.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCB95,
		author = {Charles L. A. Clarke and Gordon V. Cormack and Forbes J. Burkowski},
		editor = {Donna K. Harman},
		title = {Shortest Substring Ranking (MultiText Experiments for {TREC-4)}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/uwaterloo.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCB95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recent Experiments with INQUERY

_James Allan, Lisa Ballesteros, James P. Callan, W. Bruce Croft, Zhihong Lu_

- :fontawesome-solid-user-group: **Participant:** [umass](./adhoc/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz](http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz)
- :material-file-search: **Runs:** [INQ201](./adhoc/runs.md#inq201) | [INQ202](./adhoc/runs.md#inq202)

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

#### New Retrieval Approaches Using SMART: TREC 4

_Chris Buckley, Amit Singhal, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [cornell](./adhoc/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz)
- :material-file-search: **Runs:** [CrnlAE](./adhoc/runs.md#crnlae) | [CrnlAL](./adhoc/runs.md#crnlal)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 4, performing runs in the routing, ad-hoc, confused text, interactive, and foreign language environments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleySM95.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleySM95,
		author = {Chris Buckley and Amit Singhal and Mandar Mitra},
		editor = {Donna K. Harman},
		title = {New Retrieval Approaches Using {SMART:} {TREC} 4},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/Cornell\_trec4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleySM95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Similarity Measures for Short Queries

_Ross Wilkinson, Justin Zobel, Ron Sacks-Davis_

- :fontawesome-solid-user-group: **Participant:** [citri](./adhoc/participants.md#citri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/citri.ps.gz](http://trec.nist.gov/pubs/trec4/papers/citri.ps.gz)
- :material-file-search: **Runs:** [citri1](./adhoc/runs.md#citri1) | [citri2](./adhoc/runs.md#citri2)

??? abstract "Abstract"
	
	Ad-hoc queries are usually short, of perhaps two to ten terms. However, in previous rounds of TREC we have concentrated on obtaining optimal performance for the long TREC topics. In this paper we investigate the behaviour of similarity measures on short queries, and show experimentally that two successful measures which give similar, good performance on long TREC topics do not work well for short queries. We explore methods for achieving greater effectiveness for short queries, and conclude that a successful approach is to combine these similarity measures with other evidence. We also briefly describe our experiments with the Spanish data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WilkinsonZS95.bib) "
	```
	@inproceedings{DBLP:conf/trec/WilkinsonZS95,
		author = {Ross Wilkinson and Justin Zobel and Ron Sacks{-}Davis},
		editor = {Donna K. Harman},
		title = {Similarity Measures for Short Queries},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/citri.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WilkinsonZS95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Siemens TREC-4 Report: Further Experiments with Database Merging

_Ellen M. Voorhees_

- :fontawesome-solid-user-group: **Participant:** [siemens](./adhoc/participants.md#siemens)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/siemens.ps.gz](http://trec.nist.gov/pubs/trec4/papers/siemens.ps.gz)
- :material-file-search: **Runs:** [siems1](./adhoc/runs.md#siems1)

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

#### TREC-4 Experiments using DRIFT

_Charles L. Viles, James C. French_

- :fontawesome-solid-user-group: **Participant:** [uva](./adhoc/participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/uva.ps.gz](http://trec.nist.gov/pubs/trec4/papers/uva.ps.gz)
- :material-file-search: **Runs:** [drift1](./adhoc/runs.md#drift1) | [drift2](./adhoc/runs.md#drift2)

??? abstract "Abstract"
	
	DRIFT is a prototype, vector space based, information retrieval system in development at the University of Virginia. The system is designed to do experiments in distributed, dynamic information retrieval. We describe our first experiments using DRIFT on larger test collections, specifically the Category B subset of the TREC corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VilesF95.bib) "
	```
	@inproceedings{DBLP:conf/trec/VilesF95,
		author = {Charles L. Viles and James C. French},
		editor = {Donna K. Harman},
		title = {{TREC-4} Experiments using {DRIFT}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/uva.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VilesF95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Natural Language Information Retrieval: TREC-4 Report

_Tomek Strzalkowski, Jose Perez Carballo_

- :fontawesome-solid-user-group: **Participant:** [nyuge](./adhoc/participants.md#nyuge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/nyuge.ps.gz](http://trec.nist.gov/pubs/trec4/papers/nyuge.ps.gz)
- :material-file-search: **Runs:** [nyuge3](./adhoc/runs.md#nyuge3) | [nyuge4](./adhoc/runs.md#nyuge4)

??? abstract "Abstract"
	
	In this paper we report on the joint GE/NYU natural language information retrieval project as related to the 4th Text Retrieval Conference (TREC-4). The main thrust of this project is to use natural language processing techniques to enhance the effectiveness of full-text document retrieval. During the course of the four TREC conferences, we have built a prototype IR system designed around a statistical full-text indexing and search backbone provided by the NIST's Prise engine. The original Prise has been modified to allow handling of multi-word phrases, differential term weighting schemes, automatic query expansion, index partitioning and rank merging, as well as dealing with complex documents. Natural language processing is used to (1) preprocess the documents in order to extract content-carrying terms, (2) discover inter-term dependencies and build a conceptual hierarchy specific to the database domain, and (3) process user's natural language requests into effective search queries. The overall architecture of the system is essentially the same as in TREC-3, as our efforts this year were directed at optimizing the performance of all components. A notable exception is the new massive query expansion module used in routing experiments, which replaces a prototype extension used in the TREC-3 system. On the other hand, it has to be noted that the character and the level of difficulty of TREC queries has changed quite significantly since the last year evaluation. TREC-4 new ad-hoc queries are far shorter, less focused, and they have a flavor of information requests (What is the prognosis of ...) rather than search directives typical for earlier TRECs (The relevant document will contain ...). This makes building of good search queries a more sensitive task than before. We thus decided to introduce only minimum number of changes to our indexing and search processes, and even roll back some of the TREC-3 extensions which dealt with longer and somewhat redundant queries (e.g., locality matching? ). Overall, our system performed quite well as our position with respect to the best systems improved steadily since the beginning of TREC. It should be noted that the most significant gain in performance seems to occur in precision near the top of the ranking, at 5, 10, 15 and 20 documents. Indeed, our unofficial manual runs performed after TREC-4 conference show superior results in these categories, topping by a large margin the best manual scores by any system in the official evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrzalkowskiC95.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrzalkowskiC95,
		author = {Tomek Strzalkowski and Jose Perez Carballo},
		editor = {Donna K. Harman},
		title = {Natural Language Information Retrieval: {TREC-4} Report},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/nyuge.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StrzalkowskiC95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-4 Experiments at Dublin City University: Thresholding Posting  Lists, Query Expansion with WordNet and POS Tagging of Spanish

_Alan F. Smeaton, Fergus Kelledy, Ruairi O'Donnell_

- :fontawesome-solid-user-group: **Participant:** [dublin](./adhoc/participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/dublin.ps.gz](http://trec.nist.gov/pubs/trec4/papers/dublin.ps.gz)
- :material-file-search: **Runs:** [DCU951](./adhoc/runs.md#dcu951) | [DCU952](./adhoc/runs.md#dcu952)

??? abstract "Abstract"
	
	In this paper we describe work done as part of the TREC-4 benchmarking exercise by a team from Dublin City University. In TREC-4 we had 3 activities as follows: In work on improving the efficiency of standard SMART-like query processing we have applied various thresholding processes to the postings list of an inverted file and we have limited the number of document score accumulators available during query processing. The first run we submitted for evaluation in TREC-4 (DCU951) used our best set of thresholding and accumulator set parameters. The second run we submitted is based upon a query expansion using terms from WordNet. Essentially, for each original query term we determine its level of specificity or abstraction; for broad terms we add more specific terms, for specific original terms we add broader ones; for ones in-between we add both broader and narrower terms. When the query is expanded we then delete all the original query terms in order to add to the judged pool, documents that our expansion would find that would not have been found by other retrieval. This is run DCU952. The third run we submitted was for Spanish data. We ran the entire document corpus through a POS tagger and indexed documents (and queries) by a combination of base form of non-stopwords plus their POS class. Retrieval is performed using SMART with extra weights for query and document terms depending on their POS class. The performance figures we obtained in terms of precision and recall are given at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmeatonKO95.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmeatonKO95,
		author = {Alan F. Smeaton and Fergus Kelledy and Ruairi O'Donnell},
		editor = {Donna K. Harman},
		title = {{TREC-4} Experiments at Dublin City University: Thresholding Posting Lists, Query Expansion with WordNet and {POS} Tagging of Spanish},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/dublin.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmeatonKO95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Document Retrieval Using The MPS Information Server (A Report  on the TREC-4 Experiment)

_François Schiettecatte, Valerie Florance_

- :fontawesome-solid-user-group: **Participant:** [fs](./adhoc/participants.md#fs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/fsconsulting.ps.gz](http://trec.nist.gov/pubs/trec4/papers/fsconsulting.ps.gz)
- :material-file-search: **Runs:** [fsclt1](./adhoc/runs.md#fsclt1) | [fsclt2](./adhoc/runs.md#fsclt2)

??? abstract "Abstract"
	
	This paper summarizes the results of the experiments conducted by FS Consulting as part of the Fourth Text Retrieval Experiment Conference (TREC-4). FS Consulting participated in Category C, ran the ad hoc experiments, and produced two sets of results, fsclti and fsclt. Our long-term research interest is in building systems that help users find information to solve real-world problems. Our TREC-4 participation centered on three goals: to model information seeking behavior of an average searchers; to refine a retrieval system for use in a real-life setting; and to build tools to help searchers retrieve information effectively from large databases. Our two TREC-4 experiments were designed around a model of an experienced end user of information systems, one who might regularly use a system like the MPS Information Server while seeking information in a workplace or library setting. Our TREC-4 experiments provided us with baseline experience for initiating future retrieval projects and for participation in the TREC-5 interactive track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchiettecatteF95.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchiettecatteF95,
		author = {Fran{\c{c}}ois Schiettecatte and Valerie Florance},
		editor = {Donna K. Harman},
		title = {Document Retrieval Using The {MPS} Information Server {(A} Report on the {TREC-4} Experiment)},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/fsconsulting.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchiettecatteF95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC-4 Experiment: Combining Probabilistic and Vector-Space  Schemes

_Jacques Savoy, Melchior Ndarugendamwo, Dana Vrajitoru_

- :fontawesome-solid-user-group: **Participant:** [unine](./adhoc/participants.md#unine)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/savoy.ps.gz](http://trec.nist.gov/pubs/trec4/papers/savoy.ps.gz)
- :material-file-search: **Runs:** [UniNE3](./adhoc/runs.md#unine3) | [UniNE4](./adhoc/runs.md#unine4)

??? abstract "Abstract"
	
	This paper describes and evaluates a retrieval scheme combining the OKAPI probabilistic retrieval model with various vector-space schemes. In this study, each retrieval strategy represents both queries and documents using the same set of single terms; however they weight them differently. To combine these search schemes, we do not apply a given combination operator on the retrieval status nor the rank of each retrieved record (e.g., sum, average, max., etc.). We think that each retrieval strategy may perform well for a set of queries and poorly for other requests. Thus, based on a given query's statistical characteristics, our search model first selects the more appropriate retrieval scheme and then retrieves information based on the selected search mechanism. Since the selection procedure is done before any search operation, our approach has the advantage of limiting the search time to one retrieval algorithm instead of retrieving items using various retrieval schemes, and then combining the given results. In particular, this study addresses the following questions: (1) can the statistical characteristics of a query be good predictors in an automatic selection procedure; (2) faced with the relatively high retrieval effectiveness achieved by the OKAPI model, can various vector-space schemes further improve the retrieval performance of the OKAPI approach, and (3) can the learning results obtained with one tested collection (WS) be valid for another corpus (SJMN)? Participation: Category: B Query: ad-hoc, fully automatic
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavoyNV95.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavoyNV95,
		author = {Jacques Savoy and Melchior Ndarugendamwo and Dana Vrajitoru},
		editor = {Donna K. Harman},
		title = {Report on the {TREC-4} Experiment: Combining Probabilistic and Vector-Space Schemes},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/savoy.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SavoyNV95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-4

_Stephen E. Robertson, Steve Walker, Micheline Hancock-Beaulieu, Mike Gatford, A. Payne_

- :fontawesome-solid-user-group: **Participant:** [city](./adhoc/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/city.ps.gz](http://trec.nist.gov/pubs/trec4/papers/city.ps.gz)
- :material-file-search: **Runs:** [citya1](./adhoc/runs.md#citya1) | [citym1](./adhoc/runs.md#citym1)

??? abstract "Abstract"
	
	City have submitted interactive runs in all the previous TRECs, with fairly undistinguished results. This time the main emphasis has been on the development of an entirely new interactive ad hoc search system (Sections 3 and Appendix). On the non-interactive side routing term selection: there has been further work on methods of selecting routing terms; manual and automatic ad hoc: the automatic ad hoc was done in more or less the same way as for TREC-3, but in view of the very brief topic statements a few runs were also done with manually edited queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonWHGP95.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonWHGP95,
		author = {Stephen E. Robertson and Steve Walker and Micheline Hancock{-}Beaulieu and Mike Gatford and A. Payne},
		editor = {Donna K. Harman},
		title = {Okapi at {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/city.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonWHGP95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Acquaintance: Language-Independent Document Categorization by N-Grams

_Stephen Huffman_

- :fontawesome-solid-user-group: **Participant:** [nsa](./adhoc/participants.md#nsa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz](http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz)
- :material-file-search: **Runs:** [ACQADH](./adhoc/runs.md#acqadh)

??? abstract "Abstract"
	
	Acquaintance is the name of a novel vector-space n-gram technique for categorizing documents. The technique is completely language-independent, highly garble-resistant, and computationally simple. An unoptimized version of the algorithm was used to process the TREC database in a very short time.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Huffman95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Huffman95,
		author = {Stephen Huffman},
		editor = {Donna K. Harman},
		title = {Acquaintance: Language-Independent Document Categorization by N-Grams},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Huffman95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Logistic Regression at TREC4: Probabilistic Retrieval from Full  Text Document Collections

_Fredric C. Gey, Aitao Chen, Jianzhang He, Jason Meggs_

- :fontawesome-solid-user-group: **Participant:** [berkeley](./adhoc/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz](http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz)
- :material-file-search: **Runs:** [Brkly10](./adhoc/runs.md#brkly10) | [Brkly9](./adhoc/runs.md#brkly9)

??? abstract "Abstract"
	
	The Berkeley experiments for TREC4 extend those of TREC3 in three ways: for ad-hoc retrieval we retain the manual reformulations of the topics and experiment with limited query expansion based upon the assumption that top documents are relevant (this experiment was an interesting failure); for routing retrieval we introduce a logistic regression which assumes relevance weights to be only one clue among several in predicting probability of relevance. Finally, for Spanish retrieval we retrain the basic logistic regression equations to apply to the statistical distributions of Spanish words. In addition we apply two approaches to Spanish stemming, one which attempts to resolve verb variants into a standardized form, the other of which eschews stemming in favor of a massive stop word list of variants of common words.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyCHM95.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyCHM95,
		author = {Fredric C. Gey and Aitao Chen and Jianzhang He and Jason Meggs},
		editor = {Donna K. Harman},
		title = {Logistic Regression at {TREC4:} Probabilistic Retrieval from Full Text Document Collections},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GeyCHM95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Proximity Operators - So Near And Yet So Far

_David Hawking, Paul B. Thistlewaite_

- :fontawesome-solid-user-group: **Participant:** [hawking](./adhoc/participants.md#hawking)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/anu.ps.gz](http://trec.nist.gov/pubs/trec4/papers/anu.ps.gz)
- :material-file-search: **Runs:** [padreA](./adhoc/runs.md#padrea) | [padreZ](./adhoc/runs.md#padrez)

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

#### TREC-4 Ad-Hoc, Routing Retrieval and Filtering Experiments using  PIRCS

_K. L. Kwok, Laszlo Grunfeld_

- :fontawesome-solid-user-group: **Participant:** [queens](./adhoc/participants.md#queens)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz)
- :material-file-search: **Runs:** [pircs1](./adhoc/runs.md#pircs1) | [pircs2](./adhoc/runs.md#pircs2)

??? abstract "Abstract"
	
	Our ad-hoc submissions are pircsi which is fully automatic, and pircs2 which involves manually weighting some terms and adding some new words to the original topic descriptions. The number of words added are minimal. Both methods involve training and query expansion using the best-ranked subdocuments from an initial retrieval as feedback. For our routing experiments we make use of massive query expansion of 350 terms in pircsL, with emphasis on expansion with low frequency terms. Training is done using short and top-ranked known relevant subdocuments. In pircsC, we define four different 'expert' queries (pircsL being one of them) for each topic by using different subsets of training document, and later combine their retrieval results into one. Filtering experiment is done with the retrieval lists of pircsL. For each query, we use the training collections to define retrieval status values (RSVs) where the utilities are maximum for the three precision types. These RSVs are then used as thresholds for the new collections. Evaluated results show that both ad-hoc and routing retrievals perform substantially better than median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokG95.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokG95,
		author = {K. L. Kwok and Laszlo Grunfeld},
		editor = {Donna K. Harman},
		title = {{TREC-4} Ad-Hoc, Routing Retrieval and Filtering Experiments using {PIRCS}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokG95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Excalibur TREC-4 System, Preparations, and Results

_Paul E. Nelson_

- :fontawesome-solid-user-group: **Participant:** [excalibur](./adhoc/participants.md#excalibur)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/excalibur.ps.gz](http://trec.nist.gov/pubs/trec4/papers/excalibur.ps.gz)
- :material-file-search: **Runs:** [CnQst1](./adhoc/runs.md#cnqst1) | [CnQst2](./adhoc/runs.md#cnqst2)

??? abstract "Abstract"
	
	This paper describes the system, preparations, and results for the Excalibur text retrieval system used for the TREC conference. After a brief company history and background, we will discuss the system architecture, TREC-4 preparation, an analysis of our results, and some general conclusions. This will be the third Text REtrieval Conference (TREC) attended by the Excalibur development team. For TREC-1 and TREC-2 we participated as part of ConQuest Software. Please refer to the earlier conference proceedings (available from the National Institute of Standards and Technology) for a discussion of our earlier results in these first two conferences. We did not participate in TREC-3. ConQuest merged with Excalibur Technologies Corporation (the combined company is Excalibur) in July, 1995, just before the TREC-4 results were due. We are fortunate to have some additional resources to devote to query evaluation, to accuracy studies, and to our preparation and participation in the TREC conferences. Officially, the ConQuest server system is now part of a larger product suite available from Excalibur called RetrievalWare. We ran TREC-4 with early versions of RetrievalWare 5.0, which is now fully released and available as of December 1995. Many of the improvements and advances which we discovered as part of our TREC-4 evaluations (term grouping, new semantic network weights, a new relevancy ranking formula, and new fine-rank weighting windows) have now been incorporated into Version 5.0 of the product. ConQuest Software was founded in 1990 with the goal of using Natural Language Processing (NLP) and available linguistic data (such as dictionaries, thesauri, and semantic networks) to produce text retrieval products with high accuracy and performance for large databases and large user populations. Excalibur was founded in 1980 to create products that utilize Adaptive Pattern Recognition Processing (APRP™) to resolve user queries even in the face of unpredictable and erroneous data (in particular, errors due to the process of Optical Character Recognition when scanning and loading paper documents). The scope of both companies has grown over the years. The combined company, Excalibur, now has products for document management and high-performance text retrieval, for workgroups, enterprises, and on-line systems. Adaptive Pattern Recognition Processing, in addition to being fully incorporated into RetrievalWare, is also being applied to similar TREC-like tasks on images, such as fingerprint recognition, face recognition, and positive ID. Finally, we would like to give many fervent and heartfelt thanks to the RetrievalWare development team in the Excalibur Columbia office, who committed long hours and seemingly inexhaustible energies to the TREC-4 task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Nelson95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Nelson95,
		author = {Paul E. Nelson},
		editor = {Donna K. Harman},
		title = {The Excalibur {TREC-4} System, Preparations, and Results},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/excalibur.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Nelson95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### InTEXT Precision Indexing in TREC-4

_Mark Burnett, Craig Fisher, Richard L. Jones_

- :fontawesome-solid-user-group: **Participant:** [intext](./adhoc/participants.md#intext)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/intext.ps.gz](http://trec.nist.gov/pubs/trec4/papers/intext.ps.gz)
- :material-file-search: **Runs:** [INTXT2](./adhoc/runs.md#intxt2)

??? abstract "Abstract"
	
	InTEXT Systems is a subsidiary of the CP Software Group, headquartered in Folsom California. The company is a leader in the provision of advanced tools and end-user products for intelligent document management. The InTEXT Research and Development group, based in Canberra Australia, has been in existence for 10 years, and develops leading edge technology in the area of text retrieval, indexing, routing, content analysis and document clustering, using their Heuristic Learning architecture. The InTEXT Systems R and D group participated in TREC-1, when it formed the Centre for Electronic Document Research (CEDR), in conjunction with CITRI (Collaborative Information Technology Research Institute). [1]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BurnettFJ95.bib) "
	```
	@inproceedings{DBLP:conf/trec/BurnettFJ95,
		author = {Mark Burnett and Craig Fisher and Richard L. Jones},
		editor = {Donna K. Harman},
		title = {InTEXT Precision Indexing in {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/intext.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BurnettFJ95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLARIT TREC-4 Experiments

_David A. Evans, Natasa Milic-Frayling, Robert G. Lefferts_

- :fontawesome-solid-user-group: **Participant:** [clarit](./adhoc/participants.md#clarit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/t4_proceedings.html](https://trec.nist.gov/pubs/trec4/t4_proceedings.html)
- :material-file-search: **Runs:** [CLARTF](./adhoc/runs.md#clartf) | [CLARTN](./adhoc/runs.md#clartn)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EvansML95.bib) "
	```
	@inproceedings{DBLP:conf/trec/EvansML95,
		author = {David A. Evans and Natasa Milic{-}Frayling and Robert G. Lefferts},
		editor = {Donna K. Harman},
		title = {{CLARIT} {TREC-4} Experiments},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/t4_proceedings.html},
		timestamp = {Tue, 13 Mar 2018 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EvansML95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Automatic Word Similarity Detection for TREC-4 Query Expansion

_Susan Gauch, M. K. Chong_

- :fontawesome-solid-user-group: **Participant:** [ukansas](./adhoc/participants.md#ukansas)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/t4_proceedings.html](https://trec.nist.gov/pubs/trec4/t4_proceedings.html)
- :material-file-search: **Runs:** [KU1](./adhoc/runs.md#ku1)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GauchC95.bib) "
	```
	@inproceedings{DBLP:conf/trec/GauchC95,
		author = {Susan Gauch and M. K. Chong},
		editor = {Donna K. Harman},
		title = {Automatic Word Similarity Detection for {TREC-4} Query Expansion},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/t4_proceedings.html},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GauchC95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improving Accuracy and Run-Time Performance for TREC-4

_David A. Grossman, David O. Holmes, Ophir Frieder, Matthew D. Nguyen, Christopher E. Kingsbury_

- :fontawesome-solid-user-group: **Participant:** [gmu](./adhoc/participants.md#gmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/gmu.ps.gz](http://trec.nist.gov/pubs/trec4/papers/gmu.ps.gz)
- :material-file-search: **Runs:** [gmu1](./adhoc/runs.md#gmu1) | [gmu2](./adhoc/runs.md#gmu2)

??? abstract "Abstract"
	
	For TREC-4, we enhanced our existing prototype that implements relevance ranking using the AT&T DBC-1012 Model 4 parallel database machine to support the entire document collec-tion. Additionally, we developed a special purpose IR prototype to test a new index compression algorithm and to provide performance comparisons to the relational approach. We submitted official results for both automatic and manual adhoc queries for the entire 2GB English collection and the provided Spanish collection. Additionally, we submitted results using n-grams to process the corrupted data. In addition to implementing the vector-space model, we experimented with query reduction based on term frequency. Query reduction was shown to result in dramatically improved run-time performance and, in many cases, resulted in little or no degradation of precision/ recall.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanHFNK95.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanHFNK95,
		author = {David A. Grossman and David O. Holmes and Ophir Frieder and Matthew D. Nguyen and Christopher E. Kingsbury},
		editor = {Donna K. Harman},
		title = {Improving Accuracy and Run-Time Performance for {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/gmu.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanHFNK95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improvements on Query Term Expansion and Ranking Formula

_Kenji Satoh, Susumu Akamine, Akitoshi Okumura_

- :fontawesome-solid-user-group: **Participant:** [nec](./adhoc/participants.md#nec)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/t4_proceedings.html](https://trec.nist.gov/pubs/trec4/t4_proceedings.html)
- :material-file-search: **Runs:** [virtu4](./adhoc/runs.md#virtu4)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SatohAO95.bib) "
	```
	@inproceedings{DBLP:conf/trec/SatohAO95,
		author = {Kenji Satoh and Susumu Akamine and Akitoshi Okumura},
		editor = {Donna K. Harman},
		title = {Improvements on Query Term Expansion and Ranking Formula},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/t4_proceedings.html},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SatohAO95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Database Merging 

#### Recent Experiments with INQUERY

_James Allan, Lisa Ballesteros, James P. Callan, W. Bruce Croft, Zhihong Lu_

- :fontawesome-solid-user-group: **Participant:** [umass](./dbmerge/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz](http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz)
- :material-file-search: **Runs:** [INQ205](./dbmerge/runs.md#inq205) | [INQ206](./dbmerge/runs.md#inq206) | [INQ207](./dbmerge/runs.md#inq207) | [INQ208](./dbmerge/runs.md#inq208) | [INQ209](./dbmerge/runs.md#inq209)

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

- :fontawesome-solid-user-group: **Participant:** [siemens](./dbmerge/participants.md#siemens)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/siemens.ps.gz](http://trec.nist.gov/pubs/trec4/papers/siemens.ps.gz)
- :material-file-search: **Runs:** [siems2](./dbmerge/runs.md#siems2) | [siems3](./dbmerge/runs.md#siems3)

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

- :fontawesome-solid-user-group: **Participant:** [hawking](./dbmerge/participants.md#hawking)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/anu.ps.gz](http://trec.nist.gov/pubs/trec4/papers/anu.ps.gz)
- :material-file-search: **Runs:** [padreW](./dbmerge/runs.md#padrew)

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

## Routing 

#### Shortest Substring Ranking (MultiText Experiments for TREC-4)

_Charles L. A. Clarke, Gordon V. Cormack, Forbes J. Burkowski_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo](./routing/participants.md#uwaterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/uwaterloo.ps.gz](http://trec.nist.gov/pubs/trec4/papers/uwaterloo.ps.gz)
- :material-file-search: **Runs:** [uwgcl1](./routing/runs.md#uwgcl1)

??? abstract "Abstract"
	
	To address the TREC-4 topics, we used a precise query language that yields and combines arbitrary intervals of text rather than pre-defined units like words and documents. Each solution was scored in inverse proportion to the length of the shortest interval containing it. Each document was scored by the sum of the scores of solutions within it. Whenever the above strategy yielded less than 1000 documents, documents satisfying successively weaker queries were added with lower rank. Our results for the ad-hoc topics compare favourably with the median average precision for all groups.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCB95.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCB95,
		author = {Charles L. A. Clarke and Gordon V. Cormack and Forbes J. Burkowski},
		editor = {Donna K. Harman},
		title = {Shortest Substring Ranking (MultiText Experiments for {TREC-4)}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/uwaterloo.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCB95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recent Experiments with INQUERY

_James Allan, Lisa Ballesteros, James P. Callan, W. Bruce Croft, Zhihong Lu_

- :fontawesome-solid-user-group: **Participant:** [umass](./routing/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz](http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz)
- :material-file-search: **Runs:** [INQ203](./routing/runs.md#inq203) | [INQ204](./routing/runs.md#inq204)

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

#### New Retrieval Approaches Using SMART: TREC 4

_Chris Buckley, Amit Singhal, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [cornell](./routing/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz)
- :material-file-search: **Runs:** [CrnlRE](./routing/runs.md#crnlre) | [CrnlRL](./routing/runs.md#crnlrl)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 4, performing runs in the routing, ad-hoc, confused text, interactive, and foreign language environments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleySM95.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleySM95,
		author = {Chris Buckley and Amit Singhal and Mandar Mitra},
		editor = {Donna K. Harman},
		title = {New Retrieval Approaches Using {SMART:} {TREC} 4},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/Cornell\_trec4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleySM95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Research in Automatic Profile Generation and Passage-Level Routing  with LMDS

_Julian A. Yochum_

- :fontawesome-solid-user-group: **Participant:** [logicon](./routing/participants.md#logicon)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/logicon.ps.gz](http://trec.nist.gov/pubs/trec4/papers/logicon.ps.gz)
- :material-file-search: **Runs:** [losPA2](./routing/runs.md#lospa2) | [losPA3](./routing/runs.md#lospa3)

??? abstract "Abstract"
	
	This paper describes the development of a prototype system to generate routing profiles automatically from sets of relevant documents provided by a user, and to assign relevance scores to the documents selected by these profiles. The prototype was developed with the Logicon Message Dissemination System (LMDS) for participation in the Fourth Text REtrieval Conference (TREC-4). Each generated profile contains two sets of terms: a very small set to select documents, and a much larger set to assign a relevance score to each document selected. The profile generator chooses each term and assigns a weight to it, based on its frequency of occurrence in the set of documents provided by the user, and on its frequency of occurrence in a large representative corpus of documents. The LMDS search engine uses the resulting profiles to select documents, and then passes the documents to the scoring prototype for ranking. The score assigned is a function of the weights of all profile terms found in the entire document, and of those found in fixed-length overlapping passages within the document. Performance figures and TREC-4 results are included. An appendix describes a modification to the TREC-4 algorithm, made since the conference, which has produced significant improvements in both recall and precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yochum95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yochum95,
		author = {Julian A. Yochum},
		editor = {Donna K. Harman},
		title = {Research in Automatic Profile Generation and Passage-Level Routing with {LMDS}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/logicon.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yochum95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Natural Language Information Retrieval: TREC-4 Report

_Tomek Strzalkowski, Jose Perez Carballo_

- :fontawesome-solid-user-group: **Participant:** [nyuge](./routing/participants.md#nyuge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/nyuge.ps.gz](http://trec.nist.gov/pubs/trec4/papers/nyuge.ps.gz)
- :material-file-search: **Runs:** [nyuge1](./routing/runs.md#nyuge1) | [nyuge2](./routing/runs.md#nyuge2)

??? abstract "Abstract"
	
	In this paper we report on the joint GE/NYU natural language information retrieval project as related to the 4th Text Retrieval Conference (TREC-4). The main thrust of this project is to use natural language processing techniques to enhance the effectiveness of full-text document retrieval. During the course of the four TREC conferences, we have built a prototype IR system designed around a statistical full-text indexing and search backbone provided by the NIST's Prise engine. The original Prise has been modified to allow handling of multi-word phrases, differential term weighting schemes, automatic query expansion, index partitioning and rank merging, as well as dealing with complex documents. Natural language processing is used to (1) preprocess the documents in order to extract content-carrying terms, (2) discover inter-term dependencies and build a conceptual hierarchy specific to the database domain, and (3) process user's natural language requests into effective search queries. The overall architecture of the system is essentially the same as in TREC-3, as our efforts this year were directed at optimizing the performance of all components. A notable exception is the new massive query expansion module used in routing experiments, which replaces a prototype extension used in the TREC-3 system. On the other hand, it has to be noted that the character and the level of difficulty of TREC queries has changed quite significantly since the last year evaluation. TREC-4 new ad-hoc queries are far shorter, less focused, and they have a flavor of information requests (What is the prognosis of ...) rather than search directives typical for earlier TRECs (The relevant document will contain ...). This makes building of good search queries a more sensitive task than before. We thus decided to introduce only minimum number of changes to our indexing and search processes, and even roll back some of the TREC-3 extensions which dealt with longer and somewhat redundant queries (e.g., locality matching? ). Overall, our system performed quite well as our position with respect to the best systems improved steadily since the beginning of TREC. It should be noted that the most significant gain in performance seems to occur in precision near the top of the ranking, at 5, 10, 15 and 20 documents. Indeed, our unofficial manual runs performed after TREC-4 conference show superior results in these categories, topping by a large margin the best manual scores by any system in the official evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrzalkowskiC95.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrzalkowskiC95,
		author = {Tomek Strzalkowski and Jose Perez Carballo},
		editor = {Donna K. Harman},
		title = {Natural Language Information Retrieval: {TREC-4} Report},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/nyuge.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StrzalkowskiC95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-4

_Stephen E. Robertson, Steve Walker, Micheline Hancock-Beaulieu, Mike Gatford, A. Payne_

- :fontawesome-solid-user-group: **Participant:** [city](./routing/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/city.ps.gz](http://trec.nist.gov/pubs/trec4/papers/city.ps.gz)
- :material-file-search: **Runs:** [cityr1](./routing/runs.md#cityr1) | [cityr2](./routing/runs.md#cityr2)

??? abstract "Abstract"
	
	City have submitted interactive runs in all the previous TRECs, with fairly undistinguished results. This time the main emphasis has been on the development of an entirely new interactive ad hoc search system (Sections 3 and Appendix). On the non-interactive side routing term selection: there has been further work on methods of selecting routing terms; manual and automatic ad hoc: the automatic ad hoc was done in more or less the same way as for TREC-3, but in view of the very brief topic statements a few runs were also done with manually edited queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonWHGP95.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonWHGP95,
		author = {Stephen E. Robertson and Steve Walker and Micheline Hancock{-}Beaulieu and Mike Gatford and A. Payne},
		editor = {Donna K. Harman},
		title = {Okapi at {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/city.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonWHGP95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Xerox Site Report: Four TREC-4 Tracks

_Marti A. Hearst, Jan O. Pedersen, Peter Pirolli, Hinrich Schütze, Gregory Grefenstette, David A. Hull_

- :fontawesome-solid-user-group: **Participant:** [xerox](./routing/participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz](http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz)
- :material-file-search: **Runs:** [xerox1](./routing/runs.md#xerox1) | [xerox2](./routing/runs.md#xerox2)

??? abstract "Abstract"
	
	The Xerox research centers participated in four TREC-4 activities: the routing task, the filtering track, the Spanish track, and the interactive track. We addressed the core routing task as a problem in statistical classifica-tion: given a training set of judged documents, build an error-minimizing statistical classifier to assess the relevance of new test documents. This year, we built on the methodology developed in 21] by adding a combination strategy that pooled evidence across a number of separately trained classification schemes. Since many of our classifiers infer probability of relevance, adapting our routing methods to the filtering track consisted of obtaining probability estimates for the remaining classifiers and reporting those documents scoring above the probability thresholds determined by the three set linear utility func-tions. Our contribution to the Spanish track focussed on the effect of principled language analysis on a baseline retrieval system. We employed finite-state morphology [14] and hidden-Markov-model-based part-of-speech tagging 17] to analyze Spanish language text into canonical stemmed forms, and to identify verbs and noun phrases. Various combinations of these were then fed into SMART [1] for ranked retrieval. This year our activity on the ad hoc task focussed on the interactive track, which allows arbitrary user interaction in the process of finding relevant documents. We developed a graphical user interface to two interactive tools, Scatter/Gather [6] and Tilebars [11], and asked a number of subjects to use this tool to 'find as many good documents as you can for a topic, in around 30 minutes, without collecting too much rubbish'. We set up an experimental design to measure the value of each tool, and their combination, averaging out subject effects. That is, we were interested in determining how well the average user might perform with interactive tools rather than measuring the very best performance possible assuming an expert searcher. These efforts are described in more detail in the following sections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HearstPPSGH95.bib) "
	```
	@inproceedings{DBLP:conf/trec/HearstPPSGH95,
		author = {Marti A. Hearst and Jan O. Pedersen and Peter Pirolli and Hinrich Sch{\"{u}}tze and Gregory Grefenstette and David A. Hull},
		editor = {Donna K. Harman},
		title = {Xerox Site Report: Four {TREC-4} Tracks},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz},
		timestamp = {Thu, 08 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HearstPPSGH95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Acquaintance: Language-Independent Document Categorization by N-Grams

_Stephen Huffman_

- :fontawesome-solid-user-group: **Participant:** [nsa](./routing/participants.md#nsa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz](http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz)
- :material-file-search: **Runs:** [ACQROU](./routing/runs.md#acqrou)

??? abstract "Abstract"
	
	Acquaintance is the name of a novel vector-space n-gram technique for categorizing documents. The technique is completely language-independent, highly garble-resistant, and computationally simple. An unoptimized version of the algorithm was used to process the TREC database in a very short time.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Huffman95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Huffman95,
		author = {Stephen Huffman},
		editor = {Donna K. Harman},
		title = {Acquaintance: Language-Independent Document Categorization by N-Grams},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Huffman95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Logistic Regression at TREC4: Probabilistic Retrieval from Full  Text Document Collections

_Fredric C. Gey, Aitao Chen, Jianzhang He, Jason Meggs_

- :fontawesome-solid-user-group: **Participant:** [berkeley](./routing/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz](http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz)
- :material-file-search: **Runs:** [Brkly11](./routing/runs.md#brkly11) | [Brkly12](./routing/runs.md#brkly12)

??? abstract "Abstract"
	
	The Berkeley experiments for TREC4 extend those of TREC3 in three ways: for ad-hoc retrieval we retain the manual reformulations of the topics and experiment with limited query expansion based upon the assumption that top documents are relevant (this experiment was an interesting failure); for routing retrieval we introduce a logistic regression which assumes relevance weights to be only one clue among several in predicting probability of relevance. Finally, for Spanish retrieval we retrain the basic logistic regression equations to apply to the statistical distributions of Spanish words. In addition we apply two approaches to Spanish stemming, one which attempts to resolve verb variants into a standardized form, the other of which eschews stemming in favor of a massive stop word list of variants of common words.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyCHM95.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyCHM95,
		author = {Fredric C. Gey and Aitao Chen and Jianzhang He and Jason Meggs},
		editor = {Donna K. Harman},
		title = {Logistic Regression at {TREC4:} Probabilistic Retrieval from Full Text Document Collections},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GeyCHM95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-4 Ad-Hoc, Routing Retrieval and Filtering Experiments using  PIRCS

_K. L. Kwok, Laszlo Grunfeld_

- :fontawesome-solid-user-group: **Participant:** [queens](./routing/participants.md#queens)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz)
- :material-file-search: **Runs:** [pircsC](./routing/runs.md#pircsc) | [pircsL](./routing/runs.md#pircsl)

??? abstract "Abstract"
	
	Our ad-hoc submissions are pircsi which is fully automatic, and pircs2 which involves manually weighting some terms and adding some new words to the original topic descriptions. The number of words added are minimal. Both methods involve training and query expansion using the best-ranked subdocuments from an initial retrieval as feedback. For our routing experiments we make use of massive query expansion of 350 terms in pircsL, with emphasis on expansion with low frequency terms. Training is done using short and top-ranked known relevant subdocuments. In pircsC, we define four different 'expert' queries (pircsL being one of them) for each topic by using different subsets of training document, and later combine their retrieval results into one. Filtering experiment is done with the retrieval lists of pircsL. For each query, we use the training collections to define retrieval status values (RSVs) where the utilities are maximum for the three precision types. These RSVs are then used as thresholds for the new collections. Evaluated results show that both ad-hoc and routing retrievals perform substantially better than median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokG95.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokG95,
		author = {K. L. Kwok and Laszlo Grunfeld},
		editor = {Donna K. Harman},
		title = {{TREC-4} Ad-Hoc, Routing Retrieval and Filtering Experiments using {PIRCS}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokG95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multi-lingual Text Filtering Using Semantic Modeling

_James R. Driscoll, S. Abbott, K. Hu, M. Miller, G. Theis_

- :fontawesome-solid-user-group: **Participant:** [ucf](./routing/participants.md#ucf)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/papers/ucentral-florida.pdf](https://trec.nist.gov/pubs/trec4/papers/ucentral-florida.pdf)
- :material-file-search: **Runs:** [UCF100](./routing/runs.md#ucf100)

??? abstract "Abstract"
	
	Semantic Modeling is used to investigate multilingual text filtering. In our approach, the Entity-Relationship (ER) Model is used as a basis for descriptions of information preferences (profiles) in the information filtering process. A profile is viewed as having both a static aspect and a dynamic aspect. The static aspect of a profile can be represented as an ER schema; and the dynamic aspect of the profile can be represented by synonyms of schema components and domain values for schema attributes. For TREC-4, the routing task and the Spanish adhoc task are accomplished using this technique. For the routing task, a large amount of time was spent in an effort to optimize filter performance using the training data that was available for the routing topics. For the Spanish adhoc task, a large amount of time was spent using external sources to develop good filters; in addition, some time was spent implementing a program to help port our approach to this second language. A multi-lingual (English, French, German, and Spanish) experiment is also reported.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DriscollAHMT95.bib) "
	```
	@inproceedings{DBLP:conf/trec/DriscollAHMT95,
		author = {James R. Driscoll and S. Abbott and K. Hu and M. Miller and G. Theis},
		editor = {Donna K. Harman},
		title = {Multi-lingual Text Filtering Using Semantic Modeling},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/papers/ucentral-florida.pdf},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DriscollAHMT95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLARIT TREC-4 Interactive Experiments

_Natasa Milic-Frayling, Michael P. Mastroianni, David A. Evans, Robert G. Lefferts, ChengXiang Zhai, Xiang Tong_

- :fontawesome-solid-user-group: **Participant:** [clarit](./routing/participants.md#clarit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/t4_proceedings.html](https://trec.nist.gov/pubs/trec4/t4_proceedings.html)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Milic-FraylingMELZT95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Milic-FraylingMELZT95,
		author = {Natasa Milic{-}Frayling and Michael P. Mastroianni and David A. Evans and Robert G. Lefferts and ChengXiang Zhai and Xiang Tong},
		editor = {Donna K. Harman},
		title = {{CLARIT} {TREC-4} Interactive Experiments},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/t4_proceedings.html},
		timestamp = {Fri, 19 Jun 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Milic-FraylingMELZT95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Document Routing by Discriminant Projection: TREC-4

_Kok F. Lai, Vincent A. S. Lee, Jeremy P. Chew_

- :fontawesome-solid-user-group: **Participant:** [iti](./routing/participants.md#iti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/iti.ps.gz](http://trec.nist.gov/pubs/trec4/papers/iti.ps.gz)
- :material-file-search: **Runs:** [itidp1](./routing/runs.md#itidp1) | [itidp2](./routing/runs.md#itidp2)

??? abstract "Abstract"
	
	We present document routing as a standard problem in discriminant analysis. The standard solution involves the inversion of a large matrix whose dimension is the number of indexed terms. Typically, the solution does not exist because the number of training documents are much smaller compared to the number of terms. We show that one can project this raw document space into a lower dimensional space where solution is possible. Our projection algorithm exploits the characterisitics of the empty space, using only the training documents for efficient coding of the relevance information. Its complexity is linear with respect to the number of terms, and second order with respect to the number of training documents. We can therefore fully exploit the power of discriminant analysis without imposing severe computational and storage constraints.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LaiLC95.bib) "
	```
	@inproceedings{DBLP:conf/trec/LaiLC95,
		author = {Kok F. Lai and Vincent A. S. Lee and Jeremy P. Chew},
		editor = {Donna K. Harman},
		title = {Document Routing by Discriminant Projection: {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/iti.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LaiLC95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improvements on Query Term Expansion and Ranking Formula

_Kenji Satoh, Susumu Akamine, Akitoshi Okumura_

- :fontawesome-solid-user-group: **Participant:** [nec](./routing/participants.md#nec)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/t4_proceedings.html](https://trec.nist.gov/pubs/trec4/t4_proceedings.html)
- :material-file-search: **Runs:** [virtu3](./routing/runs.md#virtu3)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SatohAO95.bib) "
	```
	@inproceedings{DBLP:conf/trec/SatohAO95,
		author = {Kenji Satoh and Susumu Akamine and Akitoshi Okumura},
		editor = {Donna K. Harman},
		title = {Improvements on Query Term Expansion and Ranking Formula},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/t4_proceedings.html},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SatohAO95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using CONVECTIS, A Context Vector-Based Indexing System for TREC-4

_Joel Carleton, William R. Caid, R. V. Sasseen_

- :fontawesome-solid-user-group: **Participant:** [hnc](./routing/participants.md#hnc)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/t4_proceedings.html](https://trec.nist.gov/pubs/trec4/t4_proceedings.html)
- :material-file-search: **Runs:** [HNC11](./routing/runs.md#hnc11) | [HNC21](./routing/runs.md#hnc21)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarletonCS95.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarletonCS95,
		author = {Joel Carleton and William R. Caid and R. V. Sasseen},
		editor = {Donna K. Harman},
		title = {Using CONVECTIS, {A} Context Vector-Based Indexing System for {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/t4_proceedings.html},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CarletonCS95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Spanish 

#### A TREC Evaluation of Query Translation Methods For Multi-Lingual  Text Retrieval

_Mark W. Davis, Ted Dunning_

- :fontawesome-solid-user-group: **Participant:** [nmsu](./spanish/participants.md#nmsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/nmsu.ps.gz](http://trec.nist.gov/pubs/trec4/papers/nmsu.ps.gz)

??? abstract "Abstract"
	
	In a Multi-lingual Text Retrieval (MLTR) system, queries in one language are used to retrieve documents in several languages. Although all of the collection documents could be translated to a single language, a more efficient approach is to simply translate the queries into each of the document lan-guages. We have investigated five methods for query translation that rely on lexical-transfer and corpus-based methods for creating multi-lingual queries. The resulting queries produced by these systems were then used in a competitive information-retrieval environment and the results evaluated by the TREC evaluation group.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DavisD95.bib) "
	```
	@inproceedings{DBLP:conf/trec/DavisD95,
		author = {Mark W. Davis and Ted Dunning},
		editor = {Donna K. Harman},
		title = {A {TREC} Evaluation of Query Translation Methods For Multi-Lingual Text Retrieval},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/nmsu.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DavisD95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recent Experiments with INQUERY

_James Allan, Lisa Ballesteros, James P. Callan, W. Bruce Croft, Zhihong Lu_

- :fontawesome-solid-user-group: **Participant:** [umass](./spanish/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz](http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz)
- :material-file-search: **Runs:** [SIN012](./spanish/runs.md#sin012) | [SIN010](./spanish/runs.md#sin010) | [SIN011](./spanish/runs.md#sin011)

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

#### New Retrieval Approaches Using SMART: TREC 4

_Chris Buckley, Amit Singhal, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [cornell](./spanish/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz)
- :material-file-search: **Runs:** [CrnlSE](./spanish/runs.md#crnlse) | [CrnlSE](./spanish/runs.md#crnlse)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 4, performing runs in the routing, ad-hoc, confused text, interactive, and foreign language environments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleySM95.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleySM95,
		author = {Chris Buckley and Amit Singhal and Mandar Mitra},
		editor = {Donna K. Harman},
		title = {New Retrieval Approaches Using {SMART:} {TREC} 4},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/Cornell\_trec4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleySM95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Similarity Measures for Short Queries

_Ross Wilkinson, Justin Zobel, Ron Sacks-Davis_

- :fontawesome-solid-user-group: **Participant:** [citri](./spanish/participants.md#citri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/citri.ps.gz](http://trec.nist.gov/pubs/trec4/papers/citri.ps.gz)
- :material-file-search: **Runs:** [citri-sp3](./spanish/runs.md#citri-sp3) | [citri-sp1](./spanish/runs.md#citri-sp1) | [citri-sp2](./spanish/runs.md#citri-sp2)

??? abstract "Abstract"
	
	Ad-hoc queries are usually short, of perhaps two to ten terms. However, in previous rounds of TREC we have concentrated on obtaining optimal performance for the long TREC topics. In this paper we investigate the behaviour of similarity measures on short queries, and show experimentally that two successful measures which give similar, good performance on long TREC topics do not work well for short queries. We explore methods for achieving greater effectiveness for short queries, and conclude that a successful approach is to combine these similarity measures with other evidence. We also briefly describe our experiments with the Spanish data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WilkinsonZS95.bib) "
	```
	@inproceedings{DBLP:conf/trec/WilkinsonZS95,
		author = {Ross Wilkinson and Justin Zobel and Ron Sacks{-}Davis},
		editor = {Donna K. Harman},
		title = {Similarity Measures for Short Queries},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/citri.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WilkinsonZS95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-4 Experiments at Dublin City University: Thresholding Posting  Lists, Query Expansion with WordNet and POS Tagging of Spanish

_Alan F. Smeaton, Fergus Kelledy, Ruairi O'Donnell_

- :fontawesome-solid-user-group: **Participant:** [dublin](./spanish/participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/dublin.ps.gz](http://trec.nist.gov/pubs/trec4/papers/dublin.ps.gz)
- :material-file-search: **Runs:** [DCUSP0](./spanish/runs.md#dcusp0) | [DCUSP0](./spanish/runs.md#dcusp0)

??? abstract "Abstract"
	
	In this paper we describe work done as part of the TREC-4 benchmarking exercise by a team from Dublin City University. In TREC-4 we had 3 activities as follows: In work on improving the efficiency of standard SMART-like query processing we have applied various thresholding processes to the postings list of an inverted file and we have limited the number of document score accumulators available during query processing. The first run we submitted for evaluation in TREC-4 (DCU951) used our best set of thresholding and accumulator set parameters. The second run we submitted is based upon a query expansion using terms from WordNet. Essentially, for each original query term we determine its level of specificity or abstraction; for broad terms we add more specific terms, for specific original terms we add broader ones; for ones in-between we add both broader and narrower terms. When the query is expanded we then delete all the original query terms in order to add to the judged pool, documents that our expansion would find that would not have been found by other retrieval. This is run DCU952. The third run we submitted was for Spanish data. We ran the entire document corpus through a POS tagger and indexed documents (and queries) by a combination of base form of non-stopwords plus their POS class. Retrieval is performed using SMART with extra weights for query and document terms depending on their POS class. The performance figures we obtained in terms of precision and recall are given at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmeatonKO95.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmeatonKO95,
		author = {Alan F. Smeaton and Fergus Kelledy and Ruairi O'Donnell},
		editor = {Donna K. Harman},
		title = {{TREC-4} Experiments at Dublin City University: Thresholding Posting Lists, Query Expansion with WordNet and {POS} Tagging of Spanish},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/dublin.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmeatonKO95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Xerox Site Report: Four TREC-4 Tracks

_Marti A. Hearst, Jan O. Pedersen, Peter Pirolli, Hinrich Schütze, Gregory Grefenstette, David A. Hull_

- :fontawesome-solid-user-group: **Participant:** [xerox](./spanish/participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz](http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz)
- :material-file-search: **Runs:** [xerox-sp1](./spanish/runs.md#xerox-sp1) | [xerox-sp2](./spanish/runs.md#xerox-sp2) | [xerox-sp1](./spanish/runs.md#xerox-sp1) | [xerox-sp2](./spanish/runs.md#xerox-sp2)

??? abstract "Abstract"
	
	The Xerox research centers participated in four TREC-4 activities: the routing task, the filtering track, the Spanish track, and the interactive track. We addressed the core routing task as a problem in statistical classifica-tion: given a training set of judged documents, build an error-minimizing statistical classifier to assess the relevance of new test documents. This year, we built on the methodology developed in 21] by adding a combination strategy that pooled evidence across a number of separately trained classification schemes. Since many of our classifiers infer probability of relevance, adapting our routing methods to the filtering track consisted of obtaining probability estimates for the remaining classifiers and reporting those documents scoring above the probability thresholds determined by the three set linear utility func-tions. Our contribution to the Spanish track focussed on the effect of principled language analysis on a baseline retrieval system. We employed finite-state morphology [14] and hidden-Markov-model-based part-of-speech tagging 17] to analyze Spanish language text into canonical stemmed forms, and to identify verbs and noun phrases. Various combinations of these were then fed into SMART [1] for ranked retrieval. This year our activity on the ad hoc task focussed on the interactive track, which allows arbitrary user interaction in the process of finding relevant documents. We developed a graphical user interface to two interactive tools, Scatter/Gather [6] and Tilebars [11], and asked a number of subjects to use this tool to 'find as many good documents as you can for a topic, in around 30 minutes, without collecting too much rubbish'. We set up an experimental design to measure the value of each tool, and their combination, averaging out subject effects. That is, we were interested in determining how well the average user might perform with interactive tools rather than measuring the very best performance possible assuming an expert searcher. These efforts are described in more detail in the following sections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HearstPPSGH95.bib) "
	```
	@inproceedings{DBLP:conf/trec/HearstPPSGH95,
		author = {Marti A. Hearst and Jan O. Pedersen and Peter Pirolli and Hinrich Sch{\"{u}}tze and Gregory Grefenstette and David A. Hull},
		editor = {Donna K. Harman},
		title = {Xerox Site Report: Four {TREC-4} Tracks},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz},
		timestamp = {Thu, 08 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HearstPPSGH95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Logistic Regression at TREC4: Probabilistic Retrieval from Full  Text Document Collections

_Fredric C. Gey, Aitao Chen, Jianzhang He, Jason Meggs_

- :fontawesome-solid-user-group: **Participant:** [berkeley](./spanish/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz](http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz)
- :material-file-search: **Runs:** [BrklySP1](./spanish/runs.md#brklysp1) | [BrklySP2](./spanish/runs.md#brklysp2) | [BrklySP4](./spanish/runs.md#brklysp4)

??? abstract "Abstract"
	
	The Berkeley experiments for TREC4 extend those of TREC3 in three ways: for ad-hoc retrieval we retain the manual reformulations of the topics and experiment with limited query expansion based upon the assumption that top documents are relevant (this experiment was an interesting failure); for routing retrieval we introduce a logistic regression which assumes relevance weights to be only one clue among several in predicting probability of relevance. Finally, for Spanish retrieval we retrain the basic logistic regression equations to apply to the statistical distributions of Spanish words. In addition we apply two approaches to Spanish stemming, one which attempts to resolve verb variants into a standardized form, the other of which eschews stemming in favor of a massive stop word list of variants of common words.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyCHM95.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyCHM95,
		author = {Fredric C. Gey and Aitao Chen and Jianzhang He and Jason Meggs},
		editor = {Donna K. Harman},
		title = {Logistic Regression at {TREC4:} Probabilistic Retrieval from Full Text Document Collections},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GeyCHM95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multi-lingual Text Filtering Using Semantic Modeling

_James R. Driscoll, S. Abbott, K. Hu, M. Miller, G. Theis_

- :fontawesome-solid-user-group: **Participant:** [ucf](./spanish/participants.md#ucf)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/papers/ucentral-florida.pdf](https://trec.nist.gov/pubs/trec4/papers/ucentral-florida.pdf)
- :material-file-search: **Runs:** [UCFSP0](./spanish/runs.md#ucfsp0) | [UCFSP1](./spanish/runs.md#ucfsp1) | [UCFSP2](./spanish/runs.md#ucfsp2)

??? abstract "Abstract"
	
	Semantic Modeling is used to investigate multilingual text filtering. In our approach, the Entity-Relationship (ER) Model is used as a basis for descriptions of information preferences (profiles) in the information filtering process. A profile is viewed as having both a static aspect and a dynamic aspect. The static aspect of a profile can be represented as an ER schema; and the dynamic aspect of the profile can be represented by synonyms of schema components and domain values for schema attributes. For TREC-4, the routing task and the Spanish adhoc task are accomplished using this technique. For the routing task, a large amount of time was spent in an effort to optimize filter performance using the training data that was available for the routing topics. For the Spanish adhoc task, a large amount of time was spent using external sources to develop good filters; in addition, some time was spent implementing a program to help port our approach to this second language. A multi-lingual (English, French, German, and Spanish) experiment is also reported.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DriscollAHMT95.bib) "
	```
	@inproceedings{DBLP:conf/trec/DriscollAHMT95,
		author = {James R. Driscoll and S. Abbott and K. Hu and M. Miller and G. Theis},
		editor = {Donna K. Harman},
		title = {Multi-lingual Text Filtering Using Semantic Modeling},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/papers/ucentral-florida.pdf},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DriscollAHMT95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improving Accuracy and Run-Time Performance for TREC-4

_David A. Grossman, David O. Holmes, Ophir Frieder, Matthew D. Nguyen, Christopher E. Kingsbury_

- :fontawesome-solid-user-group: **Participant:** [gmu](./spanish/participants.md#gmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/gmu.ps.gz](http://trec.nist.gov/pubs/trec4/papers/gmu.ps.gz)
- :material-file-search: **Runs:** [gmuauto](./spanish/runs.md#gmuauto) | [gmuauto](./spanish/runs.md#gmuauto) | [gmuman](./spanish/runs.md#gmuman)

??? abstract "Abstract"
	
	For TREC-4, we enhanced our existing prototype that implements relevance ranking using the AT&T DBC-1012 Model 4 parallel database machine to support the entire document collec-tion. Additionally, we developed a special purpose IR prototype to test a new index compression algorithm and to provide performance comparisons to the relational approach. We submitted official results for both automatic and manual adhoc queries for the entire 2GB English collection and the provided Spanish collection. Additionally, we submitted results using n-grams to process the corrupted data. In addition to implementing the vector-space model, we experimented with query reduction based on term frequency. Query reduction was shown to result in dramatically improved run-time performance and, in many cases, resulted in little or no degradation of precision/ recall.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanHFNK95.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanHFNK95,
		author = {David A. Grossman and David O. Holmes and Ophir Frieder and Matthew D. Nguyen and Christopher E. Kingsbury},
		editor = {Donna K. Harman},
		title = {Improving Accuracy and Run-Time Performance for {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/gmu.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanHFNK95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Filtering 

#### The TREC-4 Filtering Track

_David D. Lewis_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/lewis.ps.gz](http://trec.nist.gov/pubs/trec4/papers/lewis.ps.gz)
??? abstract "Abstract"
	
	The TREC-4 filtering track was an experiment in the evaluation of binary text classification systems. In contrast to ranking systems, binary text classification systems may need to produce result sets of any size, requiring that sampling be used to estimate their effectiveness. We present an effectiveness measure based on utility, and two sampling strategies (pooling and stratified sampling) for estimating utility of submitted sets. An evaluation of four sites was successfully carried out using this approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lewis95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lewis95,
		author = {David D. Lewis},
		editor = {Donna K. Harman},
		title = {The {TREC-4} Filtering Track},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/lewis.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lewis95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-4 Ad-Hoc, Routing Retrieval and Filtering Experiments using  PIRCS

_K. L. Kwok, Laszlo Grunfeld_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz)

??? abstract "Abstract"
	
	Our ad-hoc submissions are pircs which is fully automatic, and pircs2 which involves manually weighting some terms and adding some new words to the original topic descriptions. The number of words added are minimal. Both methods involve training and query expansion using the best-ranked subdocuments from an initial retrieval as feedback. For our routing experiments we make use of massive query expansion of 350 terms in pircsL, with emphasis on expansion with low frequency terms. Training is done using short and top-ranked known relevant subdocuments. In pircsC, we define four different 'expert' queries (pircsL being one of them) for each topic by using different subsets of training document, and later combine their retrieval results into one. Filtering experiment is done with the retrieval lists of pircsL. For each query, we use the training collections to define retrieval status values (RSVs) where the utilities are maximum for the three precision types. These RSVs are then used as thresholds for the new collections. Evaluated results show that both ad-hoc and routing retrievals perform substantially better than median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokG95.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokG95,
		author = {K. L. Kwok and Laszlo Grunfeld},
		editor = {Donna K. Harman},
		title = {{TREC-4} Ad-Hoc, Routing Retrieval and Filtering Experiments using {PIRCS}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokG95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Confusion 

#### New Retrieval Approaches Using SMART: TREC 4

_Chris Buckley, Amit Singhal, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [cornell](./confusion/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz)
- :material-file-search: **Runs:** [CrnlB](./confusion/runs.md#crnlb) | [CrnlBc10](./confusion/runs.md#crnlbc10)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 4, performing runs in the routing, ad-hoc, confused text, interactive, and foreign language environments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleySM95.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleySM95,
		author = {Chris Buckley and Amit Singhal and Mandar Mitra},
		editor = {Donna K. Harman},
		title = {New Retrieval Approaches Using {SMART:} {TREC} 4},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/Cornell\_trec4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleySM95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Acquaintance: Language-Independent Document Categorization by N-Grams

_Stephen Huffman_

- :fontawesome-solid-user-group: **Participant:** [nsa](./confusion/participants.md#nsa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz](http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz)
- :material-file-search: **Runs:** [ACQC10](./confusion/runs.md#acqc10) | [ACQC20](./confusion/runs.md#acqc20) | [ACQUNC](./confusion/runs.md#acqunc)

??? abstract "Abstract"
	
	Acquaintance is the name of a novel vector-space n-gram technique for categorizing documents. The technique is completely language-independent, highly garble-resistant, and computationally simple. An unoptimized version of the algorithm was used to process the TREC database in a very short time.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Huffman95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Huffman95,
		author = {Stephen Huffman},
		editor = {Donna K. Harman},
		title = {Acquaintance: Language-Independent Document Categorization by N-Grams},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Huffman95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Two Experiments on Retrieval With Corrupted Data and Clean Queries  in the TREC-4 Adhoc Task Environment: Data Fusion and Pattern Scanning

_Kwong Bor Ng, Paul B. Kantor_

- :fontawesome-solid-user-group: **Participant:** [rutgers.kantor](./confusion/participants.md#rutgers.kantor)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/kantor.ps.gz](http://trec.nist.gov/pubs/trec4/papers/kantor.ps.gz)
- :material-file-search: **Runs:** [rutfum](./confusion/runs.md#rutfum) | [rutfuv](./confusion/runs.md#rutfuv) | [rutscn20](./confusion/runs.md#rutscn20)

??? abstract "Abstract"
	
	We report on several experiments in using data fusion to improve information retrieval, and in approximate text and 5-gram mathcing methods for retrieval of corrupted text, in the TREC context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NgK95.bib) "
	```
	@inproceedings{DBLP:conf/trec/NgK95,
		author = {Kwong Bor Ng and Paul B. Kantor},
		editor = {Donna K. Harman},
		title = {Two Experiments on Retrieval With Corrupted Data and Clean Queries in the {TREC-4} Adhoc Task Environment: Data Fusion and Pattern Scanning},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/kantor.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NgK95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improving Accuracy and Run-Time Performance for TREC-4

_David A. Grossman, David O. Holmes, Ophir Frieder, Matthew D. Nguyen, Christopher E. Kingsbury_

- :fontawesome-solid-user-group: **Participant:** [gmu](./confusion/participants.md#gmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/gmu.ps.gz](http://trec.nist.gov/pubs/trec4/papers/gmu.ps.gz)
- :material-file-search: **Runs:** [gmuc0](./confusion/runs.md#gmuc0) | [gmuc10](./confusion/runs.md#gmuc10)

??? abstract "Abstract"
	
	For TREC-4, we enhanced our existing prototype that implements relevance ranking using the AT&T DBC-1012 Model 4 parallel database machine to support the entire document collec-tion. Additionally, we developed a special purpose IR prototype to test a new index compression algorithm and to provide performance comparisons to the relational approach. We submitted official results for both automatic and manual adhoc queries for the entire 2GB English collection and the provided Spanish collection. Additionally, we submitted results using n-grams to process the corrupted data. In addition to implementing the vector-space model, we experimented with query reduction based on term frequency. Query reduction was shown to result in dramatically improved run-time performance and, in many cases, resulted in little or no degradation of precision/ recall.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanHFNK95.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanHFNK95,
		author = {David A. Grossman and David O. Holmes and Ophir Frieder and Matthew D. Nguyen and Christopher E. Kingsbury},
		editor = {Donna K. Harman},
		title = {Improving Accuracy and Run-Time Performance for {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/gmu.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanHFNK95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Interactive 

#### Using Relevance Feedback and Ranking in Interactive Searching

_Nicholas J. Belkin, Colleen Cool, Jürgen Koenemann, Kwong Bor Ng, Soyeon Park_

- :fontawesome-solid-user-group: **Participant:** [rutgers.belkin](./interactive/participants.md#rutgers.belkin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/ruint_paper.ps.gz](http://trec.nist.gov/pubs/trec4/papers/ruint_paper.ps.gz)
- :material-file-search: **Runs:** [ruint1](./interactive/runs.md#ruint1) | [ruint2](./interactive/runs.md#ruint2)

??? abstract "Abstract"
	
	We present results of a study in which 50 searchers, of varying degrees of experience in information retrieval (IR), each performed searches on two TREC-4 adhoc interactive track topics, using a simple interface to the INQUERY retrieval engine. The foci of our study were: the relationships between the users' models and experience of IR, and their performance in the TREC-4 adhoc task while using a best-match IR system with relevance feedback; the understanding, use and utility of relevance feedback and ranking in interactive IR; and, the evaluation of interactive IR.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinCKNP95.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinCKNP95,
		author = {Nicholas J. Belkin and Colleen Cool and J{\"{u}}rgen Koenemann and Kwong Bor Ng and Soyeon Park},
		editor = {Donna K. Harman},
		title = {Using Relevance Feedback and Ranking in Interactive Searching},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/ruint\_paper.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BelkinCKNP95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### New Retrieval Approaches Using SMART: TREC 4

_Chris Buckley, Amit Singhal, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [cornell](./interactive/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz)
- :material-file-search: **Runs:** [CrnlI1](./interactive/runs.md#crnli1) | [CrnlI2](./interactive/runs.md#crnli2)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 4, performing runs in the routing, ad-hoc, confused text, interactive, and foreign language environments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleySM95.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleySM95,
		author = {Chris Buckley and Amit Singhal and Mandar Mitra},
		editor = {Donna K. Harman},
		title = {New Retrieval Approaches Using {SMART:} {TREC} 4},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/Cornell\_trec4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleySM95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive TREC-4 at Georgia Tech

_Aravindan Veerasamy_

- :fontawesome-solid-user-group: **Participant:** [gatin](./interactive/participants.md#gatin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/GAT_trec4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/GAT_trec4.ps.gz)
- :material-file-search: **Runs:** [gatin1](./interactive/runs.md#gatin1) | [gatin2](./interactive/runs.md#gatin2)

??? abstract "Abstract"
	
	At Georgia Tech, we investigated the effectiveness of a visualization scheme for Information Retrieval systems. Displayed like a bar-graph, the visualization tool shows the distribution of query words in the set of documents retrieved in response to a query. We found that end-users use the visualization for two purposes: to gain specific information about individual documents - such as the distribution of different query words in that document. to gain aggregate information about the query result in general - such as getting a sense of the direction of the query results. In general they used the visualization tool as much as the title and full text in the process of deciding if a document addresses the given search topic. In structured post-session interviews with searchers, we also obtained information about what the searcher liked, what was frustrating to them, and what they wanted in the system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Veerasamy95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Veerasamy95,
		author = {Aravindan Veerasamy},
		editor = {Donna K. Harman},
		title = {Interactive {TREC-4} at Georgia Tech},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/GAT\_trec4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Veerasamy95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-4

_Stephen E. Robertson, Steve Walker, Micheline Hancock-Beaulieu, Mike Gatford, A. Payne_

- :fontawesome-solid-user-group: **Participant:** [city](./interactive/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/city.ps.gz](http://trec.nist.gov/pubs/trec4/papers/city.ps.gz)
- :material-file-search: **Runs:** [cityi1](./interactive/runs.md#cityi1)

??? abstract "Abstract"
	
	City have submitted interactive runs in all the previous TRECs, with fairly undistinguished results. This time the main emphasis has been on the development of an entirely new interactive ad hoc search system (Sections 3 and Appendix). On the non-interactive side routing term selection: there has been further work on methods of selecting routing terms; manual and automatic ad hoc: the automatic ad hoc was done in more or less the same way as for TREC-3, but in view of the very brief topic statements a few runs were also done with manually edited queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonWHGP95.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonWHGP95,
		author = {Stephen E. Robertson and Steve Walker and Micheline Hancock{-}Beaulieu and Mike Gatford and A. Payne},
		editor = {Donna K. Harman},
		title = {Okapi at {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/city.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonWHGP95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Xerox Site Report: Four TREC-4 Tracks

_Marti A. Hearst, Jan O. Pedersen, Peter Pirolli, Hinrich Schütze, Gregory Grefenstette, David A. Hull_

- :fontawesome-solid-user-group: **Participant:** [xerox](./interactive/participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz](http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz)
- :material-file-search: **Runs:** [XERINT1](./interactive/runs.md#xerint1) | [XERINT2](./interactive/runs.md#xerint2)

??? abstract "Abstract"
	
	The Xerox research centers participated in four TREC-4 activities: the routing task, the filtering track, the Spanish track, and the interactive track. We addressed the core routing task as a problem in statistical classifica-tion: given a training set of judged documents, build an error-minimizing statistical classifier to assess the relevance of new test documents. This year, we built on the methodology developed in 21] by adding a combination strategy that pooled evidence across a number of separately trained classification schemes. Since many of our classifiers infer probability of relevance, adapting our routing methods to the filtering track consisted of obtaining probability estimates for the remaining classifiers and reporting those documents scoring above the probability thresholds determined by the three set linear utility func-tions. Our contribution to the Spanish track focussed on the effect of principled language analysis on a baseline retrieval system. We employed finite-state morphology [14] and hidden-Markov-model-based part-of-speech tagging 17] to analyze Spanish language text into canonical stemmed forms, and to identify verbs and noun phrases. Various combinations of these were then fed into SMART [1] for ranked retrieval. This year our activity on the ad hoc task focussed on the interactive track, which allows arbitrary user interaction in the process of finding relevant documents. We developed a graphical user interface to two interactive tools, Scatter/Gather [6] and Tilebars [11], and asked a number of subjects to use this tool to 'find as many good documents as you can for a topic, in around 30 minutes, without collecting too much rubbish'. We set up an experimental design to measure the value of each tool, and their combination, averaging out subject effects. That is, we were interested in determining how well the average user might perform with interactive tools rather than measuring the very best performance possible assuming an expert searcher. These efforts are described in more detail in the following sections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HearstPPSGH95.bib) "
	```
	@inproceedings{DBLP:conf/trec/HearstPPSGH95,
		author = {Marti A. Hearst and Jan O. Pedersen and Peter Pirolli and Hinrich Sch{\"{u}}tze and Gregory Grefenstette and David A. Hull},
		editor = {Donna K. Harman},
		title = {Xerox Site Report: Four {TREC-4} Tracks},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz},
		timestamp = {Thu, 08 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HearstPPSGH95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Highlighting Relevant Passages for Users of the Interactive SPIDER  Retrieval System

_Daniel Knaus, Elke Mittendorf, Peter Schäuble, Paraic Sheridan_

- :fontawesome-solid-user-group: **Participant:** [eth](./interactive/participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/eth.ps.gz](http://trec.nist.gov/pubs/trec4/papers/eth.ps.gz)
- :material-file-search: **Runs:** [ETHI01](./interactive/runs.md#ethi01)

??? abstract "Abstract"
	
	We report here on our participation in the 1995 Text Retrieval (TREC 4) conference. This was limited to participation in the interactive searching task due to a re-implementation of our SPIDER retrieval system. We report on two aspects of the SPIDER system that are particularly useful for interactive searching, namely the use of fast query evaluation, and the use of passage highlighting in presenting retrieved documents to users. We also report on the lessons learned from observing people interact with our system and note the challenge faced by researchers wishing to evaluate the interactive use of information retrieval systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KnausMSS95.bib) "
	```
	@inproceedings{DBLP:conf/trec/KnausMSS95,
		author = {Daniel Knaus and Elke Mittendorf and Peter Sch{\"{a}}uble and Paraic Sheridan},
		editor = {Donna K. Harman},
		title = {Highlighting Relevant Passages for Users of the Interactive {SPIDER} Retrieval System},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/eth.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KnausMSS95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLARIT TREC-4 Experiments

_David A. Evans, Natasa Milic-Frayling, Robert G. Lefferts_

- :fontawesome-solid-user-group: **Participant:** [clarit](./interactive/participants.md#clarit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/t4_proceedings.html](https://trec.nist.gov/pubs/trec4/t4_proceedings.html)
- :material-file-search: **Runs:** [CLARITI](./interactive/runs.md#clariti)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EvansML95.bib) "
	```
	@inproceedings{DBLP:conf/trec/EvansML95,
		author = {David A. Evans and Natasa Milic{-}Frayling and Robert G. Lefferts},
		editor = {Donna K. Harman},
		title = {{CLARIT} {TREC-4} Experiments},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/t4_proceedings.html},
		timestamp = {Tue, 13 Mar 2018 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EvansML95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Is Recall Relevant? An Analysis of How User Interface Conditions Affect  Strategies and Performance in Large Scale Text Retrieval

_Nipon Charoenkitkarn, Mark H. Chignell, Gene Golovchinsky_

- :fontawesome-solid-user-group: **Participant:** [utoronto](./interactive/participants.md#utoronto)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/t4_proceedings.html](https://trec.nist.gov/pubs/trec4/t4_proceedings.html)
- :material-file-search: **Runs:** [UofTo1](./interactive/runs.md#uofto1)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CharoenkitkarnCG95.bib) "
	```
	@inproceedings{DBLP:conf/trec/CharoenkitkarnCG95,
		author = {Nipon Charoenkitkarn and Mark H. Chignell and Gene Golovchinsky},
		editor = {Donna K. Harman},
		title = {Is Recall Relevant? An Analysis of How User Interface Conditions Affect Strategies and Performance in Large Scale Text Retrieval},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/t4_proceedings.html},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CharoenkitkarnCG95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Boolean System Revisited: Its Performance and its Behavior

_X. Allan Lu, John D. Holt, David J. Miller_

- :fontawesome-solid-user-group: **Participant:** [lnbool](./interactive/participants.md#lnbool)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/LexisTREC4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/LexisTREC4.ps.gz)
- :material-file-search: **Runs:** [LNBOOL](./interactive/runs.md#lnbool)

??? abstract "Abstract"
	
	This experimental study attempts to provide a general conclusion to the Boolean information retrieval system regarding its performance on retrieval effectiveness and its behavior on retrieval of different relevant documents. Specifically a representative commercial Boolean system is compared to the best ranking systems reported in TREC4. The Boolean system delivered a comparable performance and retrieved a set of rather unique relevant docu-ments. The study also justifies its methodology for comparing non-ranking and ranking systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuHM95.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuHM95,
		author = {X. Allan Lu and John D. Holt and David J. Miller},
		editor = {Donna K. Harman},
		title = {Boolean System Revisited: Its Performance and its Behavior},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/LexisTREC4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuHM95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

