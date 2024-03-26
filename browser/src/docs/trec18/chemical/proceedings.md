# Proceedings - Chemical 2009 

#### Overview of the TREC 2009 Chemical IR Track

_Mihai Lupu, Florina Piroi, Xiangji Huang, Jianhan Zhu, John Tait_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/CHEM09.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/CHEM09.OVERVIEW.pdf)
??? abstract "Abstract"
	
	TREC 2009 was the first year of the Chemical IR Track, which focuses on evaluation of search techniques for discovery of digitally stored information on chemical patents and academic journal articles. The track included two tasks: Prior Art (PA) and Technical Survey (TS) tasks. This paper describes how we designed the two tasks and presents the official results of eight participating groups.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LupuPHZT09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LupuPHZT09,
		author = {Mihai Lupu and Florina Piroi and Xiangji Huang and Jianhan Zhu and John Tait},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2009 Chemical {IR} Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/CHEM09.OVERVIEW.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LupuPHZT09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Strategies for Effective Chemical Information Retrieval

_Suleyman Cetintas, Luo Si_

- :fontawesome-solid-user-group: **Participant:** [Purdue_Si](./participants.md#purdue_si)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/purdue.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/purdue.CHEM.pdf)
- :material-file-search: **Runs:** [purdueTS09r1](./runs.md#purduets09r1) | [purduePA09r1](./runs.md#purduepa09r1) | [purduePA09r2](./runs.md#purduepa09r2)

??? abstract "Abstract"
	
	We participated in the technology survey and prior art search subtasks of the TREC 2009 Chemical IR Track. This paper describes the methods developed for these two tasks. For the technology survey task, we propose a method that constructs highly structured queries to do retrieval on different fields of chemical patents and documents in a weighted way. The proposed method i) enriches these structured queries with synonyms of the chemicals that have been identified, and ii) uses simple entity recognition to extract information for increasing or decreasing weights of some terms and to filter out documents from the ranked list. For prior art search task; we propose an automated query generation method that uses all title words, and selects sets of terms from the claims, abstract and description fields of query patents to transform a query patent into a search query. From the selected terms, chemical entities are extracted and synonyms for the identified chemical entities are included from PubChem. Then structured queries are formed to do retrieval over different fields of documents with different weights. Furthermore a post-processing step is also proposed that i) filters out some of the retrieved documents from the ranked list because of date constraints and ii) utilizes the IPC similarities between query patent and its retrieved patents to re-rank the retrieved documents. Empirical results demonstrate the effectiveness of these methods in both tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CetintasS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CetintasS09,
		author = {Suleyman Cetintas and Luo Si},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Strategies for Effective Chemical Information Retrieval},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/purdue.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CetintasS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2009 Experiments: Chemical IR Track

_Julien Gobeill, Douglas Teodoro, Emilie Pasche, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BITEM](./participants.md#bitem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/bitem.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/bitem.CHEM.pdf)
- :material-file-search: **Runs:** [BiTeM09](./runs.md#bitem09) | [BiTeM09po](./runs.md#bitem09po) | [BiTeM09qe](./runs.md#bitem09qe) | [BiTeM09qepo](./runs.md#bitem09qepo) | [BiTeM09comb](./runs.md#bitem09comb) | [BiTeM09ipc1](./runs.md#bitem09ipc1) | [BiTeM09ipc3](./runs.md#bitem09ipc3) | [BiTeM09ipc5](./runs.md#bitem09ipc5) | [BiTeM09ipc3b](./runs.md#bitem09ipc3b) | [BiTeM09PAbl](./runs.md#bitem09pabl) | [BiTeM09PAcit](./runs.md#bitem09pacit) | [BiTeM09PAcl](./runs.md#bitem09pacl) | [BiTeM09PAqe](./runs.md#bitem09paqe) | [BiTeM09PAcba](./runs.md#bitem09pacba) | [BiTeM09PAcbb](./runs.md#bitem09pacbb)

??? abstract "Abstract"
	
	The goal of the first TREC Chemical track was to retrieve documents relevant to a given patent query, within a large collection of patents in chemistry. Regarding this objective, for the Prior Art subtask, our runs performed significantly better that runs submitted by other participating teams. Baseline retrieval methods achieved relatively poor performances (Mean Average Precision = 0.067). Query expansion, driven my chemical named entity recognition resulted in some modest improvement (+2 to 3%). Filtering based on IPC codes did not result in any significant improvement. A re-ranking strategy, based on claims only improved MAP by about 3%. The most effective gain was obtained by using patent citation patterns. Somehow similar to feed-back but restricted to citations, we used patents cited in the retrieved patents in order to boost the retrieval status value of the baseline run. This strategy led to a remarkable improvement (MAP 0.18, +168 %). Nevertheless, as official topics were sampled from the collection disregarding their creation date, our strategy happened to exploit citations of patents which were patented after the topic itself. From a user perspective, such a setting is questionable. We think that future TREC-CHEM competitions should address this issue by using patents filed as recently as possible.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GobeillTPR09.bib) "
	```
	@inproceedings{DBLP:conf/trec/GobeillTPR09,
		author = {Julien Gobeill and Douglas Teodoro and Emilie Pasche and Patrick Ruch},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2009 Experiments: Chemical {IR} Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/bitem.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GobeillTPR09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Patent Retrieval in Chemistry Based on Semantically Tagged Named Entities

_Harsha Gurulingappa, Bernd Müller, Roman Klinger, Heinz-Theodor Mevissen, Martin Hofmann-Apitius, Juliane Fluck, Christoph M. Friedrich_

- :fontawesome-solid-user-group: **Participant:** [NERCHEM116](./participants.md#nerchem116)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/scai.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/scai.CHEM.pdf)
- :material-file-search: **Runs:** [SCAI09TSNP](./runs.md#scai09tsnp) | [SCAI09TSMAN](./runs.md#scai09tsman) | [SCAI09TSPM](./runs.md#scai09tspm) | [SCAI09PAt2a](./runs.md#scai09pat2a) | [SCAI09PAf2a](./runs.md#scai09paf2a) | [SCAI09PAt2b](./runs.md#scai09pat2b) | [SCAI09PAf2b](./runs.md#scai09paf2b) | [SCAI09PAt2c](./runs.md#scai09pat2c) | [SCAI09PAf2c](./runs.md#scai09paf2c) | [SCAI09PAt2d](./runs.md#scai09pat2d) | [SCAI09PAf2d](./runs.md#scai09paf2d) | [SCAI09PAt2e](./runs.md#scai09pat2e) | [SCAI09PAf2e](./runs.md#scai09paf2e) | [SCAI09PAt1a](./runs.md#scai09pat1a) | [SCAI09PAf1a](./runs.md#scai09paf1a) | [SCAI09PAt1b](./runs.md#scai09pat1b) | [SCAI09PAf1b](./runs.md#scai09paf1b) | [SCAI09PAt1c](./runs.md#scai09pat1c) | [SCAI09PAf1c](./runs.md#scai09paf1c) | [SCAI09PAt1d](./runs.md#scai09pat1d) | [SCAI09PAf1d](./runs.md#scai09paf1d) | [SCAI09PAt1e](./runs.md#scai09pat1e) | [SCAI09PAf1e](./runs.md#scai09paf1e) | [SCAI09PAt3a](./runs.md#scai09pat3a) | [SCAI09PAf3a](./runs.md#scai09paf3a) | [SCAI09PAt3b](./runs.md#scai09pat3b) | [SCAI09PAf3b](./runs.md#scai09paf3b) | [SCAI09PAt3c](./runs.md#scai09pat3c) | [SCAI09PAf3c](./runs.md#scai09paf3c) | [SCAI09PAt3d](./runs.md#scai09pat3d) | [SCAI09PAf3d](./runs.md#scai09paf3d) | [SCAI09PAt3e](./runs.md#scai09pat3e) | [SCAI09PAf3e](./runs.md#scai09paf3e) | [SCAI09PAt4a](./runs.md#scai09pat4a) | [SCAI09PAf4a](./runs.md#scai09paf4a) | [SCAI09PAt4c](./runs.md#scai09pat4c) | [SCAI09PAf4c](./runs.md#scai09paf4c) | [SCAI09PAt4b](./runs.md#scai09pat4b) | [SCAI09PAf4b](./runs.md#scai09paf4b)

??? abstract "Abstract"
	
	This paper reports on the work that has been conducted by Fraunhofer SCAI for Trec Chemistry (Trec-Chem) track 2009. The team of Fraunhofer SCAI participated in two tasks, namely Technology Survey and Prior Art Search. The core of the framework is an index of 1.2 million chemical patents provided as a data set by Trec. For the technology survey, three runs were submitted based on semantic dictionaries and noun phrases. For the prior art search task, several fields were introduced into the index that contained normalized noun phrases, biomedical as well as chemical entities. Altogether, 36 runs were submitted for this task that were based on automatic querying with tokens, noun phrases and entities along with different search strategies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GurulingappaMKMHFF09.bib) "
	```
	@inproceedings{DBLP:conf/trec/GurulingappaMKMHFF09,
		author = {Harsha Gurulingappa and Bernd M{\"{u}}ller and Roman Klinger and Heinz{-}Theodor Mevissen and Martin Hofmann{-}Apitius and Juliane Fluck and Christoph M. Friedrich},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Patent Retrieval in Chemistry Based on Semantically Tagged Named Entities},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/scai.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GurulingappaMKMHFF09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2009: Chemical IR Track

_Song Jin, Zheng Ye, Hongfei Lin_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./participants.md#dutir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/dalianu.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/dalianu.CHEM.pdf)
- :material-file-search: **Runs:** [DUT09TSRun1](./runs.md#dut09tsrun1) | [DUT09TSRun2](./runs.md#dut09tsrun2) | [DUT09TSRun3](./runs.md#dut09tsrun3) | [DUT09TSRun4](./runs.md#dut09tsrun4) | [DUT09TSRun6](./runs.md#dut09tsrun6) | [DUTIR09BM25F](./runs.md#dutir09bm25f) | [DUTIRRun1](./runs.md#dutirrun1) | [DUTIRRun2](./runs.md#dutirrun2) | [DUTIRRun3](./runs.md#dutirrun3)

??? abstract "Abstract"
	
	This paper presents the DUTIR submission to TREC 2009 Chemical IR Track. This track included two tasks: Prior Art (PA) and Technical Survey (TS) tasks. We present a series of experiments on two text retrieval models, BM25 and Language Model for IR (LMIR). For Prior Art task, we focused on formulating the queries from the query patents and date filtering. Moreover, some traditional search techniques are used for Technical Survey task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JinYL09.bib) "
	```
	@inproceedings{DBLP:conf/trec/JinYL09,
		author = {Song Jin and Zheng Ye and Hongfei Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2009: Chemical {IR} Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/dalianu.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JinYL09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Blog and TREC Chem: A View from the Corn Fields

_Yelena Mejova, Viet Ha-Thuc, Steven Foster, Christopher G. Harris, Robert J. Arens, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [IowaS](./participants.md#iowas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf)
- :material-file-search: **Runs:** [UIowaS09PA1](./runs.md#uiowas09pa1) | [UIowaS09PA2](./runs.md#uiowas09pa2) | [UIowaS09PA3](./runs.md#uiowas09pa3)

??? abstract "Abstract"
	
	The University of Iowa Team, participated in the blog track and the chemistry track of TREC-2009. This is our first year participating in the blog track as well as the chemistry track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MejovaHFHAS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/MejovaHFHAS09,
		author = {Yelena Mejova and Viet Ha{-}Thuc and Steven Foster and Christopher G. Harris and Robert J. Arens and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Blog and {TREC} Chem: {A} View from the Corn Fields},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MejovaHFHAS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Chemical IR Track 2009: A Distributed Dimensional Indexing  Model for Chemical Patent Search

_Jay Urbain, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [msoe](./participants.md#msoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/milwaukee.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/milwaukee.CHEM.pdf)
- :material-file-search: **Runs:** [msoe09TSx1](./runs.md#msoe09tsx1) | [msoe09TSx2](./runs.md#msoe09tsx2) | [msoe09TSx3](./runs.md#msoe09tsx3) | [msoe09TSx4](./runs.md#msoe09tsx4) | [msoe09TSx5](./runs.md#msoe09tsx5) | [msoe09TSx1ta](./runs.md#msoe09tsx1ta) | [msoe09TSx2ta](./runs.md#msoe09tsx2ta) | [msoe09TSx3ta](./runs.md#msoe09tsx3ta) | [msoe09TSx4ta](./runs.md#msoe09tsx4ta) | [msoe09TSx5ta](./runs.md#msoe09tsx5ta)

??? abstract "Abstract"
	
	For the TREC-2009 Chemical IR Track, we explore development of a distributed information retrieval system based on a dimensional data model. The indexing model supports named entity identification and aggregation of term statistics at multiple levels of patent structure including individual words, sentences, claims, descriptions, abstracts, and titles. The system was deployed across 15 Amazon Web Services (AWS) Elastic Cloud Compute (EC2) instances and 15 Elastic Block Storage (EBS) database shards to support efficient indexing and query processing of the relatively large index generated from indexing each individual word (sans stop words) in the 100G+ collection of chemical patent documents. The query processing algorithm for technology survey search and prior art search uses information extraction techniques and locally aggregated term statistics to help disambiguate candidate entities and terms in context. Query processing for prior art search automatically generates a structured query based on the relative distinctiveness of individual terms and candidate entity phrases from the query patent's claims, abstract, and title sections. For both the technology survey and prior art search, we evaluated several probabilistic retrieval functions for integrating statistics of retrieved named entities with term statistics at multiple levels of document structure to identify relevant patents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UrbainF09.bib) "
	```
	@inproceedings{DBLP:conf/trec/UrbainF09,
		author = {Jay Urbain and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Chemical {IR} Track 2009: {A} Distributed Dimensional Indexing Model for Chemical Patent Search},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/milwaukee.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UrbainF09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Formulating Simple Structured Queries Using Temporal and Distributional  Cues in Patents

_Le Zhao, James P. Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU_LIRA](./participants.md#cmu_lira)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/cmu.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/cmu.CHEM.pdf)
- :material-file-search: **Runs:** [CMU09Chmtcd](./runs.md#cmu09chmtcd) | [CMU09Chmtcdd](./runs.md#cmu09chmtcdd)

??? abstract "Abstract"
	
	Patent prior art retrieval aims to find related publications, especially patents, which may invalidate the patent. The task exhibits its own characteristic because of the possible use of a whole patent as a query. This work focuses on the use of date fields and content fields of the query patent to formulate effective structured queries. Retrieval is performed on the collection of patents which also share the same structure as the query patent, mainly priority dates, application date, publication date and content fields. Unsurprisingly, results show that filtering using date information improves retrieval significantly. However, results also show that a careful choice of the date filter is important, given the multiple date fields existent in a patent. The actual ranking query is constructed based on word distributions of title, claims and content fields of the query patent. The overall MAP of this citation finding task is still in the lower 0.1 range. An error analysis focusing on the lower performing topics finds that the citation finding task (given publication recommend citations, which is a very similar setup as this year's prior art evaluation) can be very different from the prior art task (finding patents that invalidates the query patent). It raises the concern that just the citations included in query patents can be a biased and incomplete set of relevance judgements for the prior art task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoC09,
		author = {Le Zhao and James P. Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Formulating Simple Structured Queries Using Temporal and Distributional Cues in Patents},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/cmu.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2009: Chemical Track

_Jiashu Zhao, Xiangji Huang, Zheng Ye, Jianhan Zhu_

- :fontawesome-solid-user-group: **Participant:** [york09](./participants.md#york09)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/yorku.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/yorku.CHEM.pdf)
- :material-file-search: **Runs:** [york09ca03](./runs.md#york09ca03) | [york09ca04](./runs.md#york09ca04) | [york09ca05](./runs.md#york09ca05) | [york09ca06](./runs.md#york09ca06) | [york09ca02](./runs.md#york09ca02) | [york09ca07](./runs.md#york09ca07) | [york09ca08](./runs.md#york09ca08) | [york09caPA01](./runs.md#york09capa01) | [york09caPA03](./runs.md#york09capa03)

??? abstract "Abstract"
	
	Our chemical experiments mainly focus on addressing three major problems in two chemical information retrieval tasks, Technology Survey (TS) task and Prior Art (PA) task. The three problems are: (1) how to deal with chemical terminology synonyms? (2) how to deal with chemical terminology abbreviation? (3) how to deal with long queries in Prior Art (PA) task? In particular, we propose a query expansion algorithm for TS task and a keyword-selection algorithm for PA task. The Mean Average Precision (MAP) for our TS task run “york09ca07” using Algorithm 1 was 0.2519 and for our PA task run “york09caPA01” using Algorithm 2 was 0.0566. The evaluation results show that both algorithms are effective for improving retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoHYYZ09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoHYYZ09,
		author = {Jiashu Zhao and Xiangji Huang and Zheng Ye and Jianhan Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2009: Chemical Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/yorku.CHEM.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoHYYZ09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

