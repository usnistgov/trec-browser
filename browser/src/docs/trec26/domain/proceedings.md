# Proceedings - Dynamic Domain 2017 

#### TREC 2017 Dynamic Domain Track Overview

_Grace Hui Yang, Zhiwen Tang, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-DD.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-DD.pdf)
??? abstract "Abstract"
	
	The goal of dynamic domain track is promoting the research of dynamic, exploratory search within complex information domains, where the search process is usually interactive and user's information need is also complex. Dynamic Domain (DD) track has been held in the past three years. This track's name includes two parts. “Dynamic” means the search process may contain multiple runs of iteration, and the participating system is expected to adapt its search algorithm based on the relevance feedback. “Domain” means the search task focuses on special domains, where user's information need consists of multiple aspects, and the participating system is expected to help the user explore the domain through rich interaction. This task has received great attention and this track is inspired by interested groups in government, including DARPA MEMEX program. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangTS17.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangTS17,
		author = {Grace Hui Yang and Zhiwen Tang and Ian Soboroff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2017 Dynamic Domain Track Overview},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangTS17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMD_CLIP: Using Relevance Feedback to Find Diverse Documents for  TREC Dynamic Domain 2017

_Kristine M. Rogers, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMD_CLIP](./participants.md#umd_clip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/umd_clip-DD.pdf](https://trec.nist.gov/pubs/trec26/papers/umd_clip-DD.pdf)
- :material-file-search: **Runs:** [clip_baseline](./runs.md#clip_baseline) | [clip_addwords](./runs.md#clip_addwords) | [clip_filter](./runs.md#clip_filter)

??? abstract "Abstract"
	
	The University of Maryland's participation in TREC's 2017 Dynamic Domain track focused on two types of experiments: adding new terms from passages judged as being relevant, and exclusion of terms from documents that the track's jig feedback system indicated were not relevant to the topic. The best results for iterative multi-step retrieval were obtained by restricting retrieval to documents that contained all topic terms, and then ranking those documents using terms extracted from known relevant passages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RogersO17.bib) "
	```
	@inproceedings{DBLP:conf/trec/RogersO17,
		author = {Kristine M. Rogers and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UMD{\_}CLIP: Using Relevance Feedback to Find Diverse Documents for {TREC} Dynamic Domain 2017},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/umd\_clip-DD.pdf},
		timestamp = {Sun, 14 May 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RogersO17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Reinforcement Learning Approach for Dynamic Search

_Zhiwen Tang, Grace Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [georgetown](./participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/georgetown-DD.pdf](https://trec.nist.gov/pubs/trec26/papers/georgetown-DD.pdf)
- :material-file-search: **Runs:** [galago_baseline](./runs.md#galago_baseline) | [dqn_5_actions](./runs.md#dqn_5_actions) | [dqn_semantic_state](./runs.md#dqn_semantic_state)

??? abstract "Abstract"
	
	TREC Dynamic Domain (DD) track is intended to support the research in dynamic, exploratory search within complex domains. It simulates an interactive search process where the search system is expected to improve its efficiency and effectiveness based on its interaction with the user. We propose to model the dynamic search as a reinforcement learning problem and use neural network to find the best policy during a search process. We show a great potential of deep reinforcement learning on DD track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TangY17.bib) "
	```
	@inproceedings{DBLP:conf/trec/TangY17,
		author = {Zhiwen Tang and Grace Hui Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Reinforcement Learning Approach for Dynamic Search},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/georgetown-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TangY17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at TREC 2017 Dynamic Domain Track

_Weimin Zhang, Yaokang Hu, Rongqian Jia, Xianfa Wang, Le Zhang, Yue Feng, Sihao Yu, Yuanhai Xue, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ICTNET-DD.pdf](https://trec.nist.gov/pubs/trec26/papers/ICTNET-DD.pdf)
- :material-file-search: **Runs:** [ictnet_div_qe](./runs.md#ictnet_div_qe) | [ictnet_emulti](./runs.md#ictnet_emulti) | [ictnet_fom_itr1](./runs.md#ictnet_fom_itr1) | [ictnet_params1_s](./runs.md#ictnet_params1_s) | [ictnet_params2_ns](./runs.md#ictnet_params2_ns)

??? abstract "Abstract"
	
	This track focuses on interactive search algorithms that adapt to the dynamic information needs of professional users as they explore in complex domains. [1] Unlike the common retrieval, there are two different aspects in TREC Dynamic Domain task, that we need to interact with users and retrieve in a speci c data set. The JIG program acts as users' feedback, then we use the feedback to expand the query, the different subtopics of the user feedback information are also used for the result diversi cation algorithm. In addition, we also tried to integrate a variety of ranking algorithms and deal with some detail issues. Five solutions using the above algorithm were submitted. In those submissions, one combined Suggested Queries and JIG feedback [2], one didn't use stop strategy, the others all based on the same algorithm, but with different argumentstending to improve CT or ACT.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangHJWZFYXYLC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangHJWZFYXYLC17,
		author = {Weimin Zhang and Yaokang Hu and Rongqian Jia and Xianfa Wang and Le Zhang and Yue Feng and Sihao Yu and Yuanhai Xue and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC} 2017 Dynamic Domain Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ICTNET-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangHJWZFYXYLC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

