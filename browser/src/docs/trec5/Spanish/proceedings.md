# Proceedings - Spanish 1996 

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
- :material-file-search: **Runs:** [SIN300](./runs.md#sin300) | [SIN301](./runs.md#sin301)

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
- :material-file-search: **Runs:** [Cor5SP1s](./runs.md#cor5sp1s) | [Cor5SP2l](./runs.md#cor5sp2l)

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

#### New Experiments In Cross-Language Text Retrieval At NMSU's Computing  Research Lab

_Mark W. Davis_

- :fontawesome-solid-user-group: **Participant:** [NMSU-D](./participants.md#nmsu-d)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/nmsu.davis.paper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/nmsu.davis.paper.ps.gz)
- :material-file-search: **Runs:** [nmsuc1](./runs.md#nmsuc1) | [nmsuc2](./runs.md#nmsuc2) | [nmsuc3](./runs.md#nmsuc3)

??? abstract "Abstract"
	
	In Cross-Language Text Retrieval, queries in one language retrieve documents in other languages. Query translation is the least expensive approach to the retrieval task when compared to full document translation. The simple combinatorial properties of vector-based text retrieval systems simplify the translation task enormously, reducing most translation to the correct substitution of equivalents from a bilingual lexicon or corpus. New experiments are presented on methods for selecting among potential equivalents from a bilingual lexicon, including one fully-automatic method that achieves 73.5% of the performance of a monolingual system operating on the same retrieval task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Davis96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Davis96,
		author = {Mark W. Davis},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {New Experiments In Cross-Language Text Retrieval At NMSU's Computing Research Lab},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/nmsu.davis.paper.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Davis96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Term importance, Boolean conjunct training, negative terms, and foreign  language retrieval: probabilistic algorithms at TREC-5

_Fredric C. Gey, Aitao Chen, Jianzhang He, Liangjie Xu, Jason Meggs_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz](http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz)
- :material-file-search: **Runs:** [BrklySP5](./runs.md#brklysp5) | [BrklySP6](./runs.md#brklysp6)

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
- :material-file-search: **Runs:** [gmu96sp1](./runs.md#gmu96sp1) | [gmu96sp2](./runs.md#gmu96sp2)

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

#### Xerox TREC-5 Site Report: Routing, Filtering, NLP, and Spanish Tracks

_David A. Hull, Gregory Grefenstette, B. Maximilian Schulze, Éric Gaussier, Hinrich Schütze, Jan O. Pedersen_

- :fontawesome-solid-user-group: **Participant:** [Xerox](./participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz](http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz)
- :material-file-search: **Runs:** [xerox-spS](./runs.md#xerox-sps) | [xerox-spP](./runs.md#xerox-spp) | [xerox-spT](./runs.md#xerox-spt) | [xerox-spD](./runs.md#xerox-spd)

??? abstract "Abstract"
	
	Xerox participated in TREC 5 through experiments carried out separately and conjointly at the Rank Xerox Research Centre (RXRC) in Grenoble and the Xerox Palo Alto Research Center The remainder of this report is divided into three sections. The first section describes our work on routing and filtering (Hull, Schütze, and Pedersen), the second section covers the NLP track (Grefenstette, Schulze, and Gaussier), and the final section addresses the Spanish track (Grefenstette, Schulze, and Hull).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HullGSGSP96.bib) "
	```
	@inproceedings{DBLP:conf/trec/HullGSGSP96,
		author = {David A. Hull and Gregory Grefenstette and B. Maximilian Schulze and {\'{E}}ric Gaussier and Hinrich Sch{\"{u}}tze and Jan O. Pedersen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Xerox {TREC-5} Site Report: Routing, Filtering, NLP, and Spanish Tracks},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz},
		timestamp = {Thu, 08 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HullGSGSP96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Alignment of Spanish and English TREC Topic Descriptions

_Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMd](./participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/umd.ps.gz](http://trec.nist.gov/pubs/trec5/papers/umd.ps.gz)

??? abstract "Abstract"
	
	A technique is described for aligning TREC topic descriptions that is capable of producing a small multilingual test collection which can be used for cross-language ad-hoc and routing evaluations. Methods for measuring the degree of degradation induced by the necessary approximations are described and illustrated using examples from an evaluation of two cross-language routing techniques. Although the experiments were conducted on a relatively small test collection using existing TREC relevance judg-ments, the results suggest that cross-language routing is practical and that the investment required to produce a cross-language test collection for the TREC multilingual track would be justified.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Oard96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Oard96,
		author = {Douglas W. Oard},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Alignment of Spanish and English {TREC} Topic Descriptions},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/umd.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Oard96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-5 Experiments at Dublin City University: Query Space Reduction,  Spanish & Character Shape Encoding

_Fergus Kelledy, Alan F. Smeaton_

- :fontawesome-solid-user-group: **Participant:** [Dublin](./participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/dcu_trk5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/dcu_trk5.ps.gz)
- :material-file-search: **Runs:** [DCU965](./runs.md#dcu965) | [DCU966](./runs.md#dcu966) | [DCU967](./runs.md#dcu967)

??? abstract "Abstract"
	
	In this paper we describe work done as part of the TREC-5 benchmarking exercise by a team from Dublin City University. In TREC-5 we had three activities as follows: Our ad hoc submissions employ Query Space Reduction techniques which attempt to minimise the amount of data processed by an IR search engine during the retrieval process. We submitted four runs for evaluation, two automatic and two manual with one automatic run and one manual run employing our Query Space Reduction techniques. The paper reports our findings in terms of retrieval effectiveness and also in terms of the savings we make in execution time. Our submission to the multi-lingual track (Spanish) in TREC-5 involves evaluating the performance of a new stemming algorithm for Spanish developed by Martin Porter. We submitted three runs for evaluation, two automatic, and one manual, involving a manual expansion from retrieved documents. Character shape coding (CSC) is a technique for representing scanned text using a much reduced alphabet. It has been developed by Larry Spitz of Daimler Benz as an alternative to full-scale OCR for paper documents. Some of our TREC-5 experiments have started evaluating the performance of a CSC representation of scanned documents for information retrieval and this paper outlines our future work in this area
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KelledyS96.bib) "
	```
	@inproceedings{DBLP:conf/trec/KelledyS96,
		author = {Fergus Kelledy and Alan F. Smeaton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-5} Experiments at Dublin City University: Query Space Reduction, Spanish {\&} Character Shape Encoding},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/dcu\_trk5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KelledyS96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

