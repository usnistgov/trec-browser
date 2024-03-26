# Proceedings - Web 2011 

#### Overview of the TREC 2011 Web Track

_Charles L. A. Clarke, Nick Craswell, Ian Soboroff, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/WEB.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec20/papers/WEB.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Web Track explores and evaluates Web retrieval technology over large collections of Web data. In its current incarnation, the Web Track has been active since TREC 2009, where it included both a traditional adhoc retrieval task and a new diversity task [4]. The goal of this diversity task is to return a ranked list of pages that together provide complete coverage for a query, while avoiding excessive redundancy in the result list. For TREC 2010 the track introduced a new Web spam task and Web-style, six-level relevance assessment for the adhoc task [5]. For TREC 2011, as recommended by participants at the track planning session held during TREC 2010, we dropped the spam task but continued the other tasks essentially unchanged. As we did for TREC 2009 and TREC 2010, we based our TREC 2011 experiments on the billion-page ClueWeb091 collection created by the Language Technologies Institute at Carnegie Mellon University. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCSV11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCSV11,
		author = {Charles L. A. Clarke and Nick Craswell and Ian Soboroff and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2011 Web Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/WEB.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCSV11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ranking Web Pages Using Collective Knowledge

_Falah Hassan Al-akashi, Diana Inkpen_

- :fontawesome-solid-user-group: **Participant:** [uottawa](./participants.md#uottawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uottawa.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/uottawa.web.update.pdf)
- :material-file-search: **Runs:** [DFalah11](./runs.md#dfalah11)

??? abstract "Abstract"
	
	Indexing is a crucial technique for dealing with the massive amount of data present on the web. Indexing can be performed based on words or on phrases. Our approach aims to efficiently index web documents by employing a hybrid technique in which web documents are indexed in such a way that knowledge available in the Wikipedia and in meta-content is efficiently used. Our preliminary experiments on the TREC dataset have shown that our indexing scheme is a robust and efficient method for both indexing and for retrieving relevant web pages. We ranked term queries in different ways, depending if they were found in Wikipedia pages or not. This paper presents our preliminary algorithm and experiments for the ad-hoc and diversity tasks of the TREC 2011 Web track. We ran our system on the subset B (50 million web documents) from the ClueWeb09 dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Al-akashiI11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Al-akashiI11,
		author = {Falah Hassan Al{-}akashi and Diana Inkpen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ranking Web Pages Using Collective Knowledge},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uottawa.web.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Al-akashiI11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research at TREC 2011 Web Track

_Bodo Billerbeck, Nick Craswell, Dennis Fetterly, Marc Najork_

- :fontawesome-solid-user-group: **Participant:** [msrsv](./participants.md#msrsv)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/msrsv.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/msrsv.web.update.pdf)
- :material-file-search: **Runs:** [msrsv2011a1](./runs.md#msrsv2011a1) | [msrsv2011a2](./runs.md#msrsv2011a2) | [msrsv2011a3](./runs.md#msrsv2011a3) | [msrsv2011d1](./runs.md#msrsv2011d1) | [msrsv2011d2](./runs.md#msrsv2011d2) | [msrsv2011d3](./runs.md#msrsv2011d3)

??? abstract "Abstract"
	
	This paper describes our entry into the TREC 2011 Web track. We extracted and ranked results from the ClueWeb09 corpus using a parallel processing pipeline that avoids the generation of an inverted file. We describe the components of the parallel architecture and the pipeline, how we ran the TREC experiments, and we present effectiveness results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BillerbeckCFN11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BillerbeckCFN11,
		author = {Bodo Billerbeck and Nick Craswell and Dennis Fetterly and Marc Najork},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research at {TREC} 2011 Web Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/msrsv.web.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BillerbeckCFN11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluating Learning-to-Rank Methods in the Web Track Adhoc Task

_Leonid Boytsov, Anna Belova_

- :fontawesome-solid-user-group: **Participant:** [srchvrs](./participants.md#srchvrs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/srchvrs.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/srchvrs.web.update.pdf)
- :material-file-search: **Runs:** [srchvrs11b](./runs.md#srchvrs11b) | [srchvrs11o](./runs.md#srchvrs11o)

??? abstract "Abstract"
	
	Learning-to-rank methods are becoming ubiquitous in information retrieval. Their advantage lies in the ability to combine a large number of low-impact relevance signals. This requires large training and test data sets. A large test data set is also needed to verify the usefulness of specific relevance signals (using statistical methods). There are several publicly available data collections geared towards evaluation of learning-to-rank methods. These collections are large, but they typically provide a fixed set of precomputed (and often anonymized) relevance signals. In turn, computing new signals may be impossible. This limitation motivated us to experiment with learning-to-rank methods using the TREC Web adhoc collection. Specifically, we compared performance of learning-to-rank methods with performance of a hand-tuned formula (based on the same set of relevance signals). Even though the TREC data set did not have enough queries to draw definitive conclusions, the hand-tuned formula seemed to be at par with learning-to-rank methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoytsovB11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoytsovB11,
		author = {Leonid Boytsov and Anna Belova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Evaluating Learning-to-Rank Methods in the Web Track Adhoc Task},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/srchvrs.web.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoytsovB11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LIA at TREC 2011 Web Track: Experiments on the Combination of  Online Resources

_Romain Deveaud, Eric SanJuan, Patrice Bellot_

- :fontawesome-solid-user-group: **Participant:** [LIA](./participants.md#lia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/LIA.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/LIA.web.update.pdf)
- :material-file-search: **Runs:** [liaQEWikiGoo](./runs.md#liaqewikigoo) | [liaQEWikiGoA](./runs.md#liaqewikigoa) | [liaQEWikiA](./runs.md#liaqewikia) | [liaQEWikiAnA](./runs.md#liaqewikiana)

??? abstract "Abstract"
	
	In this paper, we report the experiments we conducted for our participation to the TREC 2011 Web Track. The experiments we conducted this year aim at discovering how the combination of specific external resources in a language modeling fashion can help web search. We use Wikipedia and Google as external resources for different search contexts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DeveaudSB11.bib) "
	```
	@inproceedings{DBLP:conf/trec/DeveaudSB11,
		author = {Romain Deveaud and Eric SanJuan and Patrice Bellot},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{LIA} at {TREC} 2011 Web Track: Experiments on the Combination of Online Resources},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/LIA.web.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DeveaudSB11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI at TREC 2011: Session, Web, and Medical

_Jiyin He, Vera Hollink, Corrado Boscarino, Arjen P. de Vries, Roberto Cornacchia_

- :fontawesome-solid-user-group: **Participant:** [CWI](./participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/CWI.session.web.medical.pdf](http://trec.nist.gov/pubs/trec20/papers/CWI.session.web.medical.pdf)
- :material-file-search: **Runs:** [CWIcIAt5b1](./runs.md#cwiciat5b1) | [CWIIAt5b5](./runs.md#cwiiat5b5) | [CWIcIA2t5b1](./runs.md#cwicia2t5b1)

??? abstract "Abstract"
	
	We report on the participation of the Interactive Information Access group of the CWI Amsterdam in the web, session, and medical track at TREC 2011. In the web track we focus on the diversity task. We find that cluster-based subtopic modeling approaches improve diversification performance compared to a non-cluster-based subtopic modeling approach. While gain was observed on previous years' topic sets, diversification with the proposed approaches hurt the performance when compared to a non-diversified baseline run on this year's topic set. In the session track, we examine the effects of differentiating between 'good' and 'bad' users. We find that differentiation is useful as the use of search history appears to be mainly effective when the search is not going well. However, our current strategy is not effective for 'good' users. In addition, we studied the use of random walks on query graphs for formulating session history as search queries, but results are inconclusive. In the medical track, we found that the use of medical background resources for query expansion leads to small improvements in retrieval performance. Such resources appear to be especially useful to promote early precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeHBVC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeHBVC11,
		author = {Jiyin He and Vera Hollink and Corrado Boscarino and Arjen P. de Vries and Roberto Cornacchia},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CWI} at {TREC} 2011: Session, Web, and Medical},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/CWI.session.web.medical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeHBVC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Reducing Redundancy with Anchor Text and Spam Priors

_Marijn Koolen, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uamsterdam.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/uamsterdam.web.update.pdf)
- :material-file-search: **Runs:** [UAmsAnc05LS](./runs.md#uamsanc05ls) | [UAmsM705tiLS](./runs.md#uamsm705tils) | [UAmsM7DirExS](./runs.md#uamsm7direxs) | [UAmsM705FLS](./runs.md#uamsm705fls) | [UAmsT05FLS](./runs.md#uamst05fls) | [UAmsM705tFLS](./runs.md#uamsm705tfls)

??? abstract "Abstract"
	
	In this paper, we document our efforts in participating to the TREC 2011 Web Tracks. We had multiple aims: This year, tougher topics were selected for the Web Track, for which there is less popularity information available. We look at the relative value of anchor text for these less popular topics, and at impact of spam priors. Full-text retrieval on the ClueWeb09 B collection suffers from text spam, especially in the top 5 ranks. The spam prior largely reduces the impact of spam, leading to a boost in precision. We find that, in contrast to the more common queries of last year, anchor text does improve ad hoc retrieval performance of a full-text baseline for less common queries. However, for diversity, mixing anchor text and full-text leads to an improvement. Closer analysis reveals that mixing anchor text and full-text, fewer relevant nuggets are retrieved which cover more subtopics. Anchor text is an effective way of reducing redundancy and increasing coverage of subtopics at the same time.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoolenK11.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoolenK11,
		author = {Marijn Koolen and Jaap Kamps},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Reducing Redundancy with Anchor Text and Spam Priors},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uamsterdam.web.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KoolenK11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCD SIFT in the TREC 2011 Web Track

_David Leonard, Doychin Doychev, David Lillis, Fergus Toolan, Rem W. Collier, John Dunnion_

- :fontawesome-solid-user-group: **Participant:** [UCDSIFT](./participants.md#ucdsift)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/SIFT_UCD.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/SIFT_UCD.web.update.pdf)
- :material-file-search: **Runs:** [2011SiftR1](./runs.md#2011siftr1) | [2011SiftR2](./runs.md#2011siftr2) | [2011SiftR3](./runs.md#2011siftr3)

??? abstract "Abstract"
	
	The SIFT (Segmented Information Fusion Techniques) group in UCD is dedicated to researching Data Fusion in Information Retrieval. This area of research involves the merging of multiple sets of results into a single result set that is presented to the user. As a means of both evaluating the effectiveness of this work and comparing it against other retrieval systems, the group entered Category B of the TREC 2011 Web Track. This involved the use of freely-available Information Retrieval tools to provide inputs to the data fusion process. This paper outlines the strategies of the 3 candidate entries submitted to compete in the ad-hoc task, discusses the methodology employed by them and presents a preliminary analysis of the results issued by TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeonardDLTCD11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeonardDLTCD11,
		author = {David Leonard and Doychin Doychev and David Lillis and Fergus Toolan and Rem W. Collier and John Dunnion},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCD} {SIFT} in the {TREC} 2011 Web Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/SIFT\_UCD.web.update.pdf},
		timestamp = {Thu, 11 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LeonardDLTCD11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2011 Ad-Hoc Track

_Heyuan Li, Yuanhai Xue, Xu Chen, Xiaoming Yu, Feng Guan, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-adhoc.pdf](http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-adhoc.pdf)
- :material-file-search: **Runs:** [ICTNET11ADR2](./runs.md#ictnet11adr2) | [ICTNET11DVR1](./runs.md#ictnet11dvr1) | [ICTNET11DVR2](./runs.md#ictnet11dvr2) | [ICTNET11ADR3](./runs.md#ictnet11adr3) | [ICTNET11DVR3](./runs.md#ictnet11dvr3) | [ICTNET11ADR4](./runs.md#ictnet11adr4)

??? abstract "Abstract"
	
	An ad-hoc task in TREC investigates the performance of systems that search a static set of documents using previously-unseen topics. This year, ClueWeb09 Dataset [1] was used again as document collection. But the topics developed for this year was less common and ambiguous than before. The rest of this paper is organized as follows. In Section 2, we discuss the processing of ClueWeb09, derived data and external resources. In Section 3, the BM25 model with term proximity, searching with anchor text, query expansion and promoting authoritative sites are introduced. We report experimental results in Section 4 and conclude our work in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiXCYGLC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiXCYGLC11,
		author = {Heyuan Li and Yuanhai Xue and Xu Chen and Xiaoming Yu and Feng Guan and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2011 Ad-Hoc Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-adhoc.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiXCYGLC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2011: Experiments with Terrier in  Crowdsourcing, Microblog, and Web Tracks

_Richard McCreadie, Craig Macdonald, Rodrygo L. T. Santos, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf](http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf)
- :material-file-search: **Runs:** [uogTrA45Vm](./runs.md#uogtra45vm) | [uogTrA45Nm](./runs.md#uogtra45nm) | [uogTrB47Vm](./runs.md#uogtrb47vm) | [uogTrA45Vmx](./runs.md#uogtra45vmx) | [uogTrA45Nmx2](./runs.md#uogtra45nmx2) | [uogTrB47Vmx](./runs.md#uogtrb47vmx)

??? abstract "Abstract"
	
	In TREC 2011, we focus on tackling the new challenges proposed by the pilot Crowdsourcing and Microblog tracks, using our Terrier Information Retrieval Platform. Meanwhile, we continue to build upon our novel xQuAD framework and data-driven ranking approaches within Terrier to achieve effective and efficient ranking for the TREC Web track. In particular, the aim of our Microblog track participation is the development of a learning to rank approach for filtering within a tweet ranking environment, where tweets are ranked in reverse chronological order. In the Crowdsourcing track, we work to achieve a closer integration between the crowdsourcing marketplaces that are used for relevance assessment, and Terrier, which produces the document rankings to be assessed. Moreover, we focus on generating relevance assessments quickly and at a minimal cost. For the Web track, we enhance the data-driven learning support within Terrier by proposing a novel framework for the fast computation of document features for learning to rank.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMSO11.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMSO11,
		author = {Richard McCreadie and Craig Macdonald and Rodrygo L. T. Santos and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2011: Experiments with Terrier in Crowdsourcing, Microblog, and Web Tracks},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMSO11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2011 Diversity Track

_Shengxian Wan, Yuanhai Xue, Xiaoming Yu, Feng Guan, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-diversity.pdf](http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-diversity.pdf)
- :material-file-search: **Runs:** [ICTNET11ADR2](./runs.md#ictnet11adr2) | [ICTNET11DVR1](./runs.md#ictnet11dvr1) | [ICTNET11DVR2](./runs.md#ictnet11dvr2) | [ICTNET11ADR3](./runs.md#ictnet11adr3) | [ICTNET11DVR3](./runs.md#ictnet11dvr3) | [ICTNET11ADR4](./runs.md#ictnet11adr4)

??? abstract "Abstract"
	
	Traditional IR systems use document-query relevance as the main measure for ranking and consider the relevance is independent of the other documents. However, the only measure of relevance cannot deal with redundant information and can fail to reflect the broad range of user needs that can underlie a query. IR systems need to consider the diversity and novelty of the result list. Diversity task is trying to solve this problem. The goal of diversity task is to return a ranked list of pages that together provide complete coverage for a query, while avoiding excessive redundancy in the result list. This year, the primary evaluation measure is intent aware expected reciprocal rank (ERR-IA) [1], some other evaluation measures such as α-nDCG [1] have also been evaluated. This paper is organized as follows. Section 2 describes different clustering methods used for text clustering. Section 3 describes our query expansion method. Section 4 describes the diversity model used for re-ranking. Section 5 analyzes the result and in section 6 we conclude our work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WanXYGLC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WanXYGLC11,
		author = {Shengxian Wan and Yuanhai Xue and Xiaoming Yu and Feng Guan and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2011 Diversity Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-diversity.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WanXYGLC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Study of Pattern-Based Suptopic Discovery and Integration in the  Web Track

_Wei Zheng, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [Udel_Fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Udel_Fang.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Udel_Fang.web.update.pdf)
- :material-file-search: **Runs:** [UDPattern](./runs.md#udpattern) | [UDCombine1](./runs.md#udcombine1) | [UDCombine2](./runs.md#udcombine2)

??? abstract "Abstract"
	
	We report our systems and experiments in the diversity task of TREC 2011 Web track. Our goal is to evaluate the effectiveness of the proposed methods for subtopic extraction and diversification steps on the large data collection. In the subtopic extraction step, we extract subtopics using both structured data, i.e., ODP, which provides high quality information and unstructured data, i.e., original retrieved documents, which contains terms effective in diversifying documents. In the diversification step, we use a coverage-based method to diversify documents based on the extracted subtopics. It has the desired properties of diversification which favors documents covering more subtopics and documents covering novel subtopics that have not been well covered by previously selected documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengF11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengF11,
		author = {Wei Zheng and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Study of Pattern-Based Suptopic Discovery and Integration in the Web Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Udel\_Fang.web.update.pdf},
		timestamp = {Tue, 20 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengF11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

