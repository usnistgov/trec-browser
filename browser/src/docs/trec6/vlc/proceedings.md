# Proceedings - Very Large Corpus 1997 

#### Overview of TREC-6 Very Large Collection Track

_David Hawking, Paul B. Thistlewaite_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/vlc_track.ps.gz](http://trec.nist.gov/pubs/trec6/papers/vlc_track.ps.gz)
??? abstract "Abstract"
	
	The emergence of real world applications for text collections orders of magnitude larger than the TREC collection has motivated the introduction of a Very Large Collection track within the TREC framework. The 20 gigabyte data set developed for the track is characterised, track objectives and guidelines are summarised and the measures employed are described. The contribution of the organizations which made data available is gratefully acknowledged and an overview is given of the track participants, the methods used and the results obtained. Alternative options for the future of the track are discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingT97.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingT97,
		author = {David Hawking and Paul B. Thistlewaite},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of {TREC-6} Very Large Collection Track},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {93--105},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/vlc\_track.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HawkingT97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AT&T at TREC-6

_Amit Singhal_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/att.ps.gz](http://trec.nist.gov/pubs/trec6/papers/att.ps.gz)

??? abstract "Abstract"
	
	TREC-6 is AT&T's first independent TREC participation. We are participating in the main tasks (adhoc, routing), the filtering track, the VLC track, and the SDR track This year, in the main tasks, we experimented with multi-pass query expansion using Rocchio's formulation. We concentrated a reasonable amount of our effort on our VLC track system, which is based on locally distributed, disjoint, and smaller sub-collections of the large collection. Our filtering track runs are based on our routing runs, followed by similarity thresholding to make a binary decision of the relevance prediction for a document.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Singhal97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Singhal97,
		author = {Amit Singhal},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {AT{\&}T at {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {215--225},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/att.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Singhal97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-6 Automatic ad hoc, VLC, routing, filtering and QSDR

_Steve Walker, Stephen E. Robertson, Mohand Boughanem, Gareth J. F. Jones, Karen Sparck Jones_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz](http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz)

??? abstract "Abstract"
	
	We were interested to find out whether the Okapi BSS (Basic Search System) could handle more than 20 gigabytes of text and 8 million documents without major modification. There was no problem with data structures, but one or two system parameters had to be altered. In the interests of speed and because of limited disk space, indexes without full positional information were used. This meant that it was not possible to use passage-searching. Apart from this, the runs were done in the same way as the ad hoc, but with parameters intended to maximize precision at 20 documents. Several pairs of runs were done, but only one based on the full topic statements was submitted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WalkerRBJJ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/WalkerRBJJ97,
		author = {Steve Walker and Stephen E. Robertson and Mohand Boughanem and Gareth J. F. Jones and Karen Sparck Jones},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi at {TREC-6} Automatic ad hoc, VLC, routing, filtering and {QSDR}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {125--136},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/city\_proc\_auto.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WalkerRBJJ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ANU/ACSys TREC-6 Experiments

_David Hawking, Paul B. Thistlewaite, Nick Craswell_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz](http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz)

??? abstract "Abstract"
	
	A number of experiments conducted within the framework of the TREC-6 conference and using a completely re-engineered version of the PArallel Document Retrieval Engine (PADRE97) are reported. Passage-based pseudo relevance feedback combined with a variant of City University's Okapi BM25 scoring function achieved best average precision, best recall and best precision@20 in the Long-topic Automatic Adhoc category. The same basic method was used as the basis for successful submissions in the Manual Adhoc, Filtering and VLC tasks. A new BM25-based method of scoring concept intersections was shown to produce a small but significant gain in precision on the Manual Adhoc task while the relevance feedback scheme produced a significant improvement in recall for all of the Adhoc query sets to which it was applied.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingTC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingTC97,
		author = {David Hawking and Paul B. Thistlewaite and Nick Craswell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ANU/ACSys {TREC-6} Experiments},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {275--290},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HawkingTC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage-Based Refinement (MultiText Experiements for TREC-6)

_Gordon V. Cormack, Charles L. A. Clarke, Christopher R. Palmer, Samuel S. L. To_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz)

??? abstract "Abstract"
	
	The MultiText system retrieves passages, rather than entire documents, that are likely to be relevant to a particular topic. For all runs, we used the reciprocal of the length of each passage as an estimate of its likely relevance and ranked accordingly. For the manual adhoc task we explored the limits of user interaction by judging some 13,000 documents based on retrieved passages. For the automatic adhoc task we used retrieved passages as a feedback source for new query terms. For the routing task we estimated probability of relevance from passage length and used this estimate to construct a compound (tiered) query which was used to rank the new data using passage length. For the Chinese track we indexed individual characters rather than segmented words or bigrams and used manually constructed queries and passage-length ranking. For the high precision track we performed judgements on passages using an interface similar to that used for the manual adhoc task. The Very Large Collection run was done on a network of four cheap computers using very simple manually constructed queries and passage-length ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackCPT97.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackCPT97,
		author = {Gordon V. Cormack and Charles L. A. Clarke and Christopher R. Palmer and Samuel S. L. To},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Passage-Based Refinement (MultiText Experiements for {TREC-6)}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {303--319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CormackCPT97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The GURU System in TREC-6

_Eric W. Brown, Herb A. Chong_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz)

??? abstract "Abstract"
	
	As the on-line world grows and increases its role in our daily lives, the problems of searching, categorizing, and understanding textual information become ever more important. While researchers and practitioners have made much progress in these areas over the last thirty years, anyone who has gone to the World Wide Web seeking information and returned with more frustration than answers can attest that much work remains. Today's important issues cover topics such as scalability, user interfaces, and techniques that exploit the unique hypermedia features of Web environments. To support our research in these areas, the Text Analysis and Advanced Search department at the IBM T. J. Watson Research Center has developed an experimental probabilistic text retrieval system called Guru[4]. Guru was originally built to explore new probabilistic ranking algorithms, and now serves as a test-bed for much of our text analysis, search, and categorization work. Guru may be run as a stand-alone system or in a client/server configuration. The Guru indexer performs minimal case and hyphen normalization, but otherwise indexes all words (including stop words) in their original form. The index includes document, paragraph, sentence, and word-in-sentence positional information for each word occurrence in the document collection. At search time, queries are input to Guru in a free-text format. Stop words are eliminated from the query and morphological variants for each query term are automatically generated and added as synonyms to the query term. Syntax is provided that allows the user to control morphological expansion and stop word elimination. Guru ranks documents using a probabilistic algorithm that considers the frequency statistics of the query terms in individual documents and the collection as a whole. Guru also considers lexical affinities (LAs), which are co-occurrences of two terms within a given distance. These automatically identified 'phrases' are ranked higher than instances of the component words occurring outside of the LA distance. Our purpose in participating in TREC-6 is four-fold. First, we continue to refine the base probabilistic ranking algorithm in Guru and wish to evaluate its performance on a large, standard test set. Second, we are developing a prototype user interface and seek initial feedback and guidance for further development. Third, we are interested in text search scalability as an issue orthogonal to the basic problems of search and categorization and seek feedback on initial attempts to address this issue. Fourth, hypermedia domains, such as the World Wide Web, are an increasingly important arena for application of text analysis and search technology. Such domains, however, pose a challenge for evaluation since both search and navigation must be considered by the evaluation metric. We hope that this issue will be addressed by the TREC community with the ultimate goal of defining appropriate evaluation metrics and building suitable test collections. Toward these ends, we are participating in the Ad-hoc Task, the Interactive Track, and the Very Large Corpus Track of TREC-6.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrownC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrownC97,
		author = {Eric W. Brown and Herb A. Chong},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {GURU} System in {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {535--540},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ibm\_brown.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BrownC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY Does Battle With TREC-6

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, Donald Byrd, Russell C. Swan, Jinxi Xu_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in eight of the ten tracks that were part of the TREC-6 workshop. We started with the two required tracks, ad-hoc and routing, but then included VLC, Filtering, Chinese, Cross-language, SDR, and Interactive. We omitted NLP and High Precision for want of time and energy. With so many tracks involved, it is nearly inevitable that something will go wrong. Despite our best efforts at verifying all aspects of each track-before, during, and after the experiments-we once again made mistakes that were minor in scope, but major in consequence. Those mistakes affected our results in Ad-hoc and Routing, as well as the dependent tracks of VLC and Filtering. The details of the mistakes are presented in each track's discussion, along with information comparing the submitted runs to the corrected runs. Unfortunately, those corrected runs are not included in TREC-6 summary information. This remainder of this report covers our approach to each of the tracks as well as some experimental results and analysis. We start with an overview of the major tools that were used across all tracks. The paper is divided into the following sections. The track descriptions are generally broken into approach, results, and analysis sections, though some tracks require a different description.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCCBBSX97.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCCBBSX97,
		author = {James Allan and James P. Callan and W. Bruce Croft and Lisa Ballesteros and Donald Byrd and Russell C. Swan and Jinxi Xu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} Does Battle With {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {169--206},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AllanCCBBSX97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

