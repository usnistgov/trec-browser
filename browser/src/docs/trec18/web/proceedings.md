# Proceedings - Web 2009 

#### Overview of the TREC 2009 Web Track

_Charles L. A. Clarke, Nick Craswell, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/WEB09.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/WEB09.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Web Track explores and evaluates Web retrieval technologies. Currently, the Web Track conducts experiments using the new billion-page ClueWeb09 collection1. The TREC 2009 track is the successor to the Terabyte Retrieval Track, which ran from 2004 to 2006, and to the older Web Track, which ran from 1999 to 2003. The TREC 2009 Web Track includes both a traditional adhoc retrieval task and a new diversity task. The goal of this diversity task is to return a ranked list of pages that together provide complete coverage for a query, while avoiding excessive redundancy in the result list. For example, given the query “windows”, a system might return the Windows update page first, followed by the Microsoft home page, and then a news article discussing the release of Windows 7. Mixed in these results might be pages providing product information on doors and windows for homes and businesses. The track used the new ClueWeb09 dataset as its document collection. The full collection consists of roughly 1 billion web pages, comprising approximately 25TB of uncompressed data (5TB compressed) in multiple languages. The dataset was crawled from the Web during January and February 2009. For groups who were unable to work with this full “Category A” dataset, the track accepted runs over the smaller ClueWeb09 “Category B” dataset, a subset of about 50 million English-language pages. Topics for the track were created from the logs of a commercial search engine, with the aid of tools developed at Microsoft Research. Given a target query, these tools extracted and analyzed groups of related queries, using co-clicks and other information, to identify clusters of queries that highlight different aspects and interpretations of the target query. These clusters were employed by NIST for topic development. Each resulting topic is structured as a representative set of subtopics, each related to a different user need. Documents were judged with respect to the subtopics, as well as with respect to the topic as a whole. For each subtopic, NIST assessors made a binary judgment as to whether or not the document satisfies the information need associated with the subtopic. These topics were used for both the adhoc task and the diversity task. For both tasks, partici- pants executed the original target queries over the ClueWeb09 collection. The tasks differ primarily in their evaluation measures. The adhoc task uses an estimate of mean average precision, based on overall topical relevance [3]. The diversity task uses newer measures, based on the subtopics, which explicitly consider novelty in the result list (intent aware precision [1] and alpha-nDCG [4]) A total of 26 groups submitted runs to the track, with many groups participating in both tasks. Table 1 summarizes the participation of these groups. About half the groups worked with the full collection. A few groups submitted runs over both the full (Category A) collection and the Category B collection. This report provides an overview of the track, including topic development, evaluation measures, and results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCS09,
		author = {Charles L. A. Clarke and Nick Craswell and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2009 Web Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/WEB09.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2009 Diversity Track

_Wenjing Bi, Xiaoming Yu, Yue Liu, Feng Guan, Zeying Peng, Hongbo Xu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB-DIV.pdf](http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB-DIV.pdf)
- :material-file-search: **Runs:** [ICTNETDivR1](./runs.md#ictnetdivr1) | [ICTNETDivR3](./runs.md#ictnetdivr3) | [ICTNETADRun3](./runs.md#ictnetadrun3) | [ICTNETDivR2](./runs.md#ictnetdivr2) | [ICTNETADRun4](./runs.md#ictnetadrun4) | [ICTNETADRun5](./runs.md#ictnetadrun5)

??? abstract "Abstract"
	
	We (ICTNET team) participated in Web Track of TREC2009, and in this paper, we summarize our work on Diversity task of Web Track, which is new in this year. The goal of the diversity task is to return a ranked list of pages that together provide complete coverage for a query, while avoiding excessive redundancy in the result list. For this task, we cluster the results of ad hoc task, and rerank the results depend on subtopics docs covers. Besides, we introduce two methods which tried to find the implicit subtopic by using the docs returned from commerce search engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BiYLGPXC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/BiYLGPXC09,
		author = {Wenjing Bi and Xiaoming Yu and Yue Liu and Feng Guan and Zeying Peng and Hongbo Xu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2009 Diversity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB-DIV.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BiYLGPXC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad Hoc and Diversity Retrieval at the University of Delaware

_Praveen Chandar, Aparna Kailasam, Divya Muppaneni, Sree Lekha Thota, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [UDel](./participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf)
- :material-file-search: **Runs:** [udelIndDMRM](./runs.md#udelinddmrm) | [udelIndDRSP](./runs.md#udelinddrsp) | [udelSimPrune](./runs.md#udelsimprune) | [udelFMWG](./runs.md#udelfmwg) | [udelIndDRPR](./runs.md#udelinddrpr) | [udelFMRM](./runs.md#udelfmrm)

??? abstract "Abstract"
	
	This is the report on the University of Delaware Information Retrieval Lab's participation in the TREC 2009 Web and Million Query tracks. Our report on the Relevance Feedback track is in a separate document [3].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChandarKMTC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChandarKMTC09,
		author = {Praveen Chandar and Aparna Kailasam and Divya Muppaneni and Sree Lekha Thota and Ben Carterette},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ad Hoc and Diversity Retrieval at the University of Delaware},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.WEB.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChandarKMTC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Machine Learning for Information Retrieval: TREC 2009 Web, Relevance  Feedback and Legal Tracks

_Gordon V. Cormack, Mona Mojdeh_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf)
- :material-file-search: **Runs:** [watd1](./runs.md#watd1) | [watd3](./runs.md#watd3) | [watd5](./runs.md#watd5) | [watwp](./runs.md#watwp) | [watrrfw](./runs.md#watrrfw) | [uwgym](./runs.md#uwgym) | [watprf](./runs.md#watprf)

??? abstract "Abstract"
	
	For the TREC 2009, we exhaustively classified every document in each corpus, using machine learning methods that had previously been shown to work well for email spam [9, 3]. We treated each document as a sequence of bytes, with no tokenization or parsing of tags or meta-information. This approach was used exclusively for the adhoc web, diversity and relevance feedback tasks, as well as to the batch legal task: the ClueWeb09 and Tobacco collections were processed end-to-end and never indexed. We did the interactive legal task in two phases: first, we used interactive search and judging to find a large and diverse set of training examples; then we used active learning process, similar to what we used for the other tasks, to find find more relevant documents. Finally, we fitted a censored (i.e. truncated) mixed normal distribution to estimate recall and the cutoff to optimize F1, the principal effectiveness measure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackM09,
		author = {Gordon V. Cormack and Mona Mojdeh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Machine Learning for Information Retrieval: {TREC} 2009 Web, Relevance Feedback and Legal Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research at TREC 2009: Web and Relevance Feedback Track

_Nick Craswell, Dennis Fetterly, Marc Najork, Stephen Robertson, Emine Yilmaz_

- :fontawesome-solid-user-group: **Participant:** [msrc](./participants.md#msrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf)
- :material-file-search: **Runs:** [MS1](./runs.md#ms1) | [MS2](./runs.md#ms2) | [MSDiv2](./runs.md#msdiv2) | [MSDiv1](./runs.md#msdiv1) | [MSDiv3](./runs.md#msdiv3)

??? abstract "Abstract"
	
	We took part in the Web and Relevance Feedback tracks, using the ClueWeb09 corpus. To process the corpus, we developed a parallel processing pipeline which avoids the generation of an inverted file. We describe the components of the parallel architecture and the pipeline and how we ran the TREC experiments, and we present effectiveness results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellFNRY09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellFNRY09,
		author = {Nick Craswell and Dennis Fetterly and Marc Najork and Stephen Robertson and Emine Yilmaz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research at {TREC} 2009: Web and Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellFNRY09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRRA at TREC 2009: Index Term Weighting Based on Divergence From  Independence Model

_Bekir Taner Dinçer, Ilker Kocabas, Bahar Karaoglan_

- :fontawesome-solid-user-group: **Participant:** [IRRA](./participants.md#irra)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf](http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf)
- :material-file-search: **Runs:** [irra1a](./runs.md#irra1a) | [irra2a](./runs.md#irra2a) | [irra3a](./runs.md#irra3a) | [irra1d](./runs.md#irra1d) | [irra2d](./runs.md#irra2d) | [irra3d](./runs.md#irra3d)

??? abstract "Abstract"
	
	IRRA (IR-Ra) group participated in the 2009 Web track (both adhoc task and diversity task) and the Million Query track. In this year, the major concern is to examine the effectiveness of a novel, nonparametric index term weighting model, divergence from independence (DFI). The notion of independence, which is the notion behind the well-known statistical exploratory data analysis technique called the correspondence analysis (Greenacre, 1984; Jambu, 1991), can be adapted to the index term weighting problem. In this respect, it can be thought of as a qualitative description of the importance of terms for documents, in which they appear, importance in the sense of contribution to the information contents of documents relative to other terms. According to the independence notion, if the ratios of the frequencies of two different terms are the same across documents, they are independent from documents. For example, each Web page contains a pair of “html” and a pair of “body” tags, so that the ratio of frequencies of these tags is the same across all Web pages, indicating that the “html” and “body” tags are independent from Web pages. They are used by design, irrespective of the information contents of Web pages. On the other hand, some tags, such as “image”, “table”, which are also independent from Web pages, may occur less or more in some pages than the expected frequencies suggested by the independence model; so, their associated frequency ratios may not be the same for all Web pages. However, it is reasonable to expect that, if the pages are not about the tags' usage, such as a “HTML Handbook”, frequencies of those tags should not be significantly different from their expected frequencies: they should be close to the expectation, i.e., in a parametric point of view, their observed frequencies on individual documents should be attributed to chance fluctuation. Although this tag example is helpful in exemplifying the use of independence notion, it is obvious that the tags are artificial, and so, governed by some rules completely different from the rules of a spoken language. Nonetheless, some words, like the ones in a common “stopwords list”, appear in documents, not because of their contribution to the information contents of documents, but because of the grammatical rules. On this account, such words can be modeled as if they were tags, because they are independent from documents in the same manner. Their observed frequencies in individual documents is expected to fluctuate around their frequencies expected under independence, as in the case of tags. Content bearing words are, therefore, the words whose frequencies highly diverge from the frequencies expected under independence. The results of the TREC experiments about IRRA runs show that the independence notion promises a natural basis for quantifying the categorical relationships between the terms and the documents. The TERRIER retrieval platform (Ounis et al., 2007) is used to index and search the ClueWeb09-T09B1 data set, a subset of about 50 million Web pages in English (TREC 2009 “Category B” data set). During indexing and searching, terms are stemmed and a particular set of stop words2 are eliminated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DincerKK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/DincerKK09,
		author = {Bekir Taner Din{\c{c}}er and Ilker Kocabas and Bahar Karaoglan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRRA} at {TREC} 2009: Index Term Weighting Based on Divergence From Independence Model},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/muglau.WEB.MQ.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DincerKK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research Asia at the Web Track of TREC 2009

_Zhicheng Dou, Kun Chen, Ruihua Song, Yunxiao Ma, Shuming Shi, Ji-Rong Wen_

- :fontawesome-solid-user-group: **Participant:** [MSRAsia](./participants.md#msrasia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/microsoft-asia.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/microsoft-asia.WEB.pdf)
- :material-file-search: **Runs:** [MSRANORM](./runs.md#msranorm) | [MSRAAF](./runs.md#msraaf) | [MSRAC](./runs.md#msrac) | [MSRABASE](./runs.md#msrabase) | [MSRACS](./runs.md#msracs) | [MSRAACSF](./runs.md#msraacsf)

??? abstract "Abstract"
	
	In TREC 2009, we participate in the Web track, and focus on the diversity task. We propose to diversify web search results by first mining subtopics, and then rank results based on mined subtopics. We propose a model to diversify search results by considering both relevance of documents and richness of mined subtopics. Our experimental results show that the model improves diversity of search results in terms of α-NDCG, and combining subtopics from multiple data sources helps further improve result diversity.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DouCSMSW09.bib) "
	```
	@inproceedings{DBLP:conf/trec/DouCSMSW09,
		author = {Zhicheng Dou and Kun Chen and Ruihua Song and Yunxiao Ma and Shuming Shi and Ji{-}Rong Wen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research Asia at the Web Track of {TREC} 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/microsoft-asia.WEB.pdf},
		timestamp = {Tue, 01 Dec 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DouCSMSW09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2009: Web Track

_Steven Garcia_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/rmit.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/rmit.WEB.pdf)
- :material-file-search: **Runs:** [RmitLm](./runs.md#rmitlm) | [RmitOkapi](./runs.md#rmitokapi) | [RmitDiv](./runs.md#rmitdiv)

??? abstract "Abstract"
	
	RMIT participated in the 2009 Web Track tasks. Our submissions utilised the Zettair search engine1 to index and search the Category B subset of the ClueWeb collection used by the Web Track. The Web Track was composed of two tasks, a traditional adhoc retrieval task, and a new diversity task where participants attempted to retrieve documents covering a range of sub topics for each query. Sub topics were not provided with the queries. Our experiments utilised the well known measures Okapi BM25 and language modeling with Dirichlet smoothing for the adhoc task. For the diversity task we attempted to improve the diversity of query results by minimising the number of documents returned for a single domain.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Garcia09.bib) "
	```
	@inproceedings{DBLP:conf/trec/Garcia09,
		author = {Steven Garcia},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2009: Web Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/rmit.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Garcia09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2009 Ad-hoc Task

_Feng Guan, Xiaoming Yu, Zeying Peng, Hongbo Xu, Yue Liu, Linhai Song, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB.pdf)
- :material-file-search: **Runs:** [ICTNETDivR1](./runs.md#ictnetdivr1) | [ICTNETDivR3](./runs.md#ictnetdivr3) | [ICTNETADRun3](./runs.md#ictnetadrun3) | [ICTNETDivR2](./runs.md#ictnetdivr2) | [ICTNETADRun4](./runs.md#ictnetadrun4) | [ICTNETADRun5](./runs.md#ictnetadrun5)

??? abstract "Abstract"
	
	This paper is about the work done for ad-hoc task of TREC 2009 Web Track. We introduce three methods for this task, including two improved BM25 models and query expansion. The results of these models indicate that both minimum window and query expansion could improve BM25 model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuanYPXLSC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuanYPXLSC09,
		author = {Feng Guan and Xiaoming Yu and Zeying Peng and Hongbo Xu and Yue Liu and Linhai Song and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2009 Ad-hoc Task},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ictnet.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuanYPXLSC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Twente @ TREC 2009: Indexing Half a Million Web Pages

_Claudia Hauff, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [utwente](./participants.md#utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf)
- :material-file-search: **Runs:** [twCSrs9N](./runs.md#twcsrs9n) | [twCSrsR](./runs.md#twcsrsr) | [twJ48rsU](./runs.md#twj48rsu) | [twCSodpRNB](./runs.md#twcsodprnb) | [twCSodpRBB](./runs.md#twcsodprbb)

??? abstract "Abstract"
	
	The University of Twente participated in three tasks of TREC 2009: the adhoc task, the diversity task and the relevance feedback task. All experiments are performed on the English part of ClueWeb09. We describe our approach to tuning our retrieval system in absence of training data in Section 3. We describe the use of categories and a query log for diversifying search results in Section 4. Section 5 describes preliminary results for the relevance feedback task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HauffH09.bib) "
	```
	@inproceedings{DBLP:conf/trec/HauffH09,
		author = {Claudia Hauff and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Twente @ {TREC} 2009: Indexing Half a Million Web Pages},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HauffH09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Heuristic Ranking and Diversification of Web Documents

_Jiyin He, Krisztian Balog, Katja Hofmann, Edgar Meij, Maarten de Rijke, Manos Tsagkias, Wouter Weerkamp_

- :fontawesome-solid-user-group: **Participant:** [UAms](./participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.WEB.pdf)
- :material-file-search: **Runs:** [uvaee](./runs.md#uvaee) | [uvamrf](./runs.md#uvamrf) | [uvamrftop](./runs.md#uvamrftop) | [uvaaol](./runs.md#uvaaol) | [spc](./runs.md#spc) | [tm](./runs.md#tm)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's Intelligent Systems Lab in the web track at TREC 2009. We participated in the adhoc and diversity task. We find that spam is an important issue in the ad hoc task and that Wikipedia-based heuristic optimization approaches help to boost the retrieval performance, which is assumed to potentially reduce spam in the top ranked results. As for the diversity task, we explored different methods. Clustering and a topic model-based approach have a similar performance and both are relatively better than a query log based approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeBHMRTW09.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeBHMRTW09,
		author = {Jiyin He and Krisztian Balog and Katja Hofmann and Edgar Meij and Maarten de Rijke and Manos Tsagkias and Wouter Weerkamp},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Heuristic Ranking and Diversification of Web Documents},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeBHMRTW09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Result Diversity and Entity Ranking Experiments: Anchors, Links, Text  and Wikipedia

_Rianne Kaptein, Marijn Koolen, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [Amsterdam](./participants.md#amsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf)
- :material-file-search: **Runs:** [UamsAwebQE10](./runs.md#uamsawebqe10) | [UamsDancTFb1](./runs.md#uamsdanctfb1) | [UamsDwebLFou](./runs.md#uamsdweblfou) | [UamsDwQE10TF](./runs.md#uamsdwqe10tf) | [UamsAw7an3](./runs.md#uamsaw7an3)

??? abstract "Abstract"
	
	In this paper, we document our efforts in participating to the TREC 2009 Entity Ranking and Web Tracks. We had multiple aims: For the Web Track's Adhoc task we experiment with document text and anchor text representation, and the use of the link structure. For the Web Track's Diversity task we experiment with using a top down sliding window that, given the top ranked documents, chooses as the next ranked document the one that has the most unique terms or links. We test our sliding window method on a standard document text index and an index of propagated anchor texts. We also experiment with extreme query expansions by taking the top n results of the initial ranking as multi-faceted aspects of the topic to construct n relevance models to obtain n sets of results. A final diverse set of results is obtained by merging the n results lists. For the Entity Ranking Track, we also explore the effectiveness of the anchor text representation, look at the co-citation graph, and experiment with using Wikipedia as a pivot. Our main findings can be summarized as follows: Anchor text is very effective for diversity. It gives high early precision and the results cover more relevant sub-topics than the document text index. Our baseline runs have low diversity, which limits the possible impact of the sliding window approach. New link information seems more effective for diversifying text-based search results than the amount of unique terms added by a document. In the entity ranking task, anchor text finds few primary pages , but it does retrieve a large number of relevant pages. Using Wikipedia as a pivot results in large gains of P10 and NDCG when only primary pages are considered. Although the links between the Wikipedia entities and pages in the Clueweb collection are sparse, the precision of the existing links is very high.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KapteinKK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/KapteinKK09,
		author = {Rianne Kaptein and Marijn Koolen and Jaap Kamps},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Result Diversity and Entity Ranking Experiments: Anchors, Links, Text and Wikipedia},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KapteinKK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2009 Web Track: Finding Relevant and Diverse Results  for Large Scale Web Search

_Zhichao Li, Fei Chen, Qianli Xing, Junwei Miao, Yufei Xue, Tong Zhu, Bo Zhou, Rongwei Cen, Yiqun Liu, Min Zhang, Yijiang Jin, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [THUIR](./participants.md#thuir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/tsinghuau.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/tsinghuau.WEB.pdf)
- :material-file-search: **Runs:** [THUIR09An](./runs.md#thuir09an) | [THUIR09TxAn](./runs.md#thuir09txan) | [THUIR09LuTA](./runs.md#thuir09luta) | [THUIR09QeDiv](./runs.md#thuir09qediv) | [THUIR09FuClu](./runs.md#thuir09fuclu) | [THUIR09AbClu](./runs.md#thuir09abclu)

??? abstract "Abstract"
	
	This is the 8th year that IR group of Tsinghua University (THUIR) participates in TREC. This year we focus on Web track, which contains two tasks, namely ad hoc and diversity. On ad hoc task, we improved the efficiency of our distributed retrieval system TMiner to handle terabytes of Web data. Then three studies have been done, namely page quality estimation, ranking feature analysis, and model comparison. On diversity task, we proposed several new approaches on searching strategy, user intention detection, and duplication elimination. To mine user‟s intention, we proposed and compared two different strategies, namely „searching + content-based diversity‟ which is a kind of result clustering, and „user based diverse intention prediction + searching‟ which is in the branch of query expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiCXMXZZCLZJM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiCXMXZZCLZJM09,
		author = {Zhichao Li and Fei Chen and Qianli Xing and Junwei Miao and Yufei Xue and Tong Zhu and Bo Zhou and Rongwei Cen and Yiqun Liu and Min Zhang and Yijiang Jin and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2009 Web Track: Finding Relevant and Diverse Results for Large Scale Web Search},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/tsinghuau.WEB.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiCXMXZZCLZJM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCD SIFT in the TREC 2009 Web Track

_David Lillis, Fergus Toolan, Ling Lin, Rem W. Collier, John Dunnion_

- :fontawesome-solid-user-group: **Participant:** [CSIUCD](./participants.md#csiucd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ucollege-dublin.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/ucollege-dublin.WEB.pdf)
- :material-file-search: **Runs:** [UCDSIFTslide](./runs.md#ucdsiftslide) | [UCDSIFTinter](./runs.md#ucdsiftinter) | [UCDSIFTprob](./runs.md#ucdsiftprob) | [UCDSIFTdiv](./runs.md#ucdsiftdiv)

??? abstract "Abstract"
	
	The SIFT (SIFT Information Fusion Techniques) group in UCD is dedicated to researching Data Fusion in Information Retrieval. This area of research involves the merging of multiple sets of results into a single result set that is presented to the user. As a means of evaluating the effectiveness of this work, the group entered Category B of the TREC 2009 Web Track. This paper discusses the strategies and experiments employed by the UCD SIFT group in entering the TREC Web Track 2009. This involved the use of freely-available Information Retrieval tools to provide inputs to the data fusion process, with the aim of contrasting with more sophisticated systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LillisTLCD09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LillisTLCD09,
		author = {David Lillis and Fergus Toolan and Ling Lin and Rem W. Collier and John Dunnion},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCD} {SIFT} in the {TREC} 2009 Web Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ucollege-dublin.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LillisTLCD09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Of Ivory and Smurfs: Loxodontan MapReduce Experiments for Web Search

_Jimmy Lin, Tamer Elsayed, Lidan Wang, Donald Metzler_

- :fontawesome-solid-user-group: **Participant:** [UMD](./participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/umd-yahoo.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/umd-yahoo.WEB.pdf)
- :material-file-search: **Runs:** [UMHOObm25GS](./runs.md#umhoobm25gs) | [UMHOObm25IF](./runs.md#umhoobm25if) | [UMHOObm25B](./runs.md#umhoobm25b) | [UMHOOsd](./runs.md#umhoosd) | [UMHOOsdp](./runs.md#umhoosdp) | [UMHOOqlB](./runs.md#umhooqlb) | [UMHOOqlGS](./runs.md#umhooqlgs) | [UMHOOqlIF](./runs.md#umhooqlif)

??? abstract "Abstract"
	
	This paper describes Ivory, an attempt to build a distributed retrieval system around the open-source Hadoop implementation of MapReduce. We focus on three noteworthy aspects of our work: a retrieval architecture built directly on the Hadoop Distributed File System (HDFS), a scalable MapReduce algorithm for inverted indexing, and webpage classification to enhance retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinEWM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinEWM09,
		author = {Jimmy Lin and Tamer Elsayed and Lidan Wang and Donald Metzler},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Of Ivory and Smurfs: Loxodontan MapReduce Experiments for Web Search},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/umd-yahoo.WEB.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinEWM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2009: Experiments with Terrier

_Richard McCreadie, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf)
- :material-file-search: **Runs:** [uogTrdphP](./runs.md#uogtrdphp) | [uogTrdphCEwP](./runs.md#uogtrdphcewp) | [uogTrdphA](./runs.md#uogtrdpha) | [uogTrDYScdA](./runs.md#uogtrdyscda) | [uogTrDYCcsB](./runs.md#uogtrdyccsb) | [uogTrDPCQcdB](./runs.md#uogtrdpcqcdb)

??? abstract "Abstract"
	
	In TREC 2009, we extend our Voting Model for the faceted blog distillation, top stories identification, and related entity finding tasks. Moreover, we experiment with our novel xQuAD framework for search result diversification. Besides fostering our research in mul- tiple directions, by participating in such a wide portfolio of tracks, we further develop the indexing and retrieval capabilities of our Terrier Information Retrieval platform, to effectively and efficiently cope with a new generation of large-scale test collections.
	

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

#### Lucene for n-grams using the CLUEWeb Collection

_Gregory B. Newby, Christopher T. Fallen, Kylie McCormick_

- :fontawesome-solid-user-group: **Participant:** [ARSC09](./participants.md#arsc09)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/arsc.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/arsc.WEB.pdf)
- :material-file-search: **Runs:** [arsc09web](./runs.md#arsc09web)

??? abstract "Abstract"
	
	The ARSC team made modifications to the Apache Lucene engine to accommodate “go words,” taken from the Google Gigaword vocabulary of n-grams. Indexing the Category “B” subset of the ClueWeb collection was accomplished by a divide and conquer method, working across the separate ClueWeb subsets for 1, 2 and 3-grams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NewbyFM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/NewbyFM09,
		author = {Gregory B. Newby and Christopher T. Fallen and Kylie McCormick},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Lucene for n-grams using the CLUEWeb Collection},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/arsc.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NewbyFM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Northeastern University in the TREC 2009 Web Track

_Shahzad Rajput, Evangelos Kanoulas, Virgiliu Pavlu, Javed A. Aslam_

- :fontawesome-solid-user-group: **Participant:** [NEU](./participants.md#neu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/northeasternu.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/northeasternu.WEB.pdf)
- :material-file-search: **Runs:** [NeuLMWebBase](./runs.md#neulmwebbase) | [NeuLMWeb600](./runs.md#neulmweb600) | [NeuLMWeb300](./runs.md#neulmweb300) | [NeuDiv1](./runs.md#neudiv1) | [NeuRRWeb300](./runs.md#neurrweb300) | [NeuDivW75](./runs.md#neudivw75)

??? abstract "Abstract"
	
	In a typical retrieval scenario a user poses a query to a retrieval system in order to satisfy an information need generated during some task the user is undertaking. Retrieval systems access an underline collection of searchable material and rank them according to some definition of relevance of the material to the users request and returns this ranked list to the user. In the case of web search where typical users express their information needs by 2-3 keywords submitted queries often time have ambiguous meanings, representing more than one information need. Given a query, a good retrieval system should be able to satisfy all possible users by ranking documents in a way that their content covers as many information needs as possible. The primary goal of our Web Track submission is to explore whether named entity tags can be utilized to diversify the returned ranked list of documents. Our hypothesis is that each information need could be represented by a certain named entity tag (or certain combination of them). For instance, in Table 1 one can see the example query taken from the Web Track web page. The query is “physical therapists”. The subtopics that correspond to this query are listed in the left column of the table. To illustrate our hypothesis, next to each subtopic, in bold, we have manually identified a possible combination of entity tags that could represent each subtopic/information need. Further, each document relevant to the original query could also be represented by a set of named entity tags. Instead of attempting to diversify documents based on the distance of their language models over text, we explored whether it is possible to diversify them according to the distance of their language model over entity tags. Entity tags could allow a further abstraction of documents avoiding issues like language mismatch. Our methodology highly depended on two assumptions: (1) retrieval methods based on a bug-of-words representation can retrieve many relevant documents in the top 2,000 positions, and (2) the relevant documents would be diverse enough at the first place. Then using our methodology we could abstract the representation of those documents and diversify the list based on their tag distributions. A second goal of our Web Track submission was to develop a simple spam filter. By analyzing a small subset of the documents, selected at random from the top 2,000 documents ranked by Indri language model per query over the new ClueWeb09 collection (category B) 1, we observed that 44.5% of them were spam. A large subset of the spam documents were those that contained query terms way too many times. For this purpose, we decided to develop a simple spam filter to remove these documents from the ranked list.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RajputKPA09.bib) "
	```
	@inproceedings{DBLP:conf/trec/RajputKPA09,
		author = {Shahzad Rajput and Evangelos Kanoulas and Virgiliu Pavlu and Javed A. Aslam},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Northeastern University in the {TREC} 2009 Web Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/northeasternu.WEB.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RajputKPA09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PARADISE Based Search Engine at TREC 2009 Web Track

_Dongdong Shan, Dongsheng Zhao, Jing He, Hongfei Yan_

- :fontawesome-solid-user-group: **Participant:** [pku2009](./participants.md#pku2009)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/pekingu.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/pekingu.WEB.pdf)
- :material-file-search: **Runs:** [pkuSewmTp](./runs.md#pkusewmtp) | [pkuStruct](./runs.md#pkustruct) | [pkuLink](./runs.md#pkulink)

??? abstract "Abstract"
	
	In this paper, we introduce the PARADISE search engine in TREC09 Web track. PARADISE is the abbreviation for Platform for Applying, Research and Developing Intelligent Search Engine, which is a search engine platform developed by SEWM group, Peking University. The system is designed to support both English and Chinese information retrieval. This system preprocessed and indexed the five hundred million web pages for this year's Web Track. In the preprocessing stage, the templates were removed, the encoding were identified and unified, and the anchor texts and InLink information are extracted with the mapreduce framework (using Hadoop in this system). In retrieval, our runs used an extension of BM25. This model distinguishes terms from different fields and integrated both term counts and position information. Furthermore, some web based features are also considered.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShanZHY09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShanZHY09,
		author = {Dongdong Shan and Dongsheng Zhao and Jing He and Hongfei Yan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PARADISE} Based Search Engine at {TREC} 2009 Web Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/pekingu.WEB.pdf},
		timestamp = {Mon, 15 May 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ShanZHY09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with ClueWeb09: Relevance Feedback and Web Tracks

_Mark D. Smucker, Charles L. A. Clarke, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf)
- :material-file-search: **Runs:** [WatSklq](./runs.md#watsklq) | [WatSklfu](./runs.md#watsklfu) | [WatSklfb](./runs.md#watsklfb) | [WatSdmrm3](./runs.md#watsdmrm3) | [WatSql](./runs.md#watsql) | [WatSdmrm3we](./runs.md#watsdmrm3we)

??? abstract "Abstract"
	
	In this paper, we report on our TREC experiments with the ClueWeb09 document collection. We participated in the relevance feedback and web tracks. While our phase 1 relevance feedback run's performance was good, our other relevance feedback and web track submissions' performances were lacking. We suspect this performance difference is caused by the Category B document subset of the ClueWeb09 collection having a higher prior probability of relevance than the rest of the collection. Future work will involve a more detailed error analysis of our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmuckerCC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmuckerCC09,
		author = {Mark D. Smucker and Charles L. A. Clarke and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with ClueWeb09: Relevance Feedback and Web Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmuckerCC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Diversifying Search Results with Popular Subtopics

_Dawei Yin, Zhenzhen Xue, Xiaoguang Qi, Brian D. Davison_

- :fontawesome-solid-user-group: **Participant:** [LU_WUME](./participants.md#lu_wume)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/lehighu.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/lehighu.WEB.pdf)
- :material-file-search: **Runs:** [wume1](./runs.md#wume1) | [wume2](./runs.md#wume2)

??? abstract "Abstract"
	
	This paper describes the method we use in the diversity task of web track in TREC 2009. The problem we aim to solve is the diversification of search results for ambiguous web queries. We present a model based on knowledge of the diversity of query subtopics to generate a diversified ranking for retrieved documents. We expand the original query into several related queries, assuming that query expansions expose subtopics of the original query. Moreover, each query expansion is given a weight which reflects the likelihood of the interpretation (the fraction of users who issued this query given the general query topic). We issue all those expanded queries including the original query to a standard BM25 search engine, then re-rank the retrieved documents to generate the final ranking. Our method can detect possible subtopics of a given query and provide a reasonable ranking that satisfies both relevancy and diversity metrics. The TREC evaluations show our method is effective on the diversity task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YinXQD09.bib) "
	```
	@inproceedings{DBLP:conf/trec/YinXQD09,
		author = {Dawei Yin and Zhenzhen Xue and Xiaoguang Qi and Brian D. Davison},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Diversifying Search Results with Popular Subtopics},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/lehighu.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YinXQD09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Axiomatic Approaches to Information Retrieval–University of Delaware  at TREC 2009 Million Query and Web Tracks

_Wei Zheng, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [EceUdel](./participants.md#eceudel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf)
- :material-file-search: **Runs:** [UDWAxQEWeb](./runs.md#udwaxqeweb) | [UDWAxQE](./runs.md#udwaxqe) | [UDWAxBL](./runs.md#udwaxbl)

??? abstract "Abstract"
	
	We report our experiments in TREC 2009 Million Query track and Adhoc task of Web track. Our goal is to evaluate the effectiveness of axiomatic retrieval models on the large data collection. Axiomatic approaches to information retrieval have been recently proposed and studied. The basic idea is to search for retrieval functions that can satisfy all the reasonable retrieval constraints. Previous studies showed that the derived basic axiomatic retrieval functions are less sensitive to the parameters than the other state of the art retrieval functions with comparable optimal performance. In this paper, we focus on evaluating the effectiveness of the basic axiomatic retrieval functions as well as the semantic term matching based query expansion strategy. Experiment results of the two tracks demonstrate the effectiveness of the axiomatic retrieval models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengF09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengF09,
		author = {Wei Zheng and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Axiomatic Approaches to Information Retrieval--University of Delaware at {TREC} 2009 Million Query and Web Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.MQ.WEB.pdf},
		timestamp = {Tue, 20 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengF09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

