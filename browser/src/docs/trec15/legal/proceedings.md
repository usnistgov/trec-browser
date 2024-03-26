# Proceedings - Legal 2006 

#### TREC 2006 Legal Track Overview

_Jason R. Baron, David D. Lewis, Douglas W. Oard_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/LEGAL06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/LEGAL06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	This paper describes the first year of a new TREC track focused on “e-discovery” of business records and other materials. A large collection of scanned documents produced by multiple real world discovery requests was adopted as the basis for the test collection. Topic statements were developed using a process representative of current practice in e-discovery applications, with both Boolean and natural language queries being supported. Relevance judgments were performed by personnel who had received professional training, and often considerable experience, in review of similar materials for this task. Six research teams and one manual searcher submitted a total of 33 retrieved sets for each topic. These were pooled and a portion assessed to support evaluation of both the retrieved sets themselves and for future use of the collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BaronLO06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BaronLO06,
		author = {Jason R. Baron and David D. Lewis and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 Legal Track Overview},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/LEGAL06.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BaronLO06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2006 at Maryland: Blog, Enterprise, Legal and QA Tracks

_Douglas W. Oard, Tamer Elsayed, Jianqiang Wang, Yejun Wu, Pengyi Zhang, Eileen G. Abels, Jimmy Lin, Dagobert Soergel_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf)
- :material-file-search: **Runs:** [UmdBoolAuto](./runs.md#umdboolauto) | [UmdComb](./runs.md#umdcomb) | [UmdBase](./runs.md#umdbase) | [UmdBool](./runs.md#umdbool)

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

#### Experiments with the Negotiated Boolean Queries of the TREC 2006  Legal Discovery Track

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/opentext.legal.final.pdf](http://trec.nist.gov/pubs/trec15/papers/opentext.legal.final.pdf)
- :material-file-search: **Runs:** [humL06tvo](./runs.md#huml06tvo) | [humL06dvo](./runs.md#huml06dvo) | [humL06t0](./runs.md#huml06t0) | [humL06t](./runs.md#huml06t) | [humL06tv](./runs.md#huml06tv) | [humL06tvz](./runs.md#huml06tvz) | [humL06tve](./runs.md#huml06tve) | [humL06tvc](./runs.md#huml06tvc)

??? abstract "Abstract"
	
	We analyze the results of several experimental runs submitted to the Legal Discovery and Terabyte Tracks of TREC 2006. In the Legal Track, the final negotiated boolean queries produced higher mean scores in average precision and Precision@10 than a corresponding vector run of the same query terms, but the vector run usually recalled more relevant items by rank 5000, and on average the boolean query matched less than half of the relevant items. We also report the impact of query negotiation, metadata and natural language vs. keywords. We find that robust metrics (which expose the downside of blind feedback techniques) are inappropriate for legal discovery because they favour duplicate filtering. We also report the results of depth probe experiments (depth 9000 in the Legal Track and depth 5000 in the Terabyte Track) which provide a lower-bound estimate for the number of unjudged relevant items in each track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson06,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with the Negotiated Boolean Queries of the {TREC} 2006 Legal Discovery Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/opentext.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2006: Legal Track

_Miao Wen, Xiangji Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/yorku.legal.pdf](http://trec.nist.gov/pubs/trec15/papers/yorku.legal.pdf)
- :material-file-search: **Runs:** [york06la01](./runs.md#york06la01) | [york06la02](./runs.md#york06la02)

??? abstract "Abstract"
	
	York University participated in the legal track this year. For this track, we developed an Okapi-based Legal Search Engine (LSE) v1.0. Our experiments mainly focused on evaluating the effect of a probabilistic text retrieval model on the legal domain. In order to address the special problems in legal text retrieval, new automatic feedback methods and term weighting methods are proposed and tested.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WenH06.bib) "
	```
	@inproceedings{DBLP:conf/trec/WenH06,
		author = {Miao Wen and Xiangji Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2006: Legal Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/yorku.legal.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WenH06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with Query Expansion at TREC 2006 Legal Track

_Feng C. Zhao, Yugyung Lee, Deep Medhi_

- :fontawesome-solid-user-group: **Participant:** [umkc.zhao](./participants.md#umkc.zhao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umissouri-kc.legal.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umissouri-kc.legal.final.pdf)
- :material-file-search: **Runs:** [UMKCQE100](./runs.md#umkcqe100) | [UMKCSN](./runs.md#umkcsn) | [UMKCSW](./runs.md#umkcsw) | [UMKCB](./runs.md#umkcb) | [UMKCQE25](./runs.md#umkcqe25) | [UMKCB2](./runs.md#umkcb2) | [UMKCBQE10](./runs.md#umkcbqe10) | [UMKCBQE5](./runs.md#umkcbqe5)

??? abstract "Abstract"
	
	This paper describes the UMKC TREC 2006 Legal Track experiments. We focus on a single technique that uses cooccurrence based thesaurus to expand queries. Our results indicate this technique is effective even towards the enormous vocabulary size in the IIT CDIP collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoLM06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoLM06,
		author = {Feng C. Zhao and Yugyung Lee and Deep Medhi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with Query Expansion at {TREC} 2006 Legal Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umissouri-kc.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoLM06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

