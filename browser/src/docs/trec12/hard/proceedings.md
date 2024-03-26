# Proceedings - HARD 2003 

#### HARD Track Overview in TREC 2003: High Accuracy Retrieval from  Documents

_James Allan_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/HARD.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec12/papers/HARD.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The effectiveness of ad-hoc retrieval systems appears to have reached a plateau. After several years of 10% gains every year in TREC, improvements dwindled or even stopped. This lack of progress was undoubtedly one of the reasons behind abandoning suspending the ad-hoc TREC after TREC-9. One plausible reason that document retrieval has been unable to improve is that the nature of the task requires that systems adopt “one size fits all” approaches. Given a query, a system will generally do best to return results that are good for an “average” user. Doing otherwise (i.e., targeting the results for a particular type of user) might result in substantial improvements on a query, but it is just as likely (in a TREC environment) to cause horrible degradation. By ignoring the user (or, more accurately, by treating all users identically), systems cannot possibly advance beyond a particular level of accuracy on average for a specific user. The goal of this track is to bring the user out of hiding, making him or her an integral part of both the search process and the evaluation. Systems do not have just a query to chew on, but also have as much information as possible about the person making the request, ranging from biographical data, through information seeking context, to expected type of result. The HARD track is a variant of the ad-hoc retrieval task from the past. It was a “pilot” track in 2003 because of the substantial extension on past evaluation—i.e., it is not clear how best to evaluate some of the aspects of the track, so at least for this year it was intended to be very open ended. HARD is also running as a track of TREC 2004. The HARD 2003 track ran in three phases: baseline, clarifying, and final. In the first phase, sites received and ran topics that were essentially idential to a classic TREC topic: title, description, and narrative fields. In the second phase, sites were able to acquire clarifying information about the topics. They had two means and could use either or both of them: 1. Biographical, contextual, preferred result format, and any information that disambiguates the query was captured when the topics were generated. This metadata about the query was made available for phase two. 2. Sites were permitted to generate a single “clarifying form” that the searcher would answer. For each topic, this form was a Web page that solicited useful information about the query or the searcher (e.g., disambiguating words in the query or finding out more information about what the searcher wants). The assumption was that the “clarification” would be generated automatically, but sites could have opted 0to generate manual clarification questions (can a librarian beat the best IR systems?). None did. In the final phase of the track, sites used all user- and query-information that they acquired to construct a better and more accurate ranked list. That substantially improved (because it is more targeted) list was submitted to NIST for evaluation. Because accurate retrieval could also just be pinpointed retrieval, an extension of the HARD track evaluated passage retrieval, a system's ability to select passages within documents that are relevant. Passage retrieval was an option available to sites, but could be ignored by returning full documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Allan03.bib) "
	```
	@inproceedings{DBLP:conf/trec/Allan03,
		author = {James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{HARD} Track Overview in {TREC} 2003: High Accuracy Retrieval from Documents},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {24--37},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/HARD.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Allan03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers' HARD and Web Interactive Track Experiments at TREC 2003

_Nicholas J. Belkin, Diane Kelly, Hyuk-Jin Lee, Yuelin Li, Gheorghe Muresan, Muh-Chyun (Morris) Tang, Xiaojun Yuan, Xiao-Min Zhang_

- :fontawesome-solid-user-group: **Participant:** [rutgers.belkin](./participants.md#rutgers.belkin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/rutgersu.hard.web.pdf](http://trec.nist.gov/pubs/trec12/papers/rutgersu.hard.web.pdf)
- :material-file-search: **Runs:** [rutbase1](./runs.md#rutbase1) | [rutbase2](./runs.md#rutbase2) | [Rutmeta](./runs.md#rutmeta)

??? abstract "Abstract"
	
	This year, members of our group, the Information Interaction Laboratory at Rutgers, SCILS, participated in the HARD track, and in the Interactive Sub-track of the Web track. Since there were no points of commonality between the two separate investigations, we describe and present the results and conclusions for each separately.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinKLLMTYZ03.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinKLLMTYZ03,
		author = {Nicholas J. Belkin and Diane Kelly and Hyuk{-}Jin Lee and Yuelin Li and Gheorghe Muresan and Muh{-}Chyun (Morris) Tang and Xiaojun Yuan and Xiao{-}Min Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Rutgers' {HARD} and Web Interactive Track Experiments at {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {532--543},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/rutgersu.hard.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BelkinKLLMTYZ03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2003 Robust, HARD and QA Track Experiments using PIRCS

_Laszlo Grunfeld, Kui-Lam Kwok, Norbert Dinstl, Peter Deng_

- :fontawesome-solid-user-group: **Participant:** [queensc.kwok](./participants.md#queensc.kwok)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf)
- :material-file-search: **Runs:** [pircHDBt1](./runs.md#pirchdbt1) | [pircHDBtd1](./runs.md#pirchdbtd1) | [pircHDC1t1](./runs.md#pirchdc1t1) | [pircHDC2t2](./runs.md#pirchdc2t2) | [pircHDC2t1](./runs.md#pirchdc2t1) | [pircHDC3td1](./runs.md#pirchdc3td1) | [pircHDC3td2](./runs.md#pirchdc3td2) | [pircHDC1tp](./runs.md#pirchdc1tp) | [pircHDC2tp](./runs.md#pirchdc2tp) | [pircHDC3tdp](./runs.md#pirchdc3tdp)

??? abstract "Abstract"
	
	We participated in the Robust, HARD and part of the QA tracks in TREC2003. For Robust track, a new way of doing ad-hoc retrieval based on web assistance was introduced. For HARD track, we followed the guideline to generate clarification forms for each topic so as to experiment with user feedback and metadata. In QA, we only did the factoid experiment. The approach to QA was similar to what we have used before, except that WWW searching was added as a front-end processing. These experiments are described in Sections 2, 3 and 4 respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrunfeldKDD03.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrunfeldKDD03,
		author = {Laszlo Grunfeld and Kui{-}Lam Kwok and Norbert Dinstl and Peter Deng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2003 Robust, {HARD} and {QA} Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {510--521},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/queens-college.robust.hard.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrunfeldKDD03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HARD Experiment at Maryland: From Need Negotiation to Automated  HARD Process

_Daqing He, Dina Demner-Fushman_

- :fontawesome-solid-user-group: **Participant:** [umaryland.he](./participants.md#umaryland.he)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umaryland-he.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/umaryland-he.hard.pdf)
- :material-file-search: **Runs:** [umdbsne2tit](./runs.md#umdbsne2tit) | [UMARIPVR4](./runs.md#umaripvr4) | [UMARIPVR5](./runs.md#umaripvr5) | [UMARIPVR7](./runs.md#umaripvr7) | [UMARIPVR8](./runs.md#umaripvr8)

??? abstract "Abstract"
	
	Our aim of participating in this year's High Accuracy Retrieval from Documents (HARD) track is to explore the possibility of developing an automated HARD retrieval model by leveraging existing models and theories about information need negotiation in information science. The clarification questions we developed are related to four different aspects of search topic, and four different techniques were developed to fully use the information collected from the user through these questions. Our initial analysis of the results indicates that this is a promising approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeD03.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeD03,
		author = {Daqing He and Dina Demner{-}Fushman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{HARD} Experiment at Maryland: From Need Negotiation to Automated {HARD} Process},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {707--714},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/umaryland-he.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeD03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2003: HARD and QA

_Nasreen Abdul Jaleel, Andrés Corrada-Emmanuel, Qi Li, Xiaoyong Liu, Courtney Wade, James Allan_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umass-amherst.hard.qa.pdf](http://trec.nist.gov/pubs/trec12/papers/umass-amherst.hard.qa.pdf)
- :material-file-search: **Runs:** [ciirtpsgbas](./runs.md#ciirtpsgbas) | [ciirtbas](./runs.md#ciirtbas) | [ciirtdbas](./runs.md#ciirtdbas) | [ciirtdpsgbas](./runs.md#ciirtdpsgbas) | [ciirtrt](./runs.md#ciirtrt) | [ciirtcftt](./runs.md#ciirtcftt) | [ciirtmda](./runs.md#ciirtmda) | [ciirtp](./runs.md#ciirtp) | [ciirtmdap](./runs.md#ciirtmdap) | [ciirtmdgp](./runs.md#ciirtmdgp)

??? abstract "Abstract"
	
	The Center for Intelligent Information Retrieval (CIIR) at UMass Amherst participated in two tracks for TREC 2003: High Accuracy Retrieval from Documents (HARD) and Question Answering (QA). In the HARD track, we developed document metadata to correspond to query metadata requirements; implemented clarification forms based on query expansion, passage retrieval, and clustering; and retrieved variable length passages deemed most likely to be relevant. This work is discussed at length in Section 1. In the QA track, we focused on retrieving passages that were likely to contain the answer to the question
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JaleelCLLWA03.bib) "
	```
	@inproceedings{DBLP:conf/trec/JaleelCLLWA03,
		author = {Nasreen Abdul Jaleel and Andr{\'{e}}s Corrada{-}Emmanuel and Qi Li and Xiaoyong Liu and Courtney Wade and James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2003: {HARD} and {QA}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {715--725},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/umass-amherst.hard.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JaleelCLLWA03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2003: HARD Experiments

_Liang Ma, Wei Tan, Qunxiu Chen, Shaoping Ma, Shuicai Shi, Shibin Xiao, Hongwei Wang, Hongjun Wang_

- :fontawesome-solid-user-group: **Participant:** [tsinghuau.ma](./participants.md#tsinghuau.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/tsinghuau.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/tsinghuau.hard.pdf)
- :material-file-search: **Runs:** [TUCSHardBR1](./runs.md#tucshardbr1) | [TUCSHARD3](./runs.md#tucshard3) | [TUCSHARD1](./runs.md#tucshard1) | [TUCSHARD2](./runs.md#tucshard2)

??? abstract "Abstract"
	
	In this paper, we describe ideas and related experiments of Tsinghua University IR group in TREC-12 HARD Track. In this track, we focus on an automatic delivering mechanism, which combine the existing IR methods and can provide a quick retrieval solution for the practical environment. The final official evaluation show the old ways perform not well, but we think the experiment data will be helpful in evaluating the new ideas developed by other teams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaTCMSXWW03.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaTCMSXWW03,
		author = {Liang Ma and Wei Tan and Qunxiu Chen and Shaoping Ma and Shuicai Shi and Shibin Xiao and Hongwei Wang and Hongjun Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2003: {HARD} Experiments},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {552--555},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/tsinghuau.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MaTCMSXWW03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC-12: HARD track

_Stephen E. Robertson, Hugo Zaragoza, Michael J. Taylor_

- :fontawesome-solid-user-group: **Participant:** [microsoftc.robertson](./participants.md#microsoftc.robertson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/microsoft-cambridge.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/microsoft-cambridge.hard.pdf)
- :material-file-search: **Runs:** [MSRCbase](./runs.md#msrcbase) | [MSRCs1e1p1](./runs.md#msrcs1e1p1) | [MSRCs1e1p1B](./runs.md#msrcs1e1p1b) | [MSRCs1e0p1](./runs.md#msrcs1e0p1) | [MSRCs1e0p0](./runs.md#msrcs1e0p0) | [MSRCs9e1p1](./runs.md#msrcs9e1p1) | [MSRCs2e0p1](./runs.md#msrcs2e0p1) | [MSRCs1e0p0B](./runs.md#msrcs1e0p0b) | [MSRCs1e0p1B](./runs.md#msrcs1e0p1b) | [MSRCs9e1p0](./runs.md#msrcs9e1p0)

??? abstract "Abstract"
	
	We took part in the HARD track, with an active learning method to choose which document snippets to show the user for relevance feedback (compared to baseline feedback using snippets from the top-ranked documents). The active learning method is described, and some prior experiments with the Reuters collection are summarised. We also invited user feedback on phrases chosen from the top retrieved documents, and made some use of the ‘relt' relevant texts provided as part of the metadata. Unfortunately, our results on the HARD task were not good: in most runs, feedback hurt performance, and the active learning feedback hurt more than the baseline feedback. The only runs that improved slightly on the no-feedback runs were a couple of baseline feedback runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonZT03.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonZT03,
		author = {Stephen E. Robertson and Hugo Zaragoza and Michael J. Taylor},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Cambridge at {TREC-12:} {HARD} track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {418--425},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/microsoft-cambridge.hard.pdf},
		timestamp = {Tue, 04 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonZT03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Clairvoyance Corporation Experiments in the TREC 2003 High Accuracy  Retrieval from Douments (HARD) Track

_James G. Shanahan, Jeffrey Bennett, David A. Evans, David A. Hull, Jesse Montgomery_

- :fontawesome-solid-user-group: **Participant:** [clairvoyance.evans](./participants.md#clairvoyance.evans)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/clairvoyance.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/clairvoyance.hard.pdf)
- :material-file-search: **Runs:** [CLSTD630](./runs.md#clstd630) | [CLAI1G](./runs.md#clai1g) | [CLAI1NG](./runs.md#clai1ng) | [CLAI2NG](./runs.md#clai2ng) | [CLAI2G](./runs.md#clai2g) | [CLAI2RTNG](./runs.md#clai2rtng) | [CLAI2RTG](./runs.md#clai2rtg) | [CLAI2WRTG](./runs.md#clai2wrtg) | [CLAI2WRTNG](./runs.md#clai2wrtng) | [CLAISTDG](./runs.md#claistdg) | [CLAISTDNG](./runs.md#claistdng) | [CLAISTDRTG](./runs.md#claistdrtg) | [CLAISTDRTNG](./runs.md#claistdrtng) | [CLAISTDWRTNG](./runs.md#claistdwrtng) | [CLAISTDWRTG](./runs.md#claistdwrtg)

??? abstract "Abstract"
	
	The Clairvoyance team participated in the HARD Track, submitting fifteen runs. Our experiments focused primarily on exploiting user feedback through clarification forms for query expansion. We made limited use of the genre and related text metadata. Within the clarification form feedback framework, we explored the cluster hypothesis in the context of relevance feedback. The cluster hypothesis states that closely associated documents tend to be relevant to the same requests [Van Rijsbergen, 1979]. With this in mind we investigated the impact on performance of exploiting user feedback on groups of documents (i.e., organizing the top retrieved documents for a query into intuitive groups through agglomerative clustering or document-centric clustering), as an alternative to a ranked list of titles. This forms the basis for a new blind feedback mechanism (used to expand queries) based upon clusters of documents, as an alternative to blind feedback based upon taking the top N ranked documents, an approach that is commonly used.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShanahanBEHM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShanahanBEHM03,
		author = {James G. Shanahan and Jeffrey Bennett and David A. Evans and David A. Hull and Jesse Montgomery},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Clairvoyance Corporation Experiments in the {TREC} 2003 High Accuracy Retrieval from Douments {(HARD)} Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {152--160},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/clairvoyance.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShanahanBEHM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Active Feedback - UIUC TREC-2003 HARD Experiments

_Xuehua Shen, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uillinoisuc.zhai](./participants.md#uillinoisuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.hard.pdf)
- :material-file-search: **Runs:** [uiuchard](./runs.md#uiuchard) | [UIHARD1](./runs.md#uihard1) | [UIHARD2](./runs.md#uihard2) | [UIHARD4](./runs.md#uihard4) | [UIHARD3](./runs.md#uihard3)

??? abstract "Abstract"
	
	In this paper, we report our experiments on the HARD (High Accuracy Retrieval from Documents) Track in TREC 2003. We focus on active feedback, i.e., how to intelligently propose questions for relevance feedback in order to maximize accuracy improvement in the second run. We proposed and empirically evaluated three different methods, i.e., top-k, gapped top-k, and k-cluster centroid, to extract a fixed number of text units (e.g. passage or document) for feedback. The results show that presenting the top k documents for user feedback is often not as beneficial for learning as presenting more diversified documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShenZ03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShenZ03,
		author = {Xuehua Shen and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Active Feedback - {UIUC} {TREC-2003} {HARD} Experiments},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {662--666},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShenZ03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UB at TREC 12: HARD and Genomics Tracks

_Munirathnam Srikanth, Miguel E. Ruiz, Rohini K. Srihari_

- :fontawesome-solid-user-group: **Participant:** [unybuffalo-cedar](./participants.md#unybuffalo-cedar)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uny-buffalo.hard.genomics.pdf](http://trec.nist.gov/pubs/trec12/papers/uny-buffalo.hard.genomics.pdf)
- :material-file-search: **Runs:** [ub03ugTcugTD](./runs.md#ub03ugtcugtd) | [ub03cugTD](./runs.md#ub03cugtd) | [ub03sugT](./runs.md#ub03sugt) | [ub03smfugTD](./runs.md#ub03smfugtd)

??? abstract "Abstract"
	
	University at Buffalo (UB) participated in TREC-12 in Genomics and High Accuracy Retrieval from Documents (HARD) tracks. We explored some techniques that combine Information Retrieval and Information Extraction to perform the TREC tasks. We used an Information Extrac tion engine - InfoXtract [3] from Cymfony Inc.1 - to enhance retrieval results. For the Genomics primary task, documents retrieved using a vector space model with relevance feedback are re-weighted based on the biomedical named entities discovered by InfoXtract. For the secondary task, extracted information along with cue words for text snippets that describe functionality is used for generating GeneRIFs for given Gene name and PubMed abstract. A language modeling approach that incorporates keyword and non-keyword features are used for the HARD task. Features extracted by InfoXtract from the HARD corpus are used to rank documents and/or passages as answers to the HARD queries. Cymfony's InfoXtract [3] is a customizable Information Extraction engine that performs syntactic and semantic parsing of a document to identify features like named entities, relationships and events in them. The baseline InfoXtract engine has been trained for the general English and news domain, It can be customized to recognize new named entities like Gene Names and Gene Function. Biomedical Customization of InfoXtract is briefly presented in Section 2.2.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SrikanthRS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/SrikanthRS03,
		author = {Munirathnam Srikanth and Miguel E. Ruiz and Rohini K. Srihari},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UB} at {TREC} 12: {HARD} and Genomics Tracks},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {751--755},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uny-buffalo.hard.genomics.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SrikanthRS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Search Refinement Techniques for HARD Tasks

_Olga Vechtomova, Eric Lam, Murat Karamuftuoglu_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.vechtomova](./participants.md#uwaterloo.vechtomova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uwaterloo-olga.hard.pdf](http://trec.nist.gov/pubs/trec12/papers/uwaterloo-olga.hard.pdf)
- :material-file-search: **Runs:** [UWAThard1](./runs.md#uwathard1) | [UWAThard2](./runs.md#uwathard2) | [UWAThard3](./runs.md#uwathard3)

??? abstract "Abstract"
	
	In our entry to the new HARD track, we have investigated two methods of interactively refining user search formulations. One method consists of asking the user to select a number of sentences that may represent relevant documents, and then using the documents, whose sentences were selected for query expansion. The second method is to show to the user a list of noun phrases, extracted from the initial document set, and then expanding the query with the terms from the phrases selected by the user. The results show that the second method is an effective means of interactive query expansion and yields significant performance improvements.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VechtomovaLK03.bib) "
	```
	@inproceedings{DBLP:conf/trec/VechtomovaLK03,
		author = {Olga Vechtomova and Eric Lam and Murat Karamuftuoglu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Interactive Search Refinement Techniques for {HARD} Tasks},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {820--827},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uwaterloo-olga.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VechtomovaLK03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC12 HARD Track at ISCAS

_Zeng Wu, Lin Du, Le Sun, Shiwei Ye_

- :fontawesome-solid-user-group: **Participant:** [cipc.lin](./participants.md#cipc.lin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.hard.final2.pdf](http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.hard.final2.pdf)
- :material-file-search: **Runs:** [OPEN](./runs.md#open) | [OPEN1](./runs.md#open1)

??? abstract "Abstract"
	
	Statistical model in retrieval has been shown to perform well empirically. Extended Boolean model has been widely used in business system for its easiness to be complemented and not bad results. In this paper, a statistical model and modified Boolean model and natural language processing techniques, shallow query understanding techniques are used and results show that even with very limited training corpus, an appropriate statistical model can greatly improve the performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuDSY03.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuDSY03,
		author = {Zeng Wu and Lin Du and Le Sun and Shiwei Ye},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC12} {HARD} Track at {ISCAS}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {117--125},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.hard.final2.pdf},
		timestamp = {Fri, 21 Aug 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WuDSY03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

