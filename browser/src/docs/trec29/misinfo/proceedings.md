# Proceedings - Health Misinformation 2020 

#### Overview of the TREC 2020 Health Misinformation Track

_Charles L. A. Clarke, Saira Rizvi, Mark D. Smucker, Maria Maistro, Guido Zuccon_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.HM.pdf)
??? abstract "Abstract"
	
	TREC 2020 was the second year for the Health Misinformation track, which was named the Decision Track in 2019 [1]. Information retrieval using document collections that contain misinformation are problematic. When a search engine returns documents that contain misinformation, users may have difficulty discerning correct from incorrect information and the incorrect information can lead to incorrect decisions [5]. Decisions regarding health-related topics can be consequential, and as such we want search engines that enable users to make correct decisions. The track is designed to address the problem of health misinformation in three areas: 1) adhoc retrieval, 2) the total recall of misinformation in the collection, and 3) the evaluation of retrieval in the presence of misinformation. The 2020 Health Misinformation track had both a recall task and an adhoc task for participants. With the onset of the coronavirus pandemic (COVID-19), the track organizers selected a document collection of news from the Common Crawl1 that covered the first four months of 2020. The track's topics were all related to COVID-19 and posed as questions such as “Can gargling salt water prevent COVID-19?” For both tasks, NIST assessors judged documents' usefulness for answering a topic's question, and if judged to be useful, assessors then recorded if the document contained a specific answer to the question and then judged the credibility of the document. We evaluated recall runs on their ability to find all documents containing incorrect information (misinformation). For adhoc runs, we measured their ability to return useful, correct, and credible information.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeRSMZ20.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeRSMZ20,
		author = {Charles L. A. Clarke and Saira Rizvi and Mark D. Smucker and Maria Maistro and Guido Zuccon},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2020 Health Misinformation Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.HM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeRSMZ20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2020: Health Misinformation Track Extended Abstract

_Janek Bevendorff, Michael Völske, Benno Stein, Alexander Bondarenko, Maik Fröbe, Sebastian Günther, Matthias Hagen_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/webis.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/webis.HM.pdf)
- :material-file-search: **Runs:** [cn-m-title](./runs.md#cn-m-title) | [cn-title-2](./runs.md#cn-title-2) | [cn-descr-2](./runs.md#cn-descr-2) | [cn-ax-rer](./runs.md#cn-ax-rer) | [cn-kq](./runs.md#cn-kq) | [cn-kq-t-td](./runs.md#cn-kq-t-td) | [cn-kq-td](./runs.md#cn-kq-td)

??? abstract "Abstract"
	
	We give a brief overview of the Webis group's participation in the TREC 2020 Health Misinformation track. e baseline retrieval results of our search engine ChatNoir (BM25F-based) are re-ranked in two dierent approaches: (1) axiomatically re-ranking the top-20 initial results for argumentative topics / queries, and (2) formulating keyqueries to retrieve relevant documents at the top ranks. Our axiomatic re-ranking uses three axioms that capture argumentativeness, while for the keyqueries approach, we use low-eort manual pilot judgments to identify several relevant documents per topic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BevendorffV0BFG20.bib) "
	```
	@inproceedings{DBLP:conf/trec/BevendorffV0BFG20,
		author = {Janek Bevendorff and Michael V{\"{o}}lske and Benno Stein and Alexander Bondarenko and Maik Fr{\"{o}}be and Sebastian G{\"{u}}nther and Matthias Hagen},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2020: Health Misinformation Track Extended Abstract},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/webis.HM.pdf},
		timestamp = {Fri, 19 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BevendorffV0BFG20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CiTIUS at the TREC 2020 Health Misinformation Track

_Marcos Fernández-Pichel, David E. Losada, Juan Carlos Pichel, David Elsweiler_

- :fontawesome-solid-user-group: **Participant:** [CiTIUS](./participants.md#citius)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/CiTIUS.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/CiTIUS.HM.pdf)
- :material-file-search: **Runs:** [CiTIUSCrdAdh](./runs.md#citiuscrdadh) | [CiTIUSCrdRelAdh](./runs.md#citiuscrdreladh) | [CiTIUSCrdTot](./runs.md#citiuscrdtot) | [CiTIUSCrdRelTot](./runs.md#citiuscrdreltot) | [CiTIUSSimTot](./runs.md#citiussimtot) | [CiTIUSSimAdh](./runs.md#citiussimadh) | [CiTIUSSimRelAdh](./runs.md#citiussimreladh)

??? abstract "Abstract"
	
	The TREC Health Misinformation track focuses on discerning reliable from unreliable information and correct from incorrect information. This problem is very common in Web Search results and it is especially critical when it is related to health content [1]. This year's task focuses on COVID-19 and SARS-CoV-2 misinformation. In our experiments, we applied a BM25 retrieval baseline as a first step. Afterwards, we used a document-level reliability classifier recently developed by our team [2]. Finally, we also experimented with BERT-based variants that attempt to estimate similarity between sentences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Fernandez-Pichel20.bib) "
	```
	@inproceedings{DBLP:conf/trec/Fernandez-Pichel20,
		author = {Marcos Fern{\'{a}}ndez{-}Pichel and David E. Losada and Juan Carlos Pichel and David Elsweiler},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {CiTIUS at the {TREC} 2020 Health Misinformation Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/CiTIUS.HM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Fernandez-Pichel20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RealSakaiLab at the TREC 2020 Health Misinformation Track

_Sijie Tao, Tetsuya Sakai_

- :fontawesome-solid-user-group: **Participant:** [RealSakaiLab](./participants.md#realsakailab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/RealSakaiLab.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/RealSakaiLab.HM.pdf)
- :material-file-search: **Runs:** [RSL_BM25](./runs.md#rsl_bm25) | [RSL_BM25LC](./runs.md#rsl_bm25lc) | [RSL_BM25LM](./runs.md#rsl_bm25lm) | [RSL_BM25LMC](./runs.md#rsl_bm25lmc)

??? abstract "Abstract"
	
	In this paper, we describe our experiments conducted for the AdHoc Retrieval task of the TREC 2020 Health Misinformation Track. This task offers a challenges to participants to design a ranking model that promotes retrieval of both credible and correct health information. To address both relevance and credibility, we combined several techniques to re-rank a BM25 baseline ranking. The results from a language identi cation model, a news category classi er and a majority score calculation were used to modify the BM25 scores of the baseline ranking
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TaoS20.bib) "
	```
	@inproceedings{DBLP:conf/trec/TaoS20,
		author = {Sijie Tao and Tetsuya Sakai},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {RealSakaiLab at the {TREC} 2020 Health Misinformation Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/RealSakaiLab.HM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/TaoS20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### VOH.CoLAB at TREC 2020 Health Misinformation Track

_Simao N. Goncalves, Flávio Martins_

- :fontawesome-solid-user-group: **Participant:** [vohcolab](./participants.md#vohcolab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/vohcolab.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/vohcolab.HM.pdf)
- :material-file-search: **Runs:** [vohcolabEvSim](./runs.md#vohcolabevsim) | [vohEvDivTfidf](./runs.md#vohevdivtfidf) | [vohEvDiv_colm](./runs.md#vohevdiv_colm) | [vohbm25rm3](./runs.md#vohbm25rm3) | [vohbm25](./runs.md#vohbm25)

??? abstract "Abstract"
	
	In this paper, we describe the participation of VOH.CoLAB in the TREC 2020 Health Misinformation Track (HMT). This year's edition of the track focused on two main Consumer Health Search tasks regarding COVID-19 questions: 1) to find misinformation; 2) to find relevant, credible, and correct information. In our participation in the HMT track, we submitted runs to both tasks, performing experiments to explore two main research hypothesis: 1) Does misinformation avoid mentioning the evidence text? 2) Does correct and credible information look similar to the evidence text? To explore these two complementary ideas we represent both the documents and the evidence as vectors and compute scores using a formula based on Kullback-Leibler divergence.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoncalvesM20.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoncalvesM20,
		author = {Simao N. Goncalves and Fl{\'{a}}vio Martins},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {VOH.CoLAB at {TREC} 2020 Health Misinformation Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/vohcolab.HM.pdf},
		timestamp = {Thu, 18 Nov 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GoncalvesM20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Copenhagen Participation in TREC Health Misinformation  Track 2020

_Lucas Chaves Lima, Dustin Brandon Wright, Isabelle Augenstein, Maria Maistro_

- :fontawesome-solid-user-group: **Participant:** [KU](./participants.md#ku)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/KU.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/KU.HM.pdf)
- :material-file-search: **Runs:** [run1](./runs.md#run1) | [run2](./runs.md#run2) | [run3](./runs.md#run3) | [run4](./runs.md#run4) | [run5](./runs.md#run5) | [run6](./runs.md#run6) | [run7](./runs.md#run7) | [run8](./runs.md#run8) | [run9](./runs.md#run9) | [run10](./runs.md#run10) | [run11](./runs.md#run11) | [adhoc_run1](./runs.md#adhoc_run1) | [adhoc_run2](./runs.md#adhoc_run2) | [adhoc_run3](./runs.md#adhoc_run3) | [adhoc_run4](./runs.md#adhoc_run4) | [adhoc_run5](./runs.md#adhoc_run5) | [adhoc_run6](./runs.md#adhoc_run6) | [adhoc_run7](./runs.md#adhoc_run7) | [adhoc_run8](./runs.md#adhoc_run8) | [adhoc_run9](./runs.md#adhoc_run9) | [adhoc_run10](./runs.md#adhoc_run10) | [adhoc_run11](./runs.md#adhoc_run11) | [adhoc_run12](./runs.md#adhoc_run12) | [adhoc_run13](./runs.md#adhoc_run13)

??? abstract "Abstract"
	
	In this paper, we describe our participation in the TREC Health Misinformation Track 2020. We submitted 11 runs to the Total Recall Task and 13 runs to the Ad Hoc task. Our approach consists of 3 steps: (1) we create an initial run with BM25 and RM3; (2) we estimate credibility and misinformation scores for the documents in the initial run; (3) we merge the relevance, credibility and misinformation scores to re-rank documents in the initial run. To estimate credibility scores, we implement a classifier which exploits features based on the content and the popularity of a document. To compute the misinformation score, we apply a stance detection approach with a pretrained Transformer language model. Finally, we use different approaches to merge scores: weighted average, the distance among score vectors and rank fusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LimaWAM20.bib) "
	```
	@inproceedings{DBLP:conf/trec/LimaWAM20,
		author = {Lucas Chaves Lima and Dustin Brandon Wright and Isabelle Augenstein and Maria Maistro},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Copenhagen Participation in {TREC} Health Misinformation Track 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/KU.HM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LimaWAM20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLM at TREC 2020 Health Misinformation and Deep Learning Tracks

_Yassine Mrabet, Mourad Sarrouti, Asma Ben Abacha, Soumya Gayen, Travis R. Goodwin, Alastair R. Rae, Willie Rogers, Dina Demner-Fushman_

- :fontawesome-solid-user-group: **Participant:** [NLM](./participants.md#nlm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/NLM.HM.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/NLM.HM.DL.pdf)
- :material-file-search: **Runs:** [NLM_CTM_R1](./runs.md#nlm_ctm_r1) | [NLM_CTM_R2](./runs.md#nlm_ctm_r2) | [NLM_BNU_T5_CTM](./runs.md#nlm_bnu_t5_ctm) | [NLM_BNU_ENS_NLI](./runs.md#nlm_bnu_ens_nli) | [NLM_BNU_E_NLI_C](./runs.md#nlm_bnu_e_nli_c) | [NLM_CTM_R1_C](./runs.md#nlm_ctm_r1_c) | [NLM_TME_NLIR](./runs.md#nlm_tme_nlir) | [NLM_TME_NLIR_C](./runs.md#nlm_tme_nlir_c) | [NLM_E3](./runs.md#nlm_e3) | [NLM_TME](./runs.md#nlm_tme) | [NLM_BNU_E_GH](./runs.md#nlm_bnu_e_gh) | [NLM_TME_GH](./runs.md#nlm_tme_gh) | [NLM_E4](./runs.md#nlm_e4)

??? abstract "Abstract"
	
	This paper describes the participation of the National Library of Medicine to TREC 2020. Our main focus was the health misinformation track. We also participated to the Deep Learning track to both evaluate and enhance our deep re-ranking baselines for information retrieval. Our methods include a wide variety of approaches, ranging from conventional Information Retrieval (IR) models, neural re-ranking models, Natural Language Inference (NLI) models, Claim-Truth models, hyperlinks-based scores such as Page Rank and HITS, and ensemble methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MrabetSAGGRRD20.bib) "
	```
	@inproceedings{DBLP:conf/trec/MrabetSAGGRRD20,
		author = {Yassine Mrabet and Mourad Sarrouti and Asma Ben Abacha and Soumya Gayen and Travis R. Goodwin and Alastair R. Rae and Willie Rogers and Dina Demner{-}Fushman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{NLM} at {TREC} 2020 Health Misinformation and Deep Learning Tracks},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/NLM.HM.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MrabetSAGGRRD20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### H2oloo at TREC 2020: When all you got is a hammer... Deep Learning,  Health Misinformation, and Precision Medicine

_Ronak Pradeep, Xueguang Ma, Xinyu Zhang, Hang Cui, Ruizhou Xu, Rodrigo Frassetto Nogueira, Jimmy Lin_

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf)
- :material-file-search: **Runs:** [h2oloo.m1](./runs.md#h2oloo.m1) | [h2oloo.m2](./runs.md#h2oloo.m2) | [h2oloo.m3](./runs.md#h2oloo.m3) | [h2oloo.m4](./runs.md#h2oloo.m4) | [h2oloo.m5](./runs.md#h2oloo.m5) | [h2oloo.m9](./runs.md#h2oloo.m9) | [h2oloo.m10](./runs.md#h2oloo.m10) | [h2oloo.m7](./runs.md#h2oloo.m7) | [h2oloo.m8](./runs.md#h2oloo.m8)

??? abstract "Abstract"
	
	The h2oloo team from the University of Waterloo participated in the TREC 2020 Deep Learning, Health Misinformation, and Precision Medicine Tracks. Our primary goal was to validate sequence-to-sequence based retrieval techniques that we have been working on in the context of multi-stage retrieval dubbed “Expando-Mono-Duo” [6, 10] comprising a candidate document generation stage (driven by “bag of words” techniques) followed by a pointwise and then a pairwise reranking stage built around T5 [ 11 ], a powerful sequence-to-sequence transformer language model. For the Health Misinformation task, we also employ learnings from our fact verification system, VerT5erini [9]. All of our experiments employed the open-source Anserini IR toolkit [14 , 16], which is based on the popular open-source Lucene search library, for initial retrieval that feeds the T5-based rerankers. Besides being the state of the art in various other collections (e.g., Robust04 and TREC-COVID), we found our models achieved much better effectiveness compared to the BM25 baselines as well as the median scores in all three tracks, demonstrating the versatility and the zero-shot transfer capabilities of our multi-stage ranking system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PradeepMZCXNL20.bib) "
	```
	@inproceedings{DBLP:conf/trec/PradeepMZCXNL20,
		author = {Ronak Pradeep and Xueguang Ma and Xinyu Zhang and Hang Cui and Ruizhou Xu and Rodrigo Frassetto Nogueira and Jimmy Lin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {H2oloo at {TREC} 2020: When all you got is a hammer... Deep Learning, Health Misinformation, and Precision Medicine},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf},
		timestamp = {Mon, 20 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PradeepMZCXNL20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

