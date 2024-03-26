# Proceedings 1999 

## Overview of the Eighth Text REtrieval Conference (TREC-8)

_Ellen M. Voorhees, Donna Harman_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/overview_8.ps](http://trec.nist.gov/pubs/trec8/papers/overview_8.ps)
??? abstract "Abstract"
	
	The eighth Text REtrieval Conference (TREC-8) was held at the National Institute of Standards and Technology (NIST) on November 16-19, 1999. The conference was co-sponsored by NIST and the Information Technology Office of the Defense Advanced Research Projects Agency (DARPA). TREC-8 is the latest in a series of workshops designed to foster research in text retrieval. For analyses of the results of previous workshops, see Tague-Sutcliffe and Blustein [11], Harman (4], and Sparck Jones [10]. In addition, the overview paper in each of the previous TREC proceedings summarizes the results of that TREC. The TREC workshop series has the following goals: to encourage research in text retrieval based on large test collections; to increase communication among industry, academia, and government by creating an open forum for the exchange of research ideas; to speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems; and to increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current systems. Table 1 lists the groups that participated in TREC-8. Sixty-six groups including participants from 16 different countries were represented. The diversity of the participating groups has ensured that TREC represents many different approaches to text retrieval. The emphasis on individual experiments evaluated within a common setting has proven to be a major strength of TREC. This paper serves as an introduction to the research described in detail in the remainder of the volume. It concentrates on the main task, ad hoc retrieval, which is defined in the next section. Details regarding the test collections and evaluation methodology used in TREC follow in sections 3 and 4, while section 5 provides an overview of the ad hoc retrieval results. In addition to the main ad hoc task, TREC-8 contained seven tracks, tasks that focus research on particular subproblems of text retrieval. Taken together, the tracks represent the bulk of the experiments performed in TREC-8. However, each track has its own overview paper included in the proceedings, so this paper presents only a short summary of each track in section 6. The final section looks forward to future TREC conferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VoorheesH99.bib)"
	```
	@inproceedings{DBLP:conf/trec/VoorheesH99,
		author = {Ellen M. Voorhees and Donna Harman},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of the Eighth Text REtrieval Conference {(TREC-8)}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/overview\_8.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VoorheesH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Adhoc 

#### IRIS at TREC-8

_Kiduk Yang, Kelly Maglaughlin_

- :fontawesome-solid-user-group: **Participant:** [UNC](./adhoc/participants.md#unc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/unc_tr8final.pdf](http://trec.nist.gov/pubs/trec8/papers/unc_tr8final.pdf)
- :material-file-search: **Runs:** [unc8al32](./adhoc/runs.md#unc8al32) | [unc8al42](./adhoc/runs.md#unc8al42) | [unc8al52](./adhoc/runs.md#unc8al52)

??? abstract "Abstract"
	
	We tested two relevance feedback models, an adaptive linear model and a probabilistic model, using massive feedback query expansion in TREC-S (Sumner & Shaw, 1997), experimented with a three-valued scale of relevance and reduced feedback query expansion in TREC-6 (Sumner, Yang, Akers & Shaw, 1998), and examined the effectiveness of relevance feedback using a subcollection and the effect of system features in an interactive retrieval system called IRIS (Information Retrieval Interactive System') in TREC-7 (Yang, Maglaughlin, Mehol & Sumner, 1999). In TREC-8, we continued our exploration of relevance feedback approaches. Based on the result of our TREC-7 interactive experiment, which suggested relevance feedback using user-selected passages to be an effective alternative to conventional document feedback, our TREC-8 interactive experiment compared a passage feedback system and a document feedback system that were identical in all aspects except for the feedback mechanism. For the TREC-8 ad-hoc task, we merged results of pseudo-relevance feedback to subcollections as in TREC-7. Our results were consistent with that of TREC-7. The results of passage feedback, whose system log showed high level of searcher intervention, was superior to the document feedback results. As in TREC-7, our ad-hoc results showed high precision in top few documents, but performed poorly overall compared to results using the collection as a whole.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangM99,
		author = {Kiduk Yang and Kelly Maglaughlin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{IRIS} at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/unc\_tr8final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Mirror DBMS at TREC-8

_Arjen P. de Vries, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [utwente](./adhoc/participants.md#utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ut.trec8.pdf](http://trec.nist.gov/pubs/trec8/papers/ut.trec8.pdf)
- :material-file-search: **Runs:** [UT810](./adhoc/runs.md#ut810) | [UT800](./adhoc/runs.md#ut800) | [UT803](./adhoc/runs.md#ut803) | [UT803b](./adhoc/runs.md#ut803b) | [UT813](./adhoc/runs.md#ut813)

??? abstract "Abstract"
	
	The database group at University of Twente participates in TREC-8 using the Mirror DBMS, a prototype database system especially designed for multimedia and web retrieval. From a database perspective, the purpose has been to check whether we can get sufficient performance, and to prepare for the very large corpus track in which we plan to participate next year. From an IR perspective, the experiments have been designed to learn more about the effect of the global statistics on the ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VriesH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/VriesH99,
		author = {Arjen P. de Vries and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Mirror {DBMS} at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ut.trec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VriesH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NTT DATA: Overview of system approach at TREC-8 ad-hoc and question  answering

_Toru Takaki_

- :fontawesome-solid-user-group: **Participant:** [ntt](./adhoc/participants.md#ntt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-nttdata.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-nttdata.pdf)
- :material-file-search: **Runs:** [nttd8ale](./adhoc/runs.md#nttd8ale) | [nttd8alx](./adhoc/runs.md#nttd8alx) | [nttd8al](./adhoc/runs.md#nttd8al) | [nttd8ame](./adhoc/runs.md#nttd8ame) | [nttd8am](./adhoc/runs.md#nttd8am)

??? abstract "Abstract"
	
	In TREC-8, NTT Data Corporation participated in the ad-hoc task and question answering track. In this paper, we describe our system approach and discuss the results. The summary of each task of our approach is shown below.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Takaki99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Takaki99,
		author = {Toru Takaki},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{NTT} {DATA:} Overview of system approach at {TREC-8} ad-hoc and question answering},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-nttdata.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Takaki99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Natural Language Information Retrieval: TREC-8 Report

_Tomek Strzalkowski, Jose Perez Carballo, Jussi Karlgren, Anette Hulth, Pasi Tapanainen, Timo Lahtinen_

- :fontawesome-solid-user-group: **Participant:** [ge](./adhoc/participants.md#ge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ge8adhoc2.pdf](http://trec.nist.gov/pubs/trec8/papers/ge8adhoc2.pdf)
- :material-file-search: **Runs:** [8manexT3D1N0](./adhoc/runs.md#8manext3d1n0) | [GE8ATDN1](./adhoc/runs.md#ge8atdn1) | [GE8ATDN2](./adhoc/runs.md#ge8atdn2) | [GE8ATD3](./adhoc/runs.md#ge8atd3) | [GE8MTD2](./adhoc/runs.md#ge8mtd2)

??? abstract "Abstract"
	
	This report describes the adhoc experiments performed by the GE/Rutgers/SICS/SU/Conexor team in the context of TREC-8. The research efforts went in four directions: 1. As in previous years, we performed a full linguistic analysis of the entire corpus, and used the results of the analysis to provide index terms on a higher level of abstraction than can be provided by stems alone. 2. We made use of two different query expansion techniques, one automatic and one manual, both developed for TREC-8. 3. The various analysis models were combined using a stream model architecture, where each stream represents an alternative text indexing method, and the stream's various overlapping knowledge was merged using a new merging algorithm derived from first principles. 4. The entire text was analyzed for various stylistic items. Due to the distributed approach, this years' research efforts partly canceled out each other. New experiments in every step of the process did not result in an overwhelming overall result. We are able to determine that the manual query expansion technique developed at General Electric performed very well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrzalkowskiCKHTL99.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrzalkowskiCKHTL99,
		author = {Tomek Strzalkowski and Jose Perez Carballo and Jussi Karlgren and Anette Hulth and Pasi Tapanainen and Timo Lahtinen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Natural Language Information Retrieval: {TREC-8} Report},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ge8adhoc2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StrzalkowskiCKHTL99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SCAI TREC-8 Experiments

_Dong-Ho Shin, Yu-Hwan Kim, Sun Kim, Jae-Hong Eom, Hyung-Joo Shin, Byoung-Tak Zhang_

- :fontawesome-solid-user-group: **Participant:** [seoul](./adhoc/participants.md#seoul)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps](http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps)
- :material-file-search: **Runs:** [Scai8Adhoc](./adhoc/runs.md#scai8adhoc)

??? abstract "Abstract"
	
	This working note reports our experiences with TREC-8 on four tracks: Ad Hoc, Filtering, Web, and QA. The Ad Hoc retrieval engine, SCAIR, has been used for the Web and QA experiments, and the filtering experiments were based on it's own engine. As a second entry to TREC, we focused this year on exploring possibilities of applying machine learning techniques to TREC tasks. The Ad Hoc track employed a cluster-based retrieval method where the scoring function used cluster information extracted from a collection of precompiled documents. Filtering was based on naive Bayes learning supported by an EM algorithm. In the Web track, we compared the performance of using link information to that of not using the information. In the QA track, some passage extraction techniques have been tested using the baseline SCAIR retrieval engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShinKKESZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShinKKESZ99,
		author = {Dong{-}Ho Shin and Yu{-}Hwan Kim and Sun Kim and Jae{-}Hong Eom and Hyung{-}Joo Shin and Byoung{-}Tak Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SCAI} {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShinKKESZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Novel Query Expansion Technique using Apriori Algorithm

_Arnon Rungsawang, Athichart Tangpong, Pawat Laohawee, Tawa Khampachua_

- :fontawesome-solid-user-group: **Participant:** [kasetsart](./adhoc/participants.md#kasetsart)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-ku.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-ku.pdf)
- :material-file-search: **Runs:** [kuadhoc](./adhoc/runs.md#kuadhoc)

??? abstract "Abstract"
	
	One problem in query reformulation process is to find an optimal set of terms to add to the old query. In our TREC experiments this year, we propose to use the association rule discovery (especially apriori algorithm) to find good candidate terms to enhance the query. These candidate terms are automatically derived from collection, added to the original query to build a new one. Experiments conducted on a subset of TREC collections gives quite promising results. We achieve a 19% improvement with old TREC7 adhoc queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RungsawangTLK99.bib) "
	```
	@inproceedings{DBLP:conf/trec/RungsawangTLK99,
		author = {Arnon Rungsawang and Athichart Tangpong and Pawat Laohawee and Tawa Khampachua},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Novel Query Expansion Technique using Apriori Algorithm},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-ku.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RungsawangTLK99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Automatic Query Feedback using Related Words

_Stefan M. Rüger_

- :fontawesome-solid-user-group: **Participant:** [imperial](./adhoc/participants.md#imperial)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ic99dafb.pdf](http://trec.nist.gov/pubs/trec8/papers/ic99dafb.pdf)
- :material-file-search: **Runs:** [ic99dafb](./adhoc/runs.md#ic99dafb)

??? abstract "Abstract"
	
	Our experiments for the ad hoc task of TREC & were centered around the question how to create an automatic query feedback from the documents returned by an initial query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Ruger99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Ruger99,
		author = {Stefan M. R{\"{u}}ger},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Automatic Query Feedback using Related Words},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ic99dafb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Ruger99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieval Performance and Visual Dispersion of Query Sets

_Mark E. Rorvig_

- :fontawesome-solid-user-group: **Participant:** [ntexas](./adhoc/participants.md#ntexas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/unt_rorvig.pdf](http://trec.nist.gov/pubs/trec8/papers/unt_rorvig.pdf)
- :material-file-search: **Runs:** [1](./adhoc/runs.md#1)

??? abstract "Abstract"
	
	In the course of eight TREC Conferences, retrieval performance of all systems started high and then declined. This was especially true for conference 5. Only in conferences 7 and 8 have performance levels reached those initially achieved. In this paper, scaling of the corpus of 450 TREC topics is performed. It is observed that as the visual dispersion of a topic set increases, the level of retrieval performance across systems declines for that set. Conversely, as the visual dispersion of topics decreases, system performance rises. In common elements of conferences 2, 5, and 8, this relationship appears to hold despite increases in the number of participating systems in TREC. It is proposed that visual dispersion measures should be used to describe topic set difficulty in addition to measures such as 'hardness'.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Rorvig99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Rorvig99,
		author = {Mark E. Rorvig},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Retrieval Performance and Visual Dispersion of Query Sets},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/unt\_rorvig.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Rorvig99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi/Keenbow at TREC-8

_Stephen E. Robertson, Steve Walker_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./adhoc/participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/okapi.pdf](http://trec.nist.gov/pubs/trec8/papers/okapi.pdf)
- :material-file-search: **Runs:** [ok8amxc](./adhoc/runs.md#ok8amxc) | [ok8asxc](./adhoc/runs.md#ok8asxc) | [ok8alx](./adhoc/runs.md#ok8alx)

??? abstract "Abstract"
	
	Automatic ad hoc and web track: Three ad hoc runs were submitted: long (title, description and narrative), medium (title and description) and short (title only). 'Blind' expansion was used for all runs. The queries from the medium ad hoc run were reused for the small web track submission. Most of the negative expressions were removed from the narrative field of the topic statements, and a new expansion term selection procedure was tried. Adaptive filtering: Methods were similar to those we used in TREC-7. Six runs were submitted. VLC track: Two unexpanded ad hoc runs were submitted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonW99,
		author = {Stephen E. Robertson and Steve Walker},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi/Keenbow at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/okapi.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Structuring and expanding queries in the probabilistic model

_Yasushi Ogawa, Hiroko Mano, Masumi Narita, Sakiko Honma_

- :fontawesome-solid-user-group: **Participant:** [ricoh](./adhoc/participants.md#ricoh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ricoh_notebook.pdf](http://trec.nist.gov/pubs/trec8/papers/ricoh_notebook.pdf)
- :material-file-search: **Runs:** [ric8tpn](./adhoc/runs.md#ric8tpn) | [ric8dpn](./adhoc/runs.md#ric8dpn) | [ric8dpx](./adhoc/runs.md#ric8dpx) | [ric8dnx](./adhoc/runs.md#ric8dnx) | [ric8tpx](./adhoc/runs.md#ric8tpx)

??? abstract "Abstract"
	
	This is our first participation in TREC and five runs were submitted for the ad-hoc main task. Our system is based on our Japanese text retrieval system 4, to which English tok-enizer/stemmer has been added to process English text. Our indexing system stores term positions, thus providing proximity-based search, in which the user can specify the distance between query terms. What our system does is outlined as follows: 1. Query construction The query constructor accepts each topic, extracts words in each of the appropriate fields and constructs a query to be supplied to the ranking system. 2. Initial retrieval The constucted query is fed into the ranking system, which then assigns term weights to query terms, scores each document and turns up a set of top-ranking documents assumed to be relevant to the topic (pseudo-relevant documents). 3. Query expansion Based on the feedback from the pseudo-relevant documents, the query expander collects and ranks the words in the pseudo-relevant documents and the words ranked the highest are added to the original query, with the words already in the query re-assigned new term weights. 4. Final retrieval The ranking system performs final retrieval using the modified query. In what follows, we explain what is done in each of the steps in more detail.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OgawaMNH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/OgawaMNH99,
		author = {Yasushi Ogawa and Hiroko Mano and Masumi Narita and Sakiko Honma},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Structuring and expanding queries in the probabilistic model},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ricoh\_notebook.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OgawaMNH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Maximum Likelihood Ratio Information Retrieval Model

_Kenney Ng_

- :fontawesome-solid-user-group: **Participant:** [MIT](./adhoc/participants.md#mit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/MITSLS_v2.pdf](http://trec.nist.gov/pubs/trec8/papers/MITSLS_v2.pdf)
- :material-file-search: **Runs:** [MITSLStdn](./adhoc/runs.md#mitslstdn) | [MITSLStd](./adhoc/runs.md#mitslstd)

??? abstract "Abstract"
	
	In this paper we present a novel probabilistic information retrieval model that scores documents based on the relative change in the document likelihoods, expressed as the ratio of the conditional probability of the document given the query and the prior probability of the document before the query is specified. The document likelihoods are computed using statistical language modeling techniques and the model parameters are estimated automatically and dynamically for each query to optimize well-specified (maximum likelihood) objective functions. We derive the basic retrieval model, describe the details of the model, and present some extensions to the model including a method to perform automatic feedback. Development experiments are performed using the TREC-6 ad hoc text retrieval task and performance is measured using the TREC-7 ad hoc task. Official evaluation results on the 1999 TREC-8 ad hoc task are also reported. The performance results demonstrate that the model is competitive with current state-of-the-art retrieval approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Ng99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Ng99,
		author = {Kenney Ng},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A Maximum Likelihood Ratio Information Retrieval Model},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/MITSLS\_v2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Ng99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Moving More Quickly toward Full Term Relations in Information Space

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [Newby](./adhoc/participants.md#newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/newby-trec99-proceedings.pdf](http://trec.nist.gov/pubs/trec8/papers/newby-trec99-proceedings.pdf)
- :material-file-search: **Runs:** [isa25](./adhoc/runs.md#isa25) | [isa50](./adhoc/runs.md#isa50) | [isa25t](./adhoc/runs.md#isa25t) | [isa50t](./adhoc/runs.md#isa50t)

??? abstract "Abstract"
	
	This paper describes the ISpace retrieval system's involvement in TREC8. The main goal for this year's work was to speed up document indexing and query processing compared to previous years. This goal was achieved, but retrieval performance was not as good as for TREC7. System details for the AdHoc task, small Web task, and large Web (VLC) task are presented. The AdHoc task emphasized query expansion, while the large Web track emphasized rapid indexing and retrieval. The paper describes an implementation of a multidimensional tree structure for retrieval from information space based on the kd-tree. The larger setting for ISpace, the TeraScale Retrieval project, is summarized. A concluding section describes plans for ISpace.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Newby99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Newby99,
		author = {Gregory B. Newby},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Moving More Quickly toward Full Term Relations in Information Space},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/newby-trec99-proceedings.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Newby99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fujitsu Laboratories TREC8 Report - Ad hoc, Small Web, and Large  Web Track

_Isao Namba, Nobuyuki Igata_

- :fontawesome-solid-user-group: **Participant:** [fujitsu](./adhoc/participants.md#fujitsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/flab8_proceedings_letter.pdf](http://trec.nist.gov/pubs/trec8/papers/flab8_proceedings_letter.pdf)
- :material-file-search: **Runs:** [Flab8atdn](./adhoc/runs.md#flab8atdn) | [Flab8as](./adhoc/runs.md#flab8as) | [Flab8atd2](./adhoc/runs.md#flab8atd2) | [Flab8ax](./adhoc/runs.md#flab8ax) | [Flab8at](./adhoc/runs.md#flab8at)

??? abstract "Abstract"
	
	This year a Fujitsu Laboratory team participated in three tracks:that is ad hoc, small web track, and large web track. As basic techiniques, we compared four popular stemmers, and we made simple removing stop pattern techniques for TREC queries. For the ad hoc task, and small web track, we used the same techiniques. We experimented with area weighting, co-occurence boosting, bi-gram utliza-tion, and reranking by bi-gram extraction from pilot search. The effect of blind application with those te-chiniques is rather limited, or even uncertain in the TREC8 experiment. What we can say from TREC8 result is that blind application of co-occurence boosting and area weighting may be effective for the small web track. They requerie query dependent application. In the large web track, our main interest is ef-ficiency, that is how much resources are required to process 100GB of web text and 10000 real web queries in practical time. Using a statistical based language type checker, we can eliminate 23% of non-English text. This leads to speeding up a indexing and reducing the index size. The search speed for an inverted file is CPU intensive if the target machine has main memory in excess of 10-25% of the index size. So with simple, but effective index compression methods, the throughput of query processing is about 0.54-1.1 query/second even by a single 300MHz Ultra-sparc processor.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NambaI99.bib) "
	```
	@inproceedings{DBLP:conf/trec/NambaI99,
		author = {Isao Namba and Nobuyuki Igata},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fujitsu Laboratories {TREC8} Report - Ad hoc, Small Web, and Large Web Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/flab8\_proceedings\_letter.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NambaI99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC-8: Improving Baseline Precision

_M. Catherine McCabe, David O. Holmes, Kenneth L. Alford, Abdur Chowdhury, David A. Grossman, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [iit](./adhoc/participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/iit99pr.pdf](http://trec.nist.gov/pubs/trec8/papers/iit99pr.pdf)
- :material-file-search: **Runs:** [iit99au1](./adhoc/runs.md#iit99au1) | [iit99ma1](./adhoc/runs.md#iit99ma1) | [iit99au2](./adhoc/runs.md#iit99au2)

??? abstract "Abstract"
	
	In TREC-8, we participated in the automatic and manual tracks for category A as well as the small web track. This year, we focussed on improving our baseline and then introduced some experimental improvements. Our automatic runs used relevance feedback with a high-precision first pass to select terms and then a high-recall final pass. For manual runs, we used predefined concept lists focussing on phrases and proper nouns in the query. In the small web-track, we submitted one content-only run and two link-plus-content runs. We continued to use the relational model with unchanged SQL for retrieval. Our results show some promise for the use of automatic concepts, expansion within concepts and a high-precision first pass for relevance feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCabeHACGF99.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCabeHACGF99,
		author = {M. Catherine McCabe and David O. Holmes and Kenneth L. Alford and Abdur Chowdhury and David A. Grossman and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{IIT} at {TREC-8:} Improving Baseline Precision},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/iit99pr.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCabeHACGF99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The JHU/APL HAIRCUT System at TREC-8

_James Mayfield, Paul McNamee, Christine D. Piatko_

- :fontawesome-solid-user-group: **Participant:** [jhu](./adhoc/participants.md#jhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/JHUAPL.pdf](http://trec.nist.gov/pubs/trec8/papers/JHUAPL.pdf)
- :material-file-search: **Runs:** [apl8c221](./adhoc/runs.md#apl8c221) | [apl8n](./adhoc/runs.md#apl8n) | [apl8c621](./adhoc/runs.md#apl8c621) | [apl8p](./adhoc/runs.md#apl8p) | [apl8ctd](./adhoc/runs.md#apl8ctd)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) is a second-time entrant in the TREC Category A evaluation. The focus of our information retrieval research this year has been on the relative value of and interaction among multiple term types and multiple similarity metrics. In particular, we are interested in examining words and n-grams as indexing terms, and vector models and hidden Markov models as similarity metrics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MayfieldMP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/MayfieldMP99,
		author = {James Mayfield and Paul McNamee and Christine D. Piatko},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {JHU/APL} {HAIRCUT} System at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/JHUAPL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MayfieldMP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Oracle at Trec8: A Lexical Approach

_Kavi Mahesh, Jacquelynn Kud, Paul Dixon_

- :fontawesome-solid-user-group: **Participant:** [oracle](./adhoc/participants.md#oracle)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/orcl99man.pdf](http://trec.nist.gov/pubs/trec8/papers/orcl99man.pdf)
- :material-file-search: **Runs:** [orcl99man](./adhoc/runs.md#orcl99man)

??? abstract "Abstract"
	
	Oracle's system for Trec8 was the interMedia Text retrieval engine integrated with the Oraclesi database and SQL query language. interMedia Text supports a novel theme-based document retrieval capability using an extensive lexical knowledge base. Trec8 queries constructed by extracting themes from topic titles and descriptions were manually refined. Queries were simple and intuitive. Oracle's results demonstrate that knowledge-based retrieval is a viable and scalable solution for information retrieval and that statistical training and tuning on the document collection is unnecessary for good performance in Trec.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaheshKD99.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaheshKD99,
		author = {Kavi Mahesh and Jacquelynn Kud and Paul Dixon},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Oracle at Trec8: {A} Lexical Approach},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/orcl99man.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MaheshKD99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Ad-Hoc, Query and Filtering Track Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./adhoc/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf](http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf)
- :material-file-search: **Runs:** [pir9Attd](./adhoc/runs.md#pir9attd) | [pir9Aatd](./adhoc/runs.md#pir9aatd) | [pir9Atd0](./adhoc/runs.md#pir9atd0) | [pir9Aa1](./adhoc/runs.md#pir9aa1) | [pir9At0](./adhoc/runs.md#pir9at0)

??? abstract "Abstract"
	
	In TREC-8, we participated in automatic ad-hoc retrieval as well as the query and filtering tracks. The theme of our participation is 'retrieval lists combination', and the technique is applied throughout our experiments to various degree. It is pointed out that our PIRCS system may be considered as a combination of probabilistic retrieval model and a language model approach. For ad-hoc, three types of experiments were done with short, medium and long queries as before. General approach is similar to TREC-7, but combination of retrieval lists from different query types were used to boost effectiveness. For query track, we submitted one short-query set, and performed retrieval for twenty one natural language query vairants. For filtering track, experiments for adaptive, batch filtering, and routing were performed. For adaptive, historical selected document list was used to train profile term weights and dynamically vary retrieval status value (rsv) threshold for deciding document selection during the course of filtering. For batch filtering, Financial Times FT92 data was used to define 6 retrieval profiles whose results were combined based on coefficients trained via a genetic algorithm. Logistic regression transforms rsv's to probabilities. Routing was similarly done with additional training data obtained from non-FT collections and two additional profiles were defined and combined
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGC99,
		author = {K. L. Kwok and Laszlo Grunfeld and M. Chan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Ad-Hoc, Query and Filtering Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Twenty-One at TREC-8: using Language Technology for Information  Retrieval

_Wessel Kraaij, Renée Pohlmann, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [twentyone](./adhoc/participants.md#twentyone)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf](http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf)
- :material-file-search: **Runs:** [tno8d4](./adhoc/runs.md#tno8d4) | [tno8d3](./adhoc/runs.md#tno8d3) | [tno8t2](./adhoc/runs.md#tno8t2)

??? abstract "Abstract"
	
	This paper describes the official runs of the Twenty-One group for TREC-8. The Twenty-One group participated in the Ad-hoc, CLIR, Adaptive Filtering and SDR tracks. The main focus of our experiments is the development and evaluation of retrieval methods that are motivated by natural language processing techniques. The following new techniques are introduced in this paper. In the Ad-Hoc and CLIR tasks we experimented with automatic sense disambiguation followed by query expansion or translation. We used a combination of thesaurial and corpus information for the disambiguation process. We continued research on CLIR techniques which exploit the target corpus for an implicit disambiguation, by importing the translation probabilities into the probabilistic term-weighting framework. In filtering we extended the the use of language models for document ranking with a relevance feedback algorithm for query term reweighting.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KraaijPH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/KraaijPH99,
		author = {Wessel Kraaij and Ren{\'{e}}e Pohlmann and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Twenty-One at {TREC-8:} using Language Technology for Information Retrieval},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KraaijPH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ACSys TREC-8 Experiments

_David Hawking, Peter Bailey, Nick Craswell_

- :fontawesome-solid-user-group: **Participant:** [ACSys](./adhoc/participants.md#acsys)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/acsys.pdf](http://trec.nist.gov/pubs/trec8/papers/acsys.pdf)
- :material-file-search: **Runs:** [acsys8alo](./adhoc/runs.md#acsys8alo) | [acsys8alo2](./adhoc/runs.md#acsys8alo2) | [acsys8asn](./adhoc/runs.md#acsys8asn) | [acsys8amn](./adhoc/runs.md#acsys8amn) | [acsys8aln2](./adhoc/runs.md#acsys8aln2)

??? abstract "Abstract"
	
	Experiments relating to TREC-8 Ad Hoc, Web Track (Large and Small) and Query Track tasks are described and results reported. Due to time constraints, only minimal effort was put into Ad Hoc and Query Track participation. In the Web Track, Google-style PageRanks were calculated for all 18.5 million pages in the VLC2 collection and for the 0.25 million pages in the WT2g collection. Various combinations of content score and PageRank produced no benefit for TREC style ad hoc retrieval. A major goal in the Web Track was to make engineering improvements to permit indexing of the 100 gigabyte collection and subsequent query processing using a single PC. A secondary goal was to achieve last year's performance (obtained with eight DEC Alphas) with less recourse to effectiveness-harming optimisations. The main goal was achieved and indexing times are comparable to last year's. However, effectiveness results were worse relative to last year and query processing times were approximately double.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingBC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingBC99,
		author = {David Hawking and Peter Bailey and Nick Craswell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ACSys {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/acsys.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingBC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Experiments at SUNY Buffalo

_Benjamin Han, Ramya Nagarajan, Rohini K. Srihari, Srikanth Munirathnam_

- :fontawesome-solid-user-group: **Participant:** [buffalo](./adhoc/participants.md#buffalo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ub-nbpaper.pdf](http://trec.nist.gov/pubs/trec8/papers/ub-nbpaper.pdf)
- :material-file-search: **Runs:** [UB99SW](./adhoc/runs.md#ub99sw) | [UB99T](./adhoc/runs.md#ub99t)

??? abstract "Abstract"
	
	For TREC-8, State University of New York at Buffalo(UB) participated in the ad-hoc task and the spoken document retrieval(SDR) track. This is our first year of participation at TREC. We submitted two runs for the Ad-hoc task. The first run was term vector-based using SMART[10]. The second run used the TROVE - Text Retrieval using Object VEctors - system. For the SDR Track, we participated in the IR component of the Quasi-SDR task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HanNSM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HanNSM99,
		author = {Benjamin Han and Ramya Nagarajan and Rohini K. Srihari and Srikanth Munirathnam},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Experiments at {SUNY} Buffalo},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ub-nbpaper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HanNSM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The RMIT/CSIRO Ad Hoc, Q&A, Web, Interactive, and Speech Experiments  at TREC 8

_Michael Fuller, Marcin Kaszkiel, Sam Kimberley, Corinna Ng, Ross Wilkinson, Mingfang Wu, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [rmit](./adhoc/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf](http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf)
- :material-file-search: **Runs:** [mds08a3](./adhoc/runs.md#mds08a3) | [mds08a2](./adhoc/runs.md#mds08a2) | [mds08a1](./adhoc/runs.md#mds08a1) | [mds08a4](./adhoc/runs.md#mds08a4) | [mds08a5](./adhoc/runs.md#mds08a5)

??? abstract "Abstract"
	
	The focus of our work in TREC 8 has again been on the retrieval of documents using arbitrary passages. This year the system has been refined to include variable sized passages and pivot normalisation. Passage based automatic relevance feedback has also been explored, albeit without the use of negative feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FullerKKNWWZ99,
		author = {Michael Fuller and Marcin Kaszkiel and Sam Kimberley and Corinna Ng and Ross Wilkinson and Mingfang Wu and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {RMIT/CSIRO} Ad Hoc, Q{\&}A, Web, Interactive, and Speech Experiments at {TREC} 8},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc, Cross-language and Spoken Document Information Retrieval at  IBM

_Martin Franz, J. Scott McCarley, Todd Ward_

- :fontawesome-solid-user-group: **Participant:** [ibm-franzs](./adhoc/participants.md#ibm-franzs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/t8_ibm_hlt.pdf](http://trec.nist.gov/pubs/trec8/papers/t8_ibm_hlt.pdf)

??? abstract "Abstract"
	
	The Natural Language Systems group at IBM participated in three tracks at TREC-8: ad hoc, SDR and cross-language. Our SDR and ad hoc participation included experiments involving query expansion and clustering-induced document reranking. Our CLIR participation involved both the French and English queries and included experiments with the merging strategy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FranzMW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FranzMW99,
		author = {Martin Franz and J. Scott McCarley and Todd Ward},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ad hoc, Cross-language and Spoken Document Information Retrieval at {IBM}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/t8\_ibm\_hlt.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FranzMW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLARIT TREC-8 Manual Ad-Hoc Experiments

_David A. Evans, Jeffrey Bennett, Xiang Tong, Alison Huettner, ChengXiang Zhai, Emilia Stoica_

- :fontawesome-solid-user-group: **Participant:** [claritech](./adhoc/participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/CLARIT_ManualAdHoc.pdf](http://trec.nist.gov/pubs/trec8/papers/CLARIT_ManualAdHoc.pdf)
- :material-file-search: **Runs:** [CL99XT](./adhoc/runs.md#cl99xt) | [CL99SD](./adhoc/runs.md#cl99sd) | [CL99SDopt1](./adhoc/runs.md#cl99sdopt1) | [CL99SDopt2](./adhoc/runs.md#cl99sdopt2) | [CL99XTopt](./adhoc/runs.md#cl99xtopt)

??? abstract "Abstract"
	
	CLARITECH's submission in TREC-7 demonstrated the utility of document clustering in retrieval. We continued this work in TREC-8, using a clustered document presentation exclusively. We also added significant new functionality to the manual ad hoc user interface, integrating it with an entity extraction subsystem (upgraded and customized for TREC). Extracted entities represent an alternate set of document features. Our experiments suggest that in many cases users might construct more effective queries by moving beyond surface terms and drawing from this more abstract pool of semantic types. Despite the interface enhancements, our focus this year was on system rather than human subject performance, and we simplified the experiment design accordingly. From the users' perspective, there was only one run; the five separate submissions represent variations in post-processing. We spent minimal time preparing the initial queries. Users had 20 (instead of last year's 30) minutes for relevance judgments, and were allowed to modify the query from the start. This year, as well, we reintroduced 'vector-length optimization' in the post-processing of feedback. Recent CLARITECH systems have augmented the manually generated queries with a fixed, arbitrary number of selected terms from top-ranked documents. This year, we experimented with a principled truncation of the candidate term list, and found this had a positive effect on the performance of both of our TREC-7 and TREC-8 final queries. We feel that further performance improvements are likely to be achieved only by developing several complementary techniques and applying them selectively to fine-tune individual queries. User-directed feature selection and vector-length optimization are two such promising techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EvansBTHZS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/EvansBTHZS99,
		author = {David A. Evans and Jeffrey Bennett and Xiang Tong and Alison Huettner and ChengXiang Zhai and Emilia Stoica},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CLARIT} {TREC-8} Manual Ad-Hoc Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/CLARIT\_ManualAdHoc.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EvansBTHZS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fast Automatic Passage Ranking (MultiText Experiments for TREC-8)

_Gordon V. Cormack, Charles L. A. Clarke, D. I. E. Kisman, Christopher R. Palmer_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./adhoc/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf](http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf)
- :material-file-search: **Runs:** [uwmt8a0](./adhoc/runs.md#uwmt8a0) | [uwmt8a1](./adhoc/runs.md#uwmt8a1) | [uwmt8a2](./adhoc/runs.md#uwmt8a2)

??? abstract "Abstract"
	
	TREC-8 represents the fifth year that the Multilext project has participated in TREC [2, 1, 4, 5]. The MultiText project develops and prototypes scalable technologies for parallel information retrieval systems implemented on networks of workstations. Research issues are addressed in the context of this parallel architecture. Issues of concern to the MultiText Project include data distribution, load balancing, fast update, fault tolerance, document structure, relevance ranking, and user interaction. The MultiText system incorporates a unique technique for arbitrary passage retrieval. Since our initial participation in TREC-4 our TREC work has explored variants of this technique. For TREC-8 we focused our efforts on the Web track. In addition, we submitted runs for the Adhoc task (title and title+description) and a run for the Question Answering task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackCKP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackCKP99,
		author = {Gordon V. Cormack and Charles L. A. Clarke and D. I. E. Kisman and Christopher R. Palmer},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fast Automatic Passage Ranking (MultiText Experiments for {TREC-8)}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackCKP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Automatic Ad-Hoc Experiments at Fondazione Ugo Bordoni

_Claudio Carpineto, Giovanni Romano_

- :fontawesome-solid-user-group: **Participant:** [fub](./adhoc/participants.md#fub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/fub99.pdf](http://trec.nist.gov/pubs/trec8/papers/fub99.pdf)
- :material-file-search: **Runs:** [fub99tf](./adhoc/runs.md#fub99tf) | [fub99a](./adhoc/runs.md#fub99a) | [fub99td](./adhoc/runs.md#fub99td) | [fub99tt](./adhoc/runs.md#fub99tt)

??? abstract "Abstract"
	
	We present further evidence suggesting the feasibilty of using information theoretic query expansion for improving the retrieval effectiveness of automatic document ranking. Compared to our participation in TREC-7, in which we applied this technique to an ineffective initial ranking, here we show that information theoretic query expansion may be effective even when the quality of the first pass ranking is high. In TREC-8 our system has been ranked among the best systems for both automatic ad hoc and short automatic ad hoc. These results are even more interesting considering that we used single-word indexing and well known weighting schemes. We also investigate the use of term variance to refine the weighting schemes employed by our system to weight documents and queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarpinetoR99.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarpinetoR99,
		author = {Claudio Carpineto and Giovanni Romano},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Automatic Ad-Hoc Experiments at Fondazione Ugo Bordoni},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/fub99.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarpinetoR99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SMART in TREC 8

_Chris Buckley, Janet A. Walz_

- :fontawesome-solid-user-group: **Participant:** [cornell](./adhoc/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/sabir8.pdf](http://trec.nist.gov/pubs/trec8/papers/sabir8.pdf)
- :material-file-search: **Runs:** [Sab8A1](./adhoc/runs.md#sab8a1) | [Sab8A2](./adhoc/runs.md#sab8a2) | [Sab8A3](./adhoc/runs.md#sab8a3) | [Sab8A4](./adhoc/runs.md#sab8a4)

??? abstract "Abstract"
	
	This year was a light year for the Smart Information Retrieval Project at SabIR Research and Cornell. We officially participated in only the Ad-hoc Task and the Query Track. In the Ad-hoc Task, we made minor modifications to our document weighting schemes to emphasize high-precision searches on shorter queries. This proved only mildly successful; the top relevant document was retrieved higher, but the rest of the retrieval tended to be hurt. Our Query Track runs are described here, but the much more interesting analysis of these runs is described in the Query Track Overview.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyW99a.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyW99a,
		author = {Chris Buckley and Janet A. Walz},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SMART} in {TREC} 8},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/sabir8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyW99a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at trec8: Adhoc, Web, CLIR and Filtering tasks

_Mohand Boughanem, Christine Julien, Josiane Mothe, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [irit](./adhoc/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/irit.pdf](http://trec.nist.gov/pubs/trec8/papers/irit.pdf)
- :material-file-search: **Runs:** [Mer8Adtd1](./adhoc/runs.md#mer8adtd1) | [Mer8Adtd2](./adhoc/runs.md#mer8adtd2) | [Mer8Adtnd3](./adhoc/runs.md#mer8adtnd3) | [Mer8Adtd4](./adhoc/runs.md#mer8adtd4)

??? abstract "Abstract"
	
	The tests performed for TREC8 were focused on automatic Adhoc, Web, Clir and Filtering (batch and routing) tasks. All the submitted runs were based on the Mercure system. Automatic adhoc : Four runs were submitted. All these runs were based on automatic relevance back-propagation used in the previous TREC, with a slight change for one of these runs (Mer8Adtd3). A strategy based on predicting the relevance of documents using the past relevant documents was tested for this run. More precisely, instead of using the same relevance value for all top retrieved documents, some of them are selected and have their relevance value boosted. Web : Four runs were submitted in this track: 1. content based only using Mercure simple search 2. content tilink, according to Mercure architecture, we consider that document nodes are linked each other by weighted links. The top selected documents resulting from the initial search spread their signals towards the other document nodes. The documents were then sorted according to their activations, the top 1000 documents were submitted. 3. (2) + pseudo-relevance back-propagation method. 4. reranking of the 40 top documents using their links between each others. Cross-language : Three runs were submitted for our first participation in this track. All these runs were based on query translation using an online machine translation . Two of these runs are a comparison between query translation from English to other languages and from French to other languages. Filtering - batch and routing: The profiles were learned using three different strategies : Relevance Back-propagation (RB) and Gradient Back-propagation (GB) used in the previous TREC and a new strategy based on Genetic Algorithm (GA). Four runs were submitted, two batch runs based on RB+GB and two routing runs, one based on RB+GB and the other one based on GA.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemJMS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemJMS99,
		author = {Mohand Boughanem and Christine Julien and Josiane Mothe and Chantal Soul{\'{e}}{-}Dupuy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure at trec8: Adhoc, Web, {CLIR} and Filtering tasks},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/irit.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemJMS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Weaver System for Document Retrieval

_Adam L. Berger, John D. Lafferty_

- :fontawesome-solid-user-group: **Participant:** [cmu](./adhoc/participants.md#cmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/weaver.pdf](http://trec.nist.gov/pubs/trec8/papers/weaver.pdf)
- :material-file-search: **Runs:** [weaver1](./adhoc/runs.md#weaver1) | [weaver2](./adhoc/runs.md#weaver2)

??? abstract "Abstract"
	
	This paper introduces Weaver, a probabilistic document retrieval system under development at Carnegie Mellon University, and discusses its performance in the TREC-8 ad hoc evaluation. We begin by describing the architecture and philosophy of the Weaver system, which represents a departure from traditional approaches to retrieval. The central ingredient is a statistical model of how a user might distill or 'translate' a given document into a query. The retrieval-as-translation approach is based on the noisy channel paradigm and statistical language modeling, and has much in common with other recently proposed models (12, 10]. After the initial high-level overview, the bulk of the paper contains a discussion of implementation details and the empirical performance of the Weaver retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BergerL99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BergerL99,
		author = {Adam L. Berger and John D. Lafferty},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Weaver System for Document Retrieval},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/weaver.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BergerL99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-8

_James Allan, James P. Callan, Fangfang Feng, Daniella Malin_

- :fontawesome-solid-user-group: **Participant:** [umass](./adhoc/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf)
- :material-file-search: **Runs:** [INQ601](./adhoc/runs.md#inq601) | [INQ602](./adhoc/runs.md#inq602) | [INQ603](./adhoc/runs.md#inq603) | [INQ604](./adhoc/runs.md#inq604)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in seven of the tracks: ad-hoc, filtering, spoken document retrieval, small web, large web, question and answer, and the query tracks. We spent significant time working on the filtering track, resulting in substantial performance improvement over TREC-7. For all of the other tracks, we used essentially the same system as used in previous years. In the next section, we describe some of the basic processing that was applied across most of the tracks. We then describe the details for each of the tracks and in some cases present some modest analysis of the effectiveness of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCFM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCFM99,
		author = {James Allan and James P. Callan and Fangfang Feng and Daniella Malin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCFM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Surrey Participation in TREC8: Weirdness Indexing  for Logical Document Extrapolation and Retrieval (WILDER)

_Khurshid Ahmad, Lee Gillam, Lena Tostevin_

- :fontawesome-solid-user-group: **Participant:** [city-pliers](./adhoc/participants.md#city-pliers)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/surrey2.pdf](http://trec.nist.gov/pubs/trec8/papers/surrey2.pdf)
- :material-file-search: **Runs:** [plt8ah1](./adhoc/runs.md#plt8ah1) | [plt8ah2](./adhoc/runs.md#plt8ah2) | [plt8ah3](./adhoc/runs.md#plt8ah3) | [plt8ah4](./adhoc/runs.md#plt8ah4) | [plt8ah5](./adhoc/runs.md#plt8ah5)

??? abstract "Abstract"
	
	This paper describes the development of a prototype document retrieval system based on frequency calculations and corpora comparison techniques. The prototype, WILDER, generated simple frequency information based on which calculations of document relevance could be made. The prototype was built to allow the University of Surrey to debut in the U.S. Text Retrieval Competition (TREC). User queries as specified by the TREC organisers were converted into simple word-frequency lists and compared against values for the entire corpus. These relative frequency values indicatively produced document relevance. The application of morphological and empirical heuristics enabled WILDER to produce the ranked frequency lists required.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AhmadGT99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AhmadGT99,
		author = {Khurshid Ahmad and Lee Gillam and Lena Tostevin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {University of Surrey Participation in {TREC8:} Weirdness Indexing for Logical Document Extrapolation and Retrieval {(WILDER)}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/surrey2.pdf},
		timestamp = {Tue, 30 Jun 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AhmadGT99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PLIERS at TREC8

_Andrew MacFarlane, Stephen E. Robertson, Julie A. McCann_

- :fontawesome-solid-user-group: **Participant:** [city-pliers](./adhoc/participants.md#city-pliers)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/pliers8.pdf](http://trec.nist.gov/pubs/trec8/papers/pliers8.pdf)
- :material-file-search: **Runs:** [plt8ah1](./adhoc/runs.md#plt8ah1) | [plt8ah2](./adhoc/runs.md#plt8ah2) | [plt8ah3](./adhoc/runs.md#plt8ah3) | [plt8ah4](./adhoc/runs.md#plt8ah4) | [plt8ah5](./adhoc/runs.md#plt8ah5)

??? abstract "Abstract"
	
	The use of the PLIERS text retrieval system in TREC8 experiments is described. The tracks entered for are: Ad-Hoc, Filtering (Batch and Routing) and the Web Track (Large only). We describe both retrieval efficiency and effectiveness results constant variation. for all these tracks. We also describe some preliminary experiments with BM_25 tuning constant variation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacFarlaneRM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacFarlaneRM99,
		author = {Andrew MacFarlane and Stephen E. Robertson and Julie A. McCann},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{PLIERS} at {TREC8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/pliers8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacFarlaneRM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### High Selectivity and Accuracy with READWARE's Automated System of  Knowledge Organization

_Tom Adi, O. K. Ewell, Patricia Adi_

- :fontawesome-solid-user-group: **Participant:** [miti](./adhoc/participants.md#miti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/READWARE.pdf](http://trec.nist.gov/pubs/trec8/papers/READWARE.pdf)
- :material-file-search: **Runs:** [READWARE2](./adhoc/runs.md#readware2) | [READWARE](./adhoc/runs.md#readware)

??? abstract "Abstract"
	
	READWARE performs a fully automatic text analysis that implements a system of knowledge organization based on knowledge types. A knowledge type is a set of instructions that identifies a set of knowledge elements in any text. Knowledge types include concepts (word sets), topics (an expandable hierarchical scheme of common knowledge types spanning politics, business, health, and so on), probes (investigative knowledge types), issues (knowledge types used in decisionmaking) and document subjects (traditional classification of documents by themes). An MITi analyst used this system to translate TREC topic specifications into highly selective queries (few hits per query) in two adhoc runs with high relevance rates (2019 / 3060 hits in the READWARE run and 2774 / 5785 hits in the READWARE2 run).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AdiEA99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AdiEA99,
		author = {Tom Adi and O. K. Ewell and Patricia Adi},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {High Selectivity and Accuracy with READWARE's Automated System of Knowledge Organization},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/READWARE.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AdiEA99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Filtering 

#### The TREC-8 Filtering Track Final Report

_David A. Hull, Stephen E. Robertson_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/filtering.pdf](http://trec.nist.gov/pubs/trec8/papers/filtering.pdf)
??? abstract "Abstract"
	
	The TREC-8 filtering track measures the ability of systems to build persistent user profiles which successfully separate relevant and non-relevant documents. It consists of three major subtasks: adaptive filtering, batch filtering, and routing. In adaptive filtering, the system begins with only a topic statement and must learn a better profile from on-line feedback. Batch filtering and routing are more traditional machine learning tasks where the system begins with a large sample of evaluated training documents. This report describes the track, presents the evaluation results in graphical format, and provides a general commentary on lessons learned from this year's track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HullR99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HullR99,
		author = {David A. Hull and Stephen E. Robertson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-8} Filtering Track Final Report},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/filtering.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HullR99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Optimization in CLARIT TREC-8 Adaptive Filtering

_ChengXiang Zhai, Peter Jansen, Norbert Roma, Emilia Stoica, David A. Evans_

- :fontawesome-solid-user-group: **Participant:** [claritech](./filtering/participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/CLARIT_Filtering.pdf](http://trec.nist.gov/pubs/trec8/papers/CLARIT_Filtering.pdf)
- :material-file-search: **Runs:** [CL99afL1a](./filtering/runs.md#cl99afl1a) | [CL99afL1b](./filtering/runs.md#cl99afl1b) | [CL99bfL1](./filtering/runs.md#cl99bfl1) | [CL99bfL2](./filtering/runs.md#cl99bfl2) | [CL99afL1c](./filtering/runs.md#cl99afl1c) | [CL99afL1d](./filtering/runs.md#cl99afl1d) | [CL99afL2](./filtering/runs.md#cl99afl2) | [CL99afN1](./filtering/runs.md#cl99afn1)

??? abstract "Abstract"
	
	In this paper, we describe the system and methods used for the CLARITECH entries in the TREC-8 Filtering Track. Our focus of participation was on the adaptive filtering task, as this comes closest to actual applications. In TREC-7, we proposed, evaluated, and proved effective two algorithms for threshold setting and updating— the delivery ratio mechanism, which is used to obtain a profile threshold when no feedback has been received, and beta-gamma regulation, which is used for threshold updating. This year, we explored two ways of improving filtering performance given these our threshold-setting algorithms as a basis by (1) allowing profile-specific anytime updating and (2) optimizing the other filtering system components, in particular, the retrieval/scoring mechanism and the profile vector learning. Our results show that profile-specific frequent updating indeed improves filtering performance. In addition, they suggest that optimizing the scoring function and the term vector learning component independently leads to even further improvement, providing another indication of the effectiveness and robustness of our threshold updating mechanism.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaiJRSE99.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaiJRSE99,
		author = {ChengXiang Zhai and Peter Jansen and Norbert Roma and Emilia Stoica and David A. Evans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Optimization in {CLARIT} {TREC-8} Adaptive Filtering},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/CLARIT\_Filtering.pdf},
		timestamp = {Thu, 05 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhaiJRSE99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Two-Step Feature Selection and Neural Network Classification for the  TREC-8 Routing

_Mathieu Stricker, Frantz Vichot, Gérard Dreyfus, Francis Wolinski_

- :fontawesome-solid-user-group: **Participant:** [icdc](./filtering/participants.md#icdc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/s2n2.pdf](http://trec.nist.gov/pubs/trec8/papers/s2n2.pdf)
- :material-file-search: **Runs:** [S2N2](./filtering/runs.md#s2n2)

??? abstract "Abstract"
	
	At the Caisse des Dépôts et Consignations (CDC), the Agence France-Presse (AFP) news releases are filtered continuously according to the users' interests. Once a user has specified a topic of interest, a filter is customized to fit this user's profile. Until now, these filters would rely on rule-based methods, whose efficiency is proven [Vichot et al., 1999], but which require a large amount of work for each specific filter. This drawback can be avoided by using statistical methods which have the ability to learn from examples of relevant documents. Recently, we have developed a methodology for the AFP corpus. This paper presents its application to the TREC-8 corpus. For the TREC-8 routing, one specific filter is built for each topic. Each filter is a classifier trained to recognize the documents that are relevant to the topic. When presented with a document, each classifier estimates the probability for the document to be relevant to the topic for which it has been trained. Since the procedure for building a filter is topic-independent, the system is fully automatic. Therefore, we describe it for one topic; the procedure is repeated 50 times. By making use of a sample of documents that have previously been evaluated as relevant or not relevant to a particular topic, a term selection is performed, and a neural network is trained. Each document is represented by a vector of frequencies of a list of selected terms. This list depends on the topic to be filtered; it is constructed in two steps. The first step defines the characteristic words used in the relevant documents of the corpus; the second one chooses, among the previous list, the most discriminant ones. The length of the vector is optimized automatically for each topic. At the end of the term selection, a vector of typically 25 words is defined for the topic, so that each document which has to be processed is represented by a vector of term frequencies. This vector is subsequently input to a classifier that is trained from the same sample. After training, the classifier estimates for each document of a test set its probability of being relevant; for submission to TREC, the top 1000 documents are ranked in order of decreasing relevance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrickerVDW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrickerVDW99,
		author = {Mathieu Stricker and Frantz Vichot and G{\'{e}}rard Dreyfus and Francis Wolinski},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Two-Step Feature Selection and Neural Network Classification for the {TREC-8} Routing},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/s2n2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StrickerVDW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SCAI TREC-8 Experiments

_Dong-Ho Shin, Yu-Hwan Kim, Sun Kim, Jae-Hong Eom, Hyung-Joo Shin, Byoung-Tak Zhang_

- :fontawesome-solid-user-group: **Participant:** [seoul](./filtering/participants.md#seoul)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps](http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps)
- :material-file-search: **Runs:** [Scai8Ft](./filtering/runs.md#scai8ft)

??? abstract "Abstract"
	
	This working note reports our experiences with TREC-8 on four tracks: Ad Hoc, Filtering, Web, and QA. The Ad Hoc retrieval engine, SCAIR, has been used for the Web and QA experiments, and the filtering experiments were based on it's own engine. As a second entry to TREC, we focused this year on exploring possibilities of applying machine learning techniques to TREC tasks. The Ad Hoc track employed a cluster-based retrieval method where the scoring function used cluster information extracted from a collection of precompiled documents. Filtering was based on naive Bayes learning supported by an EM algorithm. In the Web track, we compared the performance of using link information to that of not using the information. In the QA track, some passage extraction techniques have been tested using the baseline SCAIR retrieval engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShinKKESZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShinKKESZ99,
		author = {Dong{-}Ho Shin and Yu{-}Hwan Kim and Sun Kim and Jae{-}Hong Eom and Hyung{-}Joo Shin and Byoung{-}Tak Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SCAI} {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShinKKESZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi/Keenbow at TREC-8

_Stephen E. Robertson, Steve Walker_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./filtering/participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/okapi.pdf](http://trec.nist.gov/pubs/trec8/papers/okapi.pdf)
- :material-file-search: **Runs:** [ok8f112](./filtering/runs.md#ok8f112) | [ok8f122](./filtering/runs.md#ok8f122) | [ok8f311](./filtering/runs.md#ok8f311) | [ok8f312](./filtering/runs.md#ok8f312) | [ok8f321](./filtering/runs.md#ok8f321) | [ok8f222](./filtering/runs.md#ok8f222)

??? abstract "Abstract"
	
	Automatic ad hoc and web track: Three ad hoc runs were submitted: long (title, description and narrative), medium (title and description) and short (title only). 'Blind' expansion was used for all runs. The queries from the medium ad hoc run were reused for the small web track submission. Most of the negative expressions were removed from the narrative field of the topic statements, and a new expansion term selection procedure was tried. Adaptive filtering: Methods were similar to those we used in TREC-7. Six runs were submitted. VLC track: Two unexpanded ad hoc runs were submitted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonW99,
		author = {Stephen E. Robertson and Steve Walker},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi/Keenbow at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/okapi.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Experiments at Maryland: CLIR, QA and Routing

_Douglas W. Oard, Jianqiang Wang, Dekang Lin, Ian Soboroff_

- :fontawesome-solid-user-group: **Participant:** [umd](./filtering/participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf](http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf)
- :material-file-search: **Runs:** [umrqz](./filtering/runs.md#umrqz) | [umrlsi](./filtering/runs.md#umrlsi)

??? abstract "Abstract"
	
	The University of Maryland team participated in four aspects of TREC-8: the ad hoc retrieval task, the main task in the cross-language retrieval (CLIR) track, the question answering track, and the routing task in the filtering track. The CLIR method was based on Pirkola's method for Dictionary-based Query Translation, using freely available dictionaries. Broad-coverage parsing and rule-based matching was used for question answering. Routing was performed using Latent Semantic Indexing in profile space.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardWLS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardWLS99,
		author = {Douglas W. Oard and Jianqiang Wang and Dekang Lin and Ian Soboroff},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Experiments at Maryland: CLIR, {QA} and Routing},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OardWLS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DSO at TREC-8: A Hybrid Algorithm for the Routing Task

_Hwee Tou Ng, Huey Ting Ang, Wee Meng Soon_

- :fontawesome-solid-user-group: **Participant:** [dso](./filtering/participants.md#dso)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/DSO.pdf](http://trec.nist.gov/pubs/trec8/papers/DSO.pdf)
- :material-file-search: **Runs:** [dso99rt1](./filtering/runs.md#dso99rt1) | [dso99rt2](./filtering/runs.md#dso99rt2)

??? abstract "Abstract"
	
	In this paper, we describe a new hybrid algorithm that we used for the routing task at TREC-8. The algorithm combines the use of Rocchio's formula for term selection, and an improved variant of the perceptron learning algorithm for tuning the term weights. This algorithm is able to give good performance on TREC-8 test data. We also achieved a slight improvement in average uninterpolated precision by using Dynamic Feedback Optimization (DFO) as another weight tuning algorithm and combining the ranked list generated by DFO with that of perceptron.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NgAS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/NgAS99,
		author = {Hwee Tou Ng and Huey Ting Ang and Wee Meng Soon},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{DSO} at {TREC-8:} {A} Hybrid Algorithm for the Routing Task},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/DSO.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NgAS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PLIERS at TREC8

_Andrew MacFarlane, Stephen E. Robertson, Julie A. McCann_

- :fontawesome-solid-user-group: **Participant:** [city-pliers](./filtering/participants.md#city-pliers)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/pliers8.pdf](http://trec.nist.gov/pubs/trec8/papers/pliers8.pdf)
- :material-file-search: **Runs:** [plt8f1](./filtering/runs.md#plt8f1) | [plt8f2](./filtering/runs.md#plt8f2) | [plt8r1](./filtering/runs.md#plt8r1) | [plt8r2](./filtering/runs.md#plt8r2)

??? abstract "Abstract"
	
	The use of the PLIERS text retrieval system in TREC8 experiments is described. The tracks entered for are: Ad-Hoc, Filtering (Batch and Routing) and the Web Track (Large only). We describe both retrieval efficiency and effectiveness results for all these tracks. We also describe some preliminary experiments with BM_25 tuning constant variation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacFarlaneRM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacFarlaneRM99,
		author = {Andrew MacFarlane and Stephen E. Robertson and Julie A. McCann},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{PLIERS} at {TREC8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/pliers8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacFarlaneRM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Ad-Hoc, Query and Filtering Track Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./filtering/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf](http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf)
- :material-file-search: **Runs:** [pir9LF1](./filtering/runs.md#pir9lf1) | [pir9LF1a](./filtering/runs.md#pir9lf1a) | [pir9LF2](./filtering/runs.md#pir9lf2) | [pir9LF2a](./filtering/runs.md#pir9lf2a) | [pirc9BF1](./filtering/runs.md#pirc9bf1) | [pirc9BF2](./filtering/runs.md#pirc9bf2) | [pirc9R1](./filtering/runs.md#pirc9r1) | [pirc9R2](./filtering/runs.md#pirc9r2)

??? abstract "Abstract"
	
	In TREC-8, we participated in automatic ad-hoc retrieval as well as the query and filtering tracks. The theme of our participation is 'retrieval lists combination', and the technique is applied throughout our experiments to various degree. It is pointed out that our PIRCS system may be considered as a combination of probabilistic retrieval model and a language model approach. For ad-hoc, three types of experiments were done with short, medium and long queries as before. General approach is similar to TREC-7, but combination of retrieval lists from different query types were used to boost effectiveness. For query track, we submitted one short-query set, and performed retrieval for twenty one natural language query vairants. For filtering track, experiments for adaptive, batch filtering, and routing were performed. For adaptive, historical selected document list was used to train profile term weights and dynamically vary retrieval status value (rsv) threshold for deciding document selection during the course of filtering. For batch filtering, Financial Times FT92 data was used to define 6 retrieval profiles whose results were combined based on coefficients trained via a genetic algorithm. Logistic regression transforms rsv's to probabilities. Routing was similarly done with additional training data obtained from non-PT collections and two additional profiles were defined and combined
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGC99,
		author = {K. L. Kwok and Laszlo Grunfeld and M. Chan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Ad-Hoc, Query and Filtering Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Twenty-One at TREC-8: using Language Technology for Information  Retrieval

_Wessel Kraaij, Renée Pohlmann, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [twentyone](./filtering/participants.md#twentyone)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf](http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf)
- :material-file-search: **Runs:** [uttno8lf1](./filtering/runs.md#uttno8lf1) | [uttno8lf2](./filtering/runs.md#uttno8lf2) | [uttno8lf1f](./filtering/runs.md#uttno8lf1f) | [uttno8lf2f](./filtering/runs.md#uttno8lf2f) | [uttno8lf2p](./filtering/runs.md#uttno8lf2p) | [uttno8lf1p](./filtering/runs.md#uttno8lf1p)

??? abstract "Abstract"
	
	This paper describes the official runs of the Twenty-One group for TREC-8. The Twenty-One group participated in the Ad-hoc, CLIR, Adaptive Filtering and SDR tracks. The main focus of our experiments is the development and evaluation of retrieval methods that are motivated by natural language processing techniques. The following new techniques are introduced in this paper. In the Ad-Hoc and CLIR tasks we experimented with automatic sense disambiguation followed by query expansion or translation. We used a combination of thesaurial and corpus information for the disambiguation process. We continued research on CLIR techniques which exploit the target corpus for an implicit disambiguation, by importing the translation probabilities into the probabilistic term-weighting framework. In filtering we extended the the use of language models for document ranking with a relevance feedback algorithm for query term reweighting.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KraaijPH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/KraaijPH99,
		author = {Wessel Kraaij and Ren{\'{e}}e Pohlmann and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Twenty-One at {TREC-8:} using Language Technology for Information Retrieval},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KraaijPH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on the TREC-8 Filtering Track

_Keiichiro Hoashi, Kazunori Matsumoto, Naomi Inoue, Kazuo Hashimoto_

- :fontawesome-solid-user-group: **Participant:** [kdd](./filtering/participants.md#kdd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/kddtrec8.pdf](http://trec.nist.gov/pubs/trec8/papers/kddtrec8.pdf)
- :material-file-search: **Runs:** [kdd8f003](./filtering/runs.md#kdd8f003) | [kdd8f002](./filtering/runs.md#kdd8f002) | [kdd8f001](./filtering/runs.md#kdd8f001)

??? abstract "Abstract"
	
	For this year's TREC, KDD R&D Laboratories focused on the adaptive filtering experiments of the Filtering Track. The main focus of our research was the development and evaluation of the profile updating algorithm. Our profile updating algorithm is based on the query expansion method based on word contribution [1][2]. Given manual feedback, our QE method has achieved high performance in the ad hoc track. Therefore, our hypothesis is that this method should work well in the filtering track. We will describe how we implemented this method to the filtering track, and analyze experiments. Our officially submitted results to TREC were generated from a system with a major bug. The results described in this notebook paper are based on the bug-fixed version of our system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HoashiMIH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HoashiMIH99,
		author = {Keiichiro Hoashi and Kazunori Matsumoto and Naomi Inoue and Kazuo Hashimoto},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments on the {TREC-8} Filtering Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/kddtrec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HoashiMIH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filters, Webs and Answers: The University of Iowa TREC-8 Results

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [iowa](./filtering/participants.md#iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf](http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf)
- :material-file-search: **Runs:** [IOWAF993](./filtering/runs.md#iowaf993) | [IOWAF991](./filtering/runs.md#iowaf991) | [IOWAF992](./filtering/runs.md#iowaf992)

??? abstract "Abstract"
	
	The University of lowa attempted three tracks this year: filtering, question answering, and Web, the latter two new for us this year. All work was based upon that done for TREC-7 [2], with our system adapted for the specifics of the QA and Web tracks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS99,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Filters, Webs and Answers: The University of Iowa {TREC-8} Results},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at trec8: Adhoc, Web, CLIR and Filtering tasks

_Mohand Boughanem, Christine Julien, Josiane Mothe, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [irit](./filtering/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/irit.pdf](http://trec.nist.gov/pubs/trec8/papers/irit.pdf)
- :material-file-search: **Runs:** [Mer8BaLF1](./filtering/runs.md#mer8balf1) | [Mer8BaLF2](./filtering/runs.md#mer8balf2) | [Mer8BaNF1](./filtering/runs.md#mer8banf1) | [Mer8R1](./filtering/runs.md#mer8r1) | [Mer8R2](./filtering/runs.md#mer8r2)

??? abstract "Abstract"
	
	The tests performed for TREC8 were focused on automatic Adhoc, Web, Clir and Filtering (batch and routing) tasks. All the submitted runs were based on the Mercure system. Automatic adhoc : Four runs were submitted. All these runs were based on automatic relevance back-propagation used in the previous TREC, with a slight change for one of these runs (Mer8Adtd3). A strategy based on predicting the relevance of documents using the past relevant documents was tested for this run. More precisely, instead of using the same relevance value for all top retrieved documents, some of them are selected and have their relevance value boosted. Web : Four runs were submitted in this track: 1. content based only using Mercure simple search 2. content tilink, according to Mercure architecture, we consider that document nodes are linked each other by weighted links. The top selected documents resulting from the initial search spread their signals towards the other document nodes. The documents were then sorted according to their activations, the top 1000 documents were submitted. 3. (2) + pseudo-relevance back-propagation method. 4. reranking of the 40 top documents using their links between each others. Cross-language : Three runs were submitted for our first participation in this track. All these runs were based on query translation using an online machine translation . Two of these runs are a comparison between query translation from English to other languages and from French to other languages. Filtering - batch and routing: The profiles were learned using three different strategies : Relevance Back-propagation (RB) and Gradient Back-propagation (GB) used in the previous TREC and a new strategy based on Genetic Algorithm (GA). Four runs were submitted, two batch runs based on RB+GB and two routing runs, one based on RB+GB and the other one based on GA.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemJMS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemJMS99,
		author = {Mohand Boughanem and Christine Julien and Josiane Mothe and Chantal Soul{\'{e}}{-}Dupuy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure at trec8: Adhoc, Web, {CLIR} and Filtering tasks},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/irit.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemJMS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-8

_James Allan, James P. Callan, Fangfang Feng, Daniella Malin_

- :fontawesome-solid-user-group: **Participant:** [umass](./filtering/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf)
- :material-file-search: **Runs:** [INQ610](./filtering/runs.md#inq610) | [INQ611](./filtering/runs.md#inq611) | [INQ612](./filtering/runs.md#inq612) | [INQ613](./filtering/runs.md#inq613)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CI IR) at the University of Massachusetts partic- ipated in seven of the tracks: ad-ho c, ltering, sp oken do cument retrieval, small web, large web, question and answer, and the query tracks. We sp ent signi cant time working on the ltering track, resulting in substantial p erformance improvement over TREC-7. For all of the other tracks, we used essentially the same system as used in previous years. In the next section, we describ e some of the basic pro cessing that was applied across most of the tracks. We then describ e the details for each of the tracks and in some cases present some mo dest analysis of the e ectiveness of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCFM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCFM99,
		author = {James Allan and James P. Callan and Fangfang Feng and Daniella Malin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCFM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Large Web 

#### Overview of the TREC-8 Web Track

_David Hawking, Ellen M. Voorhees, Nick Craswell, Peter Bailey_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/web_overview.pdf](http://trec.nist.gov/pubs/trec8/papers/web_overview.pdf)
??? abstract "Abstract"
	
	The TREC-8 Web Track defined ad hoc retrieval tasks over the 100 gigabyte VLC2 collection (Large Web Task) and a selected 2 gigabyte subset known as WT2g (Small Web Task). Here, the guidelines and resources for both tasks are described and results presented and analysed Performance on the Small Web was strongly correlated with performance on the regular TREC Ad Hoc task. Little benefit was derived from the use of link-based methods, for standard TREC measures on the WT2g collection. The number of inter-server links within WT2g may have been too small or it may be that link-based methods would have worked better with different types of query and/or with different types of relevance judgment. In fact, a small number of link-based runs proved to be much more effective than their content-only baseline at finding documents which linked to documents judged relevant. A variety of issues were investigated by participants in the Large Web Task. One group investigated the use of PageRank scores and found no benefit on standard TREC measures. Engineering improvements by several groups led to either considerable reduction in query processing time or reduction in the amount of hardware necessary to maintain comparable performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingVCB99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingVCB99,
		author = {David Hawking and Ellen M. Voorhees and Nick Craswell and Peter Bailey},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of the {TREC-8} Web Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/web\_overview.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingVCB99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AT&T at TREC-8

_Amit Singhal, Steven P. Abney, Michiel Bacchiani, Michael Collins, Donald Hindle, Fernando C. N. Pereira_

- :fontawesome-solid-user-group: **Participant:** [ATT](./web/participants.md#att)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf](http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf)
- :material-file-search: **Runs:** [att99wtdc](./web/runs.md#att99wtdc) | [att99wtde](./web/runs.md#att99wtde)

??? abstract "Abstract"
	
	In 1999, AT&T participated in the ad-hoc task and the Question Answering (QA), Spoken Document Retrieval (SDR), and Web tracks. Most of our effort for TREC-8 focused on the QA and SDR tracks. Results from SDR track show that our document expansion techniques, presented in [8, 9], are very effective for speech retrieval. The results for question answering are also encouraging. Our system designed in a relatively short period for this task can find the correct answer for about 45% of the user questions. This is specially good given the fact that our system extracts only a short phrase as an answer.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinghalABCHP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinghalABCHP99,
		author = {Amit Singhal and Steven P. Abney and Michiel Bacchiani and Michael Collins and Donald Hindle and Fernando C. N. Pereira},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {AT{\&}T at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SinghalABCHP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SCAI TREC-8 Experiments

_Dong-Ho Shin, Yu-Hwan Kim, Sun Kim, Jae-Hong Eom, Hyung-Joo Shin, Byoung-Tak Zhang_

- :fontawesome-solid-user-group: **Participant:** [seoul](./web/participants.md#seoul)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps](http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps)
- :material-file-search: **Runs:** [Scai8Web1](./web/runs.md#scai8web1) | [Scai8Web2](./web/runs.md#scai8web2)

??? abstract "Abstract"
	
	This working note reports our experiences with TREC-8 on four tracks: Ad Hoc, Filtering, Web, and QA. The Ad Hoc retrieval engine, SCAIR, has been used for the Web and QA experiments, and the filtering experiments were based on it's own engine. As a second entry to TREC, we focused this year on exploring possibilities of applying machine learning techniques to TREC tasks. The Ad Hoc track employed a cluster-based retrieval method where the scoring function used cluster information extracted from a collection of precompiled documents. Filtering was based on naive Bayes learning supported by an EM algorithm. In the Web track, we compared the performance of using link information to that of not using the information. In the QA track, some passage extraction techniques have been tested using the baseline SCAIR retrieval engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShinKKESZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShinKKESZ99,
		author = {Dong{-}Ho Shin and Yu{-}Hwan Kim and Sun Kim and Jae{-}Hong Eom and Hyung{-}Joo Shin and Byoung{-}Tak Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SCAI} {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShinKKESZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC-8 Experiment: Searching on the Web and in Distributed  Collections

_Jacques Savoy, Justin Picard_

- :fontawesome-solid-user-group: **Participant:** [savoy](./web/participants.md#savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/neuchatel2.pdf](http://trec.nist.gov/pubs/trec8/papers/neuchatel2.pdf)
- :material-file-search: **Runs:** [UniNEWCt](./web/runs.md#uninewct) | [UniNEW2Ct](./web/runs.md#uninew2ct) | [UniNEWLink](./web/runs.md#uninewlink) | [UniNEW2Link](./web/runs.md#uninew2link)

??? abstract "Abstract"
	
	The Internet paradigm permits information searches to be made across wide-area networks where information is contained in web pages and/or whole document collections such as digital libraries. These new distributed information environments reveal new and challenging problems for the IR community. Consequently, in this TREC experiment we investigated two questions related to information searches on the web or in digital libraries: (1) an analysis of the impact of hyperlinks in improving retrieval performance, and (2) a study of techniques useful in selecting more appropriate text databases (database selection problem encountered when faced with multiple collections), including an evaluation of certain merging strategies effective in producing, single, ranked lists to be presented to the user (database merging problem).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavoyP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavoyP99,
		author = {Jacques Savoy and Justin Picard},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Report on the {TREC-8} Experiment: Searching on the Web and in Distributed Collections},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/neuchatel2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SavoyP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi/Keenbow at TREC-8

_Stephen E. Robertson, Steve Walker_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./web/participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/okapi.pdf](http://trec.nist.gov/pubs/trec8/papers/okapi.pdf)
- :material-file-search: **Runs:** [ok8wmx](./web/runs.md#ok8wmx)

??? abstract "Abstract"
	
	Automatic ad hoc and web track: Three ad hoc runs were submitted: long (title, description and narrative), medium (title and description) and short (title only). 'Blind' expansion was used for all runs. The queries from the medium ad hoc run were reused for the small web track submission. Most of the negative expressions were removed from the narrative field of the topic statements, and a new expansion term selection procedure was tried. Adaptive filtering: Methods were similar to those we used in TREC-7. Six runs were submitted. VLC track: Two unexpanded ad hoc runs were submitted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonW99,
		author = {Stephen E. Robertson and Steve Walker},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi/Keenbow at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/okapi.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Moving More Quickly toward Full Term Relations in Information Space

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [Newby](./web/participants.md#newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/newby-trec99-proceedings.pdf](http://trec.nist.gov/pubs/trec8/papers/newby-trec99-proceedings.pdf)
- :material-file-search: **Runs:** [isw25](./web/runs.md#isw25) | [isw50](./web/runs.md#isw50) | [isw25t](./web/runs.md#isw25t) | [isw50t](./web/runs.md#isw50t)

??? abstract "Abstract"
	
	This paper describes the ISpace retrieval system's involvement in TREC8. The main goal for this year's work was to speed up document indexing and query processing compared to previous years. This goal was achieved, but retrieval performance was not as good as for TREC7. System details for the AdHoc task, small Web task, and large Web (VLC) task are presented. The AdHoc task emphasized query expansion, while the large Web track emphasized rapid indexing and retrieval. The paper describes an implementation of a multidimensional tree structure for retrieval from information space based on the kd-tree. The larger setting for ISpace, the TeraScale Retrieval project, is summarized. A concluding section describes plans for ISpace.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Newby99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Newby99,
		author = {Gregory B. Newby},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Moving More Quickly toward Full Term Relations in Information Space},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/newby-trec99-proceedings.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Newby99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fujitsu Laboratories TREC8 Report - Ad hoc, Small Web, and Large  Web Track

_Isao Namba, Nobuyuki Igata_

- :fontawesome-solid-user-group: **Participant:** [fujitsu](./web/participants.md#fujitsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/flab8_proceedings_letter.pdf](http://trec.nist.gov/pubs/trec8/papers/flab8_proceedings_letter.pdf)
- :material-file-search: **Runs:** [Flab8wtdN](./web/runs.md#flab8wtdn) | [Flab8wtdnN](./web/runs.md#flab8wtdnn)

??? abstract "Abstract"
	
	This year a Fujitsu Laboratory team participated in three tracks that is ad hoc, small web track, and large web track. As basic techiniques, we compared four popular stemmers, and we made simple removing stop pattern techniques for TREC queries. For the ad hoc task, and small web track, we used the same techniques. We experimented with area weighting, co-occurence boosting, bi-gram utliza-tion, and reranking by bi-gram extraction from pilot search. The effect of blind application with those te-chiniques is rather limited, or even uncertain in the TREC8 experiment. What we can say from TREC8 result is that blind application of co-occurence boosting and area weighting may be effective for the small web track. They requerie query dependent application. In the large web track, our main interest is ef-ficiency, that is how much resources are required to process 100GB of web text and 10000 real web queries in practical time. Using a statistical based language type checker, we can eliminate 23% of non-English text. This leads to speeding up a indexing and reducing the index size. The search speed for an inverted file is CPU intensive if the target machine has main memory in excess of 10-25% of the index size. So with simple, but effective index compression methods, the throughput of query processing is about 0.54-1.1 query/second even by a single 300MHz Ultra-sparc processor.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NambaI99.bib) "
	```
	@inproceedings{DBLP:conf/trec/NambaI99,
		author = {Isao Namba and Nobuyuki Igata},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fujitsu Laboratories {TREC8} Report - Ad hoc, Small Web, and Large Web Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/flab8\_proceedings\_letter.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NambaI99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC-8: Improving Baseline Precision

_M. Catherine McCabe, David O. Holmes, Kenneth L. Alford, Abdur Chowdhury, David A. Grossman, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [iit](./web/participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/iit99pr.pdf](http://trec.nist.gov/pubs/trec8/papers/iit99pr.pdf)
- :material-file-search: **Runs:** [iit99wt1](./web/runs.md#iit99wt1) | [iit99wt2](./web/runs.md#iit99wt2) | [iit99wt3](./web/runs.md#iit99wt3)

??? abstract "Abstract"
	
	In TREC-8, we participated in the automatic and manual tracks for category A as well as the small web track. This year, we focussed on improving our baseline and then introduced some experimental improvements. Our automatic runs used relevance feedback with a high-precision first pass to select terms and then a high-recall final pass. For manual runs, we used predefined concept lists focussing on phrases and proper nouns in the query. In the small web-track, we submitted one content-only run and two link-plus-content runs. We continued to use the relational model with unchanged SQL for retrieval. Our results show some promise for the use of automatic concepts, expansion within concepts and a high-precision first pass for relevance feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCabeHACGF99.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCabeHACGF99,
		author = {M. Catherine McCabe and David O. Holmes and Kenneth L. Alford and Abdur Chowdhury and David A. Grossman and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{IIT} at {TREC-8:} Improving Baseline Precision},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/iit99pr.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCabeHACGF99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ACSys TREC-8 Experiments

_David Hawking, Peter Bailey, Nick Craswell_

- :fontawesome-solid-user-group: **Participant:** [ACSys](./web/participants.md#acsys)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/acsys.pdf](http://trec.nist.gov/pubs/trec8/papers/acsys.pdf)
- :material-file-search: **Runs:** [acsys8wm](./web/runs.md#acsys8wm) | [acsys8wmp](./web/runs.md#acsys8wmp) | [acsys8wmq](./web/runs.md#acsys8wmq) | [acsys8wmr](./web/runs.md#acsys8wmr)

??? abstract "Abstract"
	
	Experiments relating to TREC-8 Ad Hoc, Web Track (Large and Small) and Query Track tasks are described and results reported. Due to time constraints, only minimal effort was put into Ad Hoc and Query Track participation. In the Web Track, Google-style PageRanks were calculated for all 18.5 million pages in the VLC2 collection and for the 0.25 million pages in the WT2g collection. Various combinations of content score and PageRank produced no benefit for TREC style ad hoc retrieval. A major goal in the Web Track was to make engineering improvements to permit indexing of the 100 gigabyte collection and subsequent query processing using a single PC. A secondary goal was to achieve last year's performance (obtained with eight DEC Alphas) with less recourse to effectiveness-harming optimisations. The main goal was achieved and indexing times are comparable to last year's. However, effectiveness results were worse relative to last year and query processing times were approximately double.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingBC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingBC99,
		author = {David Hawking and Peter Bailey and Nick Craswell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ACSys {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/acsys.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingBC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Connectivity Analysis Approach to Increasing Precision in Retrieval  From Hyperlinked Documents

_Cathal Gurrin, Alan F. Smeaton_

- :fontawesome-solid-user-group: **Participant:** [dublin](./web/participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/dcuTREC8paper.pdf](http://trec.nist.gov/pubs/trec8/papers/dcuTREC8paper.pdf)
- :material-file-search: **Runs:** [DCU99C01](./web/runs.md#dcu99c01) | [DCU99L02](./web/runs.md#dcu99l02) | [DCU99L01](./web/runs.md#dcu99l01)

??? abstract "Abstract"
	
	Within the last few years very little as been made of the usefulness of Connectivity Analysis to Information Retrieval on the WWW. This document discusses hyperlinks on the WWW and our experiments on the exploitation of the immediate neighbourhood of a web page in an effort to improve search results. In order to test the hypothesis that Connectivity Analysis can increase precision in the top ranked documents from a set of relevant documents, we developed a software application to generate and re-rank a query relevant subset of the WT2g Dataset. We discuss our software in depth and the problems that we encountered during development. Our experiments are based on implementing a number of re-ranking formulae, each of which tests the usefulness of different approaches to re-ranking a set of relevant pages, ranging from basic context analysis (inLink ranking) to combined content and context analysis approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GurrinS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/GurrinS99,
		author = {Cathal Gurrin and Alan F. Smeaton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A Connectivity Analysis Approach to Increasing Precision in Retrieval From Hyperlinked Documents},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/dcuTREC8paper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GurrinS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The RMIT/CSIRO Ad Hoc, Q&A, Web, Interactive, and Speech Experiments  at TREC 8

_Michael Fuller, Marcin Kaszkiel, Sam Kimberley, Corinna Ng, Ross Wilkinson, Mingfang Wu, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [rmit](./web/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf](http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf)
- :material-file-search: **Runs:** [mds08w1](./web/runs.md#mds08w1) | [mds08w2](./web/runs.md#mds08w2) | [mds08w3](./web/runs.md#mds08w3)

??? abstract "Abstract"
	
	The MDS group participated in the small web track, submitting three runs; a content-only run, mds08w1, and two content-and-link runs, mds08w2 and mds08w3. Our objective in participating in this track was twofold. Firstly, to determine whether simple manipulation of linking information would enable effective re-ranking of documents within a result set. Secondly, to examine the effectiveness of content-only retrieval on web data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FullerKKNWWZ99,
		author = {Michael Fuller and Marcin Kaszkiel and Sam Kimberley and Corinna Ng and Ross Wilkinson and Mingfang Wu and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {RMIT/CSIRO} Ad Hoc, Q{\&}A, Web, Interactive, and Speech Experiments at {TREC} 8},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filters, Webs and Answers: The University of Iowa TREC-8 Results

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [iowa](./web/participants.md#iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf](http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf)
- :material-file-search: **Runs:** [uiowaweb1](./web/runs.md#uiowaweb1) | [uiowaweb2](./web/runs.md#uiowaweb2)

??? abstract "Abstract"
	
	The University of Iowa attempted three tracks this year: filtering, question answering, and Web, the latter two new for us this year. All work was based upon that done for TREC-7 [21, with our system adapted for the specifics of the QA and Web tracks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS99,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Filters, Webs and Answers: The University of Iowa {TREC-8} Results},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Early DiscoWeb Prototype at TREC8

_Brian D. Davison, Apostolos Gerasoulis, Konstantinos Kleisouris, Yingfang Lu, Hyun-ju Seo, Junyu Tian, Song Wang, Wei Wang, Baohua Wu_

- :fontawesome-solid-user-group: **Participant:** [rutgers-davison](./web/participants.md#rutgers-davison)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/discoweb.pdf](http://trec.nist.gov/pubs/trec8/papers/discoweb.pdf)
- :material-file-search: **Runs:** [disco2](./web/runs.md#disco2) | [disco3](./web/runs.md#disco3)

??? abstract "Abstract"
	
	Recently the notion of popularity and its generalizations have been investigated as a possible alternative approach to text only analysis to rank web pages in search engines (e.g. Kle98, BP98, CDR+98, CDDG+98, BH98, HHMN99] among others). We have built a research prototype that incorporates many link analysis algorithms from the literature and also new algorithms to investigate the impact of the popularity on the ranking of the search engines (DGK+ 99]. Our goal in the TREC& competition was to investigate the quality of the results using the TREC data and in particular the large web track. Unfortunately we did not have the needed hardware in time to generate results for the large web track. We only participated in the Small Web Track (Text Only and Text and Link Analysis). However, our system was designed for large datasets and the quality of the TREC8 results are not representative of the system. More recently we have experimented with larger datasets and we have come to the conclusion that link analysis can significantly increase the quality of the ranking of search engines, a conclusion that is shared by many others in the literature (BP98, PBMW98, Kle98, CDR+98, CDDG+98, CDG+ 99]. We will report these new results in a future publication.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DavisonGKLSTWWW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/DavisonGKLSTWWW99,
		author = {Brian D. Davison and Apostolos Gerasoulis and Konstantinos Kleisouris and Yingfang Lu and Hyun{-}ju Seo and Junyu Tian and Song Wang and Wei Wang and Baohua Wu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {An Early DiscoWeb Prototype at {TREC8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/discoweb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DavisonGKLSTWWW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fast Automatic Passage Ranking (MultiText Experiments for TREC-8)

_Gordon V. Cormack, Charles L. A. Clarke, D. I. E. Kisman, Christopher R. Palmer_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./web/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf](http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf)
- :material-file-search: **Runs:** [uwmt8w0](./web/runs.md#uwmt8w0)

??? abstract "Abstract"
	
	TREC-8 represents the fifth year that the MultiText project has participated in TREC [2, 1, 4, 5]. The MultiText project develops and prototypes scalable technologies for parallel information retrieval systems implemented on networks of workstations. Research issues are addressed in the context of this parallel architecture. Issues of concern to the MultiText Project include data distribution, load balancing, fast update, fault tolerance, document structure, relevance ranking, and user interaction. The MultiText system incorporates a unique technique for arbitrary passage retrieval. Since our initial participation in TREC-4 our TREC work has explored variants of this technique. For TREC-8 we focused our efforts on the Web track. In addition, we submitted runs for the Adhoc task (title and title +description) and a run for the Question Answering task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackCKP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackCKP99,
		author = {Gordon V. Cormack and Charles L. A. Clarke and D. I. E. Kisman and Christopher R. Palmer},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fast Automatic Passage Ranking (MultiText Experiments for {TREC-8)}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackCKP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at trec8: Adhoc, Web, CLIR and Filtering tasks

_Mohand Boughanem, Christine Julien, Josiane Mothe, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [irit](./web/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/irit.pdf](http://trec.nist.gov/pubs/trec8/papers/irit.pdf)
- :material-file-search: **Runs:** [Mer8Wctd](./web/runs.md#mer8wctd) | [Mer8Wci1](./web/runs.md#mer8wci1) | [Mer8Wci2](./web/runs.md#mer8wci2) | [Mer8Wci3](./web/runs.md#mer8wci3)

??? abstract "Abstract"
	
	The tests performed for TREC8 were focused on automatic Adhoc, Web, Clir and Filtering (batch and routing) tasks. All the submitted runs were based on the Mercure system. Automatic adhoc : Four runs were submitted. All these runs were based on automatic relevance back-propagation used in the previous TREC, with a slight change for one of these runs (Mer8Adtd3). A strategy based on predicting the relevance of documents using the past relevant documents was tested for this run. More precisely, instead of using the same relevance value for all top retrieved documents, some of them are selected and have their relevance value boosted. Web : Four runs were submitted in this track: 1. content based only using Mercure simple search 2. content tilink, according to Mercure architecture, we consider that document nodes are linked each other by weighted links. The top selected documents resulting from the initial search spread their signals towards the other document nodes. The documents were then sorted according to their activations, the top 1000 documents were submitted. 3. (2) + pseudo-relevance back-propagation method. 4. reranking of the 40 top documents using their links between each others. Cross-language : Three runs were submitted for our first participation in this track. All these runs were based on query translation using an online machine translation . Two of these runs are a comparison between query translation from English to other languages and from French to other languages. Filtering - batch and routing: The profiles were learned using three different strategies : Relevance Back-propagation (RB) and Gradient Back-propagation (GB) used in the previous TREC and a new strategy based on Genetic Algorithm (GA). Four runs were submitted, two batch runs based on RB+GB and two routing runs, one based on RB+GB and the other one based on GA.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemJMS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemJMS99,
		author = {Mohand Boughanem and Christine Julien and Josiane Mothe and Chantal Soul{\'{e}}{-}Dupuy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure at trec8: Adhoc, Web, {CLIR} and Filtering tasks},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/irit.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemJMS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLARIT TREC-8 Experiments in Searching Web Data

_Jeffrey Bennett, Xiang Tong, David A. Evans_

- :fontawesome-solid-user-group: **Participant:** [claritech](./web/participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/CLARIT_Web.pdf](http://trec.nist.gov/pubs/trec8/papers/CLARIT_Web.pdf)
- :material-file-search: **Runs:** [CL99WebH](./web/runs.md#cl99webh) | [CL99WebM](./web/runs.md#cl99webm)

??? abstract "Abstract"
	
	CLARITECH submitted two baseline content-only runs and completed two additional content+link runs in the TREC-8 Web Track. These represent our first serious attempt to deal with Web data, and our first automatic runs in several years. The first question was whether CLARIT would perform as well on Web data as on more traditional text. We found that, with extensive pre-processing of the raw data prior to indexing, the automatic retrieval system actually performed better on Web data than on Ad Hoc data. For the link runs, we implemented a version of the HITS algorithm [Kleinberg 1997], originally developed at IBM. Our version optimized HITS for the CLARIT environment, but also reflected some constraints imposed by limited resources. Unable to develop and sufficiently test our own matrix-processing library in time, we used a commercial product for the number crunching. Performance on the link runs was poor, but failure analysis suggests many ways to improve it.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BennettTE99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BennettTE99,
		author = {Jeffrey Bennett and Xiang Tong and David A. Evans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CLARIT} {TREC-8} Experiments in Searching Web Data},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/CLARIT\_Web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BennettTE99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-8

_James Allan, James P. Callan, Fangfang Feng, Daniella Malin_

- :fontawesome-solid-user-group: **Participant:** [umass](./web/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf)
- :material-file-search: **Runs:** [INQ620](./web/runs.md#inq620)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in seven of the tracks: ad-hoc, filtering, spoken document retrieval, small web, large web, question and answer, and the query tracks. We spent signicant time working on the filtering track, resulting in substantial performance improvement over TREC-7. For all of the other tracks, we used essentially the same system as used in previous years. In the next section, we describe some of the basic processing that was applied across most of the tracks. We then describe the details for each of the tracks and in some cases present some modest analysis of the effectiveness of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCFM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCFM99,
		author = {James Allan and James P. Callan and Fangfang Feng and Daniella Malin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCFM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Query 

#### The TREC-8 Query Track

_Chris Buckley, Janet A. Walz_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/qtrack.pdf](http://trec.nist.gov/pubs/trec8/papers/qtrack.pdf)
??? abstract "Abstract"
	
	The Query Track in TREC-8 is a bit different from all the other tracks. It is a cooperative effort among the participating groups to look at the issue of 'query variability'. The evaluation averages presented in a typical system evaluation task, such as the TREC Ad-Hoc Task, conceal a tremendous variability of system performance across topics/queries. No system can possibly perform equally well on all topics: some information needs (expressed by topics) are harder than others. But what is quite surprising, especially to people just starting to look at IR, is the large variability in system performance across topics as compared to other systems. In a typical TREC task, no system is the best for all the topics in the task. It is extremely rare for any system to be above average for all the topics. Instead, the best system is normally above average for most of the topics, and best for maybe 5%-10% of the topics. It very often happens that quite below-average systems are also best for 5%-10% of the topics, but do poorly on the other topics. The Average Precision Histograms presented on the TREC evaluation result pages are an attempt to show what is happening at the individual topic level. This large topic/query variability presents a great opportunity for improving system performance. If we can understand why some systems do well on some queries but poorly on others, then we can start introducing query dependent processing to improve results on those poor performance queries. Unfortunately, we just don't have enough information from the results of a typical TREC task to really understand what is happening. The results on 50 to 150 queries are just not enough to draw any conclusions. The Query Track at TREC is an attempt to gather enough information from a large number of systems on a large number of queries to be able to start understanding query variability.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyW99,
		author = {Chris Buckley and Janet A. Walz},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-8} Query Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/qtrack.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Ad-Hoc, Query and Filtering Track Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./query/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf](http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf)
- :material-file-search: **Runs:** [pirINQ1a](./query/runs.md#pirinq1a) | [pirINQ1b](./query/runs.md#pirinq1b) | [pirINQ1c](./query/runs.md#pirinq1c) | [pirINQ1d](./query/runs.md#pirinq1d) | [pirINQ1e](./query/runs.md#pirinq1e) | [pirINQ2b](./query/runs.md#pirinq2b) | [pirINQ2c](./query/runs.md#pirinq2c) | [pirINQ2a](./query/runs.md#pirinq2a) | [pirINQ2d](./query/runs.md#pirinq2d) | [pirINQ2e](./query/runs.md#pirinq2e) | [pirINQ3a](./query/runs.md#pirinq3a) | [pirINQ3b](./query/runs.md#pirinq3b) | [pirINQ3c](./query/runs.md#pirinq3c) | [pirINQ3d](./query/runs.md#pirinq3d) | [pirINQ3e](./query/runs.md#pirinq3e) | [pirSab1a](./query/runs.md#pirsab1a) | [pirSab1c](./query/runs.md#pirsab1c) | [pirSab1b](./query/runs.md#pirsab1b) | [pirpir1a](./query/runs.md#pirpir1a) | [piracs1a](./query/runs.md#piracs1a) | [pirSab3a](./query/runs.md#pirsab3a)

??? abstract "Abstract"
	
	In TREC-8, we participated in automatic ad-hoc retrieval as well as the query and filtering tracks. The theme of our participation is 'retrieval lists combination', and the technique is applied throughout our experiments to various degree. It is pointed out that our PIRCS system may be considered as a combination of probabilistic retrieval model and a language model approach. For ad-hoc, three types of experiments were done with short, medium and long queries as before. General approach is similar to TREC-7, but combination of retrieval lists from different query types were used to boost effectiveness. For query track, we submitted one short-query set, and performed retrieval for twenty one natural language query vairants. For filtering track, experiments for adaptive, batch filtering, and routing were performed. For adaptive, historical selected document list was used to train profile term weights and dynamically vary retrieval status value (rsv) threshold for deciding document selection during the course of filtering. For batch filtering, Financial Times FT92 data was used to define 6 retrieval profiles whose results were combined based on coefficients trained via a genetic algorithm. Logistic regression transforms rsv's to probabilities. Routing was similarly done with additional training data obtained from non-FT collections and two additional profiles were defined and combined
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGC99,
		author = {K. L. Kwok and Laszlo Grunfeld and M. Chan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Ad-Hoc, Query and Filtering Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ACSys TREC-8 Experiments

_David Hawking, Peter Bailey, Nick Craswell_

- :fontawesome-solid-user-group: **Participant:** [ACSys](./query/participants.md#acsys)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/acsys.pdf](http://trec.nist.gov/pubs/trec8/papers/acsys.pdf)
- :material-file-search: **Runs:** [acsAPL5b](./query/runs.md#acsapl5b) | [acsINQ1a](./query/runs.md#acsinq1a) | [acsAPL5a](./query/runs.md#acsapl5a) | [acsINQ1b](./query/runs.md#acsinq1b) | [acsINQ1c](./query/runs.md#acsinq1c) | [acsINQ1e](./query/runs.md#acsinq1e) | [acsINQ2a](./query/runs.md#acsinq2a) | [acsINQ2b](./query/runs.md#acsinq2b) | [acsINQ2e](./query/runs.md#acsinq2e) | [acsINQ2c](./query/runs.md#acsinq2c) | [acsINQ3a](./query/runs.md#acsinq3a) | [acsINQ3b](./query/runs.md#acsinq3b) | [acsINQ3c](./query/runs.md#acsinq3c) | [acsINQ3e](./query/runs.md#acsinq3e) | [acsSab1a](./query/runs.md#acssab1a) | [acsSab1c](./query/runs.md#acssab1c) | [acsSab1b](./query/runs.md#acssab1b) | [acspir1a](./query/runs.md#acspir1a) | [acsSab3a](./query/runs.md#acssab3a) | [acsINQ1d](./query/runs.md#acsinq1d) | [acsINQ2d](./query/runs.md#acsinq2d) | [acsINQ3d](./query/runs.md#acsinq3d) | [acsacs1a](./query/runs.md#acsacs1a)

??? abstract "Abstract"
	
	Experiments relating to TREC-8 Ad Hoc, Web Track (Large and Small) and Query Track tasks are described and results reported. Due to time constraints, only minimal effort was put into Ad Hoc and Query Track participation. In the Web Track, Google-style PageRanks were calculated for all 18.5 million pages in the VLC2 collection and for the 0.25 million pages in the WT2g collection. Various combinations of content score and PageRank produced no benefit for TREC style ad hoc retrieval. A major goal in the Web Track was to make engineering improvements to permit indexing of the 100 gigabyte collection and subsequent query processing using a single PC. A secondary goal was to achieve last year's performance (obtained with eight DEC Alphas) with less recourse to effectiveness-harming optimisations. The main goal was achieved and indexing times are comparable to last year's. However, effectiveness results were worse relative to last year and query processing times were approximately double.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingBC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingBC99,
		author = {David Hawking and Peter Bailey and Nick Craswell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ACSys {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/acsys.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingBC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SMART in TREC 8

_Chris Buckley, Janet A. Walz_

- :fontawesome-solid-user-group: **Participant:** [cornell](./query/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/sabir8.pdf](http://trec.nist.gov/pubs/trec8/papers/sabir8.pdf)
- :material-file-search: **Runs:** [SabaINQ1a](./query/runs.md#sabainq1a) | [Sab5APL5a](./query/runs.md#sab5apl5a) | [Sab5APL5b](./query/runs.md#sab5apl5b) | [SabaINQ1b](./query/runs.md#sabainq1b) | [SabaINQ1c](./query/runs.md#sabainq1c) | [SabaINQ1d](./query/runs.md#sabainq1d) | [SabaINQ1e](./query/runs.md#sabainq1e) | [SabaINQ2a](./query/runs.md#sabainq2a) | [SabaINQ2b](./query/runs.md#sabainq2b) | [SabaINQ2c](./query/runs.md#sabainq2c) | [SabaINQ2d](./query/runs.md#sabainq2d) | [SabaINQ2e](./query/runs.md#sabainq2e) | [SabaINQ3a](./query/runs.md#sabainq3a) | [SabaINQ3b](./query/runs.md#sabainq3b) | [SabaINQ3c](./query/runs.md#sabainq3c) | [SabaINQ3e](./query/runs.md#sabainq3e) | [SabaINQ3d](./query/runs.md#sabainq3d) | [SabaSab1a](./query/runs.md#sabasab1a) | [SabaSab1b](./query/runs.md#sabasab1b) | [SabaSab1c](./query/runs.md#sabasab1c) | [SabaSab3a](./query/runs.md#sabasab3a) | [Sabaacs1a](./query/runs.md#sabaacs1a) | [Sabapir1a](./query/runs.md#sabapir1a) | [SabeINQ1a](./query/runs.md#sabeinq1a) | [SabeINQ1b](./query/runs.md#sabeinq1b) | [SabeINQ1c](./query/runs.md#sabeinq1c) | [SabeINQ1d](./query/runs.md#sabeinq1d) | [SabeINQ1e](./query/runs.md#sabeinq1e) | [SabeINQ2a](./query/runs.md#sabeinq2a) | [SabeINQ2b](./query/runs.md#sabeinq2b) | [SabeINQ2c](./query/runs.md#sabeinq2c) | [SabeINQ2d](./query/runs.md#sabeinq2d) | [SabeINQ2e](./query/runs.md#sabeinq2e) | [SabeINQ3a](./query/runs.md#sabeinq3a) | [SabeINQ3b](./query/runs.md#sabeinq3b) | [SabeINQ3c](./query/runs.md#sabeinq3c) | [SabeINQ3d](./query/runs.md#sabeinq3d) | [SabeINQ3e](./query/runs.md#sabeinq3e) | [SabeSab1a](./query/runs.md#sabesab1a) | [SabeSab1b](./query/runs.md#sabesab1b) | [SabeSab1c](./query/runs.md#sabesab1c) | [SabeSab3a](./query/runs.md#sabesab3a) | [Sabeacs1a](./query/runs.md#sabeacs1a) | [Sabepir1a](./query/runs.md#sabepir1a) | [SabmINQ1a](./query/runs.md#sabminq1a) | [SabmINQ1b](./query/runs.md#sabminq1b) | [SabmINQ1c](./query/runs.md#sabminq1c) | [SabmINQ1d](./query/runs.md#sabminq1d) | [SabmINQ1e](./query/runs.md#sabminq1e) | [SabmINQ2a](./query/runs.md#sabminq2a) | [SabmINQ2b](./query/runs.md#sabminq2b) | [SabmINQ2c](./query/runs.md#sabminq2c) | [SabmINQ2d](./query/runs.md#sabminq2d) | [SabmINQ2e](./query/runs.md#sabminq2e) | [SabmINQ3a](./query/runs.md#sabminq3a) | [SabmINQ3b](./query/runs.md#sabminq3b) | [SabmINQ3c](./query/runs.md#sabminq3c) | [SabmINQ3d](./query/runs.md#sabminq3d) | [SabmINQ3e](./query/runs.md#sabminq3e) | [SabmSab1a](./query/runs.md#sabmsab1a) | [SabmSab1b](./query/runs.md#sabmsab1b) | [SabmSab1c](./query/runs.md#sabmsab1c) | [SabmSab3a](./query/runs.md#sabmsab3a) | [Sabmacs1a](./query/runs.md#sabmacs1a) | [Sabmpir1a](./query/runs.md#sabmpir1a) | [SabmAPL5b](./query/runs.md#sabmapl5b) | [SabeAPL5b](./query/runs.md#sabeapl5b) | [SabeAPL5a](./query/runs.md#sabeapl5a) | [SabmAPL5a](./query/runs.md#sabmapl5a)

??? abstract "Abstract"
	
	This year was a light year for the Smart Information Retrieval Project at SabIR Research and Cornell. We officially participated in only the Ad-hoc Task and the Query Track. In the Ad-hoc Task, we made minor modifications to our document weighting schemes to emphasize high-precision searches on shorter queries. This proved only mildly successful; the top relevant document was retrieved higher, but the rest of the retrieval tended to be hurt. Our Query Track runs are described here, but the much more interesting analysis of these runs is described in the Query Track Overview.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyW99a.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyW99a,
		author = {Chris Buckley and Janet A. Walz},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SMART} in {TREC} 8},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/sabir8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyW99a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-8

_James Allan, James P. Callan, Fangfang Feng, Daniella Malin_

- :fontawesome-solid-user-group: **Participant:** [umass](./query/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf)
- :material-file-search: **Runs:** [INQaINQ1a](./query/runs.md#inqainq1a) | [INQaINQ1b](./query/runs.md#inqainq1b) | [INQaINQ1e](./query/runs.md#inqainq1e) | [INQaINQ1c](./query/runs.md#inqainq1c) | [INQaINQ2b](./query/runs.md#inqainq2b) | [INQaINQ2a](./query/runs.md#inqainq2a) | [INQaINQ2c](./query/runs.md#inqainq2c) | [INQaINQ2d](./query/runs.md#inqainq2d) | [INQaINQ2e](./query/runs.md#inqainq2e) | [INQaINQ3a](./query/runs.md#inqainq3a) | [INQaSab1b](./query/runs.md#inqasab1b) | [INQaINQ3c](./query/runs.md#inqainq3c) | [INQaSab1a](./query/runs.md#inqasab1a) | [INQaINQ3e](./query/runs.md#inqainq3e) | [INQaSab3a](./query/runs.md#inqasab3a) | [INQaINQ1d](./query/runs.md#inqainq1d) | [INQaSab1c](./query/runs.md#inqasab1c) | [INQaacs1a](./query/runs.md#inqaacs1a) | [INQaINQ3b](./query/runs.md#inqainq3b) | [INQeINQ1a](./query/runs.md#inqeinq1a) | [INQapir1a](./query/runs.md#inqapir1a) | [INQeINQ1d](./query/runs.md#inqeinq1d) | [INQeacs1a](./query/runs.md#inqeacs1a) | [INQaINQ3d](./query/runs.md#inqainq3d) | [INQeINQ1b](./query/runs.md#inqeinq1b) | [INQeINQ2d](./query/runs.md#inqeinq2d) | [INQpAPL5a](./query/runs.md#inqpapl5a) | [INQeINQ1e](./query/runs.md#inqeinq1e) | [INQpINQ3b](./query/runs.md#inqpinq3b) | [INQpINQ3c](./query/runs.md#inqpinq3c) | [INQpINQ2d](./query/runs.md#inqpinq2d) | [INQeINQ1c](./query/runs.md#inqeinq1c) | [INQpINQ1c](./query/runs.md#inqpinq1c) | [INQpINQ3e](./query/runs.md#inqpinq3e) | [INQeINQ2a](./query/runs.md#inqeinq2a) | [INQeSab3a](./query/runs.md#inqesab3a) | [INQeSab1b](./query/runs.md#inqesab1b) | [INQpacs1a](./query/runs.md#inqpacs1a) | [INQpINQ1e](./query/runs.md#inqpinq1e) | [INQeSab1c](./query/runs.md#inqesab1c) | [INQpSab1c](./query/runs.md#inqpsab1c) | [INQpINQ1d](./query/runs.md#inqpinq1d) | [INQppir1a](./query/runs.md#inqppir1a) | [INQpINQ2a](./query/runs.md#inqpinq2a) | [INQpSab1a](./query/runs.md#inqpsab1a) | [INQeAPL5a](./query/runs.md#inqeapl5a) | [INQeAPL5b](./query/runs.md#inqeapl5b) | [INQeINQ2b](./query/runs.md#inqeinq2b) | [INQpINQ2b](./query/runs.md#inqpinq2b) | [INQeINQ3b](./query/runs.md#inqeinq3b) | [INQeINQ2e](./query/runs.md#inqeinq2e) | [INQeINQ2c](./query/runs.md#inqeinq2c) | [INQeINQ3e](./query/runs.md#inqeinq3e) | [INQeINQ3a](./query/runs.md#inqeinq3a) | [INQpAPL5b](./query/runs.md#inqpapl5b) | [INQeINQ3c](./query/runs.md#inqeinq3c) | [INQeINQ3d](./query/runs.md#inqeinq3d) | [INQpINQ2e](./query/runs.md#inqpinq2e) | [INQepir1a](./query/runs.md#inqepir1a) | [INQpINQ3d](./query/runs.md#inqpinq3d) | [INQpSab1b](./query/runs.md#inqpsab1b) | [INQpINQ3a](./query/runs.md#inqpinq3a) | [INQpINQ1b](./query/runs.md#inqpinq1b) | [INQeSab1a](./query/runs.md#inqesab1a) | [INQpINQ1a](./query/runs.md#inqpinq1a) | [INQpSab3a](./query/runs.md#inqpsab3a) | [INQpINQ2c](./query/runs.md#inqpinq2c)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in seven of the tracks: ad-hoc, filtering, spoken document retrieval, small web, large web, question and answer, and the query tracks. We spent significant time working on the filtering track, resulting in substantial performance improvement over TREC-7. For all of the other tracks, we used essentially the same system as used in previous years. In the next section, we describe some of the basic processing that was applied across most of the tracks. We then describe the details for each of the tracks and in some cases present some modest analysis of the effectiveness of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCFM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCFM99,
		author = {James Allan and James P. Callan and Fangfang Feng and Daniella Malin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCFM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Question Answering 

#### The TREC-8 Question Answering Track Evaluation

_Ellen M. Voorhees, Dawn M. Tice_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/qa8.pdf](http://trec.nist.gov/pubs/trec8/papers/qa8.pdf)
??? abstract "Abstract"
	
	The TREC-8 Question Answering track was the first large-scale evaluation of systems that return answers, as opposed to lists of documents, in response to a question. As a first evaluation, it is important to examine the evaluation methodology itself to understand any limits on the conclusions that can be drawn from the evaluation and possibly to find ways to improve subsequent evaluations. This paper has two main goals: to describe in detail how the evaluation was implemented, and to examine the consequences of the methodology on the comparative performance of the systems participating in the evaluation. The examination uncovered no serious flaws in the methodology, supporting its continued use for question answering evaluation. Nonetheless, redefining the specific task to be performed so that it more closely matches an actual user task does appear warranted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VoorheesT99.bib) "
	```
	@inproceedings{DBLP:conf/trec/VoorheesT99,
		author = {Ellen M. Voorhees and Dawn M. Tice},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-8} Question Answering Track Evaluation},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/qa8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VoorheesT99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NTT DATA: Overview of system approach at TREC-8 ad-hoc and question  answering

_Toru Takaki_

- :fontawesome-solid-user-group: **Participant:** [ntt](./qa/participants.md#ntt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-nttdata.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-nttdata.pdf)
- :material-file-search: **Runs:** [nttd8qs1](./qa/runs.md#nttd8qs1) | [nttd8qs2](./qa/runs.md#nttd8qs2) | [nttd8ql1](./qa/runs.md#nttd8ql1) | [nttd8ql4](./qa/runs.md#nttd8ql4)

??? abstract "Abstract"
	
	The question answering (QA) track is first attempt in TREC. We gave priority to the following verification for the QA track: (1) the effectiveness of technique by surface-text-based information in the text and (2) application of the information extraction technique. In our QA track, the following processing was done: (1) decision of answer form by question analysis, (2) passage scoring and selection for detailed analysis of the answer after initial retrieval, and (3) information extraction that look for words or phrases that match the form of the answer. We submitted two results to the answer categories of different strength respectively. A retrieval technique like ad-hoc is effective in a category answered by 250 bytes or less in our evaluation but the question analysis is important for a stricter category answered by 50 bytes or less.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Takaki99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Takaki99,
		author = {Toru Takaki},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{NTT} {DATA:} Overview of system approach at {TREC-8} ad-hoc and question answering},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-nttdata.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Takaki99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Extraction Supported Question Answering

_Rohini K. Srihari, Wei Li_

- :fontawesome-solid-user-group: **Participant:** [cymfony](./qa/participants.md#cymfony)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/cymfony.pdf](http://trec.nist.gov/pubs/trec8/papers/cymfony.pdf)
- :material-file-search: **Runs:** [textract9908](./qa/runs.md#textract9908)

??? abstract "Abstract"
	
	This paper discusses the use of our information extraction (IE) system, Textract, in the question-answering (QA) track of the recently held TREC-8 tests. One of our major objectives is to examine how IE can help IR (Information Retrieval) in applications like QA. Our study shows: (i) IE can provide solid support for QA; (ii) low-level IE like Named Entity tagging is often a necessary component in handling most types of questions; (iii) a robust natural language shallow parser provides a structural basis for handling questions; (iv) high-level domain independent IE, i.e. extraction of multiple relationships and general events, is expected to bring about a breakthrough in QA.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SrihariL99.bib) "
	```
	@inproceedings{DBLP:conf/trec/SrihariL99,
		author = {Rohini K. Srihari and Wei Li},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Information Extraction Supported Question Answering},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/cymfony.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SrihariL99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Xerox TREC-8 Question Answering Track Report

_David A. Hull_

- :fontawesome-solid-user-group: **Participant:** [xerox](./qa/participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/xerox-QA.pdf](http://trec.nist.gov/pubs/trec8/papers/xerox-QA.pdf)
- :material-file-search: **Runs:** [xeroxQA8lC](./qa/runs.md#xeroxqa8lc) | [xeroxQA8sC](./qa/runs.md#xeroxqa8sc)

??? abstract "Abstract"
	
	This report describes the Xerox work on the TREC-8 Question Answering Track. We linked together a few basic NLP components (a question parser, a sentence boundary identifier, and a proper noun tagger) with a sentence scoring function and an answer presentation function built specifically for the TREC Q&A task. Our system found the correct 50-byte answer (in the top 5 responses) to 45% of the questions, a quite respectable performance, but with considerable room for improvement. Based on the failure analysis presented in this paper, we can conclude that the system would benefit from having access to a broad range of other NLP technologies, including robust parsing and coreference analysis, or some good heuristic approximations thereof. The system also has a clear need for some semantic resources to help with certain difficult problems, such as finding answers that match the semantic class X in What X? questions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Hull99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Hull99,
		author = {David A. Hull},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Xerox {TREC-8} Question Answering Track Report},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/xerox-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Hull99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AT&T at TREC-8

_Amit Singhal, Steven P. Abney, Michiel Bacchiani, Michael Collins, Donald Hindle, Fernando C. N. Pereira_

- :fontawesome-solid-user-group: **Participant:** [ATT](./qa/participants.md#att)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf](http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf)
- :material-file-search: **Runs:** [attqa250e](./qa/runs.md#attqa250e) | [attqa250p](./qa/runs.md#attqa250p) | [attqa50p](./qa/runs.md#attqa50p) | [attqa50e](./qa/runs.md#attqa50e)

??? abstract "Abstract"
	
	In 1999, AT&T participated in the ad-hoc task and the Question Answering (QA), Spoken Document Retrieval (SDR), and Web tracks. Most of our effort for TREC-8 focused on the QA and SDR tracks. Results from SDR track show that our document expansion techniques, presented in [8, 9], are very effective for speech retrieval. The results for question answering are also encouraging. Our system designed in a relatively short period for this task can find the correct answer for about 45% of the user questions. This is specially good given the fact that our system extracts only a short phrase as an answer.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinghalABCHP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinghalABCHP99,
		author = {Amit Singhal and Steven P. Abney and Michiel Bacchiani and Michael Collins and Donald Hindle and Fernando C. N. Pereira},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {AT{\&}T at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SinghalABCHP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SCAI TREC-8 Experiments

_Dong-Ho Shin, Yu-Hwan Kim, Sun Kim, Jae-Hong Eom, Hyung-Joo Shin, Byoung-Tak Zhang_

- :fontawesome-solid-user-group: **Participant:** [seoul](./qa/participants.md#seoul)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps](http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps)
- :material-file-search: **Runs:** [Scai8QnA](./qa/runs.md#scai8qna)

??? abstract "Abstract"
	
	This working note reports our experiences with TREC-8 on four tracks: Ad Hoc, Filtering, Web, and QA. The Ad Hoc retrieval engine, SCAIR, has been used for the Web and QA experiments, and the filtering experiments were based on it's own engine. As a second entry to TREC, we focused this year on exploring possibilities of applying machine learning techniques to TREC tasks. The Ad Hoc track employed a cluster-based retrieval method where the scoring function used cluster information extracted from a collection of precompiled documents. Filtering was based on naive Bayes learning supported by an EM algorithm. In the Web track, we compared the performance of using link information to that of not using the information. In the QA track, some passage extraction techniques have been tested using the baseline SCAIR retrieval engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShinKKESZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShinKKESZ99,
		author = {Dong{-}Ho Shin and Yu{-}Hwan Kim and Sun Kim and Jae{-}Hong Eom and Hyung{-}Joo Shin and Byoung{-}Tak Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SCAI} {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShinKKESZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Use of Predictive Annotation for Question Answering in TREC8

_John M. Prager, Dragomir R. Radev, Eric W. Brown, Anni Coden, Valerie Samn_

- :fontawesome-solid-user-group: **Participant:** [ibm-chong](./qa/participants.md#ibm-chong)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/IBMTrec8QA.ps](http://trec.nist.gov/pubs/trec8/papers/IBMTrec8QA.ps)
- :material-file-search: **Runs:** [IBMVS995](./qa/runs.md#ibmvs995) | [IBMVS992](./qa/runs.md#ibmvs992) | [IBMDR992](./qa/runs.md#ibmdr992) | [IBMDR995](./qa/runs.md#ibmdr995)

??? abstract "Abstract"
	
	This paper introduces the technique of Predictive Annota-tion, a methodology for indexing texts for retrieval aimed at answering fact-seeking questions. The essence of the approach can be stated simply: index the answers. This is done by establishing about 20 classes of objects that can be identified in text by shallow parsing, and by annotating and indexing the text with these labels, which we call QA-Tokens. Given a question, its class is identified and the question is modified accordingly to include the appropriate token(s). The search engine is modified to rank and return short passages of text rather than documents. The QA-Tokens are used in later stages of analysis to extract the supposed answers from these returned passages. Fi-nally, all potential answers are ranked using a novel for-mula, which determines which ones among them are most likely to be correct.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PragerRBCS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/PragerRBCS99,
		author = {John M. Prager and Dragomir R. Radev and Eric W. Brown and Anni Coden and Valerie Samn},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Use of Predictive Annotation for Question Answering in {TREC8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/IBMTrec8QA.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PragerRBCS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CRL's TREC-8 Systems Cross-Lingual IR, and Q&A

_William C. Ogden, James R. Cowie, Yevgeny Ludovik, Hugo Molina-Salgado, Sergei Nirenburg, Nigel Sharples, Svetlana O. Sheremetyeva_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./qa/participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/crl_proceedings.pdf](http://trec.nist.gov/pubs/trec8/papers/crl_proceedings.pdf)
- :material-file-search: **Runs:** [clr99s](./qa/runs.md#clr99s)

??? abstract "Abstract"
	
	This paper describes the systems used by CRL in the Cross-lingual IR and Q&A tracks. The cross-language experiment was unique in that it was run interactively with a mono-lingual user simulating how a true cross-language system might be used. The methods used in the Q&A system are based on language processing technology developed at CRL for machine translation and information extraction.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OgdenCLMNSS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/OgdenCLMNSS99,
		author = {William C. Ogden and James R. Cowie and Yevgeny Ludovik and Hugo Molina{-}Salgado and Sergei Nirenburg and Nigel Sharples and Svetlana O. Sheremetyeva},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {CRL's {TREC-8} Systems Cross-Lingual IR, and Q{\&}A},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/crl\_proceedings.pdf},
		timestamp = {Thu, 17 Nov 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OgdenCLMNSS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Experiments at Maryland: CLIR, QA and Routing

_Douglas W. Oard, Jianqiang Wang, Dekang Lin, Ian Soboroff_

- :fontawesome-solid-user-group: **Participant:** [umd](./qa/participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf](http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf)
- :material-file-search: **Runs:** [umdqa](./qa/runs.md#umdqa)

??? abstract "Abstract"
	
	The University of Maryland team participated in four aspects of TREC-8: the ad hoc retrieval task, the main task in the cross-language retrieval (CLIR) track, the question answering track, and the routing task in the filtering track. The CLIR method was based on Pirkola's method for Dictionary-based Query Translation, using freely available dictionaries. Broad-coverage parsing and rule-based matching was used for question answering. Routing was performed using Latent Semantic Indexing in profile space.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardWLS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardWLS99,
		author = {Douglas W. Oard and Jianqiang Wang and Dekang Lin and Ian Soboroff},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Experiments at Maryland: CLIR, {QA} and Routing},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OardWLS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Coreference in Question Answering

_Thomas S. Morton_

- :fontawesome-solid-user-group: **Participant:** [ge](./qa/participants.md#ge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/notebook.pdf](http://trec.nist.gov/pubs/trec8/papers/notebook.pdf)
- :material-file-search: **Runs:** [CRDBASE050](./qa/runs.md#crdbase050) | [CRDBASE250](./qa/runs.md#crdbase250) | [GePenn](./qa/runs.md#gepenn)

??? abstract "Abstract"
	
	In this paper we present an overview of the system used by the GE/Penn team for the the Question Answering Track of TREC-8. Our system uses a simple sentence ranking method which is enhanced by the addition of coreference annotated data as its input. We will present an overview of our initial system and its components. Since this was the first time this track has been run, we made numerous additions to our initial system. We will describe these additions and what motivated them as a series of lessons learned after which the final system used for our submission will be described. Finally we will discuss directions for future research.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Morton99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Morton99,
		author = {Thomas S. Morton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Coreference in Question Answering},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/notebook.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Morton99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LASSO: A Tool for Surfing the Answer Net

_Dan I. Moldovan, Sanda M. Harabagiu, Marius Pasca, Rada Mihalcea, Richard Goodrum, Roxana Girju, Vasile Rus_

- :fontawesome-solid-user-group: **Participant:** [smu](./qa/participants.md#smu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/smu.pdf](http://trec.nist.gov/pubs/trec8/papers/smu.pdf)
- :material-file-search: **Runs:** [SMUNLP1](./qa/runs.md#smunlp1) | [SMUNLP2](./qa/runs.md#smunlp2)

??? abstract "Abstract"
	
	This paper presents the architecture, operation and results obtained with the LASSO system developed in the Natural Language Processing Laboratory at SMU. The system relies on a combination of syntactic and semantic techniques, and lightweight abductive inference to find answers. The search for the answer is based on a novel form of indexing called paragraph in-dexing. A score of 55.5% for short answers and 64.5% for long answers was achieved.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoldovanHPMGR99.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoldovanHPMGR99,
		author = {Dan I. Moldovan and Sanda M. Harabagiu and Marius Pasca and Rada Mihalcea and Richard Goodrum and Roxana Girju and Vasile Rus},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{LASSO:} {A} Tool for Surfing the Answer Net},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/smu.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoldovanHPMGR99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ask Me Tomorrow: The NRC and University of Ottawa Question Answering  System

_Joel D. Martin, Chris Lankester_

- :fontawesome-solid-user-group: **Participant:** [ottawa](./qa/participants.md#ottawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/UofO_QA.pdf](http://trec.nist.gov/pubs/trec8/papers/UofO_QA.pdf)
- :material-file-search: **Runs:** [UOandNRC](./qa/runs.md#uoandnrc) | [UOandNRC50](./qa/runs.md#uoandnrc50)

??? abstract "Abstract"
	
	Funny how one extra Perl sort function can make a score of 0.52' on the question answering task look a lot like 0. This paper describes our brute force approach to the question answering task and how we did achieve some success, despite formatting problems with our answer file. This paper also describes how we conducted automatic evaluations using the NIST judgment file on newly proposed answers. A good question says what it is about and constrains the form of the answer. In other words, it specifies the distinguishing context for an answer and partially describes the kind of information that would count as an answer. The question 'Who wrote the Declaration of Independence?' specifies that we are talking about someone who wrote a particular document, instead of engaging in some other action with respect to some other document. In addition, the question describes that we are looking for a 'who' which must be a person, agency, or institution. The process of finding an existing answer to a question means finding part of a document that matches the distinguishing context of the question and then extracting an answer of the right type from nearby. Ideally, the extracted answer would have the right sort of relationship to the context of the question. Since this is our first year at TREC, and we were starting with no existing code, we decided to take a brute force approach to the problem. We divided the task into three phases. Phase I does a very high recall retrieval using the words in the question with the goal of discarding 90% of the document collection. Even with only a tenth of the documents, who wants to read them all? Phase Il does an exhaustive scan of all 200-500 byte windows in the retrieved tenth, looking for strings with high similarity to the original question. This phase also ranks these text windows and adds extra points if an obvious answer type is nearby. Finally, Phase Ill was intended (and did a poor job of it) to extract the best answer of the right answer type from the best outputs from Phase II. In the rest of this notebook paper, we first describe the three phases in more detail and then describe how we evaluated the system. We end with a discussion of the results and ideas for future work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MartinL99.bib) "
	```
	@inproceedings{DBLP:conf/trec/MartinL99,
		author = {Joel D. Martin and Chris Lankester},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ask Me Tomorrow: The {NRC} and University of Ottawa Question Answering System},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/UofO\_QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MartinL99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question-Answering Using Semantic Relation Triples

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./qa/participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/clresearch.pdf](http://trec.nist.gov/pubs/trec8/papers/clresearch.pdf)
- :material-file-search: **Runs:** [clr99s](./qa/runs.md#clr99s)

??? abstract "Abstract"
	
	This paper describes the development of a prototype system to answer questions by selecting sentences from the documents in which the answers occur. After parsing each sentence in these documents, databases are constructed by extracting relational triples from the parse output. The triples consist of discourse entities, semantic relations, and the governing words to which the entities are bound in the sentence. Database triples are also generated for the questions. Question-answering consists of matching the question database records with the records for the documents. The prototype system was developed specifically to respond to the TREC-8 Q&A track, with an existing parser and some existing capability for analyzing parse output. The system was designed to investigate the viability of using structural information about the sentences in a document to answer questions. The CL Research system achieved an overall score of 0.281 (i.e., on average, providing a sentence containing a correct answer as the fourth selection). The score demonstrates the viability of the approach. Post-hoc analysis suggests that this score understates the performance of the prototype and estimates that a more accurate score is approximately 0.482. This analysis also suggests several further improvements and the potential for investigating other avenues that make use of semantic networks and computational lexicology.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Litkowski99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Litkowski99,
		author = {Kenneth C. Litkowski},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Question-Answering Using Semantic Relation Triples},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/clresearch.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Litkowski99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Description of Preliminary Results to TREC-8 QA Task

_Chuan-Jie Lin, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu](./qa/participants.md#ntu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/NTU_TREC8_QA.pdf](http://trec.nist.gov/pubs/trec8/papers/NTU_TREC8_QA.pdf)
- :material-file-search: **Runs:** [NTU99](./qa/runs.md#ntu99)

??? abstract "Abstract"
	
	Question Answering (QA) becomes a hot research topic in recent years due to the very large virtual database on the Internet. QA is defined to find the exact answer, which can meet the users' need more precisely, from a huge unstructured database. Traditional information retrieval systems cannot afford to resolve this problem. On the one hand, users have to find out the answers by themselves from the documents returned by IR systems. On the other hand, the answers may appear in any documents, even that the document is irrelevant to the question. Two possible approaches, i.e., keyword matching and template extraction, can be considered. Keyword matching postulates that the answering text contains most of the keywords. In other words, it carries enough information relevant to the question. Using templates is some sort of information extraction. The contents of documents are represented as templates. To answer a question, a QA system has to select an appropriate template, then fill the template and finally offer the answer. The major difficulties in this approach are to find general domain templates, and to decide which template can be applied to answer the question. Some other techniques are also useful. For example, to answer the questions 'Who...' and 'When...', the identification of named entities like person names and time/date expressions will help to locate the answer. In our preliminary study, we adopt keyword-matching strategy coupling with expanding the keyword set selected from the question sentence by the synonyms and the morphological forms. We participate in the group 'Sentence or under 250 bytes'. The detail will be presented below.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinC99,
		author = {Chuan{-}Jie Lin and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Description of Preliminary Results to {TREC-8} {QA} Task},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/NTU\_TREC8\_QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Sheffield TREC-8 Q&A System

_Kevin Humphreys, Robert J. Gaizauskas, Mark Hepple, Mark Sanderson_

- :fontawesome-solid-user-group: **Participant:** [sheffield](./qa/participants.md#sheffield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-ushefqa.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-ushefqa.pdf)
- :material-file-search: **Runs:** [shefinq250](./qa/runs.md#shefinq250) | [shefinq50](./qa/runs.md#shefinq50) | [shefatt50](./qa/runs.md#shefatt50) | [shefatt250](./qa/runs.md#shefatt250)

??? abstract "Abstract"
	
	The system entered by the University of Sheffield in the question answering track of TREC-8 is the result of coupling two existing technologies - information retrieval (IR) and information extraction (IE). In essence the approach is this: the IR system treats the question as a query and returns a set of top ranked documents or passages; the IE system uses NLP techniques to parse the question, analyse the top ranked documents or passages returned by the IR system, and instantiate a query variable in the semantic representation of the question against the semantic representation of the analysed documents or passages. Thus, while the IE system by no means attempts 'full text under-standing', this approach is a relatively deep approach which attempts to work with meaning representations. Since the information retrieval systems we used were not our own (AT&T and UMass) and were used more or less 'off the shelf', this paper concentrates on describing the modifications made to our existing information extraction system to allow it to participate in the Q & A task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HumphreysGHS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HumphreysGHS99,
		author = {Kevin Humphreys and Robert J. Gaizauskas and Mark Hepple and Mark Sanderson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {University of Sheffield {TREC-8} Q{\&}A System},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-ushefqa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HumphreysGHS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The RMIT/CSIRO Ad Hoc, Q&A, Web, Interactive, and Speech Experiments  at TREC 8

_Michael Fuller, Marcin Kaszkiel, Sam Kimberley, Corinna Ng, Ross Wilkinson, Mingfang Wu, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [rmit](./qa/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf](http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf)
- :material-file-search: **Runs:** [mds08q1](./qa/runs.md#mds08q1)

??? abstract "Abstract"
	
	We participated in the 250 byte category of the question and answer track, submitting one run, mds08q. Our objective in participating in this track was to determine the appropriateness of applying traditional document retrieval techniques to the retrieval and extraction of small, focused text segments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FullerKKNWWZ99,
		author = {Michael Fuller and Marcin Kaszkiel and Sam Kimberley and Corinna Ng and Ross Wilkinson and Mingfang Wu and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {RMIT/CSIRO} Ad Hoc, Q{\&}A, Web, Interactive, and Speech Experiments at {TREC} 8},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QALC - the Question-Answering program of the Language and Cognition  group at LIMSI-CNRS

_Olivier Ferret, Brigitte Grau, Gabriel Illouz, Christian Jacquemin, Nicolas Masson_

- :fontawesome-solid-user-group: **Participant:** [limsi](./qa/participants.md#limsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/LimsiLC-proceedings-paper.pdf](http://trec.nist.gov/pubs/trec8/papers/LimsiLC-proceedings-paper.pdf)
- :material-file-search: **Runs:** [LimsiLC](./qa/runs.md#limsilc)

??? abstract "Abstract"
	
	In this report we describe the QALC system (the Question-Answering program of the Language and Cognition group at LIMSI-CNRS) which has been involved in the QA-track evaluation at TREC8. The purpose of the Question-Answering track is to find the answers to a set of 200 questions. The answers are text sequences extracted from the volumes 4 and 5 of the TREC collection. All the questions have at least one answer in the collection. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerretGIJM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerretGIJM99,
		author = {Olivier Ferret and Brigitte Grau and Gabriel Illouz and Christian Jacquemin and Nicolas Masson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{QALC} - the Question-Answering program of the Language and Cognition group at {LIMSI-CNRS}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/LimsiLC-proceedings-paper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FerretGIJM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filters, Webs and Answers: The University of Iowa TREC-8 Results

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [iowa](./qa/participants.md#iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf](http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf)
- :material-file-search: **Runs:** [UIowaQA2](./qa/runs.md#uiowaqa2) | [UIowaQA3](./qa/runs.md#uiowaqa3) | [UIowaQA4](./qa/runs.md#uiowaqa4) | [UIowaQA1](./qa/runs.md#uiowaqa1)

??? abstract "Abstract"
	
	The University of Iowa attempted three tracks this year: filtering, question answering, and Web, the latter two new for us this year. All work was based upon that done for TREC-7 [2], with our system adapted for the specifics of the QA and Web tracks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS99,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Filters, Webs and Answers: The University of Iowa {TREC-8} Results},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fast Automatic Passage Ranking (MultiText Experiments for TREC-8)

_Gordon V. Cormack, Charles L. A. Clarke, D. I. E. Kisman, Christopher R. Palmer_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./qa/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf](http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf)
- :material-file-search: **Runs:** [uwmt8qa1](./qa/runs.md#uwmt8qa1)

??? abstract "Abstract"
	
	TREC-8 represents the fifth year that the MultiText project has participated in TREC |2, 1, 4, 5]. The MultiText project develops and prototypes scalable technologies for parallel information retrieval systems implemented on networks of workstations. Research issues are addressed in the context of this parallel architecture. Issues of concern to the MultiText Project include data distribution, load balancing, fast update, fault tolerance, document structure, relevance ranking, and user interaction. The MultiText system incorporates a unique technique for arbitrary passage retrieval. Since our initial participation in TREC-4 our TREC work has explored variants of this technique. For TREC-8 we focused our efforts on the Web track. In addition, we submitted runs for the Adhoc task (title and title+description) and a run for the Question Answering task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackCKP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackCKP99,
		author = {Gordon V. Cormack and Charles L. A. Clarke and D. I. E. Kisman and Christopher R. Palmer},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fast Automatic Passage Ranking (MultiText Experiments for {TREC-8)}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackCKP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Sys Called Qanda

_Eric Breck, John D. Burger, Lisa Ferro, David House, Marc Light, Inderjeet Mani_

- :fontawesome-solid-user-group: **Participant:** [mitre](./qa/participants.md#mitre)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/MITRE-TREC8-conference.pdf](http://trec.nist.gov/pubs/trec8/papers/MITRE-TREC8-conference.pdf)
- :material-file-search: **Runs:** [MTR99050](./qa/runs.md#mtr99050) | [MTR99250](./qa/runs.md#mtr99250)

??? abstract "Abstract"
	
	Our question answering system was built with a number of priorities in mind. First, we wanted to experiment with natural language processing (NLP) technologies such as shallow parsing, named entity tagging, and coreference chaining. We felt that the small number of terms in the questions coupled with the short length of the answers would make NLP technologies clearly beneficial, unlike previous experiments with NLP technologies on traditional IR tasks. At a more practical level, we were familiar with and interested in such technologies and thus their use would be relatively straightforward and enjoyable. Second, we wanted to use information retrieval (IR) techniques in hopes of achieving robustness and efficiency. It seemed obvious that many answers would appear in documents and passages laden with terms from the question. Finally, we wanted to experiment with different modules from different sites with differing input and output representation and implementational details. Thus, we needed a multi-process system with a flexible data format. Driven by these priorities, we built Qanda,' a system that combines the finer-grained representations and inference abilities of NLP with IR's robustness and domain independence. In the following, we describe the Qanda system, discuss experimental results for the system, and finally discuss automating the scoring of question answering systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BreckBFHLM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BreckBFHLM99,
		author = {Eric Breck and John D. Burger and Lisa Ferro and David House and Marc Light and Inderjeet Mani},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A Sys Called Qanda},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/MITRE-TREC8-conference.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BreckBFHLM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-8

_James Allan, James P. Callan, Fangfang Feng, Daniella Malin_

- :fontawesome-solid-user-group: **Participant:** [umass](./qa/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf)
- :material-file-search: **Runs:** [INQ634](./qa/runs.md#inq634) | [INQ635](./qa/runs.md#inq635) | [INQ638](./qa/runs.md#inq638) | [INQ639](./qa/runs.md#inq639)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in seven of the tracks: ad-hoc, filtering, spoken document retrieval, small web, large web, question and answer, and the query tracks. We spent significant time working on the filtering track, resulting in substantial performance improvement over TREC-7. For all of the other tracks, we used essentially the same system as used in previous years. In the next section, we describe some of the basic processing that was applied across most of the tracks. We then describe the details for each of the tracks and in some cases present some modest analysis of the effectiveness of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCFM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCFM99,
		author = {James Allan and James P. Callan and Fangfang Feng and Daniella Malin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCFM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Spoken Document Retrieval 

#### The TREC Spoken Document Retrieval Track: A Success Story

_John S. Garofolo, Cedric G. P. Auzanne, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-sdr-overview.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-sdr-overview.pdf)
??? abstract "Abstract"
	
	This paper describes work within the NIST Text REtrieval Conference (TREC) over the last three years in designing and implementing evaluations of Spoken Document Retrieval (SDR) technology within a broadcast news domain. SDR involves the search and retrieval of excerpts from spoken audio recordings using a combination of automatic speech recognition and information retrieval technologies. The TREC SDR Track has provided an infrastructure for the development and evaluation of SDR technology and a common forum for the exchange of knowledge between the speech recognition and information retrieval research communities. The SDR Track can be declared a success in that it has provided objective, demonstrable proof that this technology can be successfully applied to realistic audio collections using a combination of existing technologies and that it can be objectively evaluated. The design and implementation of each of the SDR evaluations are presented and the results are summarized. Plans for the 2000 TREC SDR Track are presented and thoughts about how the track might evolve are discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarofoloAV99.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarofoloAV99,
		author = {John S. Garofolo and Cedric G. P. Auzanne and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC} Spoken Document Retrieval Track: {A} Success Story},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-sdr-overview.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GarofoloAV99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AT&T at TREC-8

_Amit Singhal, Steven P. Abney, Michiel Bacchiani, Michael Collins, Donald Hindle, Fernando C. N. Pereira_

- :fontawesome-solid-user-group: **Participant:** [ATT](./sdr/participants.md#att)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf](http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf)
- :material-file-search: **Runs:** [att-r1](./sdr/runs.md#att-r1) | [att-b1](./sdr/runs.md#att-b1) | [att-s1](./sdr/runs.md#att-s1) | [att-s2](./sdr/runs.md#att-s2) | [att-cr-cmus1](./sdr/runs.md#att-cr-cmus1) | [att-cr-cuhtks1](./sdr/runs.md#att-cr-cuhtks1) | [att-cr-cuhtks1p1](./sdr/runs.md#att-cr-cuhtks1p1) | [att-cr-limsis1](./sdr/runs.md#att-cr-limsis1) | [att-cr-shefs1](./sdr/runs.md#att-cr-shefs1)

??? abstract "Abstract"
	
	In 1999, AT&T participated in the ad-hoc task and the Question Answering (QA), Spoken Document Retrieval (SDR), and Web tracks. Most of our effort for TREC-8 focused on the QA and SDR tracks. Results from SDR track show that our document expansion techniques, presented in [8, 9], are very effective for speech retrieval. The results for question answering are also encouraging. Our system designed in a relatively short period for this task can find the correct answer for about 45% of the user questions. This is specially good given the fact that our system extracts only a short phrase as an answer.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinghalABCHP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinghalABCHP99,
		author = {Amit Singhal and Steven P. Abney and Michiel Bacchiani and Michael Collins and Donald Hindle and Fernando C. N. Pereira},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {AT{\&}T at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SinghalABCHP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CMU Spoken Document Retrieval in Trec-8: Analysis of the role of  Term Frequency TF

_Matthew Siegler, Rong Jin, Alexander G. Hauptmann_

- :fontawesome-solid-user-group: **Participant:** [cmu](./sdr/participants.md#cmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-cmusdr.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-cmusdr.pdf)
- :material-file-search: **Runs:** [cmu-s1](./sdr/runs.md#cmu-s1) | [cmu-b1](./sdr/runs.md#cmu-b1) | [cmu-r1](./sdr/runs.md#cmu-r1) | [cmu-s2](./sdr/runs.md#cmu-s2)

??? abstract "Abstract"
	
	The participation of Carnegie Mellon University in the TREC-8 Spoken Document Retrieval Track used the basic same Sphinx speech recognition system as in TREC-7. Due to some unfortunate defaults in the parameter setup files, the speech recognizer did not perform in a reasonable manner. We will not analyze the results of the speech recognizer runs, as we believe the results contained abnormal types of errors, and insights or improvements on these errors would not generalize. A thorough examination of the speech recognition condition is given in [3]. However, we did evaluate a slightly modified weighting scheme in the reference (R1) and baseline (B1) conditions, which is described below.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SieglerJH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/SieglerJH99,
		author = {Matthew Siegler and Rong Jin and Alexander G. Hauptmann},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CMU} Spoken Document Retrieval in Trec-8: Analysis of the role of Term Frequency {TF}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-cmusdr.pdf},
		timestamp = {Thu, 16 Dec 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SieglerJH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Twenty-One at TREC-8: using Language Technology for Information  Retrieval

_Wessel Kraaij, Renée Pohlmann, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [twentyone](./sdr/participants.md#twentyone)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf](http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf)
- :material-file-search: **Runs:** [tno8b-b1-limsi](./sdr/runs.md#tno8b-b1-limsi) | [tno8b-r1-limsi](./sdr/runs.md#tno8b-r1-limsi) | [tno8b-s1-limsi](./sdr/runs.md#tno8b-s1-limsi) | [tno8b-b1u-limsi](./sdr/runs.md#tno8b-b1u-limsi) | [tno8b-s1u-limsi](./sdr/runs.md#tno8b-s1u-limsi)

??? abstract "Abstract"
	
	This paper describes the official runs of the Twenty-One group for TREC-8. The Twenty-One group participated in the Ad-hoc, CLIR, Adaptive Filtering and SDR tracks. The main focus of our experiments is the development and evaluation of retrieval methods that are motivated by natural language processing techniques. The following new techniques are introduced in this paper. In the Ad-Hoc and CLIR tasks we experimented with automatic sense disambiguation followed by query expansion or translation. We used a combination of thesaurial and corpus information for the disambiguation process. We continued research on CLIR techniques which exploit the target corpus for an implicit disambiguation, by importing the translation probabilities into the probabilistic term-weighting framework. In filtering we extended the the use of language models for document ranking with a relevance feedback algorithm for query term reweighting.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KraaijPH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/KraaijPH99,
		author = {Wessel Kraaij and Ren{\'{e}}e Pohlmann and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Twenty-One at {TREC-8:} using Language Technology for Information Retrieval},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KraaijPH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Spoken Document Retrieval for TREC-8 at Cambridge University

_Sue E. Johnson, Philip C. Woodland, Karen Sparck Jones, Pierre Jourlin_

- :fontawesome-solid-user-group: **Participant:** [cambridge](./sdr/participants.md#cambridge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/cuhtk-sdr-paper.pdf](http://trec.nist.gov/pubs/trec8/papers/cuhtk-sdr-paper.pdf)
- :material-file-search: **Runs:** [cuhtk-r1](./sdr/runs.md#cuhtk-r1) | [cuhtk-b1](./sdr/runs.md#cuhtk-b1) | [cuhtk-s1](./sdr/runs.md#cuhtk-s1) | [cuhtk-b1u](./sdr/runs.md#cuhtk-b1u) | [cuhtk-s1u](./sdr/runs.md#cuhtk-s1u) | [cuhtk-s1p1u](./sdr/runs.md#cuhtk-s1p1u) | [cuhtk-s1p1](./sdr/runs.md#cuhtk-s1p1) | [cuhtk-cru-nist-b2](./sdr/runs.md#cuhtk-cru-nist-b2) | [cuhtk-cru-limsi-s1](./sdr/runs.md#cuhtk-cru-limsi-s1) | [cuhtk-cru-shef-s1](./sdr/runs.md#cuhtk-cru-shef-s1) | [cuhtk-cr-att-s1](./sdr/runs.md#cuhtk-cr-att-s1) | [cuhtk-cr-cmu-s1](./sdr/runs.md#cuhtk-cr-cmu-s1) | [cuhtk-cr-shef-s1](./sdr/runs.md#cuhtk-cr-shef-s1) | [cuhtk-cr-b2](./sdr/runs.md#cuhtk-cr-b2) | [cuhtk-cr-limsi-s1](./sdr/runs.md#cuhtk-cr-limsi-s1)

??? abstract "Abstract"
	
	This paper presents work done at Cambridge University on the TREC-8 Spoken Document Retrieval (SDR) Track. The 500 hours of broadcast news audio was filtered using an automatic scheme for detecting commercials, and then transcribed using a 2-pass HTK speech recogniser which ran at 13 times real time. The system gave an overall word error rate of 20.5% on the 10 hour scored subset of the corpus, the lowest in the track. Our retrieval engine used an Okapi scheme with traditional stopping and Porter stemming, enhanced with part-of-speech weighting on query terms, a stemmer exceptions list, semantic 'poset' in-dexing, parallel collection frequency weighting, both parallel and traditional blind relevance feedback and document expansion using parallel blind relevance feedback. The final system gave an Average Precision of 55.29% on our transcriptions. For the case where story boundaries are unknown, a similar retrieval system, without the document expansion, was run on a set of 'stories' derived from windowing the transcriptions after removal of commercials. Boundaries were forced at 'commercial' or 'music' changes and some recombination of temporally close stories was allowed after retrieval. When scoring duplicate story hits and commercials as irrelevant, this system gave an Average Precision of 41.47% on our transcriptions. The paper also presents results for cross-recogniser experiments using our retrieval strategies on transcriptions from our own first pass output, AT&T, CMU, 2 NIST-run BBN baselines, LIMSI and Sheffield University, and the relationship between performance and transcription error rate is shown.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JohnsonWJJ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/JohnsonWJJ99,
		author = {Sue E. Johnson and Philip C. Woodland and Karen Sparck Jones and Pierre Jourlin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Spoken Document Retrieval for {TREC-8} at Cambridge University},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/cuhtk-sdr-paper.pdf},
		timestamp = {Wed, 05 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JohnsonWJJ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Experiments at SUNY Buffalo

_Benjamin Han, Ramya Nagarajan, Rohini K. Srihari, Srikanth Munirathnam_

- :fontawesome-solid-user-group: **Participant:** [buffalo](./sdr/participants.md#buffalo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ub-nbpaper.pdf](http://trec.nist.gov/pubs/trec8/papers/ub-nbpaper.pdf)
- :material-file-search: **Runs:** [cedar-r1](./sdr/runs.md#cedar-r1) | [cedar-b1](./sdr/runs.md#cedar-b1)

??? abstract "Abstract"
	
	For TREC-8, State University of New York at Buffalo(UB) participated in the ad-hoe task and the spoken document retrieval(SDR) track. This is our first year of participation at TREC. We submitted two runs for the Ad-hoc task. The first run was term vector-based using SMART[10]. The second run used the TROVE - Text Retrieval using Object VEctors - system. For the SDR Track, we participated in the IR component of the Quasi-SDR task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HanNSM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HanNSM99,
		author = {Benjamin Han and Ramya Nagarajan and Rohini K. Srihari and Srikanth Munirathnam},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Experiments at {SUNY} Buffalo},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ub-nbpaper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HanNSM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The LIMSI SDR System for TREC-8

_Jean-Luc Gauvain, Yannick de Kercadio, Lori Lamel, Gilles Adda_

- :fontawesome-solid-user-group: **Participant:** [limsi-tlp](./sdr/participants.md#limsi-tlp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/limsi-tlp.pdf](http://trec.nist.gov/pubs/trec8/papers/limsi-tlp.pdf)
- :material-file-search: **Runs:** [limsi-b1](./sdr/runs.md#limsi-b1) | [limsi-r1](./sdr/runs.md#limsi-r1) | [limsi-s1](./sdr/runs.md#limsi-s1) | [limsi-b2](./sdr/runs.md#limsi-b2) | [limsi-cr-att1](./sdr/runs.md#limsi-cr-att1) | [limsi-cr-cmu1](./sdr/runs.md#limsi-cr-cmu1) | [limsi-cr-cuhtk1](./sdr/runs.md#limsi-cr-cuhtk1) | [limsi-cr-shef1](./sdr/runs.md#limsi-cr-shef1)

??? abstract "Abstract"
	
	In this paper we report on our TREC-8 SDR system, which combines an adapted version of the LIMSI 1998 Hub-4E transcription system for speech recognition with an IR system based on the Okapi term weighting function. Experimental results are given in terms of word error rate and average precision for both the SDR’98 and SDR’99 data sets. In addition to the Okapi approach, we also investiged a Markovian approach, which although not used in the TREC-8 evaluation, yields comparable results. The evaluation system obtained an average precision of 0.5411 on the reference transcriptions and of 0.5072 on the automatic transcriptions. The word error rate measured on a 10 hour subset is of 21.5%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GauvainKLA99.bib) "
	```
	@inproceedings{DBLP:conf/trec/GauvainKLA99,
		author = {Jean{-}Luc Gauvain and Yannick de Kercadio and Lori Lamel and Gilles Adda},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {LIMSI} {SDR} System for {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/limsi-tlp.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GauvainKLA99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The RMIT/CSIRO Ad Hoc, Q&A, Web, Interactive, and Speech Experiments  at TREC 8

_Michael Fuller, Marcin Kaszkiel, Sam Kimberley, Corinna Ng, Ross Wilkinson, Mingfang Wu, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [rmit](./sdr/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf](http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf)
- :material-file-search: **Runs:** [mds08-b1](./sdr/runs.md#mds08-b1) | [mds08-r1](./sdr/runs.md#mds08-r1)

??? abstract "Abstract"
	
	Two runs were submitted for this year's Quasi-SDR runs. The word-based documents were first translated to phonemes using a text-to-phoneme algorithm. We assumed that there is a certain level of word recognition error for each type of tran-scription. Given this, we utilised a passage retrieval technique to perform the retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FullerKKNWWZ99,
		author = {Michael Fuller and Marcin Kaszkiel and Sam Kimberley and Corinna Ng and Ross Wilkinson and Mingfang Wu and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {RMIT/CSIRO} Ad Hoc, Q{\&}A, Web, Interactive, and Speech Experiments at {TREC} 8},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc, Cross-language and Spoken Document Information Retrieval at  IBM

_Martin Franz, J. Scott McCarley, Todd Ward_

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./sdr/participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/t8_ibm_hlt.pdf](http://trec.nist.gov/pubs/trec8/papers/t8_ibm_hlt.pdf)
- :material-file-search: **Runs:** [ibms-r1](./sdr/runs.md#ibms-r1) | [ibms-b1](./sdr/runs.md#ibms-b1)

??? abstract "Abstract"
	
	The Natural Language Systems group at IBM participated in three tracks at TREC-8: ad hoc, SDR and cross-language. Our SDR and ad hoc participation included experiments involving query expansion and clustering-induced document reranking. Our CLIR participation involved both the French and English queries and included experiments with the merging strategy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FranzMW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FranzMW99,
		author = {Martin Franz and J. Scott McCarley and Todd Ward},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ad hoc, Cross-language and Spoken Document Information Retrieval at {IBM}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/t8\_ibm\_hlt.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FranzMW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-8

_James Allan, James P. Callan, Fangfang Feng, Daniella Malin_

- :fontawesome-solid-user-group: **Participant:** [umass](./sdr/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf)
- :material-file-search: **Runs:** [umass-r1](./sdr/runs.md#umass-r1) | [umass-b1](./sdr/runs.md#umass-b1)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CI IR) at the University of Massachusetts participated in seven of the tracks: ad-ho c, ltering, sp oken do cument retrieval, small web, large web, question and answer, and the query tracks. We sp ent signi cant time working on the ltering track, resulting in substantial p erformance improvement over TREC-7. For all of the other tracks, we used essentially the same system as used in previous years. In the next section, we describ e some of the basic pro cessing that was applied across most of the tracks. We then describe the details for each of the tracks and in some cases present some mo dest analysis of the e ectiveness of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCFM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCFM99,
		author = {James Allan and James P. Callan and Fangfang Feng and Daniella Malin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCFM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The THISL SDR System At TREC-8

_Dave Abberley, Steve Renals, Dan Ellis, Anthony J. Robinson_

- :fontawesome-solid-user-group: **Participant:** [thisl](./sdr/participants.md#thisl)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/shef-proc-trec8.pdf](http://trec.nist.gov/pubs/trec8/papers/shef-proc-trec8.pdf)
- :material-file-search: **Runs:** [shef-r1](./sdr/runs.md#shef-r1) | [shef-b1](./sdr/runs.md#shef-b1) | [shef-b1u](./sdr/runs.md#shef-b1u) | [shef-s1](./sdr/runs.md#shef-s1) | [shef-s1u](./sdr/runs.md#shef-s1u) | [shef-cr-att-s1](./sdr/runs.md#shef-cr-att-s1) | [shef-cr-cmu-s1](./sdr/runs.md#shef-cr-cmu-s1) | [shef-cr-cuhtk-s1](./sdr/runs.md#shef-cr-cuhtk-s1) | [shef-cr-cuhtk-s1p1](./sdr/runs.md#shef-cr-cuhtk-s1p1) | [shef-cr-limsi-s1](./sdr/runs.md#shef-cr-limsi-s1) | [shef-cr-nist-b2](./sdr/runs.md#shef-cr-nist-b2) | [shef-cru-cuhtk-s1p1u](./sdr/runs.md#shef-cru-cuhtk-s1p1u) | [shef-cru-limsi-s1u](./sdr/runs.md#shef-cru-limsi-s1u) | [shef-cru-cuhtk-s1u](./sdr/runs.md#shef-cru-cuhtk-s1u) | [shef-cru-nist-b2u](./sdr/runs.md#shef-cru-nist-b2u)

??? abstract "Abstract"
	
	This paper describes the participation of the THISL group at the TREC-8 Spoken Document Retrieval (SDR) track. The THISL SDR system consists of the realtime version of the A BBOT large vocabulary speech recognition system and the THISL IR text retrieval system. The TREC-8 evaluation assessed SDR performance on a corpus of 500 hours of broadcast news material collected over a five month period. The main test condition involved retrieval of stories defined by manual segmentation of the corpus in which non-news material, such as commercials, were excluded. An optional test condition required required retrieval of the same stories from the unsegmented audio stream. The THISL SDR system participated at both test conditions. The results show that a system such as THISL can produce respectable information retrieval performance on a realistically-sized corpus of unsegmented audio material.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbberleyRER99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbberleyRER99,
		author = {Dave Abberley and Steve Renals and Dan Ellis and Anthony J. Robinson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {THISL} {SDR} System At {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/shef-proc-trec8.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbberleyRER99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Cross-Language 

#### Cross-Language Information Retrieval (CLIR) Track Overview

_Martin Braschler, Peter Schäuble, Carol Peters_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8ov.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8ov.pdf)
??? abstract "Abstract"
	
	A cross-language retrieval track was offered for the third time at TREC-8. The main task was the same as that of the previous year: the goal was for groups to use queries written in a single language in order to retrieve documents from a multilingual pool of documents written in many different languages. Compared to the usual definition of cross-language information retrieval, where systems work with a single language pair, retrieving documents in a language L1 using queries in language L2, this is a slightly more comprehensive task, and we feel one that more closely meets the demands of real world applications. The document languages used were the same as for TREC-7: English, German, French and Italian. The queries were available in all of these languages. Monolingual non-English retrieval was offered to new participants who preferred to begin with an easier task. However, all the groups which did not tackle the full task opted for limited cross-language rather than monolingual runs. These experiments were evaluated by NIST and are published as unofficial ('alternate') runs. We also offered a subtask, working with documents from the field of social sciences. This collection (known as 'GIRT') has some very interesting features, such as controlled vocabulary terms, title translations, and an associated multilingual thesaurus. The track was coordinated at Eurospider Information Technology AG in Zurich. Due to its multilingual nature, the topic creation and relevance assessment tasks were distributed over four sites in different countries: NIST (English), IZ Bonn (German), IEI-CNR (Italian) and University of Zurich (French). The University of Hildesheim invested considerable effort into rendering the topics homogeneous and consistent over languages. The participating groups experimented with a wide variety of strategies, ranging machine translation, corpus-, and dictionary-based approaches. Some results are given in Section 4. There were, however, also some striking similarities between many of the runs, such as the choice of English as topic language the majority, and the use of Systran by a lot of groups. Some implications of these findings are discussed in Section 5. The main goal of the TREC CLIR activities has been the creation of a multilingual test collection that is re-usable for a wide range of evaluation experiments. This means that the quality of the relevance assessments is very important. The Twenty-One group conducted an interesting analysis with respect to the completeness of the assessments and the impact of this on the pool. We address some of their findings in Section 5. The paper concludes with an indication of our plans for the future of the cross-language track, which will bring substantial changes to the format and coordination of the activities.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BraschlerSP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BraschlerSP99,
		author = {Martin Braschler and Peter Sch{\"{a}}uble and Carol Peters},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Cross-Language Information Retrieval {(CLIR)} Track Overview},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8ov.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BraschlerSP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CINDOR Conceptual Interlingua Document Retrieval: TREC-8 Evaluation

_Miguel E. Ruiz, Anne Diekema, Paraic Sheridan_

- :fontawesome-solid-user-group: **Participant:** [textwise](./xlingual/participants.md#textwise)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/TextWise.pdf](http://trec.nist.gov/pubs/trec8/papers/TextWise.pdf)
- :material-file-search: **Runs:** [TW8F2E](./xlingual/runs.md#tw8f2e) | [TW8E2F](./xlingual/runs.md#tw8e2f)

??? abstract "Abstract"
	
	The TREC-8 evaluation of the CINDOR system was based on English and French data from the cross-language retrieval track. Our objective was to continue our investigation of our conceptual interlingua approach to cross-language retrieval, specifically by measuring the contribution of conceptual retrieval over and above a baseline cross-language retrieval approach based on machine translation of queries. In both of the cross-language runs that were submitted for evaluation, corresponding to English-French and French-English retrieval, performance was measured at 75% of the equivalent monolingual searches. We noted however that absolute average precision values achieved were somewhat lower than many other systems in the cross-language track. Our hypothesis, that the underlying retrieval engine used in CINDOR was employing a simple retrieval function that was impacting performance, was confirmed through experiments with the SMART system configured with several different retrieval settings. Taken together, our TREC-8 experiments point to the value of our conceptual interlingua approach to retrieval, but indicate that our retrieval algorithm must be brought up to date so that valid comparisons may be made to other approaches used in other cross-language systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuizDS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuizDS99,
		author = {Miguel E. Ruiz and Anne Diekema and Paraic Sheridan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CINDOR} Conceptual Interlingua Document Retrieval: {TREC-8} Evaluation},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/TextWise.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuizDS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLARIT TREC-8 CLIR Experiments

_Yan Qu, Hongming Jin, Alla N. Eilerman, Emilia Stoica, David A. Evans_

- :fontawesome-solid-user-group: **Participant:** [claritech](./xlingual/participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/CLARIT_CLIR.pdf](http://trec.nist.gov/pubs/trec8/papers/CLARIT_CLIR.pdf)
- :material-file-search: **Runs:** [CLARITrmwf1](./xlingual/runs.md#claritrmwf1) | [CLARITrmwf2](./xlingual/runs.md#claritrmwf2) | [CLARITrmwf3](./xlingual/runs.md#claritrmwf3) | [CLARITdmwf](./xlingual/runs.md#claritdmwf)

??? abstract "Abstract"
	
	In the TREC-8 cross-language information retrieval (CLIR) track, we adopted the approach of using machine translation to prepare a source-language query for use in a target-language retrieval task. We empirically evaluated (1) the effect of pseudo relevance feedback on retrieval performance with two feedback vector length control methods in CLIR and (2) the effect of multilingual data merging either before or after retrieval. Our experiments show that, in general, pseudo relevance feedback significantly improves cross-language retrieval performance, and that post-retrieval merging of retrieval results can outperform pre-retrieval merging of multilingual data collections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QuJESE99.bib) "
	```
	@inproceedings{DBLP:conf/trec/QuJESE99,
		author = {Yan Qu and Hongming Jin and Alla N. Eilerman and Emilia Stoica and David A. Evans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CLARIT} {TREC-8} {CLIR} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/CLARIT\_CLIR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QuJESE99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CRL's TREC-8 Systems Cross-Lingual IR, and Q&A

_William C. Ogden, James R. Cowie, Yevgeny Ludovik, Hugo Molina-Salgado, Sergei Nirenburg, Nigel Sharples, Svetlana O. Sheremetyeva_

- :fontawesome-solid-user-group: **Participant:** [nmsu](./xlingual/participants.md#nmsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/crl_proceedings.pdf](http://trec.nist.gov/pubs/trec8/papers/crl_proceedings.pdf)
- :material-file-search: **Runs:** [nmsui1](./xlingual/runs.md#nmsui1)

??? abstract "Abstract"
	
	This paper describes the systems used by CRL in the Cross-lingual IR and Q&A tracks. The cross-language experiment was unique in that it was run interactively with a mono-lingual user simulating how a true cross-language system might be used. The methods used in the Q&A system are based on language processing technology developed at CRL for machine translation and information extraction.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OgdenCLMNSS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/OgdenCLMNSS99,
		author = {William C. Ogden and James R. Cowie and Yevgeny Ludovik and Hugo Molina{-}Salgado and Sergei Nirenburg and Nigel Sharples and Svetlana O. Sheremetyeva},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {CRL's {TREC-8} Systems Cross-Lingual IR, and Q{\&}A},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/crl\_proceedings.pdf},
		timestamp = {Thu, 17 Nov 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OgdenCLMNSS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Experiments at Maryland: CLIR, QA and Routing

_Douglas W. Oard, Jianqiang Wang, Dekang Lin, Ian Soboroff_

- :fontawesome-solid-user-group: **Participant:** [umd](./xlingual/participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf](http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf)
- :material-file-search: **Runs:** [umd99b1](./xlingual/runs.md#umd99b1) | [umd99b2](./xlingual/runs.md#umd99b2) | [umd99b3](./xlingual/runs.md#umd99b3) | [umd99c1](./xlingual/runs.md#umd99c1) | [umd99c2](./xlingual/runs.md#umd99c2)

??? abstract "Abstract"
	
	The University of Maryland team participated in four aspects of TREC-8: the ad hoc retrieval task, the main task in the cross-language retrieval (CLIR) track, the question answering track, and the routing task in the filtering track. The CLIR method was based on Pirkola's method for Dictionary-based Query Translation, using freely available dictionaries. Broad-coverage parsing and rule-based matching was used for question answering. Routing was performed using Latent Semantic Indexing in profile space.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardWLS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardWLS99,
		author = {Douglas W. Oard and Jianqiang Wang and Dekang Lin and Ian Soboroff},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Experiments at Maryland: CLIR, {QA} and Routing},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OardWLS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLIR using a Probabilistic Translation Model based on Web Documents

_Jian-Yun Nie_

- :fontawesome-solid-user-group: **Participant:** [montreal](./xlingual/participants.md#montreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/TREC8-Nie.pdf](http://trec.nist.gov/pubs/trec8/papers/TREC8-Nie.pdf)
- :material-file-search: **Runs:** [RaliWebE2EF](./xlingual/runs.md#raliwebe2ef) | [RaliWebF2EF](./xlingual/runs.md#raliwebf2ef) | [RaliHanE2EF](./xlingual/runs.md#ralihane2ef) | [RaliHanF2EF](./xlingual/runs.md#ralihanf2ef)

??? abstract "Abstract"
	
	In this report, we describe the approach we used in TREC-8 Cross-Language IR (CLIR) track. The approach is based on probabilistic translation models estimated from two parallel training corpora: one established manually, and the other built automatically with the documents mined from the Web. We describe the principle of model building, the mining of parallel texts, as well as some preliminary evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Nie99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Nie99,
		author = {Jian{-}Yun Nie},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CLIR} using a Probabilistic Translation Model based on Web Documents},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/TREC8-Nie.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Nie99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Twenty-One at TREC-8: using Language Technology for Information  Retrieval

_Wessel Kraaij, Renée Pohlmann, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [twentyone](./xlingual/participants.md#twentyone)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf](http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf)
- :material-file-search: **Runs:** [tno8dis](./xlingual/runs.md#tno8dis) | [tno8gr](./xlingual/runs.md#tno8gr) | [tno8mx](./xlingual/runs.md#tno8mx) | [tno8dpx](./xlingual/runs.md#tno8dpx)

??? abstract "Abstract"
	
	This paper describes the official runs of the Twenty-One group for TREC-8. The Twenty-One group participated in the Ad-hoc, CLIR, Adaptive Filtering and SDR tracks. The main focus of our experiments is the development and evaluation of retrieval methods that are motivated by natural language processing techniques. The following new techniques are introduced in this paper. In the Ad-Hoc and CLIR tasks we experimented with automatic sense disambiguation followed by query expansion or translation. We used a combination of thesaurial and corpus information for the disambiguation process. We continued research on CLIR techniques which exploit the target corpus for an implicit disambiguation, by importing the translation probabilities into the probabilistic term-weighting framework. In filtering we extended the the use of language models for document ranking with a relevance feedback algorithm for query term reweighting.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KraaijPH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/KraaijPH99,
		author = {Wessel Kraaij and Ren{\'{e}}e Pohlmann and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Twenty-One at {TREC-8:} using Language Technology for Information Retrieval},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KraaijPH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc, Cross-language and Spoken Document Information Retrieval at  IBM

_Martin Franz, J. Scott McCarley, Todd Ward_

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./xlingual/participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/t8_ibm_hlt.pdf](http://trec.nist.gov/pubs/trec8/papers/t8_ibm_hlt.pdf)
- :material-file-search: **Runs:** [ibmcl8ea](./xlingual/runs.md#ibmcl8ea) | [ibmcl8fa](./xlingual/runs.md#ibmcl8fa) | [ibmcl8fc](./xlingual/runs.md#ibmcl8fc) | [ibmcl8ec](./xlingual/runs.md#ibmcl8ec)

??? abstract "Abstract"
	
	The Natural Language Systems group at IBM participated in three tracks at TREC-8: ad hoc, SDR and cross-language. Our SDR and ad hoc participation included experiments involving query expansion and clustering-induced document reranking. Our CLIR participation involved both the French and English queries and included experiments with the merging strategy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FranzMW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FranzMW99,
		author = {Martin Franz and J. Scott McCarley and Todd Ward},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ad hoc, Cross-language and Spoken Document Information Retrieval at {IBM}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/t8\_ibm\_hlt.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FranzMW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Eurospider Retrieval System and the TREC-8 Cross-Language Track

_Martin Braschler, Min-Yen Kan, Peter Schäuble, Judith Klavans_

- :fontawesome-solid-user-group: **Participant:** [eurospider](./xlingual/participants.md#eurospider)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/eit_t8f.pdf](http://trec.nist.gov/pubs/trec8/papers/eit_t8f.pdf)
- :material-file-search: **Runs:** [EIT99mta](./xlingual/runs.md#eit99mta) | [EIT99sta](./xlingual/runs.md#eit99sta) | [EIT99sal](./xlingual/runs.md#eit99sal)

??? abstract "Abstract"
	
	This year the Eurospider team, with help from Columbia, focused on trying different combinations of translation approaches. We investigated the use and integration of pseudo-relevance feedback, multilingual similarity thesauri and machine translation. We also looked at different ways of merging individual cross-language retrieval runs to produce multilingual result lists. We participated in both the CLIR main task and the GIRT sub task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BraschlerKSK99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BraschlerKSK99,
		author = {Martin Braschler and Min{-}Yen Kan and Peter Sch{\"{a}}uble and Judith Klavans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Eurospider Retrieval System and the {TREC-8} Cross-Language Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/eit\_t8f.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BraschlerKSK99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at trec8: Adhoc, Web, CLIR and Filtering tasks

_Mohand Boughanem, Christine Julien, Josiane Mothe, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [irit](./xlingual/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/irit.pdf](http://trec.nist.gov/pubs/trec8/papers/irit.pdf)
- :material-file-search: **Runs:** [Mer8Can2x](./xlingual/runs.md#mer8can2x) | [Mer8Cfr2x](./xlingual/runs.md#mer8cfr2x) | [Mer8Can2x0](./xlingual/runs.md#mer8can2x0)

??? abstract "Abstract"
	
	Three runs were submitted for our first participation in this track. All these runs were based on query translation using an online machine translation . Two of these runs are a comparison between query translation from English to other languages and from French to other languages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemJMS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemJMS99,
		author = {Mohand Boughanem and Christine Julien and Josiane Mothe and Chantal Soul{\'{e}}{-}Dupuy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure at trec8: Adhoc, Web, {CLIR} and Filtering tasks},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/irit.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemJMS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## GIRT 

#### English-German Cross-Language Retrieval for the GIRT Collection  - Exploiting a Multilingual Thesaurus

_Fredric C. Gey, Hailing Jiang_

- :fontawesome-solid-user-group: **Participant:** [berkeley_gey](./girt/participants.md#berkeley_gey)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/Berkeley-GIRT-trec8.pdf](http://trec.nist.gov/pubs/trec8/papers/Berkeley-GIRT-trec8.pdf)
- :material-file-search: **Runs:** [BKCLGR01](./girt/runs.md#bkclgr01) | [BKCLGR02](./girt/runs.md#bkclgr02) | [BKCLGR03](./girt/runs.md#bkclgr03) | [BKCLGR04](./girt/runs.md#bkclgr04) | [BKCLGR05](./girt/runs.md#bkclgr05)

??? abstract "Abstract"
	
	For TREC-8, the Berkeley exp eriments concentrated on the sp ecial GIRT collection. We utilized the GIRT thesaurus in multiple ways in working on English-German Cross-Language IR. Since the GIRT collection is truly multilingual (documents contain b oth German and English text), one would exp ect multilingual queries to achieve the b est p erformance. This proved not to b e the case.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyJ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyJ99,
		author = {Fredric C. Gey and Hailing Jiang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {English-German Cross-Language Retrieval for the {GIRT} Collection - Exploiting a Multilingual Thesaurus},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/Berkeley-GIRT-trec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GeyJ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Interactive 

#### TREC-8 Interactive Track Report

_William R. Hersh, Paul Over_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/t8irep.pdf](http://trec.nist.gov/pubs/trec8/papers/t8irep.pdf)
??? abstract "Abstract"
	
	This report is an introduction to the work of the TREC-8 Interactive Track with its goal of investigating interactive information retrieval by examining the process as well as the results. Seven research groups ran a total of 14 interactive information retrieval (IR) system variants on a shared problem: a question-answering task, six statements of information need, and a collection of 210,158 articles from the Financial Times of London 1991-1994. This report summarizes the shared experimental framework, which for TREC-8 was designed to support analysis and comparison of system performance only within sites. The report refers the reader to separate discussions of the experiments performed by each participating group - their hypotheses, experimental systems, and results. The papers from each of the participating groups and the raw and evaluated results are available via the TREC home page (trec.nist.gov).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershO99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershO99,
		author = {William R. Hersh and Paul Over},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Interactive Track Report},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/t8irep.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershO99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIS at TREC-8

_Kiduk Yang, Kelly Maglaughlin_

- :fontawesome-solid-user-group: **Participant:** [UNC](./interactive/participants.md#unc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/unc_tr8final.pdf](http://trec.nist.gov/pubs/trec8/papers/unc_tr8final.pdf)
- :material-file-search: **Runs:** [unci](./interactive/runs.md#unci)

??? abstract "Abstract"
	
	We tested two relevance feedback models, an adaptive linear model and a probabilistic model, using massive feedback query expansion in TREC-5 (Sumner & Shaw, 1997), experimented with a three-valued scale of relevance and reduced feedback query expansion in TREC-6 (Sumner, Yang, Akers & Shaw, 1998), and examined the effectiveness of relevance feedback using a subcollection and the effect of system features in an interactive retrieval system called IRIS (Information Retrieval Interactive System1 ) in TREC-7 (Yang, Maglaughlin, Mehol & Sumner, 1999). In TREC-8, we continued our exploration of relevance feedback approaches. Based on the result of our TREC-7 interactive experiment, which suggested relevance feedback using user-selected passages to be an effective alternative to conventional document feedback, our TREC-8 interactive experiment compared a passage feedback system and a document feedback system that were identical in all aspects except for the feedback mechanism. For the TREC-8 ad-hoc task, we merged results of pseudo-relevance feedback to subcollections as in TREC-7. Our results were consistent with that of TREC-7. The results of passage feedback, whose system log showed high level of searcher intervention, was superior to the document feedback results. As in TREC-7, our ad-hoc results showed high precision in top few documents, but performed poorly overall compared to results using the collection as a whole.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangM99,
		author = {Kiduk Yang and Kelly Maglaughlin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{IRIS} at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/unc\_tr8final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Berkeley's TREC 8 Interactive Track Entry: Cheshire II and Zprise

_Ray R. Larson_

- :fontawesome-solid-user-group: **Participant:** [berkeley_gey](./interactive/participants.md#berkeley_gey)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/berkeley-interactive.pdf](http://trec.nist.gov/pubs/trec8/papers/berkeley-interactive.pdf)
- :material-file-search: **Runs:** [berki](./interactive/runs.md#berki)

??? abstract "Abstract"
	
	This paper briefly discusses the UC Berkeley entry in the TREC8 Interactive Track. In this year’s study twelve searchers conducted six searches each, half on the Cheshire II system and the other half on the Zprise system, for a total of 72 searches. Questionnaires were administered to each participant to gather information about basic demographic and searching experience, about each search, about each of the systems, and finally, about the user’s perceptions of the systems. In this paper I will briefly describe the systems used in the study and how they differ in design goals and implementation. The results of the interactive track evaluations and the information derived from the questionnaires are then discussed and future improvements to the Cheshire II system are considered.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Larson99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Larson99,
		author = {Ray R. Larson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Berkeley's {TREC} 8 Interactive Track Entry: Cheshire {II} and Zprise},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/berkeley-interactive.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Larson99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Do Batch and User Evaluations Give the Same Results? An Analysis from  the TREC-8 Interactive Track

_William R. Hersh, Andrew Turpin, Susan Price, Dale Kraemer, Benjamin Chan, Lynetta Sacherek, Daniel Olson_

- :fontawesome-solid-user-group: **Participant:** [OHSU](./interactive/participants.md#ohsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/hersh.pdf](http://trec.nist.gov/pubs/trec8/papers/hersh.pdf)
- :material-file-search: **Runs:** [ohsui](./interactive/runs.md#ohsui)

??? abstract "Abstract"
	
	An unanswered question in information retrieval research is whether improvements in system performance demonstrated by batch evaluations confer the same benefit for real users. We used the TREC-8 Interactive Track to investigate this question. After identifying a weighting scheme that gave maximum improvement over the baseline, we used it with real users searching on an instance recall task. Our results showed no improvement; although there was overall average improvement comparable to the batch results, it was not statistically significant and due to the effect of just one out of the six queries. Further analysis with more queries is necessary to resolve this question.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershTPKCSO99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershTPKCSO99,
		author = {William R. Hersh and Andrew Turpin and Susan Price and Dale Kraemer and Benjamin Chan and Lynetta Sacherek and Daniel Olson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Do Batch and User Evaluations Give the Same Results? An Analysis from the {TREC-8} Interactive Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/hersh.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershTPKCSO99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Okapi at Sheffield - TREC-8

_Micheline Hancock-Beaulieu, Helene Fowkes, Nega Alemayehu, Mark Sanderson_

- :fontawesome-solid-user-group: **Participant:** [sheffield](./interactive/participants.md#sheffield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/shef8.pdf](http://trec.nist.gov/pubs/trec8/papers/shef8.pdf)
- :material-file-search: **Runs:** [shefi](./interactive/runs.md#shefi)

??? abstract "Abstract"
	
	The focus of the study was to examine searching behaviour in relation to the three experimental variables, i.e. searcher, system and topic characteristics. Twenty-four subjects searched the six test topics on two versions of the Okapi system, one with relevance feedback and one without. A combination of data collection methods was used including observations, verbal protocols, transaction logs, questionnaires and structured post-search interviews. Search analysis indicates that searching behaviour was largely dependent on topic characteristics. Two types of topics and associated search tasks were identified. Overall best match ranking led to high precision searches and those which included relevance feedback were marginally but not significantly better. The study raises methodological questions with regard to the specification of interactive searching tasks and topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Hancock-BeaulieuFAS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Hancock-BeaulieuFAS99,
		author = {Micheline Hancock{-}Beaulieu and Helene Fowkes and Nega Alemayehu and Mark Sanderson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Interactive Okapi at Sheffield - {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/shef8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Hancock-BeaulieuFAS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The RMIT/CSIRO Ad Hoc, Q&A, Web, Interactive, and Speech Experiments  at TREC 8

_Michael Fuller, Marcin Kaszkiel, Sam Kimberley, Corinna Ng, Ross Wilkinson, Mingfang Wu, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [rmit](./interactive/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf](http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf)
- :material-file-search: **Runs:** [rmiti](./interactive/runs.md#rmiti)

??? abstract "Abstract"
	
	In TRECT, we tested using clustering technology to organize retrieved documents for aspectual retrieval, but did not find a significant gain for the clustering interface over a ranked list interface. This year, we investigated a question-driven categorization. Unlike the clustering approach, which was data-driven and attempted to discover and present topic relationships that existed in a set of retrieved documents without taking users into account, the question-driven approach tries to organize retrieved documents in a way that is close to the users' mental representation of the expected answer. In our approach, the retrieved documents are categorized dynamically into a set of categories derived from the user's question. The user determines which of several possible sets of categories should be used to organize retrieved documents. Our participation in TREC-8 was to investigate and compare the effectiveness and usability of this question-driven classification with a ranked list model. In the following sections we present a rationale for the question-driven approach, and then describe an experiment that compares this approach with a more traditional ranked list presentation. We then report and analyze the results of this experiment. Based on these findings and discussions, we conclude with some recommendations for future improvement.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FullerKKNWWZ99,
		author = {Michael Fuller and Marcin Kaszkiel and Sam Kimberley and Corinna Ng and Ross Wilkinson and Mingfang Wu and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {RMIT/CSIRO} Ad Hoc, Q{\&}A, Web, Interactive, and Speech Experiments at {TREC} 8},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Relevance Feedback versus Local Context Analysis as Term Suggestion  Devices: Rutgers' TREC-8 Interactive Track Experience

_Nicholas J. Belkin, Colleen Cool, J. Head, J. Jeng, Diane Kelly, Shin-jeng Lin, L. Lobash, Soyeon Park, Pamela A. Savage-Knepshield, C. Sikora_

- :fontawesome-solid-user-group: **Participant:** [rutgersb](./interactive/participants.md#rutgersb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ruint.pdf](http://trec.nist.gov/pubs/trec8/papers/ruint.pdf)
- :material-file-search: **Runs:** [ruti](./interactive/runs.md#ruti)

??? abstract "Abstract"
	
	Query formulation and reformulation is recognized as one of the most difficult tasks that users in information retrieval systems are asked to perform. This study investigated the use of two different techniques for supporting query reformulation in interactive information retrieval: relevance feedback and Local Context Analysis, both implemented as term−suggestion devices. The former represents techniques which offer user control and understanding of term suggestion; the latter represents techniques which require relatively little user effort. Using the TREC−8 Interactive Track task and experimental protocol, we found that although there were no significant differences between two systems implementing these techniques in terms of user preference and performance in the task, subjects using the Local Context Analysis system had significantly fewer user−defined query terms than those in the relevance feedback system. We conclude that term suggestion without user guidance/control is the better of the two methods tested, for this task, since it required less effort for the same level of performance. We also found that both number of documents saved and number of instances identified by subjects were significantly correlated with the criterion measures of instance recall and precision, and conclude that this suggests that it is not necessary to rely on external evaluators for measurement of performance of interactive information retrieval in the instance identification task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinCHJKLLPSS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinCHJKLLPSS99,
		author = {Nicholas J. Belkin and Colleen Cool and J. Head and J. Jeng and Diane Kelly and Shin{-}jeng Lin and L. Lobash and Soyeon Park and Pamela A. Savage{-}Knepshield and C. Sikora},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Relevance Feedback \emph{versus} Local Context Analysis as Term Suggestion Devices: Rutgers' {TREC-8} Interactive Track Experience},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ruint.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BelkinCHJKLLPSS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

