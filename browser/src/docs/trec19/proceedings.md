# Proceedings 2010 

## Blog 

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./blog/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.BLOG2.new.pdf](http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.BLOG2.new.pdf)
- :material-file-search: **Runs:** [ICTNETBDRun1](./blog/runs.md#ictnetbdrun1) | [ICTNETBDRun2](./blog/runs.md#ictnetbdrun2) | [ICTNETFBD2](./blog/runs.md#ictnetfbd2) | [ICTNETBD2](./blog/runs.md#ictnetbd2) | [ICTNETFBD3](./blog/runs.md#ictnetfbd3) | [ICTNETBD3](./blog/runs.md#ictnetbd3) | [ICTNETFBD4](./blog/runs.md#ictnetfbd4) | [ICTNETBD4](./blog/runs.md#ictnetbd4) | [ICTNETBD1](./blog/runs.md#ictnetbd1) | [ICTNETFBD1](./blog/runs.md#ictnetfbd1) | [ICTNETFBDs2](./blog/runs.md#ictnetfbds2) | [ICTNETFBDs3](./blog/runs.md#ictnetfbds3) | [ICTNETTSRun1](./blog/runs.md#ictnettsrun1) | [ICTNETTSRun3](./blog/runs.md#ictnettsrun3) | [ICTNETTSRun2](./blog/runs.md#ictnettsrun2) | [ICTNETPRRun1](./blog/runs.md#ictnetprrun1) | [ICTNETPRRun2](./blog/runs.md#ictnetprrun2) | [ICTNETPRRun3](./blog/runs.md#ictnetprrun3)

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

- :fontawesome-solid-user-group: **Participant:** [feup](./blog/participants.md#feup)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/labs-sapo-up.blog.pdf](http://trec.nist.gov/pubs/trec19/papers/labs-sapo-up.blog.pdf)
- :material-file-search: **Runs:** [FEUPirlab1](./blog/runs.md#feupirlab1) | [FEUPirlab2](./blog/runs.md#feupirlab2)

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

- :fontawesome-solid-user-group: **Participant:** [PKUTM](./blog/participants.md#pkutm)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/peking.univ.rev.BLOG.pdf](http://trec.nist.gov/pubs/trec19/papers/peking.univ.rev.BLOG.pdf)
- :material-file-search: **Runs:** [PKUTMB1](./blog/runs.md#pkutmb1) | [PKUTMB2](./blog/runs.md#pkutmb2) | [PKUTM111onB1](./blog/runs.md#pkutm111onb1) | [PKUTM121onB1](./blog/runs.md#pkutm121onb1) | [PKUTM211onB1](./blog/runs.md#pkutm211onb1) | [PKUTM321onB1](./blog/runs.md#pkutm321onb1) | [PKUTM111onB2](./blog/runs.md#pkutm111onb2) | [PKUTM211onB2](./blog/runs.md#pkutm211onb2) | [PKUTM221onB2](./blog/runs.md#pkutm221onb2) | [PKUTM321onB2](./blog/runs.md#pkutm321onb2) | [PKUTM111STD1](./blog/runs.md#pkutm111std1) | [PKUTM123STD1](./blog/runs.md#pkutm123std1) | [PKUTM211STD1](./blog/runs.md#pkutm211std1) | [PKUTM222STD1](./blog/runs.md#pkutm222std1) | [PKUTM111STD2](./blog/runs.md#pkutm111std2) | [PKUTM121STD2](./blog/runs.md#pkutm121std2) | [PKUTM221STD2](./blog/runs.md#pkutm221std2) | [PKUTM211STD2](./blog/runs.md#pkutm211std2) | [PKUTM111STD3](./blog/runs.md#pkutm111std3) | [PKUTM121STD3](./blog/runs.md#pkutm121std3) | [PKUTM211STD3](./blog/runs.md#pkutm211std3) | [PKUTM221STD3](./blog/runs.md#pkutm221std3)

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

- :fontawesome-solid-user-group: **Participant:** [UICIR](./blog/participants.md#uicir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.illinois-chicago.blog.rev2.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.illinois-chicago.blog.rev2.pdf)
- :material-file-search: **Runs:** [uicfeedir2](./blog/runs.md#uicfeedir2) | [uicfeedir1](./blog/runs.md#uicfeedir1) | [uicfbdrun2](./blog/runs.md#uicfbdrun2) | [uicfbdstd1a](./blog/runs.md#uicfbdstd1a) | [uicfbdstd2a](./blog/runs.md#uicfbdstd2a) | [uicfbdstd3a](./blog/runs.md#uicfbdstd3a) | [uicfbdstd1b](./blog/runs.md#uicfbdstd1b) | [uicfbdstd2b](./blog/runs.md#uicfbdstd2b) | [uicfbdstd3b](./blog/runs.md#uicfbdstd3b) | [uicfbdstd1c](./blog/runs.md#uicfbdstd1c)

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

- :fontawesome-solid-user-group: **Participant:** [BIT](./blog/participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.REV.pdf](http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.REV.pdf)
- :material-file-search: **Runs:** [BITblog10bl1](./blog/runs.md#bitblog10bl1) | [BITblog10bl2](./blog/runs.md#bitblog10bl2) | [BIT10std1fd1](./blog/runs.md#bit10std1fd1) | [BIT10bl1fd1](./blog/runs.md#bit10bl1fd1) | [BIT10bl1fd2](./blog/runs.md#bit10bl1fd2) | [BIT10std1fd2](./blog/runs.md#bit10std1fd2) | [BIT10std1fd4](./blog/runs.md#bit10std1fd4) | [BIT10bl1fd3](./blog/runs.md#bit10bl1fd3) | [BIT10bl1fd4](./blog/runs.md#bit10bl1fd4) | [BIT10bl2fd3](./blog/runs.md#bit10bl2fd3) | [BIT10bl2fd4](./blog/runs.md#bit10bl2fd4) | [BIT10std1fd3](./blog/runs.md#bit10std1fd3) | [BIT10bl2fd1](./blog/runs.md#bit10bl2fd1) | [BIT10bl2fd2](./blog/runs.md#bit10bl2fd2) | [BIT10std2fd1](./blog/runs.md#bit10std2fd1) | [BIT10std3fd1](./blog/runs.md#bit10std3fd1)

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

- :fontawesome-solid-user-group: **Participant:** [ULugano](./blog/participants.md#ulugano)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.lugano.blog.session.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.lugano.blog.session.pdf)
- :material-file-search: **Runs:** [bloggerModel](./blog/runs.md#bloggermodel) | [LexMIRuns1](./blog/runs.md#lexmiruns1) | [LexMIRuns2](./blog/runs.md#lexmiruns2) | [LexMIRuns3](./blog/runs.md#lexmiruns3) | [MILexRuns1](./blog/runs.md#milexruns1) | [MILexRuns2](./blog/runs.md#milexruns2) | [MILexRuns3](./blog/runs.md#milexruns3) | [ComSumScores](./blog/runs.md#comsumscores) | [CombMNZ](./blog/runs.md#combmnz) | [OWAScores](./blog/runs.md#owascores)

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

- :fontawesome-solid-user-group: **Participant:** [POSTECH_KLE](./blog/participants.md#postech_kle)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/pohang.univ.s-t.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/pohang.univ.s-t.blog.rev.pdf)
- :material-file-search: **Runs:** [KLERUN1](./blog/runs.md#klerun1) | [KLERUN2](./blog/runs.md#klerun2) | [KLERUN3](./blog/runs.md#klerun3) | [KLE1](./blog/runs.md#kle1) | [KLE2](./blog/runs.md#kle2)

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

- :fontawesome-solid-user-group: **Participant:** [PRIS](./blog/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/beijing.univ.p-t.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/beijing.univ.p-t.blog.rev.pdf)
- :material-file-search: **Runs:** [prisb](./blog/runs.md#prisb) | [pris](./blog/runs.md#pris) | [PrisStdQ0](./blog/runs.md#prisstdq0) | [PrisStdQ02](./blog/runs.md#prisstdq02) | [PrisStdQ03](./blog/runs.md#prisstdq03) | [PrisStdQ04](./blog/runs.md#prisstdq04) | [PrisStdQE1](./blog/runs.md#prisstdqe1) | [PrisStdQE2](./blog/runs.md#prisstdqe2) | [PrisStdQE3](./blog/runs.md#prisstdqe3) | [PrisQ01](./blog/runs.md#prisq01) | [PrisQ02](./blog/runs.md#prisq02) | [PrisQ03](./blog/runs.md#prisq03) | [PrisQ04](./blog/runs.md#prisq04) | [PrisQE1](./blog/runs.md#prisqe1) | [PrisQE2](./blog/runs.md#prisqe2)

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

- :fontawesome-solid-user-group: **Participant:** [ikm100](./blog/participants.md#ikm100)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/national.cheng.kung.univ.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/national.cheng.kung.univ.blog.rev.pdf)
- :material-file-search: **Runs:** [ikm100bindog](./blog/runs.md#ikm100bindog) | [ikm100ufan](./blog/runs.md#ikm100ufan) | [ikm100jing](./blog/runs.md#ikm100jing) | [run1](./blog/runs.md#run1) | [run2](./blog/runs.md#run2) | [run3](./blog/runs.md#run3)

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

- :fontawesome-solid-user-group: **Participant:** [UoS](./blog/participants.md#uos)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.strathclyde.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.strathclyde.blog.rev.pdf)
- :material-file-search: **Runs:** [strath2](./blog/runs.md#strath2) | [strath1](./blog/runs.md#strath1) | [strath3](./blog/runs.md#strath3)

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

- :fontawesome-solid-user-group: **Participant:** [uogTr](./blog/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.glasgow.blog.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.glasgow.blog.web.rev.pdf)
- :material-file-search: **Runs:** [uogTrapeMN5k](./blog/runs.md#uogtrapemn5k) | [uogTrLv450](./blog/runs.md#uogtrlv450) | [uogTrfL728](./blog/runs.md#uogtrfl728) | [uogTrfL728s1](./blog/runs.md#uogtrfl728s1) | [uogTrfL728s2](./blog/runs.md#uogtrfl728s2) | [uogTrfL728s3](./blog/runs.md#uogtrfl728s3) | [uogTrfL919](./blog/runs.md#uogtrfl919) | [uogTrfL919s1](./blog/runs.md#uogtrfl919s1) | [uogTrfL919s2](./blog/runs.md#uogtrfl919s2) | [uogTrfL919s3](./blog/runs.md#uogtrfl919s3) | [uogTrfC728](./blog/runs.md#uogtrfc728) | [uogTrfC728s1](./blog/runs.md#uogtrfc728s1) | [uogTrfC728s2](./blog/runs.md#uogtrfc728s2) | [uogTrfC728s3](./blog/runs.md#uogtrfc728s3) | [uogTrfC919](./blog/runs.md#uogtrfc919) | [uogTrfC919s1](./blog/runs.md#uogtrfc919s1) | [uogTrfC919s3](./blog/runs.md#uogtrfc919s3) | [uogTrfC919s2](./blog/runs.md#uogtrfc919s2) | [uogTrCh](./blog/runs.md#uogtrch) | [uogTrLV1076](./blog/runs.md#uogtrlv1076) | [uogTrLC151](./blog/runs.md#uogtrlc151) | [uogTrL81](./blog/runs.md#uogtrl81) | [uogTrdxE](./blog/runs.md#uogtrdxe) | [uogTrdxF](./blog/runs.md#uogtrdxf)

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

- :fontawesome-solid-user-group: **Participant:** [HIT_LTRC](./blog/participants.md#hit_ltrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/harbin.inst.tech.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/harbin.inst.tech.blog.rev.pdf)
- :material-file-search: **Runs:** [hitQuerybl](./blog/runs.md#hitquerybl) | [hitTDNbl](./blog/runs.md#hittdnbl) | [hitFeeds1](./blog/runs.md#hitfeeds1) | [hitTDNfeedbl](./blog/runs.md#hittdnfeedbl) | [hitQFeedbl](./blog/runs.md#hitqfeedbl) | [hitFeeds2](./blog/runs.md#hitfeeds2) | [hitFeeds3](./blog/runs.md#hitfeeds3) | [hitQFeedR](./blog/runs.md#hitqfeedr) | [hitTDNfeedR](./blog/runs.md#hittdnfeedr)

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

- :fontawesome-solid-user-group: **Participant:** [BIT](./blog/participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.entity.rev.pdf)
- :material-file-search: **Runs:** [BITblog10bl1](./blog/runs.md#bitblog10bl1) | [BITblog10bl2](./blog/runs.md#bitblog10bl2) | [BIT10std1fd1](./blog/runs.md#bit10std1fd1) | [BIT10bl1fd1](./blog/runs.md#bit10bl1fd1) | [BIT10bl1fd2](./blog/runs.md#bit10bl1fd2) | [BIT10std1fd2](./blog/runs.md#bit10std1fd2) | [BIT10std1fd4](./blog/runs.md#bit10std1fd4) | [BIT10bl1fd3](./blog/runs.md#bit10bl1fd3) | [BIT10bl1fd4](./blog/runs.md#bit10bl1fd4) | [BIT10bl2fd3](./blog/runs.md#bit10bl2fd3) | [BIT10bl2fd4](./blog/runs.md#bit10bl2fd4) | [BIT10std1fd3](./blog/runs.md#bit10std1fd3) | [BIT10bl2fd1](./blog/runs.md#bit10bl2fd1) | [BIT10bl2fd2](./blog/runs.md#bit10bl2fd2) | [BIT10std2fd1](./blog/runs.md#bit10std2fd1) | [BIT10std3fd1](./blog/runs.md#bit10std3fd1)

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

- :fontawesome-solid-user-group: **Participant:** [RMIT](./blog/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/rmit.blog.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/rmit.blog.rev.pdf)
- :material-file-search: **Runs:** [rmit2step](./blog/runs.md#rmit2step) | [rmitprob](./blog/runs.md#rmitprob) | [rmitfaceted](./blog/runs.md#rmitfaceted)

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

## Web 

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

- :fontawesome-solid-user-group: **Participant:** [uottawa](./web/participants.md#uottawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.ottawa.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.ottawa.web.rev.pdf)
- :material-file-search: **Runs:** [DFalah2010](./web/runs.md#dfalah2010)

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

- :fontawesome-solid-user-group: **Participant:** [unimelb](./web/participants.md#unimelb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.melbourne.web.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.melbourne.web.pdf)
- :material-file-search: **Runs:** [UMa10BASF](./web/runs.md#uma10basf) | [UMa10BSF](./web/runs.md#uma10bsf) | [UMa10IASF](./web/runs.md#uma10iasf) | [UMd10ASF](./web/runs.md#umd10asf) | [UMd10BASF](./web/runs.md#umd10basf) | [UMd10IASF](./web/runs.md#umd10iasf)

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

- :fontawesome-solid-user-group: **Participant:** [umass](./web/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.mass.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.mass.web.rev.pdf)
- :material-file-search: **Runs:** [umassSDMW](./web/runs.md#umasssdmw) | [umasswfb520](./web/runs.md#umasswfb520) | [umassSDM](./web/runs.md#umasssdm)

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

- :fontawesome-solid-user-group: **Participant:** [blv1979](./web/participants.md#blv1979)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/blv-1979.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/blv-1979.web.rev.pdf)
- :material-file-search: **Runs:** [blv79y00shnk](./web/runs.md#blv79y00shnk) | [blv79y00prob](./web/runs.md#blv79y00prob)

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

- :fontawesome-solid-user-group: **Participant:** [MMCI](./web/participants.md#mmci)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/saarland.univ.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/saarland.univ.web.rev.pdf)
- :material-file-search: **Runs:** [MMCITLl20M](./web/runs.md#mmcitll20m) | [MMCIl410m1](./web/runs.md#mmcil410m1) | [MMCITLCLl20M](./web/runs.md#mmcitlcll20m)

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./web/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.ADHOC.new.pdf](http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.ADHOC.new.pdf)
- :material-file-search: **Runs:** [ICTNETAD10R1](./web/runs.md#ictnetad10r1) | [ICTNETAD10R2](./web/runs.md#ictnetad10r2) | [ICTNETAD10R3](./web/runs.md#ictnetad10r3) | [ICTNETDV10R1](./web/runs.md#ictnetdv10r1) | [ICTNETDV10R2](./web/runs.md#ictnetdv10r2) | [ICTNETSP10R1](./web/runs.md#ictnetsp10r1) | [ICTNETDV10R3](./web/runs.md#ictnetdv10r3)

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

- :fontawesome-solid-user-group: **Participant:** [msrsv](./web/participants.md#msrsv)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/microsoft-msrsv.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/microsoft-msrsv.web.rev.pdf)
- :material-file-search: **Runs:** [msrsv1](./web/runs.md#msrsv1) | [msrsv1div](./web/runs.md#msrsv1div) | [msrsv2](./web/runs.md#msrsv2) | [msrsv2div](./web/runs.md#msrsv2div) | [msrsv3](./web/runs.md#msrsv3) | [msrsv3div](./web/runs.md#msrsv3div)

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

- :fontawesome-solid-user-group: **Participant:** [IRRA](./web/participants.md#irra)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/mugla.univ.web.pdf](http://trec.nist.gov/pubs/trec19/papers/mugla.univ.web.pdf)
- :material-file-search: **Runs:** [irra10b](./web/runs.md#irra10b) | [irra10hp](./web/runs.md#irra10hp) | [irra10rob](./web/runs.md#irra10rob)

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

- :fontawesome-solid-user-group: **Participant:** [UMD](./web/participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.maryland-usc-isi.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.maryland-usc-isi.web.rev.pdf)
- :material-file-search: **Runs:** [IvoryWSDa](./web/runs.md#ivorywsda) | [IvorySDa](./web/runs.md#ivorysda) | [IvoryBM25a](./web/runs.md#ivorybm25a) | [IVORY.70.30](./web/runs.md#ivory.70.30) | [IVORY.90.10](./web/runs.md#ivory.90.10)

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

- :fontawesome-solid-user-group: **Participant:** [utwente](./web/participants.md#utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.twente.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.twente.web.rev.pdf)
- :material-file-search: **Runs:** [utwente4](./web/runs.md#utwente4) | [utwente3](./web/runs.md#utwente3) | [utwente4SF](./web/runs.md#utwente4sf)

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

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./web/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam-kamps.web.ent.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam-kamps.web.ent.rev.pdf)
- :material-file-search: **Runs:** [UAMSA10d2a8](./web/runs.md#uamsa10d2a8) | [UAMSD10ancB](./web/runs.md#uamsd10ancb) | [UAMSA10mSF30](./web/runs.md#uamsa10msf30) | [UAMSA10mSFPR](./web/runs.md#uamsa10msfpr) | [UAMSD10ancPR](./web/runs.md#uamsd10ancpr) | [UAMSD10aSRfu](./web/runs.md#uamsd10asrfu)

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

- :fontawesome-solid-user-group: **Participant:** [UCDSIFT](./web/participants.md#ucdsift)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.college.dublin.web.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.college.dublin.web.pdf)
- :material-file-search: **Runs:** [UCDSIFTSlide](./web/runs.md#ucdsiftslide) | [UCDSIFTProb](./web/runs.md#ucdsiftprob) | [UCDSIFTMAP](./web/runs.md#ucdsiftmap) | [UCDSIFTDiv](./web/runs.md#ucdsiftdiv)

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

- :fontawesome-solid-user-group: **Participant:** [CMU_LIRA](./web/participants.md#cmu_lira)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/carnegie-mellon-univ-lira.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/carnegie-mellon-univ-lira.web.rev.pdf)
- :material-file-search: **Runs:** [cmuBase10](./web/runs.md#cmubase10) | [cmuWiki10](./web/runs.md#cmuwiki10) | [cmuFuTop10](./web/runs.md#cmufutop10) | [cmuWi10D](./web/runs.md#cmuwi10d) | [cmuFuTop10D](./web/runs.md#cmufutop10d) | [cmuComb10](./web/runs.md#cmucomb10)

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

- :fontawesome-solid-user-group: **Participant:** [uogTr](./web/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.glasgow.blog.web.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.glasgow.blog.web.rev.pdf)
- :material-file-search: **Runs:** [uogTrB67](./web/runs.md#uogtrb67) | [uogTrB67LTS](./web/runs.md#uogtrb67lts) | [uogTrA42](./web/runs.md#uogtra42) | [uogTrB67xS](./web/runs.md#uogtrb67xs) | [uogTrBdphxS](./web/runs.md#uogtrbdphxs) | [uogTrA40n](./web/runs.md#uogtra40n) | [uogTrA42x](./web/runs.md#uogtra42x)

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./web/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.DIVERSITY.new.pdf](http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.DIVERSITY.new.pdf)
- :material-file-search: **Runs:** [ICTNETAD10R1](./web/runs.md#ictnetad10r1) | [ICTNETAD10R2](./web/runs.md#ictnetad10r2) | [ICTNETAD10R3](./web/runs.md#ictnetad10r3) | [ICTNETDV10R1](./web/runs.md#ictnetdv10r1) | [ICTNETDV10R2](./web/runs.md#ictnetdv10r2) | [ICTNETSP10R1](./web/runs.md#ictnetsp10r1) | [ICTNETDV10R3](./web/runs.md#ictnetdv10r3)

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

- :fontawesome-solid-user-group: **Participant:** [Udel_Fang](./web/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.delaware-fang.web.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.delaware-fang.web.pdf)
- :material-file-search: **Runs:** [UDWebSQR](./web/runs.md#udwebsqr) | [UDWebPCOV](./web/runs.md#udwebpcov) | [UDWebLOG](./web/runs.md#udweblog)

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./web/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.SPAM.new.pdf](http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.SPAM.new.pdf)
- :material-file-search: **Runs:** [ICTNETAD10R1](./web/runs.md#ictnetad10r1) | [ICTNETAD10R2](./web/runs.md#ictnetad10r2) | [ICTNETAD10R3](./web/runs.md#ictnetad10r3) | [ICTNETDV10R1](./web/runs.md#ictnetdv10r1) | [ICTNETDV10R2](./web/runs.md#ictnetdv10r2) | [ICTNETSP10R1](./web/runs.md#ictnetsp10r1) | [ICTNETDV10R3](./web/runs.md#ictnetdv10r3)

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

## Chemical 

#### TREC-CHEM 2010

_Mihai Lupu, John Tait, Jimmy X. Huang, Jianhan Zhu_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec19/papers/CHEM.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec19/papers/CHEM.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Chemical IR Track is a domain-specific evaluation campaign working with documents containing specific lexica, including chemical formulas and specific names. The 2010 edition of the track also included supporting material in addition to text: images and structure information files. As in the previous year, we had two tasks: a patent focused prior-art (PA) task and a user-focused Technology Survey task (TS). The data collection includes patent files as well as scientific articles, together with their attachments, if any. Topics and relevance judgments were either automatically or manually created.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LupuTHZ10.bib) "
	```
	@inproceedings{DBLP:conf/trec/LupuTHZ10,
		author = {Mihai Lupu and John Tait and Jimmy X. Huang and Jianhan Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC-CHEM} 2010},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {https://trec.nist.gov/pubs/trec19/papers/CHEM.OVERVIEW.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LupuTHZ10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BiTeM site Report for TREC Chemistry 2010: Impact of Citations Feeback  for Patent Prior Art Search and Chemical Compounds Expansion for Ad  Hoc Retrieval

_Julien Gobeill, Arnaud Gaudinat, Patrick Ruch, Emilie Pasche, Douglas Teodoro, Dina Vishnyakova_

- :fontawesome-solid-user-group: **Participant:** [BiTeM](./chemical/participants.md#bitem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.geneva.chem.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.geneva.chem.rev.pdf)
- :material-file-search: **Runs:** [BiTeM09TSbl](./chemical/runs.md#bitem09tsbl) | [BiTeM09TSsqe](./chemical/runs.md#bitem09tssqe) | [BiTeM09TSmqe](./chemical/runs.md#bitem09tsmqe) | [BiTeM09TSlqe](./chemical/runs.md#bitem09tslqe) | [BiTeM10PAx](./chemical/runs.md#bitem10pax) | [BiTeM10PAsmx](./chemical/runs.md#bitem10pasmx)

??? abstract "Abstract"
	
	For two years, the TREC Chemical Track aims at evaluating participant systems in chemical patent searching. In 2010, it continued with the two tasks from 2009: Prior Art search (PA) and Technology Survey (TS). The BiTeM group participated in both tasks and obtained satisfactory results, relying on a large panel of strategies which were evaluated within the framework of past similar competitions. There are three main conclusions that we draw from this campaign. First of all, regarding a baseline computed by Information Retrieval (IR) only, simplest models achieved the best results for both tasks, such as indexing only titles, abstracts, and claims, and no stemming; however, for the PA task, the performance of this baseline remains low (Mean Average Precision 0.043) compared to last year (MAP 0.067). Further analysis of the query set reveals that description sections were in 2010 twice longer than in 2009, while citations number was stable; having longer queries obviously resulted in a degradation of the signal-to-noise ratio, and in a more complex task for standard IR. Secondly, IPC codes were of no use for the PA task, and even decreased performances, whether they were injected in the index or used for filtering the results. Because this strategy is effective when applied to EPO patents in general domain, further experiments or expertise need to determine if it fails because it is applied to a specific domain, or because the quality of IPC annotations in USPTO patents is insufficient. The last conclusion deals with our re-ranking strategy based on citations feedback for the PA task. Such a strategy led to a dramatic improvement from 0.043 to 0.261 for MAP (+ 507%), and from 0.31 to 0.62 for Recall at 500 (+ 100%). Further analysis shows that our citations feedback strategy achieves to strongly capture the chemical applicants' behaviour, which tends to cite regular patterns of multiple patents massively inter-connected with direct citations. Results of the TS task prove the effectiveness of synonyms expansion driven by chemical entities normalization.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GobeillGRPTV10.bib) "
	```
	@inproceedings{DBLP:conf/trec/GobeillGRPTV10,
		author = {Julien Gobeill and Arnaud Gaudinat and Patrick Ruch and Emilie Pasche and Douglas Teodoro and Dina Vishnyakova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BiTeM site Report for {TREC} Chemistry 2010: Impact of Citations Feeback for Patent Prior Art Search and Chemical Compounds Expansion for Ad Hoc Retrieval},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.geneva.chem.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GobeillGRPTV10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Prior Art Search in Chemistry Patents Based On Semantic Concepts and  Co-Citation Analysis

_Harsha Gurulingappa, Bernd Müller, Roman Klinger, Heinz-Theodor Mevissen, Martin Hofmann-Apitius, Christoph M. Friedrich, Juliane Fluck_

- :fontawesome-solid-user-group: **Participant:** [Fraunhofer.SCAI](./chemical/participants.md#fraunhofer.scai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/fraunhofer-scai.chem.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/fraunhofer-scai.chem.rev.pdf)
- :material-file-search: **Runs:** [SCAI10CIENTP](./chemical/runs.md#scai10cientp) | [SCAI10CITENT](./chemical/runs.md#scai10citent) | [SCAI10CITNP](./chemical/runs.md#scai10citnp) | [SCAI10CITTOK](./chemical/runs.md#scai10cittok) | [SCAI10NRMENT](./chemical/runs.md#scai10nrment) | [SCAI10NRMNP](./chemical/runs.md#scai10nrmnp) | [SCAI10NRMTOK](./chemical/runs.md#scai10nrmtok)

??? abstract "Abstract"
	
	Prior Art Search is a task of querying and retrieving the patents in order to uncover any knowledge existing prior to the inventor's question or invention at hand. For addressing this task, we present a contemporary approach that has been evaluated during Trecchem for its ability to adapt to text containing chemistry-based information. The core of the framework is an index of 1.3 million chemistry patents provided as a data set by Trecchem. For the prior art search task, the information of normalized noun phrases, biomedical and chemical entities are added to the full text index. Altogether, 7 runs were submitted for this task that were based on automatic querying with tokens, noun phrases and entities. In addition, the co-citation information was exploited in a systematic way to generate ranked citation sets from the retrieved documents. Querying with noun phrases and entities coupled with co-citation based post-processing performed considerably well with the best MAP score of 0.23.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GurulingappaMKMHFF10.bib) "
	```
	@inproceedings{DBLP:conf/trec/GurulingappaMKMHFF10,
		author = {Harsha Gurulingappa and Bernd M{\"{u}}ller and Roman Klinger and Heinz{-}Theodor Mevissen and Martin Hofmann{-}Apitius and Christoph M. Friedrich and Juliane Fluck},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Prior Art Search in Chemistry Patents Based On Semantic Concepts and Co-Citation Analysis},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/fraunhofer-scai.chem.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GurulingappaMKMHFF10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Relevance Feedback 

#### Mining Specific and General Features in Both Positive and Negative  Relevance Feedback: QUT E-Discovery Lab at the TREC 2010 Relevance  Feedback Track

_Abdulmohsen Algarni, Yuefeng Li, Xiaohui Tao_

- :fontawesome-solid-user-group: **Participant:** [QUT_eDisco](./relfdbk/participants.md#qut_edisco)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/queensland.univ.tech.RF.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/queensland.univ.tech.RF.rev.pdf)
- :material-file-search: **Runs:** [qut10rf.10-1](./relfdbk/runs.md#qut10rf.10-1) | [qut10rf.10-2](./relfdbk/runs.md#qut10rf.10-2) | [qut10rf.10-3](./relfdbk/runs.md#qut10rf.10-3) | [qut10rf.10-4](./relfdbk/runs.md#qut10rf.10-4) | [qut10rf.10-5](./relfdbk/runs.md#qut10rf.10-5) | [qut10rf.10-1.2](./relfdbk/runs.md#qut10rf.10-1.2) | [qut10rf.10-2.2](./relfdbk/runs.md#qut10rf.10-2.2) | [qut10rf.10-3.2](./relfdbk/runs.md#qut10rf.10-3.2) | [qut10rf.10-5.2](./relfdbk/runs.md#qut10rf.10-5.2) | [qut10rf.10-4.2](./relfdbk/runs.md#qut10rf.10-4.2) | [qut10rf.B](./relfdbk/runs.md#qut10rf.b)

??? abstract "Abstract"
	
	User relevance feedback is usually utilized by Web systems to interpret user information needs and retrieve effective results for users. However, how to discover useful knowledge in user relevance feedback and how to wisely use the discovered knowledge are two critical problems. However, understanding what makes an individual document good or bad for feedback can lead to the solution of the previous problem. In TREC 2010, we participated in the Relevance Feedback Track and experimented two models for extracting pseudo-relevance feedback to improve the ranking of retrieved documents. The first one, the main run, was a pattern-based model, whereas the second one, the optional run, was a term-based model. The two models consisted of two stages: one using relevance feedback provided by TREC'10 to expand queries to extract pseudo-relevance feedback; one using pseudo-relevance feedback to find useful patterns and terms according to their relevance and irrelevance judgements to rank documents. In this paper, the detailed description of those models is presented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlgarniLT10.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlgarniLT10,
		author = {Abdulmohsen Algarni and Yuefeng Li and Xiaohui Tao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Mining Specific and General Features in Both Positive and Negative Relevance Feedback: {QUT} E-Discovery Lab at the {TREC} 2010 Relevance Feedback Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/queensland.univ.tech.RF.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlgarniLT10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2010: Session, Entity and Relevance  Feedback

_Marc Bron, Jiyin He, Katja Hofmann, Edgar Meij, Maarten de Rijke, Manos Tsagkias, Wouter Weerkamp_

- :fontawesome-solid-user-group: **Participant:** [UAms](./relfdbk/participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf)
- :material-file-search: **Runs:** [UAmsRF.B](./relfdbk/runs.md#uamsrf.b) | [UAmsRF.10-1](./relfdbk/runs.md#uamsrf.10-1) | [UAmsRF.10-2](./relfdbk/runs.md#uamsrf.10-2) | [UAmsRF.10-3](./relfdbk/runs.md#uamsrf.10-3) | [UAmsRF.10-4](./relfdbk/runs.md#uamsrf.10-4) | [UAmsRF.10-5](./relfdbk/runs.md#uamsrf.10-5)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the session, entity, and relevance feedback track at TREC 2010. In the Session Track we explore the use of blind relevance feedback to bias a follow-up query towards or against the topics covered in documents returned to the user in response to the original query. In the Entity Track REF task we experiment with a window size parameter to limit the amount of context considered by the entity co-occurrence models and explore the use of Freebase for type filtering, entity normalization and homepage finding. In the ELC task we use an approach that uses the number of links shared between candidate and example entities to rank candidates. In the Relevance Feedback Track we experiment with a novel model that uses Wikipedia to expand the query language model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BronHHMRTW10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BronHHMRTW10,
		author = {Marc Bron and Jiyin He and Katja Hofmann and Edgar Meij and Maarten de Rijke and Manos Tsagkias and Wouter Weerkamp},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at {TREC} 2010: Session, Entity and Relevance Feedback},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BronHHMRTW10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluation of a Methodology for Modeling Term Relationship through  Geometry: Experiments at TREC 2010 Relevance Feedback Track

_Emanuele Di Buccio, Massimo Melucci, Jian-Yun Nie_

- :fontawesome-solid-user-group: **Participant:** [UPD](./relfdbk/participants.md#upd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.padua.RF.rev2.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.padua.RF.rev2.pdf)
- :material-file-search: **Runs:** [UPD10rf.B](./relfdbk/runs.md#upd10rf.b) | [UPD10rf.10-1](./relfdbk/runs.md#upd10rf.10-1) | [UPD10rf.10-2](./relfdbk/runs.md#upd10rf.10-2) | [UPD10rf.10-3](./relfdbk/runs.md#upd10rf.10-3) | [UPD10rf.10-4](./relfdbk/runs.md#upd10rf.10-4) | [UPD10rf.10-5](./relfdbk/runs.md#upd10rf.10-5) | [UPD10rf.10-6](./relfdbk/runs.md#upd10rf.10-6) | [UPD10rf.10-7](./relfdbk/runs.md#upd10rf.10-7) | [UPD10rf.10-8](./relfdbk/runs.md#upd10rf.10-8) | [UPD10rf.10-9](./relfdbk/runs.md#upd10rf.10-9) | [UPD10rf.10-10](./relfdbk/runs.md#upd10rf.10-10)

??? abstract "Abstract"
	
	The work reported in this paper is focused on the experimental evaluation of a methodology which models sources for feedback through a vector subspace formalism. This work considers a specific application of the methodology that exploits correlation among terms in documents judged as relevant to support feedback. Experiments were carried out during the participation to the TREC 2010 Relevance Feedback Track, thus investigating the effectiveness of the methodology application for modeling term correlation on a very large text corpus and when little evidence, namely one relevant document, is used as input for feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuccioMN10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuccioMN10,
		author = {Emanuele Di Buccio and Massimo Melucci and Jian{-}Yun Nie},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Evaluation of a Methodology for Modeling Term Relationship through Geometry: Experiments at {TREC} 2010 Relevance Feedback Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.padua.RF.rev2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuccioMN10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Legal 

#### Overview of the TREC 2010 Legal Track

_Gordon V. Cormack, Maura R. Grossman, Bruce Hedin, Douglas W. Oard_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec19/papers/LEGAL10.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec19/papers/LEGAL10.OVERVIEW.pdf)
??? abstract "Abstract"
	
	TREC 2010 was the fifth year of the Legal Track, which focuses on evaluation of search technology for discovery of electronically stored information in litigation and regulatory settings. The TREC 2010 Legal Track consisted of two distinct tasks: the Learning task, in which participants were required to estimate the probability of relevance for each document in a large collection, given a seed set of documents, each coded as responsive or non-responsive; and the Interactive task, in which participants were required to identify all relevant documents using a human-in-the-loop process.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackGHO10.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackGHO10,
		author = {Gordon V. Cormack and Maura R. Grossman and Bruce Hedin and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2010 Legal Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {https://trec.nist.gov/pubs/trec19/papers/LEGAL10.OVERVIEW.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackGHO10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Auto-Relevancy Baseline: A Hybrid System Without Human Feedback

_Cody Bennett_

- :fontawesome-solid-user-group: **Participant:** [TCDI](./legal/participants.md#tcdi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/bennett.cody.LEGAL.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/bennett.cody.LEGAL.rev.pdf)
- :material-file-search: **Runs:** [tcd1](./legal/runs.md#tcd1)

??? abstract "Abstract"
	
	On obtaining a Request for Production and automatically emulating a typical eDiscovery workflow1, a simple application of the classical Bayes algorithm upon the pseudo-hybridization of SemanticA and Latent Semantic IndexingBC systems should smooth out historically high yet noisy Recall of some LSI models and their derivatives and produce a tighter linear distribution when assessing relevant documents unsupervised.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bennett10.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bennett10,
		author = {Cody Bennett},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Auto-Relevancy Baseline: {A} Hybrid System Without Human Feedback},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/bennett.cody.LEGAL.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bennett10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IT-Discovery at TREC 2010 Legal

_Aron Culotta, Andy Liu, Mark Cordover, Bennett Borden, Sam Strickland_

- :fontawesome-solid-user-group: **Participant:** [IT.com](./legal/participants.md#it.com)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/it.com.legal.pdf](http://trec.nist.gov/pubs/trec19/papers/it.com.legal.pdf)
- :material-file-search: **Runs:** [ITCOMRUN0](./legal/runs.md#itcomrun0) | [ITD](./legal/runs.md#itd)

??? abstract "Abstract"
	
	IT-Discovery participated in both the Learning Task (Topics 201-207) and the Interactive Task (Topics 301, 303). For the Learning Task, we used an optimized Naive Bayes classifier, which obtained 90-97% cross-validation accuracy on the provided seed sets for each topic. For the Interactive Task, we used the same classifier trained with one round of active learning. The annotator averaged 36.5 hours per topic, resulting in a cross-validation classification accuracy of 90%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CulottaLCBS10.bib) "
	```
	@inproceedings{DBLP:conf/trec/CulottaLCBS10,
		author = {Aron Culotta and Andy Liu and Mark Cordover and Bennett Borden and Sam Strickland},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IT-Discovery at {TREC} 2010 Legal},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/it.com.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CulottaLCBS10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Applying Latent Semantic Indexing on the TREC 2010 Legal Dataset

_Andy Garron, April Kontostathis_

- :fontawesome-solid-user-group: **Participant:** [ursinus](./legal/participants.md#ursinus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/ursinus.college.legal.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/ursinus.college.legal.rev.pdf)
- :material-file-search: **Runs:** [URSLSIT](./legal/runs.md#urslsit) | [URSK35T](./legal/runs.md#ursk35t) | [URSK70T](./legal/runs.md#ursk70t)

??? abstract "Abstract"
	
	We applied both Latent Semantic Indexing (LSI) and Essential Dimensions of LSI (EDLSI) to the 2010 TREC Legal Learning task. This year the Enron email collection was used and teams were given a list of relevant and a list of non-relevant documents for each of the eight test queries. In this article we focus on our attempts to incorporate machine learning into the LSI process. We show the EDLSI continues to outperform LSI on large datasets. For 2011 we plan to enhance our system by adding parallel and distributed approaches to LSI and EDLSI. We believe our retrieval performance would be improved if we could process more dimensions. Our current system resources limited us to 70 dimensions this year. Even with 70 dimensions our system performance was greater than or equal to the median for 6 of the 8 queries on the F1 metric.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarronK10.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarronK10,
		author = {Andy Garron and April Kontostathis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Applying Latent Semantic Indexing on the {TREC} 2010 Legal Dataset},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/ursinus.college.legal.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GarronK10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Indian Statistical Institute, Kolkata at TREC 2010: Legal Interactive

_Kripabandhu Ghosh, Swapan K. Parui, Prasenjit Majumder, Ayan Bandyopadhyay, S. John J. Raja Singh_

- :fontawesome-solid-user-group: **Participant:** [IRISICAL](./legal/participants.md#irisical)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/indian-stat-institute.LEGAL.pdf](http://trec.nist.gov/pubs/trec19/papers/indian-stat-institute.LEGAL.pdf)
- :material-file-search: **Runs:** [IRISICAL1](./legal/runs.md#irisical1)

??? abstract "Abstract"
	
	Indian Statistical Institute, Kolkata participated in TREC for the first time this year. We participated in TREC Legal Interactive task in two topics namely, Topic 301 and Topic 302. We reduced the size of the corpus by Boolean retrieval using Lemur 4.111 and followed it by a clustering technique. We chose members from each cluster (which we called seeds) for relevance judgement by the TA and assumed all other members of the cluster whose seeds are assessed as relevant to be relevant.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GhoshPMBS10.bib) "
	```
	@inproceedings{DBLP:conf/trec/GhoshPMBS10,
		author = {Kripabandhu Ghosh and Swapan K. Parui and Prasenjit Majumder and Ayan Bandyopadhyay and S. John J. Raja Singh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Indian Statistical Institute, Kolkata at {TREC} 2010: Legal Interactive},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/indian-stat-institute.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GhoshPMBS10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Bag of Words (BOW) and Standard Deviations to Represent Expected  Structures for Document Retrieval: A Way of Thinking that Leads  to Method Choices

_Harvey S. Hyman, Warren Fridy III_

- :fontawesome-solid-user-group: **Participant:** [USF_ISDS](./legal/participants.md#usf_isds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.south.florida.rev.LEGAL.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.south.florida.rev.LEGAL.pdf)
- :material-file-search: **Runs:** [USFISDS](./legal/runs.md#usfisds)

??? abstract "Abstract"
	
	This paper discusses a theory and proposed design for a retrieval artifact using a bag of words (BOW) approach for terms and a standard deviation method for assigning weights. The paper is organized into three parts. The first part is an historical overview of the development of text mining techniques. It is intended to acquaint the reader with our perspectives and assumptions; it is not intended to be an exhaustive review of the literature. The second part discusses the application of text mining techniques to the legal domain, specifically eDiscovery. The third part describes our approach to the 2010 TREC Legal Track problem set #301. Part Three is sub-divided into three sections. Section one is a discussion of our approach to document retrieval. Section two is a description of our design approach and method specifically chosen for Problem #301. Section three discusses contributions, limitations, generalizability, and conclusions based on our experience with the initial results produced by the competing artifacts in the TREC proceeding. We include a discussion of the initial results as reported at the conference.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HymanF10.bib) "
	```
	@inproceedings{DBLP:conf/trec/HymanF10,
		author = {Harvey S. Hyman and Warren Fridy III},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Bag of Words {(BOW)} and Standard Deviations to Represent Expected Structures for Document Retrieval: {A} Way of Thinking that Leads to Method Choices},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.south.florida.rev.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HymanF10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTH Does Probabilities of Relevance at the Legal Track

_Dim P. Papadopoulos, Vicky S. Kalogeiton, Avi Arampatzis_

- :fontawesome-solid-user-group: **Participant:** [EE.DUTH.GR](./legal/participants.md#ee.duth.gr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/democritus.univ.legal.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/democritus.univ.legal.rev.pdf)
- :material-file-search: **Runs:** [DUTHsdtA](./legal/runs.md#duthsdta) | [DUTHsdeA](./legal/runs.md#duthsdea) | [DUTHlrgA](./legal/runs.md#duthlrga)

??? abstract "Abstract"
	
	We participated in the Learning Task of the TREC 2010 Legal Track, focusing solely on estimating probabilities of relevance. We submitted three automated runs based on the same tf.idf ranking, produced by the topic narratives and positive-only feedback of the training data in equal contributions. The runs differ in the way the probabilities of relevance are estimated: (1) DUTHsdtA employed the Truncated Normal-Exponential model to turn scores to probabilities. (2) DUTHsdeA did not assume any specific component score distributions but estimated those on the scores of training data via Kernel Density Estimation (KDE) methods. (3) DUTHlrgA used Logistic Regression with the co-efficients estimated on the scores of training data. We found that DUTHsdeA and DUTHlrgA are greatly affected by biases in the training set, since they assume that input score data are uniformly sampled. Also, KDE was found to be very sensitive to its parameters, influencing greatly the probability estimates. In these respects, DUTHsdtA was proven to be the most robust method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PapadopoulosKA10.bib) "
	```
	@inproceedings{DBLP:conf/trec/PapadopoulosKA10,
		author = {Dim P. Papadopoulos and Vicky S. Kalogeiton and Avi Arampatzis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTH} Does Probabilities of Relevance at the Legal Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/democritus.univ.legal.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PapadopoulosKA10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at TREC 2010: Legal Interactive

_Mark D. Smucker, Charles L. A. Clarke, Gordon V. Cormack, Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [uwaterlooclarke](./legal/participants.md#uwaterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.waterloo.LEGAL.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.waterloo.LEGAL.pdf)
- :material-file-search: **Runs:** [watlint10](./legal/runs.md#watlint10)

??? abstract "Abstract"
	
	This year the University of Waterloo (UW) participated in the TREC Legal Interactive track and used the same process as last year except that this year we used three different human operators as opposed to only one as UW did last year. We participated in three topics: 301, 302, and 303. Relative to other participants, we performed well on one of the three topics. For two of the topics, low recall significantly hurt our F1 scores. Overall, we believe a contributing factor in our lower performance this year was with our interaction with the topic authorities, which resulted in our failing to understand the wide range of what constituted relevant material.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmuckerCCV10.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmuckerCCV10,
		author = {Mark D. Smucker and Charles L. A. Clarke and Gordon V. Cormack and Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Waterloo at {TREC} 2010: Legal Interactive},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.waterloo.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmuckerCCV10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UB at TREC 2010 Legal Interactive

_Ying Sun_

- :fontawesome-solid-user-group: **Participant:** [UB](./legal/participants.md#ub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/suny.LEGAL.pdf](http://trec.nist.gov/pubs/trec19/papers/suny.LEGAL.pdf)
- :material-file-search: **Runs:** [UBlegal2010](./legal/runs.md#ublegal2010)

??? abstract "Abstract"
	
	For the TREC 2010, the State University of New York at Buffalo participated in the Legal E-Discovery task, working on the interactive search task. We selected to explore RPD task 303. Our focus was on how to approach the problem with the assumption that business communication often wants to maintain secrecy or plausible deniability. Accordingly, it is not in the spirit of the problem to approach formulating queries by limiting ourselves to the mere text of the Complaint and RPD's. We have to envision the actual business context and the actual business practices to determine truly effective queries in the context of litigation. A simple interactive system based on Indri search engine was used to test the queries and examine the results. Post-experiment analysis is underway in alignment with the official evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Sun10.bib) "
	```
	@inproceedings{DBLP:conf/trec/Sun10,
		author = {Ying Sun},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UB} at {TREC} 2010 Legal Interactive},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/suny.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Sun10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Learning Task Experiments in the TREC 2010 Legal Track

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [ot](./legal/participants.md#ot)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/open.txt.corp.legal.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/open.txt.corp.legal.rev.pdf)
- :material-file-search: **Runs:** [otL10rvlT](./legal/runs.md#otl10rvlt) | [otL10FT](./legal/runs.md#otl10ft) | [otL10bT](./legal/runs.md#otl10bt)

??? abstract "Abstract"
	
	The Learning Task of the TREC 2010 Legal Track investigated the effectiveness of e-Discovery search techniques at learning from examples to estimate the probability of relevance of every document in a collection. The task specified 8 test topics, each of which included a one-sentence request for documents to produce and several examples of relevant and non-relevant items from a new target collection of 685,592 e-mail messages and attachments. For our participation, we produced three retrieval sets to compare experimental feedback-based, topic-based and Boolean-based techniques. In this paper, we describe the experimental approaches and report the scores that each achieved on various set-based and rank-based measures. We report not just the mean scores of the experimental approaches but also the scores on each of the 8 individual test topics and the largest per-topic impacts of the techniques for several measures. Of the three experimental approaches compared, the experimental feedback-based approach had the highest score in the rank-based F1@R measure and set-based F1@K measure for a majority of the test topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson10.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson10,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Learning Task Experiments in the {TREC} 2010 Legal Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/open.txt.corp.legal.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Melbourne Team at the TREC 2010 Legal Track

_William Webber, Falk Scholer, Mingfang Wu, Xiuzhen Zhang, Douglas W. Oard, Phil Farrelly, Sandra Potter, Steven Dick, Phill Bertolus_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./legal/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec19/papers/univ.melbourne.LEGAL.pdf](https://trec.nist.gov/pubs/trec19/papers/univ.melbourne.LEGAL.pdf)
- :material-file-search: **Runs:** [rmitmlfT](./legal/runs.md#rmitmlft) | [rmitmlsT](./legal/runs.md#rmitmlst) | [rmitindA](./legal/runs.md#rmitinda) | [melbit10](./legal/runs.md#melbit10)

??? abstract "Abstract"
	
	The Melbourne team was a collaboration between academic and industry groups. The team participated in both the learning and the interactive tasks of this year's Legal Track. The baseline run for the learning track employed true-relevance feedback, achieving respectable outcomes; the experimental runs added additional features and employed an SVM classifier, with poor results. The techniques developed for the learning task were then deployed in the interactive task. The classifier again achieved poor predictive quality, although final results place our production (non-significantly) first. We describe the learning task efforts in Section 2, and the interactive task in Section 3.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WebberSWZOFPDB10.bib) "
	```
	@inproceedings{DBLP:conf/trec/WebberSWZOFPDB10,
		author = {William Webber and Falk Scholer and Mingfang Wu and Xiuzhen Zhang and Douglas W. Oard and Phil Farrelly and Sandra Potter and Steven Dick and Phill Bertolus},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Melbourne Team at the {TREC} 2010 Legal Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {https://trec.nist.gov/pubs/trec19/papers/univ.melbourne.LEGAL.pdf},
		timestamp = {Sun, 11 Feb 2018 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WebberSWZOFPDB10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Session 

#### Overview of the TREC 2010 Session Track

_Evangelos Kanoulas, Paul D. Clough, Ben Carterette, Mark Sanderson_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec19/papers/SESSION.OVERVIEW.2010.pdf](https://trec.nist.gov/pubs/trec19/papers/SESSION.OVERVIEW.2010.pdf)
??? abstract "Abstract"
	
	Research in Information Retrieval has traditionally focused on serving the best results for a single query. In practice however users often enter queries in sessions of reformulations. The Sessions Track at TREC 2010 implements an initial experiment to evaluate the effectiveness of retrieval systems over single query reformulations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KanoulasCCS10.bib) "
	```
	@inproceedings{DBLP:conf/trec/KanoulasCCS10,
		author = {Evangelos Kanoulas and Paul D. Clough and Ben Carterette and Mark Sanderson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2010 Session Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {https://trec.nist.gov/pubs/trec19/papers/SESSION.OVERVIEW.2010.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KanoulasCCS10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Essex at the TREC 2010 Session Track

_M-Dyaa Albakour, Udo Kruschwitz, Jinzhong Niu, Maria Fasli_

- :fontawesome-solid-user-group: **Participant:** [EssexUni](./session/participants.md#essexuni)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.essex.session.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.essex.session.rev.pdf)
- :material-file-search: **Runs:** [essex1.RL1](./session/runs.md#essex1.rl1) | [essex1.RL2](./session/runs.md#essex1.rl2) | [essex1.RL3](./session/runs.md#essex1.rl3) | [essex2.RL1](./session/runs.md#essex2.rl1) | [essex2.RL2](./session/runs.md#essex2.rl2) | [essex2.RL3](./session/runs.md#essex2.rl3) | [essex3.RL1](./session/runs.md#essex3.rl1) | [essex3.RL2](./session/runs.md#essex3.rl2) | [essex3.RL3](./session/runs.md#essex3.rl3)

??? abstract "Abstract"
	
	This paper provides an overview of the experiments we carried out at the TREC 2010 Session Track. We propose an approach for interpreting reformulated queries by using query expansions derived from anchor logs which we envisage to be a potential alternative to query logs. We show that expansion with terms or phrases extracted from anchor logs improves the retrieval performance over a search session. We provide a detailed discussions of our runs which were among the top performing systems of the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlbakourKNF10.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlbakourKNF10,
		author = {M{-}Dyaa Albakour and Udo Kruschwitz and Jinzhong Niu and Maria Fasli},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Essex at the {TREC} 2010 Session Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.essex.session.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlbakourKNF10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2010: Session, Entity and Relevance  Feedback

_Marc Bron, Jiyin He, Katja Hofmann, Edgar Meij, Maarten de Rijke, Manos Tsagkias, Wouter Weerkamp_

- :fontawesome-solid-user-group: **Participant:** [UAms](./session/participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf)
- :material-file-search: **Runs:** [uvaExt1.RL1](./session/runs.md#uvaext1.rl1) | [uvaExt1.RL2](./session/runs.md#uvaext1.rl2) | [uvaExt1.RL3](./session/runs.md#uvaext1.rl3) | [uvaExt2.RL1](./session/runs.md#uvaext2.rl1) | [uvaExt2.RL2](./session/runs.md#uvaext2.rl2) | [uvaExt2.RL3](./session/runs.md#uvaext2.rl3) | [uvaExt3.RL1](./session/runs.md#uvaext3.rl1) | [uvaExt3.RL2](./session/runs.md#uvaext3.rl2) | [uvaExt3.RL3](./session/runs.md#uvaext3.rl3)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the session, entity, and relevance feedback track at TREC 2010. In the Session Track we explore the use of blind relevance feedback to bias a follow-up query towards or against the topics covered in documents returned to the user in response to the original query. In the Entity Track REF task we experiment with a window size parameter to limit the amount of context considered by the entity co-occurrence models and explore the use of Freebase for type filtering, entity normalization and homepage finding. In the ELC task we use an approach that uses the number of links shared between candidate and example entities to rank candidates. In the Relevance Feedback Track we experiment with a novel model that uses Wikipedia to expand the query language model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BronHHMRTW10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BronHHMRTW10,
		author = {Marc Bron and Jiyin He and Katja Hofmann and Edgar Meij and Maarten de Rijke and Manos Tsagkias and Wouter Weerkamp},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at {TREC} 2010: Session, Entity and Relevance Feedback},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BronHHMRTW10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at the TREC 2010 Sessions Track

_Matthias Hagen, Benno Stein, Michael Völske_

- :fontawesome-solid-user-group: **Participant:** [Webis](./session/participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/bauhaus.univ.SESSION.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/bauhaus.univ.SESSION.rev.pdf)
- :material-file-search: **Runs:** [webis2010.RL1](./session/runs.md#webis2010.rl1) | [webis2010.RL2](./session/runs.md#webis2010.rl2) | [webis2010.RL3](./session/runs.md#webis2010.rl3) | [webis2010w.RL3](./session/runs.md#webis2010w.rl3)

??? abstract "Abstract"
	
	In this paper we provide an overview of the Webis group's two-phase approach to the TREC 2010 Sessions track. In a preprocessing phase the queries are segmented to highlight contained concepts. In the final retrieval phase we treat Carnegie Mellon's ClueWeb search engine as a black box and apply the MAXIMUM QUERY framework.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenSV10.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenSV10,
		author = {Matthias Hagen and Benno Stein and Michael V{\"{o}}lske},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Webis at the {TREC} 2010 Sessions Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/bauhaus.univ.SESSION.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenSV10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lugano at TREC 2010

_Mostafa Keikha, Parvaz Mahdabi, Shima Gerani, Giacomo Inches, Javier Parapar, Mark James Carman, Fabio Crestani_

- :fontawesome-solid-user-group: **Participant:** [ULugano](./session/participants.md#ulugano)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.lugano.blog.session.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.lugano.blog.session.pdf)
- :material-file-search: **Runs:** [USIML092010.RL1](./session/runs.md#usiml092010.rl1) | [USIML092010.RL2](./session/runs.md#usiml092010.rl2) | [USIML092010.RL3](./session/runs.md#usiml092010.rl3) | [USIML052010.RL1](./session/runs.md#usiml052010.rl1) | [USIML052010.RL2](./session/runs.md#usiml052010.rl2) | [USIML052010.RL3](./session/runs.md#usiml052010.rl3) | [USIRR2010.RL1](./session/runs.md#usirr2010.rl1) | [USIRR2010.RL2](./session/runs.md#usirr2010.rl2) | [USIRR2010.RL3](./session/runs.md#usirr2010.rl3)

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

#### RMIT University at TREC 2010: Session Track

_Sadegh Kharazmi, Falk Scholer, Mingfang Wu_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./session/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/rmit.session.pdf](http://trec.nist.gov/pubs/trec19/papers/rmit.session.pdf)
- :material-file-search: **Runs:** [RMITBase.RL1](./session/runs.md#rmitbase.rl1) | [RMITBase.RL2](./session/runs.md#rmitbase.rl2) | [RMITBase.RL3](./session/runs.md#rmitbase.rl3) | [RMITExp.RL1](./session/runs.md#rmitexp.rl1) | [RMITExp.RL2](./session/runs.md#rmitexp.rl2) | [RMITExp.RL3](./session/runs.md#rmitexp.rl3)

??? abstract "Abstract"
	
	The 2010 session track aimed to investigate retrieval performance over a search session, taking into account the fact that users often need to re-formulate their initial queries to find useful documents. The experiments carried out by RMIT University investigated a simple strategy of joining query terms across a session, as well as the use of Google suggested queries and whether these can improve the quality of a search result list. For our experiments, we used the Lemur toolkit (version 4.12) to index and search the ClueWeb category B dataset. Ranking was carried out using a Dirichlet-smoothed language model. Query terms were stemmed using the Krovetz stemmer, and stopwords were not removed. Some queries contained punctuation (for example in URLs), and all punctuation was replaced with whitespace. (The only manual editing was that the the sequence “U.S.” was replaced with “USA”, but this could have been done automatically through the use of a simple acronym mapping table).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KharazmiSW10.bib) "
	```
	@inproceedings{DBLP:conf/trec/KharazmiSW10,
		author = {Sadegh Kharazmi and Falk Scholer and Mingfang Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2010: Session Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/rmit.session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KharazmiSW10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cengage Learning at the TREC 2010 Session Track

_Benjamin King, Ivan Provalov_

- :fontawesome-solid-user-group: **Participant:** [GALE](./session/participants.md#gale)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/gale-cengage.rev.SESSION.pdf](http://trec.nist.gov/pubs/trec19/papers/gale-cengage.rev.SESSION.pdf)
- :material-file-search: **Runs:** [CengageS10R1.RL1](./session/runs.md#cengages10r1.rl1) | [CengageS10R1.RL2](./session/runs.md#cengages10r1.rl2) | [CengageS10R1.RL3](./session/runs.md#cengages10r1.rl3) | [CengageS10R2.RL1](./session/runs.md#cengages10r2.rl1) | [CengageS10R2.RL2](./session/runs.md#cengages10r2.rl2) | [CengageS10R2.RL3](./session/runs.md#cengages10r2.rl3) | [CengageS10R3.RL1](./session/runs.md#cengages10r3.rl1) | [CengageS10R3.RL2](./session/runs.md#cengages10r3.rl2) | [CengageS10R3.RL3](./session/runs.md#cengages10r3.rl3)

??? abstract "Abstract"
	
	This paper details Cengage Leaning's TREC 2010 Session track submission and our efforts to improve retrieval performance over a user's session. We use a number of different techniques to achieve this goal including query term weighting, query expansion and re-ranking. In this paper we detail these techniques and the results of our submission. Using our query term weighting technique combined with our corpus term collocation query expansion we were able to achieve 0.2375 for the nsDCG@10.RL13 metric.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KingP10.bib) "
	```
	@inproceedings{DBLP:conf/trec/KingP10,
		author = {Benjamin King and Ivan Provalov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Cengage Learning at the {TREC} 2010 Session Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/gale-cengage.rev.SESSION.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KingP10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Entity 

#### Overview of the TREC 2010 Entity Track

_Krisztian Balog, Pavel Serdyukov, Arjen P. de Vries_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/ENTITY.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec19/papers/ENTITY.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The overall goal of the track is to perform entity-oriented search tasks on the World Wide Web. Many user information needs concern entities (people, organizations, locations, products, ...); these are better answered by returning specific objects instead of just any type of documents. Defining entities on the Web is still an unsolved problem. We settled on representing entities by their homepages, under the assumption that any entity of interest would have at least one homepage. The homepage URL is used as unique identifier. In this scenario, entity ranking corresponds to the task of returning the homepages of entities of a given type, that are relevant to the user's information need (represented as natural language text). We have to also consider that many entity queries could have very large answer sets (e.g., “actors playing in hollywood movies”); extra problematic with corpora the size of ClueWeb. In 2009, we decided therefore that finding associations between entities would be a more challenging one (in terms of modeling) and also a more manageable one (from a test collection building perspective) than finding associations between entities and topics, and defined the Related Entity Finding (REF) task (Balog et al., 2010). Related entity finding requests a ranked list of entities (of a specified type) that engage in a given relationship with a given source entity. REF ran as a pilot in 2009 and is the track's main task in this year; the document collection has been enlarged to the English subset of ClueWeb. We intend to repeat the REF task at least one more time in 2011. One observation from the 2009 edition of the track is that many of the proposed approaches build heavily on Wikipedia and use it as a “semantic backbone”: considering Wikipedia a large repository of entity names and types. Our goal is however not to evaluate entity retrieval over Wikipedia (this task has already been looked at in INEX, and a test collection exists), nor to limit ourselves to the (mostly popular) entities that are present in Wikipedia. As of this year, we are therefore not accepting Wikipedia pages as entity homepages. The issue of combining (noisy) textual material (the Web) with semi-structured data (like Wikipedia or slightly more structured data sources like IMDB) is however an interesting line of research. As many data sources, and in particular those being constructed as so-called Linked Open Data (LOD), are naturally organized around entities, it would be reasonable to examine this problem in the context of entity retrieval. To foster research in this direction, we introduced the new Entity List Completion (ELC) pilot task. ELC is motivated by the same user scenario as REF, but with the main difference that entities are represented by their URIs in a Semantic Web crawl (the Billion Triple Collection). In addition, a small number of example entities (defined by their URIs) are made available as part of the topic definition. Our goal is to turn this pilot task to an “official” task in 2011. In the remainder of the paper we discuss the REF and ELC tasks in detail, in Sections 2 and 3, respectively. We summarize our findings and outline future plans in Section 4.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogSV10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogSV10,
		author = {Krisztian Balog and Pavel Serdyukov and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2010 Entity Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/ENTITY.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalogSV10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LIA-iSmart at TREC 2010: An Unsupervised Web-Based Approach for  Filtering Answers

_Ludovic Bonnefoy, Patrice Bellot, Michel Benoit_

- :fontawesome-solid-user-group: **Participant:** [LIA_UAPV](./entity/participants.md#lia_uapv)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.avignon.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.avignon.entity.rev.pdf)
- :material-file-search: **Runs:** [LearnDPI](./entity/runs.md#learndpi) | [RanksDivComp](./entity/runs.md#ranksdivcomp) | [Comp](./entity/runs.md#comp) | [Div](./entity/runs.md#div)

??? abstract "Abstract"
	
	Searching for named entities has been the subject of many researches in information retrieval. Our goal in participating in TREC 2010 Entity Ranking track is to look for reconizing any named entity in arbitrary categories and use this to rank candidate named entities. We propose to address the issue by means of a web oriented language modeling approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BonnefoyBB10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BonnefoyBB10,
		author = {Ludovic Bonnefoy and Patrice Bellot and Michel Benoit},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {LIA-iSmart at {TREC} 2010: An Unsupervised Web-Based Approach for Filtering Answers},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.avignon.entity.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BonnefoyBB10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2010: Session, Entity and Relevance  Feedback

_Marc Bron, Jiyin He, Katja Hofmann, Edgar Meij, Maarten de Rijke, Manos Tsagkias, Wouter Weerkamp_

- :fontawesome-solid-user-group: **Participant:** [UAms](./entity/participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf)
- :material-file-search: **Runs:** [ilpsM50](./entity/runs.md#ilpsm50) | [ilpsA500](./entity/runs.md#ilpsa500) | [ilpsM50var](./entity/runs.md#ilpsm50var) | [ilpsM50agfil](./entity/runs.md#ilpsm50agfil) | [ilpsSetOL](./entity/runs.md#ilpssetol) | [ilpsSetOLnar](./entity/runs.md#ilpssetolnar)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the ses- sion, entity, and relevance feedback track at TREC 2010. In the Session Track we explore the use of blind relevance feedback to bias a follow-up query towards or against the topics covered in documents returned to the user in response to the original query. In the Entity Track REF task we experiment with a window size parameter to limit the amount of context considered by the entity co-occurrence models and explore the use of Freebase for type filtering, entity normalization and homepage finding. In the ELC task we use an approach that uses the number of links shared between candidate and example entities to rank candidates. In the Relevance Feedback Track we experiment with a novel model that uses Wikipedia to expand the query language model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BronHHMRTW10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BronHHMRTW10,
		author = {Marc Bron and Jiyin He and Katja Hofmann and Edgar Meij and Maarten de Rijke and Manos Tsagkias and Wouter Weerkamp},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at {TREC} 2010: Session, Entity and Relevance Feedback},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BronHHMRTW10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Entity Track TREC 2010

_Lei Cao, Lu Bai, Xueqi Cheng, Jiafeng Guo, Hongbo Xu, Yue Liu, Xiaoming Yu_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./entity/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.ENTITY.new.pdf](http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.ENTITY.new.pdf)
- :material-file-search: **Runs:** [ICTNETRun1](./entity/runs.md#ictnetrun1)

??? abstract "Abstract"
	
	This paper gives an overview of our work for related entity finding which is proposed in TREC 2010 Entity Track. The goal of the Entity Track is to find the entities relevant to a given query from the web corpus. In this paper, we propose a bipartite graph reinforcement model for entity ranking. As is well known, the entities on the web are embedded not only in the natural language text, but also in the tables and lists. Given a query, both the candidate entities and relevant tables/lists are extracted from web documents. Then the candidate entities extracted from unstructured text are ranked based on a probabilistic model. But the result contains a lot of noise. If some candidate entities are in a relevant table/list, they are more relevant to the given query. And Vice versa, if a table/list contains several candidate entities, it is also more relevant to the query. Based on the above intuition, we construct a bipartite graph and then perform a reinforcement algorithm to re-rank the candidate entities.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaoBCGXLY10.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaoBCGXLY10,
		author = {Lei Cao and Lu Bai and Xueqi Cheng and Jiafeng Guo and Hongbo Xu and Yue Liu and Xiaoming Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Entity Track {TREC} 2010},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.ENTITY.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CaoBCGXLY10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Entity List Completion Using Set Expansion Techniques

_Bhavana Bharat Dalvi, Jamie Callan, William W. Cohen_

- :fontawesome-solid-user-group: **Participant:** [CMU_LIRA](./entity/participants.md#cmu_lira)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/carnegie.mellon.univ-lira.ent.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/carnegie.mellon.univ-lira.ent.rev.pdf)
- :material-file-search: **Runs:** [LiraSealClwb](./entity/runs.md#lirasealclwb) | [LiraSealgoog](./entity/runs.md#lirasealgoog)

??? abstract "Abstract"
	
	Set expansion refers to expanding a partial set of “seed” objects into a more complete set. In this paper, we focus on relation and list extraction techniques to perform Entity List Completion task through a two stage retrieval process. First stage takes given query entity and target entity examples as seeds and does set expansion. In second stage, only those candidates who have valid URI in Billion Triple dataset are ranked according to type match with given types. First stage of this system focuses on the recall while second stage tries to improve precision of the outputted list. We submitted the results on the Web as well as ClueWeb09 corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DalviCC10.bib) "
	```
	@inproceedings{DBLP:conf/trec/DalviCC10,
		author = {Bhavana Bharat Dalvi and Jamie Callan and William W. Cohen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Entity List Completion Using Set Expansion Techniques},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/carnegie.mellon.univ-lira.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DalviCC10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Purdue at TREC 2010 Entity Track: A Probabilistic Framework for  Matching Types Between Candidate and Target Entities

_Yi Fang, Luo Si, Naveen Somasundaram, Salman Al-Ansari, Zhengtao Yu, Yantuan Xian_

- :fontawesome-solid-user-group: **Participant:** [Purdue_IR](./entity/participants.md#purdue_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/purdue.univ.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/purdue.univ.entity.rev.pdf)
- :material-file-search: **Runs:** [KMR1PU](./entity/runs.md#kmr1pu) | [KMR3PU](./entity/runs.md#kmr3pu) | [KMR5PU](./entity/runs.md#kmr5pu)

??? abstract "Abstract"
	
	This paper gives an overview of our work for the TREC 2010 Entity track. The goal of the TREC Entity track is to study entity-related searches on Web data, which has not been sufficiently addressed in prior research. For both the Related Entity Finding (REF) task and the Entity List Completion (ELC) task in this track, we propose a unified probabilistic framework by incorporating the matching between target entity types and candidate entity types. This framework is motivated by the observation that much more specific type information than the given type can be inferred from the query narratives. These fine-grained types can help narrow down candidate entities. Specific probabilistic models can be derived from this general framework. For the REF task, besides the type matching component, we generally follow our previous work on TREC Entity 2009. For the ELC task, we apply the same framework and the resulting model combines structured document retrieval with type matching.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FangSSAYX10.bib) "
	```
	@inproceedings{DBLP:conf/trec/FangSSAYX10,
		author = {Yi Fang and Luo Si and Naveen Somasundaram and Salman Al{-}Ansari and Zhengtao Yu and Yantuan Xian},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Purdue at {TREC} 2010 Entity Track: {A} Probabilistic Framework for Matching Types Between Candidate and Target Entities},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/purdue.univ.entity.rev.pdf},
		timestamp = {Tue, 17 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FangSSAYX10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ECIR - A Lightweight Approach for Entity-Centric Information Retrieval

_Alexander Hold, Michael Leben, Benjamin Emde, Christoph Thiele, Felix Naumann, Wojciech M. Barczynski, Falk Brauer_

- :fontawesome-solid-user-group: **Participant:** [HPI](./entity/participants.md#hpi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/hasso-plattner-inst.rev.ENTITY.pdf](http://trec.nist.gov/pubs/trec19/papers/hasso-plattner-inst.rev.ENTITY.pdf)
- :material-file-search: **Runs:** [G16](./entity/runs.md#g16) | [G64](./entity/runs.md#g64) | [B64](./entity/runs.md#b64) | [Y64](./entity/runs.md#y64)

??? abstract "Abstract"
	
	This paper describes our system developed for the TREC 2010 Entity track. In particular we study the exploitation of advanced features of different Web search engines to achieve high quality answers for the 'related entity finding'-task. Our system preprocesses a user query using part-of-speech tagging and synonym dictionaries, and generates an enriched keyword query employing advanced features of particular Web search engines. After retrieving a corpus of documents, the system constructs rules to extract candidate entities. Potentially related entities are deduplicated and scored for each document with respect to the distance to the source entity that is defined in the query. Finally, these scores are aggregated across the corpus by incorporating the rank position of a document. For homepage retrieval we further employ advanced features of Web search engines, for instance to retrieve candidate URLs by queries such as 'entity in anchor'. Homepages are ranked by a weighted aggregation of feature vectors. The weight for each individual feature was determined in beforehand using a genetic learning algorithm. We employed a commercial information extraction system as a basis and implemented our system for three different search engines. We discuss our experiments for the different web search engines and elaborate on the lessons learned.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HoldLETNBB10.bib) "
	```
	@inproceedings{DBLP:conf/trec/HoldLETNBB10,
		author = {Alexander Hold and Michael Leben and Benjamin Emde and Christoph Thiele and Felix Naumann and Wojciech M. Barczynski and Falk Brauer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ECIR} - {A} Lightweight Approach for Entity-Centric Information Retrieval},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/hasso-plattner-inst.rev.ENTITY.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HoldLETNBB10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Anchor Text, Spam Filtering and Wikipedia for Web Search and  Entity Ranking

_Jaap Kamps, Rianne Kaptein, Marijn Koolen_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./entity/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam-kamps.web.ent.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam-kamps.web.ent.rev.pdf)
- :material-file-search: **Runs:** [UAbaseanchB](./entity/runs.md#uabaseanchb) | [UAbaselinkA](./entity/runs.md#uabaselinka) | [UAcatslinkA](./entity/runs.md#uacatslinka) | [UAcatscombB](./entity/runs.md#uacatscombb)

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

#### Searching for Entities When Retrieval Meets Extraction

_Qi Li, Daqing He_

- :fontawesome-solid-user-group: **Participant:** [PITTSIS](./entity/participants.md#pittsis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.pittsburgh.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.pittsburgh.entity.rev.pdf)
- :material-file-search: **Runs:** [ValueDoc](./entity/runs.md#valuedoc) | [EntityHP](./entity/runs.md#entityhp) | [YahooEnHP](./entity/runs.md#yahooenhp) | [EntityHP1](./entity/runs.md#entityhp1)

??? abstract "Abstract"
	
	Retrieving entities inside documents instead of documents or web pages themselves has become an active topic in both commercial search systems and academic information retrieval research. Our method of entity retrieval is based on a two-layer retrieval and extraction probability model (TREPM) for integrating document retrieval and entity extraction together. The document retrieval layer finds supporting documents from the corpus, and the entity extraction layer extracts the right entities from those supporting documents. We theoretically demonstrate that the entity extraction problem can be represented as TREPM model. The TREPM model can reduce the overall retrieval complexity while keeping high accuracy of locating target entities. The experiment is based on the document retrieval and entity extraction as well as the overall task. The preliminary results are promising and deserve for further exploration.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiH10.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiH10,
		author = {Qi Li and Daqing He},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Searching for Entities When Retrieval Meets Extraction},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.pittsburgh.entity.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiH10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Related Entity Finding: University of Waterloo at TREC 2010 Entity  Track

_Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooEng](./entity/participants.md#uwaterlooeng)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.waterlooeng.ent.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.waterlooeng.ent.rev.pdf)
- :material-file-search: **Runs:** [UWEntTI](./entity/runs.md#uwentti) | [UWAT1](./entity/runs.md#uwat1) | [UWAT2](./entity/runs.md#uwat2)

??? abstract "Abstract"
	
	The University of Waterloo participated in the Related Entity Finding task of the Entity track. Our goal is to investigate whether related entity finding problem can be addressed by unsupervised approaches that rely primarily on statistical methods and common linguistic tools, such as named-entity taggers and syntactic parsers. We approach the related entity finding problem by first retrieving documents in response to the query, and extracting an initial set of candidate entities from the text of the documents. As a separate step, we automatically construct a set of seed entities, which represent hyponyms of the target entity category specified in the narrative, and then rank the candidate entities by their similarity to the seeds. An example of the target entity category name is “authors”, extracted from the narrative “Authors awarded an Anthony Award at Bouchercon in 2007” (2009 topic #14). The system extracts category names from the free-text narrative, finds seed entities belonging to each category, and computes the similarity of candidate entities to the seeds.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Vechtomova10.bib) "
	```
	@inproceedings{DBLP:conf/trec/Vechtomova10,
		author = {Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Related Entity Finding: University of Waterloo at {TREC} 2010 Entity Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.waterlooeng.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Vechtomova10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2010: Related Entity Finding Task of Entity Track

_Zhanyi Wang, Chunsong Tang, Xueji Sun, Haoyi Ouyang, Ru Lan, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./entity/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/beijing.univ.p-t.rev.ENTITY.pdf](http://trec.nist.gov/pubs/trec19/papers/beijing.univ.p-t.rev.ENTITY.pdf)
- :material-file-search: **Runs:** [PRIS1](./entity/runs.md#pris1) | [PRIS2](./entity/runs.md#pris2) | [PRIS3](./entity/runs.md#pris3) | [PRIS4](./entity/runs.md#pris4)

??? abstract "Abstract"
	
	This paper reports the approaches to the task of Entity Track applied by PRIS lab of BUPT in TREC 2010. We used Document-Centered Model (DCM) and Entity-Centered Model (ECM) for the task. BM25 method was introduced into ECM besides indri retrieval model. Another improvement aimed at entity extraction. Special web page, NER tool and entity list generated by some rules were all taken into account. Also, some external resources such as Google and CMU search engine were applied.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangTSOLXCG10.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangTSOLXCG10,
		author = {Zhanyi Wang and Chunsong Tang and Xueji Sun and Haoyi Ouyang and Ru Lan and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2010: Related Entity Finding Task of Entity Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/beijing.univ.p-t.rev.ENTITY.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangTSOLXCG10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Multiple-Stage Framework for Related Entity Finding: FDWIM at  TREC 2010 Entity Track

_Dong Wang, Qing Wu, Haiguang Chen, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [FDWIM2010](./entity/participants.md#fdwim2010)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/fudan.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/fudan.entity.rev.pdf)
- :material-file-search: **Runs:** [FduWimET2](./entity/runs.md#fduwimet2) | [FduWimET1](./entity/runs.md#fduwimet1) | [FduWimET3](./entity/runs.md#fduwimet3) | [FduWimET4](./entity/runs.md#fduwimet4)

??? abstract "Abstract"
	
	This paper describes a multiple-stage retrieval framework for the task of related entity finding on TREC 2010 Entity Track. In the document retrieval stage, search engine is used to improve the retrieval accuracy. In the entity extraction and filtering stage, we extract entity with NER tools, Wikipedia and text pattern recognition. Then stoplist and other rules are employed to filter entity. Deep mining of the authority pages is proved to be effective in this stage. In entity ranking stage, many factors including keywords from narrative, page rank, combined results of corpus-based association rules and search engine are considered. In the final stage, an improved feature-based algorithm is proposed for the entity homepage detection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangWCN10.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangWCN10,
		author = {Dong Wang and Qing Wu and Haiguang Chen and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Multiple-Stage Framework for Related Entity Finding: {FDWIM} at {TREC} 2010 Entity Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/fudan.entity.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangWCN10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NiCT at TREC 2010: Related Entity Finding

_Youzheng Wu, Chiori Hori, Hisashi Kawai_

- :fontawesome-solid-user-group: **Participant:** [NiCT](./entity/participants.md#nict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/national.inst.info.comm.tech.rev.ENT.pdf](http://trec.nist.gov/pubs/trec19/papers/national.inst.info.comm.tech.rev.ENT.pdf)
- :material-file-search: **Runs:** [SuppHomeIsA](./entity/runs.md#supphomeisa) | [SuppHome](./entity/runs.md#supphome) | [SuppIsA](./entity/runs.md#suppisa) | [Supp](./entity/runs.md#supp)

??? abstract "Abstract"
	
	This paper describes experiments carried out at NiCT for the TREC 2010 Entity track. Our studies mainly focus on improving the NE Extraction and Ranking Entity modules, both of them play vital roles in Related Entity Finding system. In our last year's system, only a Named Entity Recognition tool is used to extract entities that match coarse-grained types of target entities such as organization, person, etc. In this year, dependency tree-based patterns learnt automatically are employed to filter out entities that do not match fine-grained types of target entities such as university, airline, author, etc. In the Entity Ranking part, we propose a dependency tree-based similarity method and incorporate homepage information to improve ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHK10.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHK10,
		author = {Youzheng Wu and Chiori Hori and Hisashi Kawai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {NiCT at {TREC} 2010: Related Entity Finding},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/national.inst.info.comm.tech.rev.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHK10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Reconstruct Logical Hierarchical Sitemap for Related Entity Finding

_Qing Yang, Peng Jiang, Chunxia Zhang, Zhendong Niu_

- :fontawesome-solid-user-group: **Participant:** [BIT](./entity/participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.entity.rev.pdf)
- :material-file-search: **Runs:** [bitDSRRun](./entity/runs.md#bitdsrrun) | [bitRFRun](./entity/runs.md#bitrfrun) | [bitDSHPRun](./entity/runs.md#bitdshprun)

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

