# Proceedings - Robust 2004 

#### Overview of the TREC 2004 Robust Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ROBUST.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec13/papers/ROBUST.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The robust retrieval track explores methods for improving the consistency of retrieval technology by focusing on poorly performing topics. The retrieval task in the track is a traditional ad hoc retrieval task where the evaluation methodology emphasizes a system's least effective topics. The most promising approach to improving poorly performing topics is exploiting text collections other than the target collection such as the web. The 2004 edition of the track used 250 topics and required systems to rank the topics by predicted difficulty. The 250 topics within the test set allowed the stability of evaluation measures that emphasize poorly performing topics to be investigated. A new measure, a variant of the traditional MAP measure that uses a geometric mean rather than an arithmetic mean to average individual topic results, shows promise of giving appropriate emphasis to poorly performing topics while being more stable at equal topic set sizes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees04b.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees04b,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2004 Robust Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ROBUST.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees04b.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fondazione Ugo Bordoni at TREC 2004

_Gianni Amati, Claudio Carpineto, Giovanni Romano_

- :fontawesome-solid-user-group: **Participant:** [fub.amati](./participants.md#fub.amati)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/fub.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/fub.robust.pdf)
- :material-file-search: **Runs:** [fub04TDNge](./runs.md#fub04tdnge) | [fub04Tge](./runs.md#fub04tge) | [fub04Dge](./runs.md#fub04dge) | [fub04Te](./runs.md#fub04te) | [fub04De](./runs.md#fub04de) | [fub04TDNe](./runs.md#fub04tdne) | [fub04TDNg](./runs.md#fub04tdng) | [fub04Tg](./runs.md#fub04tg) | [fub04Dg](./runs.md#fub04dg) | [fub04T2ge](./runs.md#fub04t2ge)

??? abstract "Abstract"
	
	Our participation in TREC 2004 aims to extend and improve the use of the DFR (Divergence From Randomness) models with Query Expansion (QE) for the robust track. We experiment with a new parameter-free version of Rocchio's Query Expansion, and use the information theory based function, InfoDFR to predict the AP (Average Precision) of queries. We also study how the use of an external collection affects the retrieval-performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiCR04.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiCR04,
		author = {Gianni Amati and Claudio Carpineto and Giovanni Romano},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Fondazione Ugo Bordoni at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/fub.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiCR04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Can We Get A Better Retrieval Function From Machine?

_Weiguo Fan, Wensi Xi, Edward A. Fox, Li Wang_

- :fontawesome-solid-user-group: **Participant:** [virginia.tech](./participants.md#virginia.tech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/va-tech.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/va-tech.robust.pdf)
- :material-file-search: **Runs:** [vtumlong254](./runs.md#vtumlong254) | [vtumlong348](./runs.md#vtumlong348) | [vtumlong436](./runs.md#vtumlong436) | [vtumlong252](./runs.md#vtumlong252) | [vtumlong344](./runs.md#vtumlong344) | [vtumlong432](./runs.md#vtumlong432) | [vtumdesc](./runs.md#vtumdesc) | [vtumtitle](./runs.md#vtumtitle)

??? abstract "Abstract"
	
	The quality of an information retrieval system heavily depends on its retrieval function, which returns a similarity measurement between the query and each document in the collection. Documents are sorted according to their similarity values with the query and those with high rank are assumed to be relevant. Okapi BM25 and their variations are very popular retrieval functions and they seem to be the default retrieval function for the IR research community; and there are many other widely used and well studied functions, for example, Pivoted TFIDF and INQUERY. Most of these retrieval functions being used today are made based on probabilistic theories and they are adjusted in real world according to different contexts and information needs. In this paper, we propose the idea that a good retrieval function can be discovered by a pure machine learning approach, without using probabilistic theories and knowledge-based techniques. Two machine learning algorithms, Support Vector Machine (SVM) and Genetic Programming (GP) are used for retrieval function discovery, and GP is found to be a more effective approach. The retrieval functions discovered by GP might be hard for human interpretation, but their performance is superior to Okapi BM25, one of the most popular functions. The new retrieval function is combined with query expansion techniques and the retrieval performance is improved significantly. Based on our observations in the empirical study, the GP function is more reliable and effective than Okapi BM25 when query expansion techniques are used.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FanXFW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/FanXFW04,
		author = {Weiguo Fan and Wensi Xi and Edward A. Fox and Li Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Can We Get {A} Better Retrieval Function From Machine?},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/va-tech.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FanXFW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2004 Robust Track Experiments Using PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, H. L. Sun, Peter Deng_

- :fontawesome-solid-user-group: **Participant:** [queens.college.kwok](./participants.md#queens.college.kwok)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/queens-college.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/queens-college.robust.pdf)
- :material-file-search: **Runs:** [pircRB04t1](./runs.md#pircrb04t1) | [pircRB04d3](./runs.md#pircrb04d3) | [pircRB04t2](./runs.md#pircrb04t2) | [pircRB04td2](./runs.md#pircrb04td2) | [pircRB04t3](./runs.md#pircrb04t3) | [pircRB04td3](./runs.md#pircrb04td3) | [pircRB04d2](./runs.md#pircrb04d2) | [pircRB04d4](./runs.md#pircrb04d4) | [pircRB04d5](./runs.md#pircrb04d5) | [pircRB04t4](./runs.md#pircrb04t4)

??? abstract "Abstract"
	
	There were two sub-tasks in the TREC2004 Robust track: given a set of topics, a) improve the effectiveness of the lowest performing 25%, and b) predict their ranking according to their average precision. For task a), we followed the strategy introduced by us last year to improve ad-hoc retrieval by employing the web as an external thesaurus to supplement a given topic description. A new method of probing the web based on a given topic statement called ‘window rotation' was tested. For task b) we employed ε-SVR (epsilon support vector regression) to predict performance of test topics based on training with some simple features such as document frequencies, query term frequencies. This allows performance prediction without retrieval. Features were also added from a retrieval list with the hope that they may predict later stage or web-assisted retrieval better. 200 old topics were used for training to predict the ranking of 49 new topics, as well as the whole set of 249. Runs were done that made use of title only, description only section of a topic, and title-description-combination retrieval lists. Ten submissions including runs that were based on initial retrieval only, retrievals with pseudo-relevance feedback, and with web-assistance. Evaluation shows that we have achieved very good performance for most of our runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGSD04.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGSD04,
		author = {Kui{-}Lam Kwok and Laszlo Grunfeld and H. L. Sun and Peter Deng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2004 Robust Track Experiments Using {PIRCS}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/queens-college.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGSD04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 2004: Robust Track

_Shuang Liu, Chaojing Sun, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [u.illinois.chicago](./participants.md#u.illinois.chicago)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uil-chicago.liu.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/uil-chicago.liu.robust.pdf)
- :material-file-search: **Runs:** [uic0401](./runs.md#uic0401)

??? abstract "Abstract"
	
	In TREC 2004, the Database and Information System Lab (DBIS) at University of Illinois at Chicago (UIC) participates in the robust track, which is a traditional ad hoc retrieval task. The emphasis is based on average effectiveness as well as individual topic effectiveness. In our system, noun phrases in the query are identified and classified into 4 types: proper names, dictionary phrases, simple phrases and complex phrases. A document has a phrase if all content words in a phrase are within a window of a certain size. The window sizes for different types of phrases are different. We consider phrases to be more important than individual terms. As a consequence, documents in response to a query are ranked with matching phrases given a higher priority. WordNet is used to disambiguate word senses. Whenever the sense of a query term is determined, its synonyms, hyponyms, words from its definition and its compound concepts are considered for possible additions to the query. The newly added terms are used to form phrases during retrieval. Pseudo feedback and web-assisted feedback are used to help retrieval. We submit one title run this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuSY04.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuSY04,
		author = {Shuang Liu and Chaojing Sun and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 2004: Robust Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uil-chicago.liu.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuSY04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2004: Robust and Terabyte Tracks

_Christine D. Piatko, James Mayfield, Paul McNamee, R. Scott Cost_

- :fontawesome-solid-user-group: **Participant:** [jhu.apl.mcnamee](./participants.md#jhu.apl.mcnamee)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/jhu-apl.robust.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/jhu-apl.robust.tera.pdf)
- :material-file-search: **Runs:** [apl04rsTDNw5](./runs.md#apl04rstdnw5) | [apl04rsTs](./runs.md#apl04rsts) | [apl04rsTw](./runs.md#apl04rstw) | [apl04rsDw](./runs.md#apl04rsdw) | [apl04rsTDNfw](./runs.md#apl04rstdnfw)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) focused on the Robust and Terabyte Tracks at the 2004 TREC conference.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PiatkoMMC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/PiatkoMMC04,
		author = {Christine D. Piatko and James Mayfield and Paul McNamee and R. Scott Cost},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{JHU/APL} at {TREC} 2004: Robust and Terabyte Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/jhu-apl.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PiatkoMMC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2004: Experiments in Web, Robust,  and Terabyte Tracks with Terrier

_Vassilis Plachouras, Ben He, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [u.glasgow](./participants.md#u.glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf)
- :material-file-search: **Runs:** [uogRobSBase](./runs.md#uogrobsbase) | [uogRobSWR5](./runs.md#uogrobswr5) | [uogRobSWR10](./runs.md#uogrobswr10) | [uogRobDBase](./runs.md#uogrobdbase) | [uogRobDWR5](./runs.md#uogrobdwr5) | [uogRobDWR10](./runs.md#uogrobdwr10) | [uogRobLBase](./runs.md#uogroblbase) | [uogRobLT](./runs.md#uogroblt) | [uogRobLWR5](./runs.md#uogroblwr5) | [uogRobLWR10](./runs.md#uogroblwr10)

??? abstract "Abstract"
	
	With our participation in TREC2004, we test Terrier, a modular and scalable Information Retrieval framework, in three tracks. For the mixed query task of the Web track, we employ a decision mechanism for selecting appropriate retrieval approaches on a per-query basis. For the robust track, in order to cope with the poorly-performing queries, we use two pre-retrieval performance predictors and a weighting function recommender mechanism. We also test a new training approach for the automatic tuning of the term frequency normalisation parameters. In the Terabyte track, we employ a distributed version of Terrier and test the effectiveness of techniques, such as using the anchor text, query expansion and selecting an optimal weighting model for each query. Overall, in all three tracks we participated, Terrier and the tested Divergence From Randomness models were shown to be stable and effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PlachourasHO04.bib) "
	```
	@inproceedings{DBLP:conf/trec/PlachourasHO04,
		author = {Vassilis Plachouras and Ben He and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2004: Experiments in Web, Robust, and Terabyte Tracks with Terrier},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PlachourasHO04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Part-of-Speech Sense Matrix Model Experiments in the TREC 2004 Robust  Track at ICL, PKU

_Bing Swen, Xue-qiang Lü, Hongying Zan, Qi Su, Zhi-guo Lai, Kun Xiang, Jing-he Hu_

- :fontawesome-solid-user-group: **Participant:** [peking.u](./participants.md#peking.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/pekingu.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/pekingu.robust.pdf)
- :material-file-search: **Runs:** [icl04pos2f](./runs.md#icl04pos2f) | [icl04pos2td](./runs.md#icl04pos2td) | [icl04pos2d](./runs.md#icl04pos2d) | [icl04pos2t](./runs.md#icl04pos2t) | [icl04pos7f](./runs.md#icl04pos7f) | [icl04pos48f](./runs.md#icl04pos48f) | [icl04pos7td](./runs.md#icl04pos7td) | [icl04pos7tap](./runs.md#icl04pos7tap) | [icl04pos7tat](./runs.md#icl04pos7tat)

??? abstract "Abstract"
	
	The Robust Retrieval track is a traditional ad hoc retrieval task with the focus on individual topic effectiveness. This track provides us an opportunity to do experiments on our recently proposed IR model using a word-by-sense matrix document representation, which was called Sense Matrix Model (SMM) [Swen 2003, 2004]. For the first time to extensively test the model, some simpler and easy-to-implement forms of SMM is used for this year's Robust track, where the part-of-speeches of words are treated as the (rough) senses of words. Though the model supports several matrix similarity measures and some advanced data analysis techniques, our initial implementation can only handle sense sets at the scale of a few hundreds of senses. Thus a relatively small part-of-speech tag set is employed and only two different matrix similarity measures used. In this paper, we describe our model configuration and methods used in the TREC 2004 Robust track. Implementation issues and the submitted runs are also discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SwenLZSLXH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SwenLZSLXH04,
		author = {Bing Swen and Xue{-}qiang L{\"{u}} and Hongying Zan and Qi Su and Zhi{-}guo Lai and Kun Xiang and Jing{-}he Hu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Part-of-Speech Sense Matrix Model Experiments in the {TREC} 2004 Robust Track at ICL, {PKU}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/pekingu.robust.pdf},
		timestamp = {Fri, 23 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SwenLZSLXH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Robust, Web and Terabyte Retrieval with Hummingbird SearchServer at  TREC 2004

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf)
- :material-file-search: **Runs:** [humR04t1](./runs.md#humr04t1) | [humR04d5](./runs.md#humr04d5) | [humR04t5e1](./runs.md#humr04t5e1) | [humR04d4e5](./runs.md#humr04d4e5) | [humR04t1m](./runs.md#humr04t1m) | [humR04d5m](./runs.md#humr04d5m) | [humR04t1i](./runs.md#humr04t1i) | [humR04t5](./runs.md#humr04t5) | [humR04d5i](./runs.md#humr04d5i) | [humR04d4](./runs.md#humr04d4)

??? abstract "Abstract"
	
	Hummingbird participated in 3 tracks of TREC 2004: the ad hoc task of the Robust Retrieval Track (find at least one relevant document in the first 10 rows from 1.9GB of news and government data), the mixed navigational and distillation task of the Web Track (find the home or named page or key resource pages in 1.2 million pages (18GB) from the .GOV domain), and the ad hoc task of the Terabyte Track (find all the relevant documents with high precision from 25.2 million pages (426GB) from the .GOV domain). In the robustness task, SearchServer found a relevant document in the first 10 rows for 46 of the 49 new short (Title-only) topics. In the web task, SearchServer returned a desired page in the first 10 rows for more than 75% of the 225 queries. In the terabyte task, SearchServer found a relevant document in the first 10 rows for 45 of the 49 short topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson04,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Robust, Web and Terabyte Retrieval with Hummingbird SearchServer at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Hong Kong Polytechnic University at the TREC 2004 Robust Track

_D. Y. Wang, Robert Wing Pong Luk, Kam-Fai Wong_

- :fontawesome-solid-user-group: **Participant:** [hkpu.luk](./participants.md#hkpu.luk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/hkp.u.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/hkp.u.robust.pdf)
- :material-file-search: **Runs:** [polyudp2](./runs.md#polyudp2) | [polyutp3](./runs.md#polyutp3) | [polyudp4](./runs.md#polyudp4) | [polyudp5](./runs.md#polyudp5) | [polyudp6](./runs.md#polyudp6) | [polyutp1](./runs.md#polyutp1)

??? abstract "Abstract"
	
	In the robust track, we mainly tested our passage-based retrieval model with different passage sizes and weighting schemes. In our approach, we used two retrieval models, namely the 2-Poisson model using BM25 term weights and the vector space model (VSM) using adaptive pivoted unique document length normalization. Also, we utilize WordNet to re-weight some PRF terms and extract some context words as expanded query terms. We show that our passage-based model achieves the comparable performance on the whole query set. Moreover, our new methods of using WordNet information for query expansion can improve the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangLW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangLW04,
		author = {D. Y. Wang and Robert Wing Pong Luk and Kam{-}Fai Wong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Hong Kong Polytechnic University at the {TREC} 2004 Robust Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/hkp.u.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangLW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLPR at TREC 2004: Robust Experiments

_Jin Xu, Jun Zhao, Bo Xu_

- :fontawesome-solid-user-group: **Participant:** [cas.nlpr](./participants.md#cas.nlpr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/cas-nlpr.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/cas-nlpr.robust.pdf)
- :material-file-search: **Runs:** [NLPR04clus9](./runs.md#nlpr04clus9) | [NLPR04oktwo](./runs.md#nlpr04oktwo) | [NLPR04OKapi](./runs.md#nlpr04okapi) | [NLPR04okall](./runs.md#nlpr04okall) | [NLPR04okdiv](./runs.md#nlpr04okdiv) | [NLPR04SemLM](./runs.md#nlpr04semlm) | [NLPR04LMts](./runs.md#nlpr04lmts) | [NLPR04LcA](./runs.md#nlpr04lca) | [NLPR04NcA](./runs.md#nlpr04nca) | [NLPR04COMB](./runs.md#nlpr04comb) | [NLPR04clus10](./runs.md#nlpr04clus10)

??? abstract "Abstract"
	
	It is the second time that the Chinese Information Processing group of NLPR participates in TREC. In the past, we have investigated the use of two key technologies: Window-based weighting method and Semantic Tree Model for query expansion, with success, to tasks in novelty and robust tracks. We focused on the Robust Retrieval Track at this year's conference. Based on the previous IR architecture, our research on this year's robust mainly focused on three aspects: (1) two-step retrieval scheme; (2) word sense entropy; (3) several strategies for merging multiple runs. Our paper is organized as follows. Section 2 shows the basic architecture of our IR system and the new techniques for improving its performance. Section 2.1 presents the two-step retrieval scheme which mainly attempts to reduce the influence of noise introduced by query expansion. Section 2.2 introduces a new method for query word weighting—word sense entropy which is a measure for the variety of the sense of query word based on WordNet's structured knowledge. Section 2.3 describes several different strategies which we have used for merging the results of multiple runs produced by different retrieval approaches. Section 3 gives the experimental verification of the techniques mentioned in section 2. Section 4 concludes our work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuZX04.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuZX04,
		author = {Jin Xu and Jun Zhao and Bo Xu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NLPR} at {TREC} 2004: Robust Experiments},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/cas-nlpr.robust.pdf},
		timestamp = {Tue, 19 Jul 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/XuZX04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2004 Genomics, Hard, Robust and Web Tracks

_Kiduk Yang, Ning Yu, Adam Wead, Gavin La Rowe, Yu-Hsiu Li, Christopher Friend, Yoon Lee_

- :fontawesome-solid-user-group: **Participant:** [indiana.u.yang](./participants.md#indiana.u.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf](http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf)
- :material-file-search: **Runs:** [wdoqdn1](./runs.md#wdoqdn1) | [wdoqla1](./runs.md#wdoqla1) | [wdoqsn1](./runs.md#wdoqsn1) | [wdo25qla1](./runs.md#wdo25qla1)

??? abstract "Abstract"
	
	To facilitate understanding of information as well as its discovery, we need to combine the capabilities of the human and the machine as well as multiple methods and sources of evidence. Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science houses several projects that aim to apply this idea of multi-level fusion in the areas of information retrieval and knowledge organization. The TREC research group of WIDIT, who engages in examination of information retrieval strategies that can accommodate a variety of data environments and search tasks, participated in the Genomics, HARD, Robust, and Web tracks in TREC-2004. The basic approach of WIDIT was to leverage multiple sources of evidence, combine multiple methods, and integrate the strengths of man and the machine. Our main strategies for the tracks were: the use of gene name thesaurus in the Genomics track; query expansion and relevance feedback in the HARD track; query expansion with keywords from Web search in the Robust track, and the interactive system tuning process called “Dynamic Tuning” in the Web track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYWRLFL04.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYWRLFL04,
		author = {Kiduk Yang and Ning Yu and Adam Wead and Gavin La Rowe and Yu{-}Hsiu Li and Christopher Friend and Yoon Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2004 Genomics, Hard, Robust and Web Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf},
		timestamp = {Tue, 24 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangYWRLFL04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Juru at TREC 2004: Experiments with Prediction of Query Difficulty

_Elad Yom-Tov, Shai Fine, David Carmel, Adam Darlow, Einat Amitay_

- :fontawesome-solid-user-group: **Participant:** [ibm.haifa.carmel](./participants.md#ibm.haifa.carmel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ibm-haifa.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/ibm-haifa.robust.pdf)
- :material-file-search: **Runs:** [JuruDesAggr](./runs.md#jurudesaggr) | [JuruDesSwQE](./runs.md#jurudesswqe) | [JuruDesQE](./runs.md#jurudesqe) | [JuruTit](./runs.md#jurutit) | [JuruDes](./runs.md#jurudes) | [JuruTitSwQE](./runs.md#jurutitswqe) | [JuruTitDes](./runs.md#jurutitdes) | [JuruDesTrSl](./runs.md#jurudestrsl) | [JuruDesLaMd](./runs.md#jurudeslamd) | [JuruTitSwDs](./runs.md#jurutitswds)

??? abstract "Abstract"
	
	Our experiments in the Robust track this year focused on predicting query difficulty and using this prediction for improving information retrieval. We developed two prediction algorithms and used the subsequent prediction in several ways in order to improve the performance of the search engine. These included modifying the search engine parameters, using selective query expansion, and switching between different topic parts. We also experimented with a new scoring model based on ideas from the field of machine learning. Our results show that query prediction is indeed efficient in improving retrieval, although further work is needed in order to improve the performance of the prediction algorithms and their uses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yom-TovFCDA04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yom-TovFCDA04,
		author = {Elad Yom{-}Tov and Shai Fine and David Carmel and Adam Darlow and Einat Amitay},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Juru at {TREC} 2004: Experiments with Prediction of Query Difficulty},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ibm-haifa.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yom-TovFCDA04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

