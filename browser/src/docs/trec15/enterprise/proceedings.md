# Proceedings - Enterprise 2006 

#### Overview of the TREC 2006 Enterprise Track

_Ian Soboroff, Arjen P. de Vries, Nick Craswell_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ENT06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/ENT06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The goal of the enterprise track is to conduct experiments with enterprise data — intranet pages, email archives, document repositories — that reflect the experiences of users in real organizations, such that for example, an email ranking technique that is effective here would be a good choice for deployment in a real multi-user email search application. This involves both understanding user needs in enterprise search and development of appropriate IR techniques. The enterprise track began in TREC 2005 as the successor to the web track, and this is reflected in the tasks and measures. While the track takes much of its inspiration from the web track, the foci are on search at the enterprise scale, incorporating non-web data and discovering relationships between entities in the organization. As a result, we have created the first test collections for multi-user email search and expert finding. This year the track has continued using the W3C collection, a crawl of the publicly available web of the World Wide Web Consortium performed in June 2004. This collection contains not only web pages but numerous mailing lists, technical documents and other kinds of data that represent the day-to-day operation of the W3C. Details of the collection may be found in the 2005 track overview (Craswell et al., 2005). Additionally, this year we began creating a repository of information derived from the collection by participants. This data is hosted alongside the W3C collection at NIST. There were two tasks this year, email discussion search and expert search, and both represent refinements of the tasks initially done in 2005. NIST developed topics and relevance judgments for the email discussion search task this year. For expert search, rather than relying on found data as last year, the track participants created the topics and relevance judgments. Twenty-five groups took part across the two tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SoboroffVC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/SoboroffVC06,
		author = {Ian Soboroff and Arjen P. de Vries and Nick Craswell},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2006 Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ENT06.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SoboroffVC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Language Models for Enterprise Search: Query Expansion and Combination  of Evidence

_Krisztian Balog, Edgar Meij, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.ilps](./participants.md#uamsterdam.ilps)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uamsterdam-derijke.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uamsterdam-derijke.ent.final.pdf)
- :material-file-search: **Runs:** [UvAbase](./runs.md#uvabase) | [UAmsBase](./runs.md#uamsbase) | [UvAprofiling](./runs.md#uvaprofiling) | [UvAPOS](./runs.md#uvapos) | [UvAprofPOS](./runs.md#uvaprofpos) | [UAmsPOSBase](./runs.md#uamsposbase) | [UAmsThreadQE](./runs.md#uamsthreadqe) | [UAmsPOStQE](./runs.md#uamspostqe)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2006 Enterprise track. We provide a detailed account of the ideas underlying our language modeling approaches to both the discussion search and expert search tasks. For discussion search, our focus was on query expansion techniques, using additional information from the topic statement and from message threads; while the former was generally helpful, the latter mostly hurt performance. In expert search our main experiments concerned query expansion as well as combinations of expert finding and expert profiling techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogMR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogMR06,
		author = {Krisztian Balog and Edgar Meij and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Language Models for Enterprise Search: Query Expansion and Combination of Evidence},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uamsterdam-derijke.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalogMR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Research on Expert Search at Enterprise Track of TREC 2006

_Shenghua Bao, Huizhong Duan, Qi Zhou, Miao Xiong, Yong Yu, Yunbo Cao_

- :fontawesome-solid-user-group: **Participant:** [sjtu-apex-lab.bao](./participants.md#sjtu-apex-lab.bao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/shanghai.final.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/shanghai.final.ent.final.pdf)
- :material-file-search: **Runs:** [SJTU01](./runs.md#sjtu01) | [SJTU02](./runs.md#sjtu02) | [SJTU03](./runs.md#sjtu03) | [SJTU04](./runs.md#sjtu04)

??? abstract "Abstract"
	
	This year, we (SJTU team) participated in the Expert Search task at the Enterprise Track. Last year, two of the members participated in the Expert Search task (MSRA team) [1]. This document reports our new experimental results on the expert search of TREC 2006. In this research, we propose a new evidence-oriented framework to expert search. Here, the evidence is defined as a quadruple, <Query, Expert, Relation, Document>. Each quadruple denotes that a 'Query' and an 'Expert', with a certain 'Relation' between them, are found in a specific 'Document'. In the proposed framework, the task of Expert Search can be accomplished in three steps, namely, 1) evidence extraction, 2) evidence quality evaluation, and 3) evidence merging. Thus, our experiments include the following items. We will explain them in detail later in the following sections. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BaoDZXYC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BaoDZXYC06,
		author = {Shenghua Bao and Huizhong Duan and Qi Zhou and Miao Xiong and Yong Yu and Yunbo Cao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Research on Expert Search at Enterprise Track of {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/shanghai.final.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BaoDZXYC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Social Network Structure Behind the Mailing Lists: ICT-IIIS at TREC  2006 Expert Finding Track

_Haiqiang Chen, Huawei Shen, Jin Xiong, Songbo Tan, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-iiis.tan](./participants.md#cas-iiis.tan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cas-ict.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/cas-ict.ent.final.pdf)
- :material-file-search: **Runs:** [IIISRUN](./runs.md#iiisrun) | [ICTCSXRUN01](./runs.md#ictcsxrun01) | [ICTCSXRUN02](./runs.md#ictcsxrun02) | [ICTCSXRUN03](./runs.md#ictcsxrun03) | [ICTCSXRUN04](./runs.md#ictcsxrun04) | [ICTCSXRUN05](./runs.md#ictcsxrun05)

??? abstract "Abstract"
	
	Expert finding system is a challenging problem in the enterprise environment. This paper introduce our research and experiments on TREC 2006's expert searching track. In our experiments, we find some interesting features of the community structures in the mailing list network. We also use some link analysis approaches to rank the candidates in the social networks. In our experiments, we choose the PageRank algorithm and a revised HITS algorithm as link analysis methods. These approaches give reasonable results in our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenSXTC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenSXTC06,
		author = {Haiqiang Chen and Huawei Shen and Jin Xiong and Songbo Tan and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Social Network Structure Behind the Mailing Lists: {ICT-IIIS} at {TREC} 2006 Expert Finding Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cas-ict.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenSXTC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### L3S Research Center at TREC 2006 Enterprise Track

_Sergey Chernov, Gianluca Demartini, Julien Gaugaz_

- :fontawesome-solid-user-group: **Participant:** [uhannover.chernov](./participants.md#uhannover.chernov)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/l3s.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/l3s.ent.final.pdf)
- :material-file-search: **Runs:** [l3s1](./runs.md#l3s1) | [l3s2](./runs.md#l3s2) | [l3s3](./runs.md#l3s3) | [l3s4](./runs.md#l3s4)

??? abstract "Abstract"
	
	The L3S Research Center submitted four runs at Enterprise Track for the first time in 2006, all of them are based solely on the W3C mailing lists. The first run serves as a fully automatically produced baseline. The second run uses a threshold on the document scores to limit the number of documents used for expert ranking. The third uses in addition a threshold on the experts scores in order to decide how many experts to retrieve. Our last run exploits the manually assigned topic specificity values, which predicts a number of relevant expert for each query. The results show that the simple threshold techniques outperform the baseline, while the current definition of query specificity does not improve the result quality.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChernovDG06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChernovDG06,
		author = {Sergey Chernov and Gianluca Demartini and Julien Gaugaz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{L3S} Research Center at {TREC} 2006 Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/l3s.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChernovDG06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM in TREC 2006 Enterprise Track

_Jennifer Chu-Carroll, Guillermo A. Averboch, Pablo Ariel Duboue, David Gondek, J. William Murdock, John M. Prager, Paul Hoffmann, Janyce Wiebe_

- :fontawesome-solid-user-group: **Participant:** [ibm.prager](./participants.md#ibm.prager)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ibm-watson.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ibm-watson.ent.final.pdf)
- :material-file-search: **Runs:** [IBM06JILAQD](./runs.md#ibm06jilaqd) | [IBM06JAQD](./runs.md#ibm06jaqd) | [IBM06JILAPQD](./runs.md#ibm06jilapqd) | [IBM06JAQ](./runs.md#ibm06jaq) | [IBM06QO](./runs.md#ibm06qo) | [IBM06PR](./runs.md#ibm06pr) | [IBM06EXP](./runs.md#ibm06exp) | [IBM06MA](./runs.md#ibm06ma)

??? abstract "Abstract"
	
	In 2006, IBM participated for the first time in the Enterprise Track, submitting runs for both the discussion and expert tasks. The Enterprise Track is intended to address information seeking tasks common in corporate settings using information that is readily available on corporate intranets. Because of confidentiality issues, the corpus used for this task is a snapshot of w3c.org as of June 2004, considering the W3C as a “corporation” that conducts its day-to-day business on the web. This corpus consists of a heterogeneous set of data sources, including web pages, mailing lists, code, wiki, etc. [Craswell et al. 2006]. The discussion task seeks e-mail messages that discuss the pro or con of a given subject matter, while the expert task requires that experts for given topics be identified. The main foci of our Enterprise Track experiments this year were on 1) problem-solving through adoption of multiple discussion and expert finding strategies, 2) combination of structured, semi-structured, and unstructured information for discussion and expert finding, 3) investigation of impact of select NLP techniques, such as multi-document summarization for expert pseudo-document generation and pro/con sentiment identification and retrieval, and 4) use of external resources for discussion and expert finding. The rest of this paper discusses the systems we developed for Enterprise Track participation, focusing on the four aspects outlined above. We will also discuss specific strategies we took to configure the systems for each of the four runs in both tasks, as well as their impact on system performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Chu-CarrollADGMPHW06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Chu-CarrollADGMPHW06,
		author = {Jennifer Chu{-}Carroll and Guillermo A. Averboch and Pablo Ariel Duboue and David Gondek and J. William Murdock and John M. Prager and Paul Hoffmann and Janyce Wiebe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IBM} in {TREC} 2006 Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ibm-watson.ent.final.pdf},
		timestamp = {Sat, 21 Jan 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Chu-CarrollADGMPHW06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SOPHIA in Enterprise Track

_Vladimir Dobrynin, Kim Son Pham, David Patterson, Niall Rooney, Mykola Galushka_

- :fontawesome-solid-user-group: **Participant:** [uulster.patterson](./participants.md#uulster.patterson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uulster.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uulster.ent.final.pdf)
- :material-file-search: **Runs:** [sophiarun1](./runs.md#sophiarun1) | [sophiarun2](./runs.md#sophiarun2) | [sophiarun3](./runs.md#sophiarun3)

??? abstract "Abstract"
	
	SOPHIA participated in TREC 2006 as part of the Enterprise track (Expert search task). Given a topic our task was to find an ordered list of up to 100 experts (from a predefined list of candidate experts) and for every expert create an ordered list of up to 20 support documents. Support document should prove that given person is indeed an expert in the domain presented by the topic. We implemented 3 algorithms to solve this task which resulted in 3 runs sophiarun1, sophiarun2 and sophiarun3. All runs are based on Contextual Document Clustering (CDC) algorithm [1,2] applied to a part of W3C document corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DobryninPPRG06.bib) "
	```
	@inproceedings{DBLP:conf/trec/DobryninPPRG06,
		author = {Vladimir Dobrynin and Kim Son Pham and David Patterson and Niall Rooney and Mykola Galushka},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{SOPHIA} in Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uulster.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DobryninPPRG06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2006: Enterprise Email Discussion Search

_Yu Fan, Xiangji Huang, Aijun An_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/yorku.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/yorku.ent.final.pdf)
- :material-file-search: **Runs:** [york06ed01](./runs.md#york06ed01) | [york06ed02](./runs.md#york06ed02) | [york06ed03](./runs.md#york06ed03) | [york06ed04](./runs.md#york06ed04)

??? abstract "Abstract"
	
	We use the Okapi retrieval system to conduct the email discussion search. The following issues are investigated. First, we make use of the thread structure in the emails to re-rank the documents retrieved by Okapi. We would like to see whether such post-processing of the retrieval result can boost the retrieval performance. Second, in terms of query formulation, we investigate whether the use of only title in a topic achieves better or worse results than the inclusion of other fields such as description and narrative. Third, we investigate whether stemming and stop word removal play an important role in the email search. Our conclusion includes that (1) re-ranking documents using a straightforward method that considers the thread structure can make a small improvement to the retrieval performance, (2) formulating the query using all the fields in a topic achieves the best result, and (3) the use of stemming and stop word removal can improve the performance, but the degree of improvement depends on the stemming method and the stop word list used.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FanHA06.bib) "
	```
	@inproceedings{DBLP:conf/trec/FanHA06,
		author = {Yu Fan and Xiangji Huang and Aijun An},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2006: Enterprise Email Discussion Search},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/yorku.ent.final.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FanHA06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Language Models for Expert Finding–UIUC TREC 2006 Enterprise Track  Experiments

_Hui Fang, Lixin Zhou, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uiuc.zhai](./participants.md#uiuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.ent.final.pdf)
- :material-file-search: **Runs:** [UIUCe1](./runs.md#uiuce1) | [UIUCeFB1](./runs.md#uiucefb1) | [UIUCeFB2](./runs.md#uiucefb2) | [UIUCe2](./runs.md#uiuce2)

??? abstract "Abstract"
	
	In this paper, we report our experiments in the TREC 2006 Enterprise Track. Our focus is to study a language model for expert finding. We extend an existing language model for expert retrieval in three aspects. First, we model the document-expert association using a mixure model instead of name matching heuristics as in the existing work; such a mixture model allows us to put different weights on email matching and name matching. Second, we propose to model the prior of an expert based on the counts of email matches in the supporting documents instead of using uniform prior as in the previous work. Finally, we perform topic expansion and generalize the model from computing the likelihood to computing the cross entropy. Our experiments show that the first two extensions are more effective than the third extension, though when optimized, they all seem to be effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FangZZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/FangZZ06,
		author = {Hui Fang and Lixin Zhou and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Language Models for Expert Finding--UIUC {TREC} 2006 Enterprise Track Experiments},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FangZZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Solving the Enterprise TREC Task with Probabilistic Data Models

_Jan Frederik Forst, Anastasios Tombros, Thomas Rölleke_

- :fontawesome-solid-user-group: **Participant:** [queen-mary-ulondon.forst](./participants.md#queen-mary-ulondon.forst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/queen-mary-ulondon.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/queen-mary-ulondon.ent.final.pdf)
- :material-file-search: **Runs:** [quotes](./runs.md#quotes) | [body](./runs.md#body) | [listbq](./runs.md#listbq) | [www](./runs.md#www)

??? abstract "Abstract"
	
	Expert identification has become an important information retrieval task. We present and investigate a number of approaches for identifying an expert. Different approaches are based on exploiting the structure of documents in the knowledge base. Furthermore, our system highlights the integration of database technology with information retrieval (DB+IR).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ForstTR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ForstTR06,
		author = {Jan Frederik Forst and Anastasios Tombros and Thomas R{\"{o}}lleke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Solving the Enterprise {TREC} Task with Probabilistic Data Models},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/queen-mary-ulondon.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ForstTR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pitt at TREC 2006: Identifying Experts via Email Discussions

_Daqing He, Yefei Peng_

- :fontawesome-solid-user-group: **Participant:** [upittsburgh.he](./participants.md#upittsburgh.he)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/upitt.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/upitt.ent.final.pdf)
- :material-file-search: **Runs:** [PITTMANUAL](./runs.md#pittmanual) | [PITTPHFREQ](./runs.md#pittphfreq) | [PITTNOPH](./runs.md#pittnoph) | [PITTPHFULL](./runs.md#pittphfull)

??? abstract "Abstract"
	
	Identifying experts in a certain domain or a subject area has always been a challenge in various settings including commercial, academia, and governmental institutions. Our interests in this year's TREC Enterprise track are to utilize the email communications as the basis for identifying experts and their expertise on certain topics. In this report, we presented a method for identifying experts based on the emails they sent around. We hypothesize that experts would be more active in relevant email threads, would send longer emails, and would participate in the discussion at the very beginning of the threads. An algorithm based on these hypotheses was developed and tested in this year TREC enterprise track experiments to find experts for 49 topics based on documents in the W3C collections. Our initial experiment results produced suboptimal performance. This motivated us to examine the hypotheses more closely in the context of provided ground truth. Interestingly, the analysis on ground truth seems to confirm that all of our hypotheses have their merits in finding experts, so one future important question is how to utilize these rules in a right way.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeP06.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeP06,
		author = {Daqing He and Yefei Peng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pitt at {TREC} 2006: Identifying Experts via Email Discussions},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/upitt.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeP06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### In Enterprise Search: Methods to Identify Argumentative Discussions  and to Find Topical Experts

_Maheedhar Kolla, Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo-clarke](./participants.md#uwaterloo-clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uwaterloo-kolla.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uwaterloo-kolla.ent.final.pdf)
- :material-file-search: **Runs:** [uwTbaseline](./runs.md#uwtbaseline) | [uwTDbaseline](./runs.md#uwtdbaseline) | [uwTsubj](./runs.md#uwtsubj) | [uwTDsubj](./runs.md#uwtdsubj) | [uwXSHUBS](./runs.md#uwxshubs) | [uwXSOUT](./runs.md#uwxsout) | [uwXSPMI](./runs.md#uwxspmi)

??? abstract "Abstract"
	
	Our intention in taking part in this year's Enterprise Track is to experiment with various re-ranking approaches in solving two problems: email search and expert search. In email discussion search, we propose methods to retrieve email messages that contain pro/con argument about the topic in discussion. We compute the likelihood of an email having a pro/con argument about the topic and re-rank emails based on the likelihood of containing topical subjective opinion. In expert search, we explored methods to identify experts for a given topic by analyzing the mailing patterns in the email archive.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KollaV06.bib) "
	```
	@inproceedings{DBLP:conf/trec/KollaV06,
		author = {Maheedhar Kolla and Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {In Enterprise Search: Methods to Identify Argumentative Discussions and to Find Topical Experts},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uwaterloo-kolla.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KollaV06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Judging Expertise–WIM at Enterprise

_Chen Lin, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [fudanu.niu](./participants.md#fudanu.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/fudan-niu.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/fudan-niu.ent.final.pdf)
- :material-file-search: **Runs:** [FDUSO](./runs.md#fduso) | [FDUSN](./runs.md#fdusn) | [FDUSF](./runs.md#fdusf)

??? abstract "Abstract"
	
	This document reports experiment and result of Fudan WIM group in Expert Search track in TREC 2006. Our research mainly focus on the measurement of expertise. Inspired by the human procedure of expert search, we construct 2 models, a language model and a social network model are compared. The association function of expert and document is modified. And email search techniques are employed in document retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinN06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinN06,
		author = {Chen Lin and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Judging Expertise--WIM at Enterprise},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/fudan-niu.ent.final.pdf},
		timestamp = {Tue, 20 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinN06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2006: Experiments in Terabyte and  Enterprise Tracks with Terrier

_Christina Lioma, Craig Macdonald, Vassilis Plachouras, Jie Peng, Ben He, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uglasgow.ounis](./participants.md#uglasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uglasgow.tera.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uglasgow.tera.ent.final.pdf)
- :material-file-search: **Runs:** [uogX06csnP](./runs.md#uogx06csnp) | [uogX06csnQEF](./runs.md#uogx06csnqef) | [uogX06csnQE](./runs.md#uogx06csnqe) | [uogX06ecm](./runs.md#uogx06ecm)

??? abstract "Abstract"
	
	In TREC 2006, we participate in three tasks of the Terabyte and Enterprise tracks. We continue experiments using Terrier1, our modular and scalable Information Retrieval (IR) platform. Furthering our research into the Divergence From Randomness (DFR) framework of weighting models, we introduce two new effective and low-cost models, which combine evidence from document structure and capture term dependence and proximity, respectively. Additionally, in the Terabyte track, we improve on our query expansion mechanism on fields, presented in TREC 2005, with a new and more refined technique, which combines evidence in a linear, rather than uniform, way. We also introduce a novel, low-cost syntactically-based noise reduction technique, which we flexibly apply to both the queries and the index. Furthermore, in the Named Page Finding task, we present a new technique for combining query-independent evidence, in the form of prior probabilities. In the Enterprise track, we test our new voting model for expert search. Our experiments focus on the need for candidate length normalisation, and on how retrieval performance can be enhanced by applying retrieval techniques to the underlying ranking of documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiomaMPPHO06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiomaMPPHO06,
		author = {Christina Lioma and Craig Macdonald and Vassilis Plachouras and Jie Peng and Ben He and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2006: Experiments in Terabyte and Enterprise Tracks with Terrier},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uglasgow.tera.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiomaMPPHO06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Window-based Enterprise Expert Search

_Wei Lu, Stephen E. Robertson, Andrew MacFarlane, Haozhen Zhao_

- :fontawesome-solid-user-group: **Participant:** [cityu.macfarlane](./participants.md#cityu.macfarlane)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cityu-london.ent.pdf](http://trec.nist.gov/pubs/trec15/papers/cityu-london.ent.pdf)
- :material-file-search: **Runs:** [ex7512](./runs.md#ex7512) | [ex5512](./runs.md#ex5512) | [ex3512](./runs.md#ex3512) | [ex5518](./runs.md#ex5518)

??? abstract "Abstract"
	
	This is the first year for the participation of the City University Centre of Interactive System Research (CISR) in the Expert Search Task. In this paper, we describe an expert search experiment based on window-based techniques, that is, we build profile for each expert by using information around the expert's name and email address in the documents. We then use the traditional IR techniques to search and rank experts. Our experiment is done on Okapi and BM25 is used as the ranking model. Results show that parameter b does have an effect on the retrieval effectiveness and using a smaller value for b produces better results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuRMZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuRMZ06,
		author = {Wei Lu and Stephen E. Robertson and Andrew MacFarlane and Haozhen Zhao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Window-based Enterprise Expert Search},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cityu-london.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuRMZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2006 at Maryland: Blog, Enterprise, Legal and QA Tracks

_Douglas W. Oard, Tamer Elsayed, Jianqiang Wang, Yejun Wu, Pengyi Zhang, Eileen G. Abels, Jimmy Lin, Dagobert Soergel_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf)
- :material-file-search: **Runs:** [UMDthrdTTL](./runs.md#umdthrdttl) | [UMDthrdTTLDS](./runs.md#umdthrdttlds) | [UMDthrdTTLNR](./runs.md#umdthrdttlnr) | [UMDemailTTL](./runs.md#umdemailttl) | [UMDemailTLNR](./runs.md#umdemailtlnr)

??? abstract "Abstract"
	
	In TREC 2006, teams from the University of Maryland participated in the Blog track, the Expert Search task of the Enterprise track, the Complex Interactive Question Answering task of the Question Answering track, and the Legal track. This paper reports our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardEWWZALS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardEWWZALS06,
		author = {Douglas W. Oard and Tamer Elsayed and Jianqiang Wang and Yejun Wu and Pengyi Zhang and Eileen G. Abels and Jimmy Lin and Dagobert Soergel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 at Maryland: Blog, Enterprise, Legal and {QA} Tracks},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/OardEWWZALS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2006: Enterprise Track

_Desislava Petkova, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umass.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umass.ent.final.pdf)
- :material-file-search: **Runs:** [UMaTiMixHdr](./runs.md#umatimixhdr) | [UMaTiMixThr](./runs.md#umatimixthr) | [UMaTDMixThr](./runs.md#umatdmixthr) | [UMaTiSmoThr](./runs.md#umatismothr) | [UMaTiDm](./runs.md#umatidm) | [UMaTNDm](./runs.md#umatndm) | [UMaTNFb](./runs.md#umatnfb) | [UMaTDFb](./runs.md#umatdfb)

??? abstract "Abstract"
	
	This paper gives an overview of the work done at the University of Massachusetts, Amherst for the TREC 2006 Enterprise track. For the discussion search task, we compare two methods for incorporating thread evidence into the language models of email messages. For the expert finding task, we create implicit expert representations as mixtures of language models from associated documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PetkovaC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/PetkovaC06,
		author = {Desislava Petkova and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2006: Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umass.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PetkovaC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT at TREC 2006: Enterprise Track

_Zhao Ru, Quian Li, Weiran Xu, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [beijingu-posts-tele.weiran](./participants.md#beijingu-posts-tele.weiran)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/beijing-upt.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/beijing-upt.ent.final.pdf)
- :material-file-search: **Runs:** [PRISEXB](./runs.md#prisexb) | [PRISEXR](./runs.md#prisexr) | [PRISEXRM](./runs.md#prisexrm) | [PRISEXRMT](./runs.md#prisexrmt)

??? abstract "Abstract"
	
	This is the second time that Pattern Recognition and Intelligent System Lab (PRIS) participate in TREC. In enterprise track, our efforts have been focused on the expert search task this year. The goal is to develop more elaborate model for expert searching and find effective support providing method for new request.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuLXG06.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuLXG06,
		author = {Zhao Ru and Quian Li and Weiran Xu and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BUPT} at {TREC} 2006: Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/beijing-upt.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuLXG06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Case Western Reserve University at the TREC 2006 Enterprise Track

_Adam D. Troy, Guo-Qiang Zhang_

- :fontawesome-solid-user-group: **Participant:** [case-western.ru.troy](./participants.md#case-western.ru.troy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/case-western.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/case-western.ent.final.pdf)
- :material-file-search: **Runs:** [basic](./runs.md#basic) | [allbasic](./runs.md#allbasic) | [w1r1s1](./runs.md#w1r1s1)

??? abstract "Abstract"
	
	For Case Western Reserve University's debut participation in TREC, we chose to participate in the Enterprise Track expert search task. Our motivation for participation stems from our work developing expert search capability for our prototype vertical digital library, MEMS World Online1. Our work incorporates two unique aspects. First, our relevance ranking mechanism relies on term position within each document rather than the number of term occurrences. This mechanism takes into account both term document rank and term co-occurrence proximity. Second, the expert score of closely related colleagues has a small effect on the score of each related expert. This follows the intuition that experts on a particular topic within a single organization tend to closely collaborate with one another. We also make some use of WordNet synonyms. We submitted a total of three runs to this years expert search task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TroyZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/TroyZ06,
		author = {Adam D. Troy and Guo{-}Qiang Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Case Western Reserve University at the {TREC} 2006 Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/case-western.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TroyZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Correlating Topic Rankings and Person Rankings to Find Experts

_Thijs Westerveld_

- :fontawesome-solid-user-group: **Participant:** [lowlands-team.deVries](./participants.md#lowlands-team.devries)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cwi.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/cwi.ent.final.pdf)
- :material-file-search: **Runs:** [MAPTrelCret](./runs.md#maptrelcret) | [MAPCrelTret](./runs.md#mapcreltret) | [SPlog](./runs.md#splog) | [SP](./runs.md#sp)

??? abstract "Abstract"
	
	Expert search is about finding people rather than documents. The goal is to retrieve a ranked list of candidates with expertise on a given topic. The task is studied in the context of the enterprise track. We describe an approach that compares topic profiles and candidate profiles directly. These profiles are not based on unordered sets of documents, but on ranked lists. This allows us to differentiate between documents that are highly related to a topic or a candidate and documents that are only marginally related. The ranked lists for topics and candidates are obtained by simple retrieval queries. The correlation between the ranked list of documents for a topic and the ranked list for a candidate is used as an indicator of the candidate's expertise on the topic. We study different ways to rank documents for the candidate profiles as well as various ways of comparing the document and candidate based ranked lists. Experiments show that starting from the right candidate profiles, reasonable results can be obtained. Furthermore, it seems important to take a correlation measure that takes into account the orderings of documents in both the candidate profile and the documents profile.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Westerveld06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Westerveld06,
		author = {Thijs Westerveld},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Correlating Topic Rankings and Person Rankings to Find Experts},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cwi.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Westerveld06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2006: Genomics and Enterprise Tracks

_Zhihao Yang, Hongfei Lin, Yanpeng Li, Linhong Xu, Yu Pan, Baoyan Liu_

- :fontawesome-solid-user-group: **Participant:** [dalianu.yang](./participants.md#dalianu.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf)
- :material-file-search: **Runs:** [DUTDS1](./runs.md#dutds1) | [DUTDS2](./runs.md#dutds2) | [DUTDS3](./runs.md#dutds3) | [DUTDS4](./runs.md#dutds4) | [DUTEX1](./runs.md#dutex1) | [DUTEX2](./runs.md#dutex2) | [DUTEX3](./runs.md#dutex3) | [DUTEX4](./runs.md#dutex4)

??? abstract "Abstract"
	
	This paper describes the techniques we applied for the two TREC 2006 tracks, i.e., Genomics and Enterprise track. For the Genomics Track, we used a Rocchio relevance feedback method to expand the terms and then performed passage retrieval by building dual index and using half overlapped windows passages. Several approaches to merge the results and rerank the passages are presented. For the Enterprise track, we stripped the non-letter character from documents and query, built the index by indri or lemur and established expert document pools.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLLXPL06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangLLXPL06,
		author = {Zhihao Yang and Hongfei Lin and Yanpeng Li and Linhong Xu and Yu Pan and Baoyan Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2006: Genomics and Enterprise Tracks},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLLXPL06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ricoh Research at TREC 2006: Enterprise Track

_Ganmei You, Yaojie Lu, Gang Li, Yueyan Yin_

- :fontawesome-solid-user-group: **Participant:** [ricoh.you](./participants.md#ricoh.you)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ricoh.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ricoh.ent.final.pdf)
- :material-file-search: **Runs:** [srcbds1](./runs.md#srcbds1) | [srcbds2](./runs.md#srcbds2) | [srcbds3](./runs.md#srcbds3) | [srcbds4](./runs.md#srcbds4) | [srcbds5](./runs.md#srcbds5) | [SRCBEX1](./runs.md#srcbex1) | [SRCBEX2](./runs.md#srcbex2) | [SRCBEX5](./runs.md#srcbex5) | [SRCBEX3](./runs.md#srcbex3) | [SRCBEX4](./runs.md#srcbex4)

??? abstract "Abstract"
	
	This article presents our contributions to expert search and discussion search of Enterprise Track in TREC 2006. In discussion search, we take advantage of the redundant patterns of emails, such as the subject, author, sent time, etc., which we incorporate in a field-based weighting method to mine discussion topics with more robustness. Some non-content features, such as time-line and mail thread are found to be useful as experiments showed they improve the precision of the search. In expert search, two variants of the BM25 and DFR_BM25 weighting models - namely V-BM25 and V-DFR_BM25 - are put forward. Query-based document length, not profile length, is used as document length in these weighting models to eliminate multiple topic drift. In addition, we propose a variant of an existing phrase weighting model to decrease topic confusion (V-phrase) and a two-stage field-based search method to refine the results. We demonstrate these approaches can effectively improve expert search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YouLLY06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YouLLY06,
		author = {Ganmei You and Yaojie Lu and Gang Li and Yueyan Yin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ricoh Research at {TREC} 2006: Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ricoh.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YouLLY06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Open University at TREC 2006 Enterprise Track Expert Search  Task

_Jianhan Zhu, Dawei Song, Stefan M. Rüger, Marc Eisenstadt, Enrico Motta_

- :fontawesome-solid-user-group: **Participant:** [openu.zhu](./participants.md#openu.zhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/openu.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/openu.ent.final.pdf)
- :material-file-search: **Runs:** [kmiZhu2](./runs.md#kmizhu2) | [kmiZhu4](./runs.md#kmizhu4) | [kmiZhu1](./runs.md#kmizhu1) | [kmiZhu5](./runs.md#kmizhu5)

??? abstract "Abstract"
	
	The Multimedia and Information Systems group at the Knowledge Media Institute of the Open University participated in the Expert Search task of the Enterprise Track in TREC 2006. We have proposed to address three main innovative points in a two-stage language model, which consists of a document relevance model and a cooccurrence model, in order to improve the performance of expert search. The three innovative points are based on characteristics of documents. First, document authority in terms of their PageRanks is considered in the document relevance model. Second, document internal structure is taken into account in the co-occurrence model. Third, we consider multiple levels of associations between experts and query terms in the co-occurrence model. Our experiments on the TREC2006 Expert Search task show that addressing the above three points has led to improved effectiveness of expert search on the W3C dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuSREM06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuSREM06,
		author = {Jianhan Zhu and Dawei Song and Stefan M. R{\"{u}}ger and Marc Eisenstadt and Enrico Motta},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Open University at {TREC} 2006 Enterprise Track Expert Search Task},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/openu.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuSREM06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

