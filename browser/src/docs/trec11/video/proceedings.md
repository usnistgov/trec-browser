# Proceedings - Video 2002 

#### The TREC-2002 Video Track Report

_Alan F. Smeaton, Paul Over_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/VIDEO.OVER.pdf](http://trec.nist.gov/pubs/trec11/papers/VIDEO.OVER.pdf)
??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmeatonO02.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmeatonO02,
		author = {Alan F. Smeaton and Paul Over},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {TREC-2002} Video Track Report},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/VIDEO.OVER.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmeatonO02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC 2002: Filtering, Q&A, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yingju Xia, Zhe Feng, Yaqian Zhou_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf](http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf)
- :material-file-search: **Runs:** [VFudan](./runs.md#vfudan)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the third time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we only participate in the sub-task of adaptive filtering. A novel method is presented, in which a winnow classifier from the description and narrative fields is constructed, and then utilized to assist our previous adaptive filtering system. A novel approach to confidence sorting, which is based on Maximum Entropy, is proposed in our Question Answering system. The rank of individual answer is determined by several weighted factors, and the confidence score is the product of the exponent of the weights of every factors. The weight of every factor is assigned during the training of previous questions. To return highly relevant key resources for web retrieval, we modified our original search system to make it return higher precision result than before. First, we proposed a novel search algorithm to get a base set of highly relevant documents. Then special post-processing modules are used to expand and re-sort the base set. This year we tried a fast manifold-based approach to face recognition in the Video Search Task. It can be used when there are only few different images of a specific person and runs fast. Experiment shows that applying this step will make the face recognition 5-fold faster and with almost no decreasing of performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHNXFZ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHNXFZ02,
		author = {Lide Wu and Xuanjing Huang and Junyu Niu and Yingju Xia and Zhe Feng and Yaqian Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDU} at {TREC} 2002: Filtering, Q{\&}A, Web and Video Tasks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHNXFZ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Video Indexing and Retrieval at UMD

_Christian Wolf, David S. Doermann, Mika Rautiainen_

- :fontawesome-solid-user-group: **Participant:** [umd_oard](./participants.md#umd_oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umd.doermann.pdf](http://trec.nist.gov/pubs/trec11/papers/umd.doermann.pdf)
- :material-file-search: **Runs:** [VUMD](./runs.md#vumd)

??? abstract "Abstract"
	
	Our team from the University of Maryland and INSA de Lyon participated in the feature extraction evaluation with overlay text features and in the search evaluation with a query retrieval and browsing system. For search we developed a weighted query mechanism by integrating 1) text (OCR and speech recognition) content using full text and n-grams through the MG system, 2) color correlogram indexing of image and video shots reported last year in TREC, and 3) ranked versions of the extracted binary features. A command line version of the interface allows users to formulate simple queries, store them and use weighted combinations of the simple queries to generate compound queries. One novel component of our interactive approach is the ability for the users to formulate dynamic queries previously developed for database applications at Maryland. The interactive interface treats each video clip as visual object in a multi-dimensional space, and each ”feature” of that clip is mapped to one dimension. The user can visualize any two dimensions by placing any two features on the horizontal and vertical axis with additional dimensions visualized by adding attributes to each object.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WolfDR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/WolfDR02,
		author = {Christian Wolf and David S. Doermann and Mika Rautiainen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Video Indexing and Retrieval at {UMD}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umd.doermann.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WolfDR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI at the TREC 2002 Video Track

_Thijs Westerveld, Arjen P. de Vries, Alex van Ballegooij_

- :fontawesome-solid-user-group: **Participant:** [cwi](./participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cwi.westerveld.pdf](http://trec.nist.gov/pubs/trec11/papers/cwi.westerveld.pdf)
- :material-file-search: **Runs:** [VCWI](./runs.md#vcwi)

??? abstract "Abstract"
	
	We present a probabilistic model for the retrieval of multimodal documents. The model is based on Bayesian decision theory and combines models for text based search with models for visual search. The textual model, applied to the LIMSI transcripts, is based on the language modelling approach to text retrieval. The visual model, a mixture of Gaussian densities, describes keyframes selected from shots. Both models have proved successful on media specific retrieval tasks. Our contribution is the combination of both techniques in a unified model, ranking shots on ASR-data and visual features simultaneously. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WesterveldVB02.bib) "
	```
	@inproceedings{DBLP:conf/trec/WesterveldVB02,
		author = {Thijs Westerveld and Arjen P. de Vries and Alex van Ballegooij},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CWI} at the {TREC} 2002 Video Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cwi.westerveld.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WesterveldVB02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Feature Extraction by Active Learning

_Jeroen Vendrig, Ioannis Patras, Cees Snoek, Marcel Worring, Jurgen den Hartog, Stephan Raaijmakers, Jeroen van Rest, David A. van Leeuwen_

- :fontawesome-solid-user-group: **Participant:** [amsterdam_isis](./participants.md#amsterdam_isis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/mediamill.vendrig.pdf](http://trec.nist.gov/pubs/trec11/papers/mediamill.vendrig.pdf)
- :material-file-search: **Runs:** [Vworring](./runs.md#vworring)

??? abstract "Abstract"
	
	[...] We present a system which interactively learns user-defined semantic concepts for a specific collection from a domain expert. For each concept, the domain expert builds a model by feeding visual evidence to the system in the form of examples, without knowledge about the underlying classifier and descriptors. We employ a large set of multimedia descriptors for use in a Maximum Entropy classifier. The space for example selection is determined by the output of the incrementally improved model. The system is evaluated against the TREC 2002 feature extraction collection. The user information consists of the ten semantic concepts defined for the feature extraction task. As our system is based on visual evidence, we focus on visual content of videos. That is, we focus on the features outdoors, indoors, face, people, cityscape, landscape, text overlay and monologue. The classification of the audio features (speech and instrumental sound) is provided independently and is described briefly in section 2.2. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VendrigPSWHRRL02.bib) "
	```
	@inproceedings{DBLP:conf/trec/VendrigPSWHRRL02,
		author = {Jeroen Vendrig and Ioannis Patras and Cees Snoek and Marcel Worring and Jurgen den Hartog and Stephan Raaijmakers and Jeroen van Rest and David A. van Leeuwen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Feature Extraction by Active Learning},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/mediamill.vendrig.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VendrigPSWHRRL02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Semantic Feature Extraction using Mpeg Macro-block Classification

_Fabrice Souvannavong, Bernard Mérialdo, Benoit Huet_

- :fontawesome-solid-user-group: **Participant:** [eurecom](./participants.md#eurecom)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/eurecom.fabrice.pdf](http://trec.nist.gov/pubs/trec11/papers/eurecom.fabrice.pdf)
- :material-file-search: **Runs:** [Veurecom](./runs.md#veurecom)

??? abstract "Abstract"
	
	In this paper, we present some first results in the extraction of semantic features from video sequences. Our approach is based on the classification of Mpeg DCT macro-blocks. Although it is clear that using macro-blocks imposes severe restrictions on the analysis accuracy of the image, it has the advantage of avoiding the complete decoding of the Mpeg stream. Our objective is to evaluate the quality of the Semantic Feature Extraction that can be obtained with this direct approach, to serve as a comparative baseline with more elaborate approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SouvannavongMH02.bib) "
	```
	@inproceedings{DBLP:conf/trec/SouvannavongMH02,
		author = {Fabrice Souvannavong and Bernard M{\'{e}}rialdo and Benoit Huet},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Semantic Feature Extraction using Mpeg Macro-block Classification},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/eurecom.fabrice.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SouvannavongMH02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2002 Video Track Experiments at MediaTeam Oulu and VTT

_Mika Rautiainen, Dmitri Vorobiev, Kai Noponen, Pertti Alvar Väyrynen, Matti Hosio, Esa Matinmikko, Timo Ojala, Tapio Seppänen, Jani Penttilä, Satu-Marja Mäkelä, Johannes Peltola_

- :fontawesome-solid-user-group: **Participant:** [oulu](./participants.md#oulu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uoulu.rautiainen.pdf](http://trec.nist.gov/pubs/trec11/papers/uoulu.rautiainen.pdf)
- :material-file-search: **Runs:** [VOulu](./runs.md#voulu)

??? abstract "Abstract"
	
	In TREC 2002 Video Track MediaTeam Oulu and VTT Technical Research Centre of Finland participated jointly in semantic feature extraction, manual search and interactive search tasks. In the semantic feature extraction task, we sent results for semantic categories of cityscape, landscape, people, speech and instrumental sound. Spatio-temporal correlation of oriented gradient occurrences was used with example shots to detect shots containing people, cityscape or landscape. The audio signal features consisted of various statistical measurements and were used to detect shots containing speech or instrumental sound. Our video browsing and retrieval system, VIRE, was used for manual and interactive search tasks. Our system offers two techniques for video retrieval: 1. Multi-modal indexing based on self-organizing feature maps with semantic filtering. 2. An interactive navigating tool that combines two inter-shot properties, temporal coherency and metric similarities, into a view where database shots are presented in a lattice structure. We tested our interactive navigating tool with eight persons to obtain results for 25 pre-defined search topics. In this paper we give an overview of the approaches and a summary of the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RautiainenVNVHMOSPMP02.bib) "
	```
	@inproceedings{DBLP:conf/trec/RautiainenVNVHMOSPMP02,
		author = {Mika Rautiainen and Dmitri Vorobiev and Kai Noponen and Pertti Alvar V{\"{a}}yrynen and Matti Hosio and Esa Matinmikko and Timo Ojala and Tapio Sepp{\"{a}}nen and Jani Penttil{\"{a}} and Satu{-}Marja M{\"{a}}kel{\"{a}} and Johannes Peltola},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 Video Track Experiments at MediaTeam Oulu and {VTT}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uoulu.rautiainen.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RautiainenVNVHMOSPMP02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLIPS at TREC 11: Experiments in Video Retrieval

_Georges Quénot, Daniel Moraru, Laurent Besacier, Philippe Mulhem_

- :fontawesome-solid-user-group: **Participant:** [clips-imag](./participants.md#clips-imag)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/clips.video.pdf](http://trec.nist.gov/pubs/trec11/papers/clips.video.pdf)
- :material-file-search: **Runs:** [Vclips](./runs.md#vclips)

??? abstract "Abstract"
	
	This pap er presents the systems used by CLIPS-IMAG to p erform the Shot Boundary Detection (SBD) task, the Feature Extraction (FE) and the Search (S) task of the Video track of the TREC-11 conference. Results obtained for the TREC-11 evaluation are presented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QuenotMBM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/QuenotMBM02,
		author = {Georges Qu{\'{e}}not and Daniel Moraru and Laurent Besacier and Philippe Mulhem},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CLIPS} at {TREC} 11: Experiments in Video Retrieval},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/clips.video.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QuenotMBM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Video Retrieval Using Global Features in Keyframes

_Marcus Jerome Pickering, Daniel Heesch, Stefan M. Rüger, Robert J. O'Callaghan, David R. Bull_

- :fontawesome-solid-user-group: **Participant:** [imperial](./participants.md#imperial)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/imperial.pickering.pdf](http://trec.nist.gov/pubs/trec11/papers/imperial.pickering.pdf)
- :material-file-search: **Runs:** [VImperial](./runs.md#vimperial)

??? abstract "Abstract"
	
	We describe our experiments for the shot-boundary detection and search tasks for the TREC-11 video track. Our shot-boundary detection scheme is based on a multi-timescale detection algorithm in which colour histogram differences are examined over a range of frames. Our search efforts are based on a system which brings together a number of global features encompassing colour, texture and text features derived from speech recognition transcripts into a unique relevance feedback system. 
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PickeringHROB02.bib) "
	```
	@inproceedings{DBLP:conf/trec/PickeringHROB02,
		author = {Marcus Jerome Pickering and Daniel Heesch and Stefan M. R{\"{u}}ger and Robert J. O'Callaghan and David R. Bull},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Video Retrieval Using Global Features in Keyframes},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/imperial.pickering.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PickeringHROB02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Automatic Shot Boundary Detection and Classification of Indoor and  Outdoor Scenes

_Andrea Miene, Thorsten Hermes, George T. Ioannidis, R. Fathi, Otthein Herzog_

- :fontawesome-solid-user-group: **Participant:** [ubremen](./participants.md#ubremen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ubremen.miene.pdf](http://trec.nist.gov/pubs/trec11/papers/ubremen.miene.pdf)
- :material-file-search: **Runs:** [VBremen](./runs.md#vbremen)

??? abstract "Abstract"
	
	This paper describes our contribution to the TREC 2002 video analysis track. We participated in the shot detection task and in the feature extraction task (features indoors and outdoors). The shot detection approach is based on histogram differences and uses adaptive thresholds. Multiple detected shot boundaries that follow each other within a short temporal interval are grouped together and classified as a gradual change beginning with the first and ending with the last shot boundary in the interval. For the feature extraction task we examined whether it is possible to classify indoor and outdoor shots by their color distribution. In order to analyze the color distribution we use first order statistical features. The shots are classified into indoor and outdoor shots using a neural net.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MieneHIFH02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MieneHIFH02,
		author = {Andrea Miene and Thorsten Hermes and George T. Ioannidis and R. Fathi and Otthein Herzog},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Automatic Shot Boundary Detection and Classification of Indoor and Outdoor Scenes},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ubremen.miene.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MieneHIFH02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM Research TREC 2002 Video Retrieval System

_Bill Adams, Giridharan Iyengar, Chalapathy Neti, Harriet J. Nock, Arnon Amir, Haim H. Permuter, Savitha Srinivasan, Chitra Dorai, Alejandro Jaimes, Christian A. Lang, Ching-Yung Lin, Apostol Natsev, Milind R. Naphade, John R. Smith, Belle L. Tseng, Sugata Ghosal, Raghavendra Singh, T. V. Ashwin, DongQing Zhang_

- :fontawesome-solid-user-group: **Participant:** [ibm-video](./participants.md#ibm-video)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ibm.smith.vid.pdf](http://trec.nist.gov/pubs/trec11/papers/ibm.smith.vid.pdf)
- :material-file-search: **Runs:** [VIBM](./runs.md#vibm)

??? abstract "Abstract"
	
	In this paper, we describe the IBM Research system for analysis, indexing, and retrieval of video, which was applied to the TREC-2002 video retrieval benchmark. The system explores novel methods for fully-automatic content analysis, shot boundary detection, multi-modal feature extraction, statistical modeling for semantic concept detection, and speech recognition and indexing. The system supports querying based on automatically extracted features, models, and speech information. Additional interactive methods for querying include multiple-example and relevance feedback searching, cluster, concept, and storyboard browsing, and iterative fusion based on user-selected aggregation and combination functions. The system was applied to all four of the tasks of the video retrieval benchmark including shot boundary detection, concept detection, concept exchange, and search. We describe the approaches for each of the tasks and discuss some of the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AdamsINNAPSDJLLNNSTGSAZ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/AdamsINNAPSDJLLNNSTGSAZ02,
		author = {Bill Adams and Giridharan Iyengar and Chalapathy Neti and Harriet J. Nock and Arnon Amir and Haim H. Permuter and Savitha Srinivasan and Chitra Dorai and Alejandro Jaimes and Christian A. Lang and Ching{-}Yung Lin and Apostol Natsev and Milind R. Naphade and John R. Smith and Belle L. Tseng and Sugata Ghosal and Raghavendra Singh and T. V. Ashwin and DongQing Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IBM} Research {TREC} 2002 Video Retrieval System},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ibm.smith.vid.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AdamsINNAPSDJLLNNSTGSAZ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Video Searching and Browsing Using Viewfinder

_Dan E. Albertson, Javed Mostafa, John Fieber_

- :fontawesome-solid-user-group: **Participant:** [indiana](./participants.md#indiana)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/indianau.albertson.pdf](http://trec.nist.gov/pubs/trec11/papers/indianau.albertson.pdf)
- :material-file-search: **Runs:** [VIndiana](./runs.md#vindiana)

??? abstract "Abstract"
	
	Several researchers consisting of students and faculty from the School of Library and Information Science at Indiana University developed a video retrieval system named ViewFinder for the purpose of providing access to video content for a project named the Cultural digital Library Indexing Our Heritage (CLIOH) at Indiana University Purdue University at Indianapolis (IUPUI). For our role in the Text Retrieval Conference (TREC) and its video track, we took the existing system, made notable modifications, and applied it to the video data provided by the conference. After conducting 1 interactive search run, we generated our search results and submitted them to TREC where human judges determined the relevancy of each returned shot and assigned an averaged precision ranking for each topic. From these results we were capable of drawing conclusions of the current system, and how to make ViewFinder more productive in future versions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlbertsonMF02.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlbertsonMF02,
		author = {Dan E. Albertson and Javed Mostafa and John Fieber},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Video Searching and Browsing Using Viewfinder},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/indianau.albertson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlbertsonMF02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Dublin City University Video Track Experiments for TREC 2002

_Paul Browne, Csaba Czirjek, Cathal Gurrin, Roman Jarina, Hyowon Lee, Seán Marlow, Kieran McDonald, Noel Murphy, Noel E. O'Connor, Alan F. Smeaton, Jiamin Ye_

- :fontawesome-solid-user-group: **Participant:** [dublin](./participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/dublincu.smeaton.pdf](http://trec.nist.gov/pubs/trec11/papers/dublincu.smeaton.pdf)
- :material-file-search: **Runs:** [VDublin](./runs.md#vdublin)

??? abstract "Abstract"
	
	Dublin City University participated in the Feature Extraction task and the Search task of the TREC-2002 Video Track. In the Feature Extraction task, we submitted 3 features: Face, Speech, and Music. In the Search task, we developed an interactive video retrieval system, which incorporated the 40 hours of the video search test collection and supported user searching using our own feature extraction data along with the donated feature data and ASR transcript from other Video Track groups. This video retrieval system allows a user to specify a query based on the 10 features and ASR transcript, and the query result is a ranked list of videos that can be further browsed at the shot level. To evaluate the usefulness of the feature-based query, we have developed a second system interface that provides only ASR transcript-based querying, and we conducted an experiment with 12 test users to compare these 2 systems. Results were submitted to NIST and we are currently conducting further analysis of user performance with these 2 systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrowneCGJLMMMOSY02.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrowneCGJLMMMOSY02,
		author = {Paul Browne and Csaba Czirjek and Cathal Gurrin and Roman Jarina and Hyowon Lee and Se{\'{a}}n Marlow and Kieran McDonald and Noel Murphy and Noel E. O'Connor and Alan F. Smeaton and Jiamin Ye},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Dublin City University Video Track Experiments for {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/dublincu.smeaton.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BrowneCGJLMMMOSY02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Temporal Multi-Resolution Framework for Shot Boundary Detection and  Keyframe Extraction

_A. Chandrashekhara, HuaMin Feng, Tat-Seng Chua_

- :fontawesome-solid-user-group: **Participant:** [singapre_hui](./participants.md#singapre_hui)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/nus.video.pdf](http://trec.nist.gov/pubs/trec11/papers/nus.video.pdf)
- :material-file-search: **Runs:** [VNUS](./runs.md#vnus)

??? abstract "Abstract"
	
	Video shot boundary detection and keyframe extraction is an important step in many video-processing applications. We observe that video shot boundary is a multi-resolution edge phenomenon in the feature space. In this experiment, we expanded our previous temporal multi-resolution analysis (TMRA) work by introducing the new feature vector based on motion, incorporating functions to detect flash and camera/object motion, and selecting automatic thresholds for noise elimination based on the type of video. The framework is used to extract meaningful keyframes. Experiments show that our new system can detect and characterize both the abrupt (CUT) and gradual (GT) transitions effectively. It has good accuracy for both the detection of transitions as well as their boundaries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChandrashekharaFC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChandrashekharaFC02,
		author = {A. Chandrashekhara and HuaMin Feng and Tat{-}Seng Chua},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Temporal Multi-Resolution Framework for Shot Boundary Detection and Keyframe Extraction},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/nus.video.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChandrashekharaFC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Video Classification and Retrieval with the Informedia Digital Video  Library System

_Alexander G. Hauptmann, Rong Yan, Yanjun Qi, Rong Jin, Michael G. Christel, Mark Derthick, Ming-Yu Chen, Robert V. Baron, Wei-Hao Lin, Tobun D. Ng_

- :fontawesome-solid-user-group: **Participant:** [cmu-Hauptmann-video](./participants.md#cmu-hauptmann-video)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cmu.hauptmann.pdf](http://trec.nist.gov/pubs/trec11/papers/cmu.hauptmann.pdf)
- :material-file-search: **Runs:** [VCMU](./runs.md#vcmu)

??? abstract "Abstract"
	
	This paper is organized in three parts. The first part details some of the lower level shot classification work, the second part describes the ‘manual' retrieval systems while the last section details the interactive retrieval system for the Carnegie Mellon University TREC Video Retrieval Track runs. The description of the data can be found elsewhere in the proceedings of the 2002 TREC conference video track overview
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HauptmannYQJCDCBLN02.bib) "
	```
	@inproceedings{DBLP:conf/trec/HauptmannYQJCDCBLN02,
		author = {Alexander G. Hauptmann and Rong Yan and Yanjun Qi and Rong Jin and Michael G. Christel and Mark Derthick and Ming{-}Yu Chen and Robert V. Baron and Wei{-}Hao Lin and Tobun D. Ng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Video Classification and Retrieval with the Informedia Digital Video Library System},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cmu.hauptmann.pdf},
		timestamp = {Thu, 16 Dec 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HauptmannYQJCDCBLN02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Shot Boundary Detection Using the Moving Query Window

_Seyed M. M. Tahaghoghi, James A. Thom, Hugh E. Williams_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/rmit.ps.gz](http://trec.nist.gov/pubs/trec11/papers/rmit.ps.gz)
- :material-file-search: **Runs:** [VRMIT](./runs.md#vrmit)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TahaghoghiTW02.bib) "
	```
	@inproceedings{DBLP:conf/trec/TahaghoghiTW02,
		author = {Seyed M. M. Tahaghoghi and James A. Thom and Hugh E. Williams},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Shot Boundary Detection Using the Moving Query Window},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/rmit.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TahaghoghiTW02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

