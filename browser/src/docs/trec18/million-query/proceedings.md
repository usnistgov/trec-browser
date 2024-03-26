# Proceedings - Million Query 2009 

#### Million Query Track 2009 Overview

_Ben Carterette, Virgiliu Pavlu, Hui Fang, Evangelos Kanoulas_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/MQ09OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/MQ09OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Million Query Track ran for the third time in 2009. The track is designed to serve two purposes: first, it is an exploration of ad hoc retrieval over a large set of queries and a large collection of documents; second, it investigates questions of system evaluation, in particular whether it is better to evaluate using many queries judged shallowly or fewer queries judged thoroughly. Fundamentally, the Million Query tracks (2007-2009) are ad-hoc tasks, only using complex but very efficient evaluation methodologies that allow human assessment effort to be spread on up to 20 times more queries than previous ad-hoc tasks. We estimate metrics like Average Precision fairly well and produce system ranking that (with high confidence) match the true ranking that would be obtained with complete judgments. We can answer budget related questions like how many queries versus how many assessments per query give an optimal strategy; a variance analysis is possible due to the large number of queries involved. While we have confidence we can evaluate participating runs well, an important question is whether the assessments produced by the evaluation process can be reused (together with the collection and the topics) for a new search strategy—that is, one that did not participate in the assessment done by NIST. To answer this, we designed a reusability study which concludes that a variant of participating track systems may be evaluated with reasonably high confidence using the MQ data, while a complete new system cannot. The 2009 track quadrupled the number of queries of previous years from 10,000 to 40,000. In addition, this year saw the introduction of a number of new threads to the basic framework established in the 2007 and 2008 tracks: Queries were classified by the task they represented as well as by their apparent difficulty; Participating sites could choose to do increasing numbers of queries, depending on time and resources available to them; We designed and implemented a novel in situ reusability study. Section 1 describes the tasks for participants. Section 2 provides an overview of the test collection that will result from the track. Section 3 briefly describes the document selection and evaluation methods. Section 4 summarizes the submitted runs. In Section 5 we summarize evaluation results from the task, and Section 6 provides deeper analysis into the results. For TREC 2009, Million Query, Relevance Feedback, and Web track ad-hoc task judging was conducted simultaneously using MQ track methods. A number of compromises had to be made to accomplish this; a note about the usability of the resulting data is included in Section 3.3
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarterettePFK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarterettePFK09,
		author = {Ben Carterette and Virgiliu Pavlu and Hui Fang and Evangelos Kanoulas},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Million Query Track 2009 Overview},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/MQ09OVERVIEW.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarterettePFK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad Hoc and Diversity Retrieval at the University of Delaware

_Praveen Chandar, Aparna Kailasam, Divya Muppaneni, Sree Lekha Thota, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [UDel](./participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf)
- :material-file-search: **Runs:** [udelIndDM](./runs.md#udelinddm) | [udelIndri](./runs.md#udelindri) | [udelIndRM](./runs.md#udelindrm) | [udelIndSP](./runs.md#udelindsp) | [udelIndPR](./runs.md#udelindpr)

??? abstract "Abstract"
	
	This is the report on the University of Delaware Information Retrieval Lab's participation in the TREC 2009 Web and Million Query tracks. Our report on the Relevance Feedback track is in a separate document [3].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChandarKMTC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChandarKMTC09,
		author = {Praveen Chandar and Aparna Kailasam and Divya Muppaneni and Sree Lekha Thota and Ben Carterette},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ad Hoc and Diversity Retrieval at the University of Delaware},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChandarKMTC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRRA at TREC 2009: Index Term Weighting Based on Divergence From  Independence Model

_Bekir Taner Dinçer, Ilker Kocabas, Bahar Karaoglan_

- :fontawesome-solid-user-group: **Participant:** [IRRA](./participants.md#irra)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf)
- :material-file-search: **Runs:** [irra1mqd](./runs.md#irra1mqd) | [irra2mqa](./runs.md#irra2mqa) | [irra2mqd](./runs.md#irra2mqd) | [irra1mqa](./runs.md#irra1mqa) | [irra3mqd](./runs.md#irra3mqd)

??? abstract "Abstract"
	
	IRRA (IR-Ra) group participated in the 2009 Web track (both adhoc task and diversity task) and the Million Query track. In this year, the major concern is to examine the effectiveness of a novel, nonparametric index term weighting model, divergence from independence (DFI). The notion of independence, which is the notion behind the well-known statistical exploratory data analysis technique called the correspondence analysis (Greenacre, 1984; Jambu, 1991), can be adapted to the index term weighting problem. In this respect, it can be thought of as a qualitative description of the importance of terms for documents, in which they appear, importance in the sense of contribution to the information contents of documents relative to other terms. According to the independence notion, if the ratios of the frequencies of two different terms are the same across documents, they are independent from documents. For example, each Web page contains a pair of “html” and a pair of “body” tags, so that the ratio of frequencies of these tags is the same across all Web pages, indicating that the “html” and “body” tags are independent from Web pages. They are used by design, irrespective of the information contents of Web pages. On the other hand, some tags, such as “image”, “table”, which are also independent from Web pages, may occur less or more in some pages than the expected frequencies suggested by the independence model; so, their associated frequency ratios may not be the same for all Web pages. However, it is reasonable to expect that, if the pages are not about the tags' usage, such as a “HTML Handbook”, frequencies of those tags should not be significantly different from their expected frequencies: they should be close to the expectation, i.e., in a parametric point of view, their observed frequencies on individual documents should be attributed to chance fluctuation. Although this tag example is helpful in exemplifying the use of independence notion, it is obvious that the tags are artificial, and so, governed by some rules completely different from the rules of a spoken language. Nonetheless, some words, like the ones in a common “stopwords list”, appear in documents, not because of their contribution to the information contents of documents, but because of the grammatical rules. On this account, such words can be modeled as if they were tags, because they are independent from documents in the same manner. Their observed frequencies in individual documents is expected to fluctuate around their frequencies expected under independence, as in the case of tags. Content bearing words are, therefore, the words whose frequencies highly diverge from the frequencies expected under independence. The results of the TREC experiments about IRRA runs show that the independence notion promises a natural basis for quantifying the categorical relationships between the terms and the documents. The TERRIER retrieval platform (Ounis et al., 2007) is used to index and search the ClueWeb09-T09B1 data set, a subset of about 50 million Web pages in English (TREC 2009 “Category B” data set). During indexing and searching, terms are stemmed and a particular set of stop words2 are eliminated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DincerKK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/DincerKK09,
		author = {Bekir Taner Din{\c{c}}er and Ilker Kocabas and Bahar Karaoglan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRRA} at {TREC} 2009: Index Term Weighting Based on Divergence From Independence Model},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DincerKK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Northeastern University in TREC 2009 Million Query Track

_Evangelos Kanoulas, Keshi Dai, Virgiliu Pavlu, Stefan Savev, Javed A. Aslam_

- :fontawesome-solid-user-group: **Participant:** [NEU](./participants.md#neu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/northeasternu.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/northeasternu.MQ.pdf)
- :material-file-search: **Runs:** [NeuSvmBase](./runs.md#neusvmbase) | [NeuSvmHE](./runs.md#neusvmhe) | [NeuSvmPR](./runs.md#neusvmpr) | [NeuSvmPRHE](./runs.md#neusvmprhe) | [NeuSvmStefan](./runs.md#neusvmstefan)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KanoulasDPSA09.bib) "
	```
	@inproceedings{DBLP:conf/trec/KanoulasDPSA09,
		author = {Evangelos Kanoulas and Keshi Dai and Virgiliu Pavlu and Stefan Savev and Javed A. Aslam},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Northeastern University in {TREC} 2009 Million Query Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/northeasternu.MQ.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KanoulasDPSA09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Study of Term Proximity and Document Weighting Normalization in  Pseudo Relevance Feedback–UIUC at TREC 2009 Million Query Track

_Yuanhua Lv, Jing He, V. G. Vinod Vydiswaran, Kavita Ganesan, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [UIUC](./participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uiuc.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/uiuc.MQ.pdf)
- :material-file-search: **Runs:** [uiuc09KL](./runs.md#uiuc09kl) | [uiuc09RegQL](./runs.md#uiuc09regql) | [uiuc09GProx](./runs.md#uiuc09gprox) | [uiuc09MProx](./runs.md#uiuc09mprox) | [uiuc09Adpt](./runs.md#uiuc09adpt)

??? abstract "Abstract"
	
	In this paper, we report our experiments in the TREC 2009 Million Query Track. Our first line of study is on proximity-based feedback, in which we propose a positional relevance model (PRM) to exploit term proximity evidence so as to assign more weights to expansion words that are closer to query words in feedback documents. The second line of study is to improve the weighting of feedback documents in the relevance model by using a regression-based method to approximate the probability of relevance (and thus the name RegRM). In the third line of study, we test a supervised approach for query classification. Besides, we also evaluate a selective pseudo feedback strategy which stops pseudo feedback for precision-oriented queries and only uses it for recall-oriented ones. The proposed PRM has shown clear improvements over the relevance model for pseudo feedback, suggesting that capturing the term proximity heuristic appropriately could lead to a better feedback model. RegRM performs as well as relevance model, but no noticeable improvement is observed. Unfortunately, the proposed query classification methods appear to not work well. The results also show that the proposed selective pseudo feedback may not work well, since precision-oriented queries can also benefit from pseudo feedback, though not as much as recall-oriented queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LvHVGZ09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LvHVGZ09,
		author = {Yuanhua Lv and Jing He and V. G. Vinod Vydiswaran and Kavita Ganesan and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Study of Term Proximity and Document Weighting Normalization in Pseudo Relevance Feedback--UIUC at {TREC} 2009 Million Query Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uiuc.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LvHVGZ09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2009: Experiments with Terrier

_Richard McCreadie, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf)
- :material-file-search: **Runs:** [uogTRMQdph40](./runs.md#uogtrmqdph40) | [uogTRMQdpA10](./runs.md#uogtrmqdpa10)

??? abstract "Abstract"
	
	In TREC 2009, we extend our Voting Model for the faceted blog distillation, top stories identification, and related entity finding tasks. Moreover, we experiment with our novel xQuAD framework for search result diversification. Besides fostering our research in multiple directions, by participating in such a wide portfolio of tracks, we further develop the indexing and retrieval capabilities of our Terrier Information Retrieval platform, to effectively and efficiently cope with a new generation of large-scale test collections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMOPS09,
		author = {Richard McCreadie and Craig Macdonald and Iadh Ounis and Jie Peng and Rodrygo L. T. Santos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2009: Experiments with Terrier},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIIT Hyderabad at Million Query Track TREC 2009

_Prashant Ullegaddi, Sudip Datta, Vinay Pande, Kushal S. Dave, Vasudeva Varma_

- :fontawesome-solid-user-group: **Participant:** [SIEL](./participants.md#siel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/iiit-hyderabad.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/iiit-hyderabad.MQ.pdf)
- :material-file-search: **Runs:** [iiithAuthPN](./runs.md#iiithauthpn) | [iiithAuEQ](./runs.md#iiithaueq) | [iiithExpQry](./runs.md#iiithexpqry)

??? abstract "Abstract"
	
	This was our maiden attempt at Million Query track, TREC 2009. We submitted three runs for ad-hoc retrieval task in Million Query track. We explored ad-hoc retrieval of web pages using Hadoop—a distributed infrastructure. To enhance recall, we expanded the queries using WordNet and also by combining the query with all possible subsets of tokens present in the query. To prevent query drift we experimented on giving selective boosts to different steps of expansion including giving higher boosts to sub-queries containing named entities as opposed to those that did not. In fact, this run achieved highest precision among our other runs. Using simple statistics we identified authoritative domains such as wikipedia.org, answers.com, etc and attempted to boost hits from them, while preventing them from overly biasing the results. An attempt to query classification was also made.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UllegaddiDPDV09.bib) "
	```
	@inproceedings{DBLP:conf/trec/UllegaddiDPDV09,
		author = {Prashant Ullegaddi and Sudip Datta and Vinay Pande and Kushal S. Dave and Vasudeva Varma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIIT} Hyderabad at Million Query Track {TREC} 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/iiit-hyderabad.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UllegaddiDPDV09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Axiomatic Approaches to Information Retrieval–University of Delaware  at TREC 2009 Million Query and Web Tracks

_Wei Zheng, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [EceUdel](./participants.md#eceudel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf)
- :material-file-search: **Runs:** [UDMQAxQEWeb](./runs.md#udmqaxqeweb) | [UDMQAxQE](./runs.md#udmqaxqe) | [UDMQAxBL](./runs.md#udmqaxbl) | [UDMQAxQEWP](./runs.md#udmqaxqewp) | [UDMQAxBLlink](./runs.md#udmqaxbllink)

??? abstract "Abstract"
	
	We report our experiments in TREC 2009 Million Query track and Adhoc task of Web track. Our goal is to evaluate the effectiveness of axiomatic retrieval models on the large data collection. Axiomatic approaches to information retrieval have been recently proposed and studied. The basic idea is to search for retrieval functions that can satisfy all the reasonable retrieval constraints. Previous studies showed that the derived basic axiomatic retrieval functions are less sensitive to the parameters than the other state of the art retrieval functions with comparable optimal performance. In this paper, we focus on evaluating the effectiveness of the basic axiomatic retrieval functions as well as the semantic term matching based query expansion strategy. Experiment results of the two tracks demonstrate the effectiveness of the axiomatic retrieval models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengF09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengF09,
		author = {Wei Zheng and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Axiomatic Approaches to Information Retrieval--University of Delaware at {TREC} 2009 Million Query and Web Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf},
		timestamp = {Tue, 20 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengF09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

