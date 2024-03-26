# Proceedings 2004 

## Overview of TREC 2004

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/OVERVIEW13.pdf](http://trec.nist.gov/pubs/trec13/papers/OVERVIEW13.pdf)
??? abstract "Abstract"
	
	The thirteenth Text REtrieval Conference, TREC 2004, was held at the National Institute of Standards and Technology (NIST) November 16-19, 2004. The conference was co-sponsored by NIST, the US Department of Defense Advanced Research and Development Activity (ARDA), and the Defense Advanced Research Projects Agency (DARPA). TREC 2004 is the latest in a series of workshops designed to foster research on technologies for information retrieval. The workshop series has four goals: to encourage retrieval research based on large test collections; to increase communication among industry, academia, and government by creating an open forum for the ex- change of research ideas; to speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems; and to increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current systems. TREC 2004 contained seven areas of focus called “tracks”. Six of the tracks had run in at least one previous TREC, while the seventh track, the terabyte track, was new in TREC 2004. The retrieval tasks performed in each of the tracks are summarized in Section 3 below. Table 2 at the end of this paper lists the 103 groups that participated in TREC 2004. The participating groups come from 21 different countries and include academic, commercial, and government institutions. This paper serves as an introduction to the research described in detail in the remainder of the volume. The next section provides a summary of the retrieval background knowledge that is assumed in the other papers. Section 3 presents a short description of each track—a more complete description of a track can be found in that track's overview paper in the proceedings. The final section looks toward future TREC conferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees04.bib)"
	```
	@inproceedings{DBLP:conf/trec/Voorhees04,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/OVERVIEW13.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Genomics 

#### TREC 2004 Genomics Track Overview

_William R. Hersh, Ravi Teja Bhupatiraju, L. Ross, Aaron M. Cohen, Dale Kraemer, Phoebe Johnson_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/GEO.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec13/papers/GEO.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC 2004 Genomics Track consisted of two tasks. The first task was a standard ad hoc retrieval task using topics obtained from real biomedical research scientists and documents from a large subset of the MEDLINE bibliographic database. The second task focused on categorization of full-text documents, simulating the task of curators of the Mouse Genome Informatics (MGI) system and consisting of three subtasks. One subtask focused on the triage of articles likely to have experimental evidence warranting the assignment of GO terms, while the other two subtasks focused on the assignment of the three top-level GO categories. The track had 33 participating groups.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershBRCKJ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershBRCKJ04,
		author = {William R. Hersh and Ravi Teja Bhupatiraju and L. Ross and Aaron M. Cohen and Dale Kraemer and Phoebe Johnson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2004 Genomics Track Overview},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/GEO.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershBRCKJ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Knowledge-Intensive and Statistical Approaches to the Retrieval and  Annotation of Genomics MEDLINE Citations

_Alan R. Aronson, Susanne M. Humphrey, Nicholas C. Ide, Won Kim, Russell F. Loane, James G. Mork, Lawrence H. Smith, Lorraine K. Tanabe, W. John Wilbur, Natalie Xie, Dina Demner-Fushman, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [nlm.umd.ul](./genomics/participants.md#nlm.umd.ul)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/nlm-umd-ul.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/nlm-umd-ul.geo.pdf)
- :material-file-search: **Runs:** [LHCUMDSE](./genomics/runs.md#lhcumdse) | [tq0](./genomics/runs.md#tq0) | [NLMT21](./genomics/runs.md#nlmt21) | [NLMT22](./genomics/runs.md#nlmt22) | [NLMT2ADA](./genomics/runs.md#nlmt2ada) | [NLMT2BAYES](./genomics/runs.md#nlmt2bayes) | [NLMT2SVM](./genomics/runs.md#nlmt2svm) | [NLMA1](./genomics/runs.md#nlma1) | [NLMA2](./genomics/runs.md#nlma2)

??? abstract "Abstract"
	
	Retrieving and annotating relevant information sources in the genomics literature are difficult but common tasks undertaken by biologists. The research presented here addresses these issues by exploring methods for retrieving MEDLINE® citations that answer real biologists' information needs and by addressing the initial tasks required to annotate MEDLINE citations having genomic content with terms from the Gene Ontology (GO). We approached the retrieval task using two methods: aggressive, knowledge-intensive query expansion and text neighboring. Our approaches to the triage subtask for annotation consisted of traditional machine learning (ML) methods as well as a novel ML algorithm for thematic analysis. Finally, we used a statistical, n-gram heuristic to decide which of the GO hierarchies should be used to annotate a given MEDLINE citation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AronsonHIKLMSTWXDL04.bib) "
	```
	@inproceedings{DBLP:conf/trec/AronsonHIKLMSTWXDL04,
		author = {Alan R. Aronson and Susanne M. Humphrey and Nicholas C. Ide and Won Kim and Russell F. Loane and James G. Mork and Lawrence H. Smith and Lorraine K. Tanabe and W. John Wilbur and Natalie Xie and Dina Demner{-}Fushman and Hongfang Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Knowledge-Intensive and Statistical Approaches to the Retrieval and Annotation of Genomics {MEDLINE} Citations},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/nlm-umd-ul.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AronsonHIKLMSTWXDL04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Expanding Queries Using Stems and Symbols

_Michela Bacchin, Massimo Melucci_

- :fontawesome-solid-user-group: **Participant:** [u.padova](./genomics/participants.md#u.padova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/upadova.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/upadova.geo.pdf)
- :material-file-search: **Runs:** [PDTNsmp4](./genomics/runs.md#pdtnsmp4) | [PD50501](./genomics/runs.md#pd50501)

??? abstract "Abstract"
	
	This paper describes the experiments conducted in the ad-hoc retrieval task of the Genomic track at TREC 2004. Different query expansion techniques based on the addition of keyword stems and of genomic product symbols selected by relevance feedback were studied. Stemming was tested using a mutual reinforcement process for building a domain-specific stemmer. Relevance feedback was tested using a technique exploiting associations between symbols and related keywords.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BacchinM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/BacchinM04,
		author = {Michela Bacchin and Massimo Melucci},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Expanding Queries Using Stems and Symbols},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/upadova.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BacchinM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2004

_Bodo Billerbeck, Adam Cannane, Abhijit Chattaraj, Nicholas Lester, William Webber, Hugh E. Williams, John Yiannis, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [rmit.scholer](./genomics/participants.md#rmit.scholer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/rmit.tera.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/rmit.tera.geo.pdf)
- :material-file-search: **Runs:** [RMITa](./genomics/runs.md#rmita) | [RMITb](./genomics/runs.md#rmitb)

??? abstract "Abstract"
	
	RMIT University participated in two tracks at TREC 2004: Terabyte and Genomics, both for the first time. This paper describes the techniques we applied and our experiments in both tracks, and discusses the results of the genomics track runs; the terabyte track results are unavailable at the time of manuscript submission. We also describe our new zettair search engine, in use for the first time at TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BillerbeckCCLWWYZ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/BillerbeckCCLWWYZ04,
		author = {Bodo Billerbeck and Adam Cannane and Abhijit Chattaraj and Nicholas Lester and William Webber and Hugh E. Williams and John Yiannis and Justin Zobel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/rmit.tera.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BillerbeckCCLWWYZ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Terabyte Searching, Genomic Retrieval and Novelty Detection  for TREC 2004

_Stephen Blott, Fabrice Camous, Paul Ferguson, Georgina Gaughan, Cathal Gurrin, Gareth J. F. Jones, Noel Murphy, Noel E. O'Connor, Alan F. Smeaton, Peter Wilkins, Oisín Boydell, Barry Smyth_

- :fontawesome-solid-user-group: **Participant:** [dubblincity.u](./genomics/participants.md#dubblincity.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf)
- :material-file-search: **Runs:** [DCUma](./genomics/runs.md#dcuma) | [DCUmatn1](./genomics/runs.md#dcumatn1)

??? abstract "Abstract"
	
	In TREC2004, Dublin City University took part in three tracks, Terabyte (in collaboration with University College Dublin), Genomic and Novelty. In this paper we will discuss each track separately and present separate conclusions from this work. In addition, we present a general description of a text retrieval engine that we have developed in the last year to support our experiments into large scale, distributed information retrieval, which underlies all of the track experiments described in this document.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BlottCFGGJMOSWBS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/BlottCFGGJMOSWBS04,
		author = {Stephen Blott and Fabrice Camous and Paul Ferguson and Georgina Gaughan and Cathal Gurrin and Gareth J. F. Jones and Noel Murphy and Noel E. O'Connor and Alan F. Smeaton and Peter Wilkins and Ois{\'{\i}}n Boydell and Barry Smyth},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Terabyte Searching, Genomic Retrieval and Novelty Detection for {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BlottCFGGJMOSWBS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Domain-Specific Synonym Expansion and Validation for Biomedical Information  Retrieval (MultiText Experiments for TREC 2004)

_Stefan Büttcher, Charles L. A. Clarke, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [u.waterloo.clarke](./genomics/participants.md#u.waterloo.clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uwaterloo-clarke.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uwaterloo-clarke.geo.pdf)
- :material-file-search: **Runs:** [uwmtDg04tn](./genomics/runs.md#uwmtdg04tn) | [uwmtDg04n](./genomics/runs.md#uwmtdg04n)

??? abstract "Abstract"
	
	In the domain of biomedical publications, synonyms and homonyms are omnipresent and pose a great challenge for document retrieval systems. For this year's TREC Genomics Ad hoc Retrieval Task, we mainly addressed the problem of dealing with synonyms. We examined the impact of domain-specific knowledge on the effectiveness of query expansion and analyzed the quality of Google as a source of query expansion terms based on pseudo-relevance feedback. Our results show that automatic acronym expansion, realized by querying the AcroMed database of biomedical acronyms, almost always improves the performance of our document retrieval system. Google, on the other hand, produced results that were worse than the other, corpus-based feedback techniques we used as well in our experiments. We believe that the primary reason for Google's bad performance in this task is its highly restricted query language.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ButtcherCC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ButtcherCC04,
		author = {Stefan B{\"{u}}ttcher and Charles L. A. Clarke and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Domain-Specific Synonym Expansion and Validation for Biomedical Information Retrieval (MultiText Experiments for {TREC} 2004)},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uwaterloo-clarke.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ButtcherCC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Phrasal Queries with LingPipe and Lucene: Ad Hoc Genomics Text Retrieval

_Bob Carpenter_

- :fontawesome-solid-user-group: **Participant:** [alias-i](./genomics/participants.md#alias-i)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/alias-i.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/alias-i.geo.pdf)
- :material-file-search: **Runs:** [aliasiTerms](./genomics/runs.md#aliasiterms) | [aliasiBase](./genomics/runs.md#aliasibase)

??? abstract "Abstract"
	
	The hypothesis we explored for the Ad Hoc task of the Genomics track for TREC 2004 was that phrase-level queries would increase precision over a baseline of token-level terms. We implemented our approach using two open source tools: the Apache Jakarta Lucene TF/IDF search engine (version 1.3) and the Alias-i LingPipe tokenizer and named-entity annotator (version 1.0.6). Contrary to our intuitions, the baseline system provided better performance in terms of recall and precision for almost every query at almost every precision/recall operating point.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Carpenter04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Carpenter04,
		author = {Bob Carpenter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Phrasal Queries with LingPipe and Lucene: Ad Hoc Genomics Text Retrieval},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/alias-i.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Carpenter04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Feature Generation, Feature Selection, Classifiers, and Conceptual  Drift for Biomedical Document Triage

_Aaron M. Cohen, Ravi Teja Bhupatiraju, William R. Hersh_

- :fontawesome-solid-user-group: **Participant:** [ohsu.hersh](./genomics/participants.md#ohsu.hersh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ohsu-hersh.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/ohsu-hersh.geo.pdf)
- :material-file-search: **Runs:** [OHSUAll](./genomics/runs.md#ohsuall) | [OHSUNeeds](./genomics/runs.md#ohsuneeds) | [OHSUNBAYES](./genomics/runs.md#ohsunbayes) | [OHSUSVMJ20](./genomics/runs.md#ohsusvmj20) | [OHSUVP](./genomics/runs.md#ohsuvp)

??? abstract "Abstract"
	
	We approached the problem of classifying papers for the TREC 2004 Genomics Track triage task as a four step process: feature generation, feature selection, classifier training, and finally, classification. Section specific binary features that discriminated significantly between positive and negative training samples were chosen using the Chi-square statistic. Three classifiers were trained on this feature set: a simple Naive Bayes classifier, the SVMLight support vector machine implementation, and a voting perceptron extended to support variable learning rates. Comparing the classifiers on the training data we found that neither Naive Bayes nor SVMLight was able to adequately account for the factor of 20 in the utility function. The voting perceptron classifier performed much better at this. The performance on the test collection was lower for all classifiers, although consistent with the relative values of the training cross-validation. Feature subsetting showed no significant differences in precision or recall, implying that there was some redundancy among the features. We also examined how well the feature set derived from the 2002 training collection represented the papers in the 2003 test collection, and found a low level of similarity between feature sets derived from the two collections. This supports the hypothesis that important classification terms change quickly over time.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CohenBH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/CohenBH04,
		author = {Aaron M. Cohen and Ravi Teja Bhupatiraju and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Feature Generation, Feature Selection, Classifiers, and Conceptual Drift for Biomedical Document Triage},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ohsu-hersh.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CohenBH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept Extraction and Synonymy Management for Biomedical Information  Retrieval

_Colleen E. Crangle, Alex Zbyslaw, J. Michael Cherry, Eurie L. Hong_

- :fontawesome-solid-user-group: **Participant:** [converspeech](./genomics/participants.md#converspeech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/converspeech.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/converspeech.geo.pdf)
- :material-file-search: **Runs:** [ConversAuto](./genomics/runs.md#conversauto) | [ConversManu](./genomics/runs.md#conversmanu)

??? abstract "Abstract"
	
	This paper reports on work done for the Genomics Track at TREC 2004 by ConverSpeech LLC in conjunction with scientists at the Saccharomyces Genome Database (SGD), the model organism database located at Stanford University, California. The rapidly increasing number of articles in the biomedical literature has created new urgency for software tools that find information relevant to specific information needs. We focused on two challenges in this work: the problems of synonymy (several terms having the same meaning) and polysemy (a term having more than one meaning), and the problem of constructing queries from information needs stated in natural language. We investigated the use of concept extraction for the second problem, relying on the limited statements of information need as the source of textual analysis. To minimize the problem of synonymy, we investigated the use of a language-oriented biomedical ontology and MeSH (Medical Subject Headings) for term expansion. Additionally, to minimize the problem of polysemy, we used extracted concepts to analyze and rank the documents returned by a search. We submitted two sets of results to TREC for evaluation, the first one produced automatically, the second derived from the first by making specific kinds of changes in the query and ranking methods. The mean average precision (MAP) for the automatic result was lower than the median of the 37 submitted runs overall; however, desirable results were obtained for mean average precision at 10 and 100 documents for almost half the topics. The MAP for the derived result was higher than the median, a desirable result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CrangleZCH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/CrangleZCH04,
		author = {Colleen E. Crangle and Alex Zbyslaw and J. Michael Cherry and Eurie L. Hong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concept Extraction and Synonymy Management for Biomedical Information Retrieval},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/converspeech.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CrangleZCH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The GUC Goes to TREC 2004: Using Whole or Partial Documents for  Retrieval and Classification in the Genomics Track

_Kareem Darwish, Amgad Madkour_

- :fontawesome-solid-user-group: **Participant:** [german.u.cairo](./genomics/participants.md#german.u.cairo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/german.u.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/german.u.geo.pdf)
- :material-file-search: **Runs:** [PSE](./genomics/runs.md#pse) | [GUClin1700](./genomics/runs.md#guclin1700) | [GUClin1260](./genomics/runs.md#guclin1260) | [GUCply1260](./genomics/runs.md#gucply1260) | [GUCply1700](./genomics/runs.md#gucply1700) | [GUCwdply2000](./genomics/runs.md#gucwdply2000) | [GUCbase](./genomics/runs.md#gucbase) | [GUCsvm0](./genomics/runs.md#gucsvm0) | [GUCsvm5](./genomics/runs.md#gucsvm5) | [GUCir30](./genomics/runs.md#gucir30) | [GUCir50](./genomics/runs.md#gucir50)

??? abstract "Abstract"
	
	We were interested in examining the relative effect of using parts of the documents, different combinations of parts of the documents, or whole documents on retrieval and classification. We were also interested in the effect of MeSH terms on retrieval. Our experiments show that indexing titles, abstracts, and MeSH terms for adhoc retrieval yielded statistically significantly better results than any other part or combination of parts, with abstracts outperforming any other individual part of the documents. In the triage sub-task, using whole documents for training a classifier outperformed using titles, abstracts, diagram captions, MeSH terms, and windows of text around gene names. However, training a classifier using the combination of titles, abstracts, and MeSH terms produced results comparable to using whole documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DarwishM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/DarwishM04,
		author = {Kareem Darwish and Amgad Madkour},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {GUC} Goes to {TREC} 2004: Using Whole or Partial Documents for Retrieval and Classification in the Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/german.u.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DarwishM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DIMACS at the TREC 2004 Genomics Track

_Aynur A. Dayanik, Dmitriy Fradkin, Alexander Genkin, Paul B. Kantor, David Madigan, David D. Lewis, Vladimir Menkov_

- :fontawesome-solid-user-group: **Participant:** [rutgers.dayanik](./genomics/participants.md#rutgers.dayanik)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/rutgers-dayanik.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/rutgers-dayanik.geo.pdf)
- :material-file-search: **Runs:** [rutgersGAH1](./genomics/runs.md#rutgersgah1) | [rutgersGAH2](./genomics/runs.md#rutgersgah2) | [dimacsAabsw1](./genomics/runs.md#dimacsaabsw1) | [dimacsAp5w5](./genomics/runs.md#dimacsap5w5) | [dimacsAw20w5](./genomics/runs.md#dimacsaw20w5) | [dimacsTfl9d](./genomics/runs.md#dimacstfl9d) | [dimacsTfl9w](./genomics/runs.md#dimacstfl9w) | [dimacsTl9md](./genomics/runs.md#dimacstl9md) | [dimacsTl9mhg](./genomics/runs.md#dimacstl9mhg) | [dimacsTl9w](./genomics/runs.md#dimacstl9w) | [dimacsAl3w](./genomics/runs.md#dimacsal3w) | [dimacsAg3mh](./genomics/runs.md#dimacsag3mh)

??? abstract "Abstract"
	
	DIMACS participated in the text categorization and ad hoc retrieval tasks of the TREC 2004 Genomics track. For the categorization task, we tackled the triage and annotation hierarchy subtasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DayanikFGKMLM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/DayanikFGKMLM04,
		author = {Aynur A. Dayanik and Dmitriy Fradkin and Alexander Genkin and Paul B. Kantor and David Madigan and David D. Lewis and Vladimir Menkov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DIMACS} at the {TREC} 2004 Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/rutgers-dayanik.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DayanikFGKMLM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Novelty, Question Answering and Genomics: The University of Iowa Response

_David Eichmann, Yi Zhang, Shannon Bradshaw, Xin Ying Qiu, Li Zhou, Padmini Srinivasan, Aditya Kumar Sehgal, Hudon Wong_

- :fontawesome-solid-user-group: **Participant:** [u.iowa](./genomics/participants.md#u.iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf)
- :material-file-search: **Runs:** [UIowaGN1](./genomics/runs.md#uiowagn1) | [iowarun1](./genomics/runs.md#iowarun1) | [iowarun2](./genomics/runs.md#iowarun2) | [iowarun3](./genomics/runs.md#iowarun3) | [iowarun4](./genomics/runs.md#iowarun4)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannZBQZSSW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannZBQZSSW04,
		author = {David Eichmann and Yi Zhang and Shannon Bradshaw and Xin Ying Qiu and Li Zhou and Padmini Srinivasan and Aditya Kumar Sehgal and Hudon Wong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Novelty, Question Answering and Genomics: The University of Iowa Response},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannZBQZSSW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Revisiting Again Document Length Hypotheses TREC 2004 Genomics Track  Experiments at Patolis

_Sumio Fujita_

- :fontawesome-solid-user-group: **Participant:** [patolis.fujita](./genomics/participants.md#patolis.fujita)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/patolis.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/patolis.geo.pdf)
- :material-file-search: **Runs:** [pllsgen4a1](./genomics/runs.md#pllsgen4a1) | [pllsgen4a2](./genomics/runs.md#pllsgen4a2) | [pllsgen4t1](./genomics/runs.md#pllsgen4t1) | [pllsgen4t2](./genomics/runs.md#pllsgen4t2) | [pllsgen4t3](./genomics/runs.md#pllsgen4t3) | [pllsgen4t4](./genomics/runs.md#pllsgen4t4) | [pllsgen4t5](./genomics/runs.md#pllsgen4t5)

??? abstract "Abstract"
	
	The TREC-2004 Genomics track evaluation experiments at Patolis Corporation are described with a focus on the document length issues in different retrieval models such as TF*IDF or probabilistic language modeling approaches. In the genomics ad hoc retrieval task, combination of pseudo-relevance feedback and reference database feedback is applied. For the triage sub-task, we trained a SVM classifier using leave-one-out-cross-validation, and calibrated parameters to be optimal against the training set.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Fujita04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Fujita04,
		author = {Sumio Fujita},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Revisiting Again Document Length Hypotheses {TREC} 2004 Genomics Track Experiments at Patolis},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/patolis.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Fujita04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Categorization of Genomics Text Based on Decision Rules

_Rocio Guillén_

- :fontawesome-solid-user-group: **Participant:** [u.sanmarcos](./genomics/participants.md#u.sanmarcos)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/cal-state-sanmarcos.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/cal-state-sanmarcos.geo.pdf)
- :material-file-search: **Runs:** [csusm](./genomics/runs.md#csusm) | [TRICSUSM](./genomics/runs.md#tricsusm)

??? abstract "Abstract"
	
	In this paper we present the approach, experiments and results for the categorization task in the Genomics Track. The approach we used is based on decision trees and decision rules for text categorization 1, 2, 3. The features selected were the keywords and the contents of the glosref tags to induce rules. Rules were then matched with the contents of font-changes in the abstracts of the documents to determine whether to select or not the text.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Guillen04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Guillen04,
		author = {Rocio Guill{\'{e}}n},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Categorization of Genomics Text Based on Decision Rules},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/cal-state-sanmarcos.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Guillen04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Sheffield University and the TREC 2004 Genomics Track: Query Expansion  Using Synonymous Terms

_Yikun Guo, Henk Harkema, Robert J. Gaizauskas_

- :fontawesome-solid-user-group: **Participant:** [u.sheffield.gaizauskas](./genomics/participants.md#u.sheffield.gaizauskas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/usheffield.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/usheffield.geo.pdf)
- :material-file-search: **Runs:** [shefauto1](./genomics/runs.md#shefauto1) | [shefauto2](./genomics/runs.md#shefauto2)

??? abstract "Abstract"
	
	In this paper we describe our approach to the Ad Hoc Retrieval task of the TREC 2004 Genomics Track. This is a conventional searching task based on a 10-year subset of MEDLINE (about 4.5 million documents and 9 gigabytes in size) and 50 topics derived from information needs obtained via interviews of real biomedical researchers. We will also discuss the results of our submitted runs. The hypothesis we want to test is whether the performance on this particular retrieval task can be improved by expanding queries with synonyms of the original query terms. We use the UMLS Metathesaurus, a comprehensive collection of controlled vocabularies in the biomedical domain, to identify query terms in topics and to determine their synonyms. Our approach is simple in the sense that we only consider synonyms of query terms and do not exploit hierarchical relations between terms such as hyponomy and hyperonymy. Synonymy-based query expansion generally increases recall, but decreases precision due to ambiguous terms. Word senses of ambiguous terms which are inappropriate with regard to the topic under consideration give rise to “polluting” synonyms. We hope that the use of a specifically biomedical term resource such as UMLS will limit the negative effects synonymy-based query expansion may have on precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuoHG04.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuoHG04,
		author = {Yikun Guo and Henk Harkema and Robert J. Gaizauskas},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Sheffield University and the {TREC} 2004 Genomics Track: Query Expansion Using Synonymous Terms},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/usheffield.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuoHG04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2004: HARD and Genomics Tracks

_Xiangji Huang, Yan Rui Huang, Ming Zhong, Miao Wen_

- :fontawesome-solid-user-group: **Participant:** [york.u](./genomics/participants.md#york.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf)
- :material-file-search: **Runs:** [york04g2](./genomics/runs.md#york04g2) | [york04g1](./genomics/runs.md#york04g1)

??? abstract "Abstract"
	
	York University participated in HARD and Genomics tracks this year. For both tracks, we used Okapi BSS (basic search system) as the basis. Our experiments mainly focused on exploiting various methods for combining document and passage scores, new term weighting formulae and feedback methods for query expansion. For HARD track, we built two levels of indexes, and search against both indexes for each topic. Then we combine these two searches into one. For Genomics track, we used a new strategy to automatically expand search terms by using relevance feedback and combined retrieval results from different fields into the final result. We achieved good results on the HARD task and average results on the Genomics task. For the HARD passage level evaluation, the automatic run 'yorku04ha1' obtained the best result (0.358) in terms of Bpref measure at 12K characters. The evaluation results show that Algorithm 1 is more effective than Algorithm 2 for the passage level retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangHZW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangHZW04,
		author = {Xiangji Huang and Yan Rui Huang and Ming Zhong and Miao Wen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2004: {HARD} and Genomics Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf},
		timestamp = {Tue, 05 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangHZW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MeSH Based Feedback, Concept Recognition and Stacked Classification  for Curation Tasks

_Wessel Kraaij, Stephan Raaijmakers, Marc Weeber, Rob Jelier_

- :fontawesome-solid-user-group: **Participant:** [tno.kraaij](./genomics/participants.md#tno.kraaij)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/tno-emc.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/tno-emc.geo.pdf)
- :material-file-search: **Runs:** [tnog2](./genomics/runs.md#tnog2) | [tnog3](./genomics/runs.md#tnog3) | [EMCTNOT1](./genomics/runs.md#emctnot1)

??? abstract "Abstract"
	
	This paper reports about experiments carried out in the context of the genomics track at TREC 2004. Experiments were concentrated on two subtasks: the ad hoc retrieval task and the triage task. Experiments for the ad hoc task aimed at improving a standard full-text ad-hoc run (using a language modeling approach) by exploiting the manual classification of MEDLINE abstracts (the MeSH terms) for relevance feedback. The triage task was modeled as a standard classification task, using stacked classifiers and complex features, recognized by the Collexis IR engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KraaijRWJ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/KraaijRWJ04,
		author = {Wessel Kraaij and Stephan Raaijmakers and Marc Weeber and Rob Jelier},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MeSH Based Feedback, Concept Recognition and Stacked Classification for Curation Tasks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/tno-emc.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KraaijRWJ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Identifying Relevant Full-Text Articles for GO Annotation Without  MeSH Terms

_Chih Lee, Wen-Juan Hou, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./genomics/participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ntu.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/ntu.geo.pdf)
- :material-file-search: **Runs:** [NTU2v3N1](./genomics/runs.md#ntu2v3n1) | [NTU3v3N1](./genomics/runs.md#ntu3v3n1) | [NTU3v3N1c2](./genomics/runs.md#ntu3v3n1c2) | [NTU4v3N1416](./genomics/runs.md#ntu4v3n1416)

??? abstract "Abstract"
	
	Gene Ontology (GO) is a controlled vocabulary. Given a gene product, GO enables scientists to clearly and unambiguously describe specific molecular functions of the gene product, specific biological processes in which it is involved, and specific cellular components to which it is localized. In this paper, we present our approach to identifying which papers have experimental evidence warranting annotation with GO codes. The training data set contains 375 relevant full-text articles and 5,462 irrelevant ones, and the test data set contains 420 positive full-text articles and 5,623 negative ones. We regarded this problem as a binary classification problem, and employed Support Vector Machines (SVMs) to distinguish positive articles from negative ones. Title, abstract, figure/table captions, and three standard sections - Results, Discussion, and Conclusion were the targets of feature extraction. Without incorporating MeSH (Medical Subject Headings) terms as part of the features, our system achieved 0.381 in Normalized Utility measure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeHC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeHC04,
		author = {Chih Lee and Wen{-}Juan Hou and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Identifying Relevant Full-Text Articles for {GO} Annotation Without MeSH Terms},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ntu.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeHC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2004: Genomics Track

_Jiao Li, Xian Zhang, Min Zhang, Xiaoyan Zhu_

- :fontawesome-solid-user-group: **Participant:** [tsinghua.ma](./genomics/participants.md#tsinghua.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.geo.pdf)
- :material-file-search: **Runs:** [THUIRgen01](./genomics/runs.md#thuirgen01) | [THUIRgen02](./genomics/runs.md#thuirgen02) | [THIRcat01](./genomics/runs.md#thircat01) | [THIRcat02](./genomics/runs.md#thircat02) | [THIRcat03](./genomics/runs.md#thircat03) | [THIRcat04](./genomics/runs.md#thircat04) | [THIRcat05](./genomics/runs.md#thircat05)

??? abstract "Abstract"
	
	This is the first time that THUIR participates in TREC Genomics Track. We took part in both Ad hoc retrieval task and Categorization task. Based on our retrieval system TMiner, our research in the Ad hoc retrieval task focuses on: (1) Category of organism retrieval strategy; (2) Primary Feature Model; (3) Query Expansion (QE) technology; (4) Result fusion method. Five official runs have been submitted at triage task in the Categorization task. Unigrams are used as features in Vector Space Model, and the high dimension feature vectors are trained and classified by SVM classifier with RBFs as the kernel function. Three ways are taken to improve the classifier: (1) Perform feature selection to reduce the dimension of feature vectors; (2) Weight the important features; (3) Balance between the positive dataset and the negative dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiZZZ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiZZZ04,
		author = {Jiao Li and Xian Zhang and Min Zhang and Xiaoyan Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2004: Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.geo.pdf},
		timestamp = {Wed, 02 Nov 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiZZZ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BioText Team Experiments for the TREC 2004 Genomics Track

_Preslav Nakov, Ariel S. Schwartz, Emilia Stoica, Marti A. Hearst_

- :fontawesome-solid-user-group: **Participant:** [u.hospital.geneva](./genomics/participants.md#u.hospital.geneva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ucal-berkeley.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/ucal-berkeley.geo.pdf)
- :material-file-search: **Runs:** [geneteam1](./genomics/runs.md#geneteam1) | [geneteam2](./genomics/runs.md#geneteam2) | [geneteam3](./genomics/runs.md#geneteam3) | [geneteamA1](./genomics/runs.md#geneteama1) | [geneteamA2](./genomics/runs.md#geneteama2) | [geneteamA3](./genomics/runs.md#geneteama3) | [geneteamA4](./genomics/runs.md#geneteama4) | [geneteamA5](./genomics/runs.md#geneteama5)

??? abstract "Abstract"
	
	The BioText group participated in the two main tasks of the TREC 2004 Genomics track. Our approach to the ad hoc task was similar to the one used in the 2003 Genomics track, but due to the lack of training data, we did not achieve the high scores of the previous year. The most novel aspect of our submission for the categorization task centers around our method for assigning Gene Ontology (GO) codes to articles marked for curation. This approach compares the text surrounding a target gene to text that has been found to be associated with GO codes assigned to homologous genes for organisms with genomes similar to mice (namely, humans and rats). We applied the same method to GO codes that have been assigned to MGI entries in years prior to the test set. In addition, we filtered out proposed GO codes based on their previously observed likelihood to co-occur with one another.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NakovSSH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/NakovSSH04,
		author = {Preslav Nakov and Ariel S. Schwartz and Emilia Stoica and Marti A. Hearst},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BioText Team Experiments for the {TREC} 2004 Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ucal-berkeley.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NakovSSH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2004 Genomics Track Experiments at UTA: The Effects of Primary  Keys, Bigram Phrases and Query Expansion on Retrieval Performance

_Ari Pirkola_

- :fontawesome-solid-user-group: **Participant:** [u.tampere](./genomics/participants.md#u.tampere)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/utampere.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/utampere.geo.pdf)
- :material-file-search: **Runs:** [utaauto](./genomics/runs.md#utaauto) | [utamanu](./genomics/runs.md#utamanu)

??? abstract "Abstract"
	
	We submitted runs for Genomics Track's ad hoc retrieval task. The first official run (utaauto) was an automatic run and the second (utamanu) manual. For utaauto, the main features of query formulation were the removal of performative and marginally topical words from the topics based on average term frequency statistics, the removal of stop-words, the identification of bigram phrases, the weighting of keys with low document frequency (which we call primary keys), and query expansion with MH terms. The utamanu queries were Boolean queries formulated on a basis of a concept analysis. New terms were selected from the MeSH, genome databases, and dictionaries. The mean average precision (MAP) for the utaauto queries was 0.3324 and for the utamanu queries 0.3128. In the additional experiments we studied the effects of utaauto's main features on retrieval performance. The results showed that assigning more weight to the primary key than the other keys of a query improves retrieval performance. The use of bigram phrases in queries was also useful. The bigram phrases were identified using a collocation technique that computes an adjacency indicator for words in topics based on the joint occurrences of the words in a large and small window of document text words. We call the technique relative key adjacency (RKA).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Pirkola04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Pirkola04,
		author = {Ari Pirkola},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2004 Genomics Track Experiments at {UTA:} The Effects of Primary Keys, Bigram Phrases and Query Expansion on Retrieval Performance},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/utampere.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Pirkola04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2004 Experiment: Genomics Track

_Patrick Ruch, Christine Chichester, Gilles Cohen, Frédéric Ehrler, Paul Fabry, Johan Marty, Henning Müller, Antoine Geissbühler_

- :fontawesome-solid-user-group: **Participant:** [u.hospital.geneva](./genomics/participants.md#u.hospital.geneva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uhosp-geneva.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uhosp-geneva.geo.pdf)
- :material-file-search: **Runs:** [geneteam1](./genomics/runs.md#geneteam1) | [geneteam2](./genomics/runs.md#geneteam2) | [geneteam3](./genomics/runs.md#geneteam3) | [geneteamA1](./genomics/runs.md#geneteama1) | [geneteamA2](./genomics/runs.md#geneteama2) | [geneteamA3](./genomics/runs.md#geneteama3) | [geneteamA4](./genomics/runs.md#geneteama4) | [geneteamA5](./genomics/runs.md#geneteama5)

??? abstract "Abstract"
	
	Because of corruptions in the XML TREC Genomics collection, which were detected only some days before the submission deadline, we were not able to submit runs for the ad hoc retrieval task (task I), although relevance judgements made after polling were used to evaluate our approaches, and therefore this report mostly focuses on the text categorization task (task II: triage and annotation). Task I. Our approach uses thesaural resources (from the UMLS) together with a variant of the Porter stemmer for string normalization. Gene and Protein Entities (GPE) of the collection were simply marked up by dictionary look up during the indexing in order to avoid erroneous conflation: strings not found in the UMLS Specialist lexicon (augmented with various English lexical resources) were considered as GPE and were moderately overweighed. Two different weighting schemas were tested: first, a standard tf-idf with cosine normalization, second a weighting based on the deviation from randomness model. For indexing the Genomic collection, the following MEDLINE records were selected: article's titles, MeSH and RN terms, and abstract fields. We investigated the use of high-precisions strategies and our system returned only highly reliable documents so that some queries were not answered by the system. Our best run achieved an average precision of 32% (ranked 6 out of 27 participants). The score was obtained using UMLS resources and GPE (Gene and Protein Entity) tagging together with a combination of a classical atc.ltn schema (following SMART notation) with a deviation from randomness [8] weighting: L(n e)C2 and KL for expansion. Task II. We participated in both the triage and annotation tasks. For these tasks we attempted to adapt a Gene Ontology categorizer, which showed very effective results in the context of the BioCreative challenge, where training data were very sparse. The tool was completed by a naïve Bayes learner in order to take advantage of the TREC training data. The use of the last year GeneRIF extraction tool has also been evaluated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuchCCEFMMG04.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuchCCEFMMG04,
		author = {Patrick Ruch and Christine Chichester and Gilles Cohen and Fr{\'{e}}d{\'{e}}ric Ehrler and Paul Fabry and Johan Marty and Henning M{\"{u}}ller and Antoine Geissb{\"{u}}hler},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2004 Experiment: Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uhosp-geneva.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuchCCEFMMG04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UB at TREC 13: Genomics Track

_Miguel E. Ruiz, Munirathnam Srikanth, Rohini K. Srihari_

- :fontawesome-solid-user-group: **Participant:** [suny.buffalo](./genomics/participants.md#suny.buffalo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/stateuny-buffalo.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/stateuny-buffalo.geo.pdf)
- :material-file-search: **Runs:** [UBgtNormJM1](./genomics/runs.md#ubgtnormjm1)

??? abstract "Abstract"
	
	This paper describes the experiments of the State University of New York at Buffalo in TREC 13. We participated in the Genomics track and submitted official runs to the Adhoc retrieval task. Our approach uses a language model IR system developed in house. We also present unofficial results for the triage sub-task of categorization task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuizSS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuizSS04,
		author = {Miguel E. Ruiz and Munirathnam Srikanth and Rohini K. Srihari},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UB} at {TREC} 13: Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/stateuny-buffalo.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuizSS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2004 Genomics Track Experiments at IUB

_Kazuhiro Seki, James C. Costello, Vasanth R. Singan, Javed Mostafa_

- :fontawesome-solid-user-group: **Participant:** [indiana.u.seki](./genomics/participants.md#indiana.u.seki)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/indianau-seki.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/indianau-seki.geo.pdf)
- :material-file-search: **Runs:** [lga1](./genomics/runs.md#lga1) | [lga2](./genomics/runs.md#lga2) | [lgcab1](./genomics/runs.md#lgcab1) | [lgcab2](./genomics/runs.md#lgcab2) | [lgcad1](./genomics/runs.md#lgcad1) | [lgcad2](./genomics/runs.md#lgcad2) | [lgct1](./genomics/runs.md#lgct1) | [lgct2](./genomics/runs.md#lgct2)

??? abstract "Abstract"
	
	This paper describes the methods we developed for the three tasks of the TREC Genomics Track, i.e., ad hoc retrieval, triage, and annotation tasks. For the ad hoc retrieval task, we used the classic vector space model and studied the use of query expansion and pseudo-relevance feedback. Our submitted runs obtained a MAP of 0.183. For the triage task, we adopted a naive Bayes classifier trained on MeSH terms and used gene names as filters to rule out false positives. The obtained normalized utility score was 0.435. For the annotation task, we focused on document representation and applied a variant of the kNN classifiers. One of our submitted runs produced an F1 score of 0.561, ranking first out of 36 runs submitted for the annotation task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SekiCSM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SekiCSM04,
		author = {Kazuhiro Seki and James C. Costello and Vasanth R. Singan and Javed Mostafa},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2004 Genomics Track Experiments at {IUB}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/indianau-seki.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SekiCSM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting Zone Information, Syntactic Rules, and Informative Terms  in Gene Ontology Annotation of Biomedical Documents

_Burr Settles, Mark Craven_

- :fontawesome-solid-user-group: **Participant:** [u.wisconsin](./genomics/participants.md#u.wisconsin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uwisconsin.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uwisconsin.geo.pdf)
- :material-file-search: **Runs:** [wiscWRT](./genomics/runs.md#wiscwrt) | [wiscW](./genomics/runs.md#wiscw) | [wiscWR](./genomics/runs.md#wiscwr) | [wiscWT](./genomics/runs.md#wiscwt)

??? abstract "Abstract"
	
	We describe a system developed for the Annotation Hierarchy subtask of the Text Retrieval Conference (TREC) 2004 Genomics Track. The goal of this track is to automatically predict Gene Ontology (GO) domain annotations given full-text biomedical journal articles and associated genes. Our system uses a two-tier statistical machine learning system that makes predictions first on 'zone'-level text (i.e. abstract, introduction, etc.) and then combines evidence to make final document-level predictions. We also describe the effects of more advanced syntactic features (equivalence classes of syntactic patterns) and 'informative terms' (phrases semantically linked to specific GO codes). These features are induced automatically from the training data and external sources, such as 'weakly labeled' MED-LINE abstracts. Our baseline system (using only traditional word features), significantly exceeds median F1 of all task submissions on unseen test data. We show further improvement by including syntactic features and informative term features. Our complete system exceeds median performance for all three evaluation metrics (precision, recall, and F1), and achieves the second highest reported F1 of all systems in the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SettlesC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SettlesC04,
		author = {Burr Settles and Mark Craven},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploiting Zone Information, Syntactic Rules, and Informative Terms in Gene Ontology Annotation of Biomedical Documents},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uwisconsin.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SettlesC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Genomics 2004

_Gail Sinclair, Bonnie L. Webber_

- :fontawesome-solid-user-group: **Participant:** [u.edinburgh.sinclair](./genomics/participants.md#u.edinburgh.sinclair)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uedinburgh-sinclair.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uedinburgh-sinclair.geo.pdf)
- :material-file-search: **Runs:** [edinauto2](./genomics/runs.md#edinauto2) | [edinauto5](./genomics/runs.md#edinauto5) | [epub2](./genomics/runs.md#epub2) | [eint2](./genomics/runs.md#eint2) | [emet2](./genomics/runs.md#emet2) | [eres2](./genomics/runs.md#eres2) | [edis2](./genomics/runs.md#edis2)

??? abstract "Abstract"
	
	The TREC Genomics track started in 2003 as the first domain specific track of the Text Retrieval Competition. The aim of the track is to develop various IR tasks specific to the biomedical field. One task of the first year involved the retrieval of documents given a specific gene, while the second task required the extraction a brief description of gene function from documents. This year sees a foray into ad hoc retrieval and a curation and categorization task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinclairW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinclairW04,
		author = {Gail Sinclair and Bonnie L. Webber},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Genomics 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uedinburgh-sinclair.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SinclairW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Meiji University Web, Novelty and Genomic Track Experiments

_Tomoe Tomiyama, Kosuke Karoji, Takeshi Kondo, Yuichi Kakuta, Tomohiro Takagi_

- :fontawesome-solid-user-group: **Participant:** [meiji.u](./genomics/participants.md#meiji.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf)
- :material-file-search: **Runs:** [MeijiHilG](./genomics/runs.md#meijihilg)

??? abstract "Abstract"
	
	We participated in Novelty track, the topic distillation task of Web track and ad hoc task of Genomic Track. Our main challenge is to deal with meaning of words and improve retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TomiyamaKKKT04.bib) "
	```
	@inproceedings{DBLP:conf/trec/TomiyamaKKKT04,
		author = {Tomoe Tomiyama and Kosuke Karoji and Takeshi Kondo and Yuichi Kakuta and Tomohiro Takagi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Meiji University Web, Novelty and Genomic Track Experiments},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TomiyamaKKKT04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Needs and Automatic Queries

_Richard M. Tong_

- :fontawesome-solid-user-group: **Participant:** [tarragon](./genomics/participants.md#tarragon)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/tarragon.tong.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/tarragon.tong.geo.pdf)
- :material-file-search: **Runs:** [tgnSplit](./genomics/runs.md#tgnsplit) | [tgnNecaux](./genomics/runs.md#tgnnecaux)

??? abstract "Abstract"
	
	Tarragon Consulting Corporation participated in the adhoc retrieval task of the TREC 2004 Genomics Track. We used a standard deployment of the K2 search engine from Verity, Inc. in which we exploited the free-text query parser to interpret the information need statements provided in the task. The primary goal of our participation was to establish a performance baseline using “of-the-shelf” tools and then to explore how knowledge-based extensions could enhance performance. Time and resource constraints prevented us from performing the knowledge-based experiments, but our official submissions show that reasonable performance can be achieved using just our baseline strategy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tong04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tong04,
		author = {Richard M. Tong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Information Needs and Automatic Queries},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/tarragon.tong.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tong04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2004 Genomics, Hard, Robust and Web Tracks

_Kiduk Yang, Ning Yu, Adam Wead, Gavin La Rowe, Yu-Hsiu Li, Christopher Friend, Yoon Lee_

- :fontawesome-solid-user-group: **Participant:** [indiana.u.yang](./genomics/participants.md#indiana.u.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf](http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf)
- :material-file-search: **Runs:** [wdvqlxa1](./genomics/runs.md#wdvqlxa1) | [wdvqlx1](./genomics/runs.md#wdvqlx1) | [wdtriage1](./genomics/runs.md#wdtriage1)

??? abstract "Abstract"
	
	To facilitate understanding of information as well as its discovery, we need to combine the capabilities of the human and the machine as well as multiple methods and sources of evidence. Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science houses several projects that aim to apply this idea of multi-level fusion in the areas of information retrieval and knowledge organization. The TREC research group of WIDIT, who engages in examination of information retrieval strategies that can accommodate a variety of data environments and search tasks, participated in the Genomics, HARD, Robust, and Web tracks in TREC-2004. The basic approach of WIDIT was to leverage multiple sources of evidence, combine multiple methods, and integrate the strengths of man and the machine. Our main strategies for the tracks were: the use of gene name thesaurus in the Genomics track; query expansion and relevance feedback in the HARD track; query expansion with keywords from Web search in the Robust track, and the interactive system tuning process called “Dynamic Tuning” in the Web track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYWRLFL04.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYWRLFL04,
		author = {Kiduk Yang and Ning Yu and Adam Wead and Gavin La Rowe and Yu{-}Hsiu Li and Christopher Friend and Yoon Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2004 Genomics, Hard, Robust and Web Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf},
		timestamp = {Tue, 24 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangYWRLFL04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experience of Using SVM for the Triage Task in TREC 2004 Genomics  Track

_Dell Zhang, Wee Sun Lee_

- :fontawesome-solid-user-group: **Participant:** [mlg.nus](./genomics/participants.md#mlg.nus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/natusing.zhang.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/natusing.zhang.geo.pdf)
- :material-file-search: **Runs:** [nusbird2004a](./genomics/runs.md#nusbird2004a) | [nusbird2004b](./genomics/runs.md#nusbird2004b) | [nusbird2004c](./genomics/runs.md#nusbird2004c) | [nusbird2004d](./genomics/runs.md#nusbird2004d) | [nusbird2004e](./genomics/runs.md#nusbird2004e)

??? abstract "Abstract"
	
	This paper reports our knowledge-ignorant machine learning approach to the triage task in TREC2004 genomics track, which is actually a text categorization problem. We applied Support Vector Machine (SVM) and found that information-gain based feature selection is helpful. Although we achieved decent performance in leave-one-out cross-validation experiments, the evaluation result on the test data turned out to be surprisingly poor. Further experiments revealed that there is a chasm between the training and test data distributions. It seems that more aggressive feature selection can partially alleviate the trouble caused by distribution change.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangL04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangL04,
		author = {Dell Zhang and Wee Sun Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experience of Using {SVM} for the Triage Task in {TREC} 2004 Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/natusing.zhang.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangL04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## HARD 

#### HARD Track Overview in TREC 2004 - High Accuracy Retrieval from  Documents

_James Allan_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/HARD.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec13/papers/HARD.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The HARD track of TREC 2004 aims to improve the accuracy of information retrieval through the use of three techniques: (1) query metadata that better describes the information need, (2) focused and time-limited interaction with the searcher through “clarification forms”, and (3) incorporation of passage-level relevance judgments and retrieval. Participation in all three aspects of the track was excellent this year with about 10 groups trying something in each area. No group was able to achieve huge gains in effectiveness using these techniques, but some improvements were found and enthusiasm for the clarification forms (in particular) remains high. The track will run again in TREC 2005.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Allan04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Allan04,
		author = {James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{HARD} Track Overview in {TREC} 2004 - High Accuracy Retrieval from Documents},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/HARD.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Allan04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers' HARD Track Experiences at TREC 2004

_Nicholas J. Belkin, I. Chaleva, Michael J. Cole, Yuelin Li, Lu Liu, Ying-Hsang Liu, Gheorghe Muresan, Catherine L. Smith, Ying Sun, Xiaojun Yuan, Xiao-Min Zhang_

- :fontawesome-solid-user-group: **Participant:** [rutgers.belkin](./HARD/participants.md#rutgers.belkin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/rutgers-belkin.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/rutgers-belkin.hard.pdf)
- :material-file-search: **Runs:** [rutinb](./HARD/runs.md#rutinb) | [Rutleb](./HARD/runs.md#rutleb) | [Rutlet1](./HARD/runs.md#rutlet1) | [Rutlet2](./HARD/runs.md#rutlet2)

??? abstract "Abstract"
	
	The goal of our work in the HARD track was to test techniques for using knowledge about various aspects of the information seeker's context to improve IR system performance. We were particularly concerned with such knowledge which could be gained through implicit sources of evidence, rather than explicit questioning of the information seeker. We therefore did not submit any clarification form1, preferring to rely on the categories of supplied metadata concerning the user which we believed could, at least in principle, be inferred from user behavior, either in the past or during the current information seeking episode. The experimental condition of the HARD track was for each site to submit at least one baseline run for the set of 50 topics, using only the title and (optionally) description fields for query construction. The results of the baseline run(s) were compared with the results from one or more experimental runs, which made use of the supplied searcher metadata, and of a clarification form submitted to the searcher, asking for whatever information each site thought would be useful in improving search results. We used only the supplied metadata, for the reasons stated above, and especially because we were interested in how to make initial queries better, rather than in how to conduct a dialogue with a searcher. There were five categories of searcher metadata for each topic (not all topics had values for all five): Genre, Familiarity, Geography, Granularity and Related text(s), which were intended to represent aspects of the searcher's context which might be useful in tailoring retrieval to the individual, and the individual situation. We made the assumption that at least some of these categories would be available to the IR system prior to (or in conjunction with) the specific search session, either through explicit or implicit evidence. Therefore, for us the HARD track experimental condition was designed to test whether knowledge of these contextual characteristics, and our specific ways of using that knowledge, would result in better retrieval performance than a good IR system without such knowledge. We understood that there would be, in general, two ways in which to take account of the metadata. One would be to modify the initial query from the (presumed) searcher, before submitting it for search; the other would be to search with the initial query, and then to modify (i.e. re-rank) the results before showing them to the searcher. We used both, but mainly concentrated on the latter of these techniques in taking account of the different types of metadata.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinCCLLLMSSYZ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinCCLLLMSSYZ04,
		author = {Nicholas J. Belkin and I. Chaleva and Michael J. Cole and Yuelin Li and Lu Liu and Ying{-}Hsang Liu and Gheorghe Muresan and Catherine L. Smith and Ying Sun and Xiaojun Yuan and Xiao{-}Min Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Rutgers' {HARD} Track Experiences at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/rutgers-belkin.hard.pdf},
		timestamp = {Wed, 24 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BelkinCCLLLMSSYZ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2004 HARD Track Experiments in Clustering

_David A. Evans, Jeffrey Bennett, Jesse Montgomery, Victor Sheftel, David A. Hull, James G. Shanahan_

- :fontawesome-solid-user-group: **Participant:** [clairvoyance](./HARD/participants.md#clairvoyance)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/clairvoyance.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/clairvoyance.hard.pdf)
- :material-file-search: **Runs:** [CL102TDN](./HARD/runs.md#cl102tdn) | [CLAI2](./HARD/runs.md#clai2) | [CLAI1](./HARD/runs.md#clai1)

??? abstract "Abstract"
	
	The Clairvoyance team participated in the High Accuracy Retrieval from Documents (HARD) Track of TREC 2004, submitting three runs. The principal hypothesis we have been pursuing is that small numbers of documents in clusters can provide a better basis for relevance feedback than ranked lists or, alternatively, than top-N pseudo-relevance feedback (PRF). Clustering of a query response can yield one or more groups of documents in which there are “significant” numbers (greater than 30%) of relevant documents; we expect the best results when such groups are selected for feedback. Following up on work we began in our TREC-2003 HARD-Track experiments [Shanahan et al. 2004], therefore, we continued to explore approaches to clustering query response sets to concentrate relevant documents, with the goal of (a) providing users (assessors) with better sets of documents to judge and (b) making the choices among sets easier to evaluate. Our experiments, thus, focused primarily on exploiting assessor feedback through clarification forms for query expansion and largely ignored other features of the documents or metadata. One of the submitted runs was a baseline automatic ad-hoc retrieval run. It used pseudo-relevance feedback, but no assessor judgments. Two non-baseline runs contrasted alternative strategies for clustering documents in the response set of a topic—one based on simple re-grouping of responding documents (our “standard” approach using quintad pseudo-clusters) and another based on reprocessing of the response set into small sub-documents (passages) and then clustering. In both cases, the grouped documents were presented to assessors in evaluation forms and the groups of documents selected as being on topic were used as the source of query expansion terms. A third version of the response set, based on summaries of sub-document clusters, was also submitted to assessors, but not as an official run. Our standard approach, using simple re-grouping of documents into quintad pseudo-clusters, proved robust and most effective, giving above-median performance. However, our attempt at producing more concentrated clusters of relevant information by using small sub-documents instead of whole documents in clusters proved to be largely unsuccessful. Upon further analysis, this result seems to derive more from the apparent difficulty assessors may have had in judging such sub-document clusters and less from the actual quality of the clusters or our ranking of them. We attribute this failure to our inability to discovery the best methods (parameters) for clustering a response set and to the limitations in representing the results of response-set analysis through the rather rigid forms interface to assessors. In the following sections, we provide the details of our work. Section 2 presents our processing approach and experiments, including examples of the assessor forms we produced. Section 3 gives a brief summary of our results. Section 4 offers an analysis of our work from the point of view of our primary hypotheses. Section 5 gives concluding thoughts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EvansBMSHS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/EvansBMSHS04,
		author = {David A. Evans and Jeffrey Bennett and Jesse Montgomery and Victor Sheftel and David A. Hull and James G. Shanahan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2004 {HARD} Track Experiments in Clustering},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/clairvoyance.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EvansBMSHS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Robert Gordon University's HARD Track Experiments at TREC  2004

_David J. Harper, Gheorghe Muresan, Bicheng Liu, Ivan Koychev, Dietrich Wettschereck, Nirmalie Wiratunga_

- :fontawesome-solid-user-group: **Participant:** [robert.gordon.u](./HARD/participants.md#robert.gordon.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/robertgordonu.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/robertgordonu.hard.pdf)
- :material-file-search: **Runs:** [RGU0](./HARD/runs.md#rgu0) | [RGUE1](./HARD/runs.md#rgue1) | [RGUE5](./HARD/runs.md#rgue5) | [RGUE6](./HARD/runs.md#rgue6) | [RGUE10](./HARD/runs.md#rgue10)

??? abstract "Abstract"
	
	The High Accuracy Retrieval from Documents (HARD) track explores methods of improving the accuracy of document retrieval systems. As part of this track, the participants have investigated how information about a searcher's context can be used to improve retrieval performance [Allan, 2003; Allan, 2004]. Searchers, referred to as assessors in this track, produce TREC-style search topics. Additionally, assessors are asked to specify values from pre-defined categories of metadata, that relate to the context of the search, as opposed to the topic of the search. The categories and values of the metadata used for the HARD track in 2004 are: Desired genre of documents, with values news, opinion-editorial, other, and any. Desired geographic treatment, with values USA, non-USA, and any. (Documents satisfying the USA metadata value may also refer to non-USA geographic areas, and vice versa.) Assessor's familiarity with the topic, with values much and little (or equivalently high and low). One or more documents related to the topic, but not from the collection to be searched. Desired granularity of response, with values passage and document. The work reported in this paper focuses on exploiting the genre, geographic and familiarity metadata. We refer to the combination of metadata category and value, e.g. genre/news, as a meta-pair.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HarperMLKWW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HarperMLKWW04,
		author = {David J. Harper and Gheorghe Muresan and Bicheng Liu and Ivan Koychev and Dietrich Wettschereck and Nirmalie Wiratunga},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Robert Gordon University's {HARD} Track Experiments at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/robertgordonu.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HarperMLKWW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improving Passage Retrieval Using Interactive Elicition and Statistical  Modeling

_Daqing He, Dina Demner-Fushman, Douglas W. Oard, Damianos G. Karakos, Sanjeev Khudanpur_

- :fontawesome-solid-user-group: **Participant:** [u.md.best.umiacs](./HARD/participants.md#u.md.best.umiacs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/umd-jhu.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/umd-jhu.hard.pdf)
- :material-file-search: **Runs:** [UMDBLTFAIDF](./HARD/runs.md#umdbltfaidf) | [UMDBLTITDES](./HARD/runs.md#umdbltitdes) | [UMDBLITFLOC](./HARD/runs.md#umdblitfloc) | [UMDBLBRF](./HARD/runs.md#umdblbrf) | [UMAREXPR1](./HARD/runs.md#umarexpr1) | [UMAREXPR3](./HARD/runs.md#umarexpr3) | [UMAREXPR5](./HARD/runs.md#umarexpr5)

??? abstract "Abstract"
	
	The University of Maryland and Johns Hopkins University worked together in the 2004 High Accuracy Retrieval from Documents (HARD) track to explore design options for interactive passage retrieval systems. HARD assessors responded to clarification forms by (1) selecting additional search terms from an automatically constructed list of potentially discriminating terms, (2) selected relevant passages from an automatically constructed list of possibly relevant passages, and (3) entered additional search terms. Query expansion based on these three types of elicited information yielded statistically significant improvements in R-precision over baselines with and without blind relevance feedback. For topics that requested passages as answers, a preliminary analysis shows that statistical models for passage extent trained on HARD 2003 data yielded a significant improvement over a replication of the University of Maryland's HARD-2003 technique for passage extent determination, and the results of the new technique appear to generally be well above the median for HARD 2004 systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeDOKK04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeDOKK04,
		author = {Daqing He and Dina Demner{-}Fushman and Douglas W. Oard and Damianos G. Karakos and Sanjeev Khudanpur},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Improving Passage Retrieval Using Interactive Elicition and Statistical Modeling},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/umd-jhu.hard.pdf},
		timestamp = {Sun, 22 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeDOKK04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2004: HARD and Genomics Tracks

_Xiangji Huang, Yan Rui Huang, Ming Zhong, Miao Wen_

- :fontawesome-solid-user-group: **Participant:** [york.u](./HARD/participants.md#york.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf)
- :material-file-search: **Runs:** [york04hb1](./HARD/runs.md#york04hb1) | [york04ha1](./HARD/runs.md#york04ha1) | [york04hm1](./HARD/runs.md#york04hm1) | [york04ha2](./HARD/runs.md#york04ha2) | [york04hm2](./HARD/runs.md#york04hm2)

??? abstract "Abstract"
	
	York University participated in HARD and Genomics tracks this year. For both tracks, we used Okapi BSS (basic search system) as the basis. Our experiments mainly focused on exploiting various methods for combining document and passage scores, new term weighting formulae and feedback methods for query expansion. For HARD track, we built two levels of indexes, and search against both indexes for each topic. Then we combine these two searches into one. For Genomics track, we used a new strategy to automatically expand search terms by using relevance feedback and combined retrieval results from different fields into the final result. We achieved good results on the HARD task and average results on the Genomics task. For the HARD passage level evaluation, the automatic run ‘yorku04ha1' obtained the best result (0.358) in terms of Bpref measure at 12K characters. The evaluation results show that Algorithm 1 is more effective than Algorithm 2 for the passage level retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangHZW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangHZW04,
		author = {Xiangji Huang and Yan Rui Huang and Ming Zhong and Miao Wen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2004: {HARD} and Genomics Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf},
		timestamp = {Tue, 05 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangHZW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2004: Novelty and HARD

_Nasreen Abdul Jaleel, James Allan, W. Bruce Croft, Fernando Diaz, Leah S. Larkey, Xiaoyan Li, Mark D. Smucker, Courtney Wade_

- :fontawesome-solid-user-group: **Participant:** [u.mass](./HARD/participants.md#u.mass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/umass.novelty.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/umass.novelty.hard.pdf)
- :material-file-search: **Runs:** [UMassBaseSVM](./HARD/runs.md#umassbasesvm) | [UMassBaseRM3](./HARD/runs.md#umassbaserm3) | [UMassBaseQL](./HARD/runs.md#umassbaseql) | [UMassVPMM](./HARD/runs.md#umassvpmm) | [UMassRGG](./HARD/runs.md#umassrgg) | [UMassCVC](./HARD/runs.md#umasscvc) | [UMassCFC](./HARD/runs.md#umasscfc) | [UMassC2](./HARD/runs.md#umassc2) | [UMassCMC](./HARD/runs.md#umasscmc) | [UMassCFMC](./HARD/runs.md#umasscfmc) | [UMassF](./HARD/runs.md#umassf) | [UMassMerge](./HARD/runs.md#umassmerge) | [UMassC3](./HARD/runs.md#umassc3)

??? abstract "Abstract"
	
	For the TREC 2004 Novelty track, UMass participated in all four tasks. Although finding relevant sentences was harder this year than last, we continue to show marked improvements over the baseline of calling all sentences relevant, with a variant of tfidf being the most successful approach. We achieve 5-9% improvements over the baseline in locating novel sentences, primarily by looking at the similarity of a sentence to earlier sentences and focusing on named entities. For the High Accuracy Retrieval from Documents (HARD) track, we investigated the use of clarification forms, fixed- and variable-length passage retrieval, and the use of metadata. Clarification form results indicate that passage level feedback can provide improvements comparable to user supplied related-text for document evaluation and outperforms related-text for passage evaluation. Document retrieval methods without a query expansion component show the most gains from related-text. We also found that displaying the top passages for feedback outperformed displaying centroid passages. Named entity feedback resulted in mixed performance. Our primary findings for passage retrieval are that document retrieval methods performed better than passage retrieval methods on the passage evaluation metric of binary preference at 12,000 characters, and that clarification forms improved passage retrieval for every retrieval method explored. We found no benefit to using variable-length passages over fixed-length passages for this corpus. Our use of geography and genre metadata resulted in no significant changes in retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JaleelACDLLSW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/JaleelACDLLSW04,
		author = {Nasreen Abdul Jaleel and James Allan and W. Bruce Croft and Fernando Diaz and Leah S. Larkey and Xiaoyan Li and Mark D. Smucker and Courtney Wade},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2004: Novelty and {HARD}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/umass.novelty.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JaleelACDLLSW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIUC in HARD 2004–Passage Retrieval Using HMMs

_Jing Jiang, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [u.illinois.uc](./HARD/participants.md#u.illinois.uc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uillinois-uc.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/uillinois-uc.hard.pdf)
- :material-file-search: **Runs:** [uiucHARDb0](./HARD/runs.md#uiuchardb0) | [uiucHARDb1](./HARD/runs.md#uiuchardb1) | [uiucHARDf0](./HARD/runs.md#uiuchardf0) | [uiucHARDf1](./HARD/runs.md#uiuchardf1) | [uiucHARDf2](./HARD/runs.md#uiuchardf2) | [uiucHARDf3](./HARD/runs.md#uiuchardf3)

??? abstract "Abstract"
	
	UIUC participated in the HARD track in TREC 2004 and focused on the evaluation of a new method for identifying variable-length passages using HMMs. Most existing approaches to passage retrieval rely on pre-segmentation of documents, but the optimal boundaries of a relevant passage depends on both the query and the document. Our new method aims at determining or improving the boundaries of a relevant passage based on both the query and topical coherence in the document. In this paper, we describe the method and present analysis of our HARD 2004 evaluation results. The results show that the HMM method can improve the boundaries of pre-segmented passages in terms of overall passage retrieval accuracy and recall, but at the price of precision sometimes. However, due to the non-optimality of the relevance feedback procedure and the poor ranking performance based on passage scoring, the best of our passage runs is still worse than a whole document baseline run. Further experiments and analysis are needed to fully understand why the language modeling approach did not work well on passage scoring.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangZ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangZ04,
		author = {Jing Jiang and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIUC} in {HARD} 2004--Passage Retrieval Using HMMs},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uillinois-uc.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangZ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of North Carolina's HARD Track Experiments at TREC  2004

_Diane Kelly, Vijay Deepak Dollu, Xin Fu_

- :fontawesome-solid-user-group: **Participant:** [u.northcarolina](./HARD/participants.md#u.northcarolina)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/unorthcarolina.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/unorthcarolina.hard.pdf)
- :material-file-search: **Runs:** [UNCHARDrun1](./HARD/runs.md#unchardrun1) | [UNCHARDq234](./HARD/runs.md#unchardq234) | [UNCHARDq2](./HARD/runs.md#unchardq2) | [UNCHARDtdn1](./HARD/runs.md#unchardtdn1) | [UNCHARDtdn2](./HARD/runs.md#unchardtdn2) | [UNCHARDq4](./HARD/runs.md#unchardq4) | [UNCHARDq3](./HARD/runs.md#unchardq3) | [UNCHARDq3q4](./HARD/runs.md#unchardq3q4) | [UNCHARDq2q3](./HARD/runs.md#unchardq2q3) | [UNCHARDq2q4](./HARD/runs.md#unchardq2q4) | [UNCHARDq2m](./HARD/runs.md#unchardq2m) | [UNCHARDq2q3m](./HARD/runs.md#unchardq2q3m) | [UNCHARDq234m](./HARD/runs.md#unchardq234m) | [UNCHARDq2q4m](./HARD/runs.md#unchardq2q4m) | [UNCHARDq3m](./HARD/runs.md#unchardq3m) | [UNCHARDq3q4m](./HARD/runs.md#unchardq3q4m) | [UNCHARDq4m](./HARD/runs.md#unchardq4m)

??? abstract "Abstract"
	
	In the experiment described in this paper, we investigate the effectiveness of a document-independent technique for eliciting additional information from searchers about their information problems. We propose that such a technique can be used to elicit terms for use in query expansion and as a follow-up when ambiguous queries are initially posed by searchers. We use a clarification form to obtain additional information from searchers and create a series of experimental runs based on the information that we obtained from this form. Although we were successful at eliciting more information from searchers, we were unable to demonstrate that this additional information increased performance because of an indexing error that resulted in very poor performance for our baseline and experimental runs. Additionally, we use our clarification form to investigate an alternative measure of topic familiarity and demonstrate how it relates to the length of searchers' topic descriptions and responses to our clarification form.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KellyDF04.bib) "
	```
	@inproceedings{DBLP:conf/trec/KellyDF04,
		author = {Diane Kelly and Vijay Deepak Dollu and Xin Fu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of North Carolina's {HARD} Track Experiments at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/unorthcarolina.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KellyDF04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Chicago at TREC 2004: HARD Track

_Gina-Anne Levow_

- :fontawesome-solid-user-group: **Participant:** [u.chichago](./HARD/participants.md#u.chichago)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uchichago.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/uchichago.hard.pdf)

??? abstract "Abstract"
	
	The University of Chicago participated in the Text Retrieval Conference 2004 (TREC 2004) HARD track. HARD track experiments focused on passage retrieval and exploitation of metadata information to increase accuracy under HARD-relevance criteria. Passage retrieval employed query-based repeated merger of 2-3 sentence pseudo-documents to extract tightly focused relevant passages. Lexical cues and statistical language modeling were applied to identify documents consistent with specified metadata criteria. Retrieval lists were reranked based on the quality of metadata match.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Levow04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Levow04,
		author = {Gina{-}Anne Levow},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Chicago at {TREC} 2004: {HARD} Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uchichago.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Levow04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Conceptual Language Models for Context-Aware Text Retrieval

_Henning Rode, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [utwente](./HARD/participants.md#utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/utwente.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/utwente.hard.pdf)
- :material-file-search: **Runs:** [utwenteB421](./HARD/runs.md#utwenteb421) | [utwenteB21](./HARD/runs.md#utwenteb21) | [utwenteB111](./HARD/runs.md#utwenteb111) | [utwenteM111](./HARD/runs.md#utwentem111)

??? abstract "Abstract"
	
	While participating in the HARD track our first question was, what an IR-application should look like that takes into account preference meta-data from the user, without the need of explicit (manual) meta-data tagging of the collection. Especially, we touch the question how contextual information can be described in an abstract model appropriate for the IR-task, which further allows improving and fine-tuning of the context representations by learning from the user. As a first result, we roughly sketch a system architecture and context representation based on statistical language models that fits well to the task of the HARD track. Furthermore, we discuss issues of ranking and score normalizations on this background.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RodeH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/RodeH04,
		author = {Henning Rode and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Conceptual Language Models for Context-Aware Text Retrieval},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/utwente.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RodeH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ISCAS at TREC 2004: HARD Track

_Le Sun, Junlin Zhang, Yufang Sun_

- :fontawesome-solid-user-group: **Participant:** [cas.sun](./HARD/participants.md#cas.sun)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/cas-sun.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/cas-sun.hard.pdf)
- :material-file-search: **Runs:** [ISCAS](./HARD/runs.md#iscas) | [chastdn](./HARD/runs.md#chastdn) | [chascfw](./HARD/runs.md#chascfw) | [chascfd](./HARD/runs.md#chascfd) | [chascfwd](./HARD/runs.md#chascfwd) | [chasbsubfam](./HARD/runs.md#chasbsubfam) | [chasbcsubfam](./HARD/runs.md#chasbcsubfam) | [chascfsubfam](./HARD/runs.md#chascfsubfam) | [chasccsubfam](./HARD/runs.md#chasccsubfam) | [chasbaserel](./HARD/runs.md#chasbaserel) | [chasbasegen](./HARD/runs.md#chasbasegen) | [chasbaseger](./HARD/runs.md#chasbaseger) | [chascfrel](./HARD/runs.md#chascfrel) | [chascfgen](./HARD/runs.md#chascfgen) | [chascfger](./HARD/runs.md#chascfger) | [chasregenger](./HARD/runs.md#chasregenger) | [chasdcfd](./HARD/runs.md#chasdcfd) | [chasdcfwd](./HARD/runs.md#chasdcfwd) | [chasdcfw](./HARD/runs.md#chasdcfw)

??? abstract "Abstract"
	
	Institute of Software, Chinese Academy of Sciences (ISCAS) participated in TREC-2004, submitting 18 runs. We focus on studying the problem of the combination of the user- and query-information from clarification forms and metadata. We provided two kinds of Clarification Form. Our experiment shows the CF2 is more effective than CF1. We use Google as a resource for query expansion base on metadata subject and familiarity together, and the R-prec is increased from 0.2308 (baseline) to 0.2646 (+14.6%). Our approach to exploiting the metadata Genre and Geography yield negative result when used alone, however, surprisedly, when combinate metadata Genre and metadata Geography with CF2 respectively, we get an increase (+1.2%) and (+5.4%) than use CF2 alone. Our combination of CF2 and metadata relt_text is the best results of all the TREC runs (R-prec), and in this run, the R-prec is increased from 0.3303 (CF2 alone) to 0.3766 (+14%), and from 0.2888 (metadata rel-text alone) to 0.3766 (+30.4%). From the results we can see the information from user (CF2) and the information from query (metadata relt-text) may complement each other.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SunZS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SunZS04,
		author = {Le Sun and Junlin Zhang and Yufang Sun},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ISCAS} at {TREC} 2004: {HARD} Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/cas-sun.hard.pdf},
		timestamp = {Fri, 21 Aug 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SunZS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Approaches to High Accuracy Retrieval: Phrase-Based Search Experiments  in the HARD Track

_Olga Vechtomova, Murat Karamuftuoglu_

- :fontawesome-solid-user-group: **Participant:** [u.waterloo.vechtomova](./HARD/participants.md#u.waterloo.vechtomova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uwaterloo-bilkent.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/uwaterloo-bilkent.hard.pdf)
- :material-file-search: **Runs:** [UwatBaseTD](./HARD/runs.md#uwatbasetd) | [UwatBaseT](./HARD/runs.md#uwatbaset) | [UWATexp1](./HARD/runs.md#uwatexp1) | [UWATexp2](./HARD/runs.md#uwatexp2) | [UWATexp3](./HARD/runs.md#uwatexp3) | [UWATexp4](./HARD/runs.md#uwatexp4) | [UWATexp5](./HARD/runs.md#uwatexp5) | [UWATexp6](./HARD/runs.md#uwatexp6)

??? abstract "Abstract"
	
	Our main research focus this year was on the use of phrases (or multi-word units) in query expansion. Multi-word units (MWUs) comprise a number of lexical units, such as named entities (“United Nations”), nominal compounds (“amusement park”) and phrasal verbs (‘check in'). Although MWUs can belong to different parts of speech, our focus was on nominal MWUs. We used a combined syntactico-statistical approach for selecting nominal MWUs. In the first selection pass we obtained valid noun phrases, and in the second pass we used statistical measures to select strongly bound MWUs. We have experimented with using two statistical measures of selecting MWUs from text: the C-value (Frantzi and Ananiadou 1996, Vintar 2004) and the Log-Likelihood ratio (Dunning 1993). Selected MWUs were then suggested to the user for interactive query expansion. Two main research questions were studied in these experiments: Whether nominal MWUs which exhibit strong degree of stability in the corpus are better candidates for interactive query expansion than nominal MWUs selected by the frequency parameters of the individual terms they contain; Whether nominal MWUs are better candidates for interactive query expansion than single terms. In more detail these experiments are presented in section 2.2. The second focus of this work is on studying the effectiveness of noun phrases in document ranking. We have developed a new method of phrase-based document re-ranking, which addresses the problem of weighting overlapping phrases in documents, which in statistical IR models, such as probabilistic leads to the over-inflation of the document score. The method is described in detail in section 2.3.1. In section 3 we present the evaluation results, and in section 4 we discuss the differences in query expansion and retrieval performance between queries formulated by users with low and high familiarity with the topic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VechtomovaK04.bib) "
	```
	@inproceedings{DBLP:conf/trec/VechtomovaK04,
		author = {Olga Vechtomova and Murat Karamuftuoglu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Approaches to High Accuracy Retrieval: Phrase-Based Search Experiments in the {HARD} Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uwaterloo-bilkent.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VechtomovaK04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2004 Genomics, Hard, Robust and Web Tracks

_Kiduk Yang, Ning Yu, Adam Wead, Gavin La Rowe, Yu-Hsiu Li, Christopher Friend, Yoon Lee_

- :fontawesome-solid-user-group: **Participant:** [indiana.u.yang](./HARD/participants.md#indiana.u.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf](http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf)
- :material-file-search: **Runs:** [wdoqlz](./HARD/runs.md#wdoqlz) | [wdvqlz](./HARD/runs.md#wdvqlz) | [wdvqlz1](./HARD/runs.md#wdvqlz1) | [wdoqlz1](./HARD/runs.md#wdoqlz1) | [wdvqlzp](./HARD/runs.md#wdvqlzp) | [wdvqlzcf1](./HARD/runs.md#wdvqlzcf1)

??? abstract "Abstract"
	
	To facilitate understanding of information as well as its discovery, we need to combine the capabilities of the human and the machine as well as multiple methods and sources of evidence. Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science houses several projects that aim to apply this idea of multi-level fusion in the areas of information retrieval and knowledge organization. The TREC research group of WIDIT, who engages in examination of information retrieval strategies that can accommodate a variety of data environments and search tasks, participated in the Genomics, HARD, Robust, and Web tracks in TREC-2004. The basic approach of WIDIT was to leverage multiple sources of evidence, combine multiple methods, and integrate the strengths of man and the machine. Our main strategies for the tracks were: the use of gene name thesaurus in the Genomics track; query expansion and relevance feedback in the HARD track; query expansion with keywords from Web search in the Robust track, and the interactive system tuning process called “Dynamic Tuning” in the Web track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYWRLFL04.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYWRLFL04,
		author = {Kiduk Yang and Ning Yu and Adam Wead and Gavin La Rowe and Yu{-}Hsiu Li and Christopher Friend and Yoon Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2004 Genomics, Hard, Robust and Web Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf},
		timestamp = {Tue, 24 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangYWRLFL04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC 13: Web and Hard Tracks

_Hugo Zaragoza, Nick Craswell, Michael J. Taylor, Suchi Saria, Stephen E. Robertson_

- :fontawesome-solid-user-group: **Participant:** [microsoft.robertson](./HARD/participants.md#microsoft.robertson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/microsoft-cambridge.web.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/microsoft-cambridge.web.hard.pdf)
- :material-file-search: **Runs:** [MSRCBaseline](./HARD/runs.md#msrcbaseline) | [MSRCh4SD](./HARD/runs.md#msrch4sd) | [MSRCh4SSnGBD](./HARD/runs.md#msrch4ssngbd) | [MSRCh4SSnGB](./HARD/runs.md#msrch4ssngb) | [MSRCh4SSnG](./HARD/runs.md#msrch4ssng) | [MSRCh4SSnB](./HARD/runs.md#msrch4ssnb) | [MSRCh4SSn](./HARD/runs.md#msrch4ssn) | [MSRCh4SGB](./HARD/runs.md#msrch4sgb) | [MSRCh4SG](./HARD/runs.md#msrch4sg)

??? abstract "Abstract"
	
	All our submissions from the Microsoft Research Cambridge (MSRC) team this year continue to explore issues in IR from a perspective very close to that of the original Okapi team, working first at City University of London, and then at MSRC. A summary of the contributions by the team, from TRECs 1 to 7 is presented in [3]. In this work, weighting schemes for ad-hoc retrieval were developed, inspired by a probabilistic interpretation of relevance; this lead, for instance, to the successful BM25 weighting function. These weighting schemes were extended to deal with pseudo relevance feedback (blind feedback). Furthermore, the Okapi team participated in most of the early interactive tracks, and also developed iterative relevance feedback strategies for the routing task. Following up on the routing work, TRECs 7-11 submissions dealt principally with the adaptive filtering task; this work is summarised in [5]. Last year MSRC entered only the HARD track, concentrating on the use of the clarification forms [6]. We hoped to make use of the query expansion methods developed for filtering in the context of feedback on snippets in the clarification forms. However, our methods were not very successful. In this year's TREC we took part in the HARD and WEB tracks. In HARD, we tried some variations on the process of feature selection for query expansion. On the WEB track, we investigated the combination of information from different content fields and from link-based features. Section 3 briefly describes the system we used. Section 4 describes our HARD participation and Section 5 our TREC participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZaragozaCTSR04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZaragozaCTSR04,
		author = {Hugo Zaragoza and Nick Craswell and Michael J. Taylor and Suchi Saria and Stephen E. Robertson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Cambridge at {TREC} 13: Web and Hard Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/microsoft-cambridge.web.hard.pdf},
		timestamp = {Tue, 04 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZaragozaCTSR04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Novelty 

#### Overview of the TREC 2004 Novelty Track

_Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/NOVELTY.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec13/papers/NOVELTY.OVERVIEW.pdf)
??? abstract "Abstract"
	
	TREC 2004 marks the third and final year for the novelty track. The task is as follows: Given a TREC topic and an ordered list of documents, systems must find the relevant and novel sentences that should be returned to the user from this set. This task integrates aspects of passage retrieval and information filtering. As in 2003, there were two categories of topics - events and opinions - and four subtasks which provided systems with varying amounts of relevance or novelty information as training data. This year, the task was made harder by the inclusion of some number of irrelevant documents in document sets. Fourteen groups participated in the track this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Soboroff04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Soboroff04,
		author = {Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2004 Novelty Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/NOVELTY.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Soboroff04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Terabyte Searching, Genomic Retrieval and Novelty Detection  for TREC 2004

_Stephen Blott, Fabrice Camous, Paul Ferguson, Georgina Gaughan, Cathal Gurrin, Gareth J. F. Jones, Noel Murphy, Noel E. O'Connor, Alan F. Smeaton, Peter Wilkins, Oisín Boydell, Barry Smyth_

- :fontawesome-solid-user-group: **Participant:** [dubblincity.u](./novelty/participants.md#dubblincity.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf)
- :material-file-search: **Runs:** [cdvp4QePnD2](./novelty/runs.md#cdvp4qepnd2) | [cdvp4CnQry2](./novelty/runs.md#cdvp4cnqry2) | [cdvp4QePDPC2](./novelty/runs.md#cdvp4qepdpc2) | [cdvp4CnS101](./novelty/runs.md#cdvp4cns101) | [cdvp4QeSnD1](./novelty/runs.md#cdvp4qesnd1) | [cdvp4UnHis3](./novelty/runs.md#cdvp4unhis3) | [cdvp4NSen4](./novelty/runs.md#cdvp4nsen4) | [cdvp4NTerFr3](./novelty/runs.md#cdvp4nterfr3) | [cdvp4NTerFr1](./novelty/runs.md#cdvp4nterfr1) | [cdvp4NSnoH4](./novelty/runs.md#cdvp4nsnoh4)

??? abstract "Abstract"
	
	In TREC2004, Dublin City University took part in three tracks, Terabyte (in collaboration with University College Dublin), Genomic and Novelty. In this paper we will discuss each track separately and present separate conclusions from this work. In addition, we present a general description of a text retrieval engine that we have developed in the last year to support our experiments into large scale, distributed information retrieval, which underlies all of the track experiments described in this document.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BlottCFGGJMOSWBS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/BlottCFGGJMOSWBS04,
		author = {Stephen Blott and Fabrice Camous and Paul Ferguson and Georgina Gaughan and Cathal Gurrin and Gareth J. F. Jones and Noel Murphy and Noel E. O'Connor and Alan F. Smeaton and Peter Wilkins and Ois{\'{\i}}n Boydell and Barry Smyth},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Terabyte Searching, Genomic Retrieval and Novelty Detection for {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BlottCFGGJMOSWBS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Hidden Markov Model for the TREC Novelty Task

_John M. Conroy_

- :fontawesome-solid-user-group: **Participant:** [ida.ccs.nsa](./novelty/participants.md#ida.ccs.nsa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ida-ccs-conroy.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/ida-ccs-conroy.novelty.pdf)
- :material-file-search: **Runs:** [ccs3fqrt1](./novelty/runs.md#ccs3fqrt1) | [ccs1f0t1](./novelty/runs.md#ccs1f0t1) | [ccs1ftop0t1](./novelty/runs.md#ccs1ftop0t1) | [ccs3ftop0t1](./novelty/runs.md#ccs3ftop0t1) | [ccs3fmmrt1](./novelty/runs.md#ccs3fmmrt1) | [ccs3fmmr95t3](./novelty/runs.md#ccs3fmmr95t3) | [ccsqrt2](./novelty/runs.md#ccsqrt2) | [ccsmmr2t2](./novelty/runs.md#ccsmmr2t2) | [ccsmmr3t2](./novelty/runs.md#ccsmmr3t2) | [ccsmmr5t2](./novelty/runs.md#ccsmmr5t2) | [ccsmmr4t2](./novelty/runs.md#ccsmmr4t2) | [ccsfbmmrt3](./novelty/runs.md#ccsfbmmrt3) | [ccs3fmmrt3](./novelty/runs.md#ccs3fmmrt3) | [ccs3fbqrt3](./novelty/runs.md#ccs3fbqrt3)

??? abstract "Abstract"
	
	The algorithms for choosing relevant sentences were tuned versions of those presented in the past DUC evaluations and TREC 2003 (see [4, 5, 10] [11] for more details). The enhancements to the previous system are detailed in Section 3. Two methods were explored to find a subset of the relevant sentences that had good coverage but low redundancy. In the multi-document summarization system, the QR algorithm is used on term-sentence matrices. For this work, the method of maximum marginal relevance was also employed. The evaluation of these methods is discussed in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Conroy04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Conroy04,
		author = {John M. Conroy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Hidden Markov Model for the {TREC} Novelty Task},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ida-ccs-conroy.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Conroy04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Novelty Track at IRIT-SIG

_Taoufiq Dkaki, Josiane Mothe_

- :fontawesome-solid-user-group: **Participant:** [irit.sig.boughanem](./novelty/participants.md#irit.sig.boughanem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/irit-sig.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/irit-sig.novelty.pdf)
- :material-file-search: **Runs:** [IRITT1](./novelty/runs.md#iritt1) | [IRITT2](./novelty/runs.md#iritt2) | [IRITT3](./novelty/runs.md#iritt3) | [IRITT4](./novelty/runs.md#iritt4) | [IRITT5](./novelty/runs.md#iritt5) | [IritTask2](./novelty/runs.md#irittask2) | [Irit2T2](./novelty/runs.md#irit2t2) | [Irit2Task3](./novelty/runs.md#irit2task3) | [Irit3Task3](./novelty/runs.md#irit3task3) | [Irit4Task3](./novelty/runs.md#irit4task3) | [Irit5Task3](./novelty/runs.md#irit5task3) | [Irit1T3](./novelty/runs.md#irit1t3)

??? abstract "Abstract"
	
	In TREC 2004, IRIT modified important features of the strategy that was developed for TREC 2003. Changes include tuning parameter values, topic expansion and exploitation of sentences context. According to our method, a sentence is considered as relevant if it matches the topic with a certain level of coverage. This coverage depends on the category of the terms used in the texts. Four types of terms have been defined highly relevant, scarcely relevant, non-relevant (like stop words), highly non-relevant terms (negative terms). Term categorization is based on topic analysis: highly non-relevant terms are extracted from the narrative parts that describe what will be a non-relevant document. The three other types of terms are extracted from the rest of the query. Each term of a topic is weighted according to both its occurrence and the topic part it belongs to (title, descriptive, narrative). Additionally we increase the score of a sentence when either the previous or the next sentence is relevant. When topic expansion is applied, terms from relevant sentences (task 3) or from the first retrieved sentences (task 1) are added to the initial terms. With regard to the novelty part, a sentence is considered as novel if its similarity with each of previously processed -and selected as novel- sentences does not exceed a certain threshold. In addition, this sentence should not be too similar to a virtual sentence made of the n best-matching and previously selected sentences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DkakiM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/DkakiM04,
		author = {Taoufiq Dkaki and Josiane Mothe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Novelty Track at {IRIT-SIG}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/irit-sig.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DkakiM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Novelty, Question Answering and Genomics: The University of Iowa Response

_David Eichmann, Yi Zhang, Shannon Bradshaw, Xin Ying Qiu, Li Zhou, Padmini Srinivasan, Aditya Kumar Sehgal, Hudon Wong_

- :fontawesome-solid-user-group: **Participant:** [u.iowa](./novelty/participants.md#u.iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf)
- :material-file-search: **Runs:** [UIowa04Nov14](./novelty/runs.md#uiowa04nov14) | [UIowa04Nov15](./novelty/runs.md#uiowa04nov15) | [UIowa04Nov11](./novelty/runs.md#uiowa04nov11) | [UIowa04Nov12](./novelty/runs.md#uiowa04nov12) | [UIowa04Nov13](./novelty/runs.md#uiowa04nov13) | [UIowa04Nov21](./novelty/runs.md#uiowa04nov21) | [UIowa04Nov31](./novelty/runs.md#uiowa04nov31) | [UIowa04Nov41](./novelty/runs.md#uiowa04nov41) | [UIowa04Nov22](./novelty/runs.md#uiowa04nov22) | [UIowa04Nov32](./novelty/runs.md#uiowa04nov32) | [UIowa04Nov42](./novelty/runs.md#uiowa04nov42) | [UIowa04Nov23](./novelty/runs.md#uiowa04nov23) | [UIowa04Nov24](./novelty/runs.md#uiowa04nov24) | [UIowa04Nov25](./novelty/runs.md#uiowa04nov25) | [UIowa04Nov33](./novelty/runs.md#uiowa04nov33) | [UIowa04Nov34](./novelty/runs.md#uiowa04nov34) | [UIowa04Nov35](./novelty/runs.md#uiowa04nov35) | [UIowa04Nov43](./novelty/runs.md#uiowa04nov43) | [UIowa04Nov44](./novelty/runs.md#uiowa04nov44) | [UIowa04Nov45](./novelty/runs.md#uiowa04nov45)

??? abstract "Abstract"
	
	Our system for novelty this year comprises three distinct variations. The first is a refinement of that used for last year involving named entity occurrences and functions as a comparative baseline. The second variation extends the baseline system in an exploration of the connection between word sense and novelty. The third variation involves more statistical similarity schemes in the positive sense for relevance and the negative sense for novelty.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannZBQZSSW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannZBQZSSW04,
		author = {David Eichmann and Yi Zhang and Shannon Bradshaw and Xin Ying Qiu and Li Zhou and Padmini Srinivasan and Aditya Kumar Sehgal and Hudon Wong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Novelty, Question Answering and Genomics: The University of Iowa Response},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannZBQZSSW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Michigan in Novelty 2004

_Günes Erkan_

- :fontawesome-solid-user-group: **Participant:** [u.michigan](./novelty/participants.md#u.michigan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/umichigan.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/umichigan.novelty.pdf)
- :material-file-search: **Runs:** [umich0411](./novelty/runs.md#umich0411) | [umich0412](./novelty/runs.md#umich0412) | [umich0413](./novelty/runs.md#umich0413) | [umich0414](./novelty/runs.md#umich0414) | [umich0415](./novelty/runs.md#umich0415) | [umich0421](./novelty/runs.md#umich0421) | [umich0422](./novelty/runs.md#umich0422) | [umich0423](./novelty/runs.md#umich0423) | [umich0424](./novelty/runs.md#umich0424) | [umich0425](./novelty/runs.md#umich0425) | [umich0433](./novelty/runs.md#umich0433) | [umich0431](./novelty/runs.md#umich0431) | [umich0432](./novelty/runs.md#umich0432) | [umich0434](./novelty/runs.md#umich0434) | [umich0435](./novelty/runs.md#umich0435) | [umich0441](./novelty/runs.md#umich0441) | [umich0442](./novelty/runs.md#umich0442) | [umich0443](./novelty/runs.md#umich0443) | [umich0444](./novelty/runs.md#umich0444)

??? abstract "Abstract"
	
	This year we participated in the Novelty track. To find the relevant sentences, we combine sentence salience features that are inherited from text summarization domain with other heuristic features based on topic statements. We propose a novel method to extract the new sentences based on the graph-based ranking of the similarity relation between the sentences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Erkan04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Erkan04,
		author = {G{\"{u}}nes Erkan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Michigan in Novelty 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/umichigan.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Erkan04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2004: Novelty and HARD

_Nasreen Abdul Jaleel, James Allan, W. Bruce Croft, Fernando Diaz, Leah S. Larkey, Xiaoyan Li, Mark D. Smucker, Courtney Wade_

- :fontawesome-solid-user-group: **Participant:** [u.mass](./novelty/participants.md#u.mass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/umass.novelty.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/umass.novelty.hard.pdf)
- :material-file-search: **Runs:** [CIIRT1R2](./novelty/runs.md#ciirt1r2) | [CIIRT1R1](./novelty/runs.md#ciirt1r1) | [CIIRT1R3](./novelty/runs.md#ciirt1r3) | [CIIRT1R5](./novelty/runs.md#ciirt1r5) | [CIIRT1R6](./novelty/runs.md#ciirt1r6) | [CIIRT3R1](./novelty/runs.md#ciirt3r1) | [CIIRT3R2](./novelty/runs.md#ciirt3r2) | [CIIRT3R3](./novelty/runs.md#ciirt3r3) | [CIIRT2R1](./novelty/runs.md#ciirt2r1) | [CIIRT2R2](./novelty/runs.md#ciirt2r2) | [CIIRT3R4](./novelty/runs.md#ciirt3r4) | [CIIRT3R5](./novelty/runs.md#ciirt3r5) | [CIIRT4R1](./novelty/runs.md#ciirt4r1) | [CIIRT4R2](./novelty/runs.md#ciirt4r2) | [CIIRT4R3](./novelty/runs.md#ciirt4r3)

??? abstract "Abstract"
	
	For the TREC 2004 Novelty track, UMass participated in all four tasks. Although finding relevant sentences was harder this year than last, we continue to show marked improvements over the baseline of calling all sentences relevant, with a variant of tfidf being the most successful approach. We achieve 5-9% improvements over the baseline in locating novel sentences, primarily by looking at the similarity of a sentence to earlier sentences and focusing on named entities. For the High Accuracy Retrieval from Documents (HARD) track, we investigated the use of clarification forms, fixed- and variable-length passage retrieval, and the use of metadata. Clarification form results indicate that passage level feedback can provide improvements comparable to user supplied related-text for document evaluation and outperforms related-text for passage evaluation. Document retrieval methods without a query expansion component show the most gains from related-text. We also found that displaying the top passages for feedback outperformed displaying centroid passages. Named entity feedback resulted in mixed performance. Our primary findings for passage retrieval are that document retrieval methods performed better than passage retrieval methods on the passage evaluation metric of binary preference at 12,000 characters, and that clarification forms improved passage retrieval for every retrieval method explored. We found no benefit to using variable-length passages over fixed-length passages for this corpus. Our use of geography and genre metadata resulted in no significant changes in retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JaleelACDLLSW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/JaleelACDLLSW04,
		author = {Nasreen Abdul Jaleel and James Allan and W. Bruce Croft and Fernando Diaz and Leah S. Larkey and Xiaoyan Li and Mark D. Smucker and Courtney Wade},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2004: Novelty and {HARD}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/umass.novelty.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JaleelACDLLSW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ISI Novelty Track System for TREC 2004

_Soo-Min Kim, Deepak Ravichandran, Eduard H. Hovy_

- :fontawesome-solid-user-group: **Participant:** [usc.isi.kim](./novelty/participants.md#usc.isi.kim)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/usc-isi.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/usc-isi.novelty.pdf)
- :material-file-search: **Runs:** [ISIALL04](./novelty/runs.md#isiall04) | [ISIRUN204](./novelty/runs.md#isirun204) | [ISIRUN304](./novelty/runs.md#isirun304) | [ISIRUN404](./novelty/runs.md#isirun404) | [ISIRUN504](./novelty/runs.md#isirun504)

??? abstract "Abstract"
	
	We describe our system developed at ISI for the Novelty track at TREC 2004. The system's two modules recognize relevant event and opinion sentences respectively. We focused mainly on recognizing relevant opinion sentences using various opinion-bearing word lists. Of our 5 runs submitted for task 1, the best run provided an F-score of 0.390 (precision 0.30 and recall 0.71).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KimRH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/KimRH04,
		author = {Soo{-}Min Kim and Deepak Ravichandran and Eduard H. Hovy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ISI} Novelty Track System for {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/usc-isi.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KimRH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evolving XML and Dictionary Strategies for Question Answering and  Novelty Tasks

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./novelty/participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/clresearch.qa.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/clresearch.qa.novelty.pdf)
- :material-file-search: **Runs:** [clr04n1h2](./novelty/runs.md#clr04n1h2) | [clr04n1h3](./novelty/runs.md#clr04n1h3) | [clr04n2](./novelty/runs.md#clr04n2) | [clr04n3h1f1](./novelty/runs.md#clr04n3h1f1) | [clr04n3h1f2](./novelty/runs.md#clr04n3h1f2) | [clr04n3h2f1](./novelty/runs.md#clr04n3h2f1) | [clr04n3h2f2](./novelty/runs.md#clr04n3h2f2) | [clr04n4](./novelty/runs.md#clr04n4)

??? abstract "Abstract"
	
	CL Research participated in the question answering and novelty tracks in TREC 2004. The Knowledge Management System (KMS), which provides a single interface for question answering, text summarization, information extraction, and document exploration, was used for these tasks. Question answering is performed directly within KMS, which answers questions either from a repository or the Internet. The novelty task was performed with the XML Analyzer, which includes many of the functions used in the KMS summarization routines. These tasks are based on creating and exploiting an XML representation of the texts used for these two tracks. For the QA track, we submitted one run and our overall score was 0.156, with scores of 0.161 for factoid questions, 0.064 for list questions, and 0.239 for “other” questions; these scores are significantly improved from TREC 2003. For the novelty track, we submitted two runs for task 1, one run for task 2, four runs for task 3, and one run for task 4. For most tasks, our scores were above the median. We describe our system in some detail, particularly emphasizing strategies that are emerging in the use of XML and lexical resources for the question answering and novelty tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Litkowski04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Litkowski04,
		author = {Kenneth C. Litkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Evolving {XML} and Dictionary Strategies for Question Answering and Novelty Tasks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/clresearch.qa.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Litkowski04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improved Feature Selection and Redundance Computing - THUIR at TREC  2004 Novelty Track

_Liyun Ru, Le Zhao, Min Zhang, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghua.ma](./novelty/participants.md#tsinghua.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.novelty.pdf)
- :material-file-search: **Runs:** [THUIRnv0411](./novelty/runs.md#thuirnv0411) | [THUIRnv0412](./novelty/runs.md#thuirnv0412) | [THUIRnv0413](./novelty/runs.md#thuirnv0413) | [THUIRnv0414](./novelty/runs.md#thuirnv0414) | [THUIRnv0415](./novelty/runs.md#thuirnv0415) | [THUIRnv0421](./novelty/runs.md#thuirnv0421) | [THUIRnv0422](./novelty/runs.md#thuirnv0422) | [THUIRnv0424](./novelty/runs.md#thuirnv0424) | [THUIRnv0423](./novelty/runs.md#thuirnv0423) | [THUIRnv0425](./novelty/runs.md#thuirnv0425) | [THUIRnv0431](./novelty/runs.md#thuirnv0431) | [THUIRnv0432](./novelty/runs.md#thuirnv0432) | [THUIRnv0433](./novelty/runs.md#thuirnv0433) | [THUIRnv0434](./novelty/runs.md#thuirnv0434) | [THUIRnv0435](./novelty/runs.md#thuirnv0435) | [THUIRnv0441](./novelty/runs.md#thuirnv0441) | [THUIRnv0442](./novelty/runs.md#thuirnv0442) | [THUIRnv0443](./novelty/runs.md#thuirnv0443) | [THUIRnv0444](./novelty/runs.md#thuirnv0444) | [THUIRnv0445](./novelty/runs.md#thuirnv0445)

??? abstract "Abstract"
	
	This is the third years that Tsinghua University Information Retrieval Group (THUIR) participates in Novelty task of TREC. Our research on this year's novelty track mainly focused on four aspects: (1) text feature selection and reduction; (2) improved sentence classification in finding relevant information; (3)efficient sentence redundancy computing; (4) effective result filtering. All experiments have been performed on TMiner IR system, developed by THU IR group last year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuZZM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuZZM04,
		author = {Liyun Ru and Le Zhao and Min Zhang and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Improved Feature Selection and Redundance Computing - {THUIR} at {TREC} 2004 Novelty Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuZZM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Columbia University in the Novelty Track at TREC 2004

_Barry Schiffman, Kathleen R. McKeown_

- :fontawesome-solid-user-group: **Participant:** [columbia.u.schiffman](./novelty/participants.md#columbia.u.schiffman)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/columbiau.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/columbiau.novelty.pdf)
- :material-file-search: **Runs:** [novcolp1](./novelty/runs.md#novcolp1) | [novcolp2](./novelty/runs.md#novcolp2) | [novcolrcl](./novelty/runs.md#novcolrcl) | [novcosine](./novelty/runs.md#novcosine) | [novcombo](./novelty/runs.md#novcombo)

??? abstract "Abstract"
	
	Our system for the Novelty Track at TREC 2004 looks beyond sentence boundaries as well as within sentences to identify novel, nonduplicative passages. It tries to identify text spans of two or more sentences that encompass mini-segments of new information. At the same time, we avoid any pairwise comparison of sentences, but rely on the presence of previously unseen terms to provide evidence of novelty. The system is guided by a number of parameters, both weights and thresholds, that are learned automatically with a randomized hill-climbing algorithm. During learning, we varied the target function to produce configurations that emphasize either precision or recall. We also implemented a straightforward vector-space model as a comparison and to test a combined approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchiffmanM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchiffmanM04,
		author = {Barry Schiffman and Kathleen R. McKeown},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Columbia University in the Novelty Track at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/columbiau.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchiffmanM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Meiji University Web, Novelty and Genomic Track Experiments

_Tomoe Tomiyama, Kosuke Karoji, Takeshi Kondo, Yuichi Kakuta, Tomohiro Takagi_

- :fontawesome-solid-user-group: **Participant:** [meiji.u](./novelty/participants.md#meiji.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf)
- :material-file-search: **Runs:** [HIL10](./novelty/runs.md#hil10) | [MeijiHIL1cfs](./novelty/runs.md#meijihil1cfs) | [MeijiHIL1odp](./novelty/runs.md#meijihil1odp) | [MeijiHIL2RS](./novelty/runs.md#meijihil2rs) | [MeijiHIL3](./novelty/runs.md#meijihil3) | [MeijiHIL2WRS](./novelty/runs.md#meijihil2wrs) | [MeijiHIL2WR](./novelty/runs.md#meijihil2wr) | [MeijiHIL3Tc](./novelty/runs.md#meijihil3tc) | [MeijiHIL3TSc](./novelty/runs.md#meijihil3tsc) | [MeijiHIL2WCS](./novelty/runs.md#meijihil2wcs) | [MeijiHIL2CS](./novelty/runs.md#meijihil2cs) | [MeijiHIL4WRS](./novelty/runs.md#meijihil4wrs) | [MeijiHIL4WR](./novelty/runs.md#meijihil4wr) | [MeijiHIL4WRc](./novelty/runs.md#meijihil4wrc) | [MeijiHIL4RS](./novelty/runs.md#meijihil4rs) | [MeijiHIL4RSc](./novelty/runs.md#meijihil4rsc)

??? abstract "Abstract"
	
	We participated in Novelty track, the topic distillation task of Web track and ad hoc task of Genomic Track. Our main challenge is to deal with meaning of words and improve retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TomiyamaKKKT04.bib) "
	```
	@inproceedings{DBLP:conf/trec/TomiyamaKKKT04,
		author = {Tomoe Tomiyama and Kosuke Karoji and Takeshi Kondo and Yuichi Kakuta and Tomohiro Takagi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Meiji University Web, Novelty and Genomic Track Experiments},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TomiyamaKKKT04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Similarity Computation in Novelty Detection and Biomedical Text Categorization

_Ming-Feng Tsai, Ming-Hung Hsu, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./novelty/participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ntu.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/ntu.novelty.pdf)
- :material-file-search: **Runs:** [NTU11](./novelty/runs.md#ntu11) | [NTU12](./novelty/runs.md#ntu12) | [NTU13](./novelty/runs.md#ntu13) | [NTU14](./novelty/runs.md#ntu14) | [NTU15](./novelty/runs.md#ntu15) | [NTU21](./novelty/runs.md#ntu21) | [NTU22](./novelty/runs.md#ntu22) | [NTU23](./novelty/runs.md#ntu23) | [NTU24](./novelty/runs.md#ntu24) | [NTU25](./novelty/runs.md#ntu25)

??? abstract "Abstract"
	
	The novelty track was first introduced in TREC 2002. Given a TREC topic, the goal of this task in 2004 is to locate relevant and new information from a set of documents. From the results in TREC 2002 and 2003, we realized the major challenging issue of recognizing relevant sentences is the lack of information used in similarity computation among sentences. In this year, we utilized the method based on variants of employing an information retrieval (IR) system to find relevant and novel sentences. This methodology is called IR with reference corpus, which can also be considered as an information expansion of sentences. A sentence is considered as a query of a reference corpus, and similarity between sentences is measured in terms of the weighting vectors of document lists ranked by IR systems. Basically, relevant sentences are extracted by comparing their results on a certain information retrieval system. Two sentences are regarded as similar if their corresponding returned document lists by the IR system are similar. In novelty parts, we used similar approach to extract novel sentences from the sentences of the relevant part. An effectively dynamic threshold setting approach that is based on what percentage of relevant sentences is within a relevant document is presented. In this paper, we paid attention to three points: first, how to utilize the results of an IR system to compare the similarity between sentences; second, how to filter out the redundant sentences; third, how to determine appropriate relevance and novelty threshold.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TsaiHC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/TsaiHC04,
		author = {Ming{-}Feng Tsai and Ming{-}Hung Hsu and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Similarity Computation in Novelty Detection and Biomedical Text Categorization},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ntu.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TsaiHC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in TREC 2004 Novelty Track at CAS-ICT

_Huaping Zhang, Hongbo Xu, Shuo Bai, Bin Wang, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas.ict.wang](./novelty/participants.md#cas.ict.wang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/cas.ict.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/cas.ict.novelty.pdf)
- :material-file-search: **Runs:** [ICTVSMCOSAP](./novelty/runs.md#ictvsmcosap) | [ICTOKAPIOVLP](./novelty/runs.md#ictokapiovlp) | [ICTVSMFDBKH](./novelty/runs.md#ictvsmfdbkh) | [ICTVSMFDBKL](./novelty/runs.md#ictvsmfdbkl) | [ICTVSMLCE](./novelty/runs.md#ictvsmlce) | [ICT2VSMOLP](./novelty/runs.md#ict2vsmolp) | [ICT2VSMIG95](./novelty/runs.md#ict2vsmig95) | [ICT2VSMLCE](./novelty/runs.md#ict2vsmlce) | [ICT2OKAPIAP](./novelty/runs.md#ict2okapiap) | [ICT2OKALCEAP](./novelty/runs.md#ict2okalceap) | [ICT3VSMOLP](./novelty/runs.md#ict3vsmolp) | [ICT3OKAPIIG](./novelty/runs.md#ict3okapiig) | [ICT3OKAPIOLP](./novelty/runs.md#ict3okapiolp) | [ICT3OKAPFDBK](./novelty/runs.md#ict3okapfdbk) | [ICT4OVERLAP](./novelty/runs.md#ict4overlap) | [ICT4IG](./novelty/runs.md#ict4ig) | [ICT4OKAPIIG](./novelty/runs.md#ict4okapiig) | [ICT4OKAAP](./novelty/runs.md#ict4okaap) | [ICT4OVLPCHI](./novelty/runs.md#ict4ovlpchi)

??? abstract "Abstract"
	
	The main task in Novelty Track is to retrieve relevant sentences and remove duplicates from a document set given a TREC topic. This track took place for the first time in TREC 2002 and it is refined to four tasks in TREC 2003. Besides 25 relevant documents, irrelevant ones are given in this year of Novelty track. In other words, a given document is either relevant or irrelevant to the topic. There are 1808 documents in 50 TREC topics. Average 11.18 documents are noise for each topic. In topic N75, the number of noise is 45. Once we mistook an irrelevant document as relevance, all results in the document are wrong. Except the document retrieval, more limited information could be applied in the last three tasks than ever. Among the first 5 given documents, average 3.14 documents are relevant and average 2.76 are new. Especially, 9 topics have no relevant sentence in the first 5 ones. In TREC2004, ICT divided Novelty track into four sequential stages. It includes: customized language parsing on original dataset, document retrieval, sentence relevance and novelty detection. The architecture in novelty is given in Figure 1. In the first preprocessing stage, we applied sentence segmenter, tokenization, part-of-speech tagging, morphological analysis, stop word remover and query analyzer on topics and documents. As for query analysis, we categorized words in topics into description words and query words. Title, description and narrative parts are all merged into query with different weights. In the stage of document and sentence retrieval, we introduced vector space model (VSM) and its variance, probability model OKAPI and statistical language model. Based on VSM, we tried various query expansion strategies: pseu-feedback, term expansion with synset or synonym in WordNet[1] and expansion with highly local co-occurrence terms. With regard to the novelty stage, we defined three types of new degree: word overlapping and its extension, similarity comparison and information gain. In the last three tasks, we used the known results to adjust threshold, estimate the number of results, and turned to classifier, such as inductive and transductive SVM.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangXBWC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangXBWC04,
		author = {Huaping Zhang and Hongbo Xu and Shuo Bai and Bin Wang and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in {TREC} 2004 Novelty Track at {CAS-ICT}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/cas.ict.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangXBWC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### From the Texts to the Contexts They Contain: A Chain of Linguistic  Treatments

_Ahmed Amrani, Jérôme Azé, Thomas Heitz, Yves Kodratoff, Mathieu Roche_

- :fontawesome-solid-user-group: **Participant:** [u.paris.lri](./novelty/participants.md#u.paris.lri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uparis.novelty2.pdf](http://trec.nist.gov/pubs/trec13/papers/uparis.novelty2.pdf)
- :material-file-search: **Runs:** [LRIaze1](./novelty/runs.md#lriaze1) | [LRIaze2](./novelty/runs.md#lriaze2) | [LRIaze3](./novelty/runs.md#lriaze3) | [LRIaze4](./novelty/runs.md#lriaze4) | [LRIaze5](./novelty/runs.md#lriaze5) | [LRIaze22](./novelty/runs.md#lriaze22) | [LRIaze32](./novelty/runs.md#lriaze32) | [LRIaze42](./novelty/runs.md#lriaze42) | [LRIaze52](./novelty/runs.md#lriaze52) | [LRIaze12](./novelty/runs.md#lriaze12)

??? abstract "Abstract"
	
	The text-mining system we are building deals with the specific problem of identifying the instances of relevant concepts present in the texts. Our system relies therefore on interactions between a field expert and the various linguistic modules we use, often adapted from existing ones, such as Brill's tagger or CMU's Link parser. We have developed learning procedures adapted to various steps of the linguistic treatment, mainly for grammatical tagging, terminology, and concept learning. Our interaction with the expert differs from classical supervised learning, in that the expert is not simply a resource who is only able to provide examples, and unable to provide the formalized knowledge underlying these examples. We are developing specific programming languages which enable the field expert to intervene directly in some of the linguistic tasks. Our approach is thus devoted to help one expert in one field to detect the concepts relevant for his/her field, using a large amount of texts. Our approach is made of two steps. The first one is an automatic approach that finds relevant and novel sentences in the texts. The second one is based on the expert's knowledge and finds more specific relevant sentences. Working on 50 different domains without an expert has been a challenge in itself, and explains our relatively poor results for the first Novelty task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmraniAHKR04.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmraniAHKR04,
		author = {Ahmed Amrani and J{\'{e}}r{\^{o}}me Az{\'{e}} and Thomas Heitz and Yves Kodratoff and Mathieu Roche},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {From the Texts to the Contexts They Contain: {A} Chain of Linguistic Treatments},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uparis.novelty2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmraniAHKR04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Question Answering 

#### Overview of the TREC 2004 Question Answering Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/QA.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec13/papers/QA.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC 2004 Question Answering track contained a single task in which question series were used to define a set of targets. Each series contained factoid and list questions and related to a single target. The final question in the series was an “Other” question that asked for additional information about the target that was not covered by previous questions in the series. Each question type was evaluated separately with the final score a weighted average of the different component scores. Applying the combined measure on a per-series basis produces a QA task evaluation that more closely mimics classic document retrieval evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees04a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees04a,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2004 Question Answering Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/QA.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees04a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering with QED and Wee at TREC 2004

_Kisuh Ahn, Johan Bos, Stephen Clark, Tiphaine Dalmas, Jochen L. Leidner, Matthew Smillie, Bonnie L. Webber, James R. Curran_

- :fontawesome-solid-user-group: **Participant:** [u.edinburgh.sydney](./qa/participants.md#u.edinburgh.sydney)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uedinburgh-syd.bos.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/uedinburgh-syd.bos.qa.pdf)
- :material-file-search: **Runs:** [Edin2004A](./qa/runs.md#edin2004a) | [Edin2004B](./qa/runs.md#edin2004b) | [Edin2004C](./qa/runs.md#edin2004c)

??? abstract "Abstract"
	
	This report describes the experiments of the University of Edinburgh and the University of Sydney at the TREC-2004 question answering evaluation exercise. Our system combines two approaches: one with deep linguistic analysis using IR on the AQUAINT corpus applied to answer extraction from text passages, and one with a shallow linguistic analysis and shallow inference applied to a large set of snippets retrieved from the web. The results of our experiments support the following claims: (1) Web-based IR is a good alternative to “traditional” IR; and (2) deep linguistic analysis improves quality of exact answers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AhnBCDLSWC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/AhnBCDLSWC04,
		author = {Kisuh Ahn and Johan Bos and Stephen Clark and Tiphaine Dalmas and Jochen L. Leidner and Matthew Smillie and Bonnie L. Webber and James R. Curran},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering with {QED} and Wee at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uedinburgh-syd.bos.qa.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AhnBCDLSWC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Wikipedia at the TREC QA Track

_David Ahn, Valentin Jijkoun, Gilad Mishne, Karin Müller, Maarten de Rijke, Stefan Schlobach_

- :fontawesome-solid-user-group: **Participant:** [u.amsterdam.lit](./qa/participants.md#u.amsterdam.lit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uamsterdam.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/uamsterdam.qa.pdf)
- :material-file-search: **Runs:** [uams04tc1](./qa/runs.md#uams04tc1) | [uams04tc2](./qa/runs.md#uams04tc2) | [uams04raw](./qa/runs.md#uams04raw)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2004 Question Answering track. We provide a detailed account of the ideas underlying our approach to the QA task, especially to the so-called “other” questions. This year we made essential use of Wikipedia, the free online encyclopedia, both as a source of answers to factoid questions and as an importance model to help us identify material to be returned in response to “other” questions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AhnJMMRS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/AhnJMMRS04,
		author = {David Ahn and Valentin Jijkoun and Gilad Mishne and Karin M{\"{u}}ller and Maarten de Rijke and Stefan Schlobach},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Wikipedia at the {TREC} {QA} Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uamsterdam.qa.pdf},
		timestamp = {Tue, 14 Jul 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AhnJMMRS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lethbridge's Participation in TREC 2004 QA Track

_Yllias Chali, Stephen Dubien_

- :fontawesome-solid-user-group: **Participant:** [u.lethbridge](./qa/participants.md#u.lethbridge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ulethbridge.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/ulethbridge.qa.pdf)
- :material-file-search: **Runs:** [UofL1](./qa/runs.md#uofl1)

??? abstract "Abstract"
	
	Text Retrieval Conference (TREC), organised by National Institute for Standards and Technology (NIST), is a set of tracks that represent different areas of text retrieval. These tracks provide a way to measure systems progress in certain fields in text retrieval such as cross-language retrieval, retrieval filtering and genomics. We participated in the question answering track. The questions in the TREC-2004 QA track are clustered by target, which is the topic of the question. The QA track for 2004 has three types of questions: factoid questions that require only one correct response, list questions that require a non redundant list of correct responses and other questions that require a non redundant list of facts about the target that has not already been discovered by a previous answer. These questions will be answered using the AQUAINT collection, a collection of over a million newswire documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChaliD04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChaliD04,
		author = {Yllias Chali and Stephen Dubien},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Lethbridge's Participation in {TREC} 2004 {QA} Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ulethbridge.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChaliD04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNT at TREC 2004: Question Answering Combining Multiple Evidences

_Jiangping Chen, He Ge, Yan Wu, Shikun Jiang_

- :fontawesome-solid-user-group: **Participant:** [u.northtexas](./qa/participants.md#u.northtexas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/unorthtexas.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/unorthtexas.qa.pdf)
- :material-file-search: **Runs:** [UNTQA04M1](./qa/runs.md#untqa04m1) | [UNTQA04M2](./qa/runs.md#untqa04m2) | [UNTQA04M3](./qa/runs.md#untqa04m3)

??? abstract "Abstract"
	
	Question Answering (QA) aims at identifying answers to users' natural language questions. A QA system can release the users from digesting large amount of text in order to locate particular facts or numbers. The research has drawn great attention from several disciplines such as information retrieval, information extraction, natural language processing, and artificial intelligence. TREC QA track has provided comparable QA system evaluation on a set of test questions since 1999. The degree of difficulty of the test questions has increased substantially in recent two years, which push the research toward applying more sophisticated strategies and better understanding of English texts. Question answering is very challenging due to the ambiguity of the questions, complexity of linguistic phenomena involved in the documents, and the difficulty to understand natural languages. More challenging is to locate short snippets or answers from a document collection with texts written in different languages, which is within our research interests focusing on cross-lingual or multilingual information access and retrieval. We have decided to participate in TREC 2004 Question Answering Track as our first step toward exploring advanced multilingual information retrieval. Our goal of this year is to develop a prototype automatic question answering system that can be continually expanded and improved. Our prototype QA system, named EagleQA, made use of available NLP (Natural Language Processing) tools and knowledge resources for question understanding and answer finding. This paper describes the overall structure of the system, NLP tools and lexical resources employed, our QA methodology for TREC 2004, QA test results & analysis, and our plan for future research.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenGWJ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenGWJ04,
		author = {Jiangping Chen and He Ge and Yan Wu and Shikun Jiang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UNT} at {TREC} 2004: Question Answering Combining Multiple Evidences},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/unorthtexas.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenGWJ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM's PIQUANT II in TREC 2004

_Jennifer Chu-Carroll, Krzysztof Czuba, John M. Prager, Abraham Ittycheriah, Sasha Blair-Goldensohn_

- :fontawesome-solid-user-group: **Participant:** [ibm.prager](./qa/participants.md#ibm.prager)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ibm-prager.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/ibm-prager.qa.pdf)
- :material-file-search: **Runs:** [IBM1](./qa/runs.md#ibm1) | [IBM2](./qa/runs.md#ibm2)

??? abstract "Abstract"
	
	PIQUANT II, the system we used for TREC 2004, is a completely reengineered system whose core functionalities for answering factoid and list questions remain largely unchanged from previous years [Chu-Carroll et al, 2003, Prager et al, 2004]. We continue to address these questions using our multi-strategy and multi-source approach. For “other” questions, we experimented with two alternative approaches, one that uses statistical collocation information for extracting prominent passages related to the target, and the other which is a slight variation of the QA-by-Dossier approach we employed last year [Prager et al, 2004] that asks a set of sub-questions of interest about the target and returns a set of relevant passages that answer these sub-questions. In addition, to address this year's new question format, we developed a question pre-processing component to interpret individual questions against the given target to generate a self-contained natural language question as expected by subsequent components of our QA system. NIST assessed scores showed substantial improvement of our new PIQUANT II system over earlier versions of our QA system both in terms of absolute scores as well as relative improvement compared to the best and median scores in each of the three component subtasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Chu-CarrollCPIB04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Chu-CarrollCPIB04,
		author = {Jennifer Chu{-}Carroll and Krzysztof Czuba and John M. Prager and Abraham Ittycheriah and Sasha Blair{-}Goldensohn},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IBM's {PIQUANT} {II} in {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ibm-prager.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Chu-CarrollCPIB04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Bangor at TREC 2004: Question Answering Track

_Terence Clifton, William John Teahan_

- :fontawesome-solid-user-group: **Participant:** [u.wales.bangor](./qa/participants.md#u.wales.bangor)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uwales-bangor.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/uwales-bangor.qa.pdf)
- :material-file-search: **Runs:** [uwbqitekat04](./qa/runs.md#uwbqitekat04)

??? abstract "Abstract"
	
	This paper describes the participation of the School of Informatics, University of Wales, Bangor in the 2004 Text Retrieval Conference. We present additions and modifications to the QITEKAT system, initially developed as an entry for the 2003 QA evaluation, including automated regular expression induction, improved question matching, and application of our knowledge framework to the modified question types presented in the 2004 track. Results are presented which show improvements on last year's performance, and we discuss future directions for the system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CliftonT04.bib) "
	```
	@inproceedings{DBLP:conf/trec/CliftonT04,
		author = {Terence Clifton and William John Teahan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Bangor at {TREC} 2004: Question Answering Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uwales-bangor.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CliftonT04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### National University of Singapore at the TREC 13 Question Answering  Main Task

_Hang Cui, Keya Li, Renxu Sun, Tat-Seng Chua, Min-Yen Kan_

- :fontawesome-solid-user-group: **Participant:** [nus.yang](./qa/participants.md#nus.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/nus.chua.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/nus.chua.qa.pdf)
- :material-file-search: **Runs:** [NUSCHUA1](./qa/runs.md#nuschua1) | [NUSCHUA2](./qa/runs.md#nuschua2) | [NUSCHUA3](./qa/runs.md#nuschua3)

??? abstract "Abstract"
	
	Our participation at TREC in the past two years (Yang et al., 2002, 2003) has focused on incorporating external knowledge to boost document and passage retrieval performance in event-based open domain question answering (QA). Despite our previous successes, we have identified three weaknesses of our system with respect to this year's task guidelines. First, our system works at the surface level to extract answers, by picking the first occurrence of a string that matches the question target type from the highest ranked passage. As such, our answer extraction relies heavily on the results of passage retrieval and named entity tagging. However, a passage that contains the correct answer may contain other strings of the same target type (Light et al., 2001), which means an incorrect string may be extracted. A technique to select the answer string that has the correct relationships with respect to the other words in the question is needed. Second, our definitional QA system utilizes manually constructed definition patterns. While these patterns are precise in selecting definition sentences, they are strict in matching (i.e., slot-by-slot matching using regular expressions), failing to match correct sentences with minor variations. Third, this year's guidelines state that factoid and list questions are not independent; instead, they are all related to given topics. Under such a contextual QA scenario, we need to revise our framework to exploit the existing topic-relevant knowledge in answering the questions. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CuiLSCK04.bib) "
	```
	@inproceedings{DBLP:conf/trec/CuiLSCK04,
		author = {Hang Cui and Keya Li and Renxu Sun and Tat{-}Seng Chua and Min{-}Yen Kan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {National University of Singapore at the {TREC} 13 Question Answering Main Task},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/nus.chua.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CuiLSCK04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Novelty, Question Answering and Genomics: The University of Iowa Response

_David Eichmann, Yi Zhang, Shannon Bradshaw, Xin Ying Qiu, Li Zhou, Padmini Srinivasan, Aditya Kumar Sehgal, Hudon Wong_

- :fontawesome-solid-user-group: **Participant:** [u.iowa](./qa/participants.md#u.iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf)
- :material-file-search: **Runs:** [UIowaQA0401](./qa/runs.md#uiowaqa0401) | [UIowaQA0402](./qa/runs.md#uiowaqa0402)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannZBQZSSW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannZBQZSSW04,
		author = {David Eichmann and Yi Zhang and Shannon Bradshaw and Xin Ying Qiu and Li Zhou and Padmini Srinivasan and Aditya Kumar Sehgal and Hudon Wong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Novelty, Question Answering and Genomics: The University of Iowa Response},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannZBQZSSW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TALP-QA System at TREC 2004: Structural and Hierarchical Relaxation  Over Semantic Constraints

_Daniel Ferrés, Samir Kanaan, Edgar González, Alicia Ageno, Horacio Rodríguez, Mihai Surdeanu, Jordi Turmo_

- :fontawesome-solid-user-group: **Participant:** [upc.ferres](./qa/participants.md#upc.ferres)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/upc.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/upc.qa.pdf)
- :material-file-search: **Runs:** [talp2004upc](./qa/runs.md#talp2004upc) | [talp2004upc2](./qa/runs.md#talp2004upc2)

??? abstract "Abstract"
	
	This paper describes TALP-QA, a multilingual open-domain Question Answering (QA) system under development at UPC for the past two years. The system is described and evaluated in the context of our participation in the TREC 2004 Main QA task. The TALP-QA system treats both factoid and definitional questions (other). Factoid questions are resolved with a process consisting of three phases: question processing, passage retrieval and answer extraction. Our approach to solve this kind of questions is to build a semantic representation of the questions and the sentences in the retrieved passages. A set of semantic constraints are extracted for each question. The answer extraction algorithm extracts and ranks sentences that satisfy the semantic constraints of the question. It matches are not possible the algorithm relaxes the semantic constraints structurally (removing constraints) and/or hierarchically (abstracting the constraints using a taxonomy). Definitional questions are treated in a three-stage process: passage retrieval, pattern scanning over the previous set of passages, and finally a filtering phase where only the most relevant and informative fragments are given as final output.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerresKGARST04.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerresKGARST04,
		author = {Daniel Ferr{\'{e}}s and Samir Kanaan and Edgar Gonz{\'{a}}lez and Alicia Ageno and Horacio Rodr{\'{\i}}guez and Mihai Surdeanu and Jordi Turmo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TALP-QA} System at {TREC} 2004: Structural and Hierarchical Relaxation Over Semantic Constraints},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/upc.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FerresKGARST04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Sheffield's TREC 2004 QA Experiments

_Robert J. Gaizauskas, Mark A. Greenwood, Mark Hepple, Ian Roberts, Horacio Saggion_

- :fontawesome-solid-user-group: **Participant:** [u.sheffield.gaizauskas](./qa/participants.md#u.sheffield.gaizauskas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/usheffield.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/usheffield.qa.pdf)
- :material-file-search: **Runs:** [shef04afv](./qa/runs.md#shef04afv) | [ShefMadCow20](./qa/runs.md#shefmadcow20) | [ShefMadCow50](./qa/runs.md#shefmadcow50)

??? abstract "Abstract"
	
	The experiments detailed in this paper are a continuation of the experiments started as part of the work undertaken in preparation for participation in the TREC 2003 QA evaluations as documented in Gaizauskas et al. [2003]. Our main experiments for TREC 2004 were concerned with investigating: a) alternative approaches to information retrieval (IR) for question answering b) alternative approaches to answer extraction for list and factoid questions, and c) alternative approaches answering definitional or ‘other' questions. In each of these three areas we have developed two principal alternatives, each of which has variants. Given the TREC limit of three test runs per site, we have not been able to evaluate properly all combinations of these approaches. Consequently, the systems we submitted only give a partial picture of work carried out, and further evaluation is underway. In the following we describe the major alternatives we have been exploring in these three areas and present the formal test results for the system combinations we submitted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaizauskasGHRS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaizauskasGHRS04,
		author = {Robert J. Gaizauskas and Mark A. Greenwood and Mark Hepple and Ian Roberts and Horacio Saggion},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Sheffield's {TREC} 2004 {QA} Experiments},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/usheffield.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaizauskasGHRS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LexiClone Inc. and NIST TREC

_Ilya S. Geller_

- :fontawesome-solid-user-group: **Participant:** [lexiclone.geller](./qa/participants.md#lexiclone.geller)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/lexiclone.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/lexiclone.qa.pdf)
- :material-file-search: **Runs:** [lexiclone04](./qa/runs.md#lexiclone04)

??? abstract "Abstract"
	
	The UniSearch-4.6 program created by the company LexiClone Inc. for seeking out textual information is intended to search for Reality as well as Truth. While running NIST TREC QA 2003 and 2004, virtually all answers obtained by LexiClone were Realities.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Geller04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Geller04,
		author = {Ilya S. Geller},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {LexiClone Inc. and {NIST} {TREC}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/lexiclone.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Geller04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Korea University Question Answering System at TREC 2004

_Kyoung-Soo Han, Hoo-Jung Chung, Sang-Bum Kim, Young-In Song, Joo-Young Lee, Hae-Chang Rim_

- :fontawesome-solid-user-group: **Participant:** [korea.u](./qa/participants.md#korea.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/korea.u.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/korea.u.qa.pdf)
- :material-file-search: **Runs:** [KUQA1](./qa/runs.md#kuqa1) | [KUQA2](./qa/runs.md#kuqa2) | [KUQA3](./qa/runs.md#kuqa3)

??? abstract "Abstract"
	
	Our QA system consists of two different components. One is for the factoid and list questions, and the other is for the other questions. The components are processed individually, and each result is combined into our submitted run. For the factoid questions, we have tried to find answers by proximity-based named entity search. Given a question, fine-grained named entities for candidate answers are selected, and all the extracted passages containing the named entities and question keywords are scored by a proximity-based measure. List questions are processed in a similar way to the factoid questions, but we empirically give a threshold value to obtain only top n candidate answers. For other questions, relevant phrases consisting of noun phrases and verb phrases are extracted using a dependency relationship to the question target from the initially retrieved sentences. After redundant phrases are eliminated from the answer candidates, final answers are selected using several selection criteria including the term statistics from an encyclopedia. Section 2 summarizes our system for factoid and list questions, and Section 3 for other questions. In Section 4, the TREC evaluation results are analyzed, and Section 5 concludes our work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HanCKSLR04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HanCKSLR04,
		author = {Kyoung{-}Soo Han and Hoo{-}Jung Chung and Sang{-}Bum Kim and Young{-}In Song and Joo{-}Young Lee and Hae{-}Chang Rim},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Korea University Question Answering System at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/korea.u.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HanCKSLR04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering by Searching Large Corpora With Linguistic Methods

_Michael Kaißer, Tilman Becker_

- :fontawesome-solid-user-group: **Participant:** [saarland.u](./qa/participants.md#saarland.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/saarlandu.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/saarlandu.qa.pdf)
- :material-file-search: **Runs:** [mk2004qar2](./qa/runs.md#mk2004qar2) | [mk2004qar3](./qa/runs.md#mk2004qar3) | [mk2004qar1](./qa/runs.md#mk2004qar1)

??? abstract "Abstract"
	
	In this paper we describe the QuALiM Question Answering system which uses linguistic analysis of questions as well as candidate sentences in its answer finding process. To this end we have developed a rephrasing algorithm based on linguistic patterns that describe the structure of questions and candidate sentences and where precisely to find the answer in the candidate sentences. With this method and a fall-back strategy, both using the web as their primary data source, we participated in TREC 2004. We present our official results and a follow-up evaluation to elucidate the contribution of the methods used.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KaisserB04.bib) "
	```
	@inproceedings{DBLP:conf/trec/KaisserB04,
		author = {Michael Kai{\ss}er and Tilman Becker},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering by Searching Large Corpora With Linguistic Methods},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/saarlandu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KaisserB04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Answering Multiple Questions on a Topic From Heterogeneous Resources

_Boris Katz, Matthew W. Bilotti, Sue Felshin, Aaron Fernandes, Wesley Hildebrandt, Roni Katzir, Jimmy Lin, Daniel Loreto, Gregory Marton, Federico Mora, Özlem Uzuner_

- :fontawesome-solid-user-group: **Participant:** [mit.lin](./qa/participants.md#mit.lin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/mit.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/mit.qa.pdf)
- :material-file-search: **Runs:** [mit1](./qa/runs.md#mit1) | [mit2](./qa/runs.md#mit2)

??? abstract "Abstract"
	
	MIT CSAIL's entry into this year's TREC Question Answering track focused on the conversational aspect of this year's task, on improving the coverage of our list and definition systems, and on an infrastructure to generalize our TREC-specific tools for other question answering tasks. While our overall architecture remained largely unchanged from last year, we have built on our strengths for each component: our web-based factoid engine was adapted for input from a new web search engine; our list engine's knowledge base expanded from 150 to over 3000 lists; our definitional nugget extractor now has expanded and improved patterns with improved component precision and recall. Beyond their internal improvements, these components were adapted to a larger conversational framework that passed information about the topic1 to factoids and lists. Answer selection for definitional2 questions newly took into account the prior questions and answers for duplicate removal. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KatzBFFHKLLMMU04.bib) "
	```
	@inproceedings{DBLP:conf/trec/KatzBFFHKLLMMU04,
		author = {Boris Katz and Matthew W. Bilotti and Sue Felshin and Aaron Fernandes and Wesley Hildebrandt and Roni Katzir and Jimmy Lin and Daniel Loreto and Gregory Marton and Federico Mora and {\"{O}}zlem Uzuner},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Answering Multiple Questions on a Topic From Heterogeneous Resources},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/mit.qa.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KatzBFFHKLLMMU04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DalTREC 2004: Question Answering Using Regular Expression Rewriting

_Vlado Keselj, Anthony Cox_

- :fontawesome-solid-user-group: **Participant:** [dalhousie.u](./qa/participants.md#dalhousie.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/dalhousieu.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/dalhousieu.qa.pdf)
- :material-file-search: **Runs:** [Dal04b](./qa/runs.md#dal04b) | [Dal04p](./qa/runs.md#dal04p) | [Dal04x](./qa/runs.md#dal04x)

??? abstract "Abstract"
	
	This is the first year that the Dalhousie University participated in TREC. We submitted three runs for the QA track. Our evaluation results are generally below the median (with one exception) but seem to be significantly higher than the worst scores, which is within our expectations considering a limited time spent on developing the system. Our approach was based on the regular expression rewriting and the use of external search engines (MultiText and PRISE). One run used Web-reinforced search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KeseljC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/KeseljC04,
		author = {Vlado Keselj and Anthony Cox},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {DalTREC 2004: Question Answering Using Regular Expression Rewriting},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/dalhousieu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KeseljC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evolving XML and Dictionary Strategies for Question Answering and  Novelty Tasks

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./qa/participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/clresearch.qa.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/clresearch.qa.novelty.pdf)
- :material-file-search: **Runs:** [clr04r1](./qa/runs.md#clr04r1)

??? abstract "Abstract"
	
	CL Research participated in the question answering and novelty tracks in TREC 2004. The Knowledge Management System (KMS), which provides a single interface for question answering, text summarization, information extraction, and document exploration, was used for these tasks. Question answering is performed directly within KMS, which answers questions either from a repository or the Internet. The novelty task was performed with the XML Analyzer, which includes many of the functions used in the KMS summarization routines. These tasks are based on creating and exploiting an XML representation of the texts used for these two tracks. For the QA track, we submitted one run and our overall score was 0.156, with scores of 0.161 for factoid questions, 0.064 for list questions, and 0.239 for “other” questions; these scores are significantly improved from TREC 2003. For the novelty track, we submitted two runs for task 1, one run for task 2, four runs for task 3, and one run for task 4. For most tasks, our scores were above the median. We describe our system in some detail, particularly emphasizing strategies that are emerging in the use of XML and lexical resources for the question answering and novelty tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Litkowski04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Litkowski04,
		author = {Kenneth C. Litkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Evolving {XML} and Dictionary Strategies for Question Answering and Novelty Tasks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/clresearch.qa.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Litkowski04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AnswerFinder at TREC 2004

_Diego Mollá, Mary Gardiner_

- :fontawesome-solid-user-group: **Participant:** [macquarie.u](./qa/participants.md#macquarie.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/macquarieu.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/macquarieu.qa.pdf)
- :material-file-search: **Runs:** [answfind1](./qa/runs.md#answfind1) | [answfind2](./qa/runs.md#answfind2) | [answfind3](./qa/runs.md#answfind3)

??? abstract "Abstract"
	
	AnswerFinder combines lexical, syntactic, and semantic information in various stages of the question answering process. The candidate sentences are preselected on the basis of (i) the presence of named entity types compatible with the expected answer type, and (ii) a score combination of the overlap of words, grammatical relations, and flat logical forms. The candidate answers, in turn, are extracted from (i) the set of compatible named entities and (ii) the output of a logical-form pattern matching algorithm.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MollaG04.bib) "
	```
	@inproceedings{DBLP:conf/trec/MollaG04,
		author = {Diego Moll{\'{a}} and Mary Gardiner},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {AnswerFinder at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/macquarieu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MollaG04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with Web QA System and TREC 2004 Questions

_Dmitri Roussinov, Yin Ding, Jose Antonio Robles-Flores_

- :fontawesome-solid-user-group: **Participant:** [arizona.state.u](./qa/participants.md#arizona.state.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/arizonau.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/arizonau.qa.pdf)
- :material-file-search: **Runs:** [ASUQA2004](./qa/runs.md#asuqa2004)

??? abstract "Abstract"
	
	We describe our first participation in TREC. We only competed in the Question Answering (QA) category and limited our runs to factoids. Our approach was to use our open domain QA system that finds the answer among Web pages indexed by a commercial search engine, then project the answer to the TREC test collection. Our Web QA takes advantage of the redundancy of the Web, obtains the candidate answers by pattern matching, then performs probabilistic triangulation of them to assign a final score. Our novel contributions are the following 1) the probabilistic triangulation algorithm, 2) a more powerful pattern language than used in prior research, and 3) use of semantic features of expected answers instead of relying on an elaborate hierarchy of question types. Although, we were able to run only first 91 out of 230 factoid questions before the submission deadline, we find our result encouraging, and if interpolated to the entire questions set, it would have placed us above the median performance on factoid questions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoussinovDR04.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoussinovDR04,
		author = {Dmitri Roussinov and Yin Ding and Jose Antonio Robles{-}Flores},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with Web {QA} System and {TREC} 2004 Questions},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/arizonau.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoussinovDR04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering with QACTIS at TREC 2004

_Patrick Schone, T. Bassi, A. Kulman, Gary M. Ciany, Paul McNamee, James Mayfield_

- :fontawesome-solid-user-group: **Participant:** [nsa.schone](./qa/participants.md#nsa.schone)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/nsa-schone.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/nsa-schone.qa.pdf)
- :material-file-search: **Runs:** [NSAQACTIS1](./qa/runs.md#nsaqactis1) | [nsaqactis2](./qa/runs.md#nsaqactis2) | [nsaqactis3](./qa/runs.md#nsaqactis3)

??? abstract "Abstract"
	
	We provide a description of the QACTIS question-answering system and its application to and performance in the 2004 TREC question-answering evaluation. Since this was also QACTIS's first year competing at TREC, we provide a complete overview of its purpose, development, structure, and its future directions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchoneBKCMM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchoneBKCMM04,
		author = {Patrick Schone and T. Bassi and A. Kulman and Gary M. Ciany and Paul McNamee and James Mayfield},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering with {QACTIS} at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/nsa-schone.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchoneBKCMM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering Using the DLT System at TREC 2004

_Richard F. E. Sutcliffe, Igal Gabbay, Kieran White, Aoife O'Gorman, Michael Mulcahy_

- :fontawesome-solid-user-group: **Participant:** [u.limerick](./qa/participants.md#u.limerick)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/u.limerick.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/u.limerick.qa.pdf)
- :material-file-search: **Runs:** [DLT04QA01](./qa/runs.md#dlt04qa01) | [DLT04QA02](./qa/runs.md#dlt04qa02) | [DLT04QA03](./qa/runs.md#dlt04qa03)

??? abstract "Abstract"
	
	This article outlines our participation in the Question Answering Track of the Text REtrieval Conference organised by the National Institute of Standards and Technology. We first provide an outline of the system. We then describe the changes made relative to last year. After this we summarise our results before drawing conclusions and identifying some next steps.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SutcliffeGWOM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SutcliffeGWOM04,
		author = {Richard F. E. Sutcliffe and Igal Gabbay and Kieran White and Aoife O'Gorman and Michael Mulcahy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering Using the {DLT} System at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/u.limerick.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SutcliffeGWOM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2004: QA

_Wei Tan, Qunxiu Chen, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghua.ma](./qa/participants.md#tsinghua.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.qa.pdf)
- :material-file-search: **Runs:** [THUQA04RUN1](./qa/runs.md#thuqa04run1)

??? abstract "Abstract"
	
	In this paper, we describe ideas and related experiments of Tsinghua University IR group in TREC 2004 QA track. In this track, our system consists three components: Question analysis, Information retrieval, and Answer extraction. Question analysis component extracts Query Term and answer type. Information retrieval component retrieves candidate documents from index set based on paragraph level and re-ranks them to find more relevant documents. And then Answer extraction component matches empirical phrases according to answer type to extract final answer
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanCM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanCM04,
		author = {Wei Tan and Qunxiu Chen and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2004: {QA}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TanCM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Linguistic Processing and Web Mining for Question Answering:  ITC-irst at TREC 2004

_Hristo Tanev, Milen Kouylekov, Bernardo Magnini_

- :fontawesome-solid-user-group: **Participant:** [itc.irst.tanev](./qa/participants.md#itc.irst.tanev)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/itc-irst-tanev.web.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/itc-irst-tanev.web.qa.pdf)
- :material-file-search: **Runs:** [irst04web](./qa/runs.md#irst04web) | [irst04parse](./qa/runs.md#irst04parse) | [irst04higher](./qa/runs.md#irst04higher)

??? abstract "Abstract"
	
	This paper describes the work we have been done in the last year on the DIOGENE Question Answering system developed at ITC-Irst. We present two preliminary experiments showing the possibility of integrating into DIOGENE a textual entailment engine based on entailment rules. We addressed the problem proposing both a methodology for acquiring rules from the Web and a matching algorithm for comparing dependency trees derived from the question and from documents. Although the overall results are not high, we consider this year participation at TREC as an intermediate step in view of a more complete and in depth integration of textual entailment rules into the system. We also report about the problems we encountered in maintaining the Web-based answer validation module.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanevKM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanevKM04,
		author = {Hristo Tanev and Milen Kouylekov and Bernardo Magnini},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Linguistic Processing and Web Mining for Question Answering: ITC-irst at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/itc-irst-tanev.web.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TanevKM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDUQA on TREC 2004 QA Track

_Lide Wu, Xuanjing Huang, Lan You, Zhushuo Zhang, Xin Li, Yaqian Zhou_

- :fontawesome-solid-user-group: **Participant:** [fudan.wu](./qa/participants.md#fudan.wu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/fudan.wu.qa.pdf](http://trec.nist.gov/pubs/trec13/papers/fudan.wu.qa.pdf)
- :material-file-search: **Runs:** [FDUQA13b](./qa/runs.md#fduqa13b) | [FDUQA13a](./qa/runs.md#fduqa13a) | [FDUQA13c](./qa/runs.md#fduqa13c)

??? abstract "Abstract"
	
	In this year's QA Track, we process factoid questions in a way that is slightly different from our previous system [1]. The most significant difference is that we developed a new answer type category, and trained a classifier for answer type classification. To answer list questions, we use a pattern-based method to find more answers other than those found in the processing of factoid question. And an algorithm that uses some knowledge bases answers definition questions. This algorithm achieves a promising result. In our system, external knowledge is widely used, which includes WordNet and Internet. The ontology in WordNet is used in the answer type classification, and its synsets are used to do query extension. Internet is used not only to find factoid question answers, but also as knowledge base for definition questions. In the following, Section 2, 3, 4 will separately introduce our algorithm to solve factoid, list and definition questions. Section 5 will present our results in TREC2004.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHYZLZ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHYZLZ04,
		author = {Lide Wu and Xuanjing Huang and Lan You and Zhushuo Zhang and Xin Li and Yaqian Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDUQA} on {TREC} 2004 {QA} Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/fudan.wu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHYZLZ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Robust 

#### Overview of the TREC 2004 Robust Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ROBUST.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec13/papers/ROBUST.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The robust retrieval track explores methods for improving the consistency of retrieval technology by focusing on poorly performing topics. The retrieval task in the track is a traditional ad hoc retrieval task where the evaluation methodology emphasizes a system's least effective topics. The most promising approach to improving poorly performing topics is exploiting text collections other than the target collection such as the web. The 2004 edition of the track used 250 topics and required systems to rank the topics by predicted difficulty. The 250 topics within the test set allowed the stability of evaluation measures that emphasize poorly performing topics to be investigated. A new measure, a variant of the traditional MAP measure that uses a geometric mean rather than an arithmetic mean to average individual topic results, shows promise of giving appropriate emphasis to poorly performing topics while being more stable at equal topic set sizes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees04b.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees04b,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2004 Robust Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ROBUST.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees04b.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fondazione Ugo Bordoni at TREC 2004

_Gianni Amati, Claudio Carpineto, Giovanni Romano_

- :fontawesome-solid-user-group: **Participant:** [fub.amati](./robust/participants.md#fub.amati)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/fub.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/fub.robust.pdf)
- :material-file-search: **Runs:** [fub04TDNge](./robust/runs.md#fub04tdnge) | [fub04Tge](./robust/runs.md#fub04tge) | [fub04Dge](./robust/runs.md#fub04dge) | [fub04Te](./robust/runs.md#fub04te) | [fub04De](./robust/runs.md#fub04de) | [fub04TDNe](./robust/runs.md#fub04tdne) | [fub04TDNg](./robust/runs.md#fub04tdng) | [fub04Tg](./robust/runs.md#fub04tg) | [fub04Dg](./robust/runs.md#fub04dg) | [fub04T2ge](./robust/runs.md#fub04t2ge)

??? abstract "Abstract"
	
	Our participation in TREC 2004 aims to extend and improve the use of the DFR (Divergence From Randomness) models with Query Expansion (QE) for the robust track. We experiment with a new parameter-free version of Rocchio's Query Expansion, and use the information theory based function, InfoDFR to predict the AP (Average Precision) of queries. We also study how the use of an external collection affects the retrieval-performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiCR04.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiCR04,
		author = {Gianni Amati and Claudio Carpineto and Giovanni Romano},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Fondazione Ugo Bordoni at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/fub.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiCR04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Can We Get A Better Retrieval Function From Machine?

_Weiguo Fan, Wensi Xi, Edward A. Fox, Li Wang_

- :fontawesome-solid-user-group: **Participant:** [virginia.tech](./robust/participants.md#virginia.tech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/va-tech.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/va-tech.robust.pdf)
- :material-file-search: **Runs:** [vtumlong254](./robust/runs.md#vtumlong254) | [vtumlong348](./robust/runs.md#vtumlong348) | [vtumlong436](./robust/runs.md#vtumlong436) | [vtumlong252](./robust/runs.md#vtumlong252) | [vtumlong344](./robust/runs.md#vtumlong344) | [vtumlong432](./robust/runs.md#vtumlong432) | [vtumdesc](./robust/runs.md#vtumdesc) | [vtumtitle](./robust/runs.md#vtumtitle)

??? abstract "Abstract"
	
	The quality of an information retrieval system heavily depends on its retrieval function, which returns a similarity measurement between the query and each document in the collection. Documents are sorted according to their similarity values with the query and those with high rank are assumed to be relevant. Okapi BM25 and their variations are very popular retrieval functions and they seem to be the default retrieval function for the IR research community; and there are many other widely used and well studied functions, for example, Pivoted TFIDF and INQUERY. Most of these retrieval functions being used today are made based on probabilistic theories and they are adjusted in real world according to different contexts and information needs. In this paper, we propose the idea that a good retrieval function can be discovered by a pure machine learning approach, without using probabilistic theories and knowledge-based techniques. Two machine learning algorithms, Support Vector Machine (SVM) and Genetic Programming (GP) are used for retrieval function discovery, and GP is found to be a more effective approach. The retrieval functions discovered by GP might be hard for human interpretation, but their performance is superior to Okapi BM25, one of the most popular functions. The new retrieval function is combined with query expansion techniques and the retrieval performance is improved significantly. Based on our observations in the empirical study, the GP function is more reliable and effective than Okapi BM25 when query expansion techniques are used.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FanXFW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/FanXFW04,
		author = {Weiguo Fan and Wensi Xi and Edward A. Fox and Li Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Can We Get {A} Better Retrieval Function From Machine?},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/va-tech.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FanXFW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2004 Robust Track Experiments Using PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, H. L. Sun, Peter Deng_

- :fontawesome-solid-user-group: **Participant:** [queens.college.kwok](./robust/participants.md#queens.college.kwok)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/queens-college.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/queens-college.robust.pdf)
- :material-file-search: **Runs:** [pircRB04t1](./robust/runs.md#pircrb04t1) | [pircRB04d3](./robust/runs.md#pircrb04d3) | [pircRB04t2](./robust/runs.md#pircrb04t2) | [pircRB04td2](./robust/runs.md#pircrb04td2) | [pircRB04t3](./robust/runs.md#pircrb04t3) | [pircRB04td3](./robust/runs.md#pircrb04td3) | [pircRB04d2](./robust/runs.md#pircrb04d2) | [pircRB04d4](./robust/runs.md#pircrb04d4) | [pircRB04d5](./robust/runs.md#pircrb04d5) | [pircRB04t4](./robust/runs.md#pircrb04t4)

??? abstract "Abstract"
	
	There were two sub-tasks in the TREC2004 Robust track: given a set of topics, a) improve the effectiveness of the lowest performing 25%, and b) predict their ranking according to their average precision. For task a), we followed the strategy introduced by us last year to improve ad-hoc retrieval by employing the web as an external thesaurus to supplement a given topic description. A new method of probing the web based on a given topic statement called ‘window rotation' was tested. For task b) we employed ε-SVR (epsilon support vector regression) to predict performance of test topics based on training with some simple features such as document frequencies, query term frequencies. This allows performance prediction without retrieval. Features were also added from a retrieval list with the hope that they may predict later stage or web-assisted retrieval better. 200 old topics were used for training to predict the ranking of 49 new topics, as well as the whole set of 249. Runs were done that made use of title only, description only section of a topic, and title-description-combination retrieval lists. Ten submissions including runs that were based on initial retrieval only, retrievals with pseudo-relevance feedback, and with web-assistance. Evaluation shows that we have achieved very good performance for most of our runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGSD04.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGSD04,
		author = {Kui{-}Lam Kwok and Laszlo Grunfeld and H. L. Sun and Peter Deng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2004 Robust Track Experiments Using {PIRCS}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/queens-college.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGSD04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 2004: Robust Track

_Shuang Liu, Chaojing Sun, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [u.illinois.chicago](./robust/participants.md#u.illinois.chicago)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uil-chicago.liu.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/uil-chicago.liu.robust.pdf)
- :material-file-search: **Runs:** [uic0401](./robust/runs.md#uic0401)

??? abstract "Abstract"
	
	In TREC 2004, the Database and Information System Lab (DBIS) at University of Illinois at Chicago (UIC) participates in the robust track, which is a traditional ad hoc retrieval task. The emphasis is based on average effectiveness as well as individual topic effectiveness. In our system, noun phrases in the query are identified and classified into 4 types: proper names, dictionary phrases, simple phrases and complex phrases. A document has a phrase if all content words in a phrase are within a window of a certain size. The window sizes for different types of phrases are different. We consider phrases to be more important than individual terms. As a consequence, documents in response to a query are ranked with matching phrases given a higher priority. WordNet is used to disambiguate word senses. Whenever the sense of a query term is determined, its synonyms, hyponyms, words from its definition and its compound concepts are considered for possible additions to the query. The newly added terms are used to form phrases during retrieval. Pseudo feedback and web-assisted feedback are used to help retrieval. We submit one title run this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuSY04.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuSY04,
		author = {Shuang Liu and Chaojing Sun and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 2004: Robust Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uil-chicago.liu.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuSY04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2004: Robust and Terabyte Tracks

_Christine D. Piatko, James Mayfield, Paul McNamee, R. Scott Cost_

- :fontawesome-solid-user-group: **Participant:** [jhu.apl.mcnamee](./robust/participants.md#jhu.apl.mcnamee)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/jhu-apl.robust.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/jhu-apl.robust.tera.pdf)
- :material-file-search: **Runs:** [apl04rsTDNw5](./robust/runs.md#apl04rstdnw5) | [apl04rsTs](./robust/runs.md#apl04rsts) | [apl04rsTw](./robust/runs.md#apl04rstw) | [apl04rsDw](./robust/runs.md#apl04rsdw) | [apl04rsTDNfw](./robust/runs.md#apl04rstdnfw)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) focused on the Robust and Terabyte Tracks at the 2004 TREC conference.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PiatkoMMC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/PiatkoMMC04,
		author = {Christine D. Piatko and James Mayfield and Paul McNamee and R. Scott Cost},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{JHU/APL} at {TREC} 2004: Robust and Terabyte Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/jhu-apl.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PiatkoMMC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2004: Experiments in Web, Robust,  and Terabyte Tracks with Terrier

_Vassilis Plachouras, Ben He, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [u.glasgow](./robust/participants.md#u.glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf)
- :material-file-search: **Runs:** [uogRobSBase](./robust/runs.md#uogrobsbase) | [uogRobSWR5](./robust/runs.md#uogrobswr5) | [uogRobSWR10](./robust/runs.md#uogrobswr10) | [uogRobDBase](./robust/runs.md#uogrobdbase) | [uogRobDWR5](./robust/runs.md#uogrobdwr5) | [uogRobDWR10](./robust/runs.md#uogrobdwr10) | [uogRobLBase](./robust/runs.md#uogroblbase) | [uogRobLT](./robust/runs.md#uogroblt) | [uogRobLWR5](./robust/runs.md#uogroblwr5) | [uogRobLWR10](./robust/runs.md#uogroblwr10)

??? abstract "Abstract"
	
	With our participation in TREC2004, we test Terrier, a modular and scalable Information Retrieval framework, in three tracks. For the mixed query task of the Web track, we employ a decision mechanism for selecting appropriate retrieval approaches on a per-query basis. For the robust track, in order to cope with the poorly-performing queries, we use two pre-retrieval performance predictors and a weighting function recommender mechanism. We also test a new training approach for the automatic tuning of the term frequency normalisation parameters. In the Terabyte track, we employ a distributed version of Terrier and test the effectiveness of techniques, such as using the anchor text, query expansion and selecting an optimal weighting model for each query. Overall, in all three tracks we participated, Terrier and the tested Divergence From Randomness models were shown to be stable and effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PlachourasHO04.bib) "
	```
	@inproceedings{DBLP:conf/trec/PlachourasHO04,
		author = {Vassilis Plachouras and Ben He and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2004: Experiments in Web, Robust, and Terabyte Tracks with Terrier},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PlachourasHO04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Part-of-Speech Sense Matrix Model Experiments in the TREC 2004 Robust  Track at ICL, PKU

_Bing Swen, Xue-qiang Lü, Hongying Zan, Qi Su, Zhi-guo Lai, Kun Xiang, Jing-he Hu_

- :fontawesome-solid-user-group: **Participant:** [peking.u](./robust/participants.md#peking.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/pekingu.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/pekingu.robust.pdf)
- :material-file-search: **Runs:** [icl04pos2f](./robust/runs.md#icl04pos2f) | [icl04pos2td](./robust/runs.md#icl04pos2td) | [icl04pos2d](./robust/runs.md#icl04pos2d) | [icl04pos2t](./robust/runs.md#icl04pos2t) | [icl04pos7f](./robust/runs.md#icl04pos7f) | [icl04pos48f](./robust/runs.md#icl04pos48f) | [icl04pos7td](./robust/runs.md#icl04pos7td) | [icl04pos7tap](./robust/runs.md#icl04pos7tap) | [icl04pos7tat](./robust/runs.md#icl04pos7tat)

??? abstract "Abstract"
	
	The Robust Retrieval track is a traditional ad hoc retrieval task with the focus on individual topic effectiveness. This track provides us an opportunity to do experiments on our recently proposed IR model using a word-by-sense matrix document representation, which was called Sense Matrix Model (SMM) [Swen 2003, 2004]. For the first time to extensively test the model, some simpler and easy-to-implement forms of SMM is used for this year's Robust track, where the part-of-speeches of words are treated as the (rough) senses of words. Though the model supports several matrix similarity measures and some advanced data analysis techniques, our initial implementation can only handle sense sets at the scale of a few hundreds of senses. Thus a relatively small part-of-speech tag set is employed and only two different matrix similarity measures used. In this paper, we describe our model configuration and methods used in the TREC 2004 Robust track. Implementation issues and the submitted runs are also discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SwenLZSLXH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SwenLZSLXH04,
		author = {Bing Swen and Xue{-}qiang L{\"{u}} and Hongying Zan and Qi Su and Zhi{-}guo Lai and Kun Xiang and Jing{-}he Hu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Part-of-Speech Sense Matrix Model Experiments in the {TREC} 2004 Robust Track at ICL, {PKU}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/pekingu.robust.pdf},
		timestamp = {Fri, 23 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SwenLZSLXH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Robust, Web and Terabyte Retrieval with Hummingbird SearchServer at  TREC 2004

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./robust/participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf)
- :material-file-search: **Runs:** [humR04t1](./robust/runs.md#humr04t1) | [humR04d5](./robust/runs.md#humr04d5) | [humR04t5e1](./robust/runs.md#humr04t5e1) | [humR04d4e5](./robust/runs.md#humr04d4e5) | [humR04t1m](./robust/runs.md#humr04t1m) | [humR04d5m](./robust/runs.md#humr04d5m) | [humR04t1i](./robust/runs.md#humr04t1i) | [humR04t5](./robust/runs.md#humr04t5) | [humR04d5i](./robust/runs.md#humr04d5i) | [humR04d4](./robust/runs.md#humr04d4)

??? abstract "Abstract"
	
	Hummingbird participated in 3 tracks of TREC 2004: the ad hoc task of the Robust Retrieval Track (find at least one relevant document in the first 10 rows from 1.9GB of news and government data), the mixed navigational and distillation task of the Web Track (find the home or named page or key resource pages in 1.2 million pages (18GB) from the .GOV domain), and the ad hoc task of the Terabyte Track (find all the relevant documents with high precision from 25.2 million pages (426GB) from the .GOV domain). In the robustness task, SearchServer found a relevant document in the first 10 rows for 46 of the 49 new short (Title-only) topics. In the web task, SearchServer returned a desired page in the first 10 rows for more than 75% of the 225 queries. In the terabyte task, SearchServer found a relevant document in the first 10 rows for 45 of the 49 short topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson04,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Robust, Web and Terabyte Retrieval with Hummingbird SearchServer at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Hong Kong Polytechnic University at the TREC 2004 Robust Track

_D. Y. Wang, Robert Wing Pong Luk, Kam-Fai Wong_

- :fontawesome-solid-user-group: **Participant:** [hkpu.luk](./robust/participants.md#hkpu.luk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/hkp.u.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/hkp.u.robust.pdf)
- :material-file-search: **Runs:** [polyudp2](./robust/runs.md#polyudp2) | [polyutp3](./robust/runs.md#polyutp3) | [polyudp4](./robust/runs.md#polyudp4) | [polyudp5](./robust/runs.md#polyudp5) | [polyudp6](./robust/runs.md#polyudp6) | [polyutp1](./robust/runs.md#polyutp1)

??? abstract "Abstract"
	
	In the robust track, we mainly tested our passage-based retrieval model with different passage sizes and weighting schemes. In our approach, we used two retrieval models, namely the 2-Poisson model using BM25 term weights and the vector space model (VSM) using adaptive pivoted unique document length normalization. Also, we utilize WordNet to re-weight some PRF terms and extract some context words as expanded query terms. We show that our passage-based model achieves the comparable performance on the whole query set. Moreover, our new methods of using WordNet information for query expansion can improve the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangLW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangLW04,
		author = {D. Y. Wang and Robert Wing Pong Luk and Kam{-}Fai Wong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Hong Kong Polytechnic University at the {TREC} 2004 Robust Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/hkp.u.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangLW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLPR at TREC 2004: Robust Experiments

_Jin Xu, Jun Zhao, Bo Xu_

- :fontawesome-solid-user-group: **Participant:** [cas.nlpr](./robust/participants.md#cas.nlpr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/cas-nlpr.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/cas-nlpr.robust.pdf)
- :material-file-search: **Runs:** [NLPR04clus9](./robust/runs.md#nlpr04clus9) | [NLPR04oktwo](./robust/runs.md#nlpr04oktwo) | [NLPR04OKapi](./robust/runs.md#nlpr04okapi) | [NLPR04okall](./robust/runs.md#nlpr04okall) | [NLPR04okdiv](./robust/runs.md#nlpr04okdiv) | [NLPR04SemLM](./robust/runs.md#nlpr04semlm) | [NLPR04LMts](./robust/runs.md#nlpr04lmts) | [NLPR04LcA](./robust/runs.md#nlpr04lca) | [NLPR04NcA](./robust/runs.md#nlpr04nca) | [NLPR04COMB](./robust/runs.md#nlpr04comb) | [NLPR04clus10](./robust/runs.md#nlpr04clus10)

??? abstract "Abstract"
	
	It is the second time that the Chinese Information Processing group of NLPR participates in TREC. In the past, we have investigated the use of two key technologies: Window-based weighting method and Semantic Tree Model for query expansion, with success, to tasks in novelty and robust tracks. We focused on the Robust Retrieval Track at this year's conference. Based on the previous IR architecture, our research on this year's robust mainly focused on three aspects: (1) two-step retrieval scheme; (2) word sense entropy; (3) several strategies for merging multiple runs. Our paper is organized as follows. Section 2 shows the basic architecture of our IR system and the new techniques for improving its performance. Section 2.1 presents the two-step retrieval scheme which mainly attempts to reduce the influence of noise introduced by query expansion. Section 2.2 introduces a new method for query word weighting—word sense entropy which is a measure for the variety of the sense of query word based on WordNet's structured knowledge. Section 2.3 describes several different strategies which we have used for merging the results of multiple runs produced by different retrieval approaches. Section 3 gives the experimental verification of the techniques mentioned in section 2. Section 4 concludes our work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuZX04.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuZX04,
		author = {Jin Xu and Jun Zhao and Bo Xu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NLPR} at {TREC} 2004: Robust Experiments},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/cas-nlpr.robust.pdf},
		timestamp = {Tue, 19 Jul 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/XuZX04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2004 Genomics, Hard, Robust and Web Tracks

_Kiduk Yang, Ning Yu, Adam Wead, Gavin La Rowe, Yu-Hsiu Li, Christopher Friend, Yoon Lee_

- :fontawesome-solid-user-group: **Participant:** [indiana.u.yang](./robust/participants.md#indiana.u.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf](http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf)
- :material-file-search: **Runs:** [wdoqdn1](./robust/runs.md#wdoqdn1) | [wdoqla1](./robust/runs.md#wdoqla1) | [wdoqsn1](./robust/runs.md#wdoqsn1) | [wdo25qla1](./robust/runs.md#wdo25qla1)

??? abstract "Abstract"
	
	To facilitate understanding of information as well as its discovery, we need to combine the capabilities of the human and the machine as well as multiple methods and sources of evidence. Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science houses several projects that aim to apply this idea of multi-level fusion in the areas of information retrieval and knowledge organization. The TREC research group of WIDIT, who engages in examination of information retrieval strategies that can accommodate a variety of data environments and search tasks, participated in the Genomics, HARD, Robust, and Web tracks in TREC-2004. The basic approach of WIDIT was to leverage multiple sources of evidence, combine multiple methods, and integrate the strengths of man and the machine. Our main strategies for the tracks were: the use of gene name thesaurus in the Genomics track; query expansion and relevance feedback in the HARD track; query expansion with keywords from Web search in the Robust track, and the interactive system tuning process called “Dynamic Tuning” in the Web track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYWRLFL04.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYWRLFL04,
		author = {Kiduk Yang and Ning Yu and Adam Wead and Gavin La Rowe and Yu{-}Hsiu Li and Christopher Friend and Yoon Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2004 Genomics, Hard, Robust and Web Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf},
		timestamp = {Tue, 24 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangYWRLFL04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Juru at TREC 2004: Experiments with Prediction of Query Difficulty

_Elad Yom-Tov, Shai Fine, David Carmel, Adam Darlow, Einat Amitay_

- :fontawesome-solid-user-group: **Participant:** [ibm.haifa.carmel](./robust/participants.md#ibm.haifa.carmel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ibm-haifa.robust.pdf](http://trec.nist.gov/pubs/trec13/papers/ibm-haifa.robust.pdf)
- :material-file-search: **Runs:** [JuruDesAggr](./robust/runs.md#jurudesaggr) | [JuruDesSwQE](./robust/runs.md#jurudesswqe) | [JuruDesQE](./robust/runs.md#jurudesqe) | [JuruTit](./robust/runs.md#jurutit) | [JuruDes](./robust/runs.md#jurudes) | [JuruTitSwQE](./robust/runs.md#jurutitswqe) | [JuruTitDes](./robust/runs.md#jurutitdes) | [JuruDesTrSl](./robust/runs.md#jurudestrsl) | [JuruDesLaMd](./robust/runs.md#jurudeslamd) | [JuruTitSwDs](./robust/runs.md#jurutitswds)

??? abstract "Abstract"
	
	Our experiments in the Robust track this year focused on predicting query difficulty and using this prediction for improving information retrieval. We developed two prediction algorithms and used the subsequent prediction in several ways in order to improve the performance of the search engine. These included modifying the search engine parameters, using selective query expansion, and switching between different topic parts. We also experimented with a new scoring model based on ideas from the field of machine learning. Our results show that query prediction is indeed efficient in improving retrieval, although further work is needed in order to improve the performance of the prediction algorithms and their uses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yom-TovFCDA04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yom-TovFCDA04,
		author = {Elad Yom{-}Tov and Shai Fine and David Carmel and Adam Darlow and Einat Amitay},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Juru at {TREC} 2004: Experiments with Prediction of Query Difficulty},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ibm-haifa.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yom-TovFCDA04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Terabyte 

#### Overview of the TREC 2004 Terabyte Track

_Charles L. A. Clarke, Nick Craswell, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/TERA.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec13/papers/TERA.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Terabyte Track explores how adhoc retrieval and evaluation techniques can scale to terabyte-sized collections. For TREC 2004, our first year, 50 new adhoc topics were created and evaluated over a a 426GB collection of 25 million documents taken from the .gov Web domain. A total of 70 runs were submitted by 17 groups. Along with the top documents, each group reported average query times, indexing times, index sizes, and hardware and software characteristics for their systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCS04,
		author = {Charles L. A. Clarke and Nick Craswell and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2004 Terabyte Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/TERA.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melbourne University 2004: Terabyte and Web Tracks

_Vo Ngoc Anh, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [u.melbourne](./terabyte/participants.md#u.melbourne)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/umelbourne.tera.web.pdf](http://trec.nist.gov/pubs/trec13/papers/umelbourne.tera.web.pdf)
- :material-file-search: **Runs:** [MU04tb1](./terabyte/runs.md#mu04tb1) | [MU04tb2](./terabyte/runs.md#mu04tb2) | [MU04tb3](./terabyte/runs.md#mu04tb3) | [MU04tb4](./terabyte/runs.md#mu04tb4) | [MU04tb5](./terabyte/runs.md#mu04tb5)

??? abstract "Abstract"
	
	The University of Melbourne carried out experiments in the Terabyte and Web tracks of TREC 2004. We applied a further variant of our impact-based retrieval approach by integrating evidence from text content, anchor text, URL depth, and link structure into the process of ranking documents, working toward a retrieval system that handles equally well all of the four query types employed in these two tracks. That is, we sought to avoid special techniques, and did not apply any explicit or implicit query classifiers. The system was designed to be scalable and efficient.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnhM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnhM04,
		author = {Vo Ngoc Anh and Alistair Moffat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Melbourne University 2004: Terabyte and Web Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/umelbourne.tera.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnhM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2004

_Bodo Billerbeck, Adam Cannane, Abhijit Chattaraj, Nicholas Lester, William Webber, Hugh E. Williams, John Yiannis, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [rmit.scholer](./terabyte/participants.md#rmit.scholer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/rmit.tera.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/rmit.tera.geo.pdf)
- :material-file-search: **Runs:** [zetbodoffff](./terabyte/runs.md#zetbodoffff) | [zetanch](./terabyte/runs.md#zetanch) | [zetplain](./terabyte/runs.md#zetplain) | [zetfuzzy](./terabyte/runs.md#zetfuzzy) | [zetfunkyz](./terabyte/runs.md#zetfunkyz)

??? abstract "Abstract"
	
	RMIT University participated in two tracks at TREC 2004: Terabyte and Genomics, both for the first time. This paper describes the techniques we applied and our experiments in both tracks, and discusses the results of the genomics track runs; the terabyte track results are unavailable at the time of manuscript submission. We also describe our new zettair search engine, in use for the first time at TREC
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BillerbeckCCLWWYZ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/BillerbeckCCLWWYZ04,
		author = {Bodo Billerbeck and Adam Cannane and Abhijit Chattaraj and Nicholas Lester and William Webber and Hugh E. Williams and John Yiannis and Justin Zobel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/rmit.tera.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BillerbeckCCLWWYZ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Terabyte Searching, Genomic Retrieval and Novelty Detection  for TREC 2004

_Stephen Blott, Fabrice Camous, Paul Ferguson, Georgina Gaughan, Cathal Gurrin, Gareth J. F. Jones, Noel Murphy, Noel E. O'Connor, Alan F. Smeaton, Peter Wilkins, Oisín Boydell, Barry Smyth_

- :fontawesome-solid-user-group: **Participant:** [dubblincity.u](./terabyte/participants.md#dubblincity.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf)
- :material-file-search: **Runs:** [DcuTB04Ucd1](./terabyte/runs.md#dcutb04ucd1) | [DcuTB04Base](./terabyte/runs.md#dcutb04base) | [DcuTB04Ucd2](./terabyte/runs.md#dcutb04ucd2) | [DcuTB04Wbm25](./terabyte/runs.md#dcutb04wbm25) | [DcuTB04Combo](./terabyte/runs.md#dcutb04combo)

??? abstract "Abstract"
	
	In TREC2004, Dublin City University took part in three tracks, Terabyte (in collaboration with University College Dublin), Genomic and Novelty. In this paper we will discuss each track separately and present separate conclusions from this work. In addition, we present a general description of a text retrieval engine that we have developed in the last year to support our experiments into large scale, distributed information retrieval, which underlies all of the track experiments described in this document.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BlottCFGGJMOSWBS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/BlottCFGGJMOSWBS04,
		author = {Stephen Blott and Fabrice Camous and Paul Ferguson and Georgina Gaughan and Cathal Gurrin and Gareth J. F. Jones and Noel Murphy and Noel E. O'Connor and Alan F. Smeaton and Peter Wilkins and Ois{\'{\i}}n Boydell and Barry Smyth},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Terabyte Searching, Genomic Retrieval and Novelty Detection for {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BlottCFGGJMOSWBS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Initial Results with Structured Queries and Language Models on Half  a Terabyte of Text

_Kevyn Collins-Thompson, Paul Ogilvie, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu.dir.callan](./terabyte/participants.md#cmu.dir.callan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/cmu-dir.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/cmu-dir.tera.pdf)
- :material-file-search: **Runs:** [cmutufs2500](./terabyte/runs.md#cmutufs2500) | [cmuapfs2500](./terabyte/runs.md#cmuapfs2500) | [cmutuns2500](./terabyte/runs.md#cmutuns2500)

??? abstract "Abstract"
	
	The CMU Distributed IR group's experiments for the TREC 2004 Terabyte track are some of the first to use Indri, a new indexing and retrieval component developed by the University of Massachusetts for the Lemur Toolkit [2]. Indri combines an inference network with a language-modeling approach and is designed to scale to terabyte-sized collections. Our goals for this year's Terabyte track were modest: to complete a set of simple baseline runs successfully using the new Indri software, and to gain more experience with Indri's retrieval model, the track's GOV2 corpus, and terabyte-scale collections in general.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Collins-ThompsonOC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Collins-ThompsonOC04,
		author = {Kevyn Collins{-}Thompson and Paul Ogilvie and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Initial Results with Structured Queries and Language Models on Half a Terabyte of Text},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/cmu-dir.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Collins-ThompsonOC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC 2004 Standard Retrieval Models Over Partitioned Indices  for the Terabyte Track

_Jefferson Heard, Ophir Frieder, David A. Grossman_

- :fontawesome-solid-user-group: **Participant:** [iit](./terabyte/participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/iit.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/iit.tera.pdf)
- :material-file-search: **Runs:** [iit00t](./terabyte/runs.md#iit00t) | [robertson](./terabyte/runs.md#robertson)

??? abstract "Abstract"
	
	For TREC-2004, we participated in the Terabyte track. We focused on partitioning the data in the GOV2 collection across a homogeneous cluster of machines and indexing and querying the collection in a distributed fashion using different standard retrieval models on a single system, such as the Robertson BM25 probabilistic measure and a vector space measure. Our partitioned indices were each independent of each other, with independent collection statistics and lexicons. We combined the results as if all indices were the same, however, not weighing any one result set more or less than another
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeardFG04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeardFG04,
		author = {Jefferson Heard and Ophir Frieder and David A. Grossman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} at {TREC} 2004 Standard Retrieval Models Over Partitioned Indices for the Terabyte Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/iit.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeardFG04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Normal PC to Index and Retrieval Terabyte Document - THUIR  at TREC 2004 Terabyte Track

_Yijiang Jin, Wei Qi, Min Zhang, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghua.ma](./terabyte/participants.md#tsinghua.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.tera.pdf)
- :material-file-search: **Runs:** [THUIRtb2](./terabyte/runs.md#thuirtb2) | [THUIRtb3](./terabyte/runs.md#thuirtb3) | [THUIRtb4](./terabyte/runs.md#thuirtb4) | [THUIRtb5](./terabyte/runs.md#thuirtb5) | [THUIRtb6](./terabyte/runs.md#thuirtb6)

??? abstract "Abstract"
	
	This year, Tsinghua University Information Retrieval Group (THUIR) participated in the terabyte track of TREC for the first time. Since the document collection is as large as about 426G and we do not have super computers, our first and most import target is to complete the task in a reasonable low cost, both on the hardware system and time-consuming. This target was archived in such approaches: carefully data preprocess, data set reduction, optimization of algorithm and program. As the effect of the approaches, the task was completed in a normal high performance desktop PC with an indexing time not more than several ten hours and an acceptable retrieval time. Furthermore, the retrieval performance is not terrible. All experiments have been performed on TMiner IR system, developed by THUIR group last year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JinQZM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/JinQZM04,
		author = {Yijiang Jin and Wei Qi and Min Zhang and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Normal {PC} to Index and Retrieval Terabyte Document - {THUIR} at {TREC} 2004 Terabyte Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JinQZM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Indri at TREC 2004: Terabyte Track

_Donald Metzler, Trevor Strohman, Howard R. Turtle, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [u.mass](./terabyte/participants.md#u.mass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/umass.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/umass.tera.pdf)
- :material-file-search: **Runs:** [indri04AWRM](./terabyte/runs.md#indri04awrm) | [indri04AW](./terabyte/runs.md#indri04aw) | [indri04QLRM](./terabyte/runs.md#indri04qlrm) | [indri04QL](./terabyte/runs.md#indri04ql) | [indri04FAW](./terabyte/runs.md#indri04faw)

??? abstract "Abstract"
	
	This paper provides an overview of experiments carried out at the TREC 2004 Terabyte Track using the Indri search engine. Indri is an efficient, effective distributed search engine. Like INQUERY, it is based on the inference network framework and supports structured queries, but unlike INQUERY, it uses language modeling probabilities within the network which allows for added flexibility. We describe our approaches to the Terabyte Track, all of which involved automatically constructing structured queries from the title portions of the TREC topics. Our methods use term proximity information and HTML document structure. In addition, a number of optimization procedures for efficient query processing are explained.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MetzlerSTC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/MetzlerSTC04,
		author = {Donald Metzler and Trevor Strohman and Howard R. Turtle and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Indri at {TREC} 2004: Terabyte Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/umass.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MetzlerSTC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Amberfish at the TREC 2004 Terabyte Track

_Nassib Nassar_

- :fontawesome-solid-user-group: **Participant:** [etymon](./terabyte/participants.md#etymon)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/etymon.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/etymon.tera.pdf)
- :material-file-search: **Runs:** [nn04test](./terabyte/runs.md#nn04test) | [nn04tint](./terabyte/runs.md#nn04tint) | [nn04eint](./terabyte/runs.md#nn04eint)

??? abstract "Abstract"
	
	The TREC 2004 Terabyte Track evaluated information retrieval in large-scale text collections, using a set of 25 million documents (426 GB). This paper gives an overview of our experiences with this collection and describes Amberfish, the text retrieval software used for the experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Nassar04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Nassar04,
		author = {Nassib Nassar},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Amberfish at the {TREC} 2004 Terabyte Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/etymon.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Nassar04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Towards Grid-Based Information Retrieval

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [u.alaska](./terabyte/participants.md#u.alaska)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ualaska.web.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/ualaska.web.tera.pdf)
- :material-file-search: **Runs:** [irttbtl](./terabyte/runs.md#irttbtl)

??? abstract "Abstract"
	
	The IRTools software toolkit was used in TREC 2004 for submissions to the Web track and the Terabyte track. Terabyte track results were not available at the time of the due date for this Proceedings paper. While Web track results were available, qrels were not. Because we discovered a bug in the MySQL++ API that truncated docid numbers in our results, we will await qrels to reevaluate submitted runs and report results. This year, the Terabyte track dictated some changes to IRTools in order to handle the 430+GB of text (about 25M documents). The main change was to operate on chunks of the collection (272 separate chunks, each containing one of the Terabyte collections' subdirectories). Chunks were generated in parallel using the National Center for Supercomputing Application's cluster, Mercury (dual Itanium systems). Up to about 40 systems were used simultaneously for both indexing and querying. Query merging was simplistic, based on the cosine value with Lnu.Ltc weighting. Use of the NCSA cluster, and other experiments with commodity clusters, is part of work underway to enable information retrieval in Grid computing environments. The site http://www.gir-wg.org has information about Grid Information Retrieval (GIR), including links to the published Requirements document and draft Architecture document. The GIR working group is chartered by the Global Grid Forum (GGF) to develop standards and reference implementations for GIR. TREC participants are urged to consider getting involved with Grid computing. Computational grids offer a very good fit for the needs of large-scale information retrieval research and practice. This brief abstract for the proceedings will be replaced with a complete analysis of this year's submissions for the full conference paper. Meanwhile, Newby (2004) provides a profile of IRTools, which is generally applicable to this year's submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Newby04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Newby04,
		author = {Gregory B. Newby},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Towards Grid-Based Information Retrieval},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ualaska.web.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Newby04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2004: Robust and Terabyte Tracks

_Christine D. Piatko, James Mayfield, Paul McNamee, R. Scott Cost_

- :fontawesome-solid-user-group: **Participant:** [jhu.apl.mcnamee](./terabyte/participants.md#jhu.apl.mcnamee)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/jhu-apl.robust.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/jhu-apl.robust.tera.pdf)
- :material-file-search: **Runs:** [apl04w4tdn](./terabyte/runs.md#apl04w4tdn) | [apl04w4t](./terabyte/runs.md#apl04w4t)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) focused on the Robust and Terabyte Tracks at the 2004 TREC conference.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PiatkoMMC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/PiatkoMMC04,
		author = {Christine D. Piatko and James Mayfield and Paul McNamee and R. Scott Cost},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{JHU/APL} at {TREC} 2004: Robust and Terabyte Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/jhu-apl.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PiatkoMMC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2004: Experiments in Web, Robust,  and Terabyte Tracks with Terrier

_Vassilis Plachouras, Ben He, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [u.glasgow](./terabyte/participants.md#u.glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf)
- :material-file-search: **Runs:** [uogTBBaseS](./terabyte/runs.md#uogtbbases) | [uogTBBaseL](./terabyte/runs.md#uogtbbasel) | [uogTBQEL](./terabyte/runs.md#uogtbqel) | [uogTBAnchS](./terabyte/runs.md#uogtbanchs) | [uogTBPoolQEL](./terabyte/runs.md#uogtbpoolqel)

??? abstract "Abstract"
	
	With our participation in TREC2004, we test Terrier, a modular and scalable Information Retrieval framework, in three tracks. For the mixed query task of the Web track, we employ a decision mechanism for selecting appropriate retrieval approaches on a per-query basis. For the robust track, in order to cope with the poorly-performing queries, we use two pre-retrieval performance predictors and a weighting function recommender mechanism. We also test a new training approach for the automatic tuning of the term frequency normalisation parameters. In the Terabyte track, we employ a distributed version of Terrier and test the effectiveness of techniques, such as using the anchor text, query expansion and selecting an optimal weighting model for each query. Overall, in all three tracks we participated, Terrier and the tested Divergence From Randomness models were shown to be stable and effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PlachourasHO04.bib) "
	```
	@inproceedings{DBLP:conf/trec/PlachourasHO04,
		author = {Vassilis Plachouras and Ben He and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2004: Experiments in Web, Robust, and Terabyte Tracks with Terrier},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PlachourasHO04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research Asia at Web Track and Terabyte Track of TREC  2004

_Ruihua Song, Ji-Rong Wen, Shuming Shi, Guomao Xin, Tie-Yan Liu, Tao Qin, Xin Zheng, Jiyu Zhang, Gui-Rong Xue, Wei-Ying Ma_

- :fontawesome-solid-user-group: **Participant:** [microsoft.asia](./terabyte/participants.md#microsoft.asia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/microsoft-asia.web.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/microsoft-asia.web.tera.pdf)
- :material-file-search: **Runs:** [MSRAt1](./terabyte/runs.md#msrat1) | [MSRAt2](./terabyte/runs.md#msrat2) | [MSRAt3](./terabyte/runs.md#msrat3) | [MSRAt4](./terabyte/runs.md#msrat4) | [MSRAt5](./terabyte/runs.md#msrat5)

??? abstract "Abstract"
	
	Terabye track aMir 2 search Asia (MRA)s experiments on the mixed query task of Web track and For Web track, we mainly test a set of new technologies. One of our efforts is to test some new features of Web pages to see if they are helpful to retrieval performance. Title extraction, sitemap based feature propagation, and URL scoring are of this kind. Another effort is to propose new function of algorithm to improve relevance or importance ranking. For example, we found that a new link analysis algorithm named HostRank that can outweigh PageRank [4] for topic distillation queries based on our experimental results. Eventually, linear combination of multiple scores with normalizations is tried to achieve stable performance improvement with mixed queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SongWSXLQZZXM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SongWSXLQZZXM04,
		author = {Ruihua Song and Ji{-}Rong Wen and Shuming Shi and Guomao Xin and Tie{-}Yan Liu and Tao Qin and Xin Zheng and Jiyu Zhang and Gui{-}Rong Xue and Wei{-}Ying Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research Asia at Web Track and Terabyte Track of {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/microsoft-asia.web.tera.pdf},
		timestamp = {Tue, 01 Dec 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SongWSXLQZZXM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Robust, Web and Terabyte Retrieval with Hummingbird SearchServer at  TREC 2004

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./terabyte/participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf)
- :material-file-search: **Runs:** [humT04](./terabyte/runs.md#humt04) | [humT04l](./terabyte/runs.md#humt04l) | [humT04vl](./terabyte/runs.md#humt04vl) | [humT04dvl](./terabyte/runs.md#humt04dvl) | [humT04l3](./terabyte/runs.md#humt04l3)

??? abstract "Abstract"
	
	Hummingbird participated in 3 tracks of TREC 2004: the ad hoc task of the Robust Retrieval Track (find at least one relevant document in the first 10 rows from 1.9GB of news and government data), the mixed navigational and distillation task of the Web Track (find the home or named page or key resource pages in 1.2 million pages (18GB) from the .GOV domain), and the ad hoc task of the Terabyte Track (find all the relevant documents with high precision from 25.2 million pages (426GB) from the .GOV domain). In the robustness task, SearchServer found a relevant document in the first 10 rows for 46 of the 49 new short (Title-only) topics. In the web task, SearchServer returned a desired page in the first 10 rows for more than 75% of the 225 queries. In the terabyte task, SearchServer found a relevant document in the first 10 rows for 45 of the 49 short topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson04,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Robust, Web and Terabyte Retrieval with Hummingbird SearchServer at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Clustering and Blade Clusters in the Terabyte Task

_Giuseppe Attardi, Andrea Esuli, Chirag Patel_

- :fontawesome-solid-user-group: **Participant:** [upisa.attardi](./terabyte/participants.md#upisa.attardi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/upisa-tera.pdf](http://trec.nist.gov/pubs/trec13/papers/upisa-tera.pdf)
- :material-file-search: **Runs:** [pisa1](./terabyte/runs.md#pisa1) | [pisa2](./terabyte/runs.md#pisa2) | [pisa3](./terabyte/runs.md#pisa3) | [pisa4](./terabyte/runs.md#pisa4)

??? abstract "Abstract"
	
	Web search engines exploit conjunctive queries and special ranking criteria which differ from the disjunctive queries typically used for ad-hoc retrieval. We wanted to asses the effectiveness of those techniques in the TeraByte task, in particular scoring criteria like: link popularity, proximity boosting, home page score, descriptions and anchor text. Since conjunctive queries sometimes produce low recall, we tested a new approach to query expansion, which extracts additional query terms from a clustering of the snippets from the first query. The technique proved effective, almost doubling the Mean Average Precision. However, the improvement was just enough to compensate for the drop that was introduced, contrary to our expectations, by the proximity boost.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AttardiEP04.bib) "
	```
	@inproceedings{DBLP:conf/trec/AttardiEP04,
		author = {Giuseppe Attardi and Andrea Esuli and Chirag Patel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Clustering and Blade Clusters in the Terabyte Task},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/upisa-tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AttardiEP04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Web 

#### Overview of the TREC 2004 Web Track

_Nick Craswell, David Hawking_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/WEB.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec13/papers/WEB.OVERVIEW.pdf)
??? abstract "Abstract"
	
	This year's main experiment involved processing a mixed query stream, with an even mix of each query type studied in TREC-2003: 75 homepage finding queries, 75 named page finding queries and 75 topic distillation queries. The goal was to find ranking approaches which work well over the 225 queries, without access to query type labels. We also ran two small experiments. First, participants were invited to submit classification runs, attempting to correctly label the 225 queries by type. Second, we invited participants to download the new W3C test collection, and think about appropriate experiments for the proposed TREC-2005 Enterprise Track. This is the last year for the Web Track in its current form, it will not run in TREC-2005.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellH04,
		author = {Nick Craswell and David Hawking},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2004 Web Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/WEB.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melbourne University 2004: Terabyte and Web Tracks

_Vo Ngoc Anh, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [u.melbourne](./web/participants.md#u.melbourne)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/umelbourne.tera.web.pdf](http://trec.nist.gov/pubs/trec13/papers/umelbourne.tera.web.pdf)
- :material-file-search: **Runs:** [MU04web1](./web/runs.md#mu04web1) | [MU04web2](./web/runs.md#mu04web2) | [MU04web3](./web/runs.md#mu04web3) | [MU04web5](./web/runs.md#mu04web5) | [MU04web4](./web/runs.md#mu04web4)

??? abstract "Abstract"
	
	The University of Melbourne carried out experiments in the Terabyte and Web tracks of TREC 2004. We applied a further variant of our impact-based retrieval approach by integrating evidence from text content, anchor text, URL depth, and link structure into the process of ranking documents, working toward a retrieval system that handles equally well all of the four query types employed in these two tracks. That is, we sought to avoid special techniques, and did not apply any explicit or implicit query classifiers. The system was designed to be scalable and efficient.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnhM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnhM04,
		author = {Vo Ngoc Anh and Alistair Moffat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Melbourne University 2004: Terabyte and Web Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/umelbourne.tera.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnhM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Novel Approaches in Text Information Retrieval - Experiments in the  Web Track of TREC 2004

_Mohamed Farah, Daniel Vanderpooten_

- :fontawesome-solid-user-group: **Participant:** [lamsade](./web/participants.md#lamsade)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/lamsade.web.pdf](http://trec.nist.gov/pubs/trec13/papers/lamsade.web.pdf)
- :material-file-search: **Runs:** [LamMcm1](./web/runs.md#lammcm1)

??? abstract "Abstract"
	
	In this paper, we report our experiments in the mixed query task of the Web track for TREC 2004. We deal with the problem of ranking Web documents within a multicriteria framework and propose a novel approach for information retrieval. We focus on the design of a set of criteria aiming at capturing complementary aspects of relevance. Moreover, we provide aggregation procedures that are based on decision rules, to get the ranking of relevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FarahV04.bib) "
	```
	@inproceedings{DBLP:conf/trec/FarahV04,
		author = {Mohamed Farah and Daniel Vanderpooten},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Novel Approaches in Text Information Retrieval - Experiments in the Web Track of {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/lamsade.web.pdf},
		timestamp = {Thu, 21 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FarahV04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Language Models for Searching in Web Corpora

_Jaap Kamps, Gilad Mishne, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [u.amsterdam.lit](./web/participants.md#u.amsterdam.lit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uamsterdam.web.pdf](http://trec.nist.gov/pubs/trec13/papers/uamsterdam.web.pdf)
- :material-file-search: **Runs:** [UAmsT04LnuNG](./web/runs.md#uamst04lnung) | [UAmsT04MSinu](./web/runs.md#uamst04msinu) | [UAmsT04MWinu](./web/runs.md#uamst04mwinu) | [UAmsT04MWScb](./web/runs.md#uamst04mwscb) | [UAmsT04MSind](./web/runs.md#uamst04msind)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2004 Web and Terabyte tracks. For the web track, we employ mixture language models based on document full-text, incoming anchor-text, and documents titles, with a range of web-centric priors. We provide a detailed analysis of the effect on relevance of document length, URL structure, and link topology. The resulting web-centric priors are applied to three types of topics—distillation, home page, and named page—and improve effectiveness for all topic types, as well as for the mixed query set. For the terabyte track, we experimented with building an index just based on the document titles, or on the incoming anchor texts. Very selective indexing leads to a compact index that is effective in terms of early precision, catering for the typical web searcher behavior
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KampsMR04.bib) "
	```
	@inproceedings{DBLP:conf/trec/KampsMR04,
		author = {Jaap Kamps and Gilad Mishne and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Language Models for Searching in Web Corpora},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uamsterdam.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KampsMR04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding "Abstract Fields" of Web Pages and Query Specific Retrieval  - THUIR at TREC 2004 Web Track

_Yiqun Liu, Canhui Wang, Min Zhang, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghua.ma](./web/participants.md#tsinghua.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.web.pdf](http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.web.pdf)
- :material-file-search: **Runs:** [THUIRmix041](./web/runs.md#thuirmix041) | [THUIRmix042](./web/runs.md#thuirmix042) | [THUIRmix043](./web/runs.md#thuirmix043) | [THUIRmix044](./web/runs.md#thuirmix044) | [THUIRmix045](./web/runs.md#thuirmix045)

??? abstract "Abstract"
	
	In this year's TREC Web Track research, THUIR participated in the Mixed-query Task. This task involves a single query set comprising 3 kinds of queries (Homepage Finding, Named Page Finding and Topic distillation) which are mixed and unlabelled. Efforts have been made on two directions: to find a strong and robust unified approach which works well for all kinds of queries, and to build a query-specific retrieval strategy that classifies queries by types and perform specific approaches. The using of non-content information has been studied in both approaches. With topic distillation and navigational search tasks in the last year, we are able to build a training set with 150 topics and corresponding relevant qrels. This training set is used to evaluate effectiveness of different methods in mixed query search. Experiments in section 2, 3 and 4 are all based on this set.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuWZM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuWZM04,
		author = {Yiqun Liu and Canhui Wang and Min Zhang and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Finding "Abstract Fields" of Web Pages and Query Specific Retrieval - {THUIR} at {TREC} 2004 Web Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.web.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiuWZM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SJTU at TREC 2004: Web Track Experiments

_Yiming Lu, Jian Hu, Fanyuan Ma_

- :fontawesome-solid-user-group: **Participant:** [shanghai.u.fanyuan](./web/participants.md#shanghai.u.fanyuan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/shanghaiu.web.pdf](http://trec.nist.gov/pubs/trec13/papers/shanghaiu.web.pdf)
- :material-file-search: **Runs:** [SJTUINCMIX2](./web/runs.md#sjtuincmix2) | [SJTUINCMIX5](./web/runs.md#sjtuincmix5) | [SJTUINCMIX4](./web/runs.md#sjtuincmix4) | [SJTUINCMIX3](./web/runs.md#sjtuincmix3) | [SJTUINCMIX1](./web/runs.md#sjtuincmix1)

??? abstract "Abstract"
	
	This is the first year our lab to participate in Trec. We participate in Mixed-Query task for the Web track. All the runs we submitted are based on the modified Okapi weighting scheme. Besides, we used several heuristics as the re-rank method: site-merging, minimal span weight, and etc. Also, the PageRank of a document is combined with the similarity of the document with the query to obtain an overall ranking of documents. Especially for the mixed-query task, we try a simple classification method to estimate whether the query is topic distillation or entry-page finding.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuHM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuHM04,
		author = {Yiming Lu and Jian Hu and Fanyuan Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{SJTU} at {TREC} 2004: Web Track Experiments},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/shanghaiu.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuHM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Towards Grid-Based Information Retrieval

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [u.alaska](./web/participants.md#u.alaska)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ualaska.web.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/ualaska.web.tera.pdf)
- :material-file-search: **Runs:** [irtbow](./web/runs.md#irtbow) | [irtphr2](./web/runs.md#irtphr2) | [irttil](./web/runs.md#irttil)

??? abstract "Abstract"
	
	The IRTools software toolkit was used in TREC 2004 for submissions to the Web track and the Terabyte track. Terabyte track results were not available at the time of the due date for this Proceedings paper. While Web track results were available, qrels were not. Because we discovered a bug in the MySQL++ API that truncated docid numbers in our results, we will await qrels to reevaluate submitted runs and report results. This year, the Terabyte track dictated some changes to IRTools in order to handle the 430+GB of text (about 25M documents). The main change was to operate on chunks of the collection (272 separate chunks, each containing one of the Terabyte collections' subdirectories). Chunks were generated in parallel using the National Center for Supercomputing Application's cluster, Mercury (dual Itanium systems). Up to about 40 systems were used simultaneously for both indexing and querying. Query merging was simplistic, based on the cosine value with Lnu.Ltc weighting. Use of the NCSA cluster, and other experiments with commodity clusters, is part of work underway to enable information retrieval in Grid computing environments. The site http://www.gir-wg.org has information about Grid Information Retrieval (GIR), including links to the published Requirements document and draft Architecture document. The GIR working group is chartered by the Global Grid Forum (GGF) to develop standards and reference implementations for GIR. TREC participants are urged to consider getting involved with Grid computing. Computational grids offer a very good fit for the needs of large-scale information retrieval research and practice. This brief abstract for the proceedings will be replaced with a complete analysis of this year's submissions for the full conference paper. Meanwhile, Newby (2004) provides a profile of IRTools, which is generally applicable to this year's submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Newby04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Newby04,
		author = {Gregory B. Newby},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Towards Grid-Based Information Retrieval},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ualaska.web.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Newby04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2004: Experiments in Web, Robust,  and Terabyte Tracks with Terrier

_Vassilis Plachouras, Ben He, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [u.glasgow](./web/participants.md#u.glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf)
- :material-file-search: **Runs:** [uogWebCA](./web/runs.md#uogwebca) | [uogWebCAU150](./web/runs.md#uogwebcau150) | [uogWebSelAn](./web/runs.md#uogwebselan) | [uogWebSelL](./web/runs.md#uogwebsell) | [uogWebSelAnL](./web/runs.md#uogwebselanl)

??? abstract "Abstract"
	
	With our participation in TREC2004, we test Terrier, a modular and scalable Information Retrieval framework, in three tracks. For the mixed query task of the Web track, we employ a decision mechanism for selecting appropriate retrieval approaches on a per-query basis. For the robust track, in order to cope with the poorly-performing queries, we use two pre-retrieval performance predictors and a weighting function recommender mechanism. We also test a new training approach for the automatic tuning of the term frequency normalisation parameters. In the Terabyte track, we employ a distributed version of Terrier and test the effectiveness of techniques, such as using the anchor text, query expansion and selecting an optimal weighting model for each query. Overall, in all three tracks we participated, Terrier and the tested Divergence From Randomness models were shown to be stable and effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PlachourasHO04.bib) "
	```
	@inproceedings{DBLP:conf/trec/PlachourasHO04,
		author = {Vassilis Plachouras and Ben He and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2004: Experiments in Web, Robust, and Terabyte Tracks with Terrier},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uglasgow.web.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PlachourasHO04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research Asia at Web Track and Terabyte Track of TREC  2004

_Ruihua Song, Ji-Rong Wen, Shuming Shi, Guomao Xin, Tie-Yan Liu, Tao Qin, Xin Zheng, Jiyu Zhang, Gui-Rong Xue, Wei-Ying Ma_

- :fontawesome-solid-user-group: **Participant:** [microsoft.asia](./web/participants.md#microsoft.asia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/microsoft-asia.web.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/microsoft-asia.web.tera.pdf)
- :material-file-search: **Runs:** [MSRAQCSVM54](./web/runs.md#msraqcsvm54) | [MSRAQC2](./web/runs.md#msraqc2) | [MSRAQC3](./web/runs.md#msraqc3) | [MSRAQC4](./web/runs.md#msraqc4) | [MSRAQC5](./web/runs.md#msraqc5) | [MSRAmixed1](./web/runs.md#msramixed1) | [MSRAmixed3](./web/runs.md#msramixed3) | [MSRAx5](./web/runs.md#msrax5) | [MSRAx2](./web/runs.md#msrax2) | [MSRAx4](./web/runs.md#msrax4)

??? abstract "Abstract"
	
	Here we report Microsoft Research Asia (MSRA)'s experiments on the mixed query task of Web track and Terabyte track at TREC 2004. For Web track, we mainly test a set of new technologies. One of our efforts is to test some new features of Web pages to see if they are helpful to retrieval performance. Title extraction, sitemap based feature propagation, and URL scoring are of this kind. Another effort is to propose new function or algorithm to improve relevance or importance ranking. For example, we found that a new link analysis algorithm named HostRank that can outweigh PageRank [4] for topic distillation queries based on our experimental results. Eventually, linear combination of multiple scores with normalizations is tried to achieve stable performance improvement with mixed queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SongWSXLQZZXM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SongWSXLQZZXM04,
		author = {Ruihua Song and Ji{-}Rong Wen and Shuming Shi and Guomao Xin and Tie{-}Yan Liu and Tao Qin and Xin Zheng and Jiyu Zhang and Gui{-}Rong Xue and Wei{-}Ying Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research Asia at Web Track and Terabyte Track of {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/microsoft-asia.web.tera.pdf},
		timestamp = {Tue, 01 Dec 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SongWSXLQZZXM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Meiji University Web, Novelty and Genomic Track Experiments

_Tomoe Tomiyama, Kosuke Karoji, Takeshi Kondo, Yuichi Kakuta, Tomohiro Takagi_

- :fontawesome-solid-user-group: **Participant:** [meiji.u](./web/participants.md#meiji.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf)
- :material-file-search: **Runs:** [MeijiHILw1](./web/runs.md#meijihilw1) | [MeijiHILw2](./web/runs.md#meijihilw2) | [MeijiHILw4](./web/runs.md#meijihilw4) | [MeijiHILwqc](./web/runs.md#meijihilwqc) | [MeijiHILw3](./web/runs.md#meijihilw3) | [MeijiHILw5](./web/runs.md#meijihilw5)

??? abstract "Abstract"
	
	We participated in Novelty track, the topic distillation task of Web track and ad hoc task of Genomic Track. Our main challenge is to deal with meaning of words and improve retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TomiyamaKKKT04.bib) "
	```
	@inproceedings{DBLP:conf/trec/TomiyamaKKKT04,
		author = {Tomoe Tomiyama and Kosuke Karoji and Takeshi Kondo and Yuichi Kakuta and Tomohiro Takagi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Meiji University Web, Novelty and Genomic Track Experiments},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TomiyamaKKKT04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Robust, Web and Terabyte Retrieval with Hummingbird SearchServer at  TREC 2004

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./web/participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf](http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf)
- :material-file-search: **Runs:** [humW04rdpl](./web/runs.md#humw04rdpl) | [humW04dpl](./web/runs.md#humw04dpl) | [humW04pl](./web/runs.md#humw04pl) | [humW04l](./web/runs.md#humw04l) | [humW04dp](./web/runs.md#humw04dp)

??? abstract "Abstract"
	
	Hummingbird participated in 3 tracks of TREC 2004: the ad hoc task of the Robust Retrieval Track (find at least one relevant document in the first 10 rows from 1.9GB of news and government data), the mixed navigational and distillation task of the Web Track (find the home or named page or key resource pages in 1.2 million pages (18GB) from the .GOV domain), and the ad hoc task of the Terabyte Track (find all the relevant documents with high precision from 25.2 million pages (426GB) from the .GOV domain). In the robustness task, SearchServer found a relevant document in the first 10 rows for 46 of the 49 new short (Title-only) topics. In the web task, SearchServer returned a desired page in the first 10 rows for more than 75% of the 225 queries. In the terabyte task, SearchServer found a relevant document in the first 10 rows for 45 of the 49 short topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson04,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Robust, Web and Terabyte Retrieval with Hummingbird SearchServer at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/humingbird.robust.web.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2004 Genomics, Hard, Robust and Web Tracks

_Kiduk Yang, Ning Yu, Adam Wead, Gavin La Rowe, Yu-Hsiu Li, Christopher Friend, Yoon Lee_

- :fontawesome-solid-user-group: **Participant:** [indiana.u.yang](./web/participants.md#indiana.u.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf](http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf)
- :material-file-search: **Runs:** [wdbs1f1](./web/runs.md#wdbs1f1) | [wdbyhf1](./web/runs.md#wdbyhf1) | [wdbyhc1](./web/runs.md#wdbyhc1) | [wdf3oks0b](./web/runs.md#wdf3oks0b) | [wdf3oks0a](./web/runs.md#wdf3oks0a) | [wdf3oks0arr1](./web/runs.md#wdf3oks0arr1) | [wdf3oks0brr1](./web/runs.md#wdf3oks0brr1)

??? abstract "Abstract"
	
	To facilitate understanding of information as well as its discovery, we need to combine the capabilities of the human and the machine as well as multiple methods and sources of evidence. Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science houses several projects that aim to apply this idea of multi-level fusion in the areas of information retrieval and knowledge organization. The TREC research group of WIDIT, who engages in examination of information retrieval strategies that can accommodate a variety of data environments and search tasks, participated in the Genomics, HARD, Robust, and Web tracks in TREC-2004. The basic approach of WIDIT was to leverage multiple sources of evidence, combine multiple methods, and integrate the strengths of man and the machine. Our main strategies for the tracks were: the use of gene name thesaurus in the Genomics track; query expansion and relevance feedback in the HARD track; query expansion with keywords from Web search in the Robust track, and the interactive system tuning process called “Dynamic Tuning” in the Web track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYWRLFL04.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYWRLFL04,
		author = {Kiduk Yang and Ning Yu and Adam Wead and Gavin La Rowe and Yu{-}Hsiu Li and Christopher Friend and Yoon Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2004 Genomics, Hard, Robust and Web Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf},
		timestamp = {Tue, 24 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangYWRLFL04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC 13: Web and Hard Tracks

_Hugo Zaragoza, Nick Craswell, Michael J. Taylor, Suchi Saria, Stephen E. Robertson_

- :fontawesome-solid-user-group: **Participant:** [microsoft.robertson](./web/participants.md#microsoft.robertson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/microsoft-cambridge.web.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/microsoft-cambridge.web.hard.pdf)
- :material-file-search: **Runs:** [MSRC04B1S](./web/runs.md#msrc04b1s) | [MSRC04B2S](./web/runs.md#msrc04b2s) | [MSRC04B1S2](./web/runs.md#msrc04b1s2) | [MSRC04B3S](./web/runs.md#msrc04b3s) | [MSRC04C12](./web/runs.md#msrc04c12)

??? abstract "Abstract"
	
	All our submissions from the Microsoft Research Cambridge (MSRC) team this year continue to explore issues in IR from a perspective very close to that of the original Okapi team, working first at City University of London, and then at MSRC. A summary of the contributions by the team, from TRECs 1 to 7 is presented in [3]. In this work, weighting schemes for ad-hoc retrieval were developed, inspired by a probabilistic interpretation of relevance; this lead, for instance, to the successful BM25 weighting function. These weighting schemes were extended to deal with pseudo relevance feedback (blind feedback). Furthermore, the Okapi team participated in most of the early interactive tracks, and also developed iterative relevance feedback strategies for the routing task. Following up on the routing work, TRECs 7-11 submissions dealt principally with the adaptive filtering task; this work is summarised in [5]. Last year MSRC entered only the HARD track, concentrating on the use of the clarification forms [6]. We hoped to make use of the query expansion methods developed for filtering in the context of feedback on snippets in the clarification forms. However, our methods were not very successful. In this year's TREC we took part in the HARD and WEB tracks. In HARD, we tried some variations on the process of feature selection for query expansion. On the WEB track, we investigated the combination of information from different content fields and from link-based features. Section 3 briefly describes the system we used. Section 4 describes our HARD participation and Section 5 our TREC participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZaragozaCTSR04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZaragozaCTSR04,
		author = {Hugo Zaragoza and Nick Craswell and Michael J. Taylor and Suchi Saria and Stephen E. Robertson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Cambridge at {TREC} 13: Web and Hard Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/microsoft-cambridge.web.hard.pdf},
		timestamp = {Tue, 04 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZaragozaCTSR04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2004 Web Track Experiments at CAS-ICT

_Zhaotao Zhou, Yan Guo, Bin Wang, Xueqi Cheng, Hongbo Xu, Gang Zhang_

- :fontawesome-solid-user-group: **Participant:** [cas.ict.wang](./web/participants.md#cas.ict.wang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/cas.ict.web.pdf](http://trec.nist.gov/pubs/trec13/papers/cas.ict.web.pdf)
- :material-file-search: **Runs:** [ICT04MNZ3](./web/runs.md#ict04mnz3) | [ICT04basic](./web/runs.md#ict04basic) | [ICT04CIIS1AT](./web/runs.md#ict04ciis1at) | [ICT04CIILC](./web/runs.md#ict04ciilc) | [ICT04RULE](./web/runs.md#ict04rule)

??? abstract "Abstract"
	
	This report presents CAS-ICT's experiments on the Mixed query task of the TREC2004 Web track. Our work focused on combining different Web page evidences together to improve the overall retrieval performance. Four kinds of evidences, including body content(C), anchor texts (AT), basic structural information (S0) and extended structural information (S1) were considered for retrieval. Six combination functions were investigated in our experiments. The experimental results show that most functions can improve the retrieval performance. Some heuristic re-ranking techniques were also introduced and tested in the task. No query classification was made during the experiments. Keywords: Web retrieval, TREC 2004, the Mixed query task, information fusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouGWCXZ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouGWCXZ04,
		author = {Zhaotao Zhou and Yan Guo and Bin Wang and Xueqi Cheng and Hongbo Xu and Gang Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2004 Web Track Experiments at {CAS-ICT}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/cas.ict.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouGWCXZ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

