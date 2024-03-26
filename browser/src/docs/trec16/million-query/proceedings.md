# Proceedings - Million Query 2007 

#### Million Query Track 2007 Overview

_James Allan, Ben Carterette, Blagovest Dachev, Javed A. Aslam, Virgiliu Pavlu, Evangelos Kanoulas_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/1MQ.OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/1MQ.OVERVIEW16.pdf)
??? abstract "Abstract"
	
	The Million Query (1MQ) track ran for the first time in TREC 2007. It was designed to serve two purposes. First, it was an exploration of ad-hoc retrieval on a large collection of documents. Second, it investigated questions of system evaluation, particularly whether it is better to evaluate using many shallow judgments or fewer thorough judgments. Participants in this track were assigned two tasks: (1) run 10,000 queries against a 426Gb collection of documents at least once and (2) judge documents for relevance with respect to some number of queries. Section 1 describes how the corpus and queries were selected, details the submission formats, and provides a brief description of all submitted runs. Section 2 provides an overview of the judging process, including a sketch of how it alternated between two methods for selecting the small set of documents to be judged. Sections 3 and 4 provide details of those two selection methods, developed at UMass and NEU, respectively. The sections also provide some analysis of the results. In Section 6 we present some statistics about the judging process, such as the total number of queries judged, how many by each approach, and so on. We present some additional results and analysis of the overall track in Sections 7 and 8.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCDAPK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCDAPK07,
		author = {James Allan and Ben Carterette and Blagovest Dachev and Javed A. Aslam and Virgiliu Pavlu and Evangelos Kanoulas},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Million Query Track 2007 Overview},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/1MQ.OVERVIEW16.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCDAPK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Hedge Algorithm for Metasearch at TREC 2007

_Javed A. Aslam, Virgiliu Pavlu, Olena Zubaryeva_

- :fontawesome-solid-user-group: **Participant:** [northeasteru.aslam](./participants.md#northeasteru.aslam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/northeasternu.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/northeasternu.mq.final.pdf)
- :material-file-search: **Runs:** [hedge0](./runs.md#hedge0)

??? abstract "Abstract"
	
	Aslam, Pavlu, and Savell [3] introduced the Hedge algorithm for metasearch which effectively combines the ranked lists of documents returned by multiple retrieval systems in response to a given query. It has been demonstrated that the Hedge algorithm is an effective technique for metasearch, often significantly exceeding the performance of standard metasearch and IR techniques over small TREC collections. In this work, we explore the effectiveness of Hedge as an automatic metasearch engine over the much larger GOV2 collection on about 1700 topics as part of the Million Query Track of TREC 2007.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AslamPZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/AslamPZ07,
		author = {Javed A. Aslam and Virgiliu Pavlu and Olena Zubaryeva},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Hedge Algorithm for Metasearch at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/northeasternu.mq.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AslamPZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Lucene and Juru at TREC 2007: 1-Million Queries Track

_Doron Cohen, Einat Amitay, David Carmel_

- :fontawesome-solid-user-group: **Participant:** [ibm.carmel](./participants.md#ibm.carmel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ibm-haifa.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ibm-haifa.mq.final.pdf)
- :material-file-search: **Runs:** [LucSynEx](./runs.md#lucsynex) | [LucSpel0](./runs.md#lucspel0) | [JuruSynE](./runs.md#jurusyne) | [LucSyn0](./runs.md#lucsyn0)

??? abstract "Abstract"
	
	Lucene is an increasingly popular open source search library. However, our experiments of search quality for TREC data and evaluations for out-of-the-box Lucene indicated inferior quality comparing to other systems participating in TREC. In this work we investigate the differences in measured search quality between Lucene and Juru, our home-brewed search engine, and show how Lucene scoring can be modified to improve its measured search quality for TREC. Our scoring modifications to Lucene were trained over the 150 topics of the tera-byte tracks. Evaluations of these modifications with the new - sample based - 1-Million Queries Track measures - NEU-Map and epsilon-Map - indicate the robustness of the scoring modifications: modified Lucene performs well when compared to stock Lucene and when compared to other systems that participated in the 1-Million Queries Track this year, both for the training set of 150 queries and for the new measures. As such, this also supports the robustness of the new measures tested in this track. This work reports our experiments and results and describes the modifications involved - namely normalizing term frequencies, different choice of document length normalization, phrase expansion and proximity scoring.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CohenAC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/CohenAC07,
		author = {Doron Cohen and Einat Amitay and David Carmel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Lucene and Juru at {TREC} 2007: 1-Million Queries Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ibm-haifa.mq.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CohenAC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Collection Selection Based on Historical Performance for Efficient  Processing

_Christopher T. Fallen, Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [ualaska.newby](./participants.md#ualaska.newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ualaska.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ualaska.mq.final.pdf)
- :material-file-search: **Runs:** [ffind07d](./runs.md#ffind07d) | [ffind07c](./runs.md#ffind07c)

??? abstract "Abstract"
	
	A Grid Information Retrieval (GIR) simulation was used to process the TREC Million Query Track queries. The GOV2 collection was partitioned by hostname and the aggregate performance of each host, as measured by qrel counts from the past TREC Terabyte Tracks, was used to rank the hosts in order of quality. Only the 100 highest quality hosts were included in the Grid IR simulation, representing less than 20% of all GOV2 documents. The IR performance of the GIR simulation, as measured by the topic-averaged AP, b-pref, and Rel@10 over the TREC Terabyte-Track topics is within one standard deviation of the respective topic-averaged TREC Million Query participant median scores. Estimated AP of the Million Query topic results is comparable to the topic-averaged AP of the Terabyte topic results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FallenN07.bib) "
	```
	@inproceedings{DBLP:conf/trec/FallenN07,
		author = {Christopher T. Fallen and Gregory B. Newby},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Collection Selection Based on Historical Performance for Efficient Processing},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ualaska.mq.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FallenN07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Parsimonious Language Models for a Terabyte of Text

_Djoerd Hiemstra, Rongmei Li, Jaap Kamps, Rianne Kaptein_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.deRijke](./participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uamsterdam-derijke.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uamsterdam-derijke.mq.final.pdf)
- :material-file-search: **Runs:** [UAmsT06tTeLM](./runs.md#uamst06ttelm) | [UAmsT06tAnLM](./runs.md#uamst06tanlm) | [UAmsT06tTeVS](./runs.md#uamst06ttevs) | [UAmsT06tTiLM](./runs.md#uamst06ttilm) | [UAmsT06tAnVS](./runs.md#uamst06tanvs) | [UAmsT07MTiLM](./runs.md#uamst07mtilm) | [UAmsT07MAnLM](./runs.md#uamst07manlm) | [UAmsT07MSum8](./runs.md#uamst07msum8) | [UAmsT07MSum6](./runs.md#uamst07msum6) | [UAmsT07MTeVS](./runs.md#uamst07mtevs) | [UAmsT07MTeLM](./runs.md#uamst07mtelm) | [UAmsT07MSm8L](./runs.md#uamst07msm8l)

??? abstract "Abstract"
	
	The aims of this paper are twofold. Our first aim is to compare results of the earlier Terabyte tracks to the Million Query track. We submitted a number of runs using different document representations (such as full-text, title-fields, or incoming anchor-texts) to increase pool diversity. The initial results show broad agreement in system rankings over various measures on topic sets judged at both Terabyte and Million Query tracks, with runs using the full-text index giving superior results on all measures, but also some noteworthy upsets. Our second aim is to explore the use of parsimonious language models for retrieval on terabyte-scale collections. These models are smaller thus more efficient than the standard language models when used at indexing time, and they may also improve retrieval performance. We have conducted initial experiments using parsimonious models in combination with pseudo-relevance feedback, for both the Terabyte and Million Query track topic sets, and obtained promising initial results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HiemstraLKK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HiemstraLKK07,
		author = {Djoerd Hiemstra and Rongmei Li and Jaap Kamps and Rianne Kaptein},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Parsimonious Language Models for a Terabyte of Text},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uamsterdam-derijke.mq.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HiemstraLKK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exegy at TREC 2007 Million Query Track

_Naveen Singla, Ronald S. Indeck_

- :fontawesome-solid-user-group: **Participant:** [exegy.indeck](./participants.md#exegy.indeck)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/exegy.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/exegy.mq.final.pdf)
- :material-file-search: **Runs:** [exegyexact](./runs.md#exegyexact)

??? abstract "Abstract"
	
	Exegy's submission for the TREC 2007 million query track consisted of results obtained by running the queries against the raw data, i.e., the data was not indexed. The hardware-accelerated streaming engine used to perform the search is the Exegy Text Miner (XTM), developed at Exegy, Inc. The search engine's architecture is novel: XTM is a hybrid system (heterogeneous compute platform) employing general purpose processors (GPPs) and field programmable gate arrays (FPGAs) in a hardware-software co-design architecture to perform the search. The GPPs are responsible for inputting the data to the FPGAs and reading and post-processing the search results that the FPGAs output. The FPGAs perform the actual search and due to the high degree of parallelism available (including pipelining) are able to do so much more efficiently than the GPPs. For the million query track the results for a particular query were obtained by searching for the exact query string within the corpus. This brute force approach, although naive, returned relevant results for most of the queries. The mean-average precision for the results is 0.3106 and 0.0529 using the UMass and the NEU evaluation tools, respectively. More importantly, XTM completed the search for the entire set of the 10,000 queries on the unindexed data in less than two and a half hours.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinglaI07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinglaI07,
		author = {Naveen Singla and Ronald S. Indeck},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exegy at {TREC} 2007 Million Query Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/exegy.mq.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SinglaI07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Indri at TREC 2007: Million Query (1MQ) Track

_Xing Yi, James Allan_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umass.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umass.mq.final.pdf)
- :material-file-search: **Runs:** [indriQL](./runs.md#indriql) | [indriQLSC](./runs.md#indriqlsc) | [indriDMCSC](./runs.md#indridmcsc) | [indriDM](./runs.md#indridm)

??? abstract "Abstract"
	
	This work details the experiments carried out using the Indri search engine for the ad hoc retrieval task in the TREC 2007 Million Query Track. We investigate using proximity features for this task, and also explore whether using a simple spelling checker - Aspell to correct plausible spelling errors in the noisy queries could help retrieval. Results evaluated by three different approaches are presented. The strength and weakness of introducing Aspell for IR are discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YiA07.bib) "
	```
	@inproceedings{DBLP:conf/trec/YiA07,
		author = {Xing Yi and James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Indri at {TREC} 2007: Million Query {(1MQ)} Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/umass.mq.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YiA07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

