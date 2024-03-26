# Proceedings - Enterprise 2008 

#### Overview of the TREC 2008 Enterprise Track

_Krisztian Balog, Ian Soboroff, Paul Thomas, Peter Bailey, Nick Craswell, Arjen P. de Vries_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec17/papers/ENTERPRISE.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec17/papers/ENTERPRISE.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The goal of the enterprise track is to conduct experiments with enterprise data that reflect the experiences of users in real organizations. This year, we continued with the CERC collection introduced in TREC 2007 (Bailey et al., 2007). Topics were developed in conjunction with CSIRO Enquiries, who field email and telephone questions about CSIRO research from the public.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogS0BCV08.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogS0BCV08,
		author = {Krisztian Balog and Ian Soboroff and Paul Thomas and Peter Bailey and Nick Craswell and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2008 Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {https://trec.nist.gov/pubs/trec17/papers/ENTERPRISE.OVERVIEW.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalogS0BCV08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Candidate and Document Models for Expert Search

_Krisztian Balog, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UAms_De_Rijke](./participants.md#uams_de_rijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.ent.rev.pdf)
- :material-file-search: **Runs:** [UvA08DSbl](./runs.md#uva08dsbl) | [UvA08DSbfb](./runs.md#uva08dsbfb) | [UvA08DSexp](./runs.md#uva08dsexp) | [UvA08DSall](./runs.md#uva08dsall) | [UvA08EScomb](./runs.md#uva08escomb) | [UvA08ESweb](./runs.md#uva08esweb) | [UvA08ESm1b](./runs.md#uva08esm1b) | [UvA08ESm2all](./runs.md#uva08esm2all)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2008 Enterprise track and detail our language modeling-based approaches. For document search, our focus was on query expansion using profiles of top ranked experts and on document priors. We found that these techniques result in small, but noticeable improvements over our baseline method. For expert search, we combine candidate- and document-based models, and also bring in web evidence. We found that the combined models significantly and consistently outperformed our very competitive baseline models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogR08.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogR08,
		author = {Krisztian Balog and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Candidate and Document Models for Expert Search},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalogR08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DERI at TREC 2008 Enterprise Search Track

_Ronan Cummins, Colm O'Riordan_

- :fontawesome-solid-user-group: **Participant:** [DERI_IR_GROUP](./participants.md#deri_ir_group)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/natu-ireland.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/natu-ireland.ent.rev.pdf)
- :material-file-search: **Runs:** [DERIrun5](./runs.md#derirun5) | [DERIrun6](./runs.md#derirun6) | [DERIrun7](./runs.md#derirun7) | [DERIrun8](./runs.md#derirun8) | [DERIrun1](./runs.md#derirun1) | [DERIrun2](./runs.md#derirun2) | [DERIrun4](./runs.md#derirun4) | [DERIrun3](./runs.md#derirun3)

??? abstract "Abstract"
	
	This paper describes the work carried out by DERI for the Enterprise Search track at TREC 2008. We participated in both the expert search task and document search task of the track. For both tasks we made use of novel learned term-weighting schemes. For the expert search task, we used two different approaches (namely a profiling approach and a two-stage document centric approach). We found that the document centric approach outperforms the profiling approach on previous years TREC data. For the document search task we adopted a standard retrieval framework and made use of the learned term-weighting schemes previously developed for the ad hoc retrieval task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CumminsO08.bib) "
	```
	@inproceedings{DBLP:conf/trec/CumminsO08,
		author = {Ronan Cummins and Colm O'Riordan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DERI} at {TREC} 2008 Enterprise Search Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/natu-ireland.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CumminsO08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2008: Experiments in Blog, Enterprise,  and Relevance Feedback Tracks with Terrier

_Ben He, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf)

??? abstract "Abstract"
	
	In TREC 2008, we participate in the Blog, Enterprise, and Relevance Feedback tracks. In all tracks, we continue the research and development of the Terrier platform1 centred around extending state-of-the-art weighting models based on the Divergence From Randomness (DFR) framework [26]. In particular, we investigate two main themes, namely, proximity-based models, and collection and profile enrichment techniques based on several resources. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeMOPS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeMOPS08,
		author = {Ben He and Craig Macdonald and Iadh Ounis and Jie Peng and Rodrygo L. T. Santos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2008: Experiments in Blog, Enterprise, and Relevance Feedback Tracks with Terrier},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeMOPS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIR at TREC 2008 Expert Search Task: Modeling Expert Evidence  in Expertise Retrieval

_Jiepu Jiang, Wei Lu, Haozhen Zhao_

- :fontawesome-solid-user-group: **Participant:** [WHU](./participants.md#whu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/wuhanu.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/wuhanu.ent.rev.pdf)
- :material-file-search: **Runs:** [WHU08BASE](./runs.md#whu08base) | [WHU08RFCAN](./runs.md#whu08rfcan) | [WHU08NOPHR](./runs.md#whu08nophr) | [WHU08CAN](./runs.md#whu08can)

??? abstract "Abstract"
	
	In this paper, we described our method for the expert search task in TREC 2008. First, we proposed an adaption to the language modeling method for expert search, which considers the probability of query generation separately using each kind of expert evidence (full name, abbreviated name, and email address). Current expert search models can be easily integrated into our method. Our experiments indicated that our method can make use of the ambiguous evidence in expert search (abbreviated name), which often casued a drop in effects in other methods. Besides, we also used a probabilistic measure to detect phrase in query, but it did not make better effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangLZ08.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangLZ08,
		author = {Jiepu Jiang and Wei Lu and Haozhen Zhao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CSIR} at {TREC} 2008 Expert Search Task: Modeling Expert Evidence in Expertise Retrieval},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/wuhanu.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangLZ08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Weighted PageRank: Cluster-Related Weights

_Danil Nemirovsky, Konstantin Avrachenkov_

- :fontawesome-solid-user-group: **Participant:** [inria](./participants.md#inria)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/inria.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/inria.ent.rev.pdf)
- :material-file-search: **Runs:** [4FvfI](./runs.md#4fvfi) | [Rkylv](./runs.md#rkylv) | [TOmUW](./runs.md#tomuw) | [ycbLS](./runs.md#ycbls)

??? abstract "Abstract"
	
	PageRank is a way to rank Web pages taking into account hyper-link structure of the Web. PageRank provides efficient and simple method to find out ranking of Web pages exploiting hyper-link structure of the Web. However, it produces just an approximation of the ranking since the random surfer model uses just uniform distributions for all situation of choice happening during the surf process. In particular, this implies that the random surfer has no preferences. The assumption is limited by its nature. Personalized PageRank was designed to solve the problem but it is still quite restrictive since it assumes non-uniform preferences just at jumping to arbitrary page on the Web and non-preferring behaviour when following outgoing hyper-links. Taking into account these limitations and restrictions of PageRank and Personalized PageRank we propose Weighted PageRank where we are free to weight hyper-links according any possible preferring behaviour of a user. In particular, cluster-related weights are considered.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NemirovskyA08.bib) "
	```
	@inproceedings{DBLP:conf/trec/NemirovskyA08,
		author = {Danil Nemirovsky and Konstantin Avrachenkov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Weighted PageRank: Cluster-Related Weights},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/inria.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NemirovskyA08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Word Importance Discrimination Using Context Information

_Danil Nemirovsky, Vladimir Dobrynin_

- :fontawesome-solid-user-group: **Participant:** [st.petersburg](./participants.md#st.petersburg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/st.petersburg.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/st.petersburg.ent.rev.pdf)
- :material-file-search: **Runs:** [8T0eZ](./runs.md#8t0ez) | [Krcy7](./runs.md#krcy7) | [U2LwQ](./runs.md#u2lwq) | [xLQOW](./runs.md#xlqow)

??? abstract "Abstract"
	
	Word importance discrimination is a task deserving attention when one treats a topic from TREC where a topic is quite long. The goal of the process is to estimate importance of words which carry any (additional) information about user information needs. In our experiments we estimated word importance using context information of a word.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NemirovskyD08.bib) "
	```
	@inproceedings{DBLP:conf/trec/NemirovskyD08,
		author = {Danil Nemirovsky and Vladimir Dobrynin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Word Importance Discrimination Using Context Information},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/st.petersburg.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NemirovskyD08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Blind Relevance Feedback with Wikipedia: Enterprise Track

_Yefei Peng, Ming Mao_

- :fontawesome-solid-user-group: **Participant:** [sebir](./participants.md#sebir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/yahoo.ent.NEW.pdf](http://trec.nist.gov/pubs/trec17/papers/yahoo.ent.NEW.pdf)
- :material-file-search: **Runs:** [TitExpBrf57](./runs.md#titexpbrf57) | [TitExp](./runs.md#titexp) | [TitBrf](./runs.md#titbrf) | [TitDes](./runs.md#titdes)

??? abstract "Abstract"
	
	In this year's Enterprise track experiment, we focused on testing Blind Relevance Feedback, especially using online Wikipedia as query expansion collection. We demonstrated that using Wikipedia as query expansion collection returns better infNDCG than not using it.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PengM08.bib) "
	```
	@inproceedings{DBLP:conf/trec/PengM08,
		author = {Yefei Peng and Ming Mao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Blind Relevance Feedback with Wikipedia: Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/yahoo.ent.NEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PengM08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Universities of Avignon and Lyon III at TREC 2008: Enterprise  Track

_Eric SanJuan, Nicolas Flavier, Patrice Bellot, Fidelia Ibekwe-Sanjuan_

- :fontawesome-solid-user-group: **Participant:** [lia-talne](./participants.md#lia-talne)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uavignon.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uavignon.ent.rev.pdf)
- :material-file-search: **Runs:** [LiaIndriMan](./runs.md#liaindriman) | [LIAIndriSiac](./runs.md#liaindrisiac) | [LiaIcAuto](./runs.md#liaicauto) | [LiaIIcAuto](./runs.md#liaiicauto) | [LiaExp08](./runs.md#liaexp08) | [LiaIcExp08](./runs.md#liaicexp08)

??? abstract "Abstract"
	
	The Enterprise track of TREC 2008 comprised of the same two tasks as in the previous years: an ad-hoc document search and an expert search. The document search consisted in retrieving documents that best matched real-life queries submitted by users to the CSIRO corporation. Systems were allowed to retrieve and rank up to a 1000 documents. The expert search consisted in locating the CSIRO staff who is best able to re- spond to the query formulated by the users. This year was our first participation in TREC-ENT. We explored three major approaches to information retrieval using various existing methods and systems. These approaches ranged from domain knowledge mapping [2] to QA [1].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SanJuanFBI08.bib) "
	```
	@inproceedings{DBLP:conf/trec/SanJuanFBI08,
		author = {Eric SanJuan and Nicolas Flavier and Patrice Bellot and Fidelia Ibekwe{-}Sanjuan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Universities of Avignon and Lyon {III} at {TREC} 2008: Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uavignon.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SanJuanFBI08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Twente at the TREC 2008 Enterprise Track: Using the  Global Web as an Expertise Evidence Source

_Pavel Serdyukov, Robin Aly, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [utwentedb](./participants.md#utwentedb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/utwente.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/utwente.ent.rev.pdf)

??? abstract "Abstract"
	
	This paper describes the details of our participation in expert search task of the TREC 2007 Enterprise track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SerdyukovAH08.bib) "
	```
	@inproceedings{DBLP:conf/trec/SerdyukovAH08,
		author = {Pavel Serdyukov and Robin Aly and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Twente at the {TREC} 2008 Enterprise Track: Using the Global Web as an Expertise Evidence Source},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/utwente.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SerdyukovAH08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Research on Enterprise Track of TREC 2008

_Huawei Shen, Lei Wang, Wenjing Bi, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [I3S_Group_of_ICT](./participants.md#i3s_group_of_ict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/cas-ict.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/cas-ict.ent.rev.pdf)
- :material-file-search: **Runs:** [ICTI3Sdoc01](./runs.md#icti3sdoc01) | [ICTI3Sdoc02](./runs.md#icti3sdoc02) | [ICTI3Sdoc04](./runs.md#icti3sdoc04) | [ICTI3Sdoc03](./runs.md#icti3sdoc03) | [ICTI3Sexp01](./runs.md#icti3sexp01) | [ICTI3Sexp02](./runs.md#icti3sexp02) | [ICTI3Sexp04](./runs.md#icti3sexp04) | [ICTI3Sexp03](./runs.md#icti3sexp03)

??? abstract "Abstract"
	
	This is the third year that we (ICT-CAS team) participated in the Enterprise Track of TREC. The track of this year includes two tasks, being document search task and expert search task. As to the document search task, we compare two retrieval models, namely BM25 model and language model. As to the expert search task, we focus on the authority of persons by exploring the persons' recommendation network constructed from their associated documents. What's more, we investigate the effectiveness of query expansion on both tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShenWBLC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShenWBLC08,
		author = {Huawei Shen and Lei Wang and Wenjing Bi and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Research on Enterprise Track of {TREC} 2008},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/cas-ict.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShenWBLC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2008: Enterprise Track

_Mingfang Wu, Falk Scholer, Steven Garcia_

- :fontawesome-solid-user-group: **Participant:** [rmit](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/rmit.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/rmit.ent.rev.pdf)
- :material-file-search: **Runs:** [RmitDocQ](./runs.md#rmitdocq) | [RmitDQRerank](./runs.md#rmitdqrerank) | [RmitDQCombLO](./runs.md#rmitdqcomblo) | [RmitDQExp](./runs.md#rmitdqexp)

??? abstract "Abstract"
	
	RMIT participated in the 2008 Enterprise Track document search task. Our experiments investigated the use of local outdegree, and whether this can improve the ranking quality of a search result list. Unlike global outdegree, which counts the number of out-links of a page that point to any other pages in a collection, local outdegree only counts the out-links that point to pages contained in a search result list. Intuitively, restricting the outdegree to the result set of a query transforms this source of evidence from something general into a topically-focused source of information, and may help to reduce the problem of topic shift. For our experiments, we used the Zettair search engine1 to index and search the CSIRO collection used for the 2008 Enterprise Track. This collection is a crawl of the the public-facing web of the Australian Commonwealth Scientific and Industrial Research Organization (CSIRO) in 2007 (Bailey et al., 2007). Document weights were calculated using the Okapi BM25 similarity function (Sparck Jones et al., 2000), with query words being terms from the query fields of the track topics. During indexing and search, words are stemmed and stopped.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuSG08.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuSG08,
		author = {Mingfang Wu and Falk Scholer and Steven Garcia},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2008: Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/rmit.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuSG08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2008: Enterprise Track

_Yufei Xue, Tong Zhu, Guichun Hua, Min Zhang, Yiqun Liu, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [THUIR](./participants.md#thuir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/tsinghua.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/tsinghua.ent.rev.pdf)
- :material-file-search: **Runs:** [THUFmfS](./runs.md#thufmfs) | [THUFS](./runs.md#thufs) | [THUFaAS](./runs.md#thufaas) | [THUFsimAncL](./runs.md#thufsimancl) | [THUPDDSwp](./runs.md#thupddswp) | [THUPDDlchrS](./runs.md#thupddlchrs) | [THUPDDlcS](./runs.md#thupddlcs) | [THUPDDSlL](./runs.md#thupddsll)

??? abstract "Abstract"
	
	We participate in document search and expert search of Enterprise Track in TREC2008. The corpus and tasks are same as the year before. Different from TREC 2007, the topics come from CSIRO Enquiries, and the topic statements are richer and more colloquial.. In document search, we look into the key resource page pre-selection, the use of anchor text, query classification, and multi-field search. In expert search, we develop methods to detect expert identifiers and experimented based on our previous PDD (personal description documents) model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XueZHZLM08.bib) "
	```
	@inproceedings{DBLP:conf/trec/XueZHZLM08,
		author = {Yufei Xue and Tong Zhu and Guichun Hua and Min Zhang and Yiqun Liu and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2008: Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/tsinghua.ent.rev.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/XueZHZLM08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Role Determination and Expert Mining in the Enterprise Environment

_Jing Yao, Jun Xu, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [wim-lab.fudan](./participants.md#wim-lab.fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/fudanu.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/fudanu.ent.rev.pdf)
- :material-file-search: **Runs:** [FDUBase](./runs.md#fdubase) | [FDUExpand](./runs.md#fduexpand) | [FDUEmail](./runs.md#fduemail) | [FDUUrl](./runs.md#fduurl) | [FDUExpBase](./runs.md#fduexpbase) | [FDUExpRole](./runs.md#fduexprole) | [FDUExpRes](./runs.md#fduexpres) | [FDURoleRes](./runs.md#fduroleres)

??? abstract "Abstract"
	
	In real world, expert search is not just only name matching. Since each kind of people has their own features, we try two methods to judge whether the person we have found is more likely to be an expert. One method is to determine the role of a person by the context of the pages; the other is to judge the authority of a person by the forms of pages where he appears considering the structure of the Intranet. The evaluation results show these new methodologies have been helpful to improve the performance of the expert search on TREC 08 queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YaoXN08.bib) "
	```
	@inproceedings{DBLP:conf/trec/YaoXN08,
		author = {Jing Yao and Jun Xu and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Role Determination and Expert Mining in the Enterprise Environment},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/fudanu.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YaoXN08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University College London at TREC 2008 Enterprise Track

_Jianhan Zhu_

- :fontawesome-solid-user-group: **Participant:** [UCL](./participants.md#ucl)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/ucollege-london.ent.NEW.pdf](http://trec.nist.gov/pubs/trec17/papers/ucollege-london.ent.NEW.pdf)
- :material-file-search: **Runs:** [ucl01](./runs.md#ucl01) | [ucl02](./runs.md#ucl02) | [ucl03](./runs.md#ucl03) | [ucl04](./runs.md#ucl04) | [UCLex01](./runs.md#uclex01) | [UCLex02](./runs.md#uclex02) | [UCLex03](./runs.md#uclex03) | [UCLex04](./runs.md#uclex04)

??? abstract "Abstract"
	
	The University College London Information Retrieval Group participated in both the Expert Search and Document Search tasks in the TREC2008 Enterprise Track. We used a generic two-stage approach, which consists of a document retrieval stage followed by an expert association discovery stage, for expert finding. Since document search is an integral part of our expert finding approach, we have studied the relationship between document search and expert search. Due to the existence of rich features that can potentially contribute to expert finding, our expert finding approach integrates these features including anchor texts, indegree, and multiple levels of associations between experts and query terms. Our experimental results show that the introduction of features has helped improve the expert finding performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zhu08.bib) "
	```
	@inproceedings{DBLP:conf/trec/Zhu08,
		author = {Jianhan Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University College London at {TREC} 2008 Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/ucollege-london.ent.NEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Zhu08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

