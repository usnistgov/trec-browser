# Proceedings - Web 2010 

#### Overview of the TREC 2010 Web Track

_Charles L. A. Clarke, Nick Craswell, Ian Soboroff, Gordon V. Cormack_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec19/papers/WEB.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec19/papers/WEB.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Web Track explores and evaluates Web retrieval technology over large collections of Web data. In its current incarnation, the Web Track has been active for two years. For TREC 2010, the track includes three tasks: 1) an adhoc retrieval task, 2) a diversity task, and 3) a spam task. As we did for TREC 2009, we based our experiments on the billion-page ClueWeb091 data set created by the Language Technologies Institute at Carnegie Mellon University. The TREC 2009 Web Track included a traditional adhoc retrieval task, employing topical binary relevance assessments and reporting estimated MAP as its primary effectiveness measure [4]. For TREC 2010, we modified this traditional assessment process to incorporate multiple relevance levels, which are similar in structure to the levels used in commercial Web search. This new assessment structure includes a spam/junk level, which also assisted in the evaluation of the spam task. The top two levels of the assessment structure are closely related to the homepage finding and topic distillation tasks appearing in older Web Tracks. The diversity task was introduced for TREC 2009 and continues in TREC 2010, essentially unchanged [4]. The goal of this diversity task is to return a ranked list of pages that together provide complete coverage for a query, while avoiding excessive redundancy in the result list. The adhoc and diversity tasks share topics, which were developed by NIST with the assistance of information extracted from the the logs of a commercial Web search engine [9]. Topic creation and judging attempts to reflect a mix of genuine user requirements for the topic. An analysis of last year's results indicates that the presence of spam and other low-quality pages substantially influenced the overall results [7]. This year we provided a preliminary spam ranking of the pages in the corpus, as an aid to groups who wish to reduce the number of low-quality pages in their results. The associated spam task required groups to provide their own ranking of the corpus according to “spamminess”. Table 1 summarizes participation in the TREC 2010 Web Track. A total of 23 groups participated in the track, a slight decrease from last year, when 26 groups participated. Many of the groups participating the diversity task also participated in the adhoc task, but not vice versa. The spam task attracted only 3 participants, including one group that participated only in this task. Only one group, ICTNET, participated in all three tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCSC10.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCSC10,
		author = {Charles L. A. Clarke and Nick Craswell and Ian Soboroff and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2010 Web Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {https://trec.nist.gov/pubs/trec19/papers/WEB.OVERVIEW.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCSC10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Ottawa at TREC 2010 Web Track: Ranking Web Documents  Using Meta-Data

_Falah Hassan Al-akashi, Diana Inkpen_

- :fontawesome-solid-user-group: **Participant:** [uottawa](./participants.md#uottawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.ottawa.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.ottawa.web.rev.pdf)
- :material-file-search: **Runs:** [DFalah2010](./runs.md#dfalah2010)

??? abstract "Abstract"
	
	This paper describes the details of our participation in the Web track of the TREC 2010. Our approach collects information from the meta data and from some html tags of the web pages. Meta data is often used by the authors to describe the main topic or purpose of the webpage. Usually, the index words are collected from the visible data, but our method is preferable, when the webpage contains only multimedia data, such as images or animations; when the webpage contains only URL links or very little text data (e.g., home pages); when the webpage contains several different topics; when documents are repetitive; when we want to reduce the size of the inverted index; and when the weighting of a webpage depends on specific topics, not on word distribution. We indexed only selected sections of each webpage: “URL”, “Title”, “Meta”, “Header”, and “Alt” fields. The “Header” field is the only visible text field that we used.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Al-akashiI10.bib) "
	```
	@inproceedings{DBLP:conf/trec/Al-akashiI10,
		author = {Falah Hassan Al{-}akashi and Diana Inkpen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Ottawa at {TREC} 2010 Web Track: Ranking Web Documents Using Meta-Data},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.ottawa.web.rev.pdf},
		timestamp = {Wed, 03 Feb 2021 08:31:24 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Al-akashiI10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Role of Anchor Text in ClueWeb09 Retrieval

_Vo Ngoc Anh, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [unimelb](./participants.md#unimelb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.melbourne.web.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.melbourne.web.pdf)
- :material-file-search: **Runs:** [UMa10BASF](./runs.md#uma10basf) | [UMa10BSF](./runs.md#uma10bsf) | [UMa10IASF](./runs.md#uma10iasf) | [UMd10ASF](./runs.md#umd10asf) | [UMd10BASF](./runs.md#umd10basf) | [UMd10IASF](./runs.md#umd10iasf)

??? abstract "Abstract"
	
	This report describes the work done at The University of Melbourne with the ClueWeb09 data corpus for the Web Track of TREC-2009 and TREC-2010, and for the Session Track of TREC-2010. We found that the impact-based retrieval model works well for the corpus, and that, along with some other factors, the use of an anchor text collection significantly boosts the retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnhM10.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnhM10,
		author = {Vo Ngoc Anh and Alistair Moffat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Role of Anchor Text in ClueWeb09 Retrieval},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.melbourne.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnhM10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2010 Web Track Notebook: Term Dependence, Spam Filtering and  Quality Bias

_Michael Bendersky, David Fisher, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.mass.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.mass.web.rev.pdf)
- :material-file-search: **Runs:** [umassSDMW](./runs.md#umasssdmw) | [umasswfb520](./runs.md#umasswfb520) | [umassSDM](./runs.md#umasssdm)

??? abstract "Abstract"
	
	Many existing retrieval approaches treat all the documents in the collection equally, and do not take into account the content quality of the retrieved documents. In our submissions for TREC 2010 Web Track, we utilize quality-biased ranking methods that are aimed to promote documents that potentially contain high-quality content, and penalize spam and low-quality documents. Our experiments with the ad hoc web topics from TREC 2010 show that features such as the spamminess of the document (as computed by the Waterloo team [6]) and the readability of the document (modeled by the fraction of stopwords in the document) are very important for improving the precision at the top ranks. Promotion of the high-quality Wikipedia pages leads to further retrieval performance improvements. In addition, we found that using Wikipedia as a high-quality document collection for query expansion can ameliorate some of the negative effects of performing pseudo-relevance feedback from a noisy web collection such as ClueWeb09.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BenderskyFC10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BenderskyFC10,
		author = {Michael Bendersky and David Fisher and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2010 Web Track Notebook: Term Dependence, Spam Filtering and Quality Bias},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.mass.web.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BenderskyFC10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Lessons Learned From Indexing Close Word Pairs

_Leonid Boytsov, Anna Belova_

- :fontawesome-solid-user-group: **Participant:** [blv1979](./participants.md#blv1979)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/blv-1979.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/blv-1979.web.rev.pdf)
- :material-file-search: **Runs:** [blv79y00shnk](./runs.md#blv79y00shnk) | [blv79y00prob](./runs.md#blv79y00prob)

??? abstract "Abstract"
	
	We describe experiments with proximity-aware ranking functions that use indexing of word pairs. Our goal is to evaluate a method of “mild” pruning of proximity information, which would be appropriate for a moderately loaded retrieval system, e.g., an enterprise search engine. We create an index that includes occurrences of close word pairs, where one of the words is frequent. This allows one to efficiently restore relative positional information for all non-stop words within a certain distance. It is also possible to answer phrase queries promptly. We use two functions to evaluate relevance: a modification of a classic proximity-aware function and a logistic function that includes a linear combination of relevance features. Additionally, we use the spam scores provided by the University of Waterloo.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoytsovB10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoytsovB10,
		author = {Leonid Boytsov and Anna Belova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Lessons Learned From Indexing Close Word Pairs},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/blv-1979.web.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoytsovB10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MMCI at the TREC 2010 Web Track

_Andreas Broschart, Ralf Schenkel_

- :fontawesome-solid-user-group: **Participant:** [MMCI](./participants.md#mmci)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/saarland.univ.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/saarland.univ.web.rev.pdf)
- :material-file-search: **Runs:** [MMCITLl20M](./runs.md#mmcitll20m) | [MMCIl410m1](./runs.md#mmcil410m1) | [MMCITLCLl20M](./runs.md#mmcitlcll20m)

??? abstract "Abstract"
	
	Term proximity scoring models incorporate distance information of query term occurrences and are an established means in information retrieval to improve retrieval quality. The integration of such proximity scoring models into efficient query processing, however, has not been equally well studied. Existing methods make use of precomputed lists of documents where tuples of terms, usually pairs, occur together, usually incurring a huge index size compared to term-only indexes. This paper uses a joint framework for trading off index size and result quality. The framework provides optimization techniques for tuning precomputed indexes towards either maximal result quality or maximal query processing performance under controlled result quality, given an upper bound for the index size.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BroschartS10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BroschartS10,
		author = {Andreas Broschart and Ralf Schenkel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{MMCI} at the {TREC} 2010 Web Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/saarland.univ.web.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BroschartS10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2010 Ad-hoc Task

_Xu Chen, Zeying Peng, Jianguo Wang, Xiaoming Yu, Yue Liu, Hongbo Xu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.ADHOC.new.pdf](http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.ADHOC.new.pdf)
- :material-file-search: **Runs:** [ICTNETAD10R1](./runs.md#ictnetad10r1) | [ICTNETAD10R2](./runs.md#ictnetad10r2) | [ICTNETAD10R3](./runs.md#ictnetad10r3) | [ICTNETDV10R1](./runs.md#ictnetdv10r1) | [ICTNETDV10R2](./runs.md#ictnetdv10r2) | [ICTNETSP10R1](./runs.md#ictnetsp10r1) | [ICTNETDV10R3](./runs.md#ictnetdv10r3)

??? abstract "Abstract"
	
	In this paper, our team - “ICTNET”, participated in the ad-hoc task of Web Track of TREC 2010. The full Category A dataset was used. The sliding window BM25 model was extended from last year's method, combining with link analysis to rank the final results. All the methods having been tried in our experiments are delineated, and the evaluation results from the organizers of Web Track are presented thereafter.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenPWYLXC10.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenPWYLXC10,
		author = {Xu Chen and Zeying Peng and Jianguo Wang and Xiaoming Yu and Yue Liu and Hongbo Xu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2010 Ad-hoc Task},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.ADHOC.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenPWYLXC10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research at TREC 2010 Web Track

_Nick Craswell, Dennis Fetterly, Marc Najork_

- :fontawesome-solid-user-group: **Participant:** [msrsv](./participants.md#msrsv)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/microsoft-msrsv.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/microsoft-msrsv.web.rev.pdf)
- :material-file-search: **Runs:** [msrsv1](./runs.md#msrsv1) | [msrsv1div](./runs.md#msrsv1div) | [msrsv2](./runs.md#msrsv2) | [msrsv2div](./runs.md#msrsv2div) | [msrsv3](./runs.md#msrsv3) | [msrsv3div](./runs.md#msrsv3div)

??? abstract "Abstract"
	
	This paper describes our entry into the TREC 2010 Web track. We extracted and ranked results for both last year's and this year's topics from the ClueWeb09 corpus using a parallel processing pipeline that avoids the generation of an inverted file. We describe the components of the parallel architecture and the pipeline and how we ran the TREC experiments, and we present effectiveness results
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellFN10.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellFN10,
		author = {Nick Craswell and Dennis Fetterly and Marc Najork},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research at {TREC} 2010 Web Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/microsoft-msrsv.web.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellFN10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRRA at TREC 2010: Index Term Weighting by Divergence From Independence  Model

_Bekir Taner Dinçer, Ilker Kocabas, Bahar Karaoglan_

- :fontawesome-solid-user-group: **Participant:** [IRRA](./participants.md#irra)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/mugla.univ.web.pdf](http://trec.nist.gov/pubs/trec19/papers/mugla.univ.web.pdf)
- :material-file-search: **Runs:** [irra10b](./runs.md#irra10b) | [irra10hp](./runs.md#irra10hp) | [irra10rob](./runs.md#irra10rob)

??? abstract "Abstract"
	
	RRA (IR-Ra) group participated in the 2010 Web track. In this year, the major concern is to examine the effect of supplementary methods on the effectiveness of the new nonparametric index term weighting model, divergence from independence (DFI). [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DincerKK10.bib) "
	```
	@inproceedings{DBLP:conf/trec/DincerKK10,
		author = {Bekir Taner Din{\c{c}}er and Ilker Kocabas and Bahar Karaoglan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRRA} at {TREC} 2010: Index Term Weighting by Divergence From Independence Model},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/mugla.univ.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DincerKK10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMD and USC/ISI: TREC 2010 Web Track Experiments with Ivory

_Tamer Elsayed, Nima Asadi, Lidan Wang, Jimmy Lin, Donald Metzler_

- :fontawesome-solid-user-group: **Participant:** [UMD](./participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.maryland-usc-isi.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.maryland-usc-isi.web.rev.pdf)
- :material-file-search: **Runs:** [IvoryWSDa](./runs.md#ivorywsda) | [IvorySDa](./runs.md#ivorysda) | [IvoryBM25a](./runs.md#ivorybm25a) | [IVORY.70.30](./runs.md#ivory.70.30) | [IVORY.90.10](./runs.md#ivory.90.10)

??? abstract "Abstract"
	
	Ivory is a web-scale retrieval engine we have been developing for the past two years, built around a cluster-based environment running Hadoop, the open-source implementation of the MapReduce programming model. Building on successes last year at TREC, we explored two major directions this year: more sophisticated retrieval models and large-scale graph analysis for spam detection. We describe results of ad hoc retrieval experiments with latent concept expansion and a greedily-learned linear ranking model. Although neither model is novel, our experiments provide some insight on the behavior of these two approaches at scale, on collections larger than those previously studied. We also discuss our link-based spam filtering algorithm that operated on the entire web graph of ClueWeb09. Unfortunately, results in the spam track were worse than the baseline provided by the track organizers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ElsayedAWLM10.bib) "
	```
	@inproceedings{DBLP:conf/trec/ElsayedAWLM10,
		author = {Tamer Elsayed and Nima Asadi and Lidan Wang and Jimmy Lin and Donald Metzler},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UMD} and {USC/ISI:} {TREC} 2010 Web Track Experiments with Ivory},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.maryland-usc-isi.web.rev.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ElsayedAWLM10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MapReduce for Experimental Search

_Djoerd Hiemstra, Claudia Hauff_

- :fontawesome-solid-user-group: **Participant:** [utwente](./participants.md#utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.twente.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.twente.web.rev.pdf)
- :material-file-search: **Runs:** [utwente4](./runs.md#utwente4) | [utwente3](./runs.md#utwente3) | [utwente4SF](./runs.md#utwente4sf)

??? abstract "Abstract"
	
	This draft report presents preliminary results for the TREC 2010 adhoc web search task. We ran our MIREX system on 0.5 billion web documents from the ClueWeb09 crawl. On average, the system retrieves at least 3 relevant documents on the first result page containing 10 results, using a simple index consisting of anchor texts, page titles, and spam removal.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HiemstraH10.bib) "
	```
	@inproceedings{DBLP:conf/trec/HiemstraH10,
		author = {Djoerd Hiemstra and Claudia Hauff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MapReduce for Experimental Search},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.twente.web.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HiemstraH10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Anchor Text, Spam Filtering and Wikipedia for Web Search and  Entity Ranking

_Jaap Kamps, Rianne Kaptein, Marijn Koolen_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam-kamps.web.ent.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam-kamps.web.ent.rev.pdf)
- :material-file-search: **Runs:** [UAMSA10d2a8](./runs.md#uamsa10d2a8) | [UAMSD10ancB](./runs.md#uamsd10ancb) | [UAMSA10mSF30](./runs.md#uamsa10msf30) | [UAMSA10mSFPR](./runs.md#uamsa10msfpr) | [UAMSD10ancPR](./runs.md#uamsd10ancpr) | [UAMSD10aSRfu](./runs.md#uamsd10asrfu)

??? abstract "Abstract"
	
	In this paper, we document our efforts in participating to the TREC 2010 Entity Ranking and Web Tracks. We had multiple aims: For the Web Track we wanted to compare the effectiveness of anchor text of the category A and B collections and the impact of global document quality measures such as PageRank and spam scores. We find that documents in ClueWeb09 category B have a higher probability of being retrieved than other documents in category A. In ClueWeb09 category B, spam is mainly an issue for full-text retrieval. Anchor text suffers little from spam. Spam scores can be used to filter spam but also to find key resources. Documents that are least likely to be spam tend to be high-quality results. For the Entity Ranking Track, we use Wikipedia as a pivot to find relevant entities on the Web. Using category information to retrieve entities within Wikipedia leads to large improvements. Although we achieve large improvements over our baseline run that does not use category information, our best scores are still weak. Following the external links on Wikipedia pages to find the homepages of the entities in the ClueWeb collection, works better than searching an anchor text index, and combining the external links with searching an anchor text index.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KampsKK10.bib) "
	```
	@inproceedings{DBLP:conf/trec/KampsKK10,
		author = {Jaap Kamps and Rianne Kaptein and Marijn Koolen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Anchor Text, Spam Filtering and Wikipedia for Web Search and Entity Ranking},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam-kamps.web.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KampsKK10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCD SIFT in the TREC 2010 Web Track

_David Leonard, Lusheng Zhang, David Lillis, Fergus Toolan, Rem W. Collier, John Dunnion_

- :fontawesome-solid-user-group: **Participant:** [UCDSIFT](./participants.md#ucdsift)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.college.dublin.web.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.college.dublin.web.pdf)
- :material-file-search: **Runs:** [UCDSIFTSlide](./runs.md#ucdsiftslide) | [UCDSIFTProb](./runs.md#ucdsiftprob) | [UCDSIFTMAP](./runs.md#ucdsiftmap) | [UCDSIFTDiv](./runs.md#ucdsiftdiv)

??? abstract "Abstract"
	
	The SIFT (Segmented Information Fusion Techniques) group in UCD is dedicated to researching Data Fusion in Information Retrieval. This area of research involves the merging of multiple sets of results into a single result set that is presented to the user. As a means of both evaluating the effectiveness of this work and comparing it against other retrieval systems, the group entered Category B of the TREC 2010 Web Track. This involved the use of freely-available Information Retrieval tools to provide inputs to the data fusion process. This paper outlines the strategies of the 3 candidate fusion algorithms entered in the ad-hoc task, discusses the methodology employed for the runs and presents a preliminary analysis of the provisional results issued by TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeonardZLTCD10.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeonardZLTCD10,
		author = {David Leonard and Lusheng Zhang and David Lillis and Fergus Toolan and Rem W. Collier and John Dunnion},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCD} {SIFT} in the {TREC} 2010 Web Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.college.dublin.web.pdf},
		timestamp = {Thu, 11 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LeonardZLTCD10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combination of Evidence for Effective Web Search

_Dong Nguyen, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU_LIRA](./participants.md#cmu_lira)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/carnegie-mellon-univ-lira.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/carnegie-mellon-univ-lira.web.rev.pdf)
- :material-file-search: **Runs:** [cmuBase10](./runs.md#cmubase10) | [cmuWiki10](./runs.md#cmuwiki10) | [cmuFuTop10](./runs.md#cmufutop10) | [cmuWi10D](./runs.md#cmuwi10d) | [cmuFuTop10D](./runs.md#cmufutop10d) | [cmuComb10](./runs.md#cmucomb10)

??? abstract "Abstract"
	
	In this paper we describe Carnegie Mellon University's submission to the TREC 2010 Web Track. Our baseline run combines different methods, of which in particular the spam prior and mixture model were found the most effective. We also experimented with expansion over the Wikipedia corpus and found that picking the right Wikipedia articles for expansion can improve performance substantially. Furthermore, we did preliminary experiments with combining expansion over the Wikipedia corpus with expansion over the top ranked web pages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenC10.bib) "
	```
	@inproceedings{DBLP:conf/trec/NguyenC10,
		author = {Dong Nguyen and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combination of Evidence for Effective Web Search},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/carnegie-mellon-univ-lira.web.rev.pdf},
		timestamp = {Tue, 24 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NguyenC10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2010: Experiments with Terrier in  Blog and Web Tracks

_Rodrygo L. T. Santos, Richard McCreadie, Craig Macdonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.glasgow.blog.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.glasgow.blog.web.rev.pdf)
- :material-file-search: **Runs:** [uogTrB67](./runs.md#uogtrb67) | [uogTrB67LTS](./runs.md#uogtrb67lts) | [uogTrA42](./runs.md#uogtra42) | [uogTrB67xS](./runs.md#uogtrb67xs) | [uogTrBdphxS](./runs.md#uogtrbdphxs) | [uogTrA40n](./runs.md#uogtra40n) | [uogTrA42x](./runs.md#uogtra42x)

??? abstract "Abstract"
	
	In TREC 2010, we continue to build upon the Voting Model and experiment with our novel xQuAD framework within the auspices of the Terrier IR Platform. In particular, our focus is the development of novel applications for data-driven learning in the Blog and Web tracks, with experimentation spanning hundreds of features. In the Blog track, we propose novel feature sets for the ranking of blogs, news stories and blog posts. In the Web track, we propose novel selective approaches for adhoc and diversity search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SantosMMO10.bib) "
	```
	@inproceedings{DBLP:conf/trec/SantosMMO10,
		author = {Rodrygo L. T. Santos and Richard McCreadie and Craig Macdonald and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2010: Experiments with Terrier in Blog and Web Tracks},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.glasgow.blog.web.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SantosMMO10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2010 Diversity Task

_Yuanhai Xue, Zeying Peng, Xiaoming Yu, Yue Liu, Hongbo Xu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.DIVERSITY.new.pdf](http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.DIVERSITY.new.pdf)
- :material-file-search: **Runs:** [ICTNETAD10R1](./runs.md#ictnetad10r1) | [ICTNETAD10R2](./runs.md#ictnetad10r2) | [ICTNETAD10R3](./runs.md#ictnetad10r3) | [ICTNETDV10R1](./runs.md#ictnetdv10r1) | [ICTNETDV10R2](./runs.md#ictnetdv10r2) | [ICTNETSP10R1](./runs.md#ictnetsp10r1) | [ICTNETDV10R3](./runs.md#ictnetdv10r3)

??? abstract "Abstract"
	
	In this paper, our team - “ICTNET”, participated in the diversity task of Web Track of TREC 2010. The full Category A dataset was used. The same settings as the ad-hoc task were adopted for retrieval. Different clustering methods which were then applied on different fields are elaborated. Query expansion techniques are presented next.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuePYLXC10.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuePYLXC10,
		author = {Yuanhai Xue and Zeying Peng and Xiaoming Yu and Yue Liu and Hongbo Xu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2010 Diversity Task},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.DIVERSITY.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuePYLXC10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Delaware at Diverstiy Task of Web Track 2010

_Wei Zheng, Hui Fang, Xuanhui Wang_

- :fontawesome-solid-user-group: **Participant:** [Udel_Fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.delaware-fang.web.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.delaware-fang.web.pdf)
- :material-file-search: **Runs:** [UDWebSQR](./runs.md#udwebsqr) | [UDWebPCOV](./runs.md#udwebpcov) | [UDWebLOG](./runs.md#udweblog)

??? abstract "Abstract"
	
	We report our systems and experiments in the diversity task of TREC 2010 Web track. Our goal is to evaluate the effectiveness of the proposed methods for search result diversification on the large data collection. In the diversification systems, we use the greedy algorithm to select the document with the highest diversity score on each position and return a re-ranked list of diversified documents based on the query subtopics. The system extracts different groups of semantically related terms from the original retrieved documents as the subtopics of the query. It then uses the proposed diversity retrieval functions to compute the diversity score of each document on a particular position based on the similarity between the document and each subtopic, the relevance score of the subtopic given the query and the novelty of the subtopic given the previously selected documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengFW10.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengFW10,
		author = {Wei Zheng and Hui Fang and Xuanhui Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Delaware at Diverstiy Task of Web Track 2010},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.delaware-fang.web.pdf},
		timestamp = {Tue, 20 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengFW10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2010 Spam Task

_Liang Zhu, Bolong Zhu, Jianguo Wang, Xu Chen, Zeying Peng, Xiaoming Yu, Yue Liu, Hongbo Xu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.SPAM.new.pdf](http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.SPAM.new.pdf)
- :material-file-search: **Runs:** [ICTNETAD10R1](./runs.md#ictnetad10r1) | [ICTNETAD10R2](./runs.md#ictnetad10r2) | [ICTNETAD10R3](./runs.md#ictnetad10r3) | [ICTNETDV10R1](./runs.md#ictnetdv10r1) | [ICTNETDV10R2](./runs.md#ictnetdv10r2) | [ICTNETSP10R1](./runs.md#ictnetsp10r1) | [ICTNETDV10R3](./runs.md#ictnetdv10r3)

??? abstract "Abstract"
	
	Web Spamming refers those web pages deceive search engines so as to get a higher rank in their search result. We work on the data set TrecWeb09, based on a content-based spamming classifier, to check the two ends of a hyperlink; if the two end pages either is content spamming, or both are not so good, then the hyperlink will be discarded. After all hyperlinks have been checked, PageRank value shall be re-count on the re-built web network. The balance of one page's PageRank value will be regarded as its link spamming. Then the link spamming score and the result of content deceiving analyzer will be combined as the final estimation of one page's spamming.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuZWCPYLXC10.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuZWCPYLXC10,
		author = {Liang Zhu and Bolong Zhu and Jianguo Wang and Xu Chen and Zeying Peng and Xiaoming Yu and Yue Liu and Hongbo Xu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2010 Spam Task},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.SPAM.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuZWCPYLXC10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

