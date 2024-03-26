# Proceedings 2007 

## Overview of TREC 2007

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/OVERVIEW16.pdf)
??? abstract "Abstract"
	
	The sixteenth Text REtrieval Conference, TREC 2007, was held at the National Institute of Standards and Technology (NIST) November 6-9, 2007. The conference was co-sponsored by NIST and the Intelligence Advanced Research Projects Activity (IARPA). TREC 2007 had 95 participating groups from 18 countries. Table 2 at the end of the paper lists the participating groups. TREC 2007 is the latest in a series of workshops designed to foster research on technologies for information retrieval. The workshop series has four goals: to encourage retrieval research based on large test collections; to increase communication among industry, academia, and government by creating an open forum for the exchange of research ideas; to speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems; and to increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current systems. TREC 2007 contained seven areas of focus called “tracks”. Six of the tracks ran in previous TRECs and explored tasks in question answering, blog search, detecting spam in an email stream, enterprise search, search in support of legal discovery, and information access within the genomics domain. A new track called the million query track investigated techniques for building fair retrieval test collections for very large corpora. This paper serves as an introduction to the research described in detail in the remainder of the proceedings. The next section provides a summary of the retrieval background knowledge that is assumed in the other papers. Section 3 presents a short description of each track—a more complete description of a track can be found in that track's overview paper in the proceedings. The final section looks toward future TREC conferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees07.bib)"
	```
	@inproceedings{DBLP:conf/trec/Voorhees07,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/OVERVIEW16.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Million Query 

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

- :fontawesome-solid-user-group: **Participant:** [northeasteru.aslam](./million-query/participants.md#northeasteru.aslam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/northeasternu.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/northeasternu.mq.final.pdf)
- :material-file-search: **Runs:** [hedge0](./million-query/runs.md#hedge0)

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

- :fontawesome-solid-user-group: **Participant:** [ibm.carmel](./million-query/participants.md#ibm.carmel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ibm-haifa.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ibm-haifa.mq.final.pdf)
- :material-file-search: **Runs:** [LucSynEx](./million-query/runs.md#lucsynex) | [LucSpel0](./million-query/runs.md#lucspel0) | [JuruSynE](./million-query/runs.md#jurusyne) | [LucSyn0](./million-query/runs.md#lucsyn0)

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

- :fontawesome-solid-user-group: **Participant:** [ualaska.newby](./million-query/participants.md#ualaska.newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ualaska.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ualaska.mq.final.pdf)
- :material-file-search: **Runs:** [ffind07d](./million-query/runs.md#ffind07d) | [ffind07c](./million-query/runs.md#ffind07c)

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

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.deRijke](./million-query/participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uamsterdam-derijke.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uamsterdam-derijke.mq.final.pdf)
- :material-file-search: **Runs:** [UAmsT06tTeLM](./million-query/runs.md#uamst06ttelm) | [UAmsT06tAnLM](./million-query/runs.md#uamst06tanlm) | [UAmsT06tTeVS](./million-query/runs.md#uamst06ttevs) | [UAmsT06tTiLM](./million-query/runs.md#uamst06ttilm) | [UAmsT06tAnVS](./million-query/runs.md#uamst06tanvs) | [UAmsT07MTiLM](./million-query/runs.md#uamst07mtilm) | [UAmsT07MAnLM](./million-query/runs.md#uamst07manlm) | [UAmsT07MSum8](./million-query/runs.md#uamst07msum8) | [UAmsT07MSum6](./million-query/runs.md#uamst07msum6) | [UAmsT07MTeVS](./million-query/runs.md#uamst07mtevs) | [UAmsT07MTeLM](./million-query/runs.md#uamst07mtelm) | [UAmsT07MSm8L](./million-query/runs.md#uamst07msm8l)

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

- :fontawesome-solid-user-group: **Participant:** [exegy.indeck](./million-query/participants.md#exegy.indeck)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/exegy.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/exegy.mq.final.pdf)
- :material-file-search: **Runs:** [exegyexact](./million-query/runs.md#exegyexact)

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

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./million-query/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umass.mq.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umass.mq.final.pdf)
- :material-file-search: **Runs:** [indriQL](./million-query/runs.md#indriql) | [indriQLSC](./million-query/runs.md#indriqlsc) | [indriDMCSC](./million-query/runs.md#indridmcsc) | [indriDM](./million-query/runs.md#indridm)

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

## Genomics 

#### TREC 2007 Genomics Track Overview

_William R. Hersh, Aaron M. Cohen, Lynn Ruslen, Phoebe M. Roberts_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/GEO.OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/GEO.OVERVIEW16.pdf)
??? abstract "Abstract"
	
	The TREC 2007 Genomics Track employed an entity-based question-answering task. Runs were required to nominate passages of text from a collection of full-text biomedical journal articles to answer the topic questions. Systems were assessed not only for the relevance of passages retrieved, but also how many aspects (entities) of the topic were covered and how many relevant documents were retrieved. We also classified the features of runs to explore which ones were associated with better performance, although the diversity of approaches and the quality of their reporting prevented definitive conclusions from being drawn.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershCRR07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershCRR07,
		author = {William R. Hersh and Aaron M. Cohen and Lynn Ruslen and Phoebe M. Roberts},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 Genomics Track Overview},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/GEO.OVERVIEW16.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershCRR07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The OHSU Biomedical Question Answering System Framework

_Aaron M. Cohen, Jianji Yang, Seeger Fisher, Brian Roark, William R. Hersh_

- :fontawesome-solid-user-group: **Participant:** [ohsu.hersh](./genomics/participants.md#ohsu.hersh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ohsu.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ohsu.geo.final.pdf)
- :material-file-search: **Runs:** [OHSUQASUBEX](./genomics/runs.md#ohsuqasubex) | [OHSUQASUB](./genomics/runs.md#ohsuqasub) | [OHSUQA](./genomics/runs.md#ohsuqa)

??? abstract "Abstract"
	
	The Oregon Health & Science University submission to the TREC 2007 Genomics Track approached the entity list question answering task using a modular object oriented system framework. A system object coordinates a collection of processing objects into a pipe that constructs a set of queries, retrieves passage, and then processes those passages into a final output answer set. Using the framework we applied multiple levels of synonym expansion and a ranked series of topic queries with a range of specificities in order to retrieve all of the likely relevant passages with the most likely ranked higher. We then applied sentence pruning to the head and tail of each passage using both NLP and term-based techniques. Overall scores finished around the TREC Genomics mean for each of the four measures. Careful passage retrieval, including synonym expansion and multiple query construction, as well as sentence pruning was essential in achieving acceptable performance on this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CohenYFRH07.bib) "
	```
	@inproceedings{DBLP:conf/trec/CohenYFRH07,
		author = {Aaron M. Cohen and Jianji Yang and Seeger Fisher and Brian Roark and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {OHSU} Biomedical Question Answering System Framework},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ohsu.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CohenYFRH07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Resources to Find Answers to Biomedical Questions

_Dina Demner-Fushman, Susanne M. Humphrey, Nicholas C. Ide, Russell F. Loane, James G. Mork, Patrick Ruch, Miguel E. Ruiz, Lawrence H. Smith, W. John Wilbur, Alan R. Aronson_

- :fontawesome-solid-user-group: **Participant:** [nlm.aronson](./genomics/participants.md#nlm.aronson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/nlm.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/nlm.geo.final.pdf)
- :material-file-search: **Runs:** [LHNCBC](./genomics/runs.md#lhncbc) | [NLMfusion](./genomics/runs.md#nlmfusion) | [NLMinter](./genomics/runs.md#nlminter)

??? abstract "Abstract"
	
	One of the NLM experimental approaches to the 2007 Genomics track question answering task followed the track evaluation design: we attempted identifying exact answers in the form of semantic relations between biomedical entities named in questions and the potential answer types and then marked the passages containing the relations as containing the answers. The goal of this knowledge-based approach was to improve the answer precision. To boost recall, evidence obtained through relation extraction was combined with passage scores obtained by semantic filtering and passage retrieval. Our second approach, the fusion of retrieval results of several search engines established to be reliably successful in the past, was used as the baseline, which ultimately was not improved upon by the knowledge-based approach. The impact of the relevance of whole documents on finding passages containing answers was tested in the third approach, an interactive retrieval experiment, in which the relevance of a document was determined by virtue of its retrieval in an expert PubMed search and an occasional examination of its abstract. This relatively moderately labor-intensive approach significantly improved the fusion retrieval results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Demner-FushmanHILMRRSWA07.bib) "
	```
	@inproceedings{DBLP:conf/trec/Demner-FushmanHILMRRSWA07,
		author = {Dina Demner{-}Fushman and Susanne M. Humphrey and Nicholas C. Ide and Russell F. Loane and James G. Mork and Patrick Ruch and Miguel E. Ruiz and Lawrence H. Smith and W. John Wilbur and Alan R. Aronson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Resources to Find Answers to Biomedical Questions},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/nlm.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Demner-FushmanHILMRRSWA07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IR-Specific Searches at TREC 2007: Genomics & Blog Experiments

_Claire Fautsch, Jacques Savoy_

- :fontawesome-solid-user-group: **Participant:** [uneuchatel.savoy](./genomics/participants.md#uneuchatel.savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf)
- :material-file-search: **Runs:** [UniNE1](./genomics/runs.md#unine1) | [UniNE2](./genomics/runs.md#unine2) | [UniNE3](./genomics/runs.md#unine3)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2007 Genomics and Blog evaluation campaigns. Within these two tracks, our main intent is to go beyond simple document retrieval, using different search and filtering strategies to obtain more specific answers to user information needs. In the Genomics track, the dedicated IR system has to extract relevant text passages in support of precise user questions. This task may also be viewed as the first stage of a Question/Answering system. In the Blog track we explore various strategies for retrieving opinions from the blogsphere, which in this case involves subjective opinions about various targets entities (e.g., person, location, organization, event, product or technology). This task can be subdivided in two parts: 1) retrieve relevant information (facts) and 2) extract positive, negative or mixed opinions about the specific entity being targeted. To achieve these objectives we evaluate retrieval effectiveness using the Okapi (BM25) and various other models derived from the Divergence from Randomness (DFR) paradigm, as well as a language model (LM). Through our experiments with the Genomics corpus we find that the DFR models perform clearly better than the Okapi model (relative difference of 70%) in terms of mean average precision (MAP). Using the blog corpus, we found the opposite; the Okapi model performs slightly better than both DFR models (relative difference around 5%) and LM (relative difference 7%) model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FautschS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/FautschS07,
		author = {Claire Fautsch and Jacques Savoy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IR-Specific Searches at {TREC} 2007: Genomics {\&} Blog Experiments},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FautschS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Vocabulary-Driven Passage Retrieval for Question-Answering in Genomics

_Julien Gobeill, Imad Tbahriti, Frédéric Ehrler, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [uhosp-geneva.ruch](./genomics/participants.md#uhosp-geneva.ruch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uhosp-geneva.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uhosp-geneva.geo.final.pdf)
- :material-file-search: **Runs:** [GenTeam1](./genomics/runs.md#genteam1) | [GenTeaBB](./genomics/runs.md#genteabb) | [GenTeaPA](./genomics/runs.md#genteapa)

??? abstract "Abstract"
	
	This year, like in 2006, we use a collection of about 160000 full-text articles. The proposed task is a passage retrieval task. Several measures are applied on the returned data: passage mean average precision, document mean average precision, aspect mean average precision. This year, our efforts concentrated on combining knowledge-driven methods on top of a standard vector-space retrieval approach. We tested a passage selection methods based on vocabulary density estimation using several terminologies of the domain. We also attempted to improve standard retrieval approaches based on vector-space similarities by using a Boolean completion principle, which overweight documents containing all keywords. These combinations did not result in a significant improvement compared to the baseline system (document map ~ 0.20) and current results do not show much improvement compared to last year's reported results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GobeillTER07.bib) "
	```
	@inproceedings{DBLP:conf/trec/GobeillTER07,
		author = {Julien Gobeill and Imad Tbahriti and Fr{\'{e}}d{\'{e}}ric Ehrler and Patrick Ruch},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Vocabulary-Driven Passage Retrieval for Question-Answering in Genomics},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uhosp-geneva.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GobeillTER07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2007: Genomics Track

_Xiangji Huang, Damon Sotoudeh-Hosseinii, Hashmat Rohian, Xiangdong An_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./genomics/participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/yorku.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/yorku.geo.final.pdf)
- :material-file-search: **Runs:** [york07ga1](./genomics/runs.md#york07ga1) | [york07ga2](./genomics/runs.md#york07ga2) | [york07ga3](./genomics/runs.md#york07ga3)

??? abstract "Abstract"
	
	Our Genomics experiments in this year mainly focus on improving the passage retrieval performance in the biomedical domain. We address this problem by constructing different indexes. In particular, we propose a method to build word-based index and sentence-based index for our experiments. The passage mean average precision (passage MAP) for our first run “york07ga1” using the word-based index was 0.095 and the passage MAP for our second run “york07ga2” using the sentence-based index was 0.086. However, the passage MAP for our third run “york07ga3” using both the word-based index and UMLS for query expansion degraded to 0.060. All these three official runs are automatic. The evaluation results show that using the word-based index is more effective than using the sentence-based index for improving the passage retrieval performance. We find that pseudo-relevance feedback can make a positive contribution to the retrieval performance. However, we also find that query expansion using UMLS and Entrez Gene does not improve the retrieval performance, and in some cases it makes a negative contribution to the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangSRA07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangSRA07,
		author = {Xiangji Huang and Damon Sotoudeh{-}Hosseinii and Hashmat Rohian and Xiangdong An},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2007: Genomics Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/yorku.geo.final.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangSRA07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Retrieval and Information Extraction in TREC Genomics  2007

_Antonio Jimeno-Yepes, Piotr Pezik_

- :fontawesome-solid-user-group: **Participant:** [ebi.yepes](./genomics/participants.md#ebi.yepes)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ebi.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ebi.geo.final.pdf)
- :material-file-search: **Runs:** [EBI1Lucene](./genomics/runs.md#ebi1lucene) | [EBI3Boosting](./genomics/runs.md#ebi3boosting) | [EBI2Fusion](./genomics/runs.md#ebi2fusion)

??? abstract "Abstract"
	
	In TREC Genomics a question/answering task has been proposed. A set of questions with a specific entity of interest is proposed and a set of passages from a collection of full text documents has to be selected from the document collection provided. We have used a two step approach: the first one is recall-oriented retrieval, and the second is an information extraction system that is intended to provide higher precision. We rely on well known techniques like query expansion and resources like MeSH and UMLS. The information extraction techniques are part of the infrastructure of the Text Mining Group at European Bioinformatics Institute. Using standard information retrieval techniques has been found more beneficial than using more complex processing. Having analyzed the results we find that the performance of query expansion varies for different topics. There are several reasons. Terminological resources may contain ambiguous synonyms or synonyms whose textual usage patterns differ from the usage of the original query terms. On the whole our performance was similar to the mean results from the three performance measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JimenoP07.bib) "
	```
	@inproceedings{DBLP:conf/trec/JimenoP07,
		author = {Antonio Jimeno{-}Yepes and Piotr Pezik},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Information Retrieval and Information Extraction in {TREC} Genomics 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ebi.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JimenoP07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Language Models for Genomics Information Retrieval: UIUC at TREC  2007 Genomics Track

_Yue Lu, Jing Jiang, Xu Ling, Xin He, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uc-zhai](./genomics/participants.md#uc-zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uiuc-lu.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uiuc-lu.geo.final.pdf)
- :material-file-search: **Runs:** [UIUCconj](./genomics/runs.md#uiucconj) | [UIUCsyn](./genomics/runs.md#uiucsyn) | [UIUCrelfb](./genomics/runs.md#uiucrelfb)

??? abstract "Abstract"
	
	The University of Illinois at Urbana-Champaign (UIUC) participated in TREC 2007 Genomics Track. Our general goal of participation is to apply language model-based approaches to the genomics retrieval task and study how we may extend the standard language models to accommodate two special needs for this year's genomics retrieval task: (1) gene synonym expansion and (2) conjunctive query interpretation. We also tested user relevance feedback. Preliminary result analysis shows that our synonym expansion method can improve document-level MAP, but generally has little influence on passage-level and aspect measures, while conjunctive scoring is not as effective as the standard KL-Divergence scoring, even though our pre-TREC experiments on a small set of training data showed otherwise. Relevance feedback appears to help. Further experiments and analysis are needed to draw more definitive conclusions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuJLHZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuJLHZ07,
		author = {Yue Lu and Jing Jiang and Xu Ling and Xin He and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Language Models for Genomics Information Retrieval: {UIUC} at {TREC} 2007 Genomics Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uiuc-lu.geo.final.pdf},
		timestamp = {Wed, 24 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LuJLHZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Bootstrapping Language Associated with Biomedical Entities

_Edgar Meij, Sophia Katrenko_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.meij](./genomics/participants.md#uamsterdam.meij)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uamsterdam-meij.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uamsterdam-meij.geo.final.pdf)
- :material-file-search: **Runs:** [AIDrun1](./genomics/runs.md#aidrun1) | [AIDrun3](./genomics/runs.md#aidrun3) | [AIDrun2](./genomics/runs.md#aidrun2)

??? abstract "Abstract"
	
	The TREC Genomics 2007 task included recognizing topic-specific entities in the returned passages. To address this task, we have designed and implemented a novel data-driven approach by combining information extraction with language modeling techniques. Instead of using an exhaustive list of all possible instances for an entity type, we look at the language usage around each entity type and use that as a classifier to determine whether or not a piece of text discusses such an entity type. We do so by comparing it with language models of the passages. E.g., given the entity type “genes”, our approach can measure the gene-iness of a piece of text. Our algorithm works as follows. Given an entity type, it first uses Hearst patterns to extract instances of the type. To extract more instances, we look for new contextual patterns around the instances and use them as input for a bootstrapping method, in which new instances and patterns are discovered iteratively. Afterwards, all discovered instances and patterns are used to find the sentences in the collection which are most on par with the requested entity type. A language model is then generated from these sentences and, at retrieval time, we use this model to rerank retrieved passages. As to the results of our submitted runs, we find that our baseline run performs well above the median of all participant's scores. Additionally, we find that applying our proposed method helps those entity types most for which there are unambiguous patterns and numerous instances.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeijK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeijK07,
		author = {Edgar Meij and Sophia Katrenko},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Bootstrapping Language Associated with Biomedical Entities},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uamsterdam-meij.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MeijK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using IR-n for Information Retrieval of Genomics Track

_María Pardiño, Rafael M. Terol, Patricio Martínez-Barco, Fernando Llopis, Elisa Noguera_

- :fontawesome-solid-user-group: **Participant:** [ualicante.terol](./genomics/participants.md#ualicante.terol)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ualicante.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ualicante.geo.final.pdf)
- :material-file-search: **Runs:** [IRn](./genomics/runs.md#irn)

??? abstract "Abstract"
	
	Nowadays there is a big amount of biomedical literature which uses complex nouns and acronyms of biological entities thus complicating the task of retrieval specific information. The Genomics Track works for this goal and this paper describes the approach we used to take part of this track of TREC 2007. As this is the first time we participate in this track, we configurated a new system consisting of the following diferenciated parts: preprocessing, passage generation, document retrieval and passage (with the answer) extraction. We want to call special attention to the textual retrieval system used, which was developed by the University of Alicante. Adapting the resources for the propouse, our system has obtained precision results over the mean and median average of the 66 official runs for the Document, Aspect and Passage2 MAP; and in the case of Passage MAP we get nearly the median and mean value. We want to emphasize we have obtained these results without incorporating specific information about the domain of the track. For the future, we would like to further develop our system in this direction.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PardinoTMLN07.bib) "
	```
	@inproceedings{DBLP:conf/trec/PardinoTMLN07,
		author = {Mar{\'{\i}}a Pardi{\~{n}}o and Rafael M. Terol and Patricio Mart{\'{\i}}nez{-}Barco and Fernando Llopis and Elisa Noguera},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using IR-n for Information Retrieval of Genomics Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ualicante.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PardinoTMLN07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cross Language Information Retrieval for Biomedical Literature

_Martijn J. Schuemie, Dolf Trieschnigg, Wessel Kraaij_

- :fontawesome-solid-user-group: **Participant:** [tno-ict](./genomics/participants.md#tno-ict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/utwente-erasmus-tno.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/utwente-erasmus-tno.geo.final.pdf)
- :material-file-search: **Runs:** [UTEMC1](./genomics/runs.md#utemc1) | [UTEMC2](./genomics/runs.md#utemc2)

??? abstract "Abstract"
	
	This workshop report discusses the collaborative work of UT, EMC and TNO on the TREC Genomics Track 2007. The biomedical information retrieval task is approached using cross language methods, in which biomedical concept detection is combined with effective IR based on unigram language models. Furthermore, a co-occurrence method is used to select and filter candidate answers. On its own, the cross lingual approach and the filtering do not strongly improve retrieval results. However, the combination of approaches does show a strong improvement over the monolingual baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchuemieTK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchuemieTK07,
		author = {Martijn J. Schuemie and Dolf Trieschnigg and Wessel Kraaij},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Cross Language Information Retrieval for Biomedical Literature},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/utwente-erasmus-tno.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchuemieTK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Retrieval Using Weights

_Jonathan Schuman, Sabine Bergler_

- :fontawesome-solid-user-group: **Participant:** [concordiau.bergler](./genomics/participants.md#concordiau.bergler)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/concordia.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/concordia.geo.final.pdf)
- :material-file-search: **Runs:** [biokiP](./genomics/runs.md#biokip) | [biokiS](./genomics/runs.md#biokis) | [biokiST](./genomics/runs.md#biokist)

??? abstract "Abstract"
	
	Using the same interactive IR component as for TREC 2006, this submission probed the ability of a user without requisite domain knowledge to interactively set appropriate weights. The weighted keyword proximity method employed allowed a computer science undergraduate to achieve rankings above the median for all measures without the use of external knowledge sources or term expansion techniques but in an interactive fashion. This suggests that domain experts should be able to perform above the median reliably, and are expected to excel when they can use domain terminology to their advantage.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchumanB07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchumanB07,
		author = {Jonathan Schuman and Sabine Bergler},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Interactive Retrieval Using Weights},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/concordia.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchumanB07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Entity-Based Relevance Feedback for Genomic List Answer Retrieval

_Nicola Stokes, Yi Li, Lawrence Cavedon, Eric Huang, Jiawen Rong, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [umelbourne.stokes](./genomics/participants.md#umelbourne.stokes)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umelbourne-stokes.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umelbourne-stokes.geo.final.pdf)
- :material-file-search: **Runs:** [MuMshFdRsc](./genomics/runs.md#mumshfdrsc) | [MuMshNfdRsc](./genomics/runs.md#mumshnfdrsc) | [MuMshFd](./genomics/runs.md#mumshfd)

??? abstract "Abstract"
	
	In this paper we present a system which uses ontological resources and a gene name variation generation tool to expand concepts in the original query. The novelty of our approach lies in our concept-based normalization ranking model. For the 2007 Genomic task, we also modified this system architecture with an additional dynamic form of query expansion called entity-based relevance feedback. This technique works by identifying potentially relevant entity instances in an initial set of retrieved candidate paragraphs. These entities are added to the initial query with the aim of boasting the rank of passages containing lists of these entities. Our final modification to the system, aims to maximizing the passage-level MAP score, by dropping sentences that do not contain any query concepts, from the beginning and the end of a candidate paragraph. Our TREC 2007 results show that our relevance feedback method can significantly improve baseline retrieval performance with respect to document-level MAP.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StokesLCHRZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/StokesLCHRZ07,
		author = {Nicola Stokes and Yi Li and Lawrence Cavedon and Eric Huang and Jiawen Rong and Justin Zobel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Entity-Based Relevance Feedback for Genomic List Answer Retrieval},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/umelbourne-stokes.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StokesLCHRZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage Relevancy Through Semantic Relatedness

_Luis Tari, Phan Huy Tu, Barry Lumpkin, Robert Leaman, Graciela Gonzalez, Chitta Baral_

- :fontawesome-solid-user-group: **Participant:** [arizona-stateu.gonzalez](./genomics/participants.md#arizona-stateu.gonzalez)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/arizonau.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/arizonau.geo.final.pdf)
- :material-file-search: **Runs:** [asubaral1](./genomics/runs.md#asubaral1) | [asubaral2](./genomics/runs.md#asubaral2) | [asubaral3](./genomics/runs.md#asubaral3)

??? abstract "Abstract"
	
	Questions that require answers in the form of a list of entities and the identification of diverse biological entity classes present an interesting challenge that required new approaches not needed for the TREC 2006 Genomics track. We added some components to our automatic question answering system, including (i) a simple algorithm to select which keywords extracted from natural language questions should be treated as essential in the formation of queries, (ii) the use of different entity recognizers for various biological entity classes in the extraction of passages (iii) determining relevancy of candidate passages with the use of semantic relatedness based on MeSH and UMLS semantic network. We present here an overview of our approach, with preliminary analysis and insights as to the performance of our system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TariTLLGB07.bib) "
	```
	@inproceedings{DBLP:conf/trec/TariTLLGB07,
		author = {Luis Tari and Phan Huy Tu and Barry Lumpkin and Robert Leaman and Graciela Gonzalez and Chitta Baral},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Passage Relevancy Through Semantic Relatedness},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/arizonau.geo.final.pdf},
		timestamp = {Wed, 25 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TariTLLGB07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT TREC 2007 Genomics Track: Using Concept-Based Semantics in  Context for Genomics Literature Passage Retrieval

_Jay Urbain, Nazli Goharian, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [iit.urbain](./genomics/participants.md#iit.urbain)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/iit-urbain.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/iit-urbain.geo.final.pdf)
- :material-file-search: **Runs:** [iitx1r2](./genomics/runs.md#iitx1r2) | [iitx2r2](./genomics/runs.md#iitx2r2) | [iitx3r2](./genomics/runs.md#iitx3r2)

??? abstract "Abstract"
	
	For the TREC-2007 Genomics Track [1], we explore unsupervised techniques for extracting semantic information about biomedical concepts with a retrieval model for using these semantics in context to improve passage retrieval precision. Dependency grammar analysis is evaluated for boosting the rank of passages where complementary subject/object concept pairs can be identified between queries and sentences from candidate passages. In our model, a concept is represented as a set of synonymous terms and a concept-word distribution. Concept terms are identified using an information extraction technique relying on shallow sentence parsing, external knowledge sources, and document context. The system combines a dimensional data model for indexing scientific literature at multiple levels of document context, with a rule-based query processing algorithm. The data model consists of two hierarchical indices: one for individual words and a second for extracted concepts. The word index provides retrieval of single or multi-word terms. The concept index provides efficient retrieval of single or multiple independent concepts. A retrieval function combines concepts with term statistics at multiple levels of context to identify relevant passages. Finally, we boost the relevance score of sentences identified within a passage where we can identify term dependencies that complement subject/object pairs between query and passage sentences via dependency grammar analysis. Our objective for this year's forum was to improve passage retrieval precision. We submitted three automatically generated results for three variations of our retrieval model to the TREC forum. The three results exceeded the track median for character based passage retrieval by 75 to 93%. The mean average precision (MAP) for our top passage retrieval model was 0.0940 which compares favorably to the top result of 0.0976.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UrbainGF07.bib) "
	```
	@inproceedings{DBLP:conf/trec/UrbainGF07,
		author = {Jay Urbain and Nazli Goharian and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} {TREC} 2007 Genomics Track: Using Concept-Based Semantics in Context for Genomics Literature Passage Retrieval},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/iit-urbain.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UrbainGF07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage Retrieval with Vector Space and Query-Level Aspect Models

_Raymond Wan, Vo Ngoc Anh, Hiroshi Mamitsuka_

- :fontawesome-solid-user-group: **Participant:** [kyotou.wan](./genomics/participants.md#kyotou.wan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/kyotou-umelbourne.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/kyotou-umelbourne.geo.final.pdf)
- :material-file-search: **Runs:** [kyoto1](./genomics/runs.md#kyoto1) | [kyoto2](./genomics/runs.md#kyoto2) | [kyoto3](./genomics/runs.md#kyoto3)

??? abstract "Abstract"
	
	This report describes the joint work by Kyoto University and the University of Melbourne for the TREC Genomics Track in 2007. As with 2006, the task for this year was the retrieval of passages from a biomedical document collection. The overall framework of our system from 2006 remains unchanged and is comprised of two parts: a paragraph-level retrieval system and a passage extraction system. These two systems are based on the vector space model and a probabilistic word-based aspect model, respectively. This year, we have adopted numerous changes to our 2007 system which we believe corrected some problems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WanAM07.bib) "
	```
	@inproceedings{DBLP:conf/trec/WanAM07,
		author = {Raymond Wan and Vo Ngoc Anh and Hiroshi Mamitsuka},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Passage Retrieval with Vector Space and Query-Level Aspect Models},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/kyotou-umelbourne.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WanAM07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIM at TREC 2007

_Jun Xu, Jing Yao, Jiaqian Zheng, Qi Sun, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [fudanu.niu](./genomics/participants.md#fudanu.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf)
- :material-file-search: **Runs:** [fdgerun1](./genomics/runs.md#fdgerun1) | [fdgerun2](./genomics/runs.md#fdgerun2) | [fdgerun3](./genomics/runs.md#fdgerun3)

??? abstract "Abstract"
	
	This paper introduced the four tracks that WIM-Lab Fudan University had taken part in at TREC 2007. For spam track, a multi-centre model was proposed considering the characteristics of spam mails in contrast of traditional 2-class classification methodology, and the incremental clustering and closeness-based classification methods were applied this year. For enterprise track, our research was mainly focused on ranking functions of experts and selecting correct supporting documents regarding to a given topic. For legal track, the effects of word distribution model in query expansion and various corpus pre-processing methods were mainly evaluated. For genomics track, three score methods were proposed to find the most relevant text snippets to a given topic. This paper gives an overview of the methods employed for each sub tasks, and compares the results of each track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuYZSN07.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuYZSN07,
		author = {Jun Xu and Jing Yao and Jiaqian Zheng and Qi Sun and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIM} at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuYZSN07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2007 Genomics Track

_Zhihao Yang, Hongfei Lin, Baojin Cui, Yanpeng Li, Xiao Zhang_

- :fontawesome-solid-user-group: **Participant:** [dalianu.yang](./genomics/participants.md#dalianu.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/dalianu.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/dalianu.geo.final.pdf)
- :material-file-search: **Runs:** [DUTgen2](./genomics/runs.md#dutgen2) | [DUTgen1](./genomics/runs.md#dutgen1) | [DUTgen3](./genomics/runs.md#dutgen3)

??? abstract "Abstract"
	
	This paper describes our experiments on TREC 2007 Genomics Track which is concerned with question answering extraction from full-text biomedical literatures. In our experiment, named entities were recognized at the preprocessing stage using a two-view method. MeSH was used to expand the terms. We performed passage retrieval by using sentence-level half overlapped sliding windows. Indri structured query language operators were also used to construct queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLCLZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangLCLZ07,
		author = {Zhihao Yang and Hongfei Lin and Baojin Cui and Yanpeng Li and Xiao Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2007 Genomics Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/dalianu.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLCLZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Genomics Track at UIC

_Wei Zhou, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [uillinois.chicago.zhou](./genomics/participants.md#uillinois.chicago.zhou)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uic-zhou.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uic-zhou.geo.final.pdf)
- :material-file-search: **Runs:** [UICGenRun1](./genomics/runs.md#uicgenrun1) | [UICGenRun2](./genomics/runs.md#uicgenrun2)

??? abstract "Abstract"
	
	We considered that a query of this year's Genomics track consists of two parts, target and qualification. A target refers to any instance of a certain entity type and the qualification refers to the condition that the target needs to satisfy in order to be qualified as an answer to the query. For example, the target and qualification of the query “What [ANTIBODIES] have been used to detect protein TLR4?” are “an instance of ANTIBODIES” and “have been used to detect protein TLR4”, respectively. The relevance of a document to a query was measured by to what degree the document contains a target and satisfies the qualification [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouY07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouY07,
		author = {Wei Zhou and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Genomics Track at {UIC}},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uic-zhou.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouY07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Spam 

#### TREC 2007 Spam Track Overview

_Gordon V. Cormack_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/SPAM.OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/SPAM.OVERVIEW16.pdf)
??? abstract "Abstract"
	
	TREC's Spam Track uses a standard testing framework that presents a set of chronologically ordered email messages a spam filter for classification. In the filtering task, the messages are presented one at at time to the filter, which yields a binary judgment (spam or ham [i.e. non-spam]) which is compared to a human-adjudicated gold standard. The filter also yields a spamminess score, intended to reflect the likelihood that the classified message is spam, which is the subject of post-hoc ROC (Receiver Operating Characteristic) analysis. Four different forms of user feedback are modeled: with immediate feedback the gold standard for each message is communicated to the filter immediately following classification; with delayed feedback the gold standard is communicated to the filter sometime later (or potentially never), so as to model a user reading email from time to time and perhaps not diligently reporting the filter's errors; with partial feedback the gold standard for only a subset of email recipients is transmitted to the filter, so as to model the case of some users never reporting filter errors; with active on-line learning (suggested by D. Sculley from Tufts University [11]) the filter is allowed to request immediate feedback for a certain quota of messages which is considerably smaller than the total number. Two test corpora - email messages plus gold standard judgments - were used to evaluate subject filters. One public corpus (trec07p) was distributed to participants, who ran their filters on the corpora using a track-supplied toolkit implementing the framework and the four kinds of feedback. One private corpus (MrX 3) was not distributed to participants; rather, participants submitted filter implementations that were run, using the toolkit, on the private data. Twelve groups participated in the track, each submitting up to four filters for evaluation in each of the four feedback modes (immediate; delayed; partial; active). Task guidelines and tools may be found on the web at http://plg.uwaterloo.ca/~gvcormac/spam/.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Cormack07.bib) "
	```
	@inproceedings{DBLP:conf/trec/Cormack07,
		author = {Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 Spam Track Overview},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/SPAM.OVERVIEW16.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Cormack07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo Participation in the TREC 2007 Spam Track

_Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.clarke](./spam/participants.md#uwaterloo.clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uwaterloo.spam.pdf](http://trec.nist.gov/pubs/trec16/papers/uwaterloo.spam.pdf)
- :material-file-search: **Runs:** [wat1](./spam/runs.md#wat1) | [wat2](./spam/runs.md#wat2) | [wat3](./spam/runs.md#wat3) | [wat4](./spam/runs.md#wat4) | [wat3p1000](./spam/runs.md#wat3p1000) | [wat4p1000](./spam/runs.md#wat4p1000) | [wat1p1000](./spam/runs.md#wat1p1000) | [wat2p1000](./spam/runs.md#wat2p1000) | [wat3pd](./spam/runs.md#wat3pd) | [wat4pd](./spam/runs.md#wat4pd) | [wat1pd](./spam/runs.md#wat1pd) | [wat2pd](./spam/runs.md#wat2pd) | [wat3pf](./spam/runs.md#wat3pf) | [wat4pf](./spam/runs.md#wat4pf) | [wat1pf](./spam/runs.md#wat1pf) | [wat2pf](./spam/runs.md#wat2pf) | [wat2pp](./spam/runs.md#wat2pp) | [wat3pp](./spam/runs.md#wat3pp) | [wat4pp](./spam/runs.md#wat4pp) | [wat1pp](./spam/runs.md#wat1pp)

??? abstract "Abstract"
	
	This is the first year that we have submitted participant runs to TREC (Cormack is track coordinator). In parallel with running the track, we have investigated two new filtering methods, inspired by the excellent results that others have shown in the task. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Cormack07a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Cormack07a,
		author = {Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Waterloo Participation in the {TREC} 2007 Spam Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uwaterloo.spam.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Cormack07a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Three Non-Bayesian Methods of Spam Filtration: CRM114 at TREC  2007

_Mamoru Kato, Joseph Langeway, Yimin Wu, William S. Yerazunis_

- :fontawesome-solid-user-group: **Participant:** [mitsubhishi.yerazunis](./spam/participants.md#mitsubhishi.yerazunis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/crm114.spam.final.pdf](http://trec.nist.gov/pubs/trec16/papers/crm114.spam.final.pdf)
- :material-file-search: **Runs:** [crm4p1000](./spam/runs.md#crm4p1000) | [crm1p1000](./spam/runs.md#crm1p1000) | [crm2p1000](./spam/runs.md#crm2p1000) | [crm1pd](./spam/runs.md#crm1pd) | [crm2pd](./spam/runs.md#crm2pd) | [crm3pd](./spam/runs.md#crm3pd) | [crm4pd](./spam/runs.md#crm4pd) | [crm1pf](./spam/runs.md#crm1pf) | [crm2pf](./spam/runs.md#crm2pf) | [crm3pf](./spam/runs.md#crm3pf) | [crm4pf](./spam/runs.md#crm4pf) | [crm4pp](./spam/runs.md#crm4pp) | [crm1pp](./spam/runs.md#crm1pp) | [crm2pp](./spam/runs.md#crm2pp) | [crm3pp](./spam/runs.md#crm3pp)

??? abstract "Abstract"
	
	For the TREC 2007 conference, the CRM114 team considered three non Bayesian methods of spam filtration in the CRM114 framework - an SVM based on the “hyperspace” feature==document paradigm, a bit entropy matcher, and substring compression based on LZ77. As a calibration yardstick, we used the well tested and widely used CRM114 OSB markov random field system (basically unchanged since 2003). The results show that the SVM has a spam filtering accuracy of about a factor of two to three better accuracy than the OSB system, that substring compression is somewhat more accurate than OSB, and that bit entropy is somewhat less accurate for the TREC 2007 test sets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KatoLWY07.bib) "
	```
	@inproceedings{DBLP:conf/trec/KatoLWY07,
		author = {Mamoru Kato and Joseph Langeway and Yimin Wu and William S. Yerazunis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Three Non-Bayesian Methods of Spam Filtration: {CRM114} at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/crm114.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KatoLWY07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Relaxed Online SVMs in the TREC Spam Filtering Track

_David Sculley, Gabriel Wachman_

- :fontawesome-solid-user-group: **Participant:** [tufts.sculley](./spam/participants.md#tufts.sculley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/tuftsu.spam.final.pdf](http://trec.nist.gov/pubs/trec16/papers/tuftsu.spam.final.pdf)
- :material-file-search: **Runs:** [tftS1F](./spam/runs.md#tfts1f) | [tftS2F](./spam/runs.md#tfts2f) | [tftS3F](./spam/runs.md#tfts3f) | [tftS4F](./spam/runs.md#tfts4f) | [tftS2Fp1000](./spam/runs.md#tfts2fp1000) | [tftS1Fp1000](./spam/runs.md#tfts1fp1000) | [tftS3Fp1000](./spam/runs.md#tfts3fp1000) | [tftS1Fpd](./spam/runs.md#tfts1fpd) | [tftS2Fpd](./spam/runs.md#tfts2fpd) | [tftS3Fpd](./spam/runs.md#tfts3fpd) | [tftS1Fpf](./spam/runs.md#tfts1fpf) | [tftS2Fpf](./spam/runs.md#tfts2fpf) | [tftS3Fpf](./spam/runs.md#tfts3fpf) | [tftS1Fpp](./spam/runs.md#tfts1fpp) | [tftS2Fpp](./spam/runs.md#tfts2fpp) | [tftS3Fpp](./spam/runs.md#tfts3fpp)

??? abstract "Abstract"
	
	Relaxed Online Support Vector Machines (ROSVMs) have recently been proposed as an efficient methodology for attaining an approximate SVM solution for streaming data such as the online spam filtering task. Here, we apply ROSVMs in the TREC 2007 Spam filtering track and report results. In particular, we explore the effect of various sliding-window sizes, trading off computation cost against classification performance with good results. We also test a variant of fixed-uncertainty sampling for Online Active Learning. The best results with this approach give classification performance near to that of the fully supervised approach while requiring only a small fraction of the examples to be labeled.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SculleyW07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SculleyW07,
		author = {David Sculley and Gabriel Wachman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Relaxed Online SVMs in the {TREC} Spam Filtering Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/tuftsu.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SculleyW07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIM at TREC 2007

_Jun Xu, Jing Yao, Jiaqian Zheng, Qi Sun, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [fudanu.niu](./spam/participants.md#fudanu.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf)
- :material-file-search: **Runs:** [fdw1](./spam/runs.md#fdw1) | [fdw2](./spam/runs.md#fdw2) | [fdw3](./spam/runs.md#fdw3) | [fdw4](./spam/runs.md#fdw4) | [fdw4pf](./spam/runs.md#fdw4pf) | [fdw4pd](./spam/runs.md#fdw4pd) | [fdw4pp](./spam/runs.md#fdw4pp) | [fdw4p1000](./spam/runs.md#fdw4p1000) | [fdw3pf](./spam/runs.md#fdw3pf) | [fdw3pd](./spam/runs.md#fdw3pd) | [fdw3pp](./spam/runs.md#fdw3pp) | [fdw3p1000](./spam/runs.md#fdw3p1000) | [fdw2pf](./spam/runs.md#fdw2pf) | [fdw2pd](./spam/runs.md#fdw2pd) | [fdw2pp](./spam/runs.md#fdw2pp) | [fdw2p1000](./spam/runs.md#fdw2p1000) | [fdw1pf](./spam/runs.md#fdw1pf) | [fdw1pd](./spam/runs.md#fdw1pd) | [fdw1pp](./spam/runs.md#fdw1pp) | [fdw1p1000](./spam/runs.md#fdw1p1000)

??? abstract "Abstract"
	
	This paper introduced the four tracks that WIM-Lab Fudan University had taken part in at TREC 2007. For spam track, a multi-centre model was proposed considering the characteristics of spam mails in contrast of traditional 2-class classification methodology, and the incremental clustering and closeness-based classification methods were applied this year. For enterprise track, our research was mainly focused on ranking functions of experts and selecting correct supporting documents regarding to a given topic. For legal track, the effects of word distribution model in query expansion and various corpus pre-processing methods were mainly evaluated. For genomics track, three score methods were proposed to find the most relevant text snippets to a given topic. This paper gives an overview of the methods employed for each sub tasks, and compares the results of each track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuYZSN07.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuYZSN07,
		author = {Jun Xu and Jing Yao and Jiaqian Zheng and Qi Sun and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIM} at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuYZSN07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Legal 

#### Overview of the TREC 2007 Legal Track

_Stephen Tomlinson, Douglas W. Oard, Jason R. Baron, Paul Thompson_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/LEGAL.OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/LEGAL.OVERVIEW16.pdf)
??? abstract "Abstract"
	
	TREC 2007 was the second year of the Legal Track, which focuses on evaluation of search technology for discovery of electronically stored information in litigation and regulatory settings. The track included three tasks: Ad Hoc (i.e., single-pass automatic) search, Relevance Feedback (two-pass search in a controlled setting with some relevant and nonrelevant documents manually marked after the first pass) and Interactive (in which real users could iteratively refine their queries and/or engage in multi-pass relevance feedback). This paper describes the design of the three tasks and analyzes the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TomlinsonOBT07.bib) "
	```
	@inproceedings{DBLP:conf/trec/TomlinsonOBT07,
		author = {Stephen Tomlinson and Douglas W. Oard and Jason R. Baron and Paul Thompson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2007 Legal Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/LEGAL.OVERVIEW16.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TomlinsonOBT07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring the Legal Discovery and Enterprise Tracks at the University  of Iowa

_Brian Almquist, Viet Ha-Thuc, Aditya Kumar Sehgal, Robert J. Arens, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [uiowa.srinivasan](./legal/participants.md#uiowa.srinivasan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uiowa.legal.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uiowa.legal.ent.final.pdf)
- :material-file-search: **Runs:** [IowaSL07Ref](./legal/runs.md#iowasl07ref) | [IowaSL0702](./legal/runs.md#iowasl0702) | [IowaSL0703](./legal/runs.md#iowasl0703) | [IowaSL0704](./legal/runs.md#iowasl0704) | [IowaSL0705](./legal/runs.md#iowasl0705) | [IowaSL0706](./legal/runs.md#iowasl0706) | [IowaSL0707](./legal/runs.md#iowasl0707)

??? abstract "Abstract"
	
	The University of Iowa Team, under coordinating professor Padmini Srinivasan, participated in the legal discovery and enterprise tracks of TREC-2007.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlmquistHSAS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlmquistHSAS07,
		author = {Brian Almquist and Viet Ha{-}Thuc and Aditya Kumar Sehgal and Robert J. Arens and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploring the Legal Discovery and Enterprise Tracks at the University of Iowa},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uiowa.legal.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlmquistHSAS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Access to Legal Documents: Exact Match, Best Match, and Combinations

_Avi Arampatzis, Jaap Kamps, Martijn Kooken, Nir Nussbaum_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.deRijke](./legal/participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uamsterdam-derijke.legal.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uamsterdam-derijke.legal.final.pdf)
- :material-file-search: **Runs:** [catchup0701p](./legal/runs.md#catchup0701p)

??? abstract "Abstract"
	
	In this paper, we document our efforts in participating to the TREC 2007 Legal track. We had multiple aims: First, to experiment with using different query formulations, trying to exploit the verbose topic statements. Second, to analyse how ranked retrieval methods can be fruitfully combined with traditional Boolean queries. Our main findings can be summarized as follows: First, we got mixed results trying to combine the original search request with terms extracted from the verbose topic statement. Second, by combining the Boolean reference run wit our ranked retrieval run allows us to get the high recall of the Boolean retrieval, whilst precision scores show an improvement over both the Boolean and the ranked retrieval runs. Third, we found out that if we treat the Boolean query as free text with varying degrees of interpretation of the original operator, we get competitive results. Moreover, both types of queries seem to capture different relevant documents, and the combination between the request text and the Boolean query leads to substantial gain in precision and recall.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ArampatzisKKN07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ArampatzisKKN07,
		author = {Avi Arampatzis and Jaap Kamps and Martijn Kooken and Nir Nussbaum},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Access to Legal Documents: Exact Match, Best Match, and Combinations},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uamsterdam-derijke.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ArampatzisKKN07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Examining Overfitting in Relevance Feedback: Sabir Research at TREC  2007

_Chris Buckley_

- :fontawesome-solid-user-group: **Participant:** [sabir.buckley](./legal/participants.md#sabir.buckley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/sabir.legal.final.pdf](http://trec.nist.gov/pubs/trec16/papers/sabir.legal.final.pdf)
- :material-file-search: **Runs:** [sab07legrf1](./legal/runs.md#sab07legrf1) | [sab07legrf2](./legal/runs.md#sab07legrf2) | [sab07legrf3](./legal/runs.md#sab07legrf3) | [SabL07ar1](./legal/runs.md#sabl07ar1) | [SabL07ar2](./legal/runs.md#sabl07ar2) | [SabL07ab1](./legal/runs.md#sabl07ab1) | [SabL07arbn](./legal/runs.md#sabl07arbn) | [sableg07i1](./legal/runs.md#sableg07i1)

??? abstract "Abstract"
	
	Sabir Research participated in TREC-2007 in the Million Query and Legal tracks. This writeup focuses on the Legal track, and in particular on the relevance feedback and interactive tasks within the Legal track. The information retrieval software used was the research version of SMART 16.0. SMART was originally developed in the early 1960's by Gerard Salton and since then has continued to be a leading research information retrieval tool. It continues to use a statistical vector space model, with stemming, stop words, weighting, inner product similarity function, and ranked retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Buckley07.bib) "
	```
	@inproceedings{DBLP:conf/trec/Buckley07,
		author = {Chris Buckley},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Examining Overfitting in Relevance Feedback: Sabir Research at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/sabir.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Buckley07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MultiText Legal Experiments at TREC 2007

_Stefan Büttcher, Charles L. A. Clarke, Gordon V. Cormack, Thomas R. Lynam, David R. Cheriton_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.clarke](./legal/participants.md#uwaterloo.clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uwaterloo-clarke.legal.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uwaterloo-clarke.legal.final.pdf)
- :material-file-search: **Runs:** [wat1fuse](./legal/runs.md#wat1fuse) | [wat2nobool](./legal/runs.md#wat2nobool) | [wat3desc](./legal/runs.md#wat3desc) | [wat4feed](./legal/runs.md#wat4feed) | [wat5nofeed](./legal/runs.md#wat5nofeed) | [wat6qap](./legal/runs.md#wat6qap) | [wat7bool](./legal/runs.md#wat7bool) | [wat8gram](./legal/runs.md#wat8gram)

??? abstract "Abstract"
	
	For the legal track we used the Wumpus search engine and investigated several methods that have proven successful in other domains, including cover density ranking and Okapi BM25 ranking. In addition to the traditional bag-of-words model we used boolean terms and character 4-grams. Pseudo-relevance feedback was effected using logistic regression on character 4-grams. Some runs specifically excluded documents returned by the boolean query so as to increase the number of such documents in the pool. While our runs were all marked as manual, this was only because the process was not fully automated and several tuning parameters were set after we viewed the data; no data-specific tuning was performed in configuring the system for our runs. Our best performing runs used a combination of all of the above-mentioned techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ButtcherCCLC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ButtcherCCLC07,
		author = {Stefan B{\"{u}}ttcher and Charles L. A. Clarke and Gordon V. Cormack and Thomas R. Lynam and David R. Cheriton},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MultiText Legal Experiments at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uwaterloo-clarke.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ButtcherCCLC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Dartmouth College at TREC 2007 Legal Track

_Wei-Ming Chen, Paul Thompson_

- :fontawesome-solid-user-group: **Participant:** [dartmouth.thompson](./legal/participants.md#dartmouth.thompson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/dartmouth.legal.final.pdf](http://trec.nist.gov/pubs/trec16/papers/dartmouth.legal.final.pdf)
- :material-file-search: **Runs:** [Dartmouth1](./legal/runs.md#dartmouth1)

??? abstract "Abstract"
	
	This report describes Dartmouth College's approach and results for the 2007 TREC Legal Track. Our original plan was to use the Combination of Expert Opinion (CEO) algorithm [1], to combine the search results from several search engines. However, we did not have enough time to build the index for more than one search engine by the time for submission for official runs. The official results described here are based only on the Lemur / Indri [2] search engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenT07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenT07,
		author = {Wei{-}Ming Chen and Paul Thompson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Dartmouth College at {TREC} 2007 Legal Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/dartmouth.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenT07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2007 Legal Track Interactive Task: A Report from the LIU  Team

_Heting Chu, Irene Crisci, Estella Cisco-Dalrymple, Tricia Daley, Lori Hoeffner, Trudy Katz, Susan Shebar, Carol Sullivan, Sarah Swammy, Maureen Weicher, Galia Yemini-Halevi_

- :fontawesome-solid-user-group: **Participant:** [liu.chu](./legal/participants.md#liu.chu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/longislandu.legal.final.pdf](http://trec.nist.gov/pubs/trec16/papers/longislandu.legal.final.pdf)
- :material-file-search: **Runs:** [LIU](./legal/runs.md#liu)

??? abstract "Abstract"
	
	The team from Long Island University (LIU) participated for the first time in the TREC 2007 Legal Track - Interactive Task. We received a call for participation in mid-March 2007 while a doctoral seminar titled Information Retrieval was in session. All nine students, evenly divided into three groups, performed this task till early May when the semester ended. Each group worked on one topic, taken from the first three on the priority list. The three topics are: Priority 1: All documents that refer or relate to pigeon deaths during the course of animal studies. (Group LIU1) Priority 2: All documents referencing or regarding lawsuits involving claims related to memory loss. (Group LIU2) Priority 3: All documents discussing, referencing, or relating to company guidelines, strategies, or internal approval for placement of tobacco products in movies that are mentioned as G-rated. (Group LIU3) Each group worked independently on the chosen topic while members within a group collaborated in one way or another from search strategy formulation to retrieved result evaluation. As requested, each group submitted their ranked, top 100 retrieved results and each participant filled out the TREC 2007 Questionnaire. The three sets of top 100 retrieved results were then evaluated by the doctoral seminar instructor's graduate assistant (GA). Those that had been judged as relevant in this round were submitted as our team's final results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChuCCDHKSSSWY07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChuCCDHKSSSWY07,
		author = {Heting Chu and Irene Crisci and Estella Cisco{-}Dalrymple and Tricia Daley and Lori Hoeffner and Trudy Katz and Susan Shebar and Carol Sullivan and Sarah Swammy and Maureen Weicher and Galia Yemini{-}Halevi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 Legal Track Interactive Task: {A} Report from the {LIU} Team},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/longislandu.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChuCCDHKSSSWY07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Washington (UW) at Legal TREC Interactive 2007

_Efthimis N. Efthimiadis, Mary A. Hotchkiss_

- :fontawesome-solid-user-group: **Participant:** [uwash.efthimiadis](./legal/participants.md#uwash.efthimiadis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uwashington.legal.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uwashington.legal.final.pdf)
- :material-file-search: **Runs:** [Washington](./legal/runs.md#washington)

??? abstract "Abstract"
	
	The TREC 2007 Legal Track Interactive Task Challenge involved five hypothetical legal “complaints” based on some facet of tobacco litigation. Each complaint included a request to produce relevant documents. These document production requests were broadly worded to force the opposing party to provide a maximum number of responsive documents during discovery. The resources for document production were two databases containing the tobacco litigation documents released under the terms of the Master Settlement Agreement (MSA) between the Attorneys General of several states and seven U.S. tobacco organizations. These two databases, the Legacy Tobacco Documents Library (LTDL) and Tobacco Documents Online (TDO), contain around 7,000,000 documents. The majority of these documents are not legal publications like cases, statutes, or regulations; the databases include scientific studies, corporate correspondence, periodical articles, news stories, and a mix of litigation documents. Finding relevant documents in large databases is easier said than done. Studies have shown that researchers tend to overestimate the effectiveness of online retrieval. In a 1985 study on retrieval effectiveness, attorneys who were confident they had located at least 75% of the relevant documents actually had a success rate of about 20%. (Blair and Maron, 1985). Their research findings had a major impact in information retrieval evaluation, especially of operational systems. In a sequel article Blair (1996) reflected on the impact of their study. Dabney (1986), Bing (1987) and Schweighofer (1999) provide in-depth reviews of the problems of full text searching for legal information and provide suggestions for solutions to the problems. In the past twenty years, the functionality of full-text document-retrieval systems has improved but more evaluation of information retrieval effectiveness is needed. Attorneys and their support staff must recognize that effective information retrieval in today's complex litigation requires a variety of tools and approaches, including a combination of automated searches, sampling of large databases, and a team-based review of these results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EfthimiadisH07.bib) "
	```
	@inproceedings{DBLP:conf/trec/EfthimiadisH07,
		author = {Efthimis N. Efthimiadis and Mary A. Hotchkiss},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Washington {(UW)} at Legal {TREC} Interactive 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uwashington.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EfthimiadisH07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### On Retrieving Legal Files: Shortening Documents and Weeding Out Garbage

_Scott Kulp, April Kontostathis_

- :fontawesome-solid-user-group: **Participant:** [ursinus-college.kontostathis](./legal/participants.md#ursinus-college.kontostathis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ursinus.legal.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ursinus.legal.final.pdf)
- :material-file-search: **Runs:** [ursinus1](./legal/runs.md#ursinus1) | [ursinus2](./legal/runs.md#ursinus2) | [ursinus3](./legal/runs.md#ursinus3) | [ursinus4](./legal/runs.md#ursinus4) | [ursinus5](./legal/runs.md#ursinus5) | [ursinus6](./legal/runs.md#ursinus6) | [ursinus7](./legal/runs.md#ursinus7) | [ursinus8](./legal/runs.md#ursinus8)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC Legal experiments in 2007. We have applied novel normalization techniques that are designed to slightly favor longer documents instead of assuming that all documents should have equal weight. We have also developed a new method for reformulating query text when background information is provided with an information request. We have also experimented with using enhanced OCR error detection to reduce the size of the term list and remove noise in the data. In this article, we discuss the impact of these effects on the TREC 2007 data sets. We show that the use of simple normalization methods significantly outperforms cosine normalization in the legal domain.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KulpK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/KulpK07,
		author = {Scott Kulp and April Kontostathis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {On Retrieving Legal Files: Shortening Documents and Weeding Out Garbage},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ursinus.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KulpK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with the Negotiated Boolean Queries of the TREC 2007  Legal Discovery Track

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [open-text.tomlinson](./legal/participants.md#open-text.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/open-text.legal.final.pdf](http://trec.nist.gov/pubs/trec16/papers/open-text.legal.final.pdf)
- :material-file-search: **Runs:** [otL07fb](./legal/runs.md#otl07fb) | [otL07fv](./legal/runs.md#otl07fv) | [otL07db](./legal/runs.md#otl07db) | [otL07rvl](./legal/runs.md#otl07rvl) | [otL07fb2x](./legal/runs.md#otl07fb2x) | [otL07fbe](./legal/runs.md#otl07fbe) | [otL07frw](./legal/runs.md#otl07frw) | [otL07pb](./legal/runs.md#otl07pb) | [otRF07fv](./legal/runs.md#otrf07fv) | [otRF07fb](./legal/runs.md#otrf07fb)

??? abstract "Abstract"
	
	We analyze the results of several experimental runs submitted for the TREC 2007 Legal Track (also sometimes known as the Legal Discovery Track). We submitted 4 boolean query runs (the initial proposal by the defendant, the rejoinder by the plaintiff, the final negotiated query, and a variation of the final query which had proximity distances doubled). We submitted 2 vector query runs (one based on the keywords of the final negotiated query, and another based on the (natural language) request text). We submitted a blind feedback run based on the final negotiated boolean query. Finally, we submitted a fusion run of the final boolean, request text and final vector runs. We found that none of the runs had a higher mean estimated Recall@B than the original final negotiated boolean query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson07.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson07,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with the Negotiated Boolean Queries of the {TREC} 2007 Legal Discovery Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/open-text.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CIIR Experiments for TREC Legal 2007

_Howard R. Turtle, Donald Metzler_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./legal/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umass.legal.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umass.legal.final.pdf)
- :material-file-search: **Runs:** [UMass10](./legal/runs.md#umass10) | [UMass11](./legal/runs.md#umass11) | [UMass12](./legal/runs.md#umass12) | [UMass13](./legal/runs.md#umass13) | [UMass14](./legal/runs.md#umass14) | [UMass15](./legal/runs.md#umass15)

??? abstract "Abstract"
	
	Four baseline experiments using standard Indri retrieval facilities and simple query formulation techniques and two experiments using more advanced formulations (dependence models and pseudo-relevance feedback) are described. All of the experiments perform substantially better than the median performance of automatic runs but exhibit lower estimated precision and recall at B than the reference Boolean run.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TurtleM07.bib) "
	```
	@inproceedings{DBLP:conf/trec/TurtleM07,
		author = {Howard R. Turtle and Donald Metzler},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CIIR} Experiments for {TREC} Legal 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/umass.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TurtleM07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIM at TREC 2007

_Jun Xu, Jing Yao, Jiaqian Zheng, Qi Sun, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [fudanu.niu](./legal/participants.md#fudanu.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf)
- :material-file-search: **Runs:** [fdwim7xj](./legal/runs.md#fdwim7xj) | [fdwim7ts](./legal/runs.md#fdwim7ts) | [fdwim7rs](./legal/runs.md#fdwim7rs) | [fdwim7ss](./legal/runs.md#fdwim7ss) | [fdwim7sl](./legal/runs.md#fdwim7sl)

??? abstract "Abstract"
	
	This paper introduced the four tracks that WIM-Lab Fudan University had taken part in at TREC 2007. For spam track, a multi-centre model was proposed considering the characteristics of spam mails in contrast of traditional 2-class classification methodology, and the incremental clustering and closeness-based classification methods were applied this year. For enterprise track, our research was mainly focused on ranking functions of experts and selecting correct supporting documents regarding to a given topic. For legal track, the effects of word distribution model in query expansion and various corpus pre-processing methods were mainly evaluated. For genomics track, three score methods were proposed to find the most relevant text snippets to a given topic. This paper gives an overview of the methods employed for each sub tasks, and compares the results of each track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuYZSN07.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuYZSN07,
		author = {Jun Xu and Jing Yao and Jiaqian Zheng and Qi Sun and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIM} at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuYZSN07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluation of Query Formulations in the Negotiated Query Refinement  Process of Legal e-Discovery: UMKC at TREC 2007 Legal Track

_Feng C. Zhao, Yugyung Lee, Deep Medhi_

- :fontawesome-solid-user-group: **Participant:** [umkc.zhao](./legal/participants.md#umkc.zhao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umissouri-kc.legal.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umissouri-kc.legal.final.pdf)
- :material-file-search: **Runs:** [UMKC1](./legal/runs.md#umkc1) | [UMKC2](./legal/runs.md#umkc2) | [UMKC3](./legal/runs.md#umkc3) | [UMKC4](./legal/runs.md#umkc4) | [UMKC6](./legal/runs.md#umkc6) | [UMKC5](./legal/runs.md#umkc5)

??? abstract "Abstract"
	
	UMKC participated in the 2007 legal track. Our experiments focused mainly on evaluating the different query formulations in the negotiated query refinement process of legal e-discovery. For our study, we considered three sets of paired runs in vector space model and language model respectively. Our experiments indicated that although the Boolean query negotiating process was successful for the standard Boolean retrieval model, it did not make statistically significant query improvements in our ranked systems. This result provided us an insight into the query negotiation process and a new direction to refine queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoLM07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoLM07,
		author = {Feng C. Zhao and Yugyung Lee and Deep Medhi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Evaluation of Query Formulations in the Negotiated Query Refinement Process of Legal e-Discovery: {UMKC} at {TREC} 2007 Legal Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/umissouri-kc.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoLM07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Stuctured Queries for Legal Search

_Yangbo Zhu, Le Zhao, Jamie Callan, Jaime G. Carbonell_

- :fontawesome-solid-user-group: **Participant:** [cmu.dir.callan](./legal/participants.md#cmu.dir.callan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/cmu-callan.legal.final.pdf](http://trec.nist.gov/pubs/trec16/papers/cmu-callan.legal.final.pdf)
- :material-file-search: **Runs:** [CMUL07std](./legal/runs.md#cmul07std) | [CMUL07ibs](./legal/runs.md#cmul07ibs) | [CMUL07ibp](./legal/runs.md#cmul07ibp) | [CMUL07ibt](./legal/runs.md#cmul07ibt) | [CMUL07irs](./legal/runs.md#cmul07irs) | [CMUL07irt](./legal/runs.md#cmul07irt) | [CMUL07o1](./legal/runs.md#cmul07o1) | [CMUL07o3](./legal/runs.md#cmul07o3) | [CMU07RFBSVME](./legal/runs.md#cmu07rfbsvme) | [CMU07RBase](./legal/runs.md#cmu07rbase) | [CMU07RSVMNP](./legal/runs.md#cmu07rsvmnp)

??? abstract "Abstract"
	
	This paper reports the experiments of using Indri for the main and routing (relevance feedback) tasks in the TREC 2007 Legal Track. For the main task, we analyze ranking algorithms using different fields, boolean constraints and structured operators. Evaluation results show that structured queries outperform bag-of-words ones. Boolean constraints improve both precision and recall. For the routing task, we train a linear SVM classifier for each topic. Terms with the largest weights are selected to form new queries. Both keywords and simple structured features (term.field) have been investigated. Named-Entity tags, LingPipe sentence breaker and metadata fields of the original documents are used to generate the field information. Results show that structured features and weighted queries improves retrieval, but only marginally. We also show which structures are more useful. It turns out metadata fields are not as important as we thought.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuZCC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuZCC07,
		author = {Yangbo Zhu and Le Zhao and Jamie Callan and Jaime G. Carbonell},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Stuctured Queries for Legal Search},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/cmu-callan.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuZCC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Question Answering 

#### Overview of the TREC 2007 Question Answering Track

_Hoa Trang Dang, Diane Kelly, Jimmy Lin_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/QA.OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/QA.OVERVIEW16.pdf)
??? abstract "Abstract"
	
	The TREC 2007 question answering (QA) track contained two tasks: the main task consisting of series of factoid, list, and “Other” questions organized around a set of targets, and the complex, interactive question answering (ciQA) task. The main task differed from previous years in that the document collection comprised blogs in addition to newswire documents, requiring systems to process diverse genres of unstructured text. The evaluation of factoid and list responses distinguished between answers that were globally correct (with respect to the document collection), and those that were only locally correct (with respect to the supporting document but not to the overall document collection). The ciQA task provided a framework for participants to investigate interaction in the context of complex information needs. Standing in for surrogate users, assessors interacted with QA systems live over the Web; this setup allowed participants to experiment with more complex interfaces but also revealed limitations in the ciQA design for evaluation of interactive systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DangKL07.bib) "
	```
	@inproceedings{DBLP:conf/trec/DangKL07,
		author = {Hoa Trang Dang and Diane Kelly and Jimmy Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2007 Question Answering Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/QA.OVERVIEW16.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DangKL07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Persuasive, Authorative and Topical Answers for Complex Question Answering

_Leif Azzopardi, Mark Baillie, Ian Ruthven_

- :fontawesome-solid-user-group: **Participant:** [ustrathclyde.ruthven](./qa/participants.md#ustrathclyde.ruthven)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ustrathclyde.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ustrathclyde.qa.final.pdf)
- :material-file-search: **Runs:** [sicka](./qa/runs.md#sicka) | [strath](./qa/runs.md#strath) | [strath2](./qa/runs.md#strath2) | [sicka2](./qa/runs.md#sicka2)

??? abstract "Abstract"
	
	The ciqa track investigates the role of interaction in answering complex questions: questions that relate two or more entities by some specified relationship. As in the ciqa 2006, our interest in ciqa 2007 was on contextual factors that may affect how answers are assessed. In ciqa 2006 we investigated factors such as topical knowledge or confidence in assessing answers through direct questioning - asking the ciqa assessors to directly estimate values for such variables using ordinal or categorical scales. In ciqa 2006 we found many useful relationships between personal contextual variables and how assessors judged answers. This year we were keen to follow this line of investigation, following a more specific research question: how do contextual variables affect the judgement of different types of information surrogate. We created information surrogates (answers) which contained similar amounts of information but presented the information in different ways; either as neutral, topically related information (topical answers), information that was presented in such a way as to entice the read (persuasive answers), or information that was presented as coming from a named authority (authorative answers). Separately, we gathered contextual information on the assessors' preferences for such answers through the use of HTML interaction forms. Our results show differences in how assessors reacted to these different information surrogates in terms of highly they were to judge the answer as good and how likely they were to read the document containing the answer.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AzzopardiBR07.bib) "
	```
	@inproceedings{DBLP:conf/trec/AzzopardiBR07,
		author = {Leif Azzopardi and Mark Baillie and Ian Ruthven},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Persuasive, Authorative and Topical Answers for Complex Question Answering},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ustrathclyde.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AzzopardiBR07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Drexel at TREC 2007: Question Answering

_Protima Banerjee, Hyoil Han_

- :fontawesome-solid-user-group: **Participant:** [drexelu.han](./qa/participants.md#drexelu.han)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/drexelu.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/drexelu.qa.final.pdf)
- :material-file-search: **Runs:** [DrexelRun1](./qa/runs.md#drexelrun1) | [DrexelRun2](./qa/runs.md#drexelrun2) | [DrexelRun3](./qa/runs.md#drexelrun3)

??? abstract "Abstract"
	
	The TREC Question Answering Track presented several distinct challenges to participants in 2007. Participants were asked to create a system which discovers the answers to factoid and list questions about people, entities, organizations and events, given both blog and newswire text data sources. In addition, participants were asked to expose interesting information nuggets which exist in the data collection, which were not uncovered by the factoid or list questions. This year is the first time the Intelligent Information Processing group at Drexel has participated in the TREC Question Answering Track. As such, our goal was the development of a Question Answering system framework to which future enhancements could be made, and the construction of simple components to populate the framework. The results of our system this year were not significant; our primary accomplishment was the establishment of a baseline system which can be improved upon in 2008 and going forward.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BanerjeeH07.bib) "
	```
	@inproceedings{DBLP:conf/trec/BanerjeeH07,
		author = {Protima Banerjee and Hyoil Han},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Drexel at {TREC} 2007: Question Answering},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/drexelu.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BanerjeeH07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Intellexer Question Answering

_Aliaksei Bondarionok, Anatoly Bobkov, Liudmila Sudanova, Pavel Mazur, Tatsiana Samuseva_

- :fontawesome-solid-user-group: **Participant:** [effectivesoft](./qa/participants.md#effectivesoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/effectivesoft.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/effectivesoft.qa.final.pdf)
- :material-file-search: **Runs:** [Intellexer7A](./qa/runs.md#intellexer7a) | [Intellexer7B](./qa/runs.md#intellexer7b) | [Intellexer7C](./qa/runs.md#intellexer7c)

??? abstract "Abstract"
	
	This is a short description of Intellexer QA system used in QA track 2007. The paper is divided into the following sections that describe modules of the system and certain steps of processing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BondarionokBSMS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/BondarionokBSMS07,
		author = {Aliaksei Bondarionok and Anatoly Bobkov and Liudmila Sudanova and Pavel Mazur and Tatsiana Samuseva},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Intellexer Question Answering},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/effectivesoft.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BondarionokBSMS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Pronto QA System at TREC 2007: Harvesting Hyponyms, Using  Nominalisation Patterns, and Computing Answer Cardinality

_Johan Bos, Edoardo Guzzetti, James R. Curran_

- :fontawesome-solid-user-group: **Participant:** [uroma.bos](./qa/participants.md#uroma.bos)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/urome.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/urome.qa.final.pdf)
- :material-file-search: **Runs:** [pronto07run1](./qa/runs.md#pronto07run1) | [pronto07run2](./qa/runs.md#pronto07run2) | [pronto07run3](./qa/runs.md#pronto07run3)

??? abstract "Abstract"
	
	The backbone of the Pronto QA system is linguistically-principled: Combinatory Categorial Grammar is used to generate syntactic analyses of questions and potential answer snippets, and Discourse Representation Theory is employed as semantic formalism to match the meanings of questions and answers. The key idea of the Pronto system is to use semantics to prune answer candidates, thereby exploiting lexical resources such as WordNet and NomLex to facilitate the selection of answers. The system performed well at TREC-2007 on factoid-questions with an answer accuracy of 22%, a score higher than the median accuracy score of all participating systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BosGC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/BosGC07,
		author = {Johan Bos and Edoardo Guzzetti and James R. Curran},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Pronto {QA} System at {TREC} 2007: Harvesting Hyponyms, Using Nominalisation Patterns, and Computing Answer Cardinality},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/urome.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BosGC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lethbridge's Participation in TREC 2007 QA Track

_Yllias Chali, Shafiq R. Joty_

- :fontawesome-solid-user-group: **Participant:** [ulethbridge.chali](./qa/participants.md#ulethbridge.chali)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ulethbridge.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ulethbridge.qa.final.pdf)
- :material-file-search: **Runs:** [UofL](./qa/runs.md#uofl)

??? abstract "Abstract"
	
	Question Answering (QA) is retrieving answers to natural language questions from a collection of documents rather than retrieving relevant documents containing the keywords of the query which is performed by search engines. What a user usually wants is often a precise answer to a question. For example, given the question “Who won the nobel prize in peace in 2006?” what a user really wants is the answer “Dr. Muhammad Yunus”, in stead of reading through lots of documents that contain the words “win”, “nobel”,“prize”, “peace” and “2006” etc. This means that question answering systems will possibly be integral to the next generation of search engines. The Text Retrieval Conference, TREC1 QA track is the major large-scale evaluation environment for open-domain question answering systems. The questions in the TREC-2007 QA track are clustered by target, which is the overall theme or topic of the questions. The track has three types of questions: 1. factoid that require only one correct response, 2. list that require a non redundant list of correct responses and 3. other questions that require a non redundant list of facts about the target that has not already been discovered by a previous answer. We took the approach of designing a question answering system that is based on document tagging and question classification. Question classification extracts useful information (i.e. answer type) from the question about how to answer the question. Document tagging extracts useful information from the documents, which will be used in finding the answer to the question. We used different available tools to tag the documents. Our system classifies the questions using manually developed rules.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChaliJ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChaliJ07,
		author = {Yllias Chali and Shafiq R. Joty},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Lethbridge's Participation in {TREC} 2007 {QA} Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ulethbridge.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChaliJ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering with LCC's CHAUCER-2 at TREC 2007

_Andrew Hickl, Kirk Roberts, Bryan Rink, Jeremy Bensley, Tobias Jungen, Ying Shi, John Williams_

- :fontawesome-solid-user-group: **Participant:** [lcc.chaucer](./qa/participants.md#lcc.chaucer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/lcc-hickl.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/lcc-hickl.qa.final.pdf)
- :material-file-search: **Runs:** [LCCFerret](./qa/runs.md#lccferret)

??? abstract "Abstract"
	
	In TREC 2007, Language Computer Corporation explored how a new, semantically-rich framework for information retrieval could be used to boost the overall performance of the answer extraction and answer selection components featured in its CHAUCER-2 automatic question-answering (Q/A) system. By replacing the traditional keyword-based retrieval system used in (?) with a new indexing and retrieval engine capable of retrieving documents or passages based on the distribution of named entities or semantic dependencies, we were able to dramatically enhance CHAUCER-2's overall accuracy, while significantly reducing the number of of candidate answers that were considered by its Answer Ranking and Answer Validation modules.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HicklRRBJSW07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HicklRRBJSW07,
		author = {Andrew Hickl and Kirk Roberts and Bryan Rink and Jeremy Bensley and Tobias Jungen and Ying Shi and John Williams},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering with LCC's {CHAUCER-2} at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/lcc-hickl.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HicklRRBJSW07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at the TREC 2007 QA Track

_Katja Hofmann, Valentin Jijkoun, Mahboob Alam Khalid, Joris van Rantwijk, Erik F. Tjong Kim Sang_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.deRijke](./qa/participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uamsterdam-hofmann.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uamsterdam-hofmann.qa.final.pdf)
- :material-file-search: **Runs:** [uams07main](./qa/runs.md#uams07main) | [uams07atch](./qa/runs.md#uams07atch) | [uams07nwrr](./qa/runs.md#uams07nwrr)

??? abstract "Abstract"
	
	In our participation in the TREC 2007 Question Answering (QA) track, we focused on three tasks. First, we processed the new blog corpus and converted it to formats which could be used by our QA system. Second, we rewrote the module interface code in Java in order to improve the maintainability of the system. And third, we added a new table stream which has learned associations between question properties and properties of candidate answers. In the three runs we submitted to the competition, we experimented with answer type checking and web re-ranking. In follow-up experiments we were able to further evaluate the contribution of these two factors, and to evaluate our new table lookup stream and combinations of streams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HofmannJKRS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HofmannJKRS07,
		author = {Katja Hofmann and Valentin Jijkoun and Mahboob Alam Khalid and Joris van Rantwijk and Erik F. Tjong Kim Sang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at the {TREC} 2007 {QA} Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uamsterdam-hofmann.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HofmannJKRS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSAIL at TREC 2007 Question Answering

_Boris Katz, Sue Felshin, Gregory Marton, Federico Mora, Yuan Kui Shen, Gabriel Zaccak, Ammar Ammar, Eric Eisner, Asli Turgut, Linda Brown Westrick_

- :fontawesome-solid-user-group: **Participant:** [mit-csail.katz](./qa/participants.md#mit-csail.katz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/mit.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/mit.qa.final.pdf)
- :material-file-search: **Runs:** [csail1](./qa/runs.md#csail1) | [csail2](./qa/runs.md#csail2) | [csail3](./qa/runs.md#csail3)

??? abstract "Abstract"
	
	MIT CSAIL's entries for the TREC 2007 question answering track built on our systems of previous years, updating them for the new corpora. Our greatest efforts went into the system that handles the 'other' questions, looking for new descriptive information about the topic. We noticed in our experiments with Nuggeteer (Marton and Radul, 2006)1 that some of the parameters made a big difference in the results, and decided to restructure our scoring to be able to tune its parameters. This represents the first such use of the Nuggeteer software that we are aware of, and yielded excellent results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KatzFMMSZAETW07.bib) "
	```
	@inproceedings{DBLP:conf/trec/KatzFMMSZAETW07,
		author = {Boris Katz and Sue Felshin and Gregory Marton and Federico Mora and Yuan Kui Shen and Gabriel Zaccak and Ammar Ammar and Eric Eisner and Asli Turgut and Linda Brown Westrick},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CSAIL} at {TREC} 2007 Question Answering},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/mit.qa.final.pdf},
		timestamp = {Sun, 10 May 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KatzFMMSZAETW07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Interactions to Improve Translation Dictionaries: UNC, Yahoo!  and ciQA

_Diane Kelly, Xin Fu, Vanessa Murdock_

- :fontawesome-solid-user-group: **Participant:** [unorth-carolina.kelly](./qa/participants.md#unorth-carolina.kelly)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/unc-yahoo.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/unc-yahoo.qa.final.pdf)
- :material-file-search: **Runs:** [UNCYA1](./qa/runs.md#uncya1) | [UNCYA2](./qa/runs.md#uncya2) | [UNCYABL30](./qa/runs.md#uncyabl30) | [UNCYAEX1](./qa/runs.md#uncyaex1) | [UNCYAEX2](./qa/runs.md#uncyaex2)

??? abstract "Abstract"
	
	Sentence retrieval is an important step in many question-answering (QA) technologies. However, characteristics of sentences and of the question-answering task itself often make it difficult to apply document retrieval techniques to sentence retrieval. The use of translation dictionaries offers one potentially useful approach to sentence retrieval, but training such dictionaries using QA corpora often introduces noise that can negatively impact retrieval performance. In this study, we experiment with using data elicited from assessors during interactions as training data for a translation dictionary. We employ two different interactions that elicit two types of data: data about assessors' topics and data about retrieved sentences. Results show that using sentence-level relevance feedback to adjust the translation dictionary improved retrieval for about half the topics, but harmed it for the other half.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KellyFM07.bib) "
	```
	@inproceedings{DBLP:conf/trec/KellyFM07,
		author = {Diane Kelly and Xin Fu and Vanessa Murdock},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Interactions to Improve Translation Dictionaries: UNC, Yahoo! and ciQA},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/unc-yahoo.qa.final.pdf},
		timestamp = {Mon, 26 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KellyFM07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Testing an Entity Ranking Function for English Factoid QA

_Kui-Lam Kwok, Norbert Dinstl_

- :fontawesome-solid-user-group: **Participant:** [queens-college-cuny.kwok](./qa/participants.md#queens-college-cuny.kwok)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/queens.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/queens.qa.final.pdf)
- :material-file-search: **Runs:** [pircs07qa2](./qa/runs.md#pircs07qa2) | [pircs07qa1](./qa/runs.md#pircs07qa1) | [pircs07qa3](./qa/runs.md#pircs07qa3)

??? abstract "Abstract"
	
	Much progress has been made in the English question-answering task since it was initiated in TREC-8 and our last participation in TREC-2001. QA is a complex semantics-oriented task, and it is necessary that much linguistic processing, auxiliary resources, and learning steps are needed to come up with adequate performance to the task [1]. Chinese language factoid QA was first introduced during NTCIR-5 and -6 [2,3] and in which we participated. Because Chinese QA was new with little training data and Chinese linguistic tools and resources were not as readily available as in English, we employed a simple answer ranking technique that depends only on surface term usage statistics in questions and document sentences [4,5]. The outcome has been surprisingly satisfactory, achieving results ~80% of the best [2,3]. We were curious how this approach may perform for English factoid questions, comparing with median result for example. The program was modified to support English in this TREC-2007 QA task. As in Chinese, we made little use of linguistic tools or training data, and no auxiliary resources. It can form a basis result from which more sophisticated tools may enhance. The Sections 2-5 describes our question classification, document processing and retrieval, entity extraction and answer ranker respectively. Section 6 shows our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokD07.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokD07,
		author = {Kui{-}Lam Kwok and Norbert Dinstl},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Testing an Entity Ranking Function for English Factoid {QA}},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/queens.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokD07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Complex Interactive Question Answering Enhanced with Wikipedia

_Ian MacKinnon, Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo-olga](./qa/participants.md#uwaterloo-olga)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uwaterloo-vechtomova.qa.pdf](http://trec.nist.gov/pubs/trec16/papers/uwaterloo-vechtomova.qa.pdf)
- :material-file-search: **Runs:** [UWinitBASE](./qa/runs.md#uwinitbase) | [UWinitWIKI](./qa/runs.md#uwinitwiki) | [UWfinWIKI](./qa/runs.md#uwfinwiki) | [UWfinLINK](./qa/runs.md#uwfinlink) | [UWfinalWIKI](./qa/runs.md#uwfinalwiki) | [UWfinalMAN](./qa/runs.md#uwfinalman)

??? abstract "Abstract"
	
	In ciQA, templates are used with several bracketed items we call ”facets” which are the basis of information being sought. This information is returned in the form of nuggets. Due to the concepts being sought having multiple terms to describe them, it becomes difficult to determine which sentences in the AQUAINT-2 news articles contain the query terms being sought, as they may be represented in the parent document by a variety of different phrases still making reference to the query term. For example, if the term ”John McCain” were being sought, it might appear in an article, however, the sentence which is the vital nugget may simply contain ”Senator McCain”; an imperfect match. Traditional query expansion[5] of facets would introduce new terms which are related but do not necessarily mean the same as the original facet. This does not always help the problem of query terms appearing in relevant documents but not relevant sentences within documents, it only introduces related terms which cannot be considered synonymous with the facet being retrieved. In this year's TREC, we hope to overcome some of this problem by looking for synonyms for facets using Wikipedia. Many of the ciQA facets are proper nouns and most thesauri, such as WordNet, do not contain entries for these. Thus, a new manner of finding synonyms must be found. In recent years, several new approaches have been proposed to use Wikipedia as a source of lexical information[2, 7], as it can be downloaded in its entirety, and contains relatively high quality articles[3].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacKinnonV07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacKinnonV07,
		author = {Ian MacKinnon and Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Complex Interactive Question Answering Enhanced with Wikipedia},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uwaterloo-vechtomova.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacKinnonV07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2007 ciQA Task: University of Maryland

_Nitin Madnani, Jimmy Lin, Bonnie J. Dorr_

- :fontawesome-solid-user-group: **Participant:** [umd-collegepark.oard](./qa/participants.md#umd-collegepark.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umd.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umd.qa.final.pdf)
- :material-file-search: **Runs:** [UMD07MMRa](./qa/runs.md#umd07mmra) | [UMD07MMRaURL](./qa/runs.md#umd07mmraurl) | [UMD07iMASCa](./qa/runs.md#umd07imasca) | [UMD07iMASCaU](./qa/runs.md#umd07imascau) | [UMD07MMRb](./qa/runs.md#umd07mmrb) | [UMD07iMASCb](./qa/runs.md#umd07imascb)

??? abstract "Abstract"
	
	Information needs are complex, evolving, and difficult to express or capture (Taylor, 1962), a fact that is often overlooked by modern information retrieval systems. TREC, through the HARD track, has been attempting to introduce elements of interaction into large-scale evaluations in order to achieve high accuracy document retrieval (Allan, 2005). Previous research has shown that well-constructed clarification questions can yield a better understanding of users' information needs and thereby improve retrieval performance (Lin et al., 2006). Interactive question answering has recently become a focus of research in the context of complex QA. The topics in the ciQA task are substantially different from factoid questions in that the information needs are complex, multi-faceted, and often not well defined or expressed. To investigate the role of interaction in complex QA, we experimented with two approaches. The first approach relied on Maximum Marginal Relevance (MMR) and is described in Section 2. The second approach employed the Multiple Alternative Sentence Compressions (MASC) framework (Zajic, 2007; Madnani et al., 2007), described in Section 3. Section 4 presents official results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MadnaniLD07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MadnaniLD07,
		author = {Nitin Madnani and Jimmy Lin and Bonnie J. Dorr},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 ciQA Task: University of Maryland},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/umd.qa.final.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MadnaniLD07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Lymba's PowerAnswer 4 in TREC 2007

_Dan I. Moldovan, Christine Clark, Moldovan Bowden_

- :fontawesome-solid-user-group: **Participant:** [lymba.clark](./qa/participants.md#lymba.clark)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/lymba.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/lymba.qa.final.pdf)
- :material-file-search: **Runs:** [LymbaPA07](./qa/runs.md#lymbapa07)

??? abstract "Abstract"
	
	This paper reports on Lymba Corporation's (a spinoff of Language Computer Corporation) participation in the TREC 2007 Question Answering track. An overview of the Power-Answer 4 question answering system and a discussion of new features added to meet the challenges of this year's evaluation are detailed. Special attention was given to methods for incorporating blogs into the searchable collection, methods for improving answer precision, both statistical and knowledge driven, new mechanisms for recognizing named entities, events, and time expressions, and updated pattern-driven approaches to answer definition questions. Lymba's results in the evaluation are presented at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoldovanCB07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoldovanCB07,
		author = {Dan I. Moldovan and Christine Clark and Moldovan Bowden},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Lymba's PowerAnswer 4 in {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/lymba.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoldovanCB07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDUQA on TREC 2007 QA Track

_Xipeng Qiu, Bo Li, Chao Shen, Lide Wu, Xuanjing Huang, Yaqian Zhou_

- :fontawesome-solid-user-group: **Participant:** [fudanu.wu](./qa/participants.md#fudanu.wu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fudan.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fudan.qa.final.pdf)
- :material-file-search: **Runs:** [FDUQAT16A](./qa/runs.md#fduqat16a) | [FDUQAT16B](./qa/runs.md#fduqat16b) | [FDUQAT16C](./qa/runs.md#fduqat16c)

??? abstract "Abstract"
	
	In this year's QA track, we only participant in the main task[Dang 2006]. There are two changes in this year. One change is that time dependent questions are added, and the other is that the corpus is consisted by two collections with different qualities. Therefore, we need add some time limitation in answer filter and merge the answers from two different datasets. The preprocess step is same as our system in TREC QA 2006[Zhou et al. 2006]. We firstly index the documents for fast retrieval. The search engine used in our system is Lucene, an open source document retrieval system. We build four different indexing files. The first two are indexed based on the whole document and the single paragraph of original articles respectively. The rest two are indexed based on the whole document and single paragraph of the morphed articles. Before analyzing question, we process the questions with our question series anaphora resolution. Our modifications mainly are done for factoid questions and definition questions. For list questions, we used the system in TREC 2006[Zhou et al. 2006]. The only modification is that we used a natural paragraph as a unit to index instead of three sentences. For factoid questions, we added query expansion and time filter to our system. For definition questions, we integrate the language model and syntactic features to rank the candidate sentences, and remove the redundancies on sub-sentence level. The rest of the paper is arranged as follows. Section 2, 3 describe our system of factoid and definition questions respectively. Section 4 presents our results in TREC 2007. At last, we give our conclusions in section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiuLSWHZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiuLSWHZ07,
		author = {Xipeng Qiu and Bo Li and Chao Shen and Lide Wu and Xuanjing Huang and Yaqian Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDUQA} on {TREC} 2007 {QA} Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fudan.qa.final.pdf},
		timestamp = {Thu, 23 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiuLSWHZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concordia University at the TREC 2007 QA Track

_Majid Razmara, Andrew Fee, Leila Kosseim_

- :fontawesome-solid-user-group: **Participant:** [concordiau.kosseim](./qa/participants.md#concordiau.kosseim)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/concordiau.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/concordiau.qa.final.pdf)
- :material-file-search: **Runs:** [QASCU1](./qa/runs.md#qascu1) | [QASCU2](./qa/runs.md#qascu2) | [QASCU3](./qa/runs.md#qascu3)

??? abstract "Abstract"
	
	In this paper, we describe the system we used for the trec-2007 Question Answering Track. For factoid questions our redundancy-based approach using a modified version of aranea was enhanced further. Our list question answerer uses a clustering method to group the candidate answers that co-occur together. It also uses the target and question keywords as spies to pinpoint the right cluster of candidates. To answer other types of questions, our system extracts from Wikipedia articles a list of interest-marking terms and uses them to extract and score sentences from the aquaint-2 and blog document collections using various interest-marking triggers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RazmaraFK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/RazmaraFK07,
		author = {Majid Razmara and Andrew Fee and Leila Kosseim},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concordia University at the {TREC} 2007 {QA} Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/concordiau.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RazmaraFK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IITD-IBMIRL System for Question Answering Using Pattern Matching,  Semantic Type and Semantic Category Recognition

_Ashish Kumar Saxena, Ganesh Viswanath Sambhu, Saroj Kaushik, L. Venkata Subramaniam_

- :fontawesome-solid-user-group: **Participant:** [iit-delhi.saxena](./qa/participants.md#iit-delhi.saxena)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/iit-delhi-ibm-india.qa.pdf](http://trec.nist.gov/pubs/trec16/papers/iit-delhi-ibm-india.qa.pdf)
- :material-file-search: **Runs:** [IITDIBM2007F](./qa/runs.md#iitdibm2007f) | [IITDIBM2007S](./qa/runs.md#iitdibm2007s) | [IITDIBM2007T](./qa/runs.md#iitdibm2007t)

??? abstract "Abstract"
	
	A Question Answering (QA) system aims to return exact answers to natural language questions. While today information retrieval techniques are quite successful at locating within large collections of documents those that are relevant to a user's query, QA techniques that extract the exact answer from these retrieved documents still do not obtain very good accuracies. We approached the TREC 2007 Question Answering task as a semantics based question to answer matching problem. Given a question we aimed to extract the relevant semantic entities in it so that we can pin-point the answer. In this paper we show that our technique obtains reasonable accuracy compared to other systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SaxenaSKS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SaxenaSKS07,
		author = {Ashish Kumar Saxena and Ganesh Viswanath Sambhu and Saroj Kaushik and L. Venkata Subramaniam},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IITD-IBMIRL} System for Question Answering Using Pattern Matching, Semantic Type and Semantic Category Recognition},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/iit-delhi-ibm-india.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SaxenaSKS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Semantic Extensions of the Ephyra QA System for TREC 2007

_Nico Schlaefer, Jeongwoo Ko, Justin Betteridge, Manas A. Pathak, Eric Nyberg, Guido Sautter_

- :fontawesome-solid-user-group: **Participant:** [ukarlsruhe-cmu.schlaefer](./qa/participants.md#ukarlsruhe-cmu.schlaefer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/cmu-ukarlsruhe.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/cmu-ukarlsruhe.qa.final.pdf)
- :material-file-search: **Runs:** [Ephyra1](./qa/runs.md#ephyra1) | [Ephyra2](./qa/runs.md#ephyra2) | [Ephyra3](./qa/runs.md#ephyra3)

??? abstract "Abstract"
	
	We describe recent extensions to the Ephyra question answering (QA) system and their evaluation in the TREC 2007 QA track. Existing syntactic answer extraction approaches for factoid and list questions have been complemented with a high-accuracy semantic approach that generates a semantic representation of the question and extracts answer candidates from similar semantic structures in the corpus. Candidates found by different answer extractors are combined and ranked by a statistical framework that integrates a variety of answer validation techniques and similarity measures to estimate a probability for each candidate. A novel answer type classifier combines a statistical model and hand-coded rules to predict the answer type based on syntactic and semantic features of the question. Our approach for the 'other' questions uses Wikipedia and Google to judge the relevance of answer candidates found in the corpora.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchlaeferKBPNS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchlaeferKBPNS07,
		author = {Nico Schlaefer and Jeongwoo Ko and Justin Betteridge and Manas A. Pathak and Eric Nyberg and Guido Sautter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Semantic Extensions of the Ephyra {QA} System for {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/cmu-ukarlsruhe.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchlaeferKBPNS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Alyssa System at TREC QA 2007: Do We Need Blog06?

_Dan Shen, Michael Wiegand, Andreas Merkel, Stefan Kazalski, Sabine Hunsicker, Jochen L. Leidner, Dietrich Klakow_

- :fontawesome-solid-user-group: **Participant:** [saarlandu.shen](./qa/participants.md#saarlandu.shen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/saarlandu.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/saarlandu.qa.final.pdf)
- :material-file-search: **Runs:** [lsv2007a](./qa/runs.md#lsv2007a) | [lsv2007b](./qa/runs.md#lsv2007b) | [lsv2007c](./qa/runs.md#lsv2007c)

??? abstract "Abstract"
	
	We describe the participation of the Saarland University LSV group in the DARPA/NIST TREC 2007 Q&A track with the Alyssa system, using an approach that combines cascaded language-model based information retrieval (LMIR) with data-driven learning methods for answer extraction and ranking. To test the robustness of this approach that was previously proven on news data also across document collections of varying levels of subjectivity, we test the hypothesis that the answer accuracy over factoid questions does not decrease significantly if blog data is added. Our results show that on the contrary, the method remains competitive on larger datasets with mixed content, such as the union of the AQUAINT 2 (news) and BLOG 06 (blog) corpora (Macdonald and Ounis, 2006). We also present evaluation results on an unofficial set of questions manually generated from BLOG 06 documents, which were created at LSV.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShenWMKHLK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShenWMKHLK07,
		author = {Dan Shen and Michael Wiegand and Andreas Merkel and Stefan Kazalski and Sabine Hunsicker and Jochen L. Leidner and Dietrich Klakow},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Alyssa System at {TREC} {QA} 2007: Do We Need Blog06?},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/saarlandu.qa.final.pdf},
		timestamp = {Mon, 17 Apr 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ShenWMKHLK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass Complex Interactive Question Answering (ciQA) 2007: Human Performance  as Question Answerers

_Mark D. Smucker, James Allan, Blagovest Dachev_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./qa/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umass.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umass.qa.final.pdf)
- :material-file-search: **Runs:** [UMassBaseAut](./qa/runs.md#umassbaseaut) | [UMass1](./qa/runs.md#umass1) | [UMass2](./qa/runs.md#umass2) | [UMassIntA](./qa/runs.md#umassinta) | [UMassIntM](./qa/runs.md#umassintm)

??? abstract "Abstract"
	
	Every day, people widely use information retrieval (IR) systems to answer their questions. We utilized the TREC 2007 complex, interactive question answering (ciQA) track to measure the performance of humans using an interactive IR system to answer questions. Using our IR system, assessors searched for relevant documents and recorded answers to their questions. We submitted the assessors' answers without modification as one of our runs. For our other submission, one of the authors used our IR system for an unlimited time and recorded answers to the questions. We found that human performance using an interactive IR system for question answering is variable but that interactive IR systems offer the potential for superior question answering performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmuckerAD07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmuckerAD07,
		author = {Mark D. Smucker and James Allan and Blagovest Dachev},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass Complex Interactive Question Answering (ciQA) 2007: Human Performance as Question Answerers},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/umass.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmuckerAD07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FSC at TREC

_Stephen Taylor, Orlando Montalvo-Huhn, Nikhil Kartha_

- :fontawesome-solid-user-group: **Participant:** [fitchburg-state.taylor](./qa/participants.md#fitchburg-state.taylor)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fitchburg.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fitchburg.qa.final.pdf)
- :material-file-search: **Runs:** [eduFsc04](./qa/runs.md#edufsc04) | [eduFsc05](./qa/runs.md#edufsc05)

??? abstract "Abstract"
	
	This is the rst time that Fitchburg State College has entered the competition and the rst project that the students had worked on of this sort. We decided that we would split our time between building an infrastructure and on speci c techniques for information processing, and to use the project to help us understand the problem better for subsequent years. Because of the time we needed to research and understand the problem and when we started we had a real time constraint. We decided to do some fast prototyping and use simple information processing techniques to test the basic infrastructure. To allow for easier insertion of more complex methods we decided on a layered approach to the information processing. A three layer approach seemed to make the most sense. The rst layer would nd the document that may have the answer. The second would try to nd the sentence that answered the question. And the third would try to extract the answer from the sentence. We wanted to try a number of di erent approaches to processing information at each layer. However because of lack of time, we only got a chance to try a few. We spent much of time experimenting with the document retrieval portion. Even when you nd a method, you need time to play with the parameters with the weight multiplier and any number of tweaks. Unfortunately, we didn't get much time to do that.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TaylorMK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/TaylorMK07,
		author = {Stephen Taylor and Orlando Montalvo{-}Huhn and Nikhil Kartha},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FSC} at {TREC}},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fitchburg.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TaylorMK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2007 Question Answering Experiments at Tokyo Institute of Technology

_Edward W. D. Whittaker, Matthias H. Heie, Josef R. Novak, Sadaoki Furui_

- :fontawesome-solid-user-group: **Participant:** [tokyo-inst-tech.whittaker](./qa/participants.md#tokyo-inst-tech.whittaker)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/tokyo-it.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/tokyo-it.qa.final.pdf)
- :material-file-search: **Runs:** [asked07a](./qa/runs.md#asked07a) | [asked07b](./qa/runs.md#asked07b) | [asked07c](./qa/runs.md#asked07c)

??? abstract "Abstract"
	
	In this paper we describe Tokyo Institute of Technology's attempt at the TREC2007 question answering (QA) track. Keeping the same theoretical QA model as for the TREC2006 task, this year we once again focused on the factoid QA task, while investigating a new method for sentence retrieval. We deviated from our earlier approach of using web data, and instead relied solely on the supplied news wire and blog data. Our factoid and list score fell significantly from last year, while we achieved a higher other question score compared to TREC2006, using sentence retrieval rather than last year's summarization method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WhittakerHNF07.bib) "
	```
	@inproceedings{DBLP:conf/trec/WhittakerHNF07,
		author = {Edward W. D. Whittaker and Matthias H. Heie and Josef R. Novak and Sadaoki Furui},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 Question Answering Experiments at Tokyo Institute of Technology},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/tokyo-it.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WhittakerHNF07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UAlbany's ILQUA at TREC 2007

_Min Wu, Song Chen, Yu Zhan, Tomek Strzalkowski_

- :fontawesome-solid-user-group: **Participant:** [suny-albany.wu](./qa/participants.md#suny-albany.wu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ualbany-suny.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ualbany-suny.qa.final.pdf)
- :material-file-search: **Runs:** [ILQUA1](./qa/runs.md#ilqua1) | [ILQUA2](./qa/runs.md#ilqua2)

??? abstract "Abstract"
	
	TREC2007 QA track introduced a combined collection of 175GB BLOG data and 2.5GB newswire data. This introduced an additional challenge for an automatic QA system to processes data in different formats without sacrificing the accuracy. In ILQUA we added a data preprocessing component to filter out noisy blog data. ILQUA has been built as an IE-driven QA system; it extracts answers from documents annotated with named entity tags. Answer extraction methods applied are surface text pattern matching, n-gram proximity search and syntactic dependency matching. The answer patterns used in ILQUA are automatically summarized by a supervised learning system and represented in form of regular expressions which contain multiple question terms. In addition to surface text pattern matching, we also adopt N-gram proximity search and syntactic dependency matching. N-grams of question terms are matched around every named entity in the candidate passages and a list of named entities are extracted as answer candidate. These named entities then go through a multi-level syntactic dependency matching component until a final answer is chosen. This year, we modified the component that tackles “Other” questions and applied different method in the two runs we submitted. One method utilized representative words and syntactic patterns, while the other method utilized representative words from TREC data and web data. Figure 1 gives an illustration of components, data flow and control flow of ILQUA. The following sections give detailed discussion of each component of the system, evaluation results, conclusion and future work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuSZS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuSZS07,
		author = {Min Wu and Song Chen and Yu Zhan and Tomek Strzalkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UAlbany's {ILQUA} at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ualbany-suny.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuSZS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2007 ciQA Track at RMIT and CSIRO

_Mingfang Wu, Andrew Turpin, Falk Scholer, Yohannes Tsegay, Ross Wilkinson_

- :fontawesome-solid-user-group: **Participant:** [rmitu.scholer](./qa/participants.md#rmitu.scholer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/rmit-csiro.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/rmit-csiro.qa.final.pdf)
- :material-file-search: **Runs:** [rmitrun1](./qa/runs.md#rmitrun1) | [rmitrun2](./qa/runs.md#rmitrun2) | [rmitrun3](./qa/runs.md#rmitrun3) | [rmitrun4](./qa/runs.md#rmitrun4) | [rmitrun5](./qa/runs.md#rmitrun5) | [rmitrun6](./qa/runs.md#rmitrun6)

??? abstract "Abstract"
	
	As part of our participation in the 2007 CiQA track, the RMIT and CSIRO team investigated the following three research questions: 1. What contextual words are helpful in improving answer quality? 2. Given two answer lists of different quality, which list would a user prefer? 3. Would a user's preference choice be correlated with her own relevance judgement of an individual list? To explore these questions, we submitted: Four system runs with various query formulation strategies; Two interactive runs, with one interface for the preference choice, and the other one for the relevance judgement of each answer sentence from an answer list.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuTSTW07.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuTSTW07,
		author = {Mingfang Wu and Andrew Turpin and Falk Scholer and Yohannes Tsegay and Ross Wilkinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 ciQA Track at {RMIT} and {CSIRO}},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/rmit-csiro.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuTSTW07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Michigan State University at the 2007 TREC ciQA Task

_Chen Zhang, Matthew Gerber, Tyler Baldwin, Steve Emelander, Joyce Yue Chai, Rong Jin_

- :fontawesome-solid-user-group: **Participant:** [mich-stateu.cha](./qa/participants.md#mich-stateu.cha)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/michiganu.qa.final.pdf](http://trec.nist.gov/pubs/trec16/papers/michiganu.qa.final.pdf)

??? abstract "Abstract"
	
	This is our first participation in the ciQA task. Instead of exploring conversation strategies in question answering [3, 4], we decided to focus on simple interaction strategies using relevance feedback. In our view, the ciQA task is not designed to evaluate user initiative interaction strategies. Since NIST assessors act as users, the motivation to take an initiative is lacking. It is not clear how to encourage the assessors to take the initiative (e.g., by asking additional questions) during the interaction process. We feel in such a setting, relevance feedback or any kind of system initiative interaction strategies seem more appropriate. Therefore, we have focused on variations of relevance feedback in this year's evaluation. For the initial runs, our two submissions were based on two distinct approaches, a heuristic approach and a machine learning approach. Since only two interactive runs can be submitted for evaluation, we decided to focus on one aspect of variation. The only difference between the two interactive and final run systems is how the feedback is solicited and incorporated. Since there are many parameters inherent in the evaluation that affect the outcome of the final runs, only varying one parameter will hopefully allow us to make some preliminary observations about how feedback solicitation can affect final performance. Although manual runs were allowed in this evaluation, all of our runs were created automatically. The following steps were taken during the evaluation. For each topic, the system first generated a query based on its question template and narrative and used this query to retrieve relevant documents. The retrieved documents were then segmented into sentences, which were further ranked and put together as the initial run results. The interactive web pages were generated based on the results from the initial runs. These pages were accessed by NIST assessors. Feedback from assessors was used to create the final run results. In the following sections, we describe in detail the steps taken to create our initial runs and final runs. We also discuss what we have learned from this exercise.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangGBECJ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangGBECJ07,
		author = {Chen Zhang and Matthew Gerber and Tyler Baldwin and Steve Emelander and Joyce Yue Chai and Rong Jin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Michigan State University at the 2007 {TREC} ciQA Task},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/michiganu.qa.final.pdf},
		timestamp = {Wed, 05 Jan 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangGBECJ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Enterprise 

#### Overview of the TREC 2007 Enterprise Track

_Peter Bailey, Arjen P. de Vries, Nick Craswell, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ENT.OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/ENT.OVERVIEW16.pdf)
??? abstract "Abstract"
	
	The goal of the enterprise track is to conduct experiments with enterprise data that reflect the experiences of users in real organizations. This year, the track has introduced a new corpus with the goal to be more representative of real-world enterprise search, by involving actual members of the organization in the topic development process, performing their real work tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BaileyVCS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/BaileyVCS07,
		author = {Peter Bailey and Arjen P. de Vries and Nick Craswell and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2007 Enterprise Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ENT.OVERVIEW16.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BaileyVCS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring the Legal Discovery and Enterprise Tracks at the University  of Iowa

_Brian Almquist, Viet Ha-Thuc, Aditya Kumar Sehgal, Robert J. Arens, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [uiowa.srinivasan](./enterprise/participants.md#uiowa.srinivasan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uiowa.legal.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uiowa.legal.ent.final.pdf)
- :material-file-search: **Runs:** [uiowa07entD1](./enterprise/runs.md#uiowa07entd1) | [uiowa07entD2](./enterprise/runs.md#uiowa07entd2) | [uiowa07entD3](./enterprise/runs.md#uiowa07entd3) | [uiowa07entD4](./enterprise/runs.md#uiowa07entd4) | [uiowa07entE2](./enterprise/runs.md#uiowa07ente2) | [uiowa07entE1](./enterprise/runs.md#uiowa07ente1)

??? abstract "Abstract"
	
	The University of Iowa Team, under coordinating professor Padmini Srinivasan, participated in the legal discovery and enterprise tracks of TREC-2007.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlmquistHSAS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlmquistHSAS07,
		author = {Brian Almquist and Viet Ha{-}Thuc and Aditya Kumar Sehgal and Robert J. Arens and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploring the Legal Discovery and Enterprise Tracks at the University of Iowa},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uiowa.legal.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlmquistHSAS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2007 Enterprise Track at CSIRO

_Peter Bailey, Deepak Agrawal, Anuj Kumar_

- :fontawesome-solid-user-group: **Participant:** [csiro-ict.bailey](./enterprise/participants.md#csiro-ict.bailey)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/csiro.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/csiro.ent.final.pdf)
- :material-file-search: **Runs:** [CSIROdsQonly](./enterprise/runs.md#csirodsqonly) | [CSIROdsQnarr](./enterprise/runs.md#csirodsqnarr) | [CSIROdsQfb](./enterprise/runs.md#csirodsqfb) | [CSIROdsQsimp](./enterprise/runs.md#csirodsqsimp) | [CSIROesQonly](./enterprise/runs.md#csiroesqonly) | [CSIROesQnarr](./enterprise/runs.md#csiroesqnarr) | [CSIROesQpage](./enterprise/runs.md#csiroesqpage) | [CSIROesQprof](./enterprise/runs.md#csiroesqprof)

??? abstract "Abstract"
	
	The goals of CSIRO's participation in the Enterprise track were formed by the nature of the tasks. With the expert finding search task, we sought to use a variety of means to associate topical expertise with individuals previously located within the collection. With the document search task, we were primarily interested in exploring issues of result diversity based on different characterisations of documents within the collection. We completed both expert and document search tasks by the submission deadline. In both cases, we submitted four runs for each task. The algorithms used for the runs for both tasks used a query-only baseline with subsequent variations. In both cases, we incorporated use of the PADRE retrieval system [2], in which the Okapi BM25 relevance function was implemented as the core ranking component. Incorporation of additional evidence such as anchor text and other characteristics of Web documents is used in the default ranking formula associated with the retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BaileyAK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/BaileyAK07,
		author = {Peter Bailey and Deepak Agrawal and Anuj Kumar},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 Enterprise Track at {CSIRO}},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/csiro.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BaileyAK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query and Document Models for Enterprise Search

_Krisztian Balog, Katja Hofmann, Wouter Weerkamp, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.deRijke](./enterprise/participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uamsterdam-balog.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uamsterdam-balog.ent.final.pdf)
- :material-file-search: **Runs:** [uams07bl](./enterprise/runs.md#uams07bl) | [uams07pr](./enterprise/runs.md#uams07pr) | [uams07bfb](./enterprise/runs.md#uams07bfb) | [uams07bfbex](./enterprise/runs.md#uams07bfbex) | [uams07exbl](./enterprise/runs.md#uams07exbl) | [uams07exmm](./enterprise/runs.md#uams07exmm) | [uams07expp](./enterprise/runs.md#uams07expp) | [uams07exfr](./enterprise/runs.md#uams07exfr)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2007 Enterprise track and detail our language modeling-based approaches. For document search, our focus was on estimating a mixture model using a standard web collection, and on constructing query models by employing blind relevance feedback and using the example documents provided with the topics. We found that settings performing well on a web collection do not carry over to the CSIRO collection, but the use of advanced query models resulted in significant improvements. In expert search, our experiments concerned document representation, identification of candidate experts, and combinations of expert search strategies. We find no significant difference in average precision but observe small overall positive effects of the advanced models, with large differences between individual topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogHWR07.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogHWR07,
		author = {Krisztian Balog and Katja Hofmann and Wouter Weerkamp and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Query and Document Models for Enterprise Search},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uamsterdam-balog.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalogHWR07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2007 Enterprise Track

_Jianmei Chen, Hui Ren, Linhong Xu, Hongfei Lin, Zhihao Yang_

- :fontawesome-solid-user-group: **Participant:** [dalianu.yang](./enterprise/participants.md#dalianu.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/dalianu.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/dalianu.ent.final.pdf)
- :material-file-search: **Runs:** [DUTDST1](./enterprise/runs.md#dutdst1) | [DUTDST2](./enterprise/runs.md#dutdst2) | [DUTDST3](./enterprise/runs.md#dutdst3) | [DUTDST4](./enterprise/runs.md#dutdst4) | [DUTEXP1](./enterprise/runs.md#dutexp1) | [DUTEXP2](./enterprise/runs.md#dutexp2) | [DUTEXP3](./enterprise/runs.md#dutexp3) | [DUTEXP4](./enterprise/runs.md#dutexp4)

??? abstract "Abstract"
	
	This paper describes our experiments on the two tasks of the TREC 2007 Enterprise track. In data preprocessing stage we stripped the non-letter character from documents and query. For the Document Search, we built the index by indri and lemur, handled the query topic and then retrieved relevant documents by indri and lemur. For the Expert Search, we recognized candidates from collection, established correlative document pool, built the index by indri and lemur, and then got expert list and supporting documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenRXLY07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenRXLY07,
		author = {Jianmei Chen and Hui Ren and Linhong Xu and Hongfei Lin and Zhihao Yang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2007 Enterprise Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/dalianu.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenRXLY07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Research on Enterprise Track of TREC 2007 at SJTU APEX Lab

_Huizhong Duan, Qi Zhou, Zhen Lu, Ou Jin, Shenghua Bao, Yunbo Cao, Yong Yu_

- :fontawesome-solid-user-group: **Participant:** [sjtu-apex-ent](./enterprise/participants.md#sjtu-apex-ent)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/sjtu-apex.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/sjtu-apex.ent.final.pdf)
- :material-file-search: **Runs:** [SJTUEntDS01](./enterprise/runs.md#sjtuentds01) | [SJTUEntDS02](./enterprise/runs.md#sjtuentds02) | [SJTUEntDS03](./enterprise/runs.md#sjtuentds03) | [SJTUEntDS04](./enterprise/runs.md#sjtuentds04) | [SJTUEntES01](./enterprise/runs.md#sjtuentes01) | [SJTUEntES02](./enterprise/runs.md#sjtuentes02) | [SJTUEntES03](./enterprise/runs.md#sjtuentes03) | [SJTUEntES04](./enterprise/runs.md#sjtuentes04)

??? abstract "Abstract"
	
	This year we (APEX Lab, Shanghai Jiao Tong University) participated in both Document Search Task and Expert Search Task in Enterprise Track of TREC 2007. For Document Search Task, we generally applied BM25 formula separately on different fields of HTML pages: Title, Anchor, H1, H2, Keywords, and Extracted Body. Various Static Ranking methods are also exploited. Scores are combined together using linear combination. Among all the techniques we have embedded in our system, our highlight is the static ranking approaches. Beside this, some data preprocessing methods and similarity function will also be introduced. 1. Static Ranking Approaches. Page quality is our focus for the task. Thus we studied various static ranking methods in Enterprise Corpus. Among them, PageRank[6] and Topic Sensitive PageRank[1], which both generate similar ranks for most pages, do not work for this Corpus. Then we research on HostRank[5]. The central problem of using HostRank is to define a host. After realizing that sub-portals of an enterprise do not necessarily earn a difference, we finally used sub-layers of sub-portals (AAA.BBB.CCC/DDD) as hosts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DuanZLJBCY07.bib) "
	```
	@inproceedings{DBLP:conf/trec/DuanZLJBCY07,
		author = {Huizhong Duan and Qi Zhou and Zhen Lu and Ou Jin and Shenghua Bao and Yunbo Cao and Yong Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Research on Enterprise Track of {TREC} 2007 at {SJTU} {APEX} Lab},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/sjtu-apex.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DuanZLJBCY07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2007: Enterprise Document Search

_Yu Fan, Xiangji Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./enterprise/participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/yorku.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/yorku.ent.final.pdf)
- :material-file-search: **Runs:** [york07ed1](./enterprise/runs.md#york07ed1) | [york07ed2](./enterprise/runs.md#york07ed2) | [york07ed3](./enterprise/runs.md#york07ed3) | [york07ed4](./enterprise/runs.md#york07ed4)

??? abstract "Abstract"
	
	York University evaluated a prepcessing approach for this year's enterprise document search task. With different parsing tools, we create two data sets. Based on each data set, we generate two official runs. Their results demonstrate that the removal of raw data in preprocessing stage has a negative impact on the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FanH07.bib) "
	```
	@inproceedings{DBLP:conf/trec/FanH07,
		author = {Yu Fan and Xiangji Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2007: Enterprise Document Search},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/yorku.ent.final.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FanH07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2007: Enterprise Track

_Yupeng Fu, Yufei Xue, Tong Zhu, Yiqun Liu, Min Zhang, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghuau.zhang](./enterprise/participants.md#tsinghuau.zhang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/tsinghuau-zhang.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/tsinghuau-zhang.ent.final.pdf)
- :material-file-search: **Runs:** [THUDSANCHOR](./enterprise/runs.md#thudsanchor) | [THUDSFULLSR](./enterprise/runs.md#thudsfullsr) | [THUDSSEL](./enterprise/runs.md#thudssel) | [THUDSSELSR](./enterprise/runs.md#thudsselsr) | [THUIRMPDD4](./enterprise/runs.md#thuirmpdd4) | [THUIRPDD2C40](./enterprise/runs.md#thuirpdd2c40) | [THUIRMPDD2](./enterprise/runs.md#thuirmpdd2) | [THUIRPDD2](./enterprise/runs.md#thuirpdd2)

??? abstract "Abstract"
	
	We participate in document search and expert search of Enterprise Track in TREC2007. The motive behind the TREC Enterprise Track is to study the issues searching the documents and experts inside an enterprise environment, which has not been sufficiently addressed in research. In document search, we focus on the key overview page pre-selection methods and link analysis algorithms. In expert search, we develop methods to detect expert identifiers and experimented based on our previous PDD model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FuXZLZM07.bib) "
	```
	@inproceedings{DBLP:conf/trec/FuXZLZM07,
		author = {Yupeng Fu and Yufei Xue and Tong Zhu and Yiqun Liu and Min Zhang and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2007: Enterprise Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/tsinghuau-zhang.ent.final.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FuXZLZM07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2007: Experiments in Blog and Enterprise  Tracks with Terrier

_David Hannah, Craig Macdonald, Jie Peng, Ben He, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [glasgow.ounis](./enterprise/participants.md#glasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uglasgow.blog.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uglasgow.blog.ent.final.pdf)
- :material-file-search: **Runs:** [uogEDSF](./enterprise/runs.md#uogedsf) | [uogEDSINLPRI](./enterprise/runs.md#uogedsinlpri) | [uogEDSComPri](./enterprise/runs.md#uogedscompri) | [uogEDSCLCDIS](./enterprise/runs.md#uogedsclcdis) | [uogEXFeMNZP](./enterprise/runs.md#uogexfemnzp) | [uogEXFeMNZcP](./enterprise/runs.md#uogexfemnzcp) | [uogEXFeMNZdQ](./enterprise/runs.md#uogexfemnzdq) | [uogEXFeMNZQE](./enterprise/runs.md#uogexfemnzqe)

??? abstract "Abstract"
	
	In TREC 2007, we participate in four tasks of the Blog and Enterprise tracks. We continue experiments using Terrier1 [14], our modular and scalable Information Retrieval (IR) platform, and the Divergence From Randomness (DFR) framework. In particular, for the Blog track opinion finding task, we propose a statistical term weighting approach to identify opinionated documents. An alternative approach based on an opinion identification tool is also utilised. Overall, a 15% improvement over a non-opinionated baseline is observed in applying the statistical term weighting approach. In the Expert Search task of the Enterprise track, we investigate the use of proximity between query terms and candidate name occurrences in documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HannahMPHO07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HannahMPHO07,
		author = {David Hannah and Craig Macdonald and Jie Peng and Ben He and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2007: Experiments in Blog and Enterprise Tracks with Terrier},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uglasgow.blog.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HannahMPHO07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIR at TREC 2007 Expert Search Task

_Jiepu Jiang, Wei Lu, Dan Liu_

- :fontawesome-solid-user-group: **Participant:** [wuhanu.lu](./enterprise/participants.md#wuhanu.lu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/wuhanu.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/wuhanu.ent.final.pdf)
- :material-file-search: **Runs:** [WHU10](./enterprise/runs.md#whu10) | [WHU15](./enterprise/runs.md#whu15) | [WHUC5](./enterprise/runs.md#whuc5) | [WHUE10](./enterprise/runs.md#whue10)

??? abstract "Abstract"
	
	This is the second year for the participation of Center for Studies of Information Resources (CSIR) in the TREC Expert Search Task. Rather than using the candidate profile based approach, a simplified two stage approach is used in our experiment, that is, documents are ranked based on topics, and each expert is scored intuitively by the weights of documents the expert appeared. Instead of the modeling of expert search, we have mainly focused on the effect of document filtering in the expert search. In our experiment, only the top n ranked topic-relevant documents where the expert also appeared are calculated into the expert score. The tuned value of n under W3C corpus for a best performance is 10, which is proved to be stable under CERC corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangLL07.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangLL07,
		author = {Jiepu Jiang and Wei Lu and Dan Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CSIR} at {TREC} 2007 Expert Search Task},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/wuhanu.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangLL07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UALR at TREC-ENT 2007

_Hemant Joshi, Sithu D. Sudarsan, Subhashish Duttachowdhury, Chuanlei Zhang, Srini Ramaswamy_

- :fontawesome-solid-user-group: **Participant:** [uarkansas-littlerock.bayrak](./enterprise/participants.md#uarkansas-littlerock.bayrak)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ualr.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ualr.ent.final.pdf)
- :material-file-search: **Runs:** [UALR07Ent1](./enterprise/runs.md#ualr07ent1) | [UALR07Ent2](./enterprise/runs.md#ualr07ent2) | [UALR07Ent3](./enterprise/runs.md#ualr07ent3) | [UALR07Ent4](./enterprise/runs.md#ualr07ent4) | [UALR07Exp1](./enterprise/runs.md#ualr07exp1) | [UALR07Exp2](./enterprise/runs.md#ualr07exp2) | [UALR07Exp3](./enterprise/runs.md#ualr07exp3)

??? abstract "Abstract"
	
	This is the first year we participated in the enterprise track. This year's enterprise track offered completely new enterprise data and two new tasks. The data offered was the CSIRO Enterprise Research Collection corpus1. The two new tasks introduced this year are Expert search and Document search. We participated in both tasks, though Document Search was our primary focus this year. We also believe that the results in our document search task might have a direct impact on the expert search task. Expert search task was to identify experts or subject matter experts given a particular topic. The goal was to drive queries regarding a certain subject be diverted to a particular set of experts. Identifying experts from the document collection is a challenging problem. We have to assert if the document is informative enough for the given topic and shows the mark of an expert. We have to also find the author of the article or the relevant name or email address mentioned. The results were to be submitted as email addresses with proof of documents that we believe are expert information for the given topic. Fifty new topics were provided by NIST2 and evaluation for expert search task was conducted with help from real-world CSIRO personnel. The document search task was to identify documents that are authoritative information about a given topic. Fifty topics were common among the document search and expert search tasks. The challenge was to determine if the document merely contained words associated with the given topic or the document was indeed the authoritative source on that topic. We had to analyze the documents relevant to the given topic and rank them according to how informative those documents are for that particular topic. We experimented with various approaches that can estimate authoritative information content contained within a document. We discuss these approaches and compare them later in this paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoshiSDZR07.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoshiSDZR07,
		author = {Hemant Joshi and Sithu D. Sudarsan and Subhashish Duttachowdhury and Chuanlei Zhang and Srini Ramaswamy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UALR} at {TREC-ENT} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ualr.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoshiSDZR07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Enterprise Search: Identifying Relevant Sentences and Using Them for  Query Expansion

_Maheedhar Kolla, Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo-olga](./enterprise/participants.md#uwaterloo-olga)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uwaterloo-vechtomova.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uwaterloo-vechtomova.ent.final.pdf)
- :material-file-search: **Runs:** [uwtbase](./enterprise/runs.md#uwtbase) | [uwKLD](./enterprise/runs.md#uwkld) | [uwRF](./enterprise/runs.md#uwrf)

??? abstract "Abstract"
	
	In this paper, we discuss the experiments conducted in context of Document Search task of 2007 Enterprise Search track. Our method is based on selecting sentences from the given relevant documents and using those selected sentences for query expansion. We observed that our method of query expansion improves system's performance over baseline run, under various methods of comparison.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KollaV07.bib) "
	```
	@inproceedings{DBLP:conf/trec/KollaV07,
		author = {Maheedhar Kolla and Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Enterprise Search: Identifying Relevant Sentences and Using Them for Query Expansion},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uwaterloo-vechtomova.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KollaV07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Twente at the TREC 2007 Enterprise Track: Modeling  Relevance Propagation for the Expert Search Task

_Pavel Serdyukov, Henning Rode, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [twenteu.serdyuko](./enterprise/participants.md#twenteu.serdyuko)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/utwente.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/utwente.ent.final.pdf)

??? abstract "Abstract"
	
	This paper describes several approaches which we used for the expert search task of the TREC 2007 Enterprise track. We studied several methods of relevance propagation from documents to related candidate experts. Instead of one-step propagation from documents to directly related candidates, used by many systems in the previous years, we do not limit the relevance flow and disseminate it further through mutual documents-candidates connections. We model relevance propagation using random walk principles, or in formal terms, discrete Markov processes. We experiment with infinite and finite number of propagation steps. We also demonstrate how additional information, namely hyperlinks among documents, organizational structure of the enterprise and relevance feedback may be utilized by the presented techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SerdyukovRH07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SerdyukovRH07,
		author = {Pavel Serdyukov and Henning Rode and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Twente at the {TREC} 2007 Enterprise Track: Modeling Relevance Propagation for the Expert Search Task},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/utwente.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SerdyukovRH07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Research on Enterprise Track of TREC 2007

_Huawei Shen, Guoyao Chen, Haiqiang Chen, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-liu](./enterprise/participants.md#cas-liu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/cas-liu.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/cas-liu.ent.final.pdf)
- :material-file-search: **Runs:** [DocRun01](./enterprise/runs.md#docrun01) | [DocRun02](./enterprise/runs.md#docrun02) | [DocRun03](./enterprise/runs.md#docrun03) | [DocRun04](./enterprise/runs.md#docrun04) | [ExpertRun04](./enterprise/runs.md#expertrun04) | [ExpertRun03](./enterprise/runs.md#expertrun03) | [ExpertRun01](./enterprise/runs.md#expertrun01) | [ExpertRun02](./enterprise/runs.md#expertrun02)

??? abstract "Abstract"
	
	We (ICT-CAS team) participated in the Enterprise Track of TREC 2007. This paper reports our experimental results on this track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShenCCLC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShenCCLC07,
		author = {Huawei Shen and Guoyao Chen and Haiqiang Chen and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Research on Enterprise Track of {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/cas-liu.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShenCCLC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at the TREC 2007 Enterprise Track

_Mingfang Wu, Falk Scholer, Milad Shokouhi, Simon J. Puglisi, Halil Ali_

- :fontawesome-solid-user-group: **Participant:** [rmitu.scholer](./enterprise/participants.md#rmitu.scholer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/rmit.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/rmit.ent.final.pdf)
- :material-file-search: **Runs:** [RmitQ](./enterprise/runs.md#rmitq) | [RmitQAnc](./enterprise/runs.md#rmitqanc) | [RmitQFir](./enterprise/runs.md#rmitqfir) | [RmitQAncIndg](./enterprise/runs.md#rmitqancindg)

??? abstract "Abstract"
	
	At TREC 2007, RMIT University participated in the document search task of the enterprise track. Our goals were to investigate: 1. Which sources of external evidence (anchor text, PageRank and Indegree) are useful for improving a document-based ranking scheme for a key page finding task? 2. Should the different source of evidence be used in isolation, or in combination? 3. Can federated search improve performance over single collection search, for example when the collection is divided into discipline or business-function related categories? In this paper, we discuss our approaches to these three questions and present experimental result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuSSPA07.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuSSPA07,
		author = {Mingfang Wu and Falk Scholer and Milad Shokouhi and Simon J. Puglisi and Halil Ali},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at the {TREC} 2007 Enterprise Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/rmit.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuSSPA07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIM at TREC 2007

_Jun Xu, Jing Yao, Jiaqian Zheng, Qi Sun, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [fudanu.niu](./enterprise/participants.md#fudanu.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf)
- :material-file-search: **Runs:** [FDUBase](./enterprise/runs.md#fdubase) | [FDUExpan](./enterprise/runs.md#fduexpan) | [FDUFeedT](./enterprise/runs.md#fdufeedt) | [FDUFeedH](./enterprise/runs.md#fdufeedh) | [FDUn5e5](./enterprise/runs.md#fdun5e5) | [FDUn3e7](./enterprise/runs.md#fdun3e7) | [FDUn7e3](./enterprise/runs.md#fdun7e3) | [FDUGroup](./enterprise/runs.md#fdugroup)

??? abstract "Abstract"
	
	This paper introduced the four tracks that WIM-Lab Fudan University had taken part in at TREC 2007. For spam track, a multi-centre model was proposed considering the characteristics of spam mails in contrast of traditional 2-class classification methodology, and the incremental clustering and closeness-based classification methods were applied this year. For enterprise track, our research was mainly focused on ranking functions of experts and selecting correct supporting documents regarding to a given topic. For legal track, the effects of word distribution model in query expansion and various corpus pre-processing methods were mainly evaluated. For genomics track, three score methods were proposed to find the most relevant text snippets to a given topic. This paper gives an overview of the methods employed for each sub tasks, and compares the results of each track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuYZSN07.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuYZSN07,
		author = {Jun Xu and Jing Yao and Jiaqian Zheng and Qi Sun and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIM} at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuYZSN07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Open University at TREC 2007 Enterprise Track

_Jianhan Zhu, Dawei Song, Stefan M. Rüger_

- :fontawesome-solid-user-group: **Participant:** [openu.zhu](./enterprise/participants.md#openu.zhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/openu.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/openu.ent.final.pdf)
- :material-file-search: **Runs:** [ouTopicOnly](./enterprise/runs.md#outopiconly) | [ouNarrRF](./enterprise/runs.md#ounarrrf) | [ouNarr](./enterprise/runs.md#ounarr) | [ouNarrAuto](./enterprise/runs.md#ounarrauto) | [ouExTitle](./enterprise/runs.md#ouextitle) | [ouExNarrRF](./enterprise/runs.md#ouexnarrrf) | [ouExNarr](./enterprise/runs.md#ouexnarr) | [ouExNarrAu](./enterprise/runs.md#ouexnarrau)

??? abstract "Abstract"
	
	The Multimedia and Information Systems group at the Knowledge Media Institute of the Open University participated in the Expert Search and Document Search tasks of the Enterprise Track in TREC 2007. In both the document and expert search tasks, we have studied the effect of anchor texts in addition to document contents, document authority, url length, query expansion, and relevance feedback in improving search effectiveness. In the expert search task, we have continued using a two-stage language model consisting of a document relevance and co-occurrence models. The document relevance model is equivalent to our approach in the document search task. We have used our innovative multiple-window-based co-occurrence approach. The assumption is that there are multiple levels of associations between an expert and his/her expertise. Our experimental results show that the introduction of additional features in addition to document contents has improved the retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuSR07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuSR07,
		author = {Jianhan Zhu and Dawei Song and Stefan M. R{\"{u}}ger},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Open University at {TREC} 2007 Enterprise Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/openu.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuSR07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Blog 

#### Overview of the TREC 2007 Blog Track

_Craig Macdonald, Iadh Ounis, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/BLOG.OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/BLOG.OVERVIEW16.pdf)
??? abstract "Abstract"
	
	The goal of the Blog track is to explore the information seeking behaviour in the blogosphere. It aims to create the required infrastructure to facilitate research into the blogosphere and to study retrieval from blogs and other related applied tasks. The track was introduced in 2006 with a main opinion finding task and an open task, which allowed participants the opportunity to influence the determination of a suitable second task for 2007 on other aspects of blogs besides their opinionated nature. As a result, we have created the first blog test collection, namely the TREC Blog06 collection, for adhoc retrieval and opinion finding. Further background information on the Blog track can be found in the 2006 track overview [2]. TREC 2007 has continued using the Blog06 collection, and saw the addition of a new main task and a new subtask, namely a blog distillation (feed search) task and an opinion polarity subtask respectively, along with a second year of the opinion finding task. NIST developed the topics and relevance judgments for the opinion finding task, and its polarity subtask. For the blog distillation task, the participating groups created the topics and the associated relevance judgments. This second year of the track has seen an increased participation compared to 2006, with 20 groups submitting runs to the opinion finding task, 11 groups submitting runs to the polarity subtask, and 9 groups submitting runs to the blog distillation task. This paper provides an overview of each task, summarises the obtained results and draws conclusions for the future. The remainder of this paper is structured as follows. Section 2 provides a short description of the used Blog06 collection. Section 3 describes the opinion finding task and its polarity subtask, providing an overview of the submitted runs, as well as a summary of the main used techniques by the participants. Section 4 describes the newly created blog distillation (feed search) task, and summarises the results of the runs and the main approaches deployed by the participating groups. We provide concluding remarks in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacdonaldOS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacdonaldOS07,
		author = {Craig Macdonald and Iadh Ounis and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/BLOG.OVERVIEW16.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacdonaldOS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FUB, IASI-CNR and University of Tor Vergata at TREC 2007 Blog  Track

_Gianni Amati, Edgardo Ambrosi, Marco Bianchi, Carlo Gaibisso, Giorgio Gambosi_

- :fontawesome-solid-user-group: **Participant:** [fondazione-ug-bordoni-netlab-team](./blog/participants.md#fondazione-ug-bordoni-netlab-team)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fub.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fub.blog.final.pdf)
- :material-file-search: **Runs:** [FIUbPL2](./blog/runs.md#fiubpl2) | [FIUdPL2](./blog/runs.md#fiudpl2) | [FIUlPL2](./blog/runs.md#fiulpl2) | [FIUlP22](./blog/runs.md#fiulp22) | [FIUlDPH](./blog/runs.md#fiuldph) | [FIUDDPH](./blog/runs.md#fiuddph)

??? abstract "Abstract"
	
	We present a fully automatic and weighted dictionary to be used in topical opinion retrieval. We also define a simple topical opinion retrieval function that is free from parameters, so that the retrieval does not need any learning or tuning phase.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiABGG07.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiABGG07,
		author = {Gianni Amati and Edgardo Ambrosi and Marco Bianchi and Carlo Gaibisso and Giorgio Gambosi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {FUB, {IASI-CNR} and University of Tor Vergata at {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fub.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiABGG07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Opinion Retrieval Experiments Using Generative Models: Experiments  for the TREC 2007 Blog Track

_Yuki Arai, Koji Eguchi_

- :fontawesome-solid-user-group: **Participant:** [kobeu.eguchi](./blog/participants.md#kobeu.eguchi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/nii.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/nii.blog.final.pdf)
- :material-file-search: **Runs:** [KobePrMIR01](./blog/runs.md#kobeprmir01) | [KobePrMIR02](./blog/runs.md#kobeprmir02) | [KobePrMIR03](./blog/runs.md#kobeprmir03) | [KobePrMIR04](./blog/runs.md#kobeprmir04) | [KobePrMIR05](./blog/runs.md#kobeprmir05) | [KobePrMIR06](./blog/runs.md#kobeprmir06)

??? abstract "Abstract"
	
	Ranking blog posts that express opinions regarding a given topic should serve a critical function in helping users. We explored a couple of methods for opinion retrieval in the framework of probabilistic language models. The first method combines topic-relevance model and opinion-relevance model, at document level, that captures topic dependence of the opinion expressions. The second method combines the aforementioned topic-opinion relevance models at sentence level, and accumulates the negative cross entropy between the combined relevance models and each sentence model to obtain a document-level score. This paper reports the overview of our methods and the evaluation results on the Opinion Retrieval Task at the TREC 2007 Blog Track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AraiE07.bib) "
	```
	@inproceedings{DBLP:conf/trec/AraiE07,
		author = {Yuki Arai and Koji Eguchi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Opinion Retrieval Experiments Using Generative Models: Experiments for the {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/nii.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AraiE07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Texas School of Information at TREC 2007

_Miles Efron, Don Turnbull, Carlos Ovalle_

- :fontawesome-solid-user-group: **Participant:** [utexas-austin.efron](./blog/participants.md#utexas-austin.efron)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/utexas-austin.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/utexas-austin.blog.final.pdf)
- :material-file-search: **Runs:** [utlc](./blog/runs.md#utlc) | [utplmu100](./blog/runs.md#utplmu100) | [utblnrr](./blog/runs.md#utblnrr) | [utblrr](./blog/runs.md#utblrr)

??? abstract "Abstract"
	
	This was the first year in which the University of Texas' School of Information (UT iSchool) participated in TREC. We limited our attention to a single task (feed distillation) within a single track (Blog). Our goal was to obtain high-precision results within a principled theoretical framework. Our system used Apache's Lucene library [1] for its core indexing and retrieval functions. We also relied on language modeling extensions to Lucene provided by the Informatics Institute at the University of Amsterdam [2]. However, We altered these libraries to enable our IR approach. In particular, our results rely on a variant of the Kullback-Leibler (KL) divergence model [3, 4]. Given a query q we derive a score for each feed f in the corpus by the negative KL-divergence between the query language model and the language model for f. In the interest of maximizing precision at low numbers of documents retrieved, we limited our analysis to each feed's RSS posts, as opposed to its complete HTML representation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EfronTO07.bib) "
	```
	@inproceedings{DBLP:conf/trec/EfronTO07,
		author = {Miles Efron and Don Turnbull and Carlos Ovalle},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Texas School of Information at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/utexas-austin.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EfronTO07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieval and Feedback Models for Blog Distillation

_Jonathan L. Elsas, Jaime Arguello, Jamie Callan, Jaime G. Carbonell_

- :fontawesome-solid-user-group: **Participant:** [cmu.dir.callan](./blog/participants.md#cmu.dir.callan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/cmu-callan.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/cmu-callan.blog.final.pdf)
- :material-file-search: **Runs:** [CMUfeed](./blog/runs.md#cmufeed) | [CMUfeedW](./blog/runs.md#cmufeedw) | [CMUentry](./blog/runs.md#cmuentry) | [CMUentryW](./blog/runs.md#cmuentryw)

??? abstract "Abstract"
	
	This paper presents our system and results for the Feed Distillation task in the Blog track at TREC 2007. Our experiments focus on two dimensions of the task: (1) a large-document model (feed retrieval) vs. a small-document model (entry or post retrieval) and (2) a novel query expansion method using the link structure and link text found within Wikipedia.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ElsasACC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ElsasACC07,
		author = {Jonathan L. Elsas and Jaime Arguello and Jamie Callan and Jaime G. Carbonell},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Retrieval and Feedback Models for Blog Distillation},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/cmu-callan.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ElsasACC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Language Modeling Approaches to Blog Postand Feed Finding

_Breyten Ernsting, Wouter Weerkamp, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.deRijke](./blog/participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uamsterdam-weerkamp.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uamsterdam-weerkamp.blog.final.pdf)
- :material-file-search: **Runs:** [uams07indbl](./blog/runs.md#uams07indbl) | [uams07topic](./blog/runs.md#uams07topic) | [uams07mmbl](./blog/runs.md#uams07mmbl) | [uams07mmq](./blog/runs.md#uams07mmq) | [uams07mmqop](./blog/runs.md#uams07mmqop) | [uams07mmqcom](./blog/runs.md#uams07mmqcom) | [uams07polqop](./blog/runs.md#uams07polqop) | [uams07polqco](./blog/runs.md#uams07polqco) | [uams07polq](./blog/runs.md#uams07polq) | [uams07polbl](./blog/runs.md#uams07polbl) | [uams07ipolt](./blog/runs.md#uams07ipolt) | [uams07bdtop](./blog/runs.md#uams07bdtop) | [uams07bdfreq](./blog/runs.md#uams07bdfreq) | [uams07bdtblm](./blog/runs.md#uams07bdtblm)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2007 Blog track. In the opinion task we looked at the differences in performance between Indri and our mixture model, the influence of external expansion and document priors to improve opinion finding; results show that an out-of-the-box Indri implementation outperforms our mixture model, and that external expansion on a news corpus is very benificial. Opinion finding can be improved using either lexicons or the number of comments as document priors. Our approach to the feed distillation task is based on aggregating post-level scores to obtain a feed-level ranking. We integrated time-based and persistence aspects into the retrieval model. After correcting bugs in our post-score aggregation module we found that time-based retrieval improves results only marginally, while persistence-based ranking results in substantial improvements under the right circumstances.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ErnstingWR07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ErnstingWR07,
		author = {Breyten Ernsting and Wouter Weerkamp and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Language Modeling Approaches to Blog Postand Feed Finding},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uamsterdam-weerkamp.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ErnstingWR07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IR-Specific Searches at TREC 2007: Genomics & Blog Experiments

_Claire Fautsch, Jacques Savoy_

- :fontawesome-solid-user-group: **Participant:** [uneuchatel.savoy](./blog/participants.md#uneuchatel.savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf)
- :material-file-search: **Runs:** [UniNEblog1](./blog/runs.md#unineblog1) | [UniNEblog2](./blog/runs.md#unineblog2) | [UniNEblog3](./blog/runs.md#unineblog3) | [UniNEblog4](./blog/runs.md#unineblog4) | [UniNEblog5](./blog/runs.md#unineblog5) | [UniNEblog6](./blog/runs.md#unineblog6)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2007 Genomics and Blog evaluation campaigns. Within these two tracks, our main intent is to go beyond simple document retrieval, using different search and filtering strategies to obtain more specific answers to user information needs. In the Genomics track, the dedicated IR system has to extract relevant text passages in support of precise user questions. This task may also be viewed as the first stage of a Question/Answering system. In the Blog track we explore various strategies for retrieving opinions from the blogsphere, which in this case involves subjective opinions about various targets entities (e.g., person, location, organization, event, product or technology). This task can be subdivided in two parts: 1) retrieve relevant information (facts) and 2) extract positive, negative or mixed opinions about the specific entity being targeted. To achieve these objectives we evaluate retrieval effectiveness using the Okapi (BM25) and various other models derived from the Divergence from Randomness (DFR) paradigm, as well as a language model (LM). Through our experiments with the Genomics corpus we find that the DFR models perform clearly better than the Okapi model (relative difference of 70%) in terms of mean average precision (MAP). Using the blog corpus, we found the opposite; the Okapi model performs slightly better than both DFR models (relative difference around 5%) and LM (relative difference 7%) model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FautschS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/FautschS07,
		author = {Claire Fautsch and Jacques Savoy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IR-Specific Searches at {TREC} 2007: Genomics {\&} Blog Experiments},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FautschS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2007: Experiments in Blog and Enterprise  Tracks with Terrier

_David Hannah, Craig Macdonald, Jie Peng, Ben He, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [glasgow.ounis](./blog/participants.md#glasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uglasgow.blog.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uglasgow.blog.ent.final.pdf)
- :material-file-search: **Runs:** [uogBOPF](./blog/runs.md#uogbopf) | [uogBOPFTDW](./blog/runs.md#uogbopftdw) | [uogBOPFProxW](./blog/runs.md#uogbopfproxw) | [uogBOPFTD](./blog/runs.md#uogbopftd) | [uogBOPFProx](./blog/runs.md#uogbopfprox) | [uogBOPFPol](./blog/runs.md#uogbopfpol) | [uogBOPFTDOF](./blog/runs.md#uogbopftdof) | [uogBDFeMNZ](./blog/runs.md#uogbdfemnz) | [uogBDFeMNZP](./blog/runs.md#uogbdfemnzp) | [uogBDFeMNZpC](./blog/runs.md#uogbdfemnzpc) | [uogBDFeMNZhA](./blog/runs.md#uogbdfemnzha)

??? abstract "Abstract"
	
	In TREC 2007, we participate in four tasks of the Blog and Enterprise tracks. We continue experiments using Terrier1 [14], our modular and scalable Information Retrieval (IR) platform, and the Divergence From Randomness (DFR) framework. In particular, for the Blog track opinion finding task, we propose a statistical term weighting approach to identify opinionated documents. An alternative approach based on an opinion identification tool is also utilised. Overall, a 15% improvement over a non-opinionated baseline is observed in applying the statistical term weighting approach. In the Expert Search task of the Enterprise track, we investigate the use of proximity between query terms and candidate name occurrences in documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HannahMPHO07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HannahMPHO07,
		author = {David Hannah and Craig Macdonald and Jie Peng and Ben He and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2007: Experiments in Blog and Enterprise Tracks with Terrier},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uglasgow.blog.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HannahMPHO07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Feed Distillation Using AdaBoost and Topic Maps

_Wai-Lung Lee, Andreas Lommatzsch, Christian Scheel_

- :fontawesome-solid-user-group: **Participant:** [uberlin.neubauer](./blog/participants.md#uberlin.neubauer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/techu-berlin.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/techu-berlin.blog.final.pdf)
- :material-file-search: **Runs:** [ADABoostM1](./blog/runs.md#adaboostm1)

??? abstract "Abstract"
	
	This paper retains the experiences by participating in TREC 2007 Blog Track 'Feed Distillation'. To perform the run various classifiers are combined, which analyze title-, content- and splog-specific features to predict the relevance of a feed related to a topic, based on the idea of AdaBoost. The implemented classifiers utilize keywords retrieved from different thesauri such as Wordnet and Wortschatz, as well as from websites providing hierarchical organized 'ontol ogy' such as the 'Open Directory Project' and Yahoo Directory. To structure the keywords, Topic Maps are utilized according to ISO/IEC 13250:2000.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeLS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeLS07,
		author = {Wai{-}Lung Lee and Andreas Lommatzsch and Christian Scheel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Feed Distillation Using AdaBoost and Topic Maps},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/techu-berlin.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeLS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in TREC 2007 Blog Opinion Task at CAS-ICT

_Xiangwen Liao, Donglin Cao, Yu Wang, Wei Liu, Songbo Tan, Hongbo Xu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-liu](./blog/participants.md#cas-liu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/cas-ict.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/cas-ict.blog.final.pdf)
- :material-file-search: **Runs:** [Relevant](./blog/runs.md#relevant) | [DrapCom](./blog/runs.md#drapcom) | [DrapOpi](./blog/runs.md#drapopi) | [DrapStm](./blog/runs.md#drapstm) | [BaseSmp](./blog/runs.md#basesmp) | [SmpStm](./blog/runs.md#smpstm) | [DrapComSub](./blog/runs.md#drapcomsub) | [DrapOpiSub](./blog/runs.md#drapopisub) | [DrapStmSub](./blog/runs.md#drapstmsub)

??? abstract "Abstract"
	
	This paper describes our participation in TREC 2007 Blog Track Tasks: Opinion retrieval and Polarity classification. As for Opinion retrieval task, a two-step approach is used to retrieve opinion relevant blog unit (that is blog post and its comments) given a query after filtering Spam blog and extracting blog unit. With Polarity Classification, Drag-push [1] based classifier is employed to get polarity of blog unit. Finally, we introduce all the runs submitted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiaoCWLTXC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiaoCWLTXC07,
		author = {Xiangwen Liao and Donglin Cao and Yu Wang and Wei Liu and Songbo Tan and Hongbo Xu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in {TREC} 2007 Blog Opinion Task at {CAS-ICT}},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/cas-ict.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiaoCWLTXC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NTU at TREC 2007 Blog Track

_Kevin Hsin-Yih Lin, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./blog/participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ntu.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ntu.blog.final.pdf)
- :material-file-search: **Runs:** [NTUAuto](./blog/runs.md#ntuauto) | [NTUAutoOp](./blog/runs.md#ntuautoop) | [NTUManual](./blog/runs.md#ntumanual) | [NTUManualOp](./blog/runs.md#ntumanualop) | [NTUManualOpP](./blog/runs.md#ntumanualopp) | [NTUAutoOpP](./blog/runs.md#ntuautoopp)

??? abstract "Abstract"
	
	We participated in the Opinion Retrieval Task and the Polarity Subtask. An SVM classifier was used to determine the opinion polarities of documents. We found that the opinion mean average precisions for the runs using the SVM classifier is better than the opinion mean average precisions for the runs produced solely by the TFIDF retrieval model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinC07,
		author = {Kevin Hsin{-}Yih Lin and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NTU} at {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ntu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLPR in TREC 2007 Blog Track

_Kang Liu, Gen Wang, Xianpei Han, Jun Zhao_

- :fontawesome-solid-user-group: **Participant:** [cas-liu-nlpr-iacas](./blog/participants.md#cas-liu-nlpr-iacas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/cas.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/cas.blog.final.pdf)
- :material-file-search: **Runs:** [NLPRPT](./blog/runs.md#nlprpt) | [NLPRPTD1](./blog/runs.md#nlprptd1) | [NLPRPTD2](./blog/runs.md#nlprptd2) | [NLPRPST](./blog/runs.md#nlprpst) | [NLPRTD](./blog/runs.md#nlprtd) | [NLPRPTONLY](./blog/runs.md#nlprptonly)

??? abstract "Abstract"
	
	This paper describes the opinion retrieval system for TREC 2007 blog track. This paper focuses on two components of the system. One component is important content block detection component which is used to extract blog contents and get rid of noises in blog pages. Another component is opinion retrieval component which is used to give each sentence an opinion score and combine it with topic score based on SVR. The evaluation proves the validity of our algorithm in the task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuWHZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuWHZ07,
		author = {Kang Liu and Gen Wang and Xianpei Han and Jun Zhao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NLPR} in {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/cas.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuWHZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Robert Gordon University at the Opinion Retrieval Task of the  2007 TREC Blog Track

_Rahman Mukras, Nirmalie Wiratunga, Robert Lothian_

- :fontawesome-solid-user-group: **Participant:** [robert-gordonu.mukras](./blog/participants.md#robert-gordonu.mukras)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/robert-gordonu.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/robert-gordonu.blog.final.pdf)
- :material-file-search: **Runs:** [rgu0](./blog/runs.md#rgu0) | [rgu1](./blog/runs.md#rgu1) | [rgu2](./blog/runs.md#rgu2) | [rgu3](./blog/runs.md#rgu3) | [rgu4](./blog/runs.md#rgu4)

??? abstract "Abstract"
	
	The Robert Gordon University (RGU) participated in the Opinion Retrieval Task of the Trec 2007 Blog Track. At the core of the system we developed is a set of training documents labeled with respect to opinion. These documents are used to train a classifier in order to classify the documents that are relevant to the given Trec topics. However, a major limitation with these training documents is that they are not always generic enough to serve as good training examples for all the 50 Trec topics. We therefore propose a solution that generalizes their content by exploiting the context of opinion related language constructs such as adjectives, verbs, and adverbs. Our system significantly improves over RGU's previous Blog Track systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MukrasWL07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MukrasWL07,
		author = {Rahman Mukras and Nirmalie Wiratunga and Robert Lothian},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Robert Gordon University at the Opinion Retrieval Task of the 2007 {TREC} Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/robert-gordonu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MukrasWL07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring Traits of Adjectives to Predict Polarity Opinion in Blogs  and Semantic Filters in Genomics

_Miguel E. Ruiz, Ying Sun, Jianqiang Wang, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [ubuffalo.ruiz](./blog/participants.md#ubuffalo.ruiz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/unorth-texas.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/unorth-texas.blog.final.pdf)
- :material-file-search: **Runs:** [UB1](./blog/runs.md#ub1) | [pUB11](./blog/runs.md#pub11) | [pUB12](./blog/runs.md#pub12) | [UB2](./blog/runs.md#ub2) | [pUB21](./blog/runs.md#pub21) | [UB3](./blog/runs.md#ub3) | [pUB32](./blog/runs.md#pub32)

??? abstract "Abstract"
	
	This paper presents the results of our team in the Genomics and Blog tracks in TREC 2007. We used the language model implementation provided by Indri for both tracks. For the BLOG track we explored the use of adjectives with in a post as a way to predict opinion polarity. Our work in the Genomics track explores two approaches to generate queries from the original topics. The first approach performs automatic term expansion using UMLS to generate a structured query that can be submitted using Indri's query language. The second approach uses a query expansion and re-ranking method based on identification of semantic relatives. This approach tries to capture the semantic of the potential answer, key terms in the topic and detection of gene/protein terms mentioned in the topic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuizSWL07.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuizSWL07,
		author = {Miguel E. Ruiz and Ying Sun and Jianqiang Wang and Hongfang Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploring Traits of Adjectives to Predict Polarity Opinion in Blogs and Semantic Filters in Genomics},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/unorth-texas.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuizSWL07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2007 Blog Track Experiments at Kobe University

_Kazuhiro Seki, Yoshihiro Kino, Shohei Sato, Kuniaki Uehara_

- :fontawesome-solid-user-group: **Participant:** [kobeu.seki](./blog/participants.md#kobeu.seki)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/kobeu.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/kobeu.blog.final.pdf)
- :material-file-search: **Runs:** [Ku](./blog/runs.md#ku) | [KuKnn](./blog/runs.md#kuknn) | [KuS](./blog/runs.md#kus) | [KuSvm](./blog/runs.md#kusvm) | [KuSvmS](./blog/runs.md#kusvms) | [kud](./blog/runs.md#kud) | [kudn](./blog/runs.md#kudn) | [kudsn](./blog/runs.md#kudsn) | [kuds](./blog/runs.md#kuds)

??? abstract "Abstract"
	
	This paper describes our approaches to the opinion retrieval and blog distillation tasks for the Blog Track. For opinion retrieval we employ a two-stage framework consisting of keyword search and opinion classification, where customer reviews collected from Amazon.com are used for feature selection. For the blog distillation task we consider all the blog posts belonging to a blog in order to estimate the relevance of the blog at large. To accomplish this, we first identify relevant blogs for a given topic by keyword search and then examine all the posts for each identified blog. In addition, we attempt to detect and discard spam blogs (splogs) and non-English blogs to improve system performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SekiKSU07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SekiKSU07,
		author = {Kazuhiro Seki and Yoshihiro Kino and Shohei Sato and Kuniaki Uehara},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 Blog Track Experiments at Kobe University},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/kobeu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SekiKSU07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2007 Blog Distillation Task

_Jangwon Seo, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./blog/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umass.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umass.blog.final.pdf)
- :material-file-search: **Runs:** [UMaTiGR](./blog/runs.md#umatigr) | [UMaTiPCS](./blog/runs.md#umatipcs) | [UMaTiPCSwGR](./blog/runs.md#umatipcswgr) | [UMaTDPCSwGR](./blog/runs.md#umatdpcswgr)

??? abstract "Abstract"
	
	The focus of the blog distillation task is finding blogs with a principle, recurring interest in a specific topic. For this task, we considered a blog as a collection of postings and used resource selection approaches. Further, we investigated techniques that penalized general blogs and combined resource selection techniques. This combination demonstrated significant improvements over baselines.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SeoC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SeoC07,
		author = {Jangwon Seo and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2007 Blog Distillation Task},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/umass.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SeoC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2007 Blog Track

_Rui Song, Qin Tang, Daming Shi, Hongfei Lin, Zhihao Yang_

- :fontawesome-solid-user-group: **Participant:** [dalianu.yang](./blog/participants.md#dalianu.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/dalianu.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/dalianu.blog.final.pdf)
- :material-file-search: **Runs:** [DUTRun1](./blog/runs.md#dutrun1) | [DUTRun4](./blog/runs.md#dutrun4) | [DUTRun4P](./blog/runs.md#dutrun4p) | [DUTRun5](./blog/runs.md#dutrun5) | [DUTRun5P](./blog/runs.md#dutrun5p) | [DUTRun2](./blog/runs.md#dutrun2) | [DUTRun1P](./blog/runs.md#dutrun1p) | [DUTRun2P](./blog/runs.md#dutrun2p) | [DUTRun3](./blog/runs.md#dutrun3) | [DUTRun3P](./blog/runs.md#dutrun3p) | [DUTRun6](./blog/runs.md#dutrun6) | [DUTRun6P](./blog/runs.md#dutrun6p) | [DUTDRun1](./blog/runs.md#dutdrun1) | [DUTDRun2](./blog/runs.md#dutdrun2) | [DUTDRun3](./blog/runs.md#dutdrun3) | [DUTDRun4](./blog/runs.md#dutdrun4)

??? abstract "Abstract"
	
	This paper describes DUTIR at TREC 2007 Blog Track. In data preprocessing, a non English language list created from the corpus was used to remove the non English blogs, blog templates were also used to extract the post and comment; in Opinion Retrieval task, information in the meta tags were also indexed; in the polarity subtask, a method based on SVM was used and the Information Gain attribute selecting method was used to assist SVM; in Feed Distillation task, three type of feeds were analyzed according to their tag structure, information extracted from particular tags of the feeds were finally indexed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SongQSLY07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SongQSLY07,
		author = {Rui Song and Qin Tang and Daming Shi and Hongfei Lin and Zhihao Yang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/dalianu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SongQSLY07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Subjective Adjectives in Opinion Retrieval from Blogs

_Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo-olga](./blog/participants.md#uwaterloo-olga)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uwaterloo.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uwaterloo.blog.final.pdf)
- :material-file-search: **Runs:** [UWbaseTerms](./blog/runs.md#uwbaseterms) | [UWbasePhrase](./blog/runs.md#uwbasephrase) | [UWopinion1](./blog/runs.md#uwopinion1) | [UWopinion2](./blog/runs.md#uwopinion2) | [UWopinion3](./blog/runs.md#uwopinion3) | [UWopinion4](./blog/runs.md#uwopinion4)

??? abstract "Abstract"
	
	The University of Waterloo participated in the opinion finding task of the Blog track. The task consists of finding blog posts (documents) containing an opinion expressed about the subject of the query. Each query represents a single “entity” that can be, for example, a person, product name, abstract concept, location or event. The relevance judgements were done on a 5-point scale: -1 - not judged, 0 - non-relevant, 1 - relevant, 2 - relevant, negative opinion; 3 - relevant, mixed positive and negative opinion, 4 - relevant, positive opinion. While many elements in the language can be used to express subjective contents, adjectives are one of the major means of expressing value judgement in English. Our approach consists in using a list of 1336 subjective adjectives manually constructed by Hatzivassiloglou and McKeown [2] for identifying opinionated contents. We hypothesise that presence of subjective adjectives within fixed-size windows around query term instances in a document is a useful feature for finding opinions directed at the query concept.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Vechtomova07.bib) "
	```
	@inproceedings{DBLP:conf/trec/Vechtomova07,
		author = {Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Subjective Adjectives in Opinion Retrieval from Blogs},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uwaterloo.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Vechtomova07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2007 Blog Track: Combining Lexicon-Based Methods  to Detect Opinionated Blogs

_Kiduk Yang, Ning Yu, Hui Zhang_

- :fontawesome-solid-user-group: **Participant:** [indianau.yang](./blog/participants.md#indianau.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/indianau.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/indianau.blog.final.pdf)
- :material-file-search: **Runs:** [oqlr2f2opt](./blog/runs.md#oqlr2f2opt) | [oqlr2fopt](./blog/runs.md#oqlr2fopt) | [oqlr2f2](./blog/runs.md#oqlr2f2) | [oqlnr2opt](./blog/runs.md#oqlnr2opt) | [oqsnr2opt](./blog/runs.md#oqsnr2opt) | [oqsnr1Base](./blog/runs.md#oqsnr1base) | [oqlr2f2optP](./blog/runs.md#oqlr2f2optp) | [oqlr2foptP](./blog/runs.md#oqlr2foptp) | [oqlr2f2P](./blog/runs.md#oqlr2f2p) | [oqlnr2optP](./blog/runs.md#oqlnr2optp) | [oqsnr2optP](./blog/runs.md#oqsnr2optp)

??? abstract "Abstract"
	
	In TREC-2007, Indiana University‟s WIDIT Lab1 participated in the Blog track‟s opinion task and the polarity subtask. For the opinion task, whose goal is to 'uncover the public sentiment towards a given entity/target', we focused on combining multiple sources of evidence to detect opinionated blog postings. Since detecting opinionated blogs on a given topic (i.e., entity/target) involves not only retrieving topically relevant blogs but also identifying those that contain opinions about the target, our approach to the opinion finding task consisted of first applying traditional IR methods to retrieve on-topic blogs and then boosting the ranks of opinionated blogs based on combined opinion scores generated by multiple opinion detection methods. The key idea underlying our opinion detection method is to rely on a variety of complementary evidences rather than trying to optimize a single approach. This fusion approach to opinionated blog detection is motivated by our past experience that suggested no single approach, whether lexicon-based or classifier-driven, is well-suited for the blog opinion retrieval task. To accomplish the polarity subtask, which requires classification of the retrieved blogs into positive or negative orientation, our opinion detection module was extended to generate polarity scores to be used for polarity determination.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYZ07,
		author = {Kiduk Yang and Ning Yu and Hui Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2007 Blog Track: Combining Lexicon-Based Methods to Detect Opinionated Blogs},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/indianau.blog.final.pdf},
		timestamp = {Wed, 29 Jun 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangYZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC 2007: Opinion Retrieval of Blog Track

_Qi Zhang, Bingqing Wang, Lide Wu, Xuanjing Huang_

- :fontawesome-solid-user-group: **Participant:** [fudanu.wu](./blog/participants.md#fudanu.wu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fudan.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fudan.blog.final.pdf)
- :material-file-search: **Runs:** [FDUNoOpTisd](./blog/runs.md#fdunooptisd) | [FDUNOpRSVMT](./blog/runs.md#fdunoprsvmt) | [FDUTisdOpSVM](./blog/runs.md#fdutisdopsvm) | [FDUNoOpTSem](./blog/runs.md#fdunooptsem) | [FDUTOSVMSem](./blog/runs.md#fdutosvmsem) | [FDUTNRSVMSem](./blog/runs.md#fdutnrsvmsem)

??? abstract "Abstract"
	
	This paper describes our participation in the opinion retrieval task at Blog Track 07. The system consisted of the preprocess part, the topic retrieval part and sentiment analysis part. In the topic retrieval part, we adopted pseudo-relevance feedback and a novel approach to form a modified query. In the sentiment analysis part, each blog post was given an opinion score based on the sentences contained in this post. The subjectivity of each sentence was predicted by a CME classifier. Then the blog posts were reranked based on the similarity given by the topic retrieval and the opinion score given by the sentiment analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangWWH07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangWWH07,
		author = {Qi Zhang and Bingqing Wang and Lide Wu and Xuanjing Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDU} at {TREC} 2007: Opinion Retrieval of Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fudan.blog.final.pdf},
		timestamp = {Thu, 23 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangWWH07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 2007 Blog Track

_Wei Zhang, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [uiuc-zhang](./blog/participants.md#uiuc-zhang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uic-zhang.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uic-zhang.blog.final.pdf)
- :material-file-search: **Runs:** [uic1c](./blog/runs.md#uic1c) | [uic1s](./blog/runs.md#uic1s) | [uic75c](./blog/runs.md#uic75c) | [uic75s](./blog/runs.md#uic75s) | [uic1cpnm](./blog/runs.md#uic1cpnm) | [uic1spnm](./blog/runs.md#uic1spnm) | [uic75cpnm](./blog/runs.md#uic75cpnm) | [uic75spnm](./blog/runs.md#uic75spnm)

??? abstract "Abstract"
	
	In TREC 2007 Blog Track, we developed a three-step algorithm for the opinion retrieval task. An information retrieval step retrieves the query-relevant documents. A following opinion identification step identifies the opinionative texts in these documents. A ranking step identifies the query-related opinions in the documents and ranks them by calculating their opinion similarity scores. For the polarity task, our strategy is to find the positive and negative documents respectively, and then find the mixed opinionative documents in the intersection of the positive and negative document sets. We implemented our opinion retrieval algorithm in two special cases, one to retrieve the positive documents, and the other to retrieve the negative documents. A judging function labeled a subset of the documents, which were in the intersection of the positive and negative documents, as the mixed opinionative documents. We studied two parameters in our opinion retrieval algorithm, each of which had two values to compare. This resulted in four submitted opinion retrieval runs and their corresponding polarity runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangY07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangY07,
		author = {Wei Zhang and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uic-zhang.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangY07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WHU at Blog Track 2007

_Haozhen Zhao, Zhicheng Luo, Wei Lu_

- :fontawesome-solid-user-group: **Participant:** [wuhanu.lu](./blog/participants.md#wuhanu.lu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/wuhanu.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/wuhanu.blog.final.pdf)
- :material-file-search: **Runs:** [NOOPWHU1](./blog/runs.md#noopwhu1) | [OTWHU101](./blog/runs.md#otwhu101) | [OTWHU102](./blog/runs.md#otwhu102) | [OTPSWHU101](./blog/runs.md#otpswhu101) | [OTPSWHU102](./blog/runs.md#otpswhu102) | [TDWHU100](./blog/runs.md#tdwhu100) | [TDWHU101](./blog/runs.md#tdwhu101) | [TDWHU201](./blog/runs.md#tdwhu201) | [TDWHU200](./blog/runs.md#tdwhu200)

??? abstract "Abstract"
	
	We participate in all the sub tracks of the Blog track 2007. For the Opinionated Task, we use an excerpt list of the SentiWordNet to determine the opinionated nature of returned blog posts. For the Topic distillation Task, we test the effectiveness of cleaning work for the data collection in improvement of retrieval performance and the use of title and description part as queries. Both results show that our method does not work well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoLL07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoLL07,
		author = {Haozhen Zhao and Zhicheng Luo and Wei Lu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WHU} at Blog Track 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/wuhanu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoLL07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Topic Categorization for Relevancy and Opinion Detection

_GuangXu Zhou, Hemant Joshi, Coskun Bayrak_

- :fontawesome-solid-user-group: **Participant:** [uarkansas-littlerock.bayrak](./blog/participants.md#uarkansas-littlerock.bayrak)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ualr.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ualr.blog.final.pdf)
- :material-file-search: **Runs:** [UALR07Base](./blog/runs.md#ualr07base) | [UALR07BlogIU](./blog/runs.md#ualr07blogiu) | [UALR07TDN](./blog/runs.md#ualr07tdn) | [UALR07IU2](./blog/runs.md#ualr07iu2) | [UALR07CML](./blog/runs.md#ualr07cml) | [UALR07Text](./blog/runs.md#ualr07text)

??? abstract "Abstract"
	
	University of Arkansas at Little Rock's Blog Track team participated in only the core task of the blog track this year. The data acquired was identical to that of previous year except some new .retrieval tasks were introduced. The core task was to identify blogs that are opinionated about a certain subject. Fifty new topics were provided by National Institute of Standards and Technology (NIST) this year. Apart from the core task, two subtasks were also introduced. Polarity subtask was to detect polarity of the opinionated blog about a given topic. Feed distillation subtask was based on finding feeds rather than individual permalinks. Last year, we participated in the core task [1] and this year we planned to continue on our previous work. Although an attempt was made last year to use Active Learning with Support Vector Machine (SVM) to detect opinionated blog, identifying the opinion expressed about a given topic was unsuccessful. The difference this time around is in the use of search engines to conduct the topic search, categorizations of queries for further training, and a Natural Language based “one-pass-processing” approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouJB07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouJB07,
		author = {GuangXu Zhou and Hemant Joshi and Coskun Bayrak},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Topic Categorization for Relevancy and Opinion Detection},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ualr.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouJB07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

