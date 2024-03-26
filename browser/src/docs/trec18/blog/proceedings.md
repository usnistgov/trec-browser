# Proceedings - Blog 2009 

#### Overview of the TREC 2009 Blog Track

_Craig Macdonald, Iadh Ounis, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/BLOG09.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/BLOG09.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Blog track explores the information seeking behaviour in the blogosphere. Thus far, since its inception in 2006 [9], the Blog track addressed two main search tasks based on the analysis of a commercial blog search engine: the opinion-finding task (i.e. “What do people think about X?”) and the blog distillation task (i.e. “Find me a blog with a principal, recurring interest in X.”). In TREC 2009, the Blog track has been markedly revamped with the use of a new and larger sample of the blogosphere, called Blogs08, which has a 13-month timespan covering a period ranging from 14th January 2008 to 10th February 2009, and the introduction of two new search tasks, addressing more refined and typical search scenarios on the blogosphere: Faceted blog distillation: A more refined version of the blog distillation task, addressing the quality aspect of the retrieved blogs. Top stories identification: A task that addresses news-related issues on the blogosphere. Most of the efforts of the organisers in the Blog track 2009 have been spent on defining the new search tasks, on building a suitable infrastructure to support the investigation of the introduced search tasks, and on establishing an appropriate methodology to evaluate the effectiveness of the submitted runs. The remainder of this paper is structured as follows. Section 2 describes the newly created Blogs08 collection. Section 3 describes the new faceted blog distillation task, and discusses the main obtained results by the participating groups. Section 4 describes the top stories identification task, and summarises the results of the runs and the main effective approaches deployed by the participating groups. Concluding remarks are provided in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacdonaldOS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacdonaldOS09,
		author = {Craig Macdonald and Iadh Ounis and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2009 Blog Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/BLOG09.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacdonaldOS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BRAT: A Random Walk Through the Semantic Spaces of the Blogosphere

_Adil El Ghali, Yann Vigile Hoareau_

- :fontawesome-solid-user-group: **Participant:** [shakwat](./participants.md#shakwat)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uparis.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/uparis.BLOG.pdf)
- :material-file-search: **Runs:** [ri2049rw3](./runs.md#ri2049rw3) | [ri1025rw2b](./runs.md#ri1025rw2b) | [ri1025rw5h2b](./runs.md#ri1025rw5h2b) | [ri1025rw5432](./runs.md#ri1025rw5432)

??? abstract "Abstract"
	
	Semantic spaces, such as the Latent Semantic Analysis (LSA), Hyperspace Ana- log to Language (HAL) or Random Indexing (RI), offer convenient methods to represent semantic relations between words and concepts, abstracted from a distribution of documents. The distribution of documents determines the local co-occurrence pattern between words all over the corpus and, then, determines the semantic abstracted from the local distribution. Such methods are sensitive to the statistical properties on the distribution of words over documents. For instance, the semantic on the word table abstracted from a scientific corpus or a general corpus may be different. In the first case, since table may occur in the context of table of correlation or table of results, it would be considered to be associated to the word correlation whereas in the second case, because it may co-occur with kitchen or living-room, it would rather be considered as similar to chair. Nevertheless, the formal relation bearing the properties of the distribution of word's co-occurence and the final semantic produced by Semantic space methods have not been described until now. In the case of a mixed “scientific and general” corpus, what makes that the semantic of table became more similar to chair than Speerman and vice-versa? We approached the Top-stories task of the Blog-Track'09 using a system named Blogosphere Random Analysis using Texts (BRAT) composed of two layers. The first layer distributes and represents blogs posts' in different semantic spaces built using Random Indexing. The second layer is an algorithm of retrieval that have the aim of navigate in the semantic space via a ramdom walk. BRAT have been constructed under two main working hypothesis that we considered important for dealing with the semantic of the blogosphere: the notion of semantic identity and the notion of semantic pollution. The article is organized as follows. In a first part, we shortly overview the methods and properties of semantic spaces models. The notions of semantic identity and semantic pollution are described in general together with their practical implication within the Top-stories task. In the second part, the BRAT system is described. The third part gives an overview of the performances of BRAT for the Top-stories task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GhaliH09.bib) "
	```
	@inproceedings{DBLP:conf/trec/GhaliH09,
		author = {Adil El Ghali and Yann Vigile Hoareau},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BRAT:} {A} Random Walk Through the Semantic Spaces of the Blogosphere},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uparis.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GhaliH09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BIT at TREC 2009 Faceted Blog Distillation Task

_Peng Jiang, Qing Yang, Chunxia Zhang, Zhendong Niu_

- :fontawesome-solid-user-group: **Participant:** [BIT](./participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/bit.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/bit.BLOG.pdf)
- :material-file-search: **Runs:** [BIT09PH](./runs.md#bit09ph) | [BIT09P](./runs.md#bit09p)

??? abstract "Abstract"
	
	This Paper presents the work done for the TREC 2009 faceted blog distillation task of blog track. In our approach, we use a mixture of language models based on global representation. Our model can be regarded as a combination of topic relevance model and faceted relevance model. By pseudo-relevance feedback method, we can estimate the above two models from topic relevance feedback documents and facet relevance feedback documents respectively. Experimental results on TREC blogs08 collection show the effectiveness of our proposed approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangYZN09.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangYZN09,
		author = {Peng Jiang and Qing Yang and Chunxia Zhang and Zhendong Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BIT} at {TREC} 2009 Faceted Blog Distillation Task},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/bit.BLOG.pdf},
		timestamp = {Fri, 04 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JiangYZN09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lugano at TREC 2009 Blog Track

_Mostafa Keikha, Mark James Carman, Robert Gwadera, Shima Gerani, Ilya Markov, Giacomo Inches, Az Azrinudin Alidin, Fabio Crestani_

- :fontawesome-solid-user-group: **Participant:** [USI](./participants.md#usi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ulugano.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/ulugano.BLOG.pdf)
- :material-file-search: **Runs:** [OWA](./runs.md#owa) | [regularized](./runs.md#regularized) | [combined](./runs.md#combined) | [runtag](./runs.md#runtag) | [RegLDM](./runs.md#regldm)

??? abstract "Abstract"
	
	We report on the University of Lugano's participation in the Blog track of TREC 2009. In particular we describe our system for performing blog distillation, faceted search and top stories identification.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KeikhaCGGMIAC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/KeikhaCGGMIAC09,
		author = {Mostafa Keikha and Mark James Carman and Robert Gwadera and Shima Gerani and Ilya Markov and Giacomo Inches and Az Azrinudin Alidin and Fabio Crestani},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Lugano at {TREC} 2009 Blog Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ulugano.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KeikhaCGGMIAC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### POSTECH at TREC 2009 Blog Track: Top Stories Identification

_Yeha Lee, Hun-Young Jung, Woosang Song, Jong-Hyeok Lee_

- :fontawesome-solid-user-group: **Participant:** [POSTECH_KLE](./participants.md#postech_kle)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/postech-kle.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/postech-kle.BLOG.pdf)
- :material-file-search: **Runs:** [KLEFeedPrior](./runs.md#klefeedprior) | [KLEFeed](./runs.md#klefeed) | [KLEClusPrior](./runs.md#kleclusprior) | [KLECluster](./runs.md#klecluster)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2009 Blog Track. Our system consists of the query likelihood component and the news headline prior component, based on the language model framework. For the query likelihood, we propose several approaches to estimate the query language model and the news headline language model. We also suggest two approaches to choose the 10 supporting relevant posts: Feed-Based Selection and Cluster-Based Selection. Furthermore, we propose two criteria to estimate the news headline prior for a given day. Experimental results show that using the prior significantly improves the performance of the task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeJSL09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeJSL09,
		author = {Yeha Lee and Hun{-}Young Jung and Woosang Song and Jong{-}Hyeok Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{POSTECH} at {TREC} 2009 Blog Track: Top Stories Identification},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/postech-kle.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeJSL09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Facet Classification of Blogs: Know-Center at the TREC 2009 Blog  Distillation Task

_Elisabeth Lex, Michael Granitzer, Andreas Juffinger_

- :fontawesome-solid-user-group: **Participant:** [knowcenter](./participants.md#knowcenter)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/know-center.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/know-center.BLOG.pdf)
- :material-file-search: **Runs:** [nounfull](./runs.md#nounfull) | [punctfull](./runs.md#punctfull) | [sentence](./runs.md#sentence)

??? abstract "Abstract"
	
	In this paper, we outline our experiments carried out at the TREC 2009 Blog Distillation Task. Our system is based on a plain text index extracted from the XML feeds of the TREC Blogs08 dataset. This index was used to retrieve candidate blogs for the given topics. The resulting blogs were classified using a Support Vector Machine that was trained on a manually labelled subset of the TREC Blogs08 dataset. Our experiments included three runs on different features: firstly on nouns, secondly on stylometric properties, and thirdly on punctuation statistics. The facet identification based on our approach was successful, although a significant number of candidate blogs were not retrieved at all.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LexGJ09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LexGJ09,
		author = {Elisabeth Lex and Michael Granitzer and Andreas Juffinger},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Facet Classification of Blogs: Know-Center at the {TREC} 2009 Blog Distillation Task},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/know-center.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LexGJ09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Study of Faceted Blog Distillation–PRIS at TREC 2009 Blog Track

_Si Li, Huiji Gao, Hao Sun, Fei Chen, Oupeng Feng, Sanyuan Gao, Hao Zhang, Xinsheng Li, Caili Tan, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [buptpris___2009](./participants.md#buptpris___2009)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/pris.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/pris.BLOG.pdf)
- :material-file-search: **Runs:** [prisb](./runs.md#prisb) | [pris](./runs.md#pris)

??? abstract "Abstract"
	
	This paper describes BUPT (pris) participation in faceted blog distillation task at Blog Track 2009. The system adopts a two-stage strategy in faceted blog distillation task. In the first stage, the system carries out a basic topic relevance retrieval to get the top k blogs for each query. In the second stage, different models are designed to judge the facets and ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiGSCFGZLTXCG09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiGSCFGZLTXCG09,
		author = {Si Li and Huiji Gao and Hao Sun and Fei Chen and Oupeng Feng and Sanyuan Gao and Hao Zhang and Xinsheng Li and Caili Tan and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Study of Faceted Blog Distillation--PRIS at {TREC} 2009 Blog Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/pris.BLOG.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiGSCFGZLTXCG09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2009: Experiments with Terrier

_Richard McCreadie, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf)
- :material-file-search: **Runs:** [uogTrTSbmmr](./runs.md#uogtrtsbmmr) | [uogTrTSemmrs](./runs.md#uogtrtsemmrs) | [uogTrTSwtime](./runs.md#uogtrtswtime) | [uogTrTStimes](./runs.md#uogtrtstimes) | [uogTrFBNclas](./runs.md#uogtrfbnclas) | [uogTrFBMclas](./runs.md#uogtrfbmclas) | [uogTrFBAlr](./runs.md#uogtrfbalr) | [uogTrFBHlr](./runs.md#uogtrfbhlr)

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

#### TREC Blog and TREC Chem: A View from the Corn Fields

_Yelena Mejova, Viet Ha-Thuc, Steven Foster, Christopher G. Harris, Robert J. Arens, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [IowaS](./participants.md#iowas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf](http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf)
- :material-file-search: **Runs:** [IowaSBT0901](./runs.md#iowasbt0901) | [IowaSBT0902](./runs.md#iowasbt0902) | [IowaSBT0903](./runs.md#iowasbt0903) | [IowaSBT0904](./runs.md#iowasbt0904) | [IowaSBD0901](./runs.md#iowasbd0901) | [IowaSBD0902](./runs.md#iowasbd0902)

??? abstract "Abstract"
	
	The University of Iowa Team, participated in the blog track and the chemistry track of TREC-2009. This is our first year participating in the blog track as well as the chemistry track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MejovaHFHAS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/MejovaHFHAS09,
		author = {Yelena Mejova and Viet Ha{-}Thuc and Steven Foster and Christopher G. Harris and Robert J. Arens and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Blog and {TREC} Chem: {A} View from the Corn Fields},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uiowa.BLOG.CHEM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MejovaHFHAS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FEUP at TREC 2009 Blog Track: Temporal Evidence in the Faceted  Blog Distillation Task

_Sérgio Nunes, Cristina Ribeiro, Gabriel David_

- :fontawesome-solid-user-group: **Participant:** [FEUP](./participants.md#feup)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/feup.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/feup.BLOG.pdf)
- :material-file-search: **Runs:** [FEUPirlab1](./runs.md#feupirlab1) | [FEUPirlab2](./runs.md#feupirlab2) | [FEUPirlab3](./runs.md#feupirlab3) | [FEUPirlab4](./runs.md#feupirlab4)

??? abstract "Abstract"
	
	This paper describes the participation of FEUP, from the University of Porto, in the TREC 2009 Blog Track. FEUP participated in the faceted blog distillation task with work focused on the use of temporal features available in the new TREC Blogs08 collection. The approach presented in this paper uses the temporal information available in most individual posts to amplify (or reduce) each post's score. Blog scores, and subsequent ranks, are obtained by combining individual posts' scores. While preparing the runs, no endeavors were made to identify a priori any temporal differences between the three distinct facets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NunesRD09.bib) "
	```
	@inproceedings{DBLP:conf/trec/NunesRD09,
		author = {S{\'{e}}rgio Nunes and Cristina Ribeiro and Gabriel David},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FEUP} at {TREC} 2009 Blog Track: Temporal Evidence in the Faceted Blog Distillation Task},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/feup.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NunesRD09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### From Blogs to News: Identifying Hot Topics in the Blogosphere

_Wouter Weerkamp, Manos Tsagkias, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UAms](./participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.BLOG.pdf)
- :material-file-search: **Runs:** [IlpsTSExP](./runs.md#ilpstsexp) | [IlpsTSExT](./runs.md#ilpstsext) | [IlpsTSHlP](./runs.md#ilpstshlp) | [IlpsTSHlT](./runs.md#ilpstshlt) | [IlpsBDm2T](./runs.md#ilpsbdm2t) | [IlpsBDmxT](./runs.md#ilpsbdmxt) | [IlpsBDmxfT](./runs.md#ilpsbdmxft) | [IlpsBDm1T](./runs.md#ilpsbdm1t)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the blog track at TREC 2009. We focus on the top stories identification task, and take an approach that does not require the headlines of top stories to be known beforehand. We explore the feasibility of a so-called blogs to news approach: given a date and a set of blog posts, identify the main topics for that date. This approach is more general than just finding top stories, but it can still be applied to the task of headline ranking. Results show that this general approach, applied to the task at hand, is among the top performing approaches in this year's TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WeerkampTR09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WeerkampTR09,
		author = {Wouter Weerkamp and Manos Tsagkias and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {From Blogs to News: Identifying Hot Topics in the Blogosphere},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WeerkampTR09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Blog Track TREC 2009

_Xueke Xu, Yue Liu, Hongbo Xu, Xiaoming Yu, Linhai Song, Feng Guan, Zeying Peng, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ictnet.BLOG.pdf](http://trec.nist.gov/pubs/trec18/papers/ictnet.BLOG.pdf)
- :material-file-search: **Runs:** [ICTNETTSRun3](./runs.md#ictnettsrun3) | [ICTNETTSRun2](./runs.md#ictnettsrun2) | [ICTNETTSRun4](./runs.md#ictnettsrun4) | [ICTNETTSRun1](./runs.md#ictnettsrun1) | [ICTNETBDRUN3](./runs.md#ictnetbdrun3) | [ICTNETBDRUN2](./runs.md#ictnetbdrun2) | [ICTNETBDRUN1](./runs.md#ictnetbdrun1) | [ICTNETBDRUN4](./runs.md#ictnetbdrun4)

??? abstract "Abstract"
	
	This paper describes our participation in blog track of TREC2009. All runs are submitted for both two task, namely Top stories identification task and faceted blog distillation task. The “FirteX” platform was used to index and retrieval posts. As for top stories identification task, to identify important headlines, we measure the importance of headline by accumulating the BM25 relevance score with posts on the query day. We propose a graph-based iterative approach and a sub-topic detecting based approach respectively to identify diverse blog posts. As for faceted blog distillation task: we adopt a very straightforward approach and measure the topical relevance by only exploiting top ad-hoc 10000 posts. To identify facet inclination, we either train centroid classifier or compute facet inclination weights of terms to compute facet inclination score and rerank feed by combining relevance score and facet inclination score.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuLXYSGPC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuLXYSGPC09,
		author = {Xueke Xu and Yue Liu and Hongbo Xu and Xiaoming Yu and Linhai Song and Feng Guan and Zeying Peng and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Blog Track {TREC} 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ictnet.BLOG.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuLXYSGPC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

