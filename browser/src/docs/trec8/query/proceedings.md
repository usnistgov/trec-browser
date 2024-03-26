# Proceedings - Query 1999 

#### The TREC-8 Query Track

_Chris Buckley, Janet A. Walz_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/qtrack.pdf](http://trec.nist.gov/pubs/trec8/papers/qtrack.pdf)
??? abstract "Abstract"
	
	The Query Track in TREC-8 is a bit different from all the other tracks. It is a cooperative effort among the participating groups to look at the issue of 'query variability'. The evaluation averages presented in a typical system evaluation task, such as the TREC Ad-Hoc Task, conceal a tremendous variability of system performance across topics/queries. No system can possibly perform equally well on all topics: some information needs (expressed by topics) are harder than others. But what is quite surprising, especially to people just starting to look at IR, is the large variability in system performance across topics as compared to other systems. In a typical TREC task, no system is the best for all the topics in the task. It is extremely rare for any system to be above average for all the topics. Instead, the best system is normally above average for most of the topics, and best for maybe 5%-10% of the topics. It very often happens that quite below-average systems are also best for 5%-10% of the topics, but do poorly on the other topics. The Average Precision Histograms presented on the TREC evaluation result pages are an attempt to show what is happening at the individual topic level. This large topic/query variability presents a great opportunity for improving system performance. If we can understand why some systems do well on some queries but poorly on others, then we can start introducing query dependent processing to improve results on those poor performance queries. Unfortunately, we just don't have enough information from the results of a typical TREC task to really understand what is happening. The results on 50 to 150 queries are just not enough to draw any conclusions. The Query Track at TREC is an attempt to gather enough information from a large number of systems on a large number of queries to be able to start understanding query variability.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyW99,
		author = {Chris Buckley and Janet A. Walz},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-8} Query Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/qtrack.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Ad-Hoc, Query and Filtering Track Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf](http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf)
- :material-file-search: **Runs:** [pirINQ1a](./runs.md#pirinq1a) | [pirINQ1b](./runs.md#pirinq1b) | [pirINQ1c](./runs.md#pirinq1c) | [pirINQ1d](./runs.md#pirinq1d) | [pirINQ1e](./runs.md#pirinq1e) | [pirINQ2b](./runs.md#pirinq2b) | [pirINQ2c](./runs.md#pirinq2c) | [pirINQ2a](./runs.md#pirinq2a) | [pirINQ2d](./runs.md#pirinq2d) | [pirINQ2e](./runs.md#pirinq2e) | [pirINQ3a](./runs.md#pirinq3a) | [pirINQ3b](./runs.md#pirinq3b) | [pirINQ3c](./runs.md#pirinq3c) | [pirINQ3d](./runs.md#pirinq3d) | [pirINQ3e](./runs.md#pirinq3e) | [pirSab1a](./runs.md#pirsab1a) | [pirSab1c](./runs.md#pirsab1c) | [pirSab1b](./runs.md#pirsab1b) | [pirpir1a](./runs.md#pirpir1a) | [piracs1a](./runs.md#piracs1a) | [pirSab3a](./runs.md#pirsab3a)

??? abstract "Abstract"
	
	In TREC-8, we participated in automatic ad-hoc retrieval as well as the query and filtering tracks. The theme of our participation is 'retrieval lists combination', and the technique is applied throughout our experiments to various degree. It is pointed out that our PIRCS system may be considered as a combination of probabilistic retrieval model and a language model approach. For ad-hoc, three types of experiments were done with short, medium and long queries as before. General approach is similar to TREC-7, but combination of retrieval lists from different query types were used to boost effectiveness. For query track, we submitted one short-query set, and performed retrieval for twenty one natural language query vairants. For filtering track, experiments for adaptive, batch filtering, and routing were performed. For adaptive, historical selected document list was used to train profile term weights and dynamically vary retrieval status value (rsv) threshold for deciding document selection during the course of filtering. For batch filtering, Financial Times FT92 data was used to define 6 retrieval profiles whose results were combined based on coefficients trained via a genetic algorithm. Logistic regression transforms rsv's to probabilities. Routing was similarly done with additional training data obtained from non-FT collections and two additional profiles were defined and combined
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGC99,
		author = {K. L. Kwok and Laszlo Grunfeld and M. Chan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Ad-Hoc, Query and Filtering Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ACSys TREC-8 Experiments

_David Hawking, Peter Bailey, Nick Craswell_

- :fontawesome-solid-user-group: **Participant:** [ACSys](./participants.md#acsys)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/acsys.pdf](http://trec.nist.gov/pubs/trec8/papers/acsys.pdf)
- :material-file-search: **Runs:** [acsAPL5b](./runs.md#acsapl5b) | [acsINQ1a](./runs.md#acsinq1a) | [acsAPL5a](./runs.md#acsapl5a) | [acsINQ1b](./runs.md#acsinq1b) | [acsINQ1c](./runs.md#acsinq1c) | [acsINQ1e](./runs.md#acsinq1e) | [acsINQ2a](./runs.md#acsinq2a) | [acsINQ2b](./runs.md#acsinq2b) | [acsINQ2e](./runs.md#acsinq2e) | [acsINQ2c](./runs.md#acsinq2c) | [acsINQ3a](./runs.md#acsinq3a) | [acsINQ3b](./runs.md#acsinq3b) | [acsINQ3c](./runs.md#acsinq3c) | [acsINQ3e](./runs.md#acsinq3e) | [acsSab1a](./runs.md#acssab1a) | [acsSab1c](./runs.md#acssab1c) | [acsSab1b](./runs.md#acssab1b) | [acspir1a](./runs.md#acspir1a) | [acsSab3a](./runs.md#acssab3a) | [acsINQ1d](./runs.md#acsinq1d) | [acsINQ2d](./runs.md#acsinq2d) | [acsINQ3d](./runs.md#acsinq3d) | [acsacs1a](./runs.md#acsacs1a)

??? abstract "Abstract"
	
	Experiments relating to TREC-8 Ad Hoc, Web Track (Large and Small) and Query Track tasks are described and results reported. Due to time constraints, only minimal effort was put into Ad Hoc and Query Track participation. In the Web Track, Google-style PageRanks were calculated for all 18.5 million pages in the VLC2 collection and for the 0.25 million pages in the WT2g collection. Various combinations of content score and PageRank produced no benefit for TREC style ad hoc retrieval. A major goal in the Web Track was to make engineering improvements to permit indexing of the 100 gigabyte collection and subsequent query processing using a single PC. A secondary goal was to achieve last year's performance (obtained with eight DEC Alphas) with less recourse to effectiveness-harming optimisations. The main goal was achieved and indexing times are comparable to last year's. However, effectiveness results were worse relative to last year and query processing times were approximately double.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingBC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingBC99,
		author = {David Hawking and Peter Bailey and Nick Craswell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ACSys {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/acsys.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingBC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SMART in TREC 8

_Chris Buckley, Janet A. Walz_

- :fontawesome-solid-user-group: **Participant:** [cornell](./participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/sabir8.pdf](http://trec.nist.gov/pubs/trec8/papers/sabir8.pdf)
- :material-file-search: **Runs:** [SabaINQ1a](./runs.md#sabainq1a) | [Sab5APL5a](./runs.md#sab5apl5a) | [Sab5APL5b](./runs.md#sab5apl5b) | [SabaINQ1b](./runs.md#sabainq1b) | [SabaINQ1c](./runs.md#sabainq1c) | [SabaINQ1d](./runs.md#sabainq1d) | [SabaINQ1e](./runs.md#sabainq1e) | [SabaINQ2a](./runs.md#sabainq2a) | [SabaINQ2b](./runs.md#sabainq2b) | [SabaINQ2c](./runs.md#sabainq2c) | [SabaINQ2d](./runs.md#sabainq2d) | [SabaINQ2e](./runs.md#sabainq2e) | [SabaINQ3a](./runs.md#sabainq3a) | [SabaINQ3b](./runs.md#sabainq3b) | [SabaINQ3c](./runs.md#sabainq3c) | [SabaINQ3e](./runs.md#sabainq3e) | [SabaINQ3d](./runs.md#sabainq3d) | [SabaSab1a](./runs.md#sabasab1a) | [SabaSab1b](./runs.md#sabasab1b) | [SabaSab1c](./runs.md#sabasab1c) | [SabaSab3a](./runs.md#sabasab3a) | [Sabaacs1a](./runs.md#sabaacs1a) | [Sabapir1a](./runs.md#sabapir1a) | [SabeINQ1a](./runs.md#sabeinq1a) | [SabeINQ1b](./runs.md#sabeinq1b) | [SabeINQ1c](./runs.md#sabeinq1c) | [SabeINQ1d](./runs.md#sabeinq1d) | [SabeINQ1e](./runs.md#sabeinq1e) | [SabeINQ2a](./runs.md#sabeinq2a) | [SabeINQ2b](./runs.md#sabeinq2b) | [SabeINQ2c](./runs.md#sabeinq2c) | [SabeINQ2d](./runs.md#sabeinq2d) | [SabeINQ2e](./runs.md#sabeinq2e) | [SabeINQ3a](./runs.md#sabeinq3a) | [SabeINQ3b](./runs.md#sabeinq3b) | [SabeINQ3c](./runs.md#sabeinq3c) | [SabeINQ3d](./runs.md#sabeinq3d) | [SabeINQ3e](./runs.md#sabeinq3e) | [SabeSab1a](./runs.md#sabesab1a) | [SabeSab1b](./runs.md#sabesab1b) | [SabeSab1c](./runs.md#sabesab1c) | [SabeSab3a](./runs.md#sabesab3a) | [Sabeacs1a](./runs.md#sabeacs1a) | [Sabepir1a](./runs.md#sabepir1a) | [SabmINQ1a](./runs.md#sabminq1a) | [SabmINQ1b](./runs.md#sabminq1b) | [SabmINQ1c](./runs.md#sabminq1c) | [SabmINQ1d](./runs.md#sabminq1d) | [SabmINQ1e](./runs.md#sabminq1e) | [SabmINQ2a](./runs.md#sabminq2a) | [SabmINQ2b](./runs.md#sabminq2b) | [SabmINQ2c](./runs.md#sabminq2c) | [SabmINQ2d](./runs.md#sabminq2d) | [SabmINQ2e](./runs.md#sabminq2e) | [SabmINQ3a](./runs.md#sabminq3a) | [SabmINQ3b](./runs.md#sabminq3b) | [SabmINQ3c](./runs.md#sabminq3c) | [SabmINQ3d](./runs.md#sabminq3d) | [SabmINQ3e](./runs.md#sabminq3e) | [SabmSab1a](./runs.md#sabmsab1a) | [SabmSab1b](./runs.md#sabmsab1b) | [SabmSab1c](./runs.md#sabmsab1c) | [SabmSab3a](./runs.md#sabmsab3a) | [Sabmacs1a](./runs.md#sabmacs1a) | [Sabmpir1a](./runs.md#sabmpir1a) | [SabmAPL5b](./runs.md#sabmapl5b) | [SabeAPL5b](./runs.md#sabeapl5b) | [SabeAPL5a](./runs.md#sabeapl5a) | [SabmAPL5a](./runs.md#sabmapl5a)

??? abstract "Abstract"
	
	This year was a light year for the Smart Information Retrieval Project at SabIR Research and Cornell. We officially participated in only the Ad-hoc Task and the Query Track. In the Ad-hoc Task, we made minor modifications to our document weighting schemes to emphasize high-precision searches on shorter queries. This proved only mildly successful; the top relevant document was retrieved higher, but the rest of the retrieval tended to be hurt. Our Query Track runs are described here, but the much more interesting analysis of these runs is described in the Query Track Overview.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyW99a.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyW99a,
		author = {Chris Buckley and Janet A. Walz},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SMART} in {TREC} 8},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/sabir8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyW99a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-8

_James Allan, James P. Callan, Fangfang Feng, Daniella Malin_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf)
- :material-file-search: **Runs:** [INQaINQ1a](./runs.md#inqainq1a) | [INQaINQ1b](./runs.md#inqainq1b) | [INQaINQ1e](./runs.md#inqainq1e) | [INQaINQ1c](./runs.md#inqainq1c) | [INQaINQ2b](./runs.md#inqainq2b) | [INQaINQ2a](./runs.md#inqainq2a) | [INQaINQ2c](./runs.md#inqainq2c) | [INQaINQ2d](./runs.md#inqainq2d) | [INQaINQ2e](./runs.md#inqainq2e) | [INQaINQ3a](./runs.md#inqainq3a) | [INQaSab1b](./runs.md#inqasab1b) | [INQaINQ3c](./runs.md#inqainq3c) | [INQaSab1a](./runs.md#inqasab1a) | [INQaINQ3e](./runs.md#inqainq3e) | [INQaSab3a](./runs.md#inqasab3a) | [INQaINQ1d](./runs.md#inqainq1d) | [INQaSab1c](./runs.md#inqasab1c) | [INQaacs1a](./runs.md#inqaacs1a) | [INQaINQ3b](./runs.md#inqainq3b) | [INQeINQ1a](./runs.md#inqeinq1a) | [INQapir1a](./runs.md#inqapir1a) | [INQeINQ1d](./runs.md#inqeinq1d) | [INQeacs1a](./runs.md#inqeacs1a) | [INQaINQ3d](./runs.md#inqainq3d) | [INQeINQ1b](./runs.md#inqeinq1b) | [INQeINQ2d](./runs.md#inqeinq2d) | [INQpAPL5a](./runs.md#inqpapl5a) | [INQeINQ1e](./runs.md#inqeinq1e) | [INQpINQ3b](./runs.md#inqpinq3b) | [INQpINQ3c](./runs.md#inqpinq3c) | [INQpINQ2d](./runs.md#inqpinq2d) | [INQeINQ1c](./runs.md#inqeinq1c) | [INQpINQ1c](./runs.md#inqpinq1c) | [INQpINQ3e](./runs.md#inqpinq3e) | [INQeINQ2a](./runs.md#inqeinq2a) | [INQeSab3a](./runs.md#inqesab3a) | [INQeSab1b](./runs.md#inqesab1b) | [INQpacs1a](./runs.md#inqpacs1a) | [INQpINQ1e](./runs.md#inqpinq1e) | [INQeSab1c](./runs.md#inqesab1c) | [INQpSab1c](./runs.md#inqpsab1c) | [INQpINQ1d](./runs.md#inqpinq1d) | [INQppir1a](./runs.md#inqppir1a) | [INQpINQ2a](./runs.md#inqpinq2a) | [INQpSab1a](./runs.md#inqpsab1a) | [INQeAPL5a](./runs.md#inqeapl5a) | [INQeAPL5b](./runs.md#inqeapl5b) | [INQeINQ2b](./runs.md#inqeinq2b) | [INQpINQ2b](./runs.md#inqpinq2b) | [INQeINQ3b](./runs.md#inqeinq3b) | [INQeINQ2e](./runs.md#inqeinq2e) | [INQeINQ2c](./runs.md#inqeinq2c) | [INQeINQ3e](./runs.md#inqeinq3e) | [INQeINQ3a](./runs.md#inqeinq3a) | [INQpAPL5b](./runs.md#inqpapl5b) | [INQeINQ3c](./runs.md#inqeinq3c) | [INQeINQ3d](./runs.md#inqeinq3d) | [INQpINQ2e](./runs.md#inqpinq2e) | [INQepir1a](./runs.md#inqepir1a) | [INQpINQ3d](./runs.md#inqpinq3d) | [INQpSab1b](./runs.md#inqpsab1b) | [INQpINQ3a](./runs.md#inqpinq3a) | [INQpINQ1b](./runs.md#inqpinq1b) | [INQeSab1a](./runs.md#inqesab1a) | [INQpINQ1a](./runs.md#inqpinq1a) | [INQpSab3a](./runs.md#inqpsab3a) | [INQpINQ2c](./runs.md#inqpinq2c)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in seven of the tracks: ad-hoc, filtering, spoken document retrieval, small web, large web, question and answer, and the query tracks. We spent significant time working on the filtering track, resulting in substantial performance improvement over TREC-7. For all of the other tracks, we used essentially the same system as used in previous years. In the next section, we describe some of the basic processing that was applied across most of the tracks. We then describe the details for each of the tracks and in some cases present some modest analysis of the effectiveness of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCFM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCFM99,
		author = {James Allan and James P. Callan and Fangfang Feng and Daniella Malin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCFM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

