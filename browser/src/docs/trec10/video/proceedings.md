# Proceedings - Video 2001 

#### The TREC-2001 Video Track Report

_Alan F. Smeaton, Paul Over, R. Taban_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/TREC10Video_Proc_Report.pdf](http://trec.nist.gov/pubs/trec10/papers/TREC10Video_Proc_Report.pdf)
??? abstract "Abstract"
	
	New in TREC-2001 was the Video Track, the goal of which was to promote progress in content-based retrieval from digital video via open, metrics-based evaluation. The track built on publicly available video provided by the Open Video Project of the University of North Carolina at Chapel Hill under Gary Marchionini (Marchionini, 2001), the NIST Digital Video Library (Over, 2001), and stock shot video provided for TREC-2001 by the British Broadcasting Corporation (Richard Wright et al). The track used very nice work on shot boundary evaluation done as part of the ISIS Coordinated Research Project (AIM, 2001). This paper is an introduction to the track framework — the tasks, data, and measures. For information about results, see the tables associated with the conference proceedings. TREC research has remained true to its late twentieth century origins, concentrating on retrieval of text documents with only occasional excursions into other media: spoken documents and images of doc-uments. Using TREC as an incubator, the Video Track has pushed into true multimedia territory with respect to formulation of search requests, analysis of multimedia material to be searched (video, audio, transcripts, text in video, music, natural sound, etc), combination of search strategies, and in some cases presentation of results to a human searcher The TREC video track had 12 participating groups, 5 from US, 2 from Asia and 5 from Europe. 11 hours of MPEG-1 data was collected and distributed as well as 74 topics or queries. What made these queries particularly interesting and challenging was that they were true multimedia queries as they all had video clips, images, or audio clips as part of the query, in addition to a text description. Participating groups used a variety of techniques to match these multimedia queries against the video dataset, some running fully automated techniques and others involving users in interactive search experiments. As might be expected for the first running of such a track, the framework was a bit unorthodox by the standards of mature TREC tracks. Participating groups contributed significant amounts of work toward the creation of the track infrastructure. Search systems were called upon to handle a very wide variety of topic types. We hoped exploring more of the possible territory, though it decreased the likelihood of definitive outcomes in any one area this year, would still generate some interesting results and more importantly provide a good foundation for a more focused track in TREC-2002. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmeatonOT01.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmeatonOT01,
		author = {Alan F. Smeaton and Paul Over and R. Taban},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-2001} Video Track Report},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/TREC10Video\_Proc\_Report.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmeatonOT01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Lazy Users and Automatic Video Retrieval Tools in (the) Lowlands

_Jan Baan, Alex van Ballegooij, Jan Mark Geusenbroek, Jurgen den Hartog, Djoerd Hiemstra, Johan List, Thijs Westerveld, Ioannis Patras, Stephan Raaijmakers, Cees Snoek, Leon Todoran, Jeroen Vendrig, Arjen P. de Vries, Marcel Worring_

- :fontawesome-solid-user-group: **Participant:** [lowlands](./participants.md#lowlands)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/lowlands01.pdf](http://trec.nist.gov/pubs/trec10/papers/lowlands01.pdf)
- :material-file-search: **Runs:** [MediaMill1](./runs.md#mediamill1) | [MediaMill2](./runs.md#mediamill2) | [Lowlands_1](./runs.md#lowlands_1) | [Lowlands_2](./runs.md#lowlands_2) | [Lowlands_3](./runs.md#lowlands_3) | [Lowlands_4](./runs.md#lowlands_4) | [Lowlands_5](./runs.md#lowlands_5)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC Video Retrieval evaluation. Our approach uses two complementary automatic approaches (the first based on visual content, the other on transcripts), to be refined in an interactive setting. The experiments focused on revealing relationships between (1) different modalities, (2) the amount of human processing, and (3) the quality of the results. We submitted five runs, summarized in Table 1. Run 1 is based on the query text and the visual content of the video. The query text is analyzed to choose the best detectors, e.g. for faces, names, specific camera techniques, dialogs, or natural scenes. Query by example based on detector specific features (e.g. number of faces, invariant color histograms) yields the final ranking result. To assess the additional value of speech content, we experimented with a transcript generated using speech recognition (made available by CMU). We queried the transcribed collection with the topic text combined with the transcripts of video examples. Despite of the error-prone recognition process, the transcripts often provide useful information about the video scenes. Run 2 combines the ranked output of the speech transcripts with (visual-only) run 1 in an attempt to improve its results; run 3 is the obligatory transcript-only run. Run 4 models a user working with the output of an automatic visual run, choosing the best answer-set from a number of options, or attempting to improve its quality by helping the system; for example, finding moon-landers by entering knowledge that the sky on the moon is black or locating the Starwars scene by pointing out that the robot has golden skin. Finally, run 5 combines all information available in our system: from detectors, to speech transcript, to the human-in-the-loop. Depending on the evaluation measures used, this leads to slightly better or slightly worse results than using these methods in isolation, caused by laziness expressed in the model for selecting the combination strategy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/X01.bib) "
	```
	@inproceedings{DBLP:conf/trec/X01,
		author = {Jan Baan and Alex van Ballegooij and Jan Mark Geusenbroek and Jurgen den Hartog and Djoerd Hiemstra and Johan List and Thijs Westerveld and Ioannis Patras and Stephan Raaijmakers and Cees Snoek and Leon Todoran and Jeroen Vendrig and Arjen P. de Vries and Marcel Worring},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Lazy Users and Automatic Video Retrieval Tools in (the) Lowlands},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/lowlands01.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/X01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC-10: Filtering, QA, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yikun Guo, Yingju Xia, Zhe Feng_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf](http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf)
- :material-file-search: **Runs:** [FundanSys1](./runs.md#fundansys1) | [FundanSys2](./runs.md#fundansys2) | [FDUSys1](./runs.md#fdusys1)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the second time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we participate in the sub-task of adaptive and batch filtering. Vector representation and computation are heavily applied in filtering procedure. Four runs have been submitted, which includes one T10SU and one T10F run for adpative filtering, as well as another one T10SU and one T10F run for batch filtering. We have tried many natural language processing techniques in our QA system, including statistical sentence breaking, POS tagging, parsing, name entity tagging, chunking and semantic verification. Various sources of world knowledge are also incorporated, such as WordNet and geographic information. For web retrieval, relevant document set is first created by an extended Boolean retrieval engine, and then reordered according to link information. Four runs with different combination of topic coverage and link information are submitted. On video track, We take part in both of the sub-tasks. In the task of shot boundary detection, we have submitted two runs with different parameters. In the task of video retrieval, we have submitted the results of 17 topics among all the topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHNGXF01.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHNGXF01,
		author = {Lide Wu and Xuanjing Huang and Junyu Niu and Yikun Guo and Yingju Xia and Zhe Feng},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{FDU} at {TREC-10:} Filtering, QA, Web and Video Tasks},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHNGXF01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Integrating Features, Models, and Semantics for TREC Video Retrieval

_John R. Smith, Savitha Srinivasan, Arnon Amir, Sankar Basu, Giridharan Iyengar, Ching-Yung Lin, Milind R. Naphade, Dulce B. Ponceleon, Belle L. Tseng_

- :fontawesome-solid-user-group: **Participant:** [ibm-video](./participants.md#ibm-video)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/IBM-TREC-VIDEO-2001.pdf](http://trec.nist.gov/pubs/trec10/papers/IBM-TREC-VIDEO-2001.pdf)
- :material-file-search: **Runs:** [IBM_Alm1](./runs.md#ibm_alm1) | [IBM_Alm2](./runs.md#ibm_alm2) | [IBM_I_ASR](./runs.md#ibm_i_asr) | [IBM_A_ASR](./runs.md#ibm_a_asr) | [IBM_I_C+S](./runs.md#ibm_i_c+s) | [IBM_A_C+S](./runs.md#ibm_a_c+s) | [IBM_I_CBR](./runs.md#ibm_i_cbr) | [IBM_A_CBR](./runs.md#ibm_a_cbr)

??? abstract "Abstract"
	
	In this paper, we describe a system for automatic and interactive content-based retrieval of video that integrates features, models, and semantics. The novelty of the approach lies in the (1) semi-automatic construction of models of scenes, events, and objects from feature descriptors, and (2) integration of content-based and model-based querying in the search process. We describe several approaches for integration including iterative filtering, score aggregation, and relevance feedback searching. We describe our effort of applying the content-based retrieval system to the TREC video retrieval benchmark.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmithSABILNPT01.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmithSABILNPT01,
		author = {John R. Smith and Savitha Srinivasan and Arnon Amir and Sankar Basu and Giridharan Iyengar and Ching{-}Yung Lin and Milind R. Naphade and Dulce B. Ponceleon and Belle L. Tseng},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Integrating Features, Models, and Semantics for {TREC} Video Retrieval},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/IBM-TREC-VIDEO-2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmithSABILNPT01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNT TRECvid: A Brighton Image Searcher Application

_Mark E. Rorvig, Ki-Tau Jeong, Anup Pachlag, Ramprasad Anusuri, Diane Jenkins, Sara Oyarce_

- :fontawesome-solid-user-group: **Participant:** [north_texas](./participants.md#north_texas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/UNT_final.pdf](http://trec.nist.gov/pubs/trec10/papers/UNT_final.pdf)
- :material-file-search: **Runs:** [UNT1](./runs.md#unt1)

??? abstract "Abstract"
	
	The results, architecture and processing steps used by the University of North Texas team in the 2001 TRECvid video retrieval trials are described. Only a limited number of questions were selected by the team due to resource limitations described in the paper. However, the average precision of the team results over thirteen questions from the General search category were reasonable at 0.59.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RorvigJPAJO01.bib) "
	```
	@inproceedings{DBLP:conf/trec/RorvigJPAJO01,
		author = {Mark E. Rorvig and Ki{-}Tau Jeong and Anup Pachlag and Ramprasad Anusuri and Diane Jenkins and Sara Oyarce},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{UNT} TRECvid: {A} Brighton Image Searcher Application},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/UNT\_final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RorvigJPAJO01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Shot Boundary Detection Task: CLIPS System Description  and Evaluation

_Georges Quénot_

- :fontawesome-solid-user-group: **Participant:** [clips-imag](./participants.md#clips-imag)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/clips-imag-bin.pdf](http://trec.nist.gov/pubs/trec10/papers/clips-imag-bin.pdf)
- :material-file-search: **Runs:** [CLIPS-1](./runs.md#clips-1) | [CLIPS-2](./runs.md#clips-2)

??? abstract "Abstract"
	
	This paper presents the system used by CLIPS-IMAG to perform the Shot Boundary Detection (SBD) task of the Video track of the TREC-10 conference. Cut detection is performed by computing image difference after motion compensation. Dissolve detection is performed by the comparison of the norm over the whole image of the first and second temporal derivatives. An output filter is added in order to clean the data of both detector and to merge them into a consistent output. This system also has a special module for detecting photographic ashes and filtering them as erroneous 'cuts'. Results obtained for the TREC-10 evaluation are presented. The system app ear to p erform in a very go o d way for cut transitions and within the average for gradual transitions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Quenot01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Quenot01,
		author = {Georges Qu{\'{e}}not},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Shot Boundary Detection Task: {CLIPS} System Description and Evaluation},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/clips-imag-bin.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Quenot01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multi-timescale Video Shot-Change Detection

_Marcus Jerome Pickering, Stefan M. Rüger_

- :fontawesome-solid-user-group: **Participant:** [imperial](./participants.md#imperial)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/video-pickering-rueger.pdf](http://trec.nist.gov/pubs/trec10/papers/video-pickering-rueger.pdf)
- :material-file-search: **Runs:** [ICKM1](./runs.md#ickm1)

??? abstract "Abstract"
	
	We describe our shot-boundary detection experiments for the TREC-10 video track, using a multi-timescale shot-change detection algorithm.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PickeringR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/PickeringR01,
		author = {Marcus Jerome Pickering and Stefan M. R{\"{u}}ger},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Multi-timescale Video Shot-Change Detection},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/video-pickering-rueger.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PickeringR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2001: Experiments in Filtering and in Arabic,  Video, and Web Retrieval

_James Mayfield, Paul McNamee, Cash Costello, Christine D. Piatko, Amit Banerjee_

- :fontawesome-solid-user-group: **Participant:** [apl-jhu](./participants.md#apl-jhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf](http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf)
- :material-file-search: **Runs:** [JHUAPL](./runs.md#jhuapl) | [JHUAPLg](./runs.md#jhuaplg)

??? abstract "Abstract"
	
	The outsider might wonder whether, in its tenth year, the Text Retrieval Conference would be a moribund workshop encouraging little innovation and undertaking few new challenges, or whether fresh research problems would continue to be addressed. We feel strongly that it is the later that is true; our group at the Johns Hopkins University Applied Physics Laboratory (JHU/APL) participated in four tracks at this year’s conference, three of which presented us with new and interesting problems. For the first time we participated in the filtering track, and we submitted official results for both the batch and routing subtasks. This year, a first attempt was made to hold a content-based video retrieval track at TREC, and we developed a new suite of tools for image analysis and multimedia retrieval. Finally, though not a stranger to cross-language text retrieval, we made a first attempt at Arabic language retrieval while emphasizing a language-neutral approach that has worked well in other languages. Thus, our team found several challenges to face this year, and this paper mainly reports our initial findings. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MayfieldMCPB01.bib) "
	```
	@inproceedings{DBLP:conf/trec/MayfieldMCPB01,
		author = {James Mayfield and Paul McNamee and Cash Costello and Christine D. Piatko and Amit Banerjee},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{JHU/APL} at {TREC} 2001: Experiments in Filtering and in Arabic, Video, and Web Retrieval},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MayfieldMCPB01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MSR-Asia at TREC-10 Video Track: Shot Boundary Detection Task

_Yufei Ma, Jia Sheng, Yuan Chen, HongJiang Zhang_

- :fontawesome-solid-user-group: **Participant:** [microsoft-china](./participants.md#microsoft-china)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/MSR_SBD.pdf](http://trec.nist.gov/pubs/trec10/papers/MSR_SBD.pdf)
- :material-file-search: **Runs:** [MSSD](./runs.md#mssd)

??? abstract "Abstract"
	
	The video track is added into TREC-10, composed of two tasks, automatic shot boundary detection and video retrieval. In this year, we (MSR-Asia) participated in the video track, focusing on shot boundary detection task. Our work is to find out all of boundaries the shot changes by a fast algorithm based on uncompressed domain. In our algorithm, all of non-cut transitions are considered as gradual transition, including dissolve, fade-in, fade-out, and all kinds of wipes. Experimental results indicate that the accuracy and processing speed of our algorithm are all very satisfactory.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaSCZ01.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaSCZ01,
		author = {Yufei Ma and Jia Sheng and Yuan Chen and HongJiang Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {MSR-Asia at {TREC-10} Video Track: Shot Boundary Detection Task},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/MSR\_SBD.pdf},
		timestamp = {Tue, 16 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MaSCZ01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Video Retrieval with the Informedia Digital Video Library System

_Alexander G. Hauptmann, Rong Jin, Norman Papernick, Tobun Dorbin Ng, Yanjun Qi, Ricky Houghton, Sue Thornton_

- :fontawesome-solid-user-group: **Participant:** [cmu-Hauptmann](./participants.md#cmu-hauptmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/CMU-VideoTrack.pdf](http://trec.nist.gov/pubs/trec10/papers/CMU-VideoTrack.pdf)
- :material-file-search: **Runs:** [CMU1](./runs.md#cmu1) | [CMU2](./runs.md#cmu2) | [CMU3](./runs.md#cmu3) | [CMU4](./runs.md#cmu4)

??? abstract "Abstract"
	
	The Informedia Digital Video Library [1] was the only NSF DLI project focusing specifically on information extraction from video and audio content. Over a terabyte of online data was collected, with automatically generated metadata and indices for retrieving videos from this library. The architecture for the project was based on the premise that real-time constraints on library and associated metadata creation could be relaxed in order to realize increased automation and deeper parsing and indexing for identifying the library contents and breaking it into segments. Library creation was an offline activity, with library exploration by users occurring online and making use of the generated metadata and segmentation. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HauptmannJPNQHT01.bib) "
	```
	@inproceedings{DBLP:conf/trec/HauptmannJPNQHT01,
		author = {Alexander G. Hauptmann and Rong Jin and Norman Papernick and Tobun Dorbin Ng and Yanjun Qi and Ricky Houghton and Sue Thornton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Video Retrieval with the Informedia Digital Video Library System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/CMU-VideoTrack.pdf},
		timestamp = {Thu, 16 Dec 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HauptmannJPNQHT01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Experiments at University of Maryland CLIR and Video

_Kareem Darwish, David S. Doermann, Ryan C. Jones, Douglas W. Oard, Mika Rautiainen_

- :fontawesome-solid-user-group: **Participant:** [umd-allen](./participants.md#umd-allen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf](http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf)
- :material-file-search: **Runs:** [UMDLAMP](./runs.md#umdlamp) | [CMRS_UMD](./runs.md#cmrs_umd) | [CMRS_UMD2](./runs.md#cmrs_umd2)

??? abstract "Abstract"
	
	The University of Maryland Researchers participated in both the Arabic-English Cross Language Information Retrieval (CLIR) and Video tracks of TREC-10. In the CLIR track, our goal was to explore effective monolingual Arabic IR techniques and effective query translation from English to Arabic for cross language IR. For the monolingual part, the use of the different index terms including words, stems, roots, and character n-grams were explored. For the English-Arabic CLIR, the use of MT, wordlist based translation, and non-dictionary words transliteration was explored. In the video track, we participated in the shot boundary detection, and known item search with the primary goals being to evaluate existing technology for shot detection and a new approach to extending simple visual image queries to video sequences. We present a general overview of the approaches, summarize the results in discuss how the algorithms are being extended.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DarwishDJOR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/DarwishDJOR01,
		author = {Kareem Darwish and David S. Doermann and Ryan C. Jones and Douglas W. Oard and Mika Rautiainen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Experiments at University of Maryland {CLIR} and Video},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DarwishDJOR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Dublin City University Video Track Experiments for TREC 2001

_Paul Browne, Cathal Gurrin, Hyowon Lee, Kieran McDonald, Sorin Sav, Alan F. Smeaton, Jiamin Ye_

- :fontawesome-solid-user-group: **Participant:** [DCUKI2001](./participants.md#dcuki2001)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/dcu_trec01_final.pdf](http://trec.nist.gov/pubs/trec10/papers/dcu_trec01_final.pdf)

??? abstract "Abstract"
	
	Dublin City University participated in the interactive search task and Shot Boundary Detection task* of the TREC Video Track. In the interactive search task experiment thirty people used three different digital video browsers to find video segments matching the given topics. Each user was under a time constraint of six minutes for each topic assigned to them. The purpose of this experiment was to compare video browsers and so a method was developed for combining independent users’ results for a topic into one set of results. Collated results based on thirty users are available herein though individual users’ and browsers’ results are currently unavailable for comparison. Our purpose in participating in this TREC track was to create the ground truth within the TREC framework, which will allow us to do direct browser performance comparisons.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrowneGLMSSY01.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrowneGLMSSY01,
		author = {Paul Browne and Cathal Gurrin and Hyowon Lee and Kieran McDonald and Sorin Sav and Alan F. Smeaton and Jiamin Ye},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Dublin City University Video Track Experiments for {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/dcu\_trec01\_final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BrowneGLMSSY01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

