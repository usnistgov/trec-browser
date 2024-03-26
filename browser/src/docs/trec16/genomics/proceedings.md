# Proceedings - Genomics 2007 

#### TREC 2007 Genomics Track Overview

_William R. Hersh, Aaron M. Cohen, Lynn Ruslen, Phoebe M. Roberts_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/GEO.OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/GEO.OVERVIEW16.pdf)
??? abstract "Abstract"
	
	The TREC 2007 Genomics Track employed an entity-based question-answering task. Runs were required to nominate passages of text from a collection of full-text biomedical journal articles to answer the topic questions. Systems were assessed not only for the relevance of passages retrieved, but also how many aspects (entities) of the topic were covered and how many relevant documents were retrieved. We also classified the features of runs to explore which ones were associated with better performance, although the diversity of approaches and the quality of their reporting prevented definitive conclusions from being drawn.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershCRR07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershCRR07,
		author = {William R. Hersh and Aaron M. Cohen and Lynn Ruslen and Phoebe M. Roberts},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 Genomics Track Overview},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/GEO.OVERVIEW16.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershCRR07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The OHSU Biomedical Question Answering System Framework

_Aaron M. Cohen, Jianji Yang, Seeger Fisher, Brian Roark, William R. Hersh_

- :fontawesome-solid-user-group: **Participant:** [ohsu.hersh](./participants.md#ohsu.hersh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ohsu.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ohsu.geo.final.pdf)
- :material-file-search: **Runs:** [OHSUQASUBEX](./runs.md#ohsuqasubex) | [OHSUQASUB](./runs.md#ohsuqasub) | [OHSUQA](./runs.md#ohsuqa)

??? abstract "Abstract"
	
	The Oregon Health & Science University submission to the TREC 2007 Genomics Track approached the entity list question answering task using a modular object oriented system framework. A system object coordinates a collection of processing objects into a pipe that constructs a set of queries, retrieves passage, and then processes those passages into a final output answer set. Using the framework we applied multiple levels of synonym expansion and a ranked series of topic queries with a range of specificities in order to retrieve all of the likely relevant passages with the most likely ranked higher. We then applied sentence pruning to the head and tail of each passage using both NLP and term-based techniques. Overall scores finished around the TREC Genomics mean for each of the four measures. Careful passage retrieval, including synonym expansion and multiple query construction, as well as sentence pruning was essential in achieving acceptable performance on this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CohenYFRH07.bib) "
	```
	@inproceedings{DBLP:conf/trec/CohenYFRH07,
		author = {Aaron M. Cohen and Jianji Yang and Seeger Fisher and Brian Roark and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {OHSU} Biomedical Question Answering System Framework},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ohsu.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CohenYFRH07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Resources to Find Answers to Biomedical Questions

_Dina Demner-Fushman, Susanne M. Humphrey, Nicholas C. Ide, Russell F. Loane, James G. Mork, Patrick Ruch, Miguel E. Ruiz, Lawrence H. Smith, W. John Wilbur, Alan R. Aronson_

- :fontawesome-solid-user-group: **Participant:** [nlm.aronson](./participants.md#nlm.aronson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/nlm.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/nlm.geo.final.pdf)
- :material-file-search: **Runs:** [LHNCBC](./runs.md#lhncbc) | [NLMfusion](./runs.md#nlmfusion) | [NLMinter](./runs.md#nlminter)

??? abstract "Abstract"
	
	One of the NLM experimental approaches to the 2007 Genomics track question answering task followed the track evaluation design: we attempted identifying exact answers in the form of semantic relations between biomedical entities named in questions and the potential answer types and then marked the passages containing the relations as containing the answers. The goal of this knowledge-based approach was to improve the answer precision. To boost recall, evidence obtained through relation extraction was combined with passage scores obtained by semantic filtering and passage retrieval. Our second approach, the fusion of retrieval results of several search engines established to be reliably successful in the past, was used as the baseline, which ultimately was not improved upon by the knowledge-based approach. The impact of the relevance of whole documents on finding passages containing answers was tested in the third approach, an interactive retrieval experiment, in which the relevance of a document was determined by virtue of its retrieval in an expert PubMed search and an occasional examination of its abstract. This relatively moderately labor-intensive approach significantly improved the fusion retrieval results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Demner-FushmanHILMRRSWA07.bib) "
	```
	@inproceedings{DBLP:conf/trec/Demner-FushmanHILMRRSWA07,
		author = {Dina Demner{-}Fushman and Susanne M. Humphrey and Nicholas C. Ide and Russell F. Loane and James G. Mork and Patrick Ruch and Miguel E. Ruiz and Lawrence H. Smith and W. John Wilbur and Alan R. Aronson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Resources to Find Answers to Biomedical Questions},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/nlm.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Demner-FushmanHILMRRSWA07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IR-Specific Searches at TREC 2007: Genomics & Blog Experiments

_Claire Fautsch, Jacques Savoy_

- :fontawesome-solid-user-group: **Participant:** [uneuchatel.savoy](./participants.md#uneuchatel.savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf)
- :material-file-search: **Runs:** [UniNE1](./runs.md#unine1) | [UniNE2](./runs.md#unine2) | [UniNE3](./runs.md#unine3)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2007 Genomics and Blog evaluation campaigns. Within these two tracks, our main intent is to go beyond simple document retrieval, using different search and filtering strategies to obtain more specific answers to user information needs. In the Genomics track, the dedicated IR system has to extract relevant text passages in support of precise user questions. This task may also be viewed as the first stage of a Question/Answering system. In the Blog track we explore various strategies for retrieving opinions from the blogsphere, which in this case involves subjective opinions about various targets entities (e.g., person, location, organization, event, product or technology). This task can be subdivided in two parts: 1) retrieve relevant information (facts) and 2) extract positive, negative or mixed opinions about the specific entity being targeted. To achieve these objectives we evaluate retrieval effectiveness using the Okapi (BM25) and various other models derived from the Divergence from Randomness (DFR) paradigm, as well as a language model (LM). Through our experiments with the Genomics corpus we find that the DFR models perform clearly better than the Okapi model (relative difference of 70%) in terms of mean average precision (MAP). Using the blog corpus, we found the opposite; the Okapi model performs slightly better than both DFR models (relative difference around 5%) and LM (relative difference 7%) model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FautschS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/FautschS07,
		author = {Claire Fautsch and Jacques Savoy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IR-Specific Searches at {TREC} 2007: Genomics {\&} Blog Experiments},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FautschS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Vocabulary-Driven Passage Retrieval for Question-Answering in Genomics

_Julien Gobeill, Imad Tbahriti, Frédéric Ehrler, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [uhosp-geneva.ruch](./participants.md#uhosp-geneva.ruch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uhosp-geneva.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uhosp-geneva.geo.final.pdf)
- :material-file-search: **Runs:** [GenTeam1](./runs.md#genteam1) | [GenTeaBB](./runs.md#genteabb) | [GenTeaPA](./runs.md#genteapa)

??? abstract "Abstract"
	
	This year, like in 2006, we use a collection of about 160000 full-text articles. The proposed task is a passage retrieval task. Several measures are applied on the returned data: passage mean average precision, document mean average precision, aspect mean average precision. This year, our efforts concentrated on combining knowledge-driven methods on top of a standard vector-space retrieval approach. We tested a passage selection methods based on vocabulary density estimation using several terminologies of the domain. We also attempted to improve standard retrieval approaches based on vector-space similarities by using a Boolean completion principle, which overweight documents containing all keywords. These combinations did not result in a significant improvement compared to the baseline system (document map ~ 0.20) and current results do not show much improvement compared to last year's reported results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GobeillTER07.bib) "
	```
	@inproceedings{DBLP:conf/trec/GobeillTER07,
		author = {Julien Gobeill and Imad Tbahriti and Fr{\'{e}}d{\'{e}}ric Ehrler and Patrick Ruch},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Vocabulary-Driven Passage Retrieval for Question-Answering in Genomics},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uhosp-geneva.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GobeillTER07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2007: Genomics Track

_Xiangji Huang, Damon Sotoudeh-Hosseinii, Hashmat Rohian, Xiangdong An_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/yorku.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/yorku.geo.final.pdf)
- :material-file-search: **Runs:** [york07ga1](./runs.md#york07ga1) | [york07ga2](./runs.md#york07ga2) | [york07ga3](./runs.md#york07ga3)

??? abstract "Abstract"
	
	Our Genomics experiments in this year mainly focus on improving the passage retrieval performance in the biomedical domain. We address this problem by constructing different indexes. In particular, we propose a method to build word-based index and sentence-based index for our experiments. The passage mean average precision (passage MAP) for our first run “york07ga1” using the word-based index was 0.095 and the passage MAP for our second run “york07ga2” using the sentence-based index was 0.086. However, the passage MAP for our third run “york07ga3” using both the word-based index and UMLS for query expansion degraded to 0.060. All these three official runs are automatic. The evaluation results show that using the word-based index is more effective than using the sentence-based index for improving the passage retrieval performance. We find that pseudo-relevance feedback can make a positive contribution to the retrieval performance. However, we also find that query expansion using UMLS and Entrez Gene does not improve the retrieval performance, and in some cases it makes a negative contribution to the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangSRA07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangSRA07,
		author = {Xiangji Huang and Damon Sotoudeh{-}Hosseinii and Hashmat Rohian and Xiangdong An},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2007: Genomics Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/yorku.geo.final.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangSRA07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Retrieval and Information Extraction in TREC Genomics  2007

_Antonio Jimeno-Yepes, Piotr Pezik_

- :fontawesome-solid-user-group: **Participant:** [ebi.yepes](./participants.md#ebi.yepes)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ebi.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ebi.geo.final.pdf)
- :material-file-search: **Runs:** [EBI1Lucene](./runs.md#ebi1lucene) | [EBI3Boosting](./runs.md#ebi3boosting) | [EBI2Fusion](./runs.md#ebi2fusion)

??? abstract "Abstract"
	
	In TREC Genomics a question/answering task has been proposed. A set of questions with a specific entity of interest is proposed and a set of passages from a collection of full text documents has to be selected from the document collection provided. We have used a two step approach: the first one is recall-oriented retrieval, and the second is an information extraction system that is intended to provide higher precision. We rely on well known techniques like query expansion and resources like MeSH and UMLS. The information extraction techniques are part of the infrastructure of the Text Mining Group at European Bioinformatics Institute. Using standard information retrieval techniques has been found more beneficial than using more complex processing. Having analyzed the results we find that the performance of query expansion varies for different topics. There are several reasons. Terminological resources may contain ambiguous synonyms or synonyms whose textual usage patterns differ from the usage of the original query terms. On the whole our performance was similar to the mean results from the three performance measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JimenoP07.bib) "
	```
	@inproceedings{DBLP:conf/trec/JimenoP07,
		author = {Antonio Jimeno{-}Yepes and Piotr Pezik},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Information Retrieval and Information Extraction in {TREC} Genomics 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ebi.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JimenoP07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Language Models for Genomics Information Retrieval: UIUC at TREC  2007 Genomics Track

_Yue Lu, Jing Jiang, Xu Ling, Xin He, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uc-zhai](./participants.md#uc-zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uiuc-lu.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uiuc-lu.geo.final.pdf)
- :material-file-search: **Runs:** [UIUCconj](./runs.md#uiucconj) | [UIUCsyn](./runs.md#uiucsyn) | [UIUCrelfb](./runs.md#uiucrelfb)

??? abstract "Abstract"
	
	The University of Illinois at Urbana-Champaign (UIUC) participated in TREC 2007 Genomics Track. Our general goal of participation is to apply language model-based approaches to the genomics retrieval task and study how we may extend the standard language models to accommodate two special needs for this year's genomics retrieval task: (1) gene synonym expansion and (2) conjunctive query interpretation. We also tested user relevance feedback. Preliminary result analysis shows that our synonym expansion method can improve document-level MAP, but generally has little influence on passage-level and aspect measures, while conjunctive scoring is not as effective as the standard KL-Divergence scoring, even though our pre-TREC experiments on a small set of training data showed otherwise. Relevance feedback appears to help. Further experiments and analysis are needed to draw more definitive conclusions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuJLHZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuJLHZ07,
		author = {Yue Lu and Jing Jiang and Xu Ling and Xin He and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Language Models for Genomics Information Retrieval: {UIUC} at {TREC} 2007 Genomics Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uiuc-lu.geo.final.pdf},
		timestamp = {Wed, 24 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LuJLHZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Bootstrapping Language Associated with Biomedical Entities

_Edgar Meij, Sophia Katrenko_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.meij](./participants.md#uamsterdam.meij)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uamsterdam-meij.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uamsterdam-meij.geo.final.pdf)
- :material-file-search: **Runs:** [AIDrun1](./runs.md#aidrun1) | [AIDrun3](./runs.md#aidrun3) | [AIDrun2](./runs.md#aidrun2)

??? abstract "Abstract"
	
	The TREC Genomics 2007 task included recognizing topic-specific entities in the returned passages. To address this task, we have designed and implemented a novel data-driven approach by combining information extraction with language modeling techniques. Instead of using an exhaustive list of all possible instances for an entity type, we look at the language usage around each entity type and use that as a classifier to determine whether or not a piece of text discusses such an entity type. We do so by comparing it with language models of the passages. E.g., given the entity type “genes”, our approach can measure the gene-iness of a piece of text. Our algorithm works as follows. Given an entity type, it first uses Hearst patterns to extract instances of the type. To extract more instances, we look for new contextual patterns around the instances and use them as input for a bootstrapping method, in which new instances and patterns are discovered iteratively. Afterwards, all discovered instances and patterns are used to find the sentences in the collection which are most on par with the requested entity type. A language model is then generated from these sentences and, at retrieval time, we use this model to rerank retrieved passages. As to the results of our submitted runs, we find that our baseline run performs well above the median of all participant's scores. Additionally, we find that applying our proposed method helps those entity types most for which there are unambiguous patterns and numerous instances.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeijK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeijK07,
		author = {Edgar Meij and Sophia Katrenko},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Bootstrapping Language Associated with Biomedical Entities},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uamsterdam-meij.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MeijK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using IR-n for Information Retrieval of Genomics Track

_María Pardiño, Rafael M. Terol, Patricio Martínez-Barco, Fernando Llopis, Elisa Noguera_

- :fontawesome-solid-user-group: **Participant:** [ualicante.terol](./participants.md#ualicante.terol)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ualicante.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ualicante.geo.final.pdf)
- :material-file-search: **Runs:** [IRn](./runs.md#irn)

??? abstract "Abstract"
	
	Nowadays there is a big amount of biomedical literature which uses complex nouns and acronyms of biological entities thus complicating the task of retrieval specific information. The Genomics Track works for this goal and this paper describes the approach we used to take part of this track of TREC 2007. As this is the first time we participate in this track, we configurated a new system consisting of the following diferenciated parts: preprocessing, passage generation, document retrieval and passage (with the answer) extraction. We want to call special attention to the textual retrieval system used, which was developed by the University of Alicante. Adapting the resources for the propouse, our system has obtained precision results over the mean and median average of the 66 official runs for the Document, Aspect and Passage2 MAP; and in the case of Passage MAP we get nearly the median and mean value. We want to emphasize we have obtained these results without incorporating specific information about the domain of the track. For the future, we would like to further develop our system in this direction.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PardinoTMLN07.bib) "
	```
	@inproceedings{DBLP:conf/trec/PardinoTMLN07,
		author = {Mar{\'{\i}}a Pardi{\~{n}}o and Rafael M. Terol and Patricio Mart{\'{\i}}nez{-}Barco and Fernando Llopis and Elisa Noguera},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using IR-n for Information Retrieval of Genomics Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ualicante.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PardinoTMLN07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cross Language Information Retrieval for Biomedical Literature

_Martijn J. Schuemie, Dolf Trieschnigg, Wessel Kraaij_

- :fontawesome-solid-user-group: **Participant:** [tno-ict](./participants.md#tno-ict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/utwente-erasmus-tno.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/utwente-erasmus-tno.geo.final.pdf)
- :material-file-search: **Runs:** [UTEMC1](./runs.md#utemc1) | [UTEMC2](./runs.md#utemc2)

??? abstract "Abstract"
	
	This workshop report discusses the collaborative work of UT, EMC and TNO on the TREC Genomics Track 2007. The biomedical information retrieval task is approached using cross language methods, in which biomedical concept detection is combined with effective IR based on unigram language models. Furthermore, a co-occurrence method is used to select and filter candidate answers. On its own, the cross lingual approach and the filtering do not strongly improve retrieval results. However, the combination of approaches does show a strong improvement over the monolingual baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchuemieTK07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchuemieTK07,
		author = {Martijn J. Schuemie and Dolf Trieschnigg and Wessel Kraaij},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Cross Language Information Retrieval for Biomedical Literature},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/utwente-erasmus-tno.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchuemieTK07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Retrieval Using Weights

_Jonathan Schuman, Sabine Bergler_

- :fontawesome-solid-user-group: **Participant:** [concordiau.bergler](./participants.md#concordiau.bergler)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/concordia.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/concordia.geo.final.pdf)
- :material-file-search: **Runs:** [biokiP](./runs.md#biokip) | [biokiS](./runs.md#biokis) | [biokiST](./runs.md#biokist)

??? abstract "Abstract"
	
	Using the same interactive IR component as for TREC 2006, this submission probed the ability of a user without requisite domain knowledge to interactively set appropriate weights. The weighted keyword proximity method employed allowed a computer science undergraduate to achieve rankings above the median for all measures without the use of external knowledge sources or term expansion techniques but in an interactive fashion. This suggests that domain experts should be able to perform above the median reliably, and are expected to excel when they can use domain terminology to their advantage.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchumanB07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchumanB07,
		author = {Jonathan Schuman and Sabine Bergler},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Interactive Retrieval Using Weights},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/concordia.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchumanB07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Entity-Based Relevance Feedback for Genomic List Answer Retrieval

_Nicola Stokes, Yi Li, Lawrence Cavedon, Eric Huang, Jiawen Rong, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [umelbourne.stokes](./participants.md#umelbourne.stokes)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umelbourne-stokes.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umelbourne-stokes.geo.final.pdf)
- :material-file-search: **Runs:** [MuMshFdRsc](./runs.md#mumshfdrsc) | [MuMshNfdRsc](./runs.md#mumshnfdrsc) | [MuMshFd](./runs.md#mumshfd)

??? abstract "Abstract"
	
	In this paper we present a system which uses ontological resources and a gene name variation generation tool to expand concepts in the original query. The novelty of our approach lies in our concept-based normalization ranking model. For the 2007 Genomic task, we also modified this system architecture with an additional dynamic form of query expansion called entity-based relevance feedback. This technique works by identifying potentially relevant entity instances in an initial set of retrieved candidate paragraphs. These entities are added to the initial query with the aim of boasting the rank of passages containing lists of these entities. Our final modification to the system, aims to maximizing the passage-level MAP score, by dropping sentences that do not contain any query concepts, from the beginning and the end of a candidate paragraph. Our TREC 2007 results show that our relevance feedback method can significantly improve baseline retrieval performance with respect to document-level MAP.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StokesLCHRZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/StokesLCHRZ07,
		author = {Nicola Stokes and Yi Li and Lawrence Cavedon and Eric Huang and Jiawen Rong and Justin Zobel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Entity-Based Relevance Feedback for Genomic List Answer Retrieval},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/umelbourne-stokes.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StokesLCHRZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage Relevancy Through Semantic Relatedness

_Luis Tari, Phan Huy Tu, Barry Lumpkin, Robert Leaman, Graciela Gonzalez, Chitta Baral_

- :fontawesome-solid-user-group: **Participant:** [arizona-stateu.gonzalez](./participants.md#arizona-stateu.gonzalez)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/arizonau.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/arizonau.geo.final.pdf)
- :material-file-search: **Runs:** [asubaral1](./runs.md#asubaral1) | [asubaral2](./runs.md#asubaral2) | [asubaral3](./runs.md#asubaral3)

??? abstract "Abstract"
	
	Questions that require answers in the form of a list of entities and the identification of diverse biological entity classes present an interesting challenge that required new approaches not needed for the TREC 2006 Genomics track. We added some components to our automatic question answering system, including (i) a simple algorithm to select which keywords extracted from natural language questions should be treated as essential in the formation of queries, (ii) the use of different entity recognizers for various biological entity classes in the extraction of passages (iii) determining relevancy of candidate passages with the use of semantic relatedness based on MeSH and UMLS semantic network. We present here an overview of our approach, with preliminary analysis and insights as to the performance of our system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TariTLLGB07.bib) "
	```
	@inproceedings{DBLP:conf/trec/TariTLLGB07,
		author = {Luis Tari and Phan Huy Tu and Barry Lumpkin and Robert Leaman and Graciela Gonzalez and Chitta Baral},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Passage Relevancy Through Semantic Relatedness},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/arizonau.geo.final.pdf},
		timestamp = {Wed, 25 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TariTLLGB07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT TREC 2007 Genomics Track: Using Concept-Based Semantics in  Context for Genomics Literature Passage Retrieval

_Jay Urbain, Nazli Goharian, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [iit.urbain](./participants.md#iit.urbain)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/iit-urbain.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/iit-urbain.geo.final.pdf)
- :material-file-search: **Runs:** [iitx1r2](./runs.md#iitx1r2) | [iitx2r2](./runs.md#iitx2r2) | [iitx3r2](./runs.md#iitx3r2)

??? abstract "Abstract"
	
	For the TREC-2007 Genomics Track [1], we explore unsupervised techniques for extracting semantic information about biomedical concepts with a retrieval model for using these semantics in context to improve passage retrieval precision. Dependency grammar analysis is evaluated for boosting the rank of passages where complementary subject/object concept pairs can be identified between queries and sentences from candidate passages. In our model, a concept is represented as a set of synonymous terms and a concept-word distribution. Concept terms are identified using an information extraction technique relying on shallow sentence parsing, external knowledge sources, and document context. The system combines a dimensional data model for indexing scientific literature at multiple levels of document context, with a rule-based query processing algorithm. The data model consists of two hierarchical indices: one for individual words and a second for extracted concepts. The word index provides retrieval of single or multi-word terms. The concept index provides efficient retrieval of single or multiple independent concepts. A retrieval function combines concepts with term statistics at multiple levels of context to identify relevant passages. Finally, we boost the relevance score of sentences identified within a passage where we can identify term dependencies that complement subject/object pairs between query and passage sentences via dependency grammar analysis. Our objective for this year's forum was to improve passage retrieval precision. We submitted three automatically generated results for three variations of our retrieval model to the TREC forum. The three results exceeded the track median for character based passage retrieval by 75 to 93%. The mean average precision (MAP) for our top passage retrieval model was 0.0940 which compares favorably to the top result of 0.0976.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UrbainGF07.bib) "
	```
	@inproceedings{DBLP:conf/trec/UrbainGF07,
		author = {Jay Urbain and Nazli Goharian and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} {TREC} 2007 Genomics Track: Using Concept-Based Semantics in Context for Genomics Literature Passage Retrieval},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/iit-urbain.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UrbainGF07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage Retrieval with Vector Space and Query-Level Aspect Models

_Raymond Wan, Vo Ngoc Anh, Hiroshi Mamitsuka_

- :fontawesome-solid-user-group: **Participant:** [kyotou.wan](./participants.md#kyotou.wan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/kyotou-umelbourne.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/kyotou-umelbourne.geo.final.pdf)
- :material-file-search: **Runs:** [kyoto1](./runs.md#kyoto1) | [kyoto2](./runs.md#kyoto2) | [kyoto3](./runs.md#kyoto3)

??? abstract "Abstract"
	
	This report describes the joint work by Kyoto University and the University of Melbourne for the TREC Genomics Track in 2007. As with 2006, the task for this year was the retrieval of passages from a biomedical document collection. The overall framework of our system from 2006 remains unchanged and is comprised of two parts: a paragraph-level retrieval system and a passage extraction system. These two systems are based on the vector space model and a probabilistic word-based aspect model, respectively. This year, we have adopted numerous changes to our 2007 system which we believe corrected some problems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WanAM07.bib) "
	```
	@inproceedings{DBLP:conf/trec/WanAM07,
		author = {Raymond Wan and Vo Ngoc Anh and Hiroshi Mamitsuka},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Passage Retrieval with Vector Space and Query-Level Aspect Models},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/kyotou-umelbourne.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WanAM07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIM at TREC 2007

_Jun Xu, Jing Yao, Jiaqian Zheng, Qi Sun, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [fudanu.niu](./participants.md#fudanu.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf)
- :material-file-search: **Runs:** [fdgerun1](./runs.md#fdgerun1) | [fdgerun2](./runs.md#fdgerun2) | [fdgerun3](./runs.md#fdgerun3)

??? abstract "Abstract"
	
	This paper introduced the four tracks that WIM-Lab Fudan University had taken part in at TREC 2007. For spam track, a multi-centre model was proposed considering the characteristics of spam mails in contrast of traditional 2-class classification methodology, and the incremental clustering and closeness-based classification methods were applied this year. For enterprise track, our research was mainly focused on ranking functions of experts and selecting correct supporting documents regarding to a given topic. For legal track, the effects of word distribution model in query expansion and various corpus pre-processing methods were mainly evaluated. For genomics track, three score methods were proposed to find the most relevant text snippets to a given topic. This paper gives an overview of the methods employed for each sub tasks, and compares the results of each track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuYZSN07.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuYZSN07,
		author = {Jun Xu and Jing Yao and Jiaqian Zheng and Qi Sun and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIM} at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuYZSN07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2007 Genomics Track

_Zhihao Yang, Hongfei Lin, Baojin Cui, Yanpeng Li, Xiao Zhang_

- :fontawesome-solid-user-group: **Participant:** [dalianu.yang](./participants.md#dalianu.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/dalianu.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/dalianu.geo.final.pdf)
- :material-file-search: **Runs:** [DUTgen2](./runs.md#dutgen2) | [DUTgen1](./runs.md#dutgen1) | [DUTgen3](./runs.md#dutgen3)

??? abstract "Abstract"
	
	This paper describes our experiments on TREC 2007 Genomics Track which is concerned with question answering extraction from full-text biomedical literatures. In our experiment, named entities were recognized at the preprocessing stage using a two-view method. MeSH was used to expand the terms. We performed passage retrieval by using sentence-level half overlapped sliding windows. Indri structured query language operators were also used to construct queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLCLZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangLCLZ07,
		author = {Zhihao Yang and Hongfei Lin and Baojin Cui and Yanpeng Li and Xiao Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2007 Genomics Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/dalianu.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLCLZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Genomics Track at UIC

_Wei Zhou, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [uillinois.chicago.zhou](./participants.md#uillinois.chicago.zhou)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uic-zhou.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uic-zhou.geo.final.pdf)
- :material-file-search: **Runs:** [UICGenRun1](./runs.md#uicgenrun1) | [UICGenRun2](./runs.md#uicgenrun2)

??? abstract "Abstract"
	
	We considered that a query of this year's Genomics track consists of two parts, target and qualification. A target refers to any instance of a certain entity type and the qualification refers to the condition that the target needs to satisfy in order to be qualified as an answer to the query. For example, the target and qualification of the query “What [ANTIBODIES] have been used to detect protein TLR4?” are “an instance of ANTIBODIES” and “have been used to detect protein TLR4”, respectively. The relevance of a document to a query was measured by to what degree the document contains a target and satisfies the qualification [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouY07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouY07,
		author = {Wei Zhou and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Genomics Track at {UIC}},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uic-zhou.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouY07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

