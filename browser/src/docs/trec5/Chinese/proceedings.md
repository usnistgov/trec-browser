# Proceedings - Chinese 1996 

#### Spanish and Chinese Document Retrieval in TREC-5

_Alan F. Smeaton_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/multilingual_track.ps.gz](http://trec.nist.gov/pubs/trec5/papers/multilingual_track.ps.gz)
??? abstract "Abstract"
	
	The TREC-5 conference was the third year in which document retrieval in a language other than English was benchmarked. In TREC-3, 4 groups participated in an ad hoc retrieval task on a collection of 208 Mbytes of Mexican newspaper text in the Spanish language. In TREC-4 there were 10 groups who participated, once again in an ad hoc document retrieval task on the same Mexican newspaper texts but with new topics. In TREC-5 there was a change of document corpus and new topics for the Spanish ad hoc retrieval task and a corpus of documents and topics to support ad hoc retrieval in the Chinese language was introduced for the first time. There were 7 groups who submitted runs for the Spanish track and 10 who submitted results for Chinese. The corpus of texts used in the TREC-5 Spanish language task was approximately the same size as the one used in TREC-3 and TREC-4 but differed in that there was a more consistent use of accented characters and it was European Spanish as opposed to Mexican Spanish. This slightly affected the morphological processing of word forms. In the Chinese language each character represents at least a complete syllable, rather than a letter as in other languages. Many characters are also single syllable words. The total number of characters is therefore quite large and somewhat ill defined. A literate adult would typically recognise at least 5-6,000 characters. The various modern standards define between 10-12,000 characters, although if early and ancient literature is included the number rises to approximately 100,000. Chinese is agglutinating - there is no space between consecutive characters, except perhaps, at the end of a sentence. Thus to perform retrieval in Chinese, the basis has to be characters unless the text is pre-segmented into words.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Smeaton96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Smeaton96,
		author = {Alan F. Smeaton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Spanish and Chinese Document Retrieval in {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/multilingual\_track.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Smeaton96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY at TREC-5

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, John Broglio, Jinxi Xu, Hongming Shu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz](http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz)
- :material-file-search: **Runs:** [HIN300](./runs.md#hin300) | [HIN301](./runs.md#hin301)

??? abstract "Abstract"
	
	The University of Massachusetts participated in five tracks in TREC-5: Ad-hoc, Routing, Fil-tering, Chinese, and Spanish. Our results are generally positive, continuing to indicate that the techniques we have applied perform well in a variety of settings. Significant changes in our approaches include emphasis on identifying key concepts/terms in the query topics, expansion of the query using a variant of automatic feedback called 'Local Context Analysis', and application of these techniques to a non-European language. The results show the broad applicability of Local Context Analysis, demonstrate successful identification and use of key concepts, raise interesting questions about how key concepts affect precision, support the belief that many IR techniques can be applied across languages, present an intriguing lack of tradeoff between recall and precision when filtering, and confirm once again several known results about query formulation and combination. Regrettably, three of our official submissions were marred by errors in the processing (an undetected syntax error in some queries, and an incomplete data set in an another case). The following discussion analyzes corrected runs as well as those (not particularly meaningful) submitted runs. Our experiments were conducted with version 3.1 of the INQUERY information retrieval system. INQUERY is based on the Bayesian inference network retrieval model. It is described elsewhere [5, 4, 12, 11], so this paper focuses on relevant differences to the previously published algorithms.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCCBBHS96.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCCBBHS96,
		author = {James Allan and James P. Callan and W. Bruce Croft and Lisa Ballesteros and John Broglio and Jinxi Xu and Hongming Shu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} at {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AllanCCBBHS96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Query Zoning and Correlation Within SMART: TREC 5

_Chris Buckley, Amit Singhal, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [Cornell](./participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz](http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz)
- :material-file-search: **Runs:** [Cor5C1vt](./runs.md#cor5c1vt) | [Cor5C2ex](./runs.md#cor5c2ex)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 5, performing runs in the routing, ad-hoc, and foreign language environments. The major focus this year is on 'zoning' different parts of an initial retrieval ranking, and treating each type of query zone differently as processing continues. We also experiment with dynamic phrasing, seeing which words co-occur with original query words in documents judged relevant. Exactly the same procedure is used for foreign language environments as for English; our tenet is that good information retrieval techniques are more powerful than linguistic knowledge.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleySM96.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleySM96,
		author = {Chris Buckley and Amit Singhal and Mandar Mitra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Query Zoning and Correlation Within {SMART:} {TREC} 5},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleySM96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Term importance, Boolean conjunct training, negative terms, and foreign  language retrieval: probabilistic algorithms at TREC-5

_Fredric C. Gey, Aitao Chen, Jianzhang He, Liangjie Xu, Jason Meggs_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz](http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz)
- :material-file-search: **Runs:** [BrklyCH1](./runs.md#brklych1) | [BrklyCH2](./runs.md#brklych2)

??? abstract "Abstract"
	
	The Berkeley experiments for TREC-5 extend those of TREC-4 in numerous ways. For routing retrieval we experimented with the idea of term importance in three ways -- training on Boolean con-juncts of the most important terms, filtering with the most important terms, and, finally, logistic regression on presence or absence of those terms. For ad-hoc retrieval we retained the manual reformulations of the topics and experimented with negative query terms. The ad-hoc retrieval formula originally devised for TREC-2 has proven to be robust, and was used for the TREC-5 ad-hoc retrieval and for our Chinese and Spanish retrieval. Chinese retrieval was accomplished through development of a segmentation algorithm which was used to augment a Chinese dictionary. The manual query run BrklyCH2 achieved a spectacular 97.48 percent recall over the 19 queries evaluated before the conference.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyCHXM96.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyCHXM96,
		author = {Fredric C. Gey and Aitao Chen and Jianzhang He and Liangjie Xu and Jason Meggs},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Term importance, Boolean conjunct training, negative terms, and foreign language retrieval: probabilistic algorithms at {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GeyCHXM96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Relevance Feedback within the Relational Model for TREC-5

_David A. Grossman, Carol Lundquist, John Reichart, David O. Holmes, Abdur Chowdhury, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [GMU](./participants.md#gmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz)
- :material-file-search: **Runs:** [gmu96ca1](./runs.md#gmu96ca1) | [gmu96ca2](./runs.md#gmu96ca2) | [gmu96cm1](./runs.md#gmu96cm1) | [gmu96cm2](./runs.md#gmu96cm2)

??? abstract "Abstract"
	
	For TREC-5, we enhanced our existing prototype that implements relevance ranking using the AT&T DBC-1012 Model 4 parallel database machine to include relevance feedback. We identified SQL to compute relevance feedback and ran several experiments to identify good cutoffs for the number of documents that should be assumed to be relevant and the number of terms to add to a query. We also tried to find an optimal weighting scheme such that terms added by relevance feedback are weighted differently from those in the original query. We implemented relevance feedback in our special purpose IR prototype. Additionally, we used relevance feedback as a part of our submissions for English, Spanish, Chinese and corrupted data. Finally, we were a participant in the large data track as well. We used a text merging approach whereby a single Pentium processor was able to implement adhoc retrieval on a 4GB text collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanLRHCF96,
		author = {David A. Grossman and Carol Lundquist and John Reichart and David O. Holmes and Abdur Chowdhury and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Relevance Feedback within the Relational Model for {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-5

_Micheline Hancock-Beaulieu, Mike Gatford, Xiangji Huang, Stephen E. Robertson, Steve Walker, P. W. Williams_

- :fontawesome-solid-user-group: **Participant:** [City](./participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz)
- :material-file-search: **Runs:** [city96c1](./runs.md#city96c1) | [city96c2](./runs.md#city96c2)

??? abstract "Abstract"
	
	City submitted two runs each for the automatic ad hoc, very large collection track, automatic routing and Chinese track; and took part in the interactive and filtering tracks. There were no very significant new developments; the same Okapi-style weighting as in TREC-3 and TREC-4 was used this time round, although there were attempts, in the ad hoc and more notably in the Chinese experiments, to extend the weighting to cover searches containing both words and phrases. All submitted runs except for the Chinese incorporated run-time passage determination and searching. The Okapi back-end search engine has been considerably speeded, and a few new functions incorporated. See Section 3.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Hancock-BeaulieuGHRWW96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Hancock-BeaulieuGHRWW96,
		author = {Micheline Hancock{-}Beaulieu and Mike Gatford and Xiangji Huang and Stephen E. Robertson and Steve Walker and P. W. Williams},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi at {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Hancock-BeaulieuGHRWW96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Berkeley Chinese Information Retrieval at TREC-5: Technical Report

_Jianzhang He, Jack Xu, Aitao Chen, Jason Meggs, Fredric C. Gey_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.chinese.ps.gz](http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.chinese.ps.gz)
- :material-file-search: **Runs:** [BrklyCH1](./runs.md#brklych1) | [BrklyCH2](./runs.md#brklych2)

??? abstract "Abstract"
	
	The Berkeley experiments for TREC-5 extend those of TREC-4 in numerous ways. For routing retrieval we experimented with the idea of term importance in three ways -- training on Boolean con-juncts of the most important terms, filtering with the most important terms, and, finally, logistic regression on presence or absence of those terms. For ad-hoc retrieval we retained the manual reformulations of the topics and experimented with negative query terms. The ad-hoc retrieval formula originally devised for TREC-2 has proven to be robust, and was used for the TREC-5 ad-hoc retrieval and for our Chinese and Spanish retrieval. Chinese retrieval was accomplished through development of a segmentation algorithm which was used to augment a Chinese dictionary. The manual query run BrklyCH2 achieved a spectacular 97.48 percent recall over the 19 queries evaluated before the conference.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeXCMG96.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeXCMG96,
		author = {Jianzhang He and Jack Xu and Aitao Chen and Jason Meggs and Fredric C. Gey},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Berkeley Chinese Information Retrieval at {TREC-5:} Technical Report},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.chinese.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeXCMG96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on Chinese Text Indexing – CLARIT TREC-5 Chinese  Track Report

_Xiang Tong, ChengXiang Zhai, Natasa Milic-Frayling, David A. Evans_

- :fontawesome-solid-user-group: **Participant:** [CLARITECH](./participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/CLARIT-Chinese.ps.gz](http://trec.nist.gov/pubs/trec5/papers/CLARIT-Chinese.ps.gz)
- :material-file-search: **Runs:** [CLCHNA](./runs.md#clchna) | [CLCHNM](./runs.md#clchnm)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TongZME96.bib) "
	```
	@inproceedings{DBLP:conf/trec/TongZME96,
		author = {Xiang Tong and ChengXiang Zhai and Natasa Milic{-}Frayling and David A. Evans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments on Chinese Text Indexing -- {CLARIT} {TREC-5} Chinese Track Report},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/CLARIT-Chinese.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TongZME96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on Routing, Filtering and Chinese Text Retrieval in TREC-5

_Chong-Wah Ngo, Kok F. Lai_

- :fontawesome-solid-user-group: **Participant:** [ITI-SG](./participants.md#iti-sg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz)
- :material-file-search: **Runs:** [iticn1](./runs.md#iticn1) | [iticn2](./runs.md#iticn2)

??? abstract "Abstract"
	
	We describes our experiments in the routing, filtering and Chinese text retrieval. We based our routing and filtering experiments on our discriminant project algorithm. The algorithm sequentially constructs a series of orthogonal axis from the training documents using the Gram-Schmidt procedure. It then rotates the resulting subspace using principal component analysis so that the axis are ordered by their importance. For Chinese text retrieval, we experimented both with an automatic method and a manual method. For the automatic method, we use all phrases in the description field and compute the aggregate scores using the simple tf.idf formula. We then manually construct boolean phrase queries which are thought to improve the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NgoL96.bib) "
	```
	@inproceedings{DBLP:conf/trec/NgoL96,
		author = {Chong{-}Wah Ngo and Kok F. Lai},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments on Routing, Filtering and Chinese Text Retrieval in {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NgoL96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-5 English and Chinese Retrieval Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld_

- :fontawesome-solid-user-group: **Participant:** [CUNY](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz](http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz)
- :material-file-search: **Runs:** [pircsCw](./runs.md#pircscw) | [pircsCwc](./runs.md#pircscwc)

??? abstract "Abstract"
	
	Two English automatic ad-hoc runs have been submitted: pircsAAS uses short and pircsAAL employs long topics. Our new avtf*ildf term weighting was used for short queries. 2-stage retrieval were performed. Both automatic runs are much better than the overall automatic average. Two manual runs are based on short topics: pircAM1 employs double weighting for user-selected query terms and pircs AM2 additionally extends these queries with new terms chosen manually. They perform about average compared with the the overall manual runs. Our two Chinese automatic ad-hoc runs are: pircsCw, using short-word segmentation for Chinese texts and piresCwc, which additionally includes single characters. Both runs are much better than average, but pircsCwe has a slight edge over pircsCw. In routing a genetic algorithm is used to select suitable subsets of relevant documents for training queries. Out of an initial random population of 15, the best subset (based on average precision) was employed to train the routing queries for the pircsRGO run. This ith (= 0) population is operated by a probabilistic reproduction and crossover strategy to produce the (i+1)th and evaluated, and this iterates for 6 generations. The best relevant subset of the 6th is used for training our queries for pircsRG6. It performs a few percent better than pircsRGO, and both are well above average. For the filtering experiment, we use thresholding on the retrieval status values; thresholds are trained based on the utility functions. Results are also good.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokG96.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokG96,
		author = {K. L. Kwok and Laszlo Grunfeld},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-5} English and Chinese Retrieval Experiments using {PIRCS}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokG96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

