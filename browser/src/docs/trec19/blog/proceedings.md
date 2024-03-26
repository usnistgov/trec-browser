# Proceedings - Blog 2010 

#### Overview of the TREC 2010 Blog Track

_Iadh Ounis, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec19/papers/BLOG.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec19/papers/BLOG.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Blog track aims to investigate the information seeking behaviour in the blogosphere. The track was initiated in 2006, and has used an incremental approach in tackling several search tasks by their level of difficulty. In TREC 2010, the track has investigated two main search tasks: Faceted blog distillation: A blog search task where systems aim to retrieve bloggers (i.e. RSS feeds) that have a recurring and central interest in a topic X [6], and which also satisfy a number of facets (or attributes), representing the nature or the quality of the sought blogs (e.g. opinionated, factual) [7]. Top stories identification: A task that addresses news-related issues on the blogosphere, namely investigating whether the blogosphere can be leveraged to identify the top news stories of a given day in a real-time fashion. The task has also a search diversity flavour, where for a given story, a representative set of blog posts discussing the story from various perspectives [7] is shown to the user. Both tasks this year used the Blogs08 corpus [7, 9], which is a sample of the blogosphere covering a timespan ranging from January 2008 to February 2009. The Blogs08 collection consists of roughly 1.4M blog feeds and 29M blog posts. In addition, for the purposes of the top stories identification task, a new large corpus of news stories covering the same timespan as Blogs08 has been released by Thomson Reuters. The corpus, called Thomson Reuters Research Collection (TRC2), contains both the headlines and content of over 1.8M news stories. The topics for the faceted blog distillation task have been developed and assessed by NIST. On the other hand, for the top stories identification task, a number of dates have been sampled from the range of dates covered by Blogs08 and used as query dates. To develop topics for the search diversification component of the top stories identification task, the organisers have selected a set of news stories, for which the participating groups were asked to rank diverse blog posts discussing these stories in the blogosphere. In a marked departure from the usually adopted community judgements, in TREC 2010, the Blog track organisers made a first attempt at using crowdsourcing within TREC, where all runs submitted to the top stories task have been assessed through the use of the Amazon Mechanical Turk (AMT) service. A total of 16 different groups participated in the 2010 Blog track, spread across four continents. Many groups attempted both tasks, deploying varying approaches ranging from advanced probabilistic retrieval models, to classification and/or machine learning-driven techniques. The remainder of this paper is structured as follows. Section 2 describes the faceted blog distillation task, and discusses the main obtained results by the participating groups. Section 3 describes the top stories identification task and its corresponding results. Concluding remarks are provided in Section 4.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OunisS10.bib) "
	```
	@inproceedings{DBLP:conf/trec/OunisS10,
		author = {Iadh Ounis and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2010 Blog Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {https://trec.nist.gov/pubs/trec19/papers/BLOG.OVERVIEW.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OunisS10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Blog Track TREC 2010

_Xueke Xu, Yue Liu, Hongbo Xu, Xiaoming Yu, Zeying Peng, Xueqi Cheng, Lihao Xiao, Shuaishuai Nie_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.BLOG2.new.pdf](http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.BLOG2.new.pdf)
- :material-file-search: **Runs:** [ICTNETBDRun1](./runs.md#ictnetbdrun1) | [ICTNETBDRun2](./runs.md#ictnetbdrun2) | [ICTNETFBD2](./runs.md#ictnetfbd2) | [ICTNETBD2](./runs.md#ictnetbd2) | [ICTNETFBD3](./runs.md#ictnetfbd3) | [ICTNETBD3](./runs.md#ictnetbd3) | [ICTNETFBD4](./runs.md#ictnetfbd4) | [ICTNETBD4](./runs.md#ictnetbd4) | [ICTNETBD1](./runs.md#ictnetbd1) | [ICTNETFBD1](./runs.md#ictnetfbd1) | [ICTNETFBDs2](./runs.md#ictnetfbds2) | [ICTNETFBDs3](./runs.md#ictnetfbds3) | [ICTNETTSRun1](./runs.md#ictnettsrun1) | [ICTNETTSRun3](./runs.md#ictnettsrun3) | [ICTNETTSRun2](./runs.md#ictnettsrun2) | [ICTNETPRRun1](./runs.md#ictnetprrun1) | [ICTNETPRRun2](./runs.md#ictnetprrun2) | [ICTNETPRRun3](./runs.md#ictnetprrun3)

??? abstract "Abstract"
	
	This paper describes our participation in blog track of TREC2010. We submit runs for both two tasks, this paper mainly describe approaches to the two tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuLXYPCXN10.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuLXYPCXN10,
		author = {Xueke Xu and Yue Liu and Hongbo Xu and Xiaoming Yu and Zeying Peng and Xueqi Cheng and Lihao Xiao and Shuaishuai Nie},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Blog Track {TREC} 2010},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.BLOG2.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuLXYPCXN10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FEUP at TREC 2010 Blog Track: Using h-index for blog ranking

_José Luís Devezas, Sérgio Nunes, Cristina Ribeiro_

- :fontawesome-solid-user-group: **Participant:** [feup](./participants.md#feup)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/labs-sapo-up.blog.pdf](http://trec.nist.gov/pubs/trec19/papers/labs-sapo-up.blog.pdf)
- :material-file-search: **Runs:** [FEUPirlab1](./runs.md#feupirlab1) | [FEUPirlab2](./runs.md#feupirlab2)

??? abstract "Abstract"
	
	This paper describes the participation of FEUP, from the University of Porto, in the TREC 2010 Blog Track. FEUP participated in the baseline blog distillation task with work focused on the use of link features available in the TREC Blogs08 collection. The approach presented in this paper uses the link information available in most individual posts to amplify each post's score. Blog scores, and subsequent ranks, are obtained by combining individual post scores. We boost post scores using the in-degree of each post and the h-index of each blog. This results in an improvement of P@10, over our baseline, for the in-degree and the h-index runs. When compared to the indegree, the h-index run results in higher performance values for each of the applied evaluation metrics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DevezasNR10.bib) "
	```
	@inproceedings{DBLP:conf/trec/DevezasNR10,
		author = {Jos{\'{e}} Lu{\'{\i}}s Devezas and S{\'{e}}rgio Nunes and Cristina Ribeiro},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FEUP} at {TREC} 2010 Blog Track: Using h-index for blog ranking},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/labs-sapo-up.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DevezasNR10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKUTM at TREC 2010 Blog Track

_Liqiang Guo, Fangzhou Zhai, Yan Shao, Xiaojun Wan_

- :fontawesome-solid-user-group: **Participant:** [PKUTM](./participants.md#pkutm)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/peking.univ.rev.BLOG.pdf](http://trec.nist.gov/pubs/trec19/papers/peking.univ.rev.BLOG.pdf)
- :material-file-search: **Runs:** [PKUTMB1](./runs.md#pkutmb1) | [PKUTMB2](./runs.md#pkutmb2) | [PKUTM111onB1](./runs.md#pkutm111onb1) | [PKUTM121onB1](./runs.md#pkutm121onb1) | [PKUTM211onB1](./runs.md#pkutm211onb1) | [PKUTM321onB1](./runs.md#pkutm321onb1) | [PKUTM111onB2](./runs.md#pkutm111onb2) | [PKUTM211onB2](./runs.md#pkutm211onb2) | [PKUTM221onB2](./runs.md#pkutm221onb2) | [PKUTM321onB2](./runs.md#pkutm321onb2) | [PKUTM111STD1](./runs.md#pkutm111std1) | [PKUTM123STD1](./runs.md#pkutm123std1) | [PKUTM211STD1](./runs.md#pkutm211std1) | [PKUTM222STD1](./runs.md#pkutm222std1) | [PKUTM111STD2](./runs.md#pkutm111std2) | [PKUTM121STD2](./runs.md#pkutm121std2) | [PKUTM221STD2](./runs.md#pkutm221std2) | [PKUTM211STD2](./runs.md#pkutm211std2) | [PKUTM111STD3](./runs.md#pkutm111std3) | [PKUTM121STD3](./runs.md#pkutm121std3) | [PKUTM211STD3](./runs.md#pkutm211std3) | [PKUTM221STD3](./runs.md#pkutm221std3)

??? abstract "Abstract"
	
	This paper describes the PKUTM participation in the TREC 2010 Blog Track. We only concentrated on the Faceted Blog Distillation Task this year. Our system adopts a two-stage approach for this task. In the first stage, our system makes use of an IR platform - indri to obtain the top N ad-hoc topic-relevant blog posts for each query. In the second stage, different models are designed to identify the facet inclination. The experimental results show the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuoZSW10.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuoZSW10,
		author = {Liqiang Guo and Fangzhou Zhai and Yan Shao and Xiaojun Wan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PKUTM} at {TREC} 2010 Blog Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/peking.univ.rev.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuoZSW10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 2010 Faceted Blog Distillation

_Lifeng Jia, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [UICIR](./participants.md#uicir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.illinois-chicago.blog.rev2.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.illinois-chicago.blog.rev2.pdf)
- :material-file-search: **Runs:** [uicfeedir2](./runs.md#uicfeedir2) | [uicfeedir1](./runs.md#uicfeedir1) | [uicfbdrun2](./runs.md#uicfbdrun2) | [uicfbdstd1a](./runs.md#uicfbdstd1a) | [uicfbdstd2a](./runs.md#uicfbdstd2a) | [uicfbdstd3a](./runs.md#uicfbdstd3a) | [uicfbdstd1b](./runs.md#uicfbdstd1b) | [uicfbdstd2b](./runs.md#uicfbdstd2b) | [uicfbdstd3b](./runs.md#uicfbdstd3b) | [uicfbdstd1c](./runs.md#uicfbdstd1c)

??? abstract "Abstract"
	
	Our system consists of a concept-based retrieval subsystem which performs the baseline blog distillation, an opinion identification subsystem and an opinion-in-depth analysis subsystem which performs the faceted blog distillation task. In the baseline task, documents which are deemed relevant are retrieved by the retrieval system with respect to the query, without taking into consideration of any facet requirements. The feeds are ranked in descending order of the sum of the relevance scores of retrieved documents. In order to improve the recall of the retrieval subsystem, we recognize proper nouns or dictionary phrases without requiring matching all the words of the phrases. In the opinionated vs. factual and personal vs. official faceted tasks, the opinion identification subsystem is employed to recognize query-relevant opinions within the documents. Personal documents are more likely to be opinionated than official documents. In the in-depth vs. shallow faceted task, the depth of the opinion within a document is measured by the number of concepts which are related with the query the document contains.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiaY10.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiaY10,
		author = {Lifeng Jia and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 2010 Faceted Blog Distillation},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.illinois-chicago.blog.rev2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiaY10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BIT at TREC 2010 Blog Track: Faceted Blog Distillation

_Peng Jiang, Qing Yang, Chunxia Zhang, Zhendong Niu_

- :fontawesome-solid-user-group: **Participant:** [BIT](./participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.REV.pdf](http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.REV.pdf)
- :material-file-search: **Runs:** [BITblog10bl1](./runs.md#bitblog10bl1) | [BITblog10bl2](./runs.md#bitblog10bl2) | [BIT10std1fd1](./runs.md#bit10std1fd1) | [BIT10bl1fd1](./runs.md#bit10bl1fd1) | [BIT10bl1fd2](./runs.md#bit10bl1fd2) | [BIT10std1fd2](./runs.md#bit10std1fd2) | [BIT10std1fd4](./runs.md#bit10std1fd4) | [BIT10bl1fd3](./runs.md#bit10bl1fd3) | [BIT10bl1fd4](./runs.md#bit10bl1fd4) | [BIT10bl2fd3](./runs.md#bit10bl2fd3) | [BIT10bl2fd4](./runs.md#bit10bl2fd4) | [BIT10std1fd3](./runs.md#bit10std1fd3) | [BIT10bl2fd1](./runs.md#bit10bl2fd1) | [BIT10bl2fd2](./runs.md#bit10bl2fd2) | [BIT10std2fd1](./runs.md#bit10std2fd1) | [BIT10std3fd1](./runs.md#bit10std3fd1)

??? abstract "Abstract"
	
	This paper presents the work done for the TREC 2010 faceted blog distillation task. As the approach used in TREC 2009, a mixture of language models based on global representation is employed to rank the entire blogs by relevance and facets. The parameters in our approach are adjusted according to the experimental results in TREC 2009. In addition, we make use of the results evaluated in TREC 2009 to train a SVM classifier. This classifier is used to filter and re-rank the results obtained by the mixture model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangYZN10.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangYZN10,
		author = {Peng Jiang and Qing Yang and Chunxia Zhang and Zhendong Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BIT} at {TREC} 2010 Blog Track: Faceted Blog Distillation},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.REV.pdf},
		timestamp = {Fri, 04 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JiangYZN10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lugano at TREC 2010

_Mostafa Keikha, Parvaz Mahdabi, Shima Gerani, Giacomo Inches, Javier Parapar, Mark James Carman, Fabio Crestani_

- :fontawesome-solid-user-group: **Participant:** [ULugano](./participants.md#ulugano)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.lugano.blog.session.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.lugano.blog.session.pdf)
- :material-file-search: **Runs:** [bloggerModel](./runs.md#bloggermodel) | [LexMIRuns1](./runs.md#lexmiruns1) | [LexMIRuns2](./runs.md#lexmiruns2) | [LexMIRuns3](./runs.md#lexmiruns3) | [MILexRuns1](./runs.md#milexruns1) | [MILexRuns2](./runs.md#milexruns2) | [MILexRuns3](./runs.md#milexruns3) | [ComSumScores](./runs.md#comsumscores) | [CombMNZ](./runs.md#combmnz) | [OWAScores](./runs.md#owascores)

??? abstract "Abstract"
	
	We report on the University of Lugano's participation in the Blog and Session tracks of TREC 2010. In particular we describe our system for performing blog distillation, faceted search, top stories identification and session reranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KeikhaMGIPCC10.bib) "
	```
	@inproceedings{DBLP:conf/trec/KeikhaMGIPCC10,
		author = {Mostafa Keikha and Parvaz Mahdabi and Shima Gerani and Giacomo Inches and Javier Parapar and Mark James Carman and Fabio Crestani},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Lugano at {TREC} 2010},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.lugano.blog.session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KeikhaMGIPCC10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2010 Blog Track: Top Stories Identification

_Yeha Lee, Woosang Song, Hun-Young Jung, Vinh Tao Thanh, Jong-Hyeok Lee_

- :fontawesome-solid-user-group: **Participant:** [POSTECH_KLE](./participants.md#postech_kle)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/pohang.univ.s-t.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/pohang.univ.s-t.blog.rev.pdf)
- :material-file-search: **Runs:** [KLERUN1](./runs.md#klerun1) | [KLERUN2](./runs.md#klerun2) | [KLERUN3](./runs.md#klerun3) | [KLE1](./runs.md#kle1) | [KLE2](./runs.md#kle2)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2010 Blog Track. For the Top Stories Identification Task, we explore the relationship among news events, news stories and blog posts. We first extract important news events from the TRC2 corpus using a probabilistic mixture model. Then, we propose a probabilistic approach to identify top news stories. Furthermore, we use an additional feature that can be useful in identifying top news stories. For the News Blog Post Ranking Task, we apply the Maximal Marginal Relevance method (MMR) to make the aspects of the blog posts more diverse.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeSJTL10.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeSJTL10,
		author = {Yeha Lee and Woosang Song and Hun{-}Young Jung and Vinh Tao Thanh and Jong{-}Hyeok Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2010 Blog Track: Top Stories Identification},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/pohang.univ.s-t.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeSJTL10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2010 Blog Track: Faceted Blog Distillaton

_Si Li, Yan Li, Jiayue Zhang, Jingyi Guan, Xueji Sun, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/beijing.univ.p-t.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/beijing.univ.p-t.blog.rev.pdf)
- :material-file-search: **Runs:** [prisb](./runs.md#prisb) | [pris](./runs.md#pris) | [PrisStdQ0](./runs.md#prisstdq0) | [PrisStdQ02](./runs.md#prisstdq02) | [PrisStdQ03](./runs.md#prisstdq03) | [PrisStdQ04](./runs.md#prisstdq04) | [PrisStdQE1](./runs.md#prisstdqe1) | [PrisStdQE2](./runs.md#prisstdqe2) | [PrisStdQE3](./runs.md#prisstdqe3) | [PrisQ01](./runs.md#prisq01) | [PrisQ02](./runs.md#prisq02) | [PrisQ03](./runs.md#prisq03) | [PrisQ04](./runs.md#prisq04) | [PrisQE1](./runs.md#prisqe1) | [PrisQE2](./runs.md#prisqe2)

??? abstract "Abstract"
	
	This paper presents the system adopted for the Faceted Blog Distillation task by PRIS team. The PRIS system is submitted by Pattern Recognition and Intelligent System Lab at Beijing University of Posts and Telecommunications. And a two-stage strategy is involved for this task. First, an adaptable Voting Model is carried out for blog distillation. Then, different models are designed to judge the facets and ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiLZGSXCG10.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiLZGSXCG10,
		author = {Si Li and Yan Li and Jiayue Zhang and Jingyi Guan and Xueji Sun and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2010 Blog Track: Faceted Blog Distillaton},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/beijing.univ.p-t.blog.rev.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiLZGSXCG10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Top Stories Identification From Blog to News in TREC 2010 Blog Track

_Yu-Fan Lin, Jing-Hau Wang, Liang-Cheng Lai, Hung-Yu Kao_

- :fontawesome-solid-user-group: **Participant:** [ikm100](./participants.md#ikm100)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/national.cheng.kung.univ.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/national.cheng.kung.univ.blog.rev.pdf)
- :material-file-search: **Runs:** [ikm100bindog](./runs.md#ikm100bindog) | [ikm100ufan](./runs.md#ikm100ufan) | [ikm100jing](./runs.md#ikm100jing) | [run1](./runs.md#run1) | [run2](./runs.md#run2) | [run3](./runs.md#run3)

??? abstract "Abstract"
	
	In 2010 Blog Track, there are two tasks including Faceted Blog Distillation Task and Top Stories Identification Task. We mainly focus on the Top Stories Identification Task. In this task, there are two issues to solve. The first issue is ranking the important news stories on the specified day, named Story Ranking Task. The second issue is named News Blog Post Ranking Task. News Blog Post Ranking Task is ranking the blog posts that are relevant to the news story and diversifying the topics of blog posts. In Story Ranking Task, our team Ikm100 (NCKU_CSIE_IKMLAB) submitted three runs. In the first run, a news story is scored by its number of discussion posts. In the second run, our idea is that if the news story is discussed by more people and the supporting blog post is relatively important, the news story would be more important. In the last run, we use the “Relevant-Post Time-Entropy evaluation” to score the news story. In News Blog Post Ranking Task, we use the cosine similarity between the news story and the blog post, and also use importance of posts to extract the supporting blog posts of the news query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinWLK10.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinWLK10,
		author = {Yu{-}Fan Lin and Jing{-}Hau Wang and Liang{-}Cheng Lai and Hung{-}Yu Kao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Top Stories Identification From Blog to News in {TREC} 2010 Blog Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/national.cheng.kung.univ.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinWLK10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Strathclyde at Headline Ranking TREC BLOG 2010

_Dmitri Roussinov_

- :fontawesome-solid-user-group: **Participant:** [UoS](./participants.md#uos)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.strathclyde.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.strathclyde.blog.rev.pdf)
- :material-file-search: **Runs:** [strath2](./runs.md#strath2) | [strath1](./runs.md#strath1) | [strath3](./runs.md#strath3)

??? abstract "Abstract"
	
	The University of Strathclyde participated in TREC BLOG Headline Ranking task only. Our general theme was to explore how the lexical changes in the BLOG corpus can reflect the importance of the articles appearing in the news corpus. Three (3) runs were submitted. For automated run 'strath1', our algorithm identified the word unigrams, the frequencies of mentioning of which in the blog corpus increased substantially on the day of the query. Up to 100 such words were used as a query to return and rank the headlines using the Terrier platform and its PL2 model. Automated run “strath3” was similar to “strath1” except the weights were estimated based on the amount of the increase in the frequency of use and applied to the query words. “Strath2” was a manual run. Event descriptions were taken from the 'Current Event' articles of Wikipedia Portal on the day of each topic (e.g. 22 January 2008 for the first topic). The description of each event was sent to Bing search engine. The words that occurred more frequently within the snippets than on the Web in average, were used to query the headlines corpus. Our participation was in close collaboration with the University of Glasgow group, which provided 1) the index to the news corpus 2) the daily statistics on the lexicons of the blog corpus and 3) the classification of the headlines into the required set of categories.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Roussinov10.bib) "
	```
	@inproceedings{DBLP:conf/trec/Roussinov10,
		author = {Dmitri Roussinov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Strathclyde at Headline Ranking {TREC} {BLOG} 2010},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.strathclyde.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Roussinov10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2010: Experiments with Terrier in  Blog and Web Tracks

_Rodrygo L. T. Santos, Richard McCreadie, Craig Macdonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.glasgow.blog.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.glasgow.blog.web.rev.pdf)
- :material-file-search: **Runs:** [uogTrapeMN5k](./runs.md#uogtrapemn5k) | [uogTrLv450](./runs.md#uogtrlv450) | [uogTrfL728](./runs.md#uogtrfl728) | [uogTrfL728s1](./runs.md#uogtrfl728s1) | [uogTrfL728s2](./runs.md#uogtrfl728s2) | [uogTrfL728s3](./runs.md#uogtrfl728s3) | [uogTrfL919](./runs.md#uogtrfl919) | [uogTrfL919s1](./runs.md#uogtrfl919s1) | [uogTrfL919s2](./runs.md#uogtrfl919s2) | [uogTrfL919s3](./runs.md#uogtrfl919s3) | [uogTrfC728](./runs.md#uogtrfc728) | [uogTrfC728s1](./runs.md#uogtrfc728s1) | [uogTrfC728s2](./runs.md#uogtrfc728s2) | [uogTrfC728s3](./runs.md#uogtrfc728s3) | [uogTrfC919](./runs.md#uogtrfc919) | [uogTrfC919s1](./runs.md#uogtrfc919s1) | [uogTrfC919s3](./runs.md#uogtrfc919s3) | [uogTrfC919s2](./runs.md#uogtrfc919s2) | [uogTrCh](./runs.md#uogtrch) | [uogTrLV1076](./runs.md#uogtrlv1076) | [uogTrLC151](./runs.md#uogtrlc151) | [uogTrL81](./runs.md#uogtrl81) | [uogTrdxE](./runs.md#uogtrdxe) | [uogTrdxF](./runs.md#uogtrdxf)

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

#### HIT_LTRC at TREC 2010 Blog Track: Faceted Blog Distillation

_Jinfeng Yang, Xishuang Dong, Yi Guan, Chengzhen Huang, Sheng Wang_

- :fontawesome-solid-user-group: **Participant:** [HIT_LTRC](./participants.md#hit_ltrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/harbin.inst.tech.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/harbin.inst.tech.blog.rev.pdf)
- :material-file-search: **Runs:** [hitQuerybl](./runs.md#hitquerybl) | [hitTDNbl](./runs.md#hittdnbl) | [hitFeeds1](./runs.md#hitfeeds1) | [hitTDNfeedbl](./runs.md#hittdnfeedbl) | [hitQFeedbl](./runs.md#hitqfeedbl) | [hitFeeds2](./runs.md#hitfeeds2) | [hitFeeds3](./runs.md#hitfeeds3) | [hitQFeedR](./runs.md#hitqfeedr) | [hitTDNfeedR](./runs.md#hittdnfeedr)

??? abstract "Abstract"
	
	This paper describes our participation in the faceted blog distillation task at Blog Track 2010. In our approach, indri toolkit is applied for basic topic relevance retrieval. Then the Maximum Entropy (ME) model is adopted to judge the relevance of each blog to specified facet. Feed faceted relevance is calculated by integrating the average relevance of all blogs within a feed and the average relevance of the most relevant N blogs. Two implementations are applied to calculate feed faceted relevance. Experimental results on Blogs08 dataset show the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangDGHW10.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangDGHW10,
		author = {Jinfeng Yang and Xishuang Dong and Yi Guan and Chengzhen Huang and Sheng Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {HIT{\_}LTRC at {TREC} 2010 Blog Track: Faceted Blog Distillation},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/harbin.inst.tech.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangDGHW10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Reconstruct Logical Hierarchical Sitemap for Related Entity Finding

_Qing Yang, Peng Jiang, Chunxia Zhang, Zhendong Niu_

- :fontawesome-solid-user-group: **Participant:** [BIT](./participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.entity.rev.pdf)
- :material-file-search: **Runs:** [BITblog10bl1](./runs.md#bitblog10bl1) | [BITblog10bl2](./runs.md#bitblog10bl2) | [BIT10std1fd1](./runs.md#bit10std1fd1) | [BIT10bl1fd1](./runs.md#bit10bl1fd1) | [BIT10bl1fd2](./runs.md#bit10bl1fd2) | [BIT10std1fd2](./runs.md#bit10std1fd2) | [BIT10std1fd4](./runs.md#bit10std1fd4) | [BIT10bl1fd3](./runs.md#bit10bl1fd3) | [BIT10bl1fd4](./runs.md#bit10bl1fd4) | [BIT10bl2fd3](./runs.md#bit10bl2fd3) | [BIT10bl2fd4](./runs.md#bit10bl2fd4) | [BIT10std1fd3](./runs.md#bit10std1fd3) | [BIT10bl2fd1](./runs.md#bit10bl2fd1) | [BIT10bl2fd2](./runs.md#bit10bl2fd2) | [BIT10std2fd1](./runs.md#bit10std2fd1) | [BIT10std3fd1](./runs.md#bit10std3fd1)

??? abstract "Abstract"
	
	This Paper presents the work done for the TREC 2010 entity track. We concentrate on constructing enriched anchor text model by exploiting hierarchical information presented in web pages to retrieve promising pages, and heuristic rules to extract potential candidate entities by zooming in the right section.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangJZN10.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangJZN10,
		author = {Qing Yang and Peng Jiang and Chunxia Zhang and Zhendong Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Reconstruct Logical Hierarchical Sitemap for Related Entity Finding},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.entity.rev.pdf},
		timestamp = {Fri, 04 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangJZN10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at TREC 2010 Blog Track: Faceted Blog Distillation Task

_Zhixin Zhou, Xiuzhen Zhang, Phil Vines_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/rmit.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/rmit.blog.rev.pdf)
- :material-file-search: **Runs:** [rmit2step](./runs.md#rmit2step) | [rmitprob](./runs.md#rmitprob) | [rmitfaceted](./runs.md#rmitfaceted)

??? abstract "Abstract"
	
	This paper reports RMIT's participation in the TREC Blog Track 2010. For the baseline task, we adopted the BM25 model implemented in the Zettair search engine to establish a retrieval system of blog posts based on topic relevance. We then experimented with a number of different approaches to aggregate the post similarity scores to retrieve the most relevant blogs. Similarly, for the faceted distillation task we built a system at the post level first. After that, scores are aggregated for blogs to re-rank the most relevant blogs for the facet inclinations. A SVM classifier has been trained on Blog 06 collection to produce the opinion scores for each post. The cross entropy is used to evaluate posts for the in-depth versus shallow facet. For the personal versus official facet, we assumed blogs which are opinionated are also personal.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouZV10.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouZV10,
		author = {Zhixin Zhou and Xiuzhen Zhang and Phil Vines},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} at {TREC} 2010 Blog Track: Faceted Blog Distillation Task},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/rmit.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouZV10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

