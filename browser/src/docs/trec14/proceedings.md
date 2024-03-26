# Proceedings 2005 

## Overview of TREC 2005

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/OVERVIEW14.pdf](http://trec.nist.gov/pubs/trec14/papers/OVERVIEW14.pdf)
??? abstract "Abstract"
	
	The fourteenth Text REtrieval Conference, TREC 2005, was held at the National Institute of Standards and Technology (NIST) 15 to 18 November 2005. The conference was co-sponsored by NIST and the US Department of Defense Advanced Research and Development Activity (ARDA). TREC 2005 had 117 participating groups from 23 different countries. Table 2 at the end of the paper lists the participating groups. TREC 2005 is the latest in a series of workshops designed to foster research on technologies for information retrieval. The workshop series has four goals: to encourage retrieval research based on large test collections; to increase communication among industry, academia, and government by creating an open forum for the exchange of research ideas; to speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems; and to increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current systems. TREC 2005 contained seven areas of focus called “tracks”. Two tracks focused on improving basic retrieval effectiveness by either providing more context or by trying to reduce the number of queries that fail. Other tracks explored tasks in question answering, detecting spam in an email stream, enterprise search, search on (almost) terabyte-scale document sets, and information access within the genomics domain. The specific tasks performed in each of the tracks are summarized in Section 3 below. This paper serves as an introduction to the research described in detail in the remainder of the proceedings. The next section provides a summary of the retrieval background knowledge that is assumed in the other papers. Section 3 presents a short description of each track—a more complete description of a track can be found in that track's overview paper in the proceedings. The final section looks toward future TREC conferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees05.bib)"
	```
	@inproceedings{DBLP:conf/trec/Voorhees05,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/OVERVIEW14.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Spam 

#### TREC 2005 Spam Track Overview

_Gordon V. Cormack, Thomas R. Lynam_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/SPAM.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/SPAM.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The robust retrieval track explores methods for improving the consistency of retrieval technology by focusing on poorly performing topics. The retrieval task in the track is a traditional ad hoc retrieval task where the evaluation methodology emphasizes a system's least effective topics. The 2005 edition of the track used 50 topics that had been demonstrated to be difficult on one document collection, and ran those topics on a different document collection. Relevance information from the first collection could be exploited in producing a query for the second collection, if desired. The main measure for evaluating system effectiveness is “gmap”, a variant of the traditional MAP measure that uses a geometric mean rather than an arithmetic mean to average individual topic results. As in previous years, the most effective retrieval strategy was to expand queries using terms derived from additional corpora. The relative difficulty of topics differed across the two document sets. Systems were also required to rank the topics by predicted difficulty. This task is motivated by the hope that systems will eventually be able to use such predictions to do topic-specific processing. This remains a challenging task. Since difficulty depends on more then the topic set alone, prediction methods that train on data from other test collections do not generalize well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackL05,
		author = {Gordon V. Cormack and Thomas R. Lynam},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Spam Track Overview},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/SPAM.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CRM114 versus Mr. X: CRM114 Notes for the TREC 2005 Spam Track

_Fidelis Assis, William S. Yerazunis, Christian Siefkes, Shalendra Chhabra_

- :fontawesome-solid-user-group: **Participant:** [merl.yerazunis](./spam/participants.md#merl.yerazunis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/crm.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/crm.spam.pdf)
- :material-file-search: **Runs:** [crmSPAMp2wi](./spam/runs.md#crmspamp2wi) | [crmSPAMp1of](./spam/runs.md#crmspamp1of) | [crmSPAM2win](./spam/runs.md#crmspam2win) | [crmSPAM4osb](./spam/runs.md#crmspam4osb) | [crmSPAM1osf](./spam/runs.md#crmspam1osf) | [crmSPAM3osu](./spam/runs.md#crmspam3osu) | [crmSPAM2full](./spam/runs.md#crmspam2full) | [crmSPAM2ham2](./spam/runs.md#crmspam2ham2) | [crmSPAM2ham5](./spam/runs.md#crmspam2ham5) | [crmSPAM2spm2](./spam/runs.md#crmspam2spm2) | [crmSPAM2spm5](./spam/runs.md#crmspam2spm5) | [crmSPAM4full](./spam/runs.md#crmspam4full) | [crmSPAM3full](./spam/runs.md#crmspam3full) | [crmSPAM1full](./spam/runs.md#crmspam1full) | [crmSPAM1ham2](./spam/runs.md#crmspam1ham2) | [crmSPAM1ham5](./spam/runs.md#crmspam1ham5) | [crmSPAM1spm5](./spam/runs.md#crmspam1spm5) | [crmSPAM1spm2](./spam/runs.md#crmspam1spm2) | [crmSPAM3ham2](./spam/runs.md#crmspam3ham2) | [crmSPAM3ham5](./spam/runs.md#crmspam3ham5) | [crmSPAM3spm2](./spam/runs.md#crmspam3spm2) | [crmSPAM3spm5](./spam/runs.md#crmspam3spm5) | [crmSPAM4ham2](./spam/runs.md#crmspam4ham2) | [crmSPAM4ham5](./spam/runs.md#crmspam4ham5) | [crmSPAM4spm2](./spam/runs.md#crmspam4spm2) | [crmSPAM4spm5](./spam/runs.md#crmspam4spm5)

??? abstract "Abstract"
	
	This paper discusses the design decisions underlying the CRM114 Discriminator software, how it can be configured as a spam filter, and what we may glean from the preliminary TREC 2005 results. Unlike most other filters, CRM114 is not a fixedpurpos e antis pam filter; rather, it's a general purpose language meant to expedite the creation of text filters. The pluggable CRM114 architecture allows rapid prototyping and easy support of multiple classifier engines; rather than testing different cutoff parameters, the CRM114 TREC test set tested different classifier algorithms and learning protocols.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AssisYSC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AssisYSC05,
		author = {Fidelis Assis and William S. Yerazunis and Christian Siefkes and Shalendra Chhabra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CRM114} versus Mr. {X:} {CRM114} Notes for the {TREC} 2005 Spam Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/crm.spam.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AssisYSC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DBACL at the TREC 2005

_L. A. Breyer_

- :fontawesome-solid-user-group: **Participant:** [breyer.laird](./spam/participants.md#breyer.laird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/breyer.laird-spam.ps](http://trec.nist.gov/pubs/trec14/papers/breyer.laird-spam.ps)
- :material-file-search: **Runs:** [p1cefhuj](./spam/runs.md#p1cefhuj) | [p2adphu](./spam/runs.md#p2adphu) | [p3adphd](./spam/runs.md#p3adphd) | [p4adp](./spam/runs.md#p4adp) | [1cefhuj](./spam/runs.md#1cefhuj) | [2adphu](./spam/runs.md#2adphu) | [3adphd](./spam/runs.md#3adphd) | [4adp](./spam/runs.md#4adp) | [pub1full](./spam/runs.md#pub1full) | [pub1ham50](./spam/runs.md#pub1ham50) | [pub1spam50](./spam/runs.md#pub1spam50) | [pub2full](./spam/runs.md#pub2full) | [pub4full](./spam/runs.md#pub4full) | [pub3full](./spam/runs.md#pub3full)

??? abstract "Abstract"
	
	The dbacl classifier is an open source command line tool which performs spam classification based on simple maximum entropy models; dbacl learns each class separately, and individual categories can be mixed and matched for classification. Here we present the simulation results obtained for TREC 2005, with an empirical comparison of several feature extraction methods. We also try to gain insight into their different performance characteristics, with limited success.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Breyer05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Breyer05,
		author = {L. A. Breyer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DBACL} at the {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/breyer.laird-spam.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Breyer05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Spam Filtering Using Character-Level Markov Models: Experiments for  the TREC 2005 Spam Track

_Andrej Bratko, Bogdan Filipic_

- :fontawesome-solid-user-group: **Participant:** [jozef-stefan-inst.bratko](./spam/participants.md#jozef-stefan-inst.bratko)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/jozef-stefan.bratko.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/jozef-stefan.bratko.spam.pdf)
- :material-file-search: **Runs:** [ijsSPAM1pm1](./spam/runs.md#ijsspam1pm1) | [ijsSPAM2cw1](./spam/runs.md#ijsspam2cw1) | [ijsSPAM3pm2](./spam/runs.md#ijsspam3pm2) | [ijsSPAM3cw2](./spam/runs.md#ijsspam3cw2) | [ijsSPAM4cw2](./spam/runs.md#ijsspam4cw2) | [ijsSPAM1pm8](./spam/runs.md#ijsspam1pm8) | [ijsSPAM2pm6](./spam/runs.md#ijsspam2pm6) | [ijsSPAM3pm4](./spam/runs.md#ijsspam3pm4) | [ijsSPAM4cw8](./spam/runs.md#ijsspam4cw8) | [ijsSPAM1full](./spam/runs.md#ijsspam1full) | [ijsSPAM2full](./spam/runs.md#ijsspam2full) | [ijsSPAM3full](./spam/runs.md#ijsspam3full) | [ijsSPAM4full](./spam/runs.md#ijsspam4full) | [ijsSPAM1h25](./spam/runs.md#ijsspam1h25) | [ijsSPAM2h25](./spam/runs.md#ijsspam2h25) | [ijsSPAM3h25](./spam/runs.md#ijsspam3h25) | [ijsSPAM4h25](./spam/runs.md#ijsspam4h25)

??? abstract "Abstract"
	
	This paper summarizes our participation in the TREC 2005 spam track, in which we consider the use of adaptive statistical data compression models for the spam filtering task. The nature of these models allows them to be employed as Bayesian text classifiers based on character sequences. We experimented with two different compression algorithms under varying model parameters. All four filters that we submitted exhibited strong performance in the official evaluation, indicating that data compression models are well suited to the spam filtering problem.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BratkoF05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BratkoF05,
		author = {Andrej Bratko and Bogdan Filipic},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Spam Filtering Using Character-Level Markov Models: Experiments for the {TREC} 2005 Spam Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/jozef-stefan.bratko.spam.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BratkoF05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2005: SPAM Track

_Wei Cao, Aijun An, Xiangji Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./spam/participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/yorku-huang.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/yorku-huang.spam.pdf)
- :material-file-search: **Runs:** [yorSPAMpknn](./spam/runs.md#yorspampknn) | [yorSPAM1knf](./spam/runs.md#yorspam1knf) | [cao1knf](./spam/runs.md#cao1knf) | [yorSPAM3knf](./spam/runs.md#yorspam3knf) | [cao3knf](./spam/runs.md#cao3knf) | [yorSPAM2ruk](./spam/runs.md#yorspam2ruk) | [cao2ruk](./spam/runs.md#cao2ruk) | [yorSPAM4hyb](./spam/runs.md#yorspam4hyb) | [cao4hyb](./spam/runs.md#cao4hyb) | [yorSPAM1full](./spam/runs.md#yorspam1full) | [yorSPAM1ham2](./spam/runs.md#yorspam1ham2) | [yorSPAM1ham5](./spam/runs.md#yorspam1ham5) | [yorSPAM1spa2](./spam/runs.md#yorspam1spa2) | [yorSPAM1spa5](./spam/runs.md#yorspam1spa5) | [yorSPAM2full](./spam/runs.md#yorspam2full) | [yorSPAM2ham2](./spam/runs.md#yorspam2ham2) | [yorSPAM2ham5](./spam/runs.md#yorspam2ham5) | [yorSPAM2spa2](./spam/runs.md#yorspam2spa2) | [yorSPAM2spa5](./spam/runs.md#yorspam2spa5) | [yorSPAM3full](./spam/runs.md#yorspam3full) | [yorSPAM3ham2](./spam/runs.md#yorspam3ham2) | [yorSPAM3ham5](./spam/runs.md#yorspam3ham5) | [yorSPAM3spa2](./spam/runs.md#yorspam3spa2) | [yorSPAM3spa5](./spam/runs.md#yorspam3spa5) | [yorSPAM4full](./spam/runs.md#yorspam4full) | [yorSPAM4ham2](./spam/runs.md#yorspam4ham2) | [yorSPAM4ham5](./spam/runs.md#yorspam4ham5) | [yorSPAM4spa2](./spam/runs.md#yorspam4spa2) | [yorSPAM4spa5](./spam/runs.md#yorspam4spa5)

??? abstract "Abstract"
	
	We propose a variant of the k-nearest neighbor classification method, called instance-weighted k-nearest neighbor method, for adaptive spam filtering. The method assigns two weights, distance weight and correctness weight, to a training instance, and makes use of the two weights when classifying a new email. The correctness weight is also used in the maintenance of the training data to make the training data more adaptive to the changes of spam characteristics. We submitted 4 spam filters to the Spam Track. Two of the filters are purely based on the instance-weighted kNN method. The two other filters combine the kNN method with other spam filtering and classification techniques. We report the official results of our submissions on the Spam Track evaluation data sets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaoAH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaoAH05,
		author = {Wei Cao and Aijun An and Xiangji Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2005: {SPAM} Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/yorku-huang.spam.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CaoAH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DalTREC 2005 Spam Track: Spam Filtering Using N-gram-based Techniques

_Vlado Keselj, Evangelos E. Milios, Andrew Tuttle, Singer Wang, Roger Zhang_

- :fontawesome-solid-user-group: **Participant:** [dalhousieu.keselj](./spam/participants.md#dalhousieu.keselj)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dalhousieu.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/dalhousieu.spam.pdf)
- :material-file-search: **Runs:** [dalSPAM2vla](./spam/runs.md#dalspam2vla) | [dalSPAM3vla](./spam/runs.md#dalspam3vla) | [dalSPAM4sxw](./spam/runs.md#dalspam4sxw) | [dalSPAM1sxw](./spam/runs.md#dalspam1sxw) | [dalSPAM1fsw](./spam/runs.md#dalspam1fsw) | [dalSPAM4fsw](./spam/runs.md#dalspam4fsw) | [DalSPAM2n4](./spam/runs.md#dalspam2n4) | [DalSPAM3n5](./spam/runs.md#dalspam3n5) | [dalSPAM2h25](./spam/runs.md#dalspam2h25) | [dalSPAM2f](./spam/runs.md#dalspam2f) | [dalSPAM2h50](./spam/runs.md#dalspam2h50) | [dalSPAM2s25](./spam/runs.md#dalspam2s25) | [dalSPAM2s50](./spam/runs.md#dalspam2s50) | [dalSPAM3f](./spam/runs.md#dalspam3f) | [dalSPAM1sw1](./spam/runs.md#dalspam1sw1) | [dalSPAM4sw1](./spam/runs.md#dalspam4sw1) | [dalSPAM3h25](./spam/runs.md#dalspam3h25) | [dalSPAM3s50](./spam/runs.md#dalspam3s50) | [dalSPAM3s25](./spam/runs.md#dalspam3s25) | [dalSPAM3h50](./spam/runs.md#dalspam3h50) | [dalSPAM1sx2](./spam/runs.md#dalspam1sx2) | [dalSPAM4sx2](./spam/runs.md#dalspam4sx2)

??? abstract "Abstract"
	
	We briefly describe DalTREC 2005 Spam submission. DalTREC is the TREC research project at Dalhousie University. Four packages were submitted and they resulted in a median performance. The results are interesting and may be seen positive in the light of simplicity of our approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KeseljMTWZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KeseljMTWZ05,
		author = {Vlado Keselj and Evangelos E. Milios and Andrew Tuttle and Singer Wang and Roger Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {DalTREC 2005 Spam Track: Spam Filtering Using N-gram-based Techniques},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/dalhousieu.spam.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KeseljMTWZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A TREC Along the Spam Track with SpamBayes

_Tony Andrew Meyer_

- :fontawesome-solid-user-group: **Participant:** [masseyu.meyer](./spam/participants.md#masseyu.meyer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/masseyu.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/masseyu.spam.pdf)
- :material-file-search: **Runs:** [tamSPAMpplt](./spam/runs.md#tamspampplt) | [tamSPAM1dte](./spam/runs.md#tamspam1dte) | [tamSPAM2ber](./spam/runs.md#tamspam2ber) | [tamSPAM3bex](./spam/runs.md#tamspam3bex) | [tamSPAM4aex](./spam/runs.md#tamspam4aex) | [tamSPAM1h25](./spam/runs.md#tamspam1h25) | [tamSPAM2h25](./spam/runs.md#tamspam2h25) | [tamSPAM1h50](./spam/runs.md#tamspam1h50) | [tamSPAM2h50](./spam/runs.md#tamspam2h50) | [tamSPAM1s25](./spam/runs.md#tamspam1s25) | [tamSPAM2s25](./spam/runs.md#tamspam2s25) | [tamSPAM3s25](./spam/runs.md#tamspam3s25) | [tamSPAM1s50](./spam/runs.md#tamspam1s50) | [tamSPAM2s50](./spam/runs.md#tamspam2s50) | [tamSPAM1full](./spam/runs.md#tamspam1full) | [tamSPAM2full](./spam/runs.md#tamspam2full) | [tamSPAM3full](./spam/runs.md#tamspam3full)

??? abstract "Abstract"
	
	This paper describes the SpamBayes submissions made to the Spam Track of the 2005 Text Retrieval Conference (TREC). SpamBayes is briefly introduced, but the paper focuses more on how the submissions differ from the standard installation. Unlike in the majority of earlier publications evaluating the effectiveness of SpamBayes, the fundamental ‘unsure' range is discussed, and the method of removing the range is outlined. Finally, an analysis of the results of the running the four submissions through the Spam Track ‘jig' with the three private corpora and one public corpus is made.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Meyer05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Meyer05,
		author = {Tony Andrew Meyer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A {TREC} Along the Spam Track with SpamBayes},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/masseyu.spam.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Meyer05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM SpamGuru on the TREC 2005 Spam Track

_Richard B. Segal_

- :fontawesome-solid-user-group: **Participant:** [ibm.segal](./spam/participants.md#ibm.segal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm-segal.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm-segal.spam.pdf)
- :material-file-search: **Runs:** [621SPAM1FT1](./spam/runs.md#621spam1ft1) | [621SPAMFT1](./spam/runs.md#621spamft1) | [621SPAM1FIN](./spam/runs.md#621spam1fin) | [621SPAM1FUL](./spam/runs.md#621spam1ful) | [621SPAM2FUL](./spam/runs.md#621spam2ful) | [621SPAM3FUL](./spam/runs.md#621spam3ful) | [621SPAM1S50](./spam/runs.md#621spam1s50) | [621SPAM2S50](./spam/runs.md#621spam2s50) | [621SPAM3S50](./spam/runs.md#621spam3s50) | [621SPAM1S25](./spam/runs.md#621spam1s25) | [621SPAM2S25](./spam/runs.md#621spam2s25) | [621SPAM3S25](./spam/runs.md#621spam3s25) | [621SPAM1H50](./spam/runs.md#621spam1h50) | [621SPAM2H50](./spam/runs.md#621spam2h50) | [621SPAM3H50](./spam/runs.md#621spam3h50) | [621SPAM1H25](./spam/runs.md#621spam1h25) | [621SPAM2H25](./spam/runs.md#621spam2h25) | [621SPAM3H25](./spam/runs.md#621spam3h25)

??? abstract "Abstract"
	
	BM Research is developing an enterpriseclass anti-spam filter as part of our overall strategy of attacking the Spam problem on multiple fronts. Our anti-spam filter, SpamGuru, mirrors this philosophy by incorporating several different filtering technologies and intelligently combining their output to produce a single spamminess rating. The use of multiple algorithms improves the system's effectiveness and makes it more difficult for spammers to attack. While our overall performance was strong, our results did uncover some flaws and weaknesses in our existing implementation. Our latest code, with these weaknesses addressed as well as other enhancements, produces results on par with the best performing classifiers reported for TREC 2005 on the public corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Segal05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Segal05,
		author = {Richard B. Segal},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IBM} SpamGuru on the {TREC} 2005 Spam Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ibm-segal.spam.pdf},
		timestamp = {Sun, 29 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Segal05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Simple Language Models for Spam Detection

_Egidio Terra_

- :fontawesome-solid-user-group: **Participant:** [puc-rs.terra](./spam/participants.md#puc-rs.terra)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/pontificiau.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/pontificiau.spam.pdf)
- :material-file-search: **Runs:** [PUC](./spam/runs.md#puc) | [pucrs2](./spam/runs.md#pucrs2) | [pucrs1](./spam/runs.md#pucrs1) | [pucrs0](./spam/runs.md#pucrs0) | [pucrs0full](./spam/runs.md#pucrs0full) | [pucrs1full](./spam/runs.md#pucrs1full) | [pucrs2full](./spam/runs.md#pucrs2full) | [pucrs0ham25](./spam/runs.md#pucrs0ham25) | [pucrs0ham50](./spam/runs.md#pucrs0ham50) | [pucrs0spam25](./spam/runs.md#pucrs0spam25) | [pucrs0spam50](./spam/runs.md#pucrs0spam50) | [pucrs1ham25](./spam/runs.md#pucrs1ham25) | [pucrs1ham50](./spam/runs.md#pucrs1ham50) | [pucrs1spam25](./spam/runs.md#pucrs1spam25) | [pucrs1spam50](./spam/runs.md#pucrs1spam50) | [pucrs2ham25](./spam/runs.md#pucrs2ham25) | [pucrs2ham50](./spam/runs.md#pucrs2ham50) | [pucrs2spam25](./spam/runs.md#pucrs2spam25) | [pucrs2spam50](./spam/runs.md#pucrs2spam50)

??? abstract "Abstract"
	
	For this year's Spam track we used classifiers based on language models. These models are used to compute the log-likelihood for each individual message and then classify them as either ham or spam. Different data sets were used to train these language models. Our approach is simple, we initially create simple unigram language models and smooth the probabilities of unseen tokens by means of the expected likelihood estimator with a small discount probability tuned in a training corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Terra05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Terra05,
		author = {Egidio Terra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Simple Language Models for Spam Detection},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/pontificiau.spam.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Terra05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CAS-ICT at TREC 2005 SPAM Track: Using Non-Textual Information  to Improve Spam Filtering Performance

_Shuhua Wang, Bin Wang, Hao Lang, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-ict.wang](./spam/participants.md#cas-ict.wang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-bin.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-bin.spam.pdf)
- :material-file-search: **Runs:** [ICTSPAMpWNB](./spam/runs.md#ictspampwnb) | [ICTSPAM1WNB](./spam/runs.md#ictspam1wnb) | [ICTSPAM2WNH](./spam/runs.md#ictspam2wnh) | [ICTSPAM3NBH](./spam/runs.md#ictspam3nbh) | [ICTSPAM4NBB](./spam/runs.md#ictspam4nbb)

??? abstract "Abstract"
	
	This paper introduces our work in the TREC2005 SPAM track. Naïve Bayes and Littlestone's Winnow are chosen as our basic classifiers. In our investigation, we found that when the structures of Ham and Spam are very different, the feature distributions of them vary a lot. Thus the factor of structure is introduced into our filter. Besides textual word feature, some kind of other features are also considered in our filter. Our experimental results show that Winnow outperforms Naïve Bayes and the multi-feature model outperforms structure based model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangWLC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangWLC05,
		author = {Shuhua Wang and Bin Wang and Hao Lang and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CAS-ICT} at {TREC} 2005 {SPAM} Track: Using Non-Textual Information to Improve Spam Filtering Performance},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-bin.spam.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangWLC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS Kidult Anti-SPAM Solution at the TREC 2005 Spam Track: Improving  the Performance of Naive Bayes for Spam Detection

_Zhen Yang, Weiran Xu, Bo Chen, Jiani Hu, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [beijingu.guo](./spam/participants.md#beijingu.guo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/beijingu-of-pt.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/beijingu-of-pt.spam.pdf)
- :material-file-search: **Runs:** [kidSPAMpBAS](./spam/runs.md#kidspampbas) | [kidSPAM1BAS](./spam/runs.md#kidspam1bas) | [kidSPAM2V2B](./spam/runs.md#kidspam2v2b) | [kidSPAM3V2E](./spam/runs.md#kidspam3v2e) | [kidSPAM4V5B](./spam/runs.md#kidspam4v5b) | [1BASresults](./spam/runs.md#1basresults) | [2V2Bresults](./spam/runs.md#2v2bresults) | [3V2Eresults](./spam/runs.md#3v2eresults) | [4V5Bresults](./spam/runs.md#4v5bresults)

??? abstract "Abstract"
	
	Recently, the spam already constituted a serious problem for both e-mail users and Internet Service Providers (ISP). Solutions to the abuse of spam would be both technical and legal regulatory. This paper reports our solution for the TREC 2005 spam track, in which we consider the use of Naive Bayes spam filter for its desirable properties (simplicity, low time and memory requirements, etc.). Then the approaches to modify the Naive Bayes by simply introducing weight and classifier assemble based on dynamic threshold are proposed, which can help to improve the accuracy of a Naive Bayes spam classifier dramatically. Additionally, we discuss some steps that must be adopted naturally thought before, such as stop list, word stemming, feature selection, class prior probabilities. The theory analysis implies these steps are not necessarily the best way to extend the Bayesian classifier, and these were also verified empirically. Many of these techniques appear to be counterintuitive but can be explained by the statistical properties of e-mail itself. Experiment results of TREC 2005 spam track demonstrate the effectiveness of the proposed method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangXCHG05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangXCHG05,
		author = {Zhen Yang and Weiran Xu and Bo Chen and Jiani Hu and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} Kidult Anti-SPAM Solution at the {TREC} 2005 Spam Track: Improving the Performance of Naive Bayes for Spam Detection},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/beijingu-of-pt.spam.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangXCHG05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2005 HARD, Robust, and SPAM Tracks

_Kiduk Yang, Ning Yu, Nicholas George, Aaron Loehrlein, David McCaulay, Hui Zhang, Shahrier Akram, Jue Mei, Ivan Record_

- :fontawesome-solid-user-group: **Participant:** [indianau.yang](./spam/participants.md#indianau.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf)
- :material-file-search: **Runs:** [indSPAMpwf4](./spam/runs.md#indspampwf4) | [indSPAM1f4f](./spam/runs.md#indspam1f4f) | [indSPAM2f42](./spam/runs.md#indspam2f42) | [indSPAM3f40](./spam/runs.md#indspam3f40) | [indSPAM4pf4](./spam/runs.md#indspam4pf4)

??? abstract "Abstract"
	
	Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science participated in the HARD, Robust, and SPAM tracks in TREC-2005. The basic approach of WIDIT is to combine multiple methods as well as to leverage multiple sources of evidence. Our main strategies for the tracks were: query expansion and fusion optimization for the HARD and Robust tracks; and combination of probabilistic, rule-based, pattern-based, and blacklist email filters for the SPAM track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYGLMZAMR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYGLMZAMR05,
		author = {Kiduk Yang and Ning Yu and Nicholas George and Aaron Loehrlein and David McCaulay and Hui Zhang and Shahrier Akram and Jue Mei and Ivan Record},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2005 HARD, Robust, and {SPAM} Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf},
		timestamp = {Wed, 29 Jun 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangYGLMZAMR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Terabyte 

#### The TREC 2005 Terabyte Track

_Charles L. A. Clarke, Falk Scholer, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/TERABYTE.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/TERABYTE.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Terabyte Track explores how retrieval and evaluation techniques can scale to terabyte-sized collections, examining both efficiency and effectiveness issues. TREC 2005 is the second year for the track. The track was introduced as part of TREC 2004, with a single adhoc retrieval task. That year, 17 groups submitted 70 runs in total. This year, the track consisted of three experimental tasks: an adhoc retrieval task, an efficiency task and a named page finding task. 18 groups submitted runs to the adhoc retrieval task, 13 groups submitted runs to the efficiency task, and 13 groups submitted runs to the named page finding task. This report provides an overview of each task, summarizes the results and discusses directions for the future. Further background information on the development of the track can be found in last year's track report [4].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeSS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeSS05,
		author = {Charles L. A. Clarke and Falk Scholer and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {TREC} 2005 Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/TERABYTE.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeSS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Efficiency vs. Effectiveness in Terabyte-Scale Information Retrieval

_Stefan Büttcher, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.clarke](./terabyte/participants.md#uwaterloo.clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uwaterloo-tera.pdf](http://trec.nist.gov/pubs/trec14/papers/uwaterloo-tera.pdf)
- :material-file-search: **Runs:** [uwmtEwteD00](./terabyte/runs.md#uwmtewted00) | [uwmtEwtePTP](./terabyte/runs.md#uwmtewteptp) | [uwmtEwteD10](./terabyte/runs.md#uwmtewted10) | [uwmtEwteD02](./terabyte/runs.md#uwmtewted02) | [uwmtEwtaPt](./terabyte/runs.md#uwmtewtapt) | [uwmtEwtaPtdn](./terabyte/runs.md#uwmtewtaptdn) | [uwmtEwtaD00t](./terabyte/runs.md#uwmtewtad00t) | [uwmtEwtaD02t](./terabyte/runs.md#uwmtewtad02t) | [uwmtEwtnpDpr](./terabyte/runs.md#uwmtewtnpdpr) | [uwmtEwtnpD](./terabyte/runs.md#uwmtewtnpd) | [uwmtEwtnpP](./terabyte/runs.md#uwmtewtnpp) | [uwmtEwtnpPpr](./terabyte/runs.md#uwmtewtnpppr)

??? abstract "Abstract"
	
	We describe indexing and retrieval techniques that are suited to perform terabyte-scale information retrieval tasks on a standard desktop PC. Starting from an Okapi-BM25-based default baseline retrieval function, we explore both sides of the effectiveness spectrum. On one side, we show how term proximity can be integrated into the scoring function in order to improve the search results. On the other side, we show how index pruning can be employed to increase retrieval efficiency - at the cost of reduced retrieval effectiveness. We show that, although index pruning can harm the quality of the search results considerably, according to standard evaluation measures, the actual loss of precision, according to other measures that are more realistic for the given task, is rather small and is in most cases outweighed by the immense efficiency gains that come along with it.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ButtcherC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ButtcherC05,
		author = {Stefan B{\"{u}}ttcher and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Efficiency vs. Effectiveness in Terabyte-Scale Information Retrieval},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uwaterloo-tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ButtcherC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Indri at TREC 2005: Terabyte Track

_Donald Metzler, Trevor Strohman, Yun Zhou, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./terabyte/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umass-tera.pdf](http://trec.nist.gov/pubs/trec14/papers/umass-tera.pdf)
- :material-file-search: **Runs:** [indri05Eql](./terabyte/runs.md#indri05eql) | [indri05EqlD](./terabyte/runs.md#indri05eqld) | [indri05Aql](./terabyte/runs.md#indri05aql) | [indri05Adm](./terabyte/runs.md#indri05adm) | [indri05AdmfS](./terabyte/runs.md#indri05admfs) | [indri05AdmfL](./terabyte/runs.md#indri05admfl) | [indri05Nmpsd](./terabyte/runs.md#indri05nmpsd) | [indri05Nf](./terabyte/runs.md#indri05nf) | [indri05Nmp](./terabyte/runs.md#indri05nmp)

??? abstract "Abstract"
	
	This work details the experiments carried out using the Indri search engine during the TREC 2005 Terabyte Track. Results are presented for each of the three tasks, including efficiency, ad hoc, and named page finding. Our efficiency runs focused on query optimization techniques, our ad hoc runs look at the importance of term proximity and document quality, and our named-page finding runs investigate the use of document priors and document structure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MetzlerSZC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MetzlerSZC05,
		author = {Donald Metzler and Trevor Strohman and Yun Zhou and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Indri at {TREC} 2005: Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umass-tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MetzlerSZC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melbourne University 2005: Enterprise and Terabyte Tasks

_Vo Ngoc Anh, William Webber, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [umelbourne.anh](./terabyte/participants.md#umelbourne.anh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umelbourne.ent.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/umelbourne.ent.tera.pdf)
- :material-file-search: **Runs:** [MU05TBy4](./terabyte/runs.md#mu05tby4) | [MU05TBy2](./terabyte/runs.md#mu05tby2) | [MU05TBy1](./terabyte/runs.md#mu05tby1) | [MU05TBy3](./terabyte/runs.md#mu05tby3) | [MU05TBa1](./terabyte/runs.md#mu05tba1) | [MU05TBa2](./terabyte/runs.md#mu05tba2) | [MU05TBa3](./terabyte/runs.md#mu05tba3) | [MU05TBa4](./terabyte/runs.md#mu05tba4)

??? abstract "Abstract"
	
	This report describes the work done at The University of Melbourne for the TREC-2005 Enterprise and Terabyte Tracks. In the Enterprise Track, we participated in the Discussion Task. We tried a number of different methods to make use of special features of mailing lists to improve retrieval effectiveness, and found the use of thread context to be promising. In the Terabyte Track, we continued our work with impact-based ranking and sought to reduce indexing as well as query time. A new retrieval system has been developed for this purpose and has shown several improvements over our system from last year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnhWM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnhWM05,
		author = {Vo Ngoc Anh and William Webber and Alistair Moffat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Melbourne University 2005: Enterprise and Terabyte Tasks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umelbourne.ent.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnhWM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IXE at the TREC 2005 Terabyte Task

_Giuseppe Attardi_

- :fontawesome-solid-user-group: **Participant:** [upisa.attardi](./terabyte/participants.md#upisa.attardi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/upisa.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/upisa.tera.pdf)
- :material-file-search: **Runs:** [pisaEff3](./terabyte/runs.md#pisaeff3) | [pisaEff4](./terabyte/runs.md#pisaeff4) | [pisaEff2](./terabyte/runs.md#pisaeff2) | [pisaTTitProx](./terabyte/runs.md#pisattitprox) | [pisaTLonProx](./terabyte/runs.md#pisatlonprox) | [pisaTLonPrxA](./terabyte/runs.md#pisatlonprxa) | [pisaTLonPrxC](./terabyte/runs.md#pisatlonprxc) | [pisaTNp](./terabyte/runs.md#pisatnp) | [pisaTNpProx](./terabyte/runs.md#pisatnpprox) | [pisaTNpProxC](./terabyte/runs.md#pisatnpproxc)

??? abstract "Abstract"
	
	The TREC Terabyte task provides an opportunity to analyze scalability issues in document retrieval systems. I describe how to overcome some of these issues and in particular improvements to the IXE search engine in order to achieve higher precision while maintaining good retrieval performance. A new algorithm has been introduced to handle OR queries efficiently. A proximity factor is also computed and added to the relevance score obtained by the PL2 document weighting model: several experiments have been performed to tune its parameters. By tuning also other parameters used in relevance ranking, IXE achieved second best overall P@10 score, combined with the fastest reported retrieval speed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Attardi05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Attardi05,
		author = {Giuseppe Attardi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IXE} at the {TREC} 2005 Terabyte Task},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/upisa.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Attardi05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2005: Terabyte and Robust Track

_Yaniv Bernstein, Bodo Billerbeck, Steven Garcia, Nicholas Lester, Falk Scholer, Justin Zobel, William Webber_

- :fontawesome-solid-user-group: **Participant:** [rmit.scholer](./terabyte/participants.md#rmit.scholer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/rmit-falk.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/rmit-falk.tera.robust.pdf)
- :material-file-search: **Runs:** [zetdir](./terabyte/runs.md#zetdir) | [zetdist](./terabyte/runs.md#zetdist) | [zetdirhoc](./terabyte/runs.md#zetdirhoc) | [zetdirA](./terabyte/runs.md#zetdira) | [zetnp](./terabyte/runs.md#zetnp) | [zetnpancfuzz](./terabyte/runs.md#zetnpancfuzz) | [zetnpanc](./terabyte/runs.md#zetnpanc) | [zetnp50w](./terabyte/runs.md#zetnp50w)

??? abstract "Abstract"
	
	RMIT University participated in the terabyte and robust tracks in TREC 2005. The terabyte track consists of the three tasks: adhoc retrieval, efficient retrieval, and named page finding. For the adhoc retrieval task we used a language modelling approach based on query likelihood, as well as a new technique aimed at reducing the amount of memory used for ranking documents. For the efficiency task, we submitted results from both a single-machine system and one that was distrubuted among a number of machines, with promising results. The named page task was organised by RMIT University and as a result we repeated last year's experiments, slightly modified, with this year's data. The robust track has two subtasks: adhoc retrieval, and query difficulty prediction. For adhoc retrieval, we employed a standard local analysis query expansion method, sourcing expansion terms for different runs from the collection supplied, from a side corpus, or a combination of both. In one run, we also tested removing duplicate documents from the list of results; in order to predict topic difficulty, we evaluated different document priors of the documents in the result set, in the hope of supplying a more robust set of answers at the cost of returning a potentially smaller number of relevant documents. The second task was to predict query difficulty. To this end, we compared the order of the documents in the result sets to the ordering as determined by document priors. A high similarity in orderings indicated that the query was poor. Two different priors were used. The first was based on document access counts, where each document is given a score that is derived from how likely it is to be ranked by a randomly generated query. The second was directly related to the document size. In this paper we outline our approaches and experiments in both tracks, and discuss our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BernsteinBGLSZW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BernsteinBGLSZW05,
		author = {Yaniv Bernstein and Bodo Billerbeck and Steven Garcia and Nicholas Lester and Falk Scholer and Justin Zobel and William Webber},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2005: Terabyte and Robust Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/rmit-falk.tera.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BernsteinBGLSZW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MG4J at TREC 2005

_Paolo Boldi, Sebastiano Vigna_

- :fontawesome-solid-user-group: **Participant:** [umilano.vigna](./terabyte/participants.md#umilano.vigna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/unimi.vigna.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/unimi.vigna.tera.pdf)
- :material-file-search: **Runs:** [mg4jeff](./terabyte/runs.md#mg4jeff) | [adhocmg4j](./terabyte/runs.md#adhocmg4j)

??? abstract "Abstract"
	
	MG4J participated in two tracks of TREC 2005 — the ad hoc task and the efficiency task of the Terabyte Track (find all the relevant documents with high precision from 25.2 million pages from the .gov domain). It was the first time the MG4J group participated to TREC, and we concentrated our efforts on the ad hoc task, using a combination of techniques based on a new multi-index minimal-interval semantics and PageRank.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoldiV05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoldiV05,
		author = {Paolo Boldi and Sebastiano Vigna},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{MG4J} at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/unimi.vigna.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoldiV05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Looking at Limits and Tradeoffs: Sabir Research at TREC 2005

_Chris Buckley_

- :fontawesome-solid-user-group: **Participant:** [sabir.buckley](./terabyte/participants.md#sabir.buckley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf)
- :material-file-search: **Runs:** [sabtb05ef1](./terabyte/runs.md#sabtb05ef1) | [sab05tbt](./terabyte/runs.md#sab05tbt) | [sab05tball](./terabyte/runs.md#sab05tball) | [sab05tbas](./terabyte/runs.md#sab05tbas)

??? abstract "Abstract"
	
	Sabir Research participated in TREC-2005 in the Terabyte, Robust, and document retrieval part of the Question Answering tracks. This writeup focuses on the Robust track, and in particular on a “routing” run that took advantage of relevance judgements for the topics on the old trec V45 collection to construct queries for the new Aquaint collection. The smart_retro tool is described which given a query and the set of relevant documents, constructs an optimally weighted version of the query. smart_retro is also used to examine the differences in difficulty between the V45 and Aquaint collections (the Aquaint collection is considerably easier). The final part of the paper describes the compression algorithms and tradeoffs that were used in both TREC 2004 and 2005. These were presented in the TREC 2004 speaker session, but never formally written up. The hardware used for all runs was a single commodity PC with a total cost of $1600: $540 for a Dell PC, $520 for four 250 GByte disks, and $500 to bring the memory up to 2.5 GBytes. The information retrieval software used was the research version of SMART 15.0. SMART was originally developed in the early 1960's by Gerard Salton and since then has continued to be a leading research information retrieval tool. It continues to use a statistical vector space model, with stemming, stop words, weighting, inner product similarity function, and ranked retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Buckley05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Buckley05,
		author = {Chris Buckley},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Looking at Limits and Tradeoffs: Sabir Research at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Buckley05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Logistic Regression Merging of Amberfish and Lucene Multisearch Results

_Christopher T. Fallen, Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [arsc.newby](./terabyte/participants.md#arsc.newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ualaska.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/ualaska.tera.pdf)
- :material-file-search: **Runs:** [ctfluc1](./terabyte/runs.md#ctfluc1) | [ctfadhocaf1](./terabyte/runs.md#ctfadhocaf1) | [ctfadhocluc1](./terabyte/runs.md#ctfadhocluc1) | [ctfm1](./terabyte/runs.md#ctfm1) | [ctfm2](./terabyte/runs.md#ctfm2) | [ctflnp1](./terabyte/runs.md#ctflnp1)

??? abstract "Abstract"
	
	A simple logistic-regression based isolated data fusion algorithm was used to merge results from two free open-source text retrieval tools. The algorithm is described and results from each search tool are compared against the merged results and against each other. Basic performance measures are reported and discussed, and future projects are outlined.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FallenN05.bib) "
	```
	@inproceedings{DBLP:conf/trec/FallenN05,
		author = {Christopher T. Fallen and Gregory B. Newby},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Logistic Regression Merging of Amberfish and Lucene Multisearch Results},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ualaska.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FallenN05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Dublin City University at the TREC 2005 Terabyte Track

_Paul Ferguson, Cathal Gurrin, Alan F. Smeaton, Peter Wilkins_

- :fontawesome-solid-user-group: **Participant:** [dublincityu.gurrin](./terabyte/participants.md#dublincityu.gurrin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dublincu.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/dublincu.tera.pdf)
- :material-file-search: **Runs:** [DCU05DISTWTF](./terabyte/runs.md#dcu05distwtf) | [DCU05DISTDID](./terabyte/runs.md#dcu05distdid) | [DCU05WTF](./terabyte/runs.md#dcu05wtf) | [DCU05WTFQ](./terabyte/runs.md#dcu05wtfq) | [DCU05AWTF](./terabyte/runs.md#dcu05awtf) | [DCU05ADID](./terabyte/runs.md#dcu05adid) | [DCU05ACOMBO](./terabyte/runs.md#dcu05acombo) | [DCU05ABM25](./terabyte/runs.md#dcu05abm25) | [DCU05NPWTF](./terabyte/runs.md#dcu05npwtf) | [DCU05NPBM25](./terabyte/runs.md#dcu05npbm25) | [DCU05NPDID](./terabyte/runs.md#dcu05npdid) | [DCU05NPCOMBO](./terabyte/runs.md#dcu05npcombo)

??? abstract "Abstract"
	
	For the 2005 Terabyte track in TREC Dublin City University participated in all three tasks: Adhoc, Efficiency and Named Page Finding. Our runs for TREC in all tasks were primarily focussed on the application of “Top Subset Retrieval” to the Terabyte Track. This retrieval utilises different types of sorted inverted indices so that less documents are processed in order to reduce query times, and is done so in a way that minimises loss of effectiveness in terms of query precision. We also compare a distributed version of our F´ısr´eal search system [1][2] against the same system deployed on a single machine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FergusonGSW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/FergusonGSW05,
		author = {Paul Ferguson and Cathal Gurrin and Alan F. Smeaton and Peter Wilkins},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Dublin City University at the {TREC} 2005 Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/dublincu.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FergusonGSW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### National Taiwan University at Terabyte Track of TREC 2005

_Ming-Hung Hsu, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./terabyte/participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ntu.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/ntu.tera.pdf)
- :material-file-search: **Runs:** [NTUET1](./terabyte/runs.md#ntuet1) | [NTUET2](./terabyte/runs.md#ntuet2) | [NTUAH1](./terabyte/runs.md#ntuah1) | [NTUAH2](./terabyte/runs.md#ntuah2) | [NTUAH3](./terabyte/runs.md#ntuah3) | [NTUAH4](./terabyte/runs.md#ntuah4) | [NTUNF1](./terabyte/runs.md#ntunf1) | [NTUNF2](./terabyte/runs.md#ntunf2) | [NTUNF4](./terabyte/runs.md#ntunf4) | [NTUNF3](./terabyte/runs.md#ntunf3)

??? abstract "Abstract"
	
	There are three tasks in the Terabyte track of TREC 2005, i.e. Efficiency, Ad hoc and Named page finding. We participated in all the tasks and use different retrieval methods to deal with each task, aiming to vary the retrieval method according to the different characteristics of different tasks. In Ah hoc task, we adopt the technique of query-specific clustering. In Named page finding task, we cared more about the information of document title and anchor text of out-links.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HsuC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HsuC05,
		author = {Ming{-}Hung Hsu and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {National Taiwan University at Terabyte Track of {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ntu.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HsuC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Effective Smoothing for a Terabyte of Text

_Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.mueller](./terabyte/participants.md#uamsterdam.mueller)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uamsterdam.tera.kamps.pdf](http://trec.nist.gov/pubs/trec14/papers/uamsterdam.tera.kamps.pdf)
- :material-file-search: **Runs:** [UAmsT05aTeLM](./terabyte/runs.md#uamst05atelm) | [UAmsT05aTeVS](./terabyte/runs.md#uamst05atevs) | [UAmsT05n3SUM](./terabyte/runs.md#uamst05n3sum) | [UAmsT05nTeLM](./terabyte/runs.md#uamst05ntelm) | [UAmsT05nTurl](./terabyte/runs.md#uamst05nturl) | [UAmsT05nTind](./terabyte/runs.md#uamst05ntind)

??? abstract "Abstract"
	
	As part of the TREC 2005 Terabyte track, we conducted a range of experiments investigating the effects of larger collections. Our main findings can be summarized as follows. First, we tested whether our retrieval system scales up to terabyte-scale collections. We found that our retrieval system can handle 25 million documents, although in terms of indexing time we are approaching the limits of a non-distributed retrieval system. Second, we hoped to find out whether results from earlier Web Tracks carry over to this task. For known-item search we found that, on the one hand, indegree and URL priors did not promote retrieval effectiveness, but that, on the other hand, the combination of different document representations improved retrieval effectiveness. Third, we investigated the role of smoothing for collections of this size. We found that larger collections require far less smoothing, especially for the adhoc task using very little smoothing leads to substantial gains in retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Kamps05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Kamps05,
		author = {Jaap Kamps},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Effective Smoothing for a Terabyte of Text},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uamsterdam.tera.kamps.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Kamps05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2005: Terabyte Track

_Mladen Kovacevic, Xiangji Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./terabyte/participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/yorku-huang.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/yorku-huang.tera.pdf)
- :material-file-search: **Runs:** [york05tAa1](./terabyte/runs.md#york05taa1) | [york05tNa1](./terabyte/runs.md#york05tna1)

??? abstract "Abstract"
	
	York University participated in the terabyte track this year. Using the GOV2 collection, we used filtering techniques to shorten the amount of data to be indexed before indexing into eight partitions. As there were several different subsections of the terabyte track, we chose to participate in the ad hoc and named page retrieval runs. Our technique involved partitioned indexes across a single machine. We combined our results by first calculating the document frequency of a term across all the indexes, calculating the weight, then using the same weight in retrieving the top results from each index. This approach effectively tried to mimic the results that would be obtained if there were only one large index.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KovacevicH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KovacevicH05,
		author = {Mladen Kovacevic and Xiangji Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2005: Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/yorku-huang.tera.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KovacevicH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2005: Experiments in Terabyte and  Enterprise Tracks with Terrier

_Craig Macdonald, Ben He, Vassilis Plachouras, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uglasgow.ounis](./terabyte/participants.md#uglasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uglasgow.tera.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/uglasgow.tera.ent.pdf)
- :material-file-search: **Runs:** [uogTB05SQE](./terabyte/runs.md#uogtb05sqe) | [uogTB05LQEV](./terabyte/runs.md#uogtb05lqev) | [uogTB05SQES](./terabyte/runs.md#uogtb05sqes) | [uogTB05SQEH](./terabyte/runs.md#uogtb05sqeh) | [uogNP05base](./terabyte/runs.md#uognp05base) | [uogNP05bis](./terabyte/runs.md#uognp05bis) | [uogNP05bisP](./terabyte/runs.md#uognp05bisp) | [uogNP05baseN](./terabyte/runs.md#uognp05basen)

??? abstract "Abstract"
	
	With our participation in TREC 2005, we continue experiments using Terrier, a modular and scalable Information Retrieval (IR) framework, in 4 tasks from the Terabyte and Enterprise tracks. In the Terabyte track, we investigate new Divergence From Randomness weighting models, and a novel query expansion approach that can take into account various document fields, namely content, title and anchor text. In addition, we test a new selective query expansion mechanism which determines the appropriateness of using query expansion on a per-query basis, using statistical information from a low-cost query performance predictor. In the Enterprise track, we investigate combining document fields evidence with other information occurring in an Enterprise setting. In the email known item task, we also investigate temporal and thread priors suitable for email search. In the expert search task, for each candidate, we generate profiles of expertise evidence from the W3C collection. Moreover, we propose a model for ranking these candidate profiles in response to a query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacdonaldHPO05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacdonaldHPO05,
		author = {Craig Macdonald and Ben He and Vassilis Plachouras and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2005: Experiments in Terabyte and Enterprise Tracks with Terrier},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uglasgow.tera.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacdonaldHPO05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Enterprise, QA, Robust and Terabyte Experiments with Hummingbird SearchServer  at TREC 2005

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./terabyte/participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf)
- :material-file-search: **Runs:** [humTE05i4](./terabyte/runs.md#humte05i4) | [humTE05i4l](./terabyte/runs.md#humte05i4l) | [humTE05i4ld](./terabyte/runs.md#humte05i4ld) | [humTE05i5](./terabyte/runs.md#humte05i5) | [humT05l](./terabyte/runs.md#humt05l) | [humT05x5l](./terabyte/runs.md#humt05x5l) | [humT05xl](./terabyte/runs.md#humt05xl) | [humT05xle](./terabyte/runs.md#humt05xle) | [humTN05dpl](./terabyte/runs.md#humtn05dpl) | [humTN05pl](./terabyte/runs.md#humtn05pl) | [humTN05l](./terabyte/runs.md#humtn05l) | [humTN05rdpl](./terabyte/runs.md#humtn05rdpl)

??? abstract "Abstract"
	
	Hummingbird participated in 6 tasks of TREC 2005: the email known-item search task of the Enterprise Track, the document ranking task of the Question Answering Track, the ad hoc topic relevance task of the Robust Retrieval Track, and the adhoc, efficiency and named page finding tasks of the Terabyte Track. In the email known-item task, SearchServer found the desired message in the first 10 rows for more than 80% of the 125 queries. In the document ranking task, SearchServer returned an answering document in the first 10 rows for more than 90% of the 50 questions. In the robustness task, SearchServer found a relevant document in the first 10 rows for 88% of the 50 short (title) topics. In the terabyte adhoc and efficiency tasks, SearchServer found a relevant document in the first 10 rows for more than 90% of the 50 title topics. A new retrieval measure, First Relevant Score, is investigated; it is found to more accurately reflect known-item differences than reciprocal rank and to better reflect robustness across topics than the primary measure of the Robust track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson05,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Enterprise, QA, Robust and Terabyte Experiments with Hummingbird SearchServer at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Queensland University of Technology at TREC 2005

_Alan Woodley, Chengye Lu, Tony Sahama, John King, Shlomo Geva_

- :fontawesome-solid-user-group: **Participant:** [queenslandu.geva](./terabyte/participants.md#queenslandu.geva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/queenslandu.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/queenslandu.tera.robust.pdf)
- :material-file-search: **Runs:** [QUT05TBMRel](./terabyte/runs.md#qut05tbmrel) | [QUT05TBEn](./terabyte/runs.md#qut05tben) | [QUT05DBEn](./terabyte/runs.md#qut05dben) | [QUT05TSynEn](./terabyte/runs.md#qut05tsynen)

??? abstract "Abstract"
	
	The Information Retrieval and Web Intelligence (IR-WI) research group is a research team at the Faculty of Information Technology, QUT, Brisbane, Australia. The IR-WI group participated in the Terabyte and Robust track at TREC 2005, both for the first time. For the Robust track we applied our existing information retrieval system that was originally designed for use with structured (XML) retrieval to the domain of document retrieval. For the Terabyte track we experimented with an open source IR system, Zettair and performed two types of experiments. First, we compared Zettair's performance on both a high-powered supercomputer and a distributed system across seven midrange personal computers. Second, we compared Zettair's performance when a standard TREC title is used, compared with a natural language query, and a query expanded with synonyms. We compare the systems both in terms of efficiency and retrieval performance. Our results indicate that the distributed system is faster than the supercomputer, while slightly decreasing retrieval performance, and that natural language queries also slightly decrease retrieval performance, while our query expansion technique significantly decreased performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WoodleyLSKG05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WoodleyLSKG05,
		author = {Alan Woodley and Chengye Lu and Tony Sahama and John King and Shlomo Geva},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Queensland University of Technology at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/queenslandu.tera.robust.pdf},
		timestamp = {Wed, 14 Jun 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WoodleyLSKG05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Tianwang Search Engine at TREC 2005: Terabyte Track

_Hongfei Yan, Jingjing Li, Jiaji Zhu, Bo Peng_

- :fontawesome-solid-user-group: **Participant:** [pekingu.yan](./terabyte/participants.md#pekingu.yan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/pekingu-he.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/pekingu-he.tera.pdf)
- :material-file-search: **Runs:** [TWTB05EF01](./terabyte/runs.md#twtb05ef01) | [TWTB05AD01](./terabyte/runs.md#twtb05ad01) | [TWTB05AD02](./terabyte/runs.md#twtb05ad02) | [TWTB05NP01](./terabyte/runs.md#twtb05np01) | [TWTB05NP02](./terabyte/runs.md#twtb05np02) | [TWTB05NP03](./terabyte/runs.md#twtb05np03)

??? abstract "Abstract"
	
	Tianwang for the first time participated in all three tasks of the Terabyte Track of TREC 2005 to explore its performance. All three tasks, including the adhoc task (find all the relevant documents with high precision ), the efficiency task (find top-20 results for each of 50k-entry queries with efficiency and scalability) and the named page finding task (sometimes search a page by name), are based on a 426GB collection of 25.2 million pages taken from the .gov Web domain (“GOV2”). In the adhoc task with 50 topics, Tianwang returned at least one relevant document in top 10 for 42 topics. In the efficiency task, Tianwang returned at least one relevant document in top 20 for 44 of the 50 quires. In the named page task with 252 topics, Tianwang returned a desired page in top 10 for 99 topics; meanwhile, it failed to find a correct one for 120 topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YanLZP05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YanLZP05,
		author = {Hongfei Yan and Jingjing Li and Jiaji Zhu and Bo Peng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Tianwang Search Engine at {TREC} 2005: Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/pekingu-he.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YanLZP05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Juru at TREC 2005: Query Prediction in the Terabyte and the Robust  Tracks

_Elad Yom-Tov, David Carmel, Adam Darlow, Dan Pelleg, Shai Errera-Yaakov, Shai Fine_

- :fontawesome-solid-user-group: **Participant:** [ibm-haifa.carmel](./terabyte/participants.md#ibm-haifa.carmel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm-haifa.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm-haifa.tera.robust.pdf)
- :material-file-search: **Runs:** [JuruDF0](./terabyte/runs.md#jurudf0) | [JuruDF1](./terabyte/runs.md#jurudf1) | [juruFeSe](./terabyte/runs.md#jurufese) | [juruFeRa](./terabyte/runs.md#jurufera)

??? abstract "Abstract"
	
	Our experiments focus this year on the ad-hock tasks of the Terabyte and the Robust tracks. In both tracks we experimented with the query prediction technology we developed recently. In the Terabyte track, we investigated how query prediction can be used to improve federation of search results extracted from several indices. We show that federated search based on query prediction can achieve comparable results to single-index search. In the Robust track we trained a predictor over one collection (TREC-8) for predicting query difficulty over another collection (AQUAINT). The experimental results show that difficult topics on the TREC-8 collection were not found to be consistently difficult on the AQUAINT collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yom-TovCDPEF05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yom-TovCDPEF05,
		author = {Elad Yom{-}Tov and David Carmel and Adam Darlow and Dan Pelleg and Shai Errera{-}Yaakov and Shai Fine},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Juru at {TREC} 2005: Query Prediction in the Terabyte and the Robust Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ibm-haifa.tera.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yom-TovCDPEF05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2005 Terabyte Track

_Le Zhao, Rongwei Ceng, Min Zhang, Yijiang Jin, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghua.ma](./terabyte/participants.md#tsinghua.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.tera.pdf)
- :material-file-search: **Runs:** [THUtb05SQWP1](./terabyte/runs.md#thutb05sqwp1) | [THUtb05VQWP2](./terabyte/runs.md#thutb05vqwp2) | [THUtb05LQWP1](./terabyte/runs.md#thutb05lqwp1) | [THUtb05npB](./terabyte/runs.md#thutb05npb) | [THUtb05npWP2](./terabyte/runs.md#thutb05npwp2) | [THUtb05npW15](./terabyte/runs.md#thutb05npw15)

??? abstract "Abstract"
	
	IR group of Tsinghua University this year has used its TMiner text retrieval system for indexing and retrieval of the Terabyte track ad hoc and named-page subtasks. In doing the two tasks, we used the in-link anchor texts (the anchor of the URLs that point to the current page in the collection) together with the content texts of the web pages for building the indices. When retrieving, the word-pair method [1] was used and proved effective on 2004 and 2005 Terabyte ad hoc task topics and the 2005 named-page task. We analyze the performance of word-pair method in comparison with the Markov random field term dependence model of [2] and a generative phrase model we proposed, which is natural on the language modeling framework [3].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoCZJM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoCZJM05,
		author = {Le Zhao and Rongwei Ceng and Min Zhang and Yijiang Jin and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2005 Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoCZJM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Genomics 

#### TREC 2005 Genomics Track Overview

_William R. Hersh, Aaron M. Cohen, Jianji Yang, Ravi Teja Bhupatiraju, Phoebe M. Roberts, Marti A. Hearst_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/GEO.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/GEO.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC 2005 Genomics Track featured two tasks, an ad hoc retrieval task and four subtasks in text categorization. The ad hoc retrieval task utilized a 10-year, 4.5-million document subset of the MEDLINE bibliographic database, with 50 topics conforming to five generic topic types. The categorization task used a full-text document collection with training and test sets consisting of about 6,000 biomedical journal articles each. Participants aimed to triage the documents into categories representing data resources in the Mouse Genome Informatics database, with performance assessed via a utility measure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershCYBRH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershCYBRH05,
		author = {William R. Hersh and Aaron M. Cohen and Jianji Yang and Ravi Teja Bhupatiraju and Phoebe M. Roberts and Marti A. Hearst},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track Overview},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/GEO.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershCYBRH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Comparison of Techniques for Classification and Ad Hoc Retrieval  of Biomedical Documents

_Aaron M. Cohen, Jianji Yang, William R. Hersh_

- :fontawesome-solid-user-group: **Participant:** [ohsu.hersh](./genomics/participants.md#ohsu.hersh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ohsu-geo.pdf](http://trec.nist.gov/pubs/trec14/papers/ohsu-geo.pdf)
- :material-file-search: **Runs:** [OHSUall](./genomics/runs.md#ohsuall) | [OHSUkey](./genomics/runs.md#ohsukey) | [AOHSUBF](./genomics/runs.md#aohsubf) | [AOHSUSL](./genomics/runs.md#aohsusl) | [AOHSUVP](./genomics/runs.md#aohsuvp) | [EOHSUBF](./genomics/runs.md#eohsubf) | [EOHSUSL](./genomics/runs.md#eohsusl) | [EOHSUVP](./genomics/runs.md#eohsuvp) | [GOHSUBF](./genomics/runs.md#gohsubf) | [GOHSUSL](./genomics/runs.md#gohsusl) | [GOHSUVP](./genomics/runs.md#gohsuvp) | [TOHSUBF](./genomics/runs.md#tohsubf) | [TOHSUSL](./genomics/runs.md#tohsusl) | [TOHSUVP](./genomics/runs.md#tohsuvp)

??? abstract "Abstract"
	
	Oregon Health & Science University participated in both the classification and ad hoc retrieval tasks of the TREC 2005 Genomics Track. To better understand the text classification techniques that lead to improved performance, we applied a set of general purpose biomedical document classification systems to the four triage tasks, varying one system feature or text processing technique at a time. We found that our best and most consistent system consisted of a voting perceptron classifier, chi-square feature selection on full text articles, binary feature weighting, stemming and stopping, and pre-filtering based on the MeSH term Mice. This system approached, but did not surpass, the performance of the best TREC entry for each of the four tasks. Full text provided a substantial benefit over only title plus abstract. Other common techniques such as inverse-document frequency feature weighting, and cosine normalization were ineffective. For the ad hoc retrieval task, we used Zettair search engine. Both of our submissions used Okapi measure with the parameters optimized using the sample topics that were provided. Two different query sets were used in our runs; one with all the words and the other with only the keywords from the topic file. Queries with only keywords consistently outperformed queries with all words from the topic file. Optimization of the Okapi parameters improved our performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CohenYH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CohenYH05,
		author = {Aaron M. Cohen and Jianji Yang and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Comparison of Techniques for Classification and Ad Hoc Retrieval of Biomedical Documents},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ohsu-geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CohenYH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieval of Biomedical Documents by Prioritizing Key Phrases

_Kevin Hsin-Yih Lin, Wen-Juan Hou, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./genomics/participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ntu.geo.adhoc.pdf](http://trec.nist.gov/pubs/trec14/papers/ntu.geo.adhoc.pdf)
- :material-file-search: **Runs:** [NTUgah1](./genomics/runs.md#ntugah1) | [NTUgah2](./genomics/runs.md#ntugah2) | [aNTUMAC](./genomics/runs.md#antumac) | [tNTUMAC](./genomics/runs.md#tntumac) | [eNTUMAC](./genomics/runs.md#entumac) | [gNTUMAC](./genomics/runs.md#gntumac) | [tNTUMACasem](./genomics/runs.md#tntumacasem) | [tNTUMACwj](./genomics/runs.md#tntumacwj)

??? abstract "Abstract"
	
	In this paper, we present an approach for retrieving relevant articles from the biomedical corpus. Our first run considered four kinds of operators as query expansion. The operators are phrase, mandatory, optional and synonym set. The second run lowered the ranking of documents which contained query terms only in their MeSH fields. The results of the official runs and further experiments were listed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinHC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinHC05,
		author = {Kevin Hsin{-}Yih Lin and Wen{-}Juan Hou and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Retrieval of Biomedical Documents by Prioritizing Key Phrases},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ntu.geo.adhoc.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinHC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluation of Stemming, Query Expansion and Manual Indexing Approaches  for the Genomic Task

_Samir Abdou, Jacques Savoy, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [uneuchatel.savoy](./genomics/participants.md#uneuchatel.savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uneuchatel.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uneuchatel.geo.pdf)
- :material-file-search: **Runs:** [UniNeHug2c](./genomics/runs.md#uninehug2c) | [UniNeHug2](./genomics/runs.md#uninehug2)

??? abstract "Abstract"
	
	This paper describes our participation in TREC-2005 for the ad hoc Genomic track, in which we evaluate five different stemming approaches to performing domain-specific searches within a MEDLINE subset. We also evaluate the impact that manually assigned descriptors (MeSH headings) have on retrieval effectiveness. We design a domain-specific query expansion scheme and compare it with the more classic Rocchio approach. In our experiments on this collection subset, we discover that mean average precision does not improve when using different stemming algorithm. We then show how the presence of the MeSH headings significantly enhances mean average precision by about 9%. Finally, we illustrate how the use of various query expansion techniques can impairs retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbdouSR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbdouSR05,
		author = {Samir Abdou and Jacques Savoy and Patrick Ruch},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Evaluation of Stemming, Query Expansion and Manual Indexing Approaches for the Genomic Task},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uneuchatel.geo.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbdouSR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Genomics Track Experiments at IBM Watson

_Rie Kubota Ando, Mark Dredze, Tong Zhang_

- :fontawesome-solid-user-group: **Participant:** [ibm.zhang](./genomics/participants.md#ibm.zhang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm-tjwatson.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm-tjwatson.geo.pdf)
- :material-file-search: **Runs:** [ibmadz05bs](./genomics/runs.md#ibmadz05bs) | [ibmadz05us](./genomics/runs.md#ibmadz05us) | [aibmadz05m1](./genomics/runs.md#aibmadz05m1) | [eibmadz05m1](./genomics/runs.md#eibmadz05m1) | [gibmadz05m1](./genomics/runs.md#gibmadz05m1) | [tibmadz05m1](./genomics/runs.md#tibmadz05m1) | [aibmadz05m2](./genomics/runs.md#aibmadz05m2) | [eibmadz05m2](./genomics/runs.md#eibmadz05m2) | [gibmadz05m2](./genomics/runs.md#gibmadz05m2) | [tibmadz05m2](./genomics/runs.md#tibmadz05m2) | [aibmadz05s](./genomics/runs.md#aibmadz05s) | [eibmadz05s](./genomics/runs.md#eibmadz05s) | [gibmadz05s](./genomics/runs.md#gibmadz05s) | [tibmadz05s](./genomics/runs.md#tibmadz05s)

??? abstract "Abstract"
	
	This paper describes our experiments in the TREC 2005 Genomics Track. For the ad-hoc retrieval task, we study synonym-based query expan-sion, as well as the effectiveness of a new pseudo-relevance feedback method which is derived from our recent work on semi-supervised learning. For the categorization task, we study various methods for estimating conditional class probability and determining the optimal threshold parameter - essential for obtaining high performance results for this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AndoDZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AndoDZ05,
		author = {Rie Kubota Ando and Mark Dredze and Tong Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track Experiments at {IBM} Watson},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ibm-tjwatson.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AndoDZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fusion of Knowledge-Intensive and Statistical Approaches for Retrieving  and Annotating Textual Genomics Documents

_Alan R. Aronson, Dina Demner-Fushman, Susanne M. Humphrey, Jimmy Lin, Patrick Ruch, Miguel E. Ruiz, Lawrence H. Smith, Lorraine K. Tanabe, W. John Wilbur, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [nlm-umd.aronson](./genomics/participants.md#nlm-umd.aronson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/nlm-umd.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/nlm-umd.geo.pdf)
- :material-file-search: **Runs:** [NLMfusionA](./genomics/runs.md#nlmfusiona) | [NLMfusionB](./genomics/runs.md#nlmfusionb) | [aNLMF](./genomics/runs.md#anlmf) | [eNLMF](./genomics/runs.md#enlmf) | [gNLMF](./genomics/runs.md#gnlmf) | [tNLMF](./genomics/runs.md#tnlmf) | [NLM2A](./genomics/runs.md#nlm2a) | [NLM2E](./genomics/runs.md#nlm2e) | [NLM2G](./genomics/runs.md#nlm2g) | [NLM2T](./genomics/runs.md#nlm2t) | [aNLMB](./genomics/runs.md#anlmb) | [NLM1T](./genomics/runs.md#nlm1t) | [eNLMKNN](./genomics/runs.md#enlmknn) | [NLM1G](./genomics/runs.md#nlm1g)

??? abstract "Abstract"
	
	This paper represents a continuation of research into the retrieval and annotation of textual genomics documents (both MEDLINE® citations and full text articles) for the purpose of satisfying biologists' real information needs. The overall approach taken here for both the ad hoc retrieval and categorization tasks within the TREC genomics track in 2005 was one combining the results of several NLP, statistical and ML methods, using a fusion method for ad hoc retrieval and ensemble methods for categorization. The results show that fusion approaches can improve the final outcome for the ad hoc and the categorization tasks, but that care must be taken in order to take advantage of the strengths of the constituent methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AronsonDHLRRSTWL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AronsonDHLRRSTWL05,
		author = {Alan R. Aronson and Dina Demner{-}Fushman and Susanne M. Humphrey and Jimmy Lin and Patrick Ruch and Miguel E. Ruiz and Lawrence H. Smith and Lorraine K. Tanabe and W. John Wilbur and Hongfang Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Fusion of Knowledge-Intensive and Statistical Approaches for Retrieving and Annotating Textual Genomics Documents},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/nlm-umd.geo.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AronsonDHLRRSTWL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Classifying Biomedical Articles by Making Localized Decisions

_Thomas Brow, Burr Settles, Mark Craven_

- :fontawesome-solid-user-group: **Participant:** [uwisconsin.craven](./genomics/participants.md#uwisconsin.craven)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uwisconsin.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uwisconsin.geo.pdf)
- :material-file-search: **Runs:** [Afull](./genomics/runs.md#afull) | [Efull](./genomics/runs.md#efull) | [Gfull](./genomics/runs.md#gfull) | [Tfull](./genomics/runs.md#tfull) | [Apars](./genomics/runs.md#apars) | [Epars](./genomics/runs.md#epars) | [Gpars](./genomics/runs.md#gpars) | [Tpars](./genomics/runs.md#tpars) | [Ameta](./genomics/runs.md#ameta) | [Emeta](./genomics/runs.md#emeta) | [Gmeta](./genomics/runs.md#gmeta) | [Tmeta](./genomics/runs.md#tmeta)

??? abstract "Abstract"
	
	We describe a system developed for the Categorization task of the Text Retrieval Conference (TREC) 2005 Genomics track, and experiments we conducted in the process of developing our system. Our research effort for this task explored the hypothesis that more accurate predictions could be achieved by considering only selected passages in the documents being processed. We investigated methods that involve (i) basing classifications on selected passages from test articles, and (ii) adjusting the classifier training process such that certain putatively relevant passages affect the learned model more than other passages. Whereas the first approach was effective at improving predictive accuracy in our experiments, the latter approach was not
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrowSC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrowSC05,
		author = {Thomas Brow and Burr Settles and Mark Craven},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Classifying Biomedical Articles by Making Localized Decisions},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uwisconsin.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BrowSC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Structural Term Extraction for Expansion of Template-Based Genomic  Queries

_Fabrice Camous, Stephen Blott, Cathal Gurrin, Gareth J. F. Jones, Alan F. Smeaton_

- :fontawesome-solid-user-group: **Participant:** [dublincityu.gurrin](./genomics/participants.md#dublincityu.gurrin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dublincu.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/dublincu.geo.pdf)
- :material-file-search: **Runs:** [dcu1](./genomics/runs.md#dcu1) | [dcu2](./genomics/runs.md#dcu2)

??? abstract "Abstract"
	
	This paper describes our experiments run to address the ad hoc task of the TREC 2005 Genomics track. The task topics were expressed with 5 different structures called Generic Topic Templates (GTTs). We hypothesized the presence of GTT-specific structural terms in the free-text fields of documents relevant to a topic instantiated from that same GTT. Our experiments aimed at extracting and selecting candidate structural terms for each GTT. Selected terms were used to expand initial queries and the quality of the term selection was measured by the impact of the expansion on initial search results. The evaluation used the task training topics and the associated relevance information. This paper describes the two term extraction methods used in the experiments and the resulting two runs sent to NIST for evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CamousBGJS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CamousBGJS05,
		author = {Fabrice Camous and Stephen Blott and Cathal Gurrin and Gareth J. F. Jones and Alan F. Smeaton},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Structural Term Extraction for Expansion of Template-Based Genomic Queries},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/dublincu.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CamousBGJS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept Recognition and the TREC Genomics Tasks

_J. Gregory Caporaso, William A. Baumgartner Jr., K. Bretonnel Cohen, Helen L. Johnson, Jesse Paquette, Lawrence Hunter_

- :fontawesome-solid-user-group: **Participant:** [ucolorado.cohen](./genomics/participants.md#ucolorado.cohen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ucolorado-hsc.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/ucolorado-hsc.geo.pdf)
- :material-file-search: **Runs:** [CCP0](./genomics/runs.md#ccp0) | [CCP1](./genomics/runs.md#ccp1) | [aUCHSCnb1En3](./genomics/runs.md#auchscnb1en3) | [eUCHSCnb1En3](./genomics/runs.md#euchscnb1en3) | [gUCHSCnb1En3](./genomics/runs.md#guchscnb1en3) | [tUCHSCnb1En3](./genomics/runs.md#tuchscnb1en3) | [aUCHSCnb1En4](./genomics/runs.md#auchscnb1en4) | [eUCHSCnb1En4](./genomics/runs.md#euchscnb1en4) | [gUCHSCnb1En4](./genomics/runs.md#guchscnb1en4) | [tUCHSCnb1En4](./genomics/runs.md#tuchscnb1en4) | [aUCHSCsvm](./genomics/runs.md#auchscsvm) | [eUCHSCsvm](./genomics/runs.md#euchscsvm) | [gUCHSCsvm](./genomics/runs.md#guchscsvm) | [tUCHSCsvm](./genomics/runs.md#tuchscsvm)

??? abstract "Abstract"
	
	We applied concept recognition techniques to the Genomics track primary and secondary tasks. For the primary task, we developed a foundational information retrieval system which incorporated Entrez Gene entries and UMLS concepts for query expansion via phrasal and term boosting representations of synonyms. For the secondary task, we evaluated three conceptual features—mouse strain names, indexed MeSH terms, and normalized citations—in addition to two surface linguistic features—BOW and bigrams. Our final feature set yielded consistently high F-measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaporasoBCJPH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaporasoBCJPH05,
		author = {J. Gregory Caporaso and William A. Baumgartner Jr. and K. Bretonnel Cohen and Helen L. Johnson and Jesse Paquette and Lawrence Hunter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concept Recognition and the {TREC} Genomics Tasks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ucolorado-hsc.geo.pdf},
		timestamp = {Tue, 26 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CaporasoBCJPH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DIMACS at the TREC 2005 Genomics Track

_Aynur A. Dayanik, Alexander Genkin, Paul B. Kantor, David D. Lewis, David Madigan_

- :fontawesome-solid-user-group: **Participant:** [rutgers.dayanik](./genomics/participants.md#rutgers.dayanik)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/rutgersu-dimacs.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/rutgersu-dimacs.geo.pdf)
- :material-file-search: **Runs:** [aDIMACSg9md](./genomics/runs.md#adimacsg9md) | [eDIMACSg9md](./genomics/runs.md#edimacsg9md) | [gDIMACSg9md](./genomics/runs.md#gdimacsg9md) | [tDIMACSg9md](./genomics/runs.md#tdimacsg9md) | [aDIMACSg9w](./genomics/runs.md#adimacsg9w) | [eDIMACSg9w](./genomics/runs.md#edimacsg9w) | [gDIMACSg9w](./genomics/runs.md#gdimacsg9w) | [tDIMACSg9w](./genomics/runs.md#tdimacsg9w) | [aDIMACSl9w](./genomics/runs.md#adimacsl9w) | [eDIMACSl9w](./genomics/runs.md#edimacsl9w) | [gDIMACSl9w](./genomics/runs.md#gdimacsl9w) | [tDIMACSl9w](./genomics/runs.md#tdimacsl9w) | [aDIMACSl9md](./genomics/runs.md#adimacsl9md) | [eDIMACSl9md](./genomics/runs.md#edimacsl9md) | [gDIMACSl9md](./genomics/runs.md#gdimacsl9md) | [tDIMACSl9md](./genomics/runs.md#tdimacsl9md)

??? abstract "Abstract"
	
	This report describes DIMACS work on the text categorization task of the TREC 2005 Genomics track. Our approach to this task was similar to the triage subtask studied in the TREC 2004 Genomics track. We applied Bayesian logistic regression and achieved good effectiveness on all categories.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DayanikGKLM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/DayanikGKLM05,
		author = {Aynur A. Dayanik and Alexander Genkin and Paul B. Kantor and David D. Lewis and David Madigan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DIMACS} at the {TREC} 2005 Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/rutgersu-dimacs.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DayanikGKLM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Questions and Relationships at the University of Iowa

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [uiowa.eichmann](./genomics/participants.md#uiowa.eichmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf)
- :material-file-search: **Runs:** [UIowa05GN101](./genomics/runs.md#uiowa05gn101) | [UIowa05GN102](./genomics/runs.md#uiowa05gn102)

??? abstract "Abstract"
	
	The University of Iowa participated in the genomics and question answering tracks of TREC-2005. This paper covers only our work in question answering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS05,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Questions and Relationships at the University of Iowa},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSUSM at TREC 2005: Genomics and Enterprise Track

_Rocio Guillén_

- :fontawesome-solid-user-group: **Participant:** [csusm.guillen](./genomics/participants.md#csusm.guillen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/calstateu-sanmarcos.geo.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/calstateu-sanmarcos.geo.ent.pdf)
- :material-file-search: **Runs:** [genome1](./genomics/runs.md#genome1) | [genome2](./genomics/runs.md#genome2) | [Tcsusm1](./genomics/runs.md#tcsusm1) | [Tcsusm2](./genomics/runs.md#tcsusm2)

??? abstract "Abstract"
	
	In this paper we report on the approach, experiments and results for the Enterprise Track and the Genomics Track. We participated in the adhoc and one of the categorization tasks for the Genomics track. For the enterprise track we participated in the known-item search. We ran experiments using Indri (1], which combines inference networks with language modeling, for the adhoc and the known-item search tasks. For the categorization task we filtered the documents in different stages using decision trees.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Guillen05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Guillen05,
		author = {Rocio Guill{\'{e}}n},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CSUSM} at {TREC} 2005: Genomics and Enterprise Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/calstateu-sanmarcos.geo.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Guillen05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UM-D at TREC 2005: Genomics Track

_Liping Huang, ZhiHang Chen, Yi Lu Murphey_

- :fontawesome-solid-user-group: **Participant:** [umichigan-dearborn.murphey](./genomics/participants.md#umichigan-dearborn.murphey)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umich-dearborn.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/umich-dearborn.geo.pdf)
- :material-file-search: **Runs:** [UMD01](./genomics/runs.md#umd01) | [UMD02](./genomics/runs.md#umd02)

??? abstract "Abstract"
	
	The University of Michigan-Dearborn team participated in the ad hoc task and submitted two runs in TREC 2005. The Genomics track is different from others since it focuses on document retrieval in genomics domain as opposed to general retrieval tasks such as question-answering, multi-lingual IR, etc. Since we were not familiar with the knowledge in biomedical field, we utilized the database publicly available online to obtain alias and variations of names for genes/proteins. We generated a term list based on each topic description and their alias and variations. The terms were further transformed into a logical expression in which terms were connected by “AND” and “OR”. The documents satisfying the logical expression are retrieved and their similarity scores are calculated based on the weighted terms using the method of Okapi BM25 proposed by Robertson et al[RWJ94][RWB98] [BCC04].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangCM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangCM05,
		author = {Liping Huang and ZhiHang Chen and Yi Lu Murphey},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UM-D} at {TREC} 2005: Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umich-dearborn.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HuangCM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2005: Genomics Track

_Xiangji Huang, Ming Zhong, Luo Si_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./genomics/participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/yorku-huang2.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/yorku-huang2.geo.pdf)
- :material-file-search: **Runs:** [york05ga1](./genomics/runs.md#york05ga1) | [york05gm1](./genomics/runs.md#york05gm1) | [york05ga2](./genomics/runs.md#york05ga2) | [york05ga3](./genomics/runs.md#york05ga3) | [york05ga4](./genomics/runs.md#york05ga4) | [york05ga5](./genomics/runs.md#york05ga5)

??? abstract "Abstract"
	
	Our Genomics experiments mainly focus on addressing three major problems in biomedical information retrieval. The three problems are: (1) how to deal with synonyms? (2) how to deal with the frequent use of acronyms? (3) how to deal with homonyms? In particular, we propose two query expansion algorithms to construct structured queries for our experiments. The mean average precision (MAP) for our automatic run “york05ga1” using Algorithm 1 was 0.2888 and for our manual run “york05gm1” using Algorithm 2 was 0.3020. The evaluation results show that both algorithms are effective for improving retrieval performance. We also find that some other techniques such as pseudo-relevance feedback and using an extended stop word set can make positive contributions to the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangZS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangZS05,
		author = {Xiangji Huang and Ming Zhong and Luo Si},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2005: Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/yorku-huang2.geo.pdf},
		timestamp = {Tue, 05 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangZS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pattern Based Customized Learning for TREC Genomics Track Categorization  Task

_Wai Lam, Yiqiu Han, Ki Chan_

- :fontawesome-solid-user-group: **Participant:** [cuhk.lam](./genomics/participants.md#cuhk.lam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/chineseu-hongkong-lam.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/chineseu-hongkong-lam.geo.pdf)
- :material-file-search: **Runs:** [cuhkrun1](./genomics/runs.md#cuhkrun1) | [cuhkrun1E](./genomics/runs.md#cuhkrun1e) | [cuhkrun1G](./genomics/runs.md#cuhkrun1g) | [cuhkrun1T](./genomics/runs.md#cuhkrun1t) | [cuhkrun2A](./genomics/runs.md#cuhkrun2a) | [cuhkrun2E](./genomics/runs.md#cuhkrun2e) | [cuhkrun2G](./genomics/runs.md#cuhkrun2g) | [cuhkrun2T](./genomics/runs.md#cuhkrun2t) | [cuhkrun3A](./genomics/runs.md#cuhkrun3a) | [cuhkrun3G](./genomics/runs.md#cuhkrun3g) | [cuhkrun3T](./genomics/runs.md#cuhkrun3t) | [cuhkrun3E](./genomics/runs.md#cuhkrun3e)

??? abstract "Abstract"
	
	Our group participated in the categorization task in the TREC Genomics Track  2005, where biological literatures have to be categorized into four types of information. Our approach to this problem adopts customized learning methods in model learning  and document categorization. Our pattern-based learning approach can discover useful patterns for tackling categorization challenges.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LamHC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LamHC05,
		author = {Wai Lam and Yiqiu Han and Ki Chan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pattern Based Customized Learning for {TREC} Genomics Track Categorization Task},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/chineseu-hongkong-lam.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LamHC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Identifying Relevant Full-Text Articles for Database Curation

_Chih Lee, Wen-Juan Hou, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./genomics/participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ntu.geo.cate.pdf](http://trec.nist.gov/pubs/trec14/papers/ntu.geo.cate.pdf)
- :material-file-search: **Runs:** [NTUgah1](./genomics/runs.md#ntugah1) | [NTUgah2](./genomics/runs.md#ntugah2) | [aNTUMAC](./genomics/runs.md#antumac) | [tNTUMAC](./genomics/runs.md#tntumac) | [eNTUMAC](./genomics/runs.md#entumac) | [gNTUMAC](./genomics/runs.md#gntumac) | [tNTUMACasem](./genomics/runs.md#tntumacasem) | [tNTUMACwj](./genomics/runs.md#tntumacwj)

??? abstract "Abstract"
	
	In this paper, we propose an approach for identifying curatable articles from a large pool. Our system currently considers three parts of an article as three individual representations of the article, and utilizes two domain-specific resources to reveal the deep knowledge contained in the article in order to generate more representations of the article. Cross-validation is employed to find the best combination of representations and an SVM classifier is trained out of this combination. The cross-validation results and results of the official runs are listed. The experimental results show overall high performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeHC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeHC05,
		author = {Chih Lee and Wen{-}Juan Hou and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Identifying Relevant Full-Text Articles for Database Curation},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ntu.geo.cate.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeHC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Learning Domain-Specific Knowledge from Context–THUIR at TREC 2005  Genomics Track

_Jiao Li, Xian Zhang, Yu Hao, Minlie Huang, Xiaoyan Zhu_

- :fontawesome-solid-user-group: **Participant:** [tsinghua.ma](./genomics/participants.md#tsinghua.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.geo.pdf)
- :material-file-search: **Runs:** [THUIRgen1S](./genomics/runs.md#thuirgen1s) | [THUIRgen2P](./genomics/runs.md#thuirgen2p) | [THUIRgenA1p1](./genomics/runs.md#thuirgena1p1) | [THUIRgenE1p8](./genomics/runs.md#thuirgene1p8) | [THUIRgenG1p1](./genomics/runs.md#thuirgeng1p1) | [THUIRgenT1p5](./genomics/runs.md#thuirgent1p5) | [THUIRgenGMNG](./genomics/runs.md#thuirgengmng) | [THUIRgA0p9x](./genomics/runs.md#thuirga0p9x)

??? abstract "Abstract"
	
	We(Tsinghua University) participated both Ad Hoc Retrieval Task and Categorization Task in TREC2005 Genomics Track, in which we designed and implemented a serious of methods encompassed learning domain-specific knowledge from context. In Ad Hoc Retrieval Task, internal resource is introduced to expand query, different granularity indexing provides more flexible retrieval space, and pattern discovering imports Information Extraction (IE) concept into Information Retrieval (IR). In Categorization Task, instead of the single word feature, we presented Seed-based Loose N-gram Feature, which achieved success in the four subtasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiZHHZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiZHHZ05,
		author = {Jiao Li and Xian Zhang and Yu Hao and Minlie Huang and Xiaoyan Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Learning Domain-Specific Knowledge from Context--THUIR at {TREC} 2005 Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.geo.pdf},
		timestamp = {Thu, 02 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiZHHZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Menagerie of Tracks at Maryland: HARD, Enterprise, QA, and Genomics,  Oh My!

_Jimmy Lin, Eileen G. Abels, Dina Demner-Fushman, Douglas W. Oard, Philip Fei Wu, Yejun Wu_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./genomics/participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf)
- :material-file-search: **Runs:** [MARYGEN1](./genomics/runs.md#marygen1)

??? abstract "Abstract"
	
	This year, the University of Maryland participated in four separate tracks: HARD, enterprise, question answering, and genomics. Our HARD experiments involved a trained intermediary who searched for documents on behalf of the user, created clarification forms manually, and exploited user responses accordingly. The aim was to better understand the nature of single-iteration clarification dialogs and to develop an “ontology of clarifications” that can be leveraged to guide system development. For the enterprise track, we submitted official runs to the Known Item Search and the Discussion Search tasks. Document transformation to normalize dates and version numbers was found to be helpful, but suppression of text quoted from earlier messages and expansion of the indexed terms for a message based on subject line threading proved to not be. For the QA track, we submitted a manual run of “other” questions in an effort to quantify human performance on the task. Our genomics track participation was in collaboration with the National Library of Medicine, and is primarily reported in NLM's overview paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinADOWW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinADOWW05,
		author = {Jimmy Lin and Eileen G. Abels and Dina Demner{-}Fushman and Douglas W. Oard and Philip Fei Wu and Yejun Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Menagerie of Tracks at Maryland: HARD, Enterprise, QA, and Genomics, Oh My!},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf},
		timestamp = {Sat, 29 Jul 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinADOWW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Thesauri-Based Methods for Biomedical Retrieval

_Edgar Meij, Leonie IJzereef, Leif Azzopardi, Jaap Kamps, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.aidteam](./genomics/participants.md#uamsterdam.aidteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uamsterdam-infoinst.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uamsterdam-infoinst.geo.pdf)
- :material-file-search: **Runs:** [UAmscombGeFb](./genomics/runs.md#uamscombgefb) | [UAmscombGeMl](./genomics/runs.md#uamscombgeml)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2005 Genomics track. We took part in the ad hoc retrieval task and aimed at integrating thesauri in the retrieval model. We developed three thesauri-based methods, two of which made use of the existing MeSH thesaurus. One method uses blind relevance feedback on MeSH terms, the second uses an index of the MeSH thesaurus for query expansion. The third method makes use of a dynamically generated lookup list, by which acronyms and synonyms could be inferred. We show that, despite the relatively minor improvements in retrieval performance of individually applied methods, a combination works best and is able to deliver significant improvements over the baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeijIAKR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeijIAKR05,
		author = {Edgar Meij and Leonie IJzereef and Leif Azzopardi and Jaap Kamps and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Thesauri-Based Methods for Biomedical Retrieval},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uamsterdam-infoinst.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MeijIAKR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIM at TREC 2005

_Junyu Niu, Lin Sun, Luqun Lou, Fang Deng, Chen Lin, Haiqing Zheng, Xuanjing Huang_

- :fontawesome-solid-user-group: **Participant:** [fudan.niu](./genomics/participants.md#fudan.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/fudanu-sun.geo.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/fudanu-sun.geo.ent.pdf)
- :material-file-search: **Runs:** [wim1](./genomics/runs.md#wim1) | [wim2](./genomics/runs.md#wim2) | [aFduMarsI](./genomics/runs.md#afdumarsi) | [eFduMarsI](./genomics/runs.md#efdumarsi) | [gFduMarsI](./genomics/runs.md#gfdumarsi) | [tFduMarsI](./genomics/runs.md#tfdumarsi) | [aFduMarsII](./genomics/runs.md#afdumarsii) | [eFduMarsII](./genomics/runs.md#efdumarsii) | [gFduMarsII](./genomics/runs.md#gfdumarsii) | [tFduMarsII](./genomics/runs.md#tfdumarsii) | [aFduMarsIII](./genomics/runs.md#afdumarsiii) | [eFduMarsIII](./genomics/runs.md#efdumarsiii) | [gFduMarsIII](./genomics/runs.md#gfdumarsiii) | [tFduMarsIII](./genomics/runs.md#tfdumarsiii)

??? abstract "Abstract"
	
	This paper describes the three TREC tasks we participated in this year, which are, Genomics track's categorization task and ad hoc task, and Enterprise track's known item search task. For the categorization task, we adopt a domain-specific terms extraction method and an ontology-based method for feature selection. A SVM classifier and a Rocchio based two staged classifier were also used in this experiment. For the ad-hoc task, we used BM25 algorithm, probabilistic model and query expansion. For the Enterprise track, language model was adopted, and entity recognition was also implemented in our experiment.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NiuSLDLZH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/NiuSLDLZH05,
		author = {Junyu Niu and Lin Sun and Luqun Lou and Fang Deng and Chen Lin and Haiqing Zheng and Xuanjing Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIM} at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/fudanu-sun.geo.ent.pdf},
		timestamp = {Tue, 20 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NiuSLDLZH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Genomics Track Experiments at UTA

_Ari Pirkola_

- :fontawesome-solid-user-group: **Participant:** [utampere.pirkola](./genomics/participants.md#utampere.pirkola)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/utampere.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/utampere.geo.pdf)
- :material-file-search: **Runs:** [uta05a](./genomics/runs.md#uta05a) | [uta05i](./genomics/runs.md#uta05i)

??? abstract "Abstract"
	
	University of Tampere submitted runs for Genomics Track ad hoc retrieval task. The first run (uta05a) was an automatic and the second (uta05i) an interactive run. The uta05a queries were constructed by using the original topic terms as query keys. The uta05a queries served as a baseline for the uta05i queries which were constructed by expanding the uta05a queries with synonyms for the topic gene names from the Entrez Gene database and by further expanding with synonymous gene names and MH terms from the top documents of an initial uta05i search. The mean average precision for uta05a was 0.2385 and for uta05i 0.1980. Next in Section 2.1 we present the indexing methods and the processing of query keys. Section 2.2 considers the retrieval system and query operators. Query formulation is presented in Section 2.3. Section 3 contains the results and conclusions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Pirkola05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Pirkola05,
		author = {Ari Pirkola},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track Experiments at {UTA}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/utampere.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Pirkola05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2005 Experiment: Genomics Track

_Patrick Ruch, Frédéric Ehrler, Samir Abdou, Jacques Savoy_

- :fontawesome-solid-user-group: **Participant:** [u.geneva](./genomics/participants.md#u.geneva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uhospital-geneva.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uhospital-geneva.geo.pdf)
- :material-file-search: **Runs:** [UniGeNe](./genomics/runs.md#unigene) | [UniGe2](./genomics/runs.md#unige2)

??? abstract "Abstract"
	
	This year, for our participation to the TREC Genomics track, we participated in the two tasks: the ad hoc and the categorization task. In this notebook report, we do not detail our experiments, which will be described more precisely in the final proceedings. This papers focuses on the ad hoc task, while experiments conducted for task 2 are described in the Aronson and al. 2005. Task I. For the ad hoc retrieval task, we used the easyIR tool, a standard vector-space engine developed at the University of Geneva. Our approach uses thesaural resources together with a variant of the Porter stemmer for string normalization. Gene and Protein Entities (GPE) in queries are marked up by dictionary look up at retrieval time in order to be expanded using a gene and protein thesaurus. For indexing the Genomic collection, the following MEDLINE records were selected: article's titles, MeSH and RN terms, and abstract fields. Following observations made on MEDLINE documents regarding their length distribution, we decided to rely on a slightly modified dtu.dtn weighting schema. This constitutes our baseline run (Baseline=0.2312; Baseline+expansion=0.2373). Finally, we used a run provided by the University of Neuchâtel, which features thesaurus-based GPE expansion and automatic feed back (UniGeNe=0.2150) to produce a third run, which achieved our best results (UniGe2=0.2396).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuchEAS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuchEAS05,
		author = {Patrick Ruch and Fr{\'{e}}d{\'{e}}ric Ehrler and Samir Abdou and Jacques Savoy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2005 Experiment: Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uhospital-geneva.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuchEAS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on Genomics Ad Hoc Retrieval

_Miguel E. Ruiz_

- :fontawesome-solid-user-group: **Participant:** [suny-buffalo.ruiz](./genomics/participants.md#suny-buffalo.ruiz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/stateu-ny-buffalo.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/stateu-ny-buffalo.geo.pdf)
- :material-file-search: **Runs:** [UBIgeneA](./genomics/runs.md#ubigenea)

??? abstract "Abstract"
	
	This paper represents te results of the State University of New York at Buffalo (School of Informatics) in the TREC 2005 Conference. We participated in the Genomics ad hoc retrieval task. Our approach used the SMART system for indexing the large collection of MEDLINE documents. For this purpose we used a distributed retrieval approach and divided the large collection into 5 non overlapping sub collections. We tried several approaches on the training topics to select the best run possible. Our results perform slightly above the median system in the conference. We also paired with the NLM team to contribute a run for their fusion approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Ruiz05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Ruiz05,
		author = {Miguel E. Ruiz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments on Genomics Ad Hoc Retrieval},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/stateu-ny-buffalo.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Ruiz05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Genomics Track A Concept-Based Approach to Text Categorization

_Bob J. A. Schijvenaars, Martijn J. Schuemie, Erik M. van Mulligen, Marc Weeber, Rob Jelier, Barend Mons, Jan A. Kors, Wessel Kraaij_

- :fontawesome-solid-user-group: **Participant:** [erasmus.kors](./genomics/participants.md#erasmus.kors)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/erasmus-tno.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/erasmus-tno.geo.pdf)
- :material-file-search: **Runs:** [ABPLUS](./genomics/runs.md#abplus) | [ABPLUSE](./genomics/runs.md#abpluse) | [ABPLUSG](./genomics/runs.md#abplusg) | [ABPLUST](./genomics/runs.md#abplust) | [FTA](./genomics/runs.md#fta) | [FTE](./genomics/runs.md#fte) | [FTT](./genomics/runs.md#ftt) | [FTG](./genomics/runs.md#ftg)

??? abstract "Abstract"
	
	The Biosemantics group (Erasmus University Medical Center, Rotterdam) participated in the text categorization task of the Genomics Track. We followed a thesaurus-based approach, using the Collexis indexing system, in combination with a simple classification algorithm to assign a document to one of the four categories. Our thesaurus consisted of a combination of MeSH, Gene Ontology, and a thesaurus with gene and protein symbols and names extracted from the Mouse Genome Database, Swiss-Prot and Entrez Gene. To increase the coverage of the gene thesaurus, several rewrite rules were applied to take possible spelling variations into account. Each document in the training set was indexed and the found concepts were ranked on term frequency, resulting in one concept vector per document. No particular care was taken to resolve ambiguous terms. For each of the four categories, two average concept vectors were computed, one by averaging the concept vectors of the documents in that category and the other by averaging all remaining concept vectors. The latter vector was then subtracted from the first, yielding a final category concept vector. The subtraction served to emphasize distinguishing concepts: high-ranked concepts in the final concept vector should, on average, occur relatively frequently in documents belonging to the category, while occurring infrequently or not at all in documents not belonging to the category. For all documents in the training set, a matching score between the concept vector of a document and each of the category concept vectors was computed. A score threshold to discriminate between category and non-category documents was then determined per category by optimizing the performance measure (normalized utility). Different matching algorithms and different cutoffs for the number of concepts in the category vectors were evaluated. A standard cosine similarity score and a category vector with the 40 highest-ranking concepts proved to perform best on the training set. These settings and the score thresholds were subsequently used to categorize all documents in the test set. Two runs were submitted: one based on the full text without any special treatment of particular sections, and one based on the Medline abstract, including the title and the MeSH headings. In addition two runs were submitted by TNO for the ad-hoc search task. The ad-hoc system was based on the TREC 2004 system, with a small experiment trying to leverage information about the authority level of specific journals.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchijvenaarsSMWJMKK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchijvenaarsSMWJMKK05,
		author = {Bob J. A. Schijvenaars and Martijn J. Schuemie and Erik M. van Mulligen and Marc Weeber and Rob Jelier and Barend Mons and Jan A. Kors and Wessel Kraaij},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track {A} Concept-Based Approach to Text Categorization},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/erasmus-tno.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchijvenaarsSMWJMKK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Synonym-Based Expansion and Boosting-Based Re-Ranking: A Two-phase  Approach for Genomic Information Retrieval

_Zhongmin Shi, Baohua Gu, Fred Popowich, Anoop Sarkar_

- :fontawesome-solid-user-group: **Participant:** [simon-fraseru.shi](./genomics/participants.md#simon-fraseru.shi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/simon-fraseru.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/simon-fraseru.geo.pdf)
- :material-file-search: **Runs:** [SFUshi](./genomics/runs.md#sfushi)

??? abstract "Abstract"
	
	We describe in this paper the design and evaluation of the system built at Simon Fraser University for the TREC 2005 adhoc retrieval task in the Genomics track. The main approach taken in our system was to expand synonyms by exploiting a fusion of a set of biomedical and general ontology sources, and apply machine learning and natural language processing techniques to re-rank retrieved documents. In our system, we integrated EntrezGene, HUGO, Eugenes, ARGH, GO, MeSH, UMLSKS and WordNet into a large reference database and then used a conventional Information Retrieval (IR) toolkit, the Lemur toolkit (Lemur, 2005), to build an IR system. In the post-processing phase, we applied a boosting algorithm (Kudo and Matsumoto, 2004) that captured natural language substructures embedded in texts to re-rank the retrieved documents. Experimental results show that the boosting algorithm worked well in cases where a conventional IR system performs poorly, but this re-ranking approach was not robust enough when applied to broad coverage task typically associated with IR.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShiGPS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShiGPS05,
		author = {Zhongmin Shi and Baohua Gu and Fred Popowich and Anoop Sarkar},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Synonym-Based Expansion and Boosting-Based Re-Ranking: {A} Two-phase Approach for Genomic Information Retrieval},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/simon-fraseru.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShiGPS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Thresholding Strategies for Text Classifiers: TREC 2005 Biomedical  Triage Task Experiments

_Luo Si, Tapas Kanungo_

- :fontawesome-solid-user-group: **Participant:** [ibm.kanungo](./genomics/participants.md#ibm.kanungo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-kanungo.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-kanungo.geo.pdf)
- :material-file-search: **Runs:** [ABBR003](./genomics/runs.md#abbr003) | [ABBR003SThr](./genomics/runs.md#abbr003sthr) | [ASVMN03](./genomics/runs.md#asvmn03) | [EBBR0006](./genomics/runs.md#ebbr0006) | [EBBR0006SThr](./genomics/runs.md#ebbr0006sthr) | [ESVMN075](./genomics/runs.md#esvmn075) | [GAbsBBR0083](./genomics/runs.md#gabsbbr0083) | [GBBR004](./genomics/runs.md#gbbr004) | [GSVMN08](./genomics/runs.md#gsvmn08) | [TBBR0004](./genomics/runs.md#tbbr0004) | [TBBR0004SThr](./genomics/runs.md#tbbr0004sthr) | [TSVM0035](./genomics/runs.md#tsvm0035)

??? abstract "Abstract"
	
	We participated in the triage task of biomedical documents in the TREC genomic track. In this paper we describe the methods we developed for the four triage1subtasks. Logistic regression and support vector machine algorithms were first trained to generate ranked lists of test documents. Then a subset of the test documents was identified as positive instances by selecting the top-k documents of the ranked lists. Deciding on the ideal value for k requires a good thresholding strategy. In this paper we first describe two thresholding strategies based on i) logistic regression and ii) support vector machines. In addition to these methods, we describe a thresholding method that combines the outputs from logistic regression and support vector machine by applying a joint thresholding strategy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SiK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/SiK05,
		author = {Luo Si and Tapas Kanungo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Thresholding Strategies for Text Classifiers: {TREC} 2005 Biomedical Triage Task Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-kanungo.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SiK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Biomedical Document Triage: Automatic Classification Exploiting Category  Specific Knowledge

_L. Venkata Subramaniam, Sougata Mukherjea, Diwakar Punjani_

- :fontawesome-solid-user-group: **Participant:** [ibm-india.ramakrishnan](./genomics/participants.md#ibm-india.ramakrishnan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm-india.subramaniam.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm-india.subramaniam.geo.pdf)
- :material-file-search: **Runs:** [aIBMIRLsvm](./genomics/runs.md#aibmirlsvm) | [aIBMIRLrul](./genomics/runs.md#aibmirlrul) | [aIBMIRLmet](./genomics/runs.md#aibmirlmet) | [eIBMIRLsvm](./genomics/runs.md#eibmirlsvm) | [eIBMIRLrul](./genomics/runs.md#eibmirlrul) | [eIBMIRLmet](./genomics/runs.md#eibmirlmet) | [gIBMIRLsvm](./genomics/runs.md#gibmirlsvm) | [gIBMIRLrul](./genomics/runs.md#gibmirlrul) | [gIBMIRLmet](./genomics/runs.md#gibmirlmet) | [tIBMIRLsvm](./genomics/runs.md#tibmirlsvm) | [tIBMIRLrul](./genomics/runs.md#tibmirlrul) | [tIBMIRLmet](./genomics/runs.md#tibmirlmet)

??? abstract "Abstract"
	
	We approached the problem of categorizing papers for the 2005 TREC Genomics Track Categorization task in three different ways. In the first, we used a machine learning based approach. We used the MeSH ontology and other specialized ontologies from MGI to identify the set of features to be used in the classification. In the second, for each of the categories, we identified a set of terms to use for filtering the articles. In the third, combined approach, we used the machine learning based approach on the filtered set of articles. In all three approaches we incorporate biological knowledge about the classes into the classification system to achieve improved utility.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SubramaniamMP05.bib) "
	```
	@inproceedings{DBLP:conf/trec/SubramaniamMP05,
		author = {L. Venkata Subramaniam and Sougata Mukherjea and Diwakar Punjani},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Biomedical Document Triage: Automatic Classification Exploiting Category Specific Knowledge},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ibm-india.subramaniam.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SubramaniamMP05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Enhance Genomic IR with Term Variation and Expansion: Experience  of the IASL Group at Genomic Track 2005

_Tsung-Han Tsai, Chia-Wei Wu, Hsieh-Chuan Hung, Yu-Chun Wang, Ding He, Yi-Feng Lin, Cheng-Wei Lee, Ting-Yi Sung, Wen-Lian Hsu_

- :fontawesome-solid-user-group: **Participant:** [academia.sinica.tsai](./genomics/participants.md#academia.sinica.tsai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/academia-sinica.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/academia-sinica.geo.pdf)
- :material-file-search: **Runs:** [iasl1](./genomics/runs.md#iasl1) | [iasl2](./genomics/runs.md#iasl2)

??? abstract "Abstract"
	
	The rapid increase of biomedical literature available on the web has made it increasingly difficult to find precise information. To implement an accurate biomedical information retrieval (IR) system, we must deal with the variants of biomedical terms carefully. In this paper, we focus on the generation of aliases, synonyms, acronyms, and lexical variants of such terms. In addition, we also propose a hyphen handling technique for processing hyphenated terms. We use the original terms/phrases, and expanded terms/phrases to construct an Indri query, and evaluate the effectiveness of various methods by two indicators: MAP, and recall. Our experiment results show that tackling hyphenation improves information retrieval significantly. In addition, synonym expansion also enhances IR performance when the focus of a query is identified. For a natural language query, deep semantic analysis and more knowledge-oriented expansion should be applied.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TsaiWHWHLLSH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/TsaiWHWHLLSH05,
		author = {Tsung{-}Han Tsai and Chia{-}Wei Wu and Hsieh{-}Chuan Hung and Yu{-}Chun Wang and Ding He and Yi{-}Feng Lin and Cheng{-}Wei Lee and Ting{-}Yi Sung and Wen{-}Lian Hsu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Enhance Genomic {IR} with Term Variation and Expansion: Experience of the {IASL} Group at Genomic Track 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/academia-sinica.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TsaiWHWHLLSH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT TREC 2005: Genomics Track

_Jay Urbain, Nazli Goharian, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [iit.urbain](./genomics/participants.md#iit.urbain)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/iit-urbain.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/iit-urbain.geo.pdf)
- :material-file-search: **Runs:** [iitprf011003](./genomics/runs.md#iitprf011003)

??? abstract "Abstract"
	
	For the TREC-2005 Genomics Track ad-hoc retrieval task, we report on the development of a scalable information retrieval engine based on a relational data model for the integration of structured data and text. Our objectives are to meet the need for the integrated search of heterogeneous data sets of biomedical literature and structured data found in biological databases, and to demonstrate the efficacy of using a relational database for a large biomedical information retrieval application. Utilizing pivoted document normalization (PN) [1], pseudo relevance feedback [2, 3], and without performing stemming or domain specific normalization of biological terms, we received a mean average precision (MAP) of 0.1913 that places our results at the median of 32 Genomics track ad-hoc retrieval participants. Subsequent to our participation in TREC, we have added a new gene/protein term normalization scheme, and have evaluated additional retrieval strategies including: BM25 [15], pivoted unique normalization [1], and language models utilizing absolute discounting, Dirichlet, and Jelinek-Mercer smoothing techniques [12, 13, 16]. With the addition of Porter stemming [17], gene/protein term normalization, and the BM25 probabilistic retrieval strategy, we received a MAP of 0.2879 that places us among the top results for official manual runs reported for the TREC Genomics track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UrbainGF05.bib) "
	```
	@inproceedings{DBLP:conf/trec/UrbainGF05,
		author = {Jay Urbain and Nazli Goharian and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} {TREC} 2005: Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/iit-urbain.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UrbainGF05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Genomics Track Experiments at DUTAI

_Zhihao Yang, Hongfei Lin, Yanpeng Li, Baoyan Liu, Ye Lu_

- :fontawesome-solid-user-group: **Participant:** [dalianu.yang](./genomics/participants.md#dalianu.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dalianu.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/dalianu.geo.pdf)
- :material-file-search: **Runs:** [DUTAdHoc1](./genomics/runs.md#dutadhoc1) | [DUTAdHoc2](./genomics/runs.md#dutadhoc2) | [aDUTCat1](./genomics/runs.md#adutcat1) | [eDUTCat1](./genomics/runs.md#edutcat1) | [gDUTCat1](./genomics/runs.md#gdutcat1) | [tDUTCat1](./genomics/runs.md#tdutcat1) | [aDUTCat2](./genomics/runs.md#adutcat2) | [eDUTCat2](./genomics/runs.md#edutcat2) | [gDUTCat2](./genomics/runs.md#gdutcat2) | [tDUTCat2](./genomics/runs.md#tdutcat2)

??? abstract "Abstract"
	
	This paper describes the techniques we applied for the two tasks of the TREC Genomics track, i.e., ad hoc retrieval and categorization tasks. For the ad hoc retrieval task, we used query expansion, different scoring strategy on different parts of Medline record (Title, Abstract, RN, MH, etc.) and pseudo relevance feedback. Our submitted run DUTAdHoc2 obtained a MAP of 0.2349. For the categorization task, our system used a SVM classifier with TFIDF term weighting scheme. In addition concept replacing and filtering methods were adopted. Two of our submitted runs (eDUTCat1 and gDUTCat1) produced a Utility score of 0.8496 and 0.572 respectively ranking third and fourth out of 46 runs submitted for the categorization task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLLLL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangLLLL05,
		author = {Zhihao Yang and Hongfei Lin and Yanpeng Li and Baoyan Liu and Ye Lu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track Experiments at {DUTAI}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/dalianu.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLLLL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Genomic Information Retrieval Through Selective Extraction and Tagging  by the ASU-BioAL Group

_Lian Yu, Syed Toufeeq Ahmed, Graciela Gonzalez, Brendan Logsdon, Mutsumi Nakamura, Shawn Nikkila, Kalpesh Shah, Luis Tari, Ryan Wendt, Amanda Zeigler, Chitta Baral_

- :fontawesome-solid-user-group: **Participant:** [arizonau.baral](./genomics/participants.md#arizonau.baral)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/arizonasu.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/arizonasu.geo.pdf)
- :material-file-search: **Runs:** [asubaral](./genomics/runs.md#asubaral)

??? abstract "Abstract"
	
	In this paper we describe the approach used by the Arizona State University BioAI group for the ad-hoc retrieval task of the TREC Genomics Track 2005. We pre-process TREC query expression by adding the synonyms of genes, diseases, bio-processes, functions of organs, and selectively adding stemming verbs, nouns, and Mesh Heading categories. The pre-processed queries are used to perform initial search on the TREC Genomics collection of MEDLINE abstracts and produce a set of target abstracts using Apache Lucene. Tagging, anaphor resolution and fact extraction are performed on the target abstracts to refine the search results in terms of relevance. Finally, we rank the target abstracts according to the extracted facts, distance between terms and terms appeared in the query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuAGLNNSTWZB05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuAGLNNSTWZB05,
		author = {Lian Yu and Syed Toufeeq Ahmed and Graciela Gonzalez and Brendan Logsdon and Mutsumi Nakamura and Shawn Nikkila and Kalpesh Shah and Luis Tari and Ryan Wendt and Amanda Zeigler and Chitta Baral},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Genomic Information Retrieval Through Selective Extraction and Tagging by the ASU-BioAL Group},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/arizonasu.geo.pdf},
		timestamp = {Wed, 25 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuAGLNNSTWZB05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Genomics Track at I2R

_Nie Yu, Lingpeng Yang, Dong-Hong Ji, Jie Zhang, Jian Su, Xiaofeng Yang, Soon-Heng Tan, Juan Xiao, Guodong Zhou_

- :fontawesome-solid-user-group: **Participant:** [iir.yu](./genomics/participants.md#iir.yu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/inst-infocomm.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/inst-infocomm.geo.pdf)
- :material-file-search: **Runs:** [i2r1](./genomics/runs.md#i2r1) | [i2r2](./genomics/runs.md#i2r2)

??? abstract "Abstract"
	
	This paper describes the methods we used for the Ad Hoc task of TREC Genomics Track. Synonym dictionary for genes and pseudo relevance feedback are used to expand queries. BM25 model is implemented to retrieve relevant documents. We also tried to exploit name entities and their co-references in the retrieval. Results of submitted runs are listed and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuYJJSYTXZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuYJJSYTXZ05,
		author = {Nie Yu and Lingpeng Yang and Dong{-}Hong Ji and Jie Zhang and Jian Su and Xiaofeng Yang and Soon{-}Heng Tan and Juan Xiao and Guodong Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track at {I2R}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/inst-infocomm.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuYJJSYTXZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DataparkSearch at TREC 2005

_Maxim Zakharov_

- :fontawesome-solid-user-group: **Participant:** [datapark.zakharov](./genomics/participants.md#datapark.zakharov)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/datapark.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/datapark.geo.pdf)
- :material-file-search: **Runs:** [dpsearch1](./genomics/runs.md#dpsearch1) | [dpsearch2](./genomics/runs.md#dpsearch2)

??? abstract "Abstract"
	
	This paper describes the experiments of the OOO Datapark in TREC-2005. We participated in the Genomics track and submitted official runs to the Adhoc retrieval task. Our goal is to compare two methods of relevance calculation uses in the DataparkSearch Engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zakharov05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Zakharov05,
		author = {Maxim Zakharov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {DataparkSearch at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/datapark.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Zakharov05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIUC/MUSC at TREC 2005 Genomics Track

_ChengXiang Zhai, Xu Ling, Xin He, Atulya Velivelli, Xuanhui Wang, Hui Fang, Azadeh Shakery, Xinghua Lu_

- :fontawesome-solid-user-group: **Participant:** [uiuc.zhai](./genomics/participants.md#uiuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.geo.pdf)
- :material-file-search: **Runs:** [UIUCgAuto](./genomics/runs.md#uiucgauto) | [UIUCgInt](./genomics/runs.md#uiucgint) | [aMUSCUIUC1](./genomics/runs.md#amuscuiuc1) | [aMUSCUIUC2](./genomics/runs.md#amuscuiuc2) | [aMUSCUIUC3](./genomics/runs.md#amuscuiuc3) | [eMUSCUIUC1](./genomics/runs.md#emuscuiuc1) | [eMUSCUIUC2](./genomics/runs.md#emuscuiuc2) | [eMUSCUIUC3](./genomics/runs.md#emuscuiuc3) | [gMUSCUIUC1](./genomics/runs.md#gmuscuiuc1) | [gMUSCUIUC2](./genomics/runs.md#gmuscuiuc2) | [gMUSCUIUC3](./genomics/runs.md#gmuscuiuc3) | [tMUSCUIUC1](./genomics/runs.md#tmuscuiuc1) | [tMUSCUIUC2](./genomics/runs.md#tmuscuiuc2) | [tMUSCUIUC3](./genomics/runs.md#tmuscuiuc3)

??? abstract "Abstract"
	
	We report experiment results from the collaborative participation of UIUC and MUSC in the TREC 2005 Genomics Track. We participated in both the adhoc task and the categorization task, and studied the use of some mixture language models in these tasks. Experiment results show that a structured theme-based language modeling approach is effective in improving retrieval effectiveness for the ad hoc taks and the Latent Dirichlet Allocation method is effective in dimension reduction for the categorization task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaiLHVWFSL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaiLHVWFSL05,
		author = {ChengXiang Zhai and Xu Ling and Xin He and Atulya Velivelli and Xuanhui Wang and Hui Fang and Azadeh Shakery and Xinghua Lu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIUC/MUSC} at {TREC} 2005 Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaiLHVWFSL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Applying Probabilistic Thematic Clustering for Classification in the  TREC 2005 Genomics Track

_Z. H. Zheng, Scott Brady, Akash Garg, Hagit Shatkay_

- :fontawesome-solid-user-group: **Participant:** [queensu.shatkay](./genomics/participants.md#queensu.shatkay)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/queensu.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/queensu.geo.pdf)
- :material-file-search: **Runs:** [aQUNB8](./genomics/runs.md#aqunb8) | [aQUT11](./genomics/runs.md#aqut11) | [aQUT14](./genomics/runs.md#aqut14) | [eQUNB11](./genomics/runs.md#equnb11) | [eQUNB19](./genomics/runs.md#equnb19) | [eQUT18](./genomics/runs.md#equt18) | [gQUNB12](./genomics/runs.md#gqunb12) | [gQUNB15](./genomics/runs.md#gqunb15) | [gQUT22](./genomics/runs.md#gqut22) | [tQUNB3](./genomics/runs.md#tqunb3) | [tQUT10](./genomics/runs.md#tqut10) | [tQUT14](./genomics/runs.md#tqut14)

??? abstract "Abstract"
	
	Our group participated in the categorization task of the TREC Genomics Track. We introduced and investigated a cluster-based approach for classifying documents. We first clustered the abstracts of the negative training examples based on their term distribution, then built a classifier to distinguish between each cluster and the set of positive examples. The large number of resulting classifiers (a total of 14-19 classifiers per domain) was combined to categorize the test set. We also conducted experiments for cluster-based feature selection; Rather than select features from the whole negative and positive training sets, we selected features from each of the clusters and took the union of these features as the selected features for representing the whole training and test data. We compared our cluster-based multi-classifier approach against a simple naïve Bayes classification. We also compared the cluster-based feature selection strategy with the commonly used Chi-square-based feature selection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengBGS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengBGS05,
		author = {Z. H. Zheng and Scott Brady and Akash Garg and Hagit Shatkay},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Applying Probabilistic Thematic Clustering for Classification in the {TREC} 2005 Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/queensu.geo.pdf},
		timestamp = {Mon, 17 Apr 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengBGS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiment Report of TREC 2005 Genomics Track ad hoc Retrieval Task

_Wei Zhou, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [uillinois-chicago.liu](./genomics/participants.md#uillinois-chicago.liu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.geo.pdf)
- :material-file-search: **Runs:** [UICgen1](./genomics/runs.md#uicgen1)

??? abstract "Abstract"
	
	This report describes the experiments we have conducted on the ad hoc retrieval task of Genomics track at TREC 2005. In the experiment, a number of different techniques were employed, including Porter stemming, MeSH term and gene name identification, Okapi, weighting schemes, query expansion, and concept-based ranking strategy. The results on sample topics are reported. Future improvements, such as utilizing domain-specific knowledge, gene name disambiguation, and pseudo-feedback are discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouY05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouY05,
		author = {Wei Zhou and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiment Report of {TREC} 2005 Genomics Track ad hoc Retrieval Task},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouY05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## HARD 

#### HARD Track Overview in TREC 2005 High Accuracy Retrieval from  Documents

_James Allan_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/HARD.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/HARD.OVERVIEW.pdf)
??? abstract "Abstract"
	
	TREC 2005 saw the third year of the High Accuracy Retrieval from Documents (HARD) track. The HARD track explores methods for improving the accuracy of document retrieval systems, with particular attention paid to the start of the ranked list. Although it has done so in a few different ways in the past, budget realities limited the track to “clarification forms” this year. The question investigated was whether highly focused interaction with the searcher be used to improve the accuracy of a system. Participants created “clarification forms” generated in response to a query—and leveraging any information available in the corpus—that were filled out by the searcher. Typical clarification questions might ask whether some titles seem relevant, whether some words or names are on topic, or whether a short passage of text is related. The following summarizes the changes from the HARD track in TREC 2004 [Allan, 2005]: There was no passage retrieval evaluation as part of the track this year. There was no use of metadata this year. The evaluation corpus was the full AQUAINT collection. In HARD 2003 the track used part of AQUAINT plus additional documents. In HARD 2004 it was a collection of news from 2003 collated especially for HARD. The topics were selected from existing TREC topics. The same topics were used by the Robust track [Voorhees, 2006]. The topics had not been judged against the AQUAINT collection, though had been judged against a different collection. There was no notion of “hard relevance” and “soft relevance”, though documents were judged on a trinary scale of not relevant, relevant, or highly relevant. Clarification forms were allowed to be much more complex this year. Corpus and topic development, clarification form processing, and relevance assessments took place at NIST rather than at the Linguistic Data Consortium (LDC). The official evaluation measure of the track was R-precision. The HARD track's Web page may also contain useful pointers, though is not guaranteed to be in place indefinitely. As of early 2006, it was available at http://ciir.cs.umass.edu/research/hard. For TREC 2006, the HARD track is being “rolled into” the Question Answering track. The new aspect of the QA track is called “ciQA” for “complex, interactive Question Answering.” The goal of ciQA is to investigate interactive approaches to cope with complex information needs specified by a templated query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Allan05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Allan05,
		author = {James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{HARD} Track Overview in {TREC} 2005 High Accuracy Retrieval from Documents},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/HARD.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Allan05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### When Less is More: Relevance Feedback Falls Short and Term Expansion  Succeeds at HARD 2005

_Fernando Diaz, James Allan_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./HARD/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umass-hard.pdf](http://trec.nist.gov/pubs/trec14/papers/umass-hard.pdf)
- :material-file-search: **Runs:** [MASS1](./HARD/runs.md#mass1) | [MASS2](./HARD/runs.md#mass2) | [MASSbaseDEE3](./HARD/runs.md#massbasedee3) | [MASSbaseTEE3](./HARD/runs.md#massbasetee3) | [MASSbaseTRM3](./HARD/runs.md#massbasetrm3) | [MASSbaseDRM3](./HARD/runs.md#massbasedrm3) | [MASSpsgRM3R](./HARD/runs.md#masspsgrm3r) | [MASSpsgRM3](./HARD/runs.md#masspsgrm3) | [MASStrmS](./HARD/runs.md#masstrms) | [MASStrmR](./HARD/runs.md#masstrmr)

??? abstract "Abstract"
	
	We used clarification forms to study passage term feedback. When compared against pseudo-relevance feedback with an extremely large external corpus, we found that passage feedback resulted in a reduction in performance while term feed back significantly improved recall.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DiazA05.bib) "
	```
	@inproceedings{DBLP:conf/trec/DiazA05,
		author = {Fernando Diaz and James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {When Less is More: Relevance Feedback Falls Short and Term Expansion Succeeds at {HARD} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umass-hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DiazA05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SAIC & University of Virginia at TREC 2005: HARD Track

_Jonathan Michel, Xiangyu Jin, James C. French_

- :fontawesome-solid-user-group: **Participant:** [saic.michel](./HARD/participants.md#saic.michel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/saic-hard.pdf](http://trec.nist.gov/pubs/trec14/papers/saic-hard.pdf)
- :material-file-search: **Runs:** [SAICBASE1](./HARD/runs.md#saicbase1) | [SAICBASE2](./HARD/runs.md#saicbase2) | [SAIC1](./HARD/runs.md#saic1) | [SAIC2](./HARD/runs.md#saic2) | [SAICFINAL1](./HARD/runs.md#saicfinal1) | [SAICFINAL3](./HARD/runs.md#saicfinal3) | [SAICFINAL2](./HARD/runs.md#saicfinal2) | [SAICFINAL4](./HARD/runs.md#saicfinal4) | [SAICFINAL5](./HARD/runs.md#saicfinal5) | [SAICFINAL6](./HARD/runs.md#saicfinal6)

??? abstract "Abstract"
	
	SAIC (Science Applications International Corporation) and the University of Virginia collaborated to participate in the HARD (High Accuracy Retrieval from Documents) track of TREC 2005. Two clarification forms (CF) and 8 runs were submitted. The main focus of our work is to estimate the impact of incorrect user judgment on relevance feedback performance. The same set of documents are presented to the user to make judgments with different information shown on two CFs. Theoretically speaking if the user could make 100% accurate judgment, CF2 would perform much better than CF1. However, in practice, the user judgment accuracy is about 77.2% for CF1 and 65.4% for CF2. Thus results from feedback based on CF2 actually performs worse than CF1. This indicates possible unfairness when comparing relevance feedback techniques in a purely automatic evaluation environment where the user is assumed to be 'perfect'.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MichelJF05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MichelJF05,
		author = {Jonathan Michel and Xiangyu Jin and James C. French},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{SAIC} {\&} University of Virginia at {TREC} 2005: {HARD} Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/saic-hard.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MichelJF05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Strathclyde at TREC HARD

_Mark Baillie, David Elsweiler, Emma Nicol, Ian Ruthven, Simon O. Sweeney, Murat Yakici, Fabio Crestani, Monica Landoni_

- :fontawesome-solid-user-group: **Participant:** [ustrathclyde.baillie](./HARD/participants.md#ustrathclyde.baillie)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ustrathclyde.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/ustrathclyde.hard.pdf)
- :material-file-search: **Runs:** [STRA1](./HARD/runs.md#stra1) | [STRA3](./HARD/runs.md#stra3) | [STRA2](./HARD/runs.md#stra2) | [STRAxreadG](./HARD/runs.md#straxreadg) | [STRAxreadA](./HARD/runs.md#straxreada) | [STRAxprfb](./HARD/runs.md#straxprfb) | [STRAxmtg](./HARD/runs.md#straxmtg) | [STRAxqedt](./HARD/runs.md#straxqedt) | [STRAxmta](./HARD/runs.md#straxmta) | [STRAxqert](./HARD/runs.md#straxqert)

??? abstract "Abstract"
	
	The motivation behind the University of Strathclyde's approach to this years HARD track was inspired from previous experiences by other participants, in particular research by [1], [3] and [4]. A running theme throughout these papers was the underlying hypothesis that a user's familiarity in a topic (i.e. their previous experience searching a subject), will form the basis for what type or style of document they will perceive as relevant. In other words, the user's context with regards to their previous search experience will determine what type of document(s) they wish to retrieve.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BaillieENRSYCL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BaillieENRSYCL05,
		author = {Mark Baillie and David Elsweiler and Emma Nicol and Ian Ruthven and Simon O. Sweeney and Murat Yakici and Fabio Crestani and Monica Landoni},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Strathclyde at {TREC} {HARD}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ustrathclyde.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BaillieENRSYCL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers Information Interaction Lab at TREC 2005: Trying HARD

_Nicholas J. Belkin, Michael J. Cole, Jacek Gwizdka, Yuelin Li, Jingjing Liu, Gheorghe Muresan, Catherine Smith, Arthur R. Taylor, Xiaojun Yuan, Dmitri Roussinov_

- :fontawesome-solid-user-group: **Participant:** [rutgers.belkin](./HARD/participants.md#rutgers.belkin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/rutgersu.hard.murensan.pdf](http://trec.nist.gov/pubs/trec14/papers/rutgersu.hard.murensan.pdf)
- :material-file-search: **Runs:** [RUTGBLDR](./HARD/runs.md#rutgbldr) | [RUTG2](./HARD/runs.md#rutg2) | [RUTG1](./HARD/runs.md#rutg1) | [ALLcs0807](./HARD/runs.md#allcs0807) | [UG1cs0807](./HARD/runs.md#ug1cs0807) | [RUTBE](./HARD/runs.md#rutbe) | [RUTIN](./HARD/runs.md#rutin) | [LS1cs0807](./HARD/runs.md#ls1cs0807) | [AS1cs0807](./HARD/runs.md#as1cs0807) | [US1cs0807](./HARD/runs.md#us1cs0807) | [RS1cs0807](./HARD/runs.md#rs1cs0807) | [BF3cs0807](./HARD/runs.md#bf3cs0807) | [WS1cs0807](./HARD/runs.md#ws1cs0807) | [BLcs0807](./HARD/runs.md#blcs0807)

??? abstract "Abstract"
	
	Within the structure of the TREC 2005 HARD track guidelines, we investigated the following hypotheses: H1: Query expansion using a “clarity”-based approach will increase effectiveness over baseline queries and baseline queries plus pseudo-relevance feedback; H2: Query expansion based on the Web will increase effectiveness over baseline queries and baseline queries plus pseudo-relevance feedback; H3: Query expansion using terms selected by the searcher from those suggested by clarity modeling and/or the web will increase effectiveness over baseline queries, baseline queries plus pseudo-relevance feedback, and queries expanded by all suggested terms; H4: Query expansion using “problem statements” elicited from the searcher will increase effectiveness over baseline queries and baseline queries plus pseudo-relevance feedback; H5: The effectiveness of query expansion using problem statements will be negatively correlated with query “clarity”. H1 and H2 were tested without user intervention; H3 and H4 were tested using two different “clarification forms”; H5 was tested using the results of the H4 clarification form. Baseline queries were generated from the topic titles and descriptions; query expansion was accomplished by adding terms to the baseline queries, with a variety of weights given to the expansion terms, relative to the baseline terms. Preliminary results indicate that H1, H2, H3 and H4 are in part weakly supported, in that performance is increased over baseline, but it is not increased over pseudo-relevance feedback. H5 was not supported. Combining some degree of user interaction (H3) with pseudo-relevance feedback appears to lead to increased performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinCGLLMSTYR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinCGLLMSTYR05,
		author = {Nicholas J. Belkin and Michael J. Cole and Jacek Gwizdka and Yuelin Li and Jingjing Liu and Gheorghe Muresan and Catherine Smith and Arthur R. Taylor and Xiaojun Yuan and Dmitri Roussinov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Rutgers Information Interaction Lab at {TREC} 2005: Trying {HARD}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/rutgersu.hard.murensan.pdf},
		timestamp = {Tue, 31 Jan 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BelkinCGLLMSTYR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pitt at TREC 2005: HARD and Enterprise

_Daqing He, Jae-wook Ahn_

- :fontawesome-solid-user-group: **Participant:** [upittsburgh.he](./HARD/participants.md#upittsburgh.he)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/upittsburgh.hard.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/upittsburgh.hard.ent.pdf)
- :material-file-search: **Runs:** [PITTBTD](./HARD/runs.md#pittbtd) | [PITTBTDN225](./HARD/runs.md#pittbtdn225) | [PITT1](./HARD/runs.md#pitt1) | [PITT2](./HARD/runs.md#pitt2) | [PITTEC2NOB1](./HARD/runs.md#pittec2nob1) | [PITTEC1BWWB](./HARD/runs.md#pittec1bwwb) | [PITTEC2B225A](./HARD/runs.md#pittec2b225a) | [PITTHDCOMB1](./HARD/runs.md#pitthdcomb1)

??? abstract "Abstract"
	
	The University of Pittsburgh team participated in two tracks for TREC 2005: the High Accuracy Retrieval from Documents (HARD) track and the Enterprise Retrieval track. The goal of Pitt's HARD study in TREC 2005 was to examine the effectiveness of applying Self Organizing Maps (SOM) as a visual presentation tool and as a clustering tool in the context of HARD tasks, especially its role in clarification form generation. Our experiment results demonstrate that SOM can be used as a clustering tool to generate terms for query expansion based on interactive relevance feedback. It produced significant improvement over the baseline when measured by R-Prec. However, its effectiveness of being a visualization tool for users to make relevance feedback still needs careful examination and further studies. Our goal in this year's enterprise search track was to study the effect of query expansion based on an expansion corpus in retrieving emails from an email corpus. The expansion corpus consisted of the WWW, People and ESW sub-collections of the W3C test collection. The results indicate that query expansion based on the expansion corpus can achieve significant improvement over the no expansion baselines. However, there is no significant difference to the simpler query expansion approach using blind relevance feedback. Interestingly the terms used in these two query expansion approaches are different, with averagely only 6 term overlap among 20 possible terms. Further study is needed for examining the effect of combining these two approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeA05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeA05,
		author = {Daqing He and Jae{-}wook Ahn},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pitt at {TREC} 2005: {HARD} and Enterprise},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/upittsburgh.hard.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeA05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of North Carolina's HARD Track Experiment at TREC 2005

_Diane Kelly, Xin Fu_

- :fontawesome-solid-user-group: **Participant:** [unc.kelly](./HARD/participants.md#unc.kelly)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/unc-kelly.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/unc-kelly.hard.pdf)
- :material-file-search: **Runs:** [NCARhard05B](./HARD/runs.md#ncarhard05b) | [NCAR1](./HARD/runs.md#ncar1) | [NCAR2](./HARD/runs.md#ncar2) | [NCAR3](./HARD/runs.md#ncar3) | [NCARhard05F1](./HARD/runs.md#ncarhard05f1) | [NCARhard05F2](./HARD/runs.md#ncarhard05f2) | [NCARhard05F3](./HARD/runs.md#ncarhard05f3)

??? abstract "Abstract"
	
	In this year's HARD Track, we focused on two aspects related to the elicitation of relevance feedback: the display of document surrogates and features for identifying and selecting terms. We looked at these issues with respect to interactive query expansion (IQE). In typical interactive query expansion scenarios, users mark documents that they find relevant and the system automatically extracts terms from these documents and adds them to users' queries, or suggests potential query terms from these documents and allows users to determine which of these terms are added to their queries. While a large number of studies have been conducted on IQE, results of such studies do not convey a consistent picture of IQE use and effectiveness. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KellyF05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KellyF05,
		author = {Diane Kelly and Xin Fu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of North Carolina's {HARD} Track Experiment at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/unc-kelly.hard.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KellyF05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Meiji University HARD and Robust Track Experiments

_Kazuya Kudo, Kenji Imai, Makoto Hashimoto, Tomohiro Takagi_

- :fontawesome-solid-user-group: **Participant:** [meijiu.kakuta](./HARD/participants.md#meijiu.kakuta)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf)
- :material-file-search: **Runs:** [MeijiHilBL1](./HARD/runs.md#meijihilbl1) | [MeijiHilBL2](./HARD/runs.md#meijihilbl2) | [MEIJ1](./HARD/runs.md#meij1) | [MEIJ2](./HARD/runs.md#meij2) | [MeijiHilWN](./HARD/runs.md#meijihilwn) | [MeijiHilCWE1](./HARD/runs.md#meijihilcwe1) | [MeijiHilCWE2](./HARD/runs.md#meijihilcwe2) | [MeijiHilRW](./HARD/runs.md#meijihilrw) | [MeijiHilRC](./HARD/runs.md#meijihilrc) | [MeijiHilRWC](./HARD/runs.md#meijihilrwc) | [MeijiHilMrg](./HARD/runs.md#meijihilmrg)

??? abstract "Abstract"
	
	We participated in HARD Track and Robust Track at TREC2005. Our main challenge is to deal with expansion of a word by recognition of context. In HARD Track, we handled semantic expansion of a word. In Robust Track, we tried a challenge to new approach of “Document expansion” by context recognition. In this paper, the next section presents HARD Track. Section 3 describes Robust Track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KudoIHT05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KudoIHT05,
		author = {Kazuya Kudo and Kenji Imai and Makoto Hashimoto and Tomohiro Takagi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Meiji University {HARD} and Robust Track Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KudoIHT05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Menagerie of Tracks at Maryland: HARD, Enterprise, QA, and Genomics,  Oh My!

_Jimmy Lin, Eileen G. Abels, Dina Demner-Fushman, Douglas W. Oard, Philip Fei Wu, Yejun Wu_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./HARD/participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf)
- :material-file-search: **Runs:** [MARYB1](./HARD/runs.md#maryb1) | [MARYB2](./HARD/runs.md#maryb2) | [MARYB3](./HARD/runs.md#maryb3) | [MARY1](./HARD/runs.md#mary1) | [MARY05C1](./HARD/runs.md#mary05c1) | [MARY05C2](./HARD/runs.md#mary05c2) | [MARY05C3](./HARD/runs.md#mary05c3)

??? abstract "Abstract"
	
	This year, the University of Maryland participated in four separate tracks: HARD, enterprise, question answering, and genomics. Our HARD experiments involved a trained intermediary who searched for documents on behalf of the user, created clarification forms manually, and exploited user responses accordingly. The aim was to better understand the nature of single-iteration clarification dialogs and to develop an “ontology of clarifications” that can be leveraged to guide system development. For the enterprise track, we submitted official runs to the Known Item Search and the Discussion Search tasks. Document transformation to normalize dates and version numbers was found to be helpful, but suppression of text quoted from earlier messages and expansion of the indexed terms for a message based on subject line threading proved to not be. For the QA track, we submitted a manual run of “other” questions in an effort to quantify human performance on the task. Our genomics track participation was in collaboration with the National Library of Medicine, and is primarily reported in NLM's overview paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinADOWW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinADOWW05,
		author = {Jimmy Lin and Eileen G. Abels and Dina Demner{-}Fushman and Douglas W. Oard and Philip Fei Wu and Yejun Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Menagerie of Tracks at Maryland: HARD, Enterprise, QA, and Genomics, Oh My!},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf},
		timestamp = {Sat, 29 Jul 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinADOWW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLPR at TREC 2005: HARD Experiments

_Bibo Lv, Jun Zhao_

- :fontawesome-solid-user-group: **Participant:** [cas.nlpr.jzhao](./HARD/participants.md#cas.nlpr.jzhao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-nlpr.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-nlpr.hard.pdf)
- :material-file-search: **Runs:** [NLPRB](./HARD/runs.md#nlprb) | [CASP1](./HARD/runs.md#casp1) | [CASP2](./HARD/runs.md#casp2) | [NLPRCF1CF2](./HARD/runs.md#nlprcf1cf2) | [NLPRCF1](./HARD/runs.md#nlprcf1) | [NLPRCF2](./HARD/runs.md#nlprcf2) | [NLPRCF1S1](./HARD/runs.md#nlprcf1s1) | [NLPRCF1S2](./HARD/runs.md#nlprcf1s2) | [NLPRCF1W](./HARD/runs.md#nlprcf1w) | [NLPRCF1S1CF2](./HARD/runs.md#nlprcf1s1cf2) | [NLPRCF1S2CF2](./HARD/runs.md#nlprcf1s2cf2) | [NLPRCF1WCF2](./HARD/runs.md#nlprcf1wcf2)

??? abstract "Abstract"
	
	It is the third time that Chinese Information Processing Group of NLPR takes part in TREC. In the past, we participated in Novelty track and Robust track, in which we had evaluated our two key notions: Window-based Retrieval Algorithm and Result Emerging Strategy [1][2]. This year we focus on investigating the significance of relevance feedback, so HARD track is our best choice. HARD2005 is very different from that in the past two years. Firstly, Metadata is removed from topic description so that the topic description in HARD is the same as that of Robust track. Secondly, passage retrieval is cancelled this year. The paper introduces our work on HARD Track in TREC 2005, mainly (1) we propose a new feature selection method for query expansion in relevance feedback; (2) we adopt some query expansion methods. Our paper is organized as follows. Section 2 introduces our system, a new term selection algorithm for query expansion, and our clarification forms. Section 3 presents our query expansion methods. In section 4 experimental results are given, and finally we conclude our work in section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LvZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LvZ05,
		author = {Bibo Lv and Jun Zhao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NLPR} at {TREC} 2005: {HARD} Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-nlpr.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LvZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Lowlands' TREC Experiments 2005

_Henning Rode, Djoerd Hiemstra, Georgina Ramírez, Thijs Westerveld, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [utwente.rode](./HARD/participants.md#utwente.rode)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/lowlands-team.hard.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/lowlands-team.hard.ent.pdf)
- :material-file-search: **Runs:** [TWENbase1](./HARD/runs.md#twenbase1) | [TWENbase2](./HARD/runs.md#twenbase2) | [TWEN1](./HARD/runs.md#twen1) | [TWEN2](./HARD/runs.md#twen2) | [TWENblind1](./HARD/runs.md#twenblind1) | [TWENall1](./HARD/runs.md#twenall1) | [TWENdiff1](./HARD/runs.md#twendiff1) | [TWENall2](./HARD/runs.md#twenall2) | [TWENdiff2](./HARD/runs.md#twendiff2) | [TWENblind2](./HARD/runs.md#twenblind2)

??? abstract "Abstract"
	
	This paper describes our participation to the TREC HARD track (High Accuracy Retrieval of Documents) and the TREC Enterprise track. The main goal of our HARD participation is the development and evaluation of so-called query profiles: Short summaries of the retrieved results that enable the user to perform more focused search, for instance by zooming in on a particular time period. The main goal of our Enterprise track participation is to investigate the potential of the structural information for this type of retrieval task. In particular, we study the use of the thread information and the subject and header fields of the email documents. As a secondary and long standing research goal, we aim at developing an information retrieval framework that supports many diverse retrieval applications by means of one simple yet powerful query language (similar to SQL or relational algebra) that hides the implementation details of retrieval approaches from the application developer, while still giving the application developer control over the ranking process. Both the HARD system and the Enterprise system (as well as our TRECVID video retrieval system [14]) are based on MonetDB, an open source database system developed at CWI [1]. The paper is organised as follows. First, we discusses our participation in the HARD track. We define query profiles and discuss the way we generate them in Section 2. Section 3 describes the clarification forms used and Section 4 explains how we refine the queries and rank the results. We end this part by analysing our experimental results in Section 5 and giving some conclusions for this track in Section 6. The second part of the paper discusses our participation in the enterprise track. We start by describing the system and experimental setup in Section 7. Section 8 discusses the approaches taken for each of the subtasks and Section 9 analyses the results. We end by giving some conclusions and future work for this track in Section 10. The final part of the paper describes our future plans for building a so-called parameterised search engine within the Dutch National project MultimediaN.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RodeHRWV05.bib) "
	```
	@inproceedings{DBLP:conf/trec/RodeHRWV05,
		author = {Henning Rode and Djoerd Hiemstra and Georgina Ram{\'{\i}}rez and Thijs Westerveld and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Lowlands' {TREC} Experiments 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/lowlands-team.hard.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RodeHRWV05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Construction of Query Language Models - UIUC TREC  2005 HARD Track Experiments

_Bin Tan, Atulya Velivelli, Hui Fang, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uiuc.zhai](./HARD/participants.md#uiuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.hard.pdf)
- :material-file-search: **Runs:** [UIUC05Hardb0](./HARD/runs.md#uiuc05hardb0) | [UIUC1](./HARD/runs.md#uiuc1) | [UIUC2](./HARD/runs.md#uiuc2) | [UIUC3](./HARD/runs.md#uiuc3) | [UIUChTFB1](./HARD/runs.md#uiuchtfb1) | [UIUChTFB3](./HARD/runs.md#uiuchtfb3) | [UIUChTFB6](./HARD/runs.md#uiuchtfb6) | [UIUChCFB1](./HARD/runs.md#uiuchcfb1) | [UIUChCFB3](./HARD/runs.md#uiuchcfb3) | [UIUChCFB6](./HARD/runs.md#uiuchcfb6)

??? abstract "Abstract"
	
	In the language modeling approach, feedback is often modeled as estimating an improved query model or relevance model based on a set of feedback documents [3, 1]. This is in line with the traditional way of doing relevance feedback - presenting the user with documents or passages for relevance judgment and then extracting terms from the judged documents or passages to improve a query model. Such an indirect way of obtaining help from a user to construct a query model has the drawback that irrelevant terms that occur with relevant ones in the judged content may be erroneously used for query model modification. A more direct way to involve a user in improving the query model is to present some candidate terms to a user and directly ask the user to judge the relevance of each term or specify the probability of each term. This strategy has been discussed in [2], but has not been seriously studied in any existing work. In participating in the TREC 2005 HARD Track task, we explored how to exploit term-based feedback to better involve a user in constructing an improved query model for information retrieval with language models. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanVFZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanVFZ05,
		author = {Bin Tan and Atulya Velivelli and Hui Fang and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Interactive Construction of Query Language Models - {UIUC} {TREC} 2005 {HARD} Track Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TanVFZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments for HARD and Enterprise Tracks

_Olga Vechtomova, Maheedhar Kolla, Murat Karamuftuoglu_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.vechtomova](./HARD/participants.md#uwaterloo.vechtomova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uwaterloo-vechtomova.hard.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/uwaterloo-vechtomova.hard.ent.pdf)
- :material-file-search: **Runs:** [UWATbaseT](./HARD/runs.md#uwatbaset) | [UWATbaseTD](./HARD/runs.md#uwatbasetd) | [UWAT1](./HARD/runs.md#uwat1) | [UWAT2](./HARD/runs.md#uwat2) | [UWAT3](./HARD/runs.md#uwat3) | [UwatHARDexp1](./HARD/runs.md#uwathardexp1) | [UwatHARDexp2](./HARD/runs.md#uwathardexp2) | [UwatHARDexp3](./HARD/runs.md#uwathardexp3) | [UWAThardLC1](./HARD/runs.md#uwathardlc1)

??? abstract "Abstract"
	
	The main theme in our participation in this year's HARD track was experimentation with the effect of lexical cohesion on document retrieval. Lexical cohesion is a major characteristic of natural language texts, which is achieved through semantic connectedness between words in text, and expresses continuity between the parts of text [7]. Segments of text which are about the same or similar subjects (topics) have higher lexical cohesion, i.e. share a larger number of words than unrelated segments. We have experimented with two approaches to the selection of query expansion terms based on lexical cohesion: (1) by selecting query expansion terms that form lexical links between the distinct original query terms in the document (section 1.1); and (2) by identifying lexical chains in the document and selecting query expansion terms from the strongest lexical chains (section 1.2).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VechtomovaKK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/VechtomovaKK05,
		author = {Olga Vechtomova and Maheedhar Kolla and Murat Karamuftuoglu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments for {HARD} and Enterprise Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uwaterloo-vechtomova.hard.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VechtomovaKK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2005: HARD Track

_Miao Wen, Xiangji Huang, Aijun An, Yan Rui Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./HARD/participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/yorku-huang.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/yorku-huang.hard.pdf)
- :material-file-search: **Runs:** [york05hb1](./HARD/runs.md#york05hb1) | [york05hb2](./HARD/runs.md#york05hb2) | [york05hb3](./HARD/runs.md#york05hb3) | [YORK1](./HARD/runs.md#york1) | [YORK2](./HARD/runs.md#york2) | [YORK3](./HARD/runs.md#york3) | [YORK4](./HARD/runs.md#york4) | [york05ha1](./HARD/runs.md#york05ha1) | [york05ha2](./HARD/runs.md#york05ha2) | [york05ha3](./HARD/runs.md#york05ha3) | [york05ha4](./HARD/runs.md#york05ha4) | [york05ha5](./HARD/runs.md#york05ha5)

??? abstract "Abstract"
	
	In an IR model, “user”, “query” and “result” are three important components. Traditionally, a query is considered to be independent of the user. IR systems search documents without considering who issues the query and why the query is asked. However, those factors can affect the user's satisfaction about the result. The information about the user, such as the genre preference of the user, occupation of the user, location of the user, which are normally called personalized information, indicate users' preferences to the retrieval result. We demonstrate the effectiveness of a dual indexing technique and a feedback method on the HARD 2005 data set. We also propose a non-content based method to measure user's familiarity to a query. A similarity model is built to utilize the familiarity information and to improve the overall performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WenHAH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WenHAH05,
		author = {Miao Wen and Xiangji Huang and Aijun An and Yan Rui Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2005: {HARD} Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/yorku-huang.hard.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WenHAH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2005 HARD, Robust, and SPAM Tracks

_Kiduk Yang, Ning Yu, Nicholas George, Aaron Loehrlein, David McCaulay, Hui Zhang, Shahrier Akram, Jue Mei, Ivan Record_

- :fontawesome-solid-user-group: **Participant:** [indianau.yang](./HARD/participants.md#indianau.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf)
- :material-file-search: **Runs:** [wdf1t10q1](./HARD/runs.md#wdf1t10q1) | [wdf1t3qf2](./HARD/runs.md#wdf1t3qf2) | [wdoqdn1d2](./HARD/runs.md#wdoqdn1d2) | [wdoqsz1d2](./HARD/runs.md#wdoqsz1d2) | [INDI1](./HARD/runs.md#indi1) | [INDI2](./HARD/runs.md#indi2) | [wf1t10q1RCDX](./HARD/runs.md#wf1t10q1rcdx) | [wf1t10q1RODX](./HARD/runs.md#wf1t10q1rodx) | [wf2t3qs1RODX](./HARD/runs.md#wf2t3qs1rodx) | [wf1t3qdROD10](./HARD/runs.md#wf1t3qdrod10) | [wf2t3qs1RCX](./HARD/runs.md#wf2t3qs1rcx) | [wf1t3qdRC10](./HARD/runs.md#wf1t3qdrc10)

??? abstract "Abstract"
	
	Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science participated in the HARD, Robust, and SPAM tracks in TREC-2005. The basic approach of WIDIT is to combine multiple methods as well as to leverage multiple sources of evidence. Our main strategies for the tracks were: query expansion and fusion optimization for the HARD and Robust tracks; and combination of probabilistic, rule-based, pattern-based, and blacklist email filters for the SPAM track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYGLMZAMR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYGLMZAMR05,
		author = {Kiduk Yang and Ning Yu and Nicholas George and Aaron Loehrlein and David McCaulay and Hui Zhang and Shahrier Akram and Jue Mei and Ivan Record},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2005 HARD, Robust, and {SPAM} Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf},
		timestamp = {Wed, 29 Jun 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangYGLMZAMR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Relevance Feedback by Exploring the Different Feedback Sources and  Collection Structure

_Junlin Zhang, Le Sun, Yuanhua Lv, Wei Zhang_

- :fontawesome-solid-user-group: **Participant:** [cas.zhang](./HARD/participants.md#cas.zhang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-zhang.hard.pdf](http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-zhang.hard.pdf)
- :material-file-search: **Runs:** [CASS1](./HARD/runs.md#cass1) | [CASS2](./HARD/runs.md#cass2) | [cassbase](./HARD/runs.md#cassbase) | [cassbasere](./HARD/runs.md#cassbasere) | [cassgoogle](./HARD/runs.md#cassgoogle) | [casstopdoc](./HARD/runs.md#casstopdoc) | [cassself](./HARD/runs.md#cassself) | [cassselfre](./HARD/runs.md#cassselfre) | [cassallfb](./HARD/runs.md#cassallfb) | [cassallre](./HARD/runs.md#cassallre) | [cassallfb2](./HARD/runs.md#cassallfb2) | [cassallfb2re](./HARD/runs.md#cassallfb2re)

??? abstract "Abstract"
	
	In HARD track of HARD 2005, we classify the 50 queries into 7 categories and make use of 3 kinds of feedback sources in various tasks. We find that the different kinds of queries perform differently in feedback tasks and the “CASE “ and “EVENT” queries are more sensitive to the feedback source. We also explore the internal structure of corpus and try to estimate the distribution of relevant documents within sub-collections. The experiments show that this technology is partly effective and the main existing problem is how to predict the distribution more precisely.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangSLZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangSLZ05,
		author = {Junlin Zhang and Le Sun and Yuanhua Lv and Wei Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Relevance Feedback by Exploring the Different Feedback Sources and Collection Structure},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-zhang.hard.pdf},
		timestamp = {Fri, 21 Aug 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangSLZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Question Answering 

#### Overview of the TREC 2005 Question Answering Track

_Ellen M. Voorhees, Hoa Trang Dang_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/QA.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/QA.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC 2005 Question Answering (QA) track contained three tasks: the main question answering task, the document ranking task, and the relationship task. In the main task, question series were used to define a set of targets. Each series was about a single target and contained factoid and list questions. The final question in the series was an “Other” question that asked for additional information about the target that was not covered by previous questions in the series. The main task was the same as the single TREC 2004 QA task, except that targets could also be events; the addition of events and dependencies between questions in a series made the task more difficult and resulted in lower evaluation scores than in 2004. The document ranking task was to return a ranked list of documents for each question from a subset of the questions in the main task, where the documents were thought to contain an answer to the question. In the relationship task, systems were given TREC-like topic statements that ended with a question asking for evidence for a particular relationship.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VoorheesD05.bib) "
	```
	@inproceedings{DBLP:conf/trec/VoorheesD05,
		author = {Ellen M. Voorhees and Hoa Trang Dang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2005 Question Answering Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/QA.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VoorheesD05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring Document Content with XML to Answer Questions

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch.litkowski](./qa/participants.md#clresearch.litkowski)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/clresearch.pdf](http://trec.nist.gov/pubs/trec14/papers/clresearch.pdf)
- :material-file-search: **Runs:** [clr05](./qa/runs.md#clr05) | [clr05r1](./qa/runs.md#clr05r1) | [clr05r2](./qa/runs.md#clr05r2)

??? abstract "Abstract"
	
	CL Research participated in the question answering track in TREC 2004, submitting runs for the main task, the document relevance task, and the relationship task. The tasks were performed using the Knowledge Management System (KMS), which provides a single interface for question answering, text summarization, information extraction, and document exploration. These tasks are based on creating and exploiting an XML representation of the texts in the AQUAINT collection. Question answering is performed directly within KMS, which answers questions either from the collection or from the Internet projected back onto the collection. For the main task, we submitted one run and our average per-series score was 0.136, with scores of 0.180 for factoid questions, 0.026 for list questions, and 0.152 for “other” questions. For the document ranking task, the average precision was 0.2253 and the R-precision was 0.2405. For the relationship task, we submitted two runs, with scores of 0.276 and 0.216, the first run was the best score on this task. We describe the overall architecture of KMS and how it permits examination of the question-answering task and strategies within TREC, but also in a real-world application in the bioterrorism domain. We also raise some issues concerning the judgments used for evaluating TREC results and their possible relevance in a wider context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Litkowski05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Litkowski05,
		author = {Kenneth C. Litkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploring Document Content with {XML} to Answer Questions},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/clresearch.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Litkowski05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DalTREC 2005 QA System Jellyfish: Mark-and-Match Approach to Question  Answering

_Tony Abou-Assaleh, Nick Cercone, Jon Doyle, Vlado Keselj, Chris Whidden_

- :fontawesome-solid-user-group: **Participant:** [dalhousieu.keselj](./qa/participants.md#dalhousieu.keselj)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dalhousieu.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/dalhousieu.qa.pdf)
- :material-file-search: **Runs:** [Dal05s](./qa/runs.md#dal05s) | [Dal05p](./qa/runs.md#dal05p) | [Dal05m](./qa/runs.md#dal05m)

??? abstract "Abstract"
	
	This is the second year that Dalhousie University actively participated in TREC. Three runs were submitted for the Question Answering track. Our results are below the median; however, they're signifantly larger than minimal, the lesson learnt will guide our future development of the system. Our approach was based on a mark-and-match methodology with regular expression rewriting.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Abou-AssalehCDKW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Abou-AssalehCDKW05,
		author = {Tony Abou{-}Assaleh and Nick Cercone and Jon Doyle and Vlado Keselj and Chris Whidden},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {DalTREC 2005 {QA} System Jellyfish: Mark-and-Match Approach to Question Answering},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/dalhousieu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Abou-AssalehCDKW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Towards a Multi-Stream Question Answering-As-XML-Retrieval Strategy

_David Ahn, Sisay Fissaha Adafre, Valentin Jijkoun, Karin Müller, Maarten de Rijke, Erik F. Tjong Kim Sang_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.mueller](./qa/participants.md#uamsterdam.mueller)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uamsterdam.qa.erik.pdf](http://trec.nist.gov/pubs/trec14/papers/uamsterdam.qa.erik.pdf)
- :material-file-search: **Runs:** [uams05all](./qa/runs.md#uams05all) | [uams05rnk](./qa/runs.md#uams05rnk) | [uams05be3](./qa/runs.md#uams05be3) | [uams05s](./qa/runs.md#uams05s) | [uams05l](./qa/runs.md#uams05l)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2005 Question Answering track; our main focus this year was on improving our multi-stream approach to question answering and on making a first step towards a question answering-as-XML retrieval strategy. We provide a detailed account of the ideas underlying our approaches to the QA task, report on our results, and give a summary of our findings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AhnAJMRS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AhnAJMRS05,
		author = {David Ahn and Sisay Fissaha Adafre and Valentin Jijkoun and Karin M{\"{u}}ller and Maarten de Rijke and Erik F. Tjong Kim Sang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Towards a Multi-Stream Question Answering-As-XML-Retrieval Strategy},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uamsterdam.qa.erik.pdf},
		timestamp = {Tue, 14 Jul 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AhnAJMRS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering with QED at TREC 2005

_Kisuh Ahn, Johan Bos, David Kor, Malvina Nissim, Bonnie L. Webber, James R. Curran_

- :fontawesome-solid-user-group: **Participant:** [uedinburgh.dalmas](./qa/participants.md#uedinburgh.dalmas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uedinburgh-nissim.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/uedinburgh-nissim.qa.pdf)
- :material-file-search: **Runs:** [Edin2005a](./qa/runs.md#edin2005a) | [Edin2005b](./qa/runs.md#edin2005b) | [Edin2005c](./qa/runs.md#edin2005c)

??? abstract "Abstract"
	
	This report describes the system developed by the University of Edinburgh and the University of Sydney for the TREC-2005 question answering evaluation exercise. The backbone of our question-answering platform is QED, a linguistically-principled QA system. We experimented with external sources of knowledge, such as Google and Wikipedia, to enhance the performance of QED, especially for reranking and off-line processing of the corpus. For factoid and list questions we performed significantly above the median accuracy score of all participating systems at TREC 2005.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AhnBKNWC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AhnBKNWC05,
		author = {Kisuh Ahn and Johan Bos and David Kor and Malvina Nissim and Bonnie L. Webber and James R. Curran},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering with {QED} at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uedinburgh-nissim.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AhnBKNWC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Looking at Limits and Tradeoffs: Sabir Research at TREC 2005

_Chris Buckley_

- :fontawesome-solid-user-group: **Participant:** [sabir.buckley](./qa/participants.md#sabir.buckley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf)
- :material-file-search: **Runs:** [sab05qa1b](./qa/runs.md#sab05qa1b)

??? abstract "Abstract"
	
	Sabir Research participated in TREC-2005 in the Terabyte, Robust, and document retrieval part of the Question Answering tracks. This writeup focuses on the Robust track, and in particular on a “routing” run that took advantage of relevance judgements for the topics on the old trec V45 collection to construct queries for the new Aquaint collection. The s ¯mart retro tool is described which given a query and the set of relevant documents, con- structs an optimally weighted version of the query. smart_retro is also used to examine the differences in difficulty between the V45 and Aquaint collections (the Aquaint collection is considerably easier). The final part of the paper describes the compression algorithms and tradeoffs that were used in both TREC 2004 and 2005. These were presented in the TREC 2004 speaker session, but never formally written up. The hardware used for all runs was a single commodity PC with a total cost of $1600: $540 for a Dell PC, $520 for four 250 GByte disks, and $500 to bring the memory up to 2.5 GBytes. The information retrieval software used was the research version of SMART 15.0. SMART was originally developed in the early 1960's by Gerard Salton and since then has continued to be a leading research information retrieval tool. It continues to use a statistical vector space model, with stemming, stop words, weighting, inner product similarity function, and ranked retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Buckley05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Buckley05,
		author = {Chris Buckley},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Looking at Limits and Tradeoffs: Sabir Research at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Buckley05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MITRE's Qanda at TREC 14

_John D. Burger, Samuel Bayer_

- :fontawesome-solid-user-group: **Participant:** [mitre.burger](./qa/participants.md#mitre.burger)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/mitre-corp.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/mitre-corp.qa.pdf)
- :material-file-search: **Runs:** [MITRE2005A](./qa/runs.md#mitre2005a) | [MITRE2005B](./qa/runs.md#mitre2005b) | [MITRE2005C](./qa/runs.md#mitre2005c)

??? abstract "Abstract"
	
	Qanda is MITRE's TREC-style question answering system. In recent years, we have been able to apply only a small effort to the TREC QA activity, approximately two person-months this year. (Accordingly, much of this discussion is strikingly similar to prior system descriptions.) We have made some general improvements in Qanda's processing, including genuine question parsing, generalizing answer selection to better handle variant question types like lists and definition questions, and better integration with a maximum entropy answer scorer, both in training and at run time. We have also attempted to better integrate the results of question processing and document retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BurgerB05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BurgerB05,
		author = {John D. Burger and Samuel Bayer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MITRE's Qanda at {TREC} 14},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/mitre-corp.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BurgerB05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNT 2005 TREC QA Participation: Using Lemur as IR Search Engine

_Jiangping Chen, Ping Yu, He Ge_

- :fontawesome-solid-user-group: **Participant:** [untexas.chen](./qa/participants.md#untexas.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/unorth-texas.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/unorth-texas.qa.pdf)
- :material-file-search: **Runs:** [UNTQA0503](./qa/runs.md#untqa0503) | [UNTQA0502](./qa/runs.md#untqa0502) | [UNTQA0501](./qa/runs.md#untqa0501)

??? abstract "Abstract"
	
	This paper reports our TREC 2005 QA participation. Our QA system EagleQA developed last year was expanded and modified for this year's QA experiments. Particularly, we used Lemur 4.1 (http://www.lemurproject.org/) as the Information Retrieval (IR) Engine this year to find documents that may contain answers for the test questions from the document collection. Our result shows Lemur did a reasonable job on finding relevant documents. But certainly there is room for further improvement.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenYG05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenYG05,
		author = {Jiangping Chen and Ping Yu and He Ge},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UNT} 2005 {TREC} {QA} Participation: Using Lemur as {IR} Search Engine},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/unorth-texas.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenYG05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM's PIQUANT II in TREC 2005

_Jennifer Chu-Carroll, Pablo Ariel Duboue, John M. Prager, Krzysztof Czuba_

- :fontawesome-solid-user-group: **Participant:** [ibm.prager](./qa/participants.md#ibm.prager)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm.tjwatson.qa.prager.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm.tjwatson.qa.prager.pdf)
- :material-file-search: **Runs:** [IBM05C3PD](./qa/runs.md#ibm05c3pd) | [IBM05L3P](./qa/runs.md#ibm05l3p) | [IBM05L1P](./qa/runs.md#ibm05l1p)

??? abstract "Abstract"
	
	This year, the PIQUANT II system we used in the TREC QA track is an improved version over the reengineered system we used in last year's entry [Chu-Carroll et al., 2005]. Our system adopts a multi-agent approach to question answering. In this framework, a question is submitted to multiple agents, each adopting a different question answering strategy and/or consults a different information source to produce a set of answers, which are then combined using a voting scheme to determine the overall system's answer(s) to the question. In our 2005 system, we have made improvements along several dimensions, by improving the performance of select answering agents, by developing two new agents, and finally, by improving our answer resolution algorithm for combining answers from individual agents. In this paper, we describe these improvements and their impact on the factoid, list, and other subtasks in the main task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Chu-CarrollDPC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Chu-CarrollDPC05,
		author = {Jennifer Chu{-}Carroll and Pablo Ariel Duboue and John M. Prager and Krzysztof Czuba},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IBM's {PIQUANT} {II} in {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ibm.tjwatson.qa.prager.pdf},
		timestamp = {Sat, 21 Jan 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Chu-CarrollDPC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Factoid Question Answering over Unstructured and Structured Web Content

_Silviu Cucerzan, Eugene Agichtein_

- :fontawesome-solid-user-group: **Participant:** [microsoft.brill](./qa/participants.md#microsoft.brill)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/microsoft-res.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/microsoft-res.qa.pdf)
- :material-file-search: **Runs:** [MSRWSQA05](./qa/runs.md#msrwsqa05) | [MSRTQA05](./qa/runs.md#msrtqa05) | [MSRCOMB05](./qa/runs.md#msrcomb05)

??? abstract "Abstract"
	
	We describe our experience with two new, built-from-scratch, web-based question answering systems applied to the TREC 2005 Main Question Answering task, which use complementary models of answering questions over both structured and unstructured content on the Web. Our approaches depart from previous question answering (QA) work in several ways. For unstructured content, we used a web-based system with novel features such as web snippet pattern matching and generic answer type matching using web counts. We also experimented with a new, complementary question answering approach that uses information from the millions of tables and lists that abound on the web. This system attempts to answer factoid questions by guessing relevant rows and fields in matching web tables and integrating the results. We believe a combination of the two approaches holds promise.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CucerzanA05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CucerzanA05,
		author = {Silviu Cucerzan and Eugene Agichtein},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Factoid Question Answering over Unstructured and Structured Web Content},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/microsoft-res.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CucerzanA05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Questions and Relationships at the University of Iowa

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [uiowa.eichmann](./qa/participants.md#uiowa.eichmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf)
- :material-file-search: **Runs:** [UIowaQA0501](./qa/runs.md#uiowaqa0501) | [UIowaQA0502](./qa/runs.md#uiowaqa0502) | [UIowaQA0503](./qa/runs.md#uiowaqa0503) | [UIowa05QAR01](./qa/runs.md#uiowa05qar01)

??? abstract "Abstract"
	
	The University of Iowa participated in the genomics and question answering tracks of TREC-2005. This paper covers only our work in question answering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS05,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Questions and Relationships at the University of Iowa},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TALP-UPC at TREC 2005: Experiments Using a Voting Scheme Among  Three Heterogeneous QA Systems

_Daniel Ferrés, Samir Kanaan, David Dominguez-Sal, Edgar González, Alicia Ageno, María Fuentes Fort, Horacio Rodríguez, Mihai Surdeanu, Jordi Turmo_

- :fontawesome-solid-user-group: **Participant:** [upc-talp.ferres](./qa/participants.md#upc-talp.ferres)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/upolitecnicade-catalunya.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/upolitecnicade-catalunya.qa.pdf)
- :material-file-search: **Runs:** [talpupc05b](./qa/runs.md#talpupc05b) | [talpupc05c](./qa/runs.md#talpupc05c) | [talpupc05a](./qa/runs.md#talpupc05a)

??? abstract "Abstract"
	
	This paper describes the experiments of the TALP-UPC group for factoid and 'other' (definitional) questions at TREC 2005 Main Question Answering (QA) task. Our current approach for factoid questions is based on a voting scheme among three QA systems: TALP-QA (our previous QA system), Sibyl (a new QA system developed at DAMA-UPC and TALP-UPC), and Aranea (a web-based data-driven approach). For defitional questions, we used two different systems: the TALP-QA Definitional system and LCSUM (a Summarization-based system). Our results for factoid questions indicate that the voting strategy improves the accuracy from 7.5% to 17.1%. While these numbers are low (due to technical problems in the Answer Extraction phase of TALP-QA system) they indicate that voting is a succesful approach for performance boosting of QA systems. The answer to definitional questions is produced by selecting phrases using set of patterns associated with definitions. Its results are 17.2% of F-score in the best configuration of TALP-QA Definitional system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerresKDGAFRST05.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerresKDGAFRST05,
		author = {Daniel Ferr{\'{e}}s and Samir Kanaan and David Dominguez{-}Sal and Edgar Gonz{\'{a}}lez and Alicia Ageno and Mar{\'{\i}}a Fuentes Fort and Horacio Rodr{\'{\i}}guez and Mihai Surdeanu and Jordi Turmo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TALP-UPC} at {TREC} 2005: Experiments Using a Voting Scheme Among Three Heterogeneous {QA} Systems},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/upolitecnicade-catalunya.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FerresKDGAFRST05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Sheffield's TREC 2005 Q&A Experiments

_Robert J. Gaizauskas, Mark A. Greenwood, Henk Harkema, Mark Hepple, Horacio Saggion, Atheesh Sanka_

- :fontawesome-solid-user-group: **Participant:** [usheffield.gaizauskas](./qa/participants.md#usheffield.gaizauskas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/usheffield.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/usheffield.qa.pdf)
- :material-file-search: **Runs:** [shef05lmg](./qa/runs.md#shef05lmg) | [SHEF05MC](./qa/runs.md#shef05mc) | [SHEF05LC](./qa/runs.md#shef05lc)

??? abstract "Abstract"
	
	Our entries in the TREC 2005 QA evaluation continue experiments carried out as part of TREC 2004. Hence here, as there, we report work on multiple approaches to both the main and document ranking tasks. For query generation and document retrieval we explored two approaches, one based on Lucene 1, the other on MadCow, an in-house boolean search engine. For answer extractrion we have also explored two approaches, one a shallow approach based on semantic typing and question-answer word overlap, the other based on syntactic analysis and logical form matching. As well as continuing independent development of these multiple approaches, we have also concentrated on developing common resources to to be shared between these approaches in order to allow for more principled comparison
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaizauskasGHHSS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaizauskasGHHSS05,
		author = {Robert J. Gaizauskas and Mark A. Greenwood and Henk Harkema and Mark Hepple and Horacio Saggion and Atheesh Sanka},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Sheffield's {TREC} 2005 Q{\&}A Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/usheffield.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaizauskasGHHSS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Differential Linguistics at NIST TREC

_Ilya S. Geller_

- :fontawesome-solid-user-group: **Participant:** [lexiclone.geller](./qa/participants.md#lexiclone.geller)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/lexiclone.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/lexiclone.qa.pdf)
- :material-file-search: **Runs:** [lexiclone5](./qa/runs.md#lexiclone5) | [lexicloneB](./qa/runs.md#lexicloneb)

??? abstract "Abstract"
	
	In the course of carrying out NIST TRECs I created and tested a computer program for textual information searches, based on ‘understanding' the meanings of words in texts. The computer using the program ‘understands' not only the abstract, standardized meanings of the words in the text, but the specific, concrete meanings given to those words by the author(s) of the texts. In this article I attempt to bring the language I used to create the algorithm of the program in line with the generally accepted, formalized language of mathematics. (Doing this I must apply the philosophy and metaphysics of Cynicism.)
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Geller05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Geller05,
		author = {Ilya S. Geller},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Differential Linguistics at {NIST} {TREC}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/lexiclone.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Geller05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering with SEMEX at TREC 2005

_Demetrios G. Glinos_

- :fontawesome-solid-user-group: **Participant:** [ucentralfla.glinos](./qa/participants.md#ucentralfla.glinos)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ucentralfl.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/ucentralfl.qa.pdf)
- :material-file-search: **Runs:** [dggQA05](./qa/runs.md#dggqa05) | [dggQA05X](./qa/runs.md#dggqa05x)

??? abstract "Abstract"
	
	We describe the SEMEX question-answering system and report its performance in the TREC 2005 Question Answering track. Since this was SEMEX's first year participating in the TREC evaluations, implementation teething pains were expected and indeed encountered. Nevertheless, performance against difficult factoid and list questions was supportive of the question answering approach that was implemented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Glinos05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Glinos05,
		author = {Demetrios G. Glinos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering with {SEMEX} at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ucentralfl.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Glinos05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Employing Two Question Answering Systems in TREC 2005

_Sanda M. Harabagiu, Dan I. Moldovan, Christine Clark, Mitchell Bowden, Andrew Hickl, Patrick Wang_

- :fontawesome-solid-user-group: **Participant:** [lcc.harabagiu](./qa/participants.md#lcc.harabagiu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/lcc-sanda.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/lcc-sanda.qa.pdf)
- :material-file-search: **Runs:** [lcc05](./qa/runs.md#lcc05) | [lcc05rel1](./qa/runs.md#lcc05rel1) | [lcc05rel2](./qa/runs.md#lcc05rel2)

??? abstract "Abstract"
	
	n 2005, the TREC QA track had two separate tasks: the main task and the relationship task. To participate in TREC 2005 we employed two different QA systems. PowerAnswer-2 was used in the main task, whereas PALANTIR was used for the relationship questions. For the main task, new this year is the use of events as targets in addition to the nominal concepts used last year. Event targets ranged from a nominal event such as “Preakness 1998” to a description of an event as in “Plane clips cable wires in Italian resort”. There were 17 event targets total. Unlike nominal targets, which most often act as the topic of the subsequent questions, events provide a context for the questions. Therefore, targets representing events had questions that asked about participants in the event, about characteristics of the vent and furthermore, had temporal constraints. Also many questions referred to answers of previous questions. To complicate matters, several answers could be candidate for the anaphors used in follow-up questions, but salience mattered. This introduced new complexities for the coreference resolution. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HarabagiuMCBHW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HarabagiuMCBHW05,
		author = {Sanda M. Harabagiu and Dan I. Moldovan and Christine Clark and Mitchell Bowden and Andrew Hickl and Patrick Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Employing Two Question Answering Systems in {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/lcc-sanda.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HarabagiuMCBHW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Peking University at the TREC 2005 Question and Answering Track

_Jing He, Cheng Chen, Conglei Yao, Ping Yin, Yongjun Bao_

- :fontawesome-solid-user-group: **Participant:** [pekingu.yan](./qa/participants.md#pekingu.yan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/pekingu-he.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/pekingu-he.qa.pdf)
- :material-file-search: **Runs:** [TWQA0501](./qa/runs.md#twqa0501) | [TWQA0502](./qa/runs.md#twqa0502)

??? abstract "Abstract"
	
	This paper describes the architecture and implementation of Tianwang QA system, which can work for the Main task and the Document Ranking task. The system is designed to extract candidate answer snippets from different pipelines, e.g. the high quality search engines' results, the frequently asked question (FAQ) set, and the well-structured web facts, etc..So the system need to process the Web documents, the FAQ corpus and the knowledge base (KB) from the structural web pages, besides analyzing the query, the TREC document retrieval and the answer merging. The external knowledge we made use of, i.e. FAQ and KB, are proved to be effective for our final results. We classify questions with SVM approaches, construct queries in Boolean way, retrieve and rank the passage with span model and extract answers using named entity technologies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeCYYB05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeCYYB05,
		author = {Jing He and Cheng Chen and Conglei Yao and Ping Yin and Yongjun Bao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Peking University at the {TREC} 2005 Question and Answering Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/pekingu-he.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeCYYB05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QuALiM at TREC 2005: Web-Question Answering with FrameNet

_Michael Kaisser_

- :fontawesome-solid-user-group: **Participant:** [dfki-saarlandu.kaisser](./qa/participants.md#dfki-saarlandu.kaisser)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/usaarland.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/usaarland.qa.pdf)
- :material-file-search: **Runs:** [mk2005qar1](./qa/runs.md#mk2005qar1) | [mk2005qar2](./qa/runs.md#mk2005qar2)

??? abstract "Abstract"
	
	In this paper I describe my TREC 2005 participation. The system used was-except from one new module-the same as in TREC 2004. In the following I will describe this new module, which uses the annotated Natural Language data collected in the FrameNet project in order to find paraphrases to answer questions. I will furthermore present and discuss the TREC 2005 results and compare them to those achieved in TREC 2004.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Kaisser05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Kaisser05,
		author = {Michael Kaisser},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {QuALiM at {TREC} 2005: Web-Question Answering with FrameNet},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/usaarland.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Kaisser05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### External Knowledge Sources for Question Answering

_Boris Katz, Gregory Marton, Gary C. Borchardt, Alexis Brownell, Sue Felshin, Daniel Loreto, Jesse Louis-Rosenberg, Ben Lu, Federico Mora, Stephan Stiller, Özlem Uzuner, Angela Wilcox_

- :fontawesome-solid-user-group: **Participant:** [mit.katz](./qa/participants.md#mit.katz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/mit-katz.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/mit-katz.qa.pdf)
- :material-file-search: **Runs:** [csail1](./qa/runs.md#csail1) | [csail2](./qa/runs.md#csail2) | [csail3](./qa/runs.md#csail3) | [csail2005m](./qa/runs.md#csail2005m) | [csail2005a](./qa/runs.md#csail2005a)

??? abstract "Abstract"
	
	MIT CSAIL's entries for the TREC Question Answering track (Voorhees, 2005) focused on incorporating external general-knowledge sources into the question answering process. We also explored the effect of document retrieval on factoid question answering, in cooperation with a community focus on document retrieval. For the new relationship task, we present a new passage-retrieval based algorithm emphasizing synonymy, which performed best among automatic systems this year. Our most prominent new external knowledge source is the Wikipedia1, and its most useful component is the synonymy implicit in its subtitles and redirect link structure. Wikipedia is also a large new source of hypernym information. The main task included factoid questions, for which we modified the freely available Web-based Aranea question answering engine; list questions, for which we used hypernym hierarchies to constrain candidate answers; and definitional 'other' questions, for which we combined candidate snippets generated by several previous definition systems using a new novelty-based reranking method inspired by (Allan et al., 2003). [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KatzMBBFLLLMSUW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KatzMBBFLLLMSUW05,
		author = {Boris Katz and Gregory Marton and Gary C. Borchardt and Alexis Brownell and Sue Felshin and Daniel Loreto and Jesse Louis{-}Rosenberg and Ben Lu and Federico Mora and Stephan Stiller and {\"{O}}zlem Uzuner and Angela Wilcox},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {External Knowledge Sources for Question Answering},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/mit-katz.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KatzMBBFLLLMSUW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering with Lydia (TREC 2005 QA Track)

_Jae Hong Kil, Levon Lloyd, Steven Skiena_

- :fontawesome-solid-user-group: **Participant:** [suny.skiena](./qa/participants.md#suny.skiena)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/suny-stonybrook.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/suny-stonybrook.qa.pdf)
- :material-file-search: **Runs:** [SUNYSB05qa1](./qa/runs.md#sunysb05qa1) | [SUNYSB05qa2](./qa/runs.md#sunysb05qa2) | [SUNYSB05qa3](./qa/runs.md#sunysb05qa3)

??? abstract "Abstract"
	
	The goal of our participation in TREC 2005 was to determine how effectively our entity recognition/text analysis system, Lydia (http://www.textmap.com) [1-3] could be adapted to question answering. Indeed, our entire QA subsystem consists of only about 2000 additional lines of Perl code. Lydia detects every named entity mentioned in the AQUAINT corpus, and keeps a variety of information on named entities and documents in a relational database. We can collect candidate answers by means of information kept in the database. To produce a response for the main task or a ranked list of documents for the document ranking task, we rank the collected candidate answers or documents using syntactic and statistical analyses. A significant distinction from other question answering systems [4-6] presented earlier at TREC is that we do not use web sources such as Wikipedia and Google to generate candidate answers or answers. Rather, we only use syntactic and statistical features of the test set of questions and corpus provided. Our approach is independent of other sources, and finds answers from the text provided. We describe the design of Lydia and associated algorithms in Section 2, and focus on the design and algorithms of the QA system in Section 3. We then analyze the performance of the QA system in Section 4, and conclude this paper with discussion on future directions in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KilLS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KilLS05,
		author = {Jae Hong Kil and Levon Lloyd and Steven Skiena},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering with Lydia {(TREC} 2005 {QA} Track)},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/suny-stonybrook.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KilLS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2005: QA Retrieval and Robust Tracks

_James Mayfield, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [jhu.mayfield](./qa/participants.md#jhu.mayfield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf)
- :material-file-search: **Runs:** [apl05aug](./qa/runs.md#apl05aug) | [apl05w5](./qa/runs.md#apl05w5)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) focused on the Robust and Question Answering Information Retrieval (QAIR) Tracks at the 2005 TREC conference. For the Robust Track, we attempted to use the difference in retrieval scores between the top retrieved and the 100th document to predict performance; the result was not competitive. For QAIR, we augmented each query with terms that appeared frequently in documents that contained answers to questions from previous question sets; the results showed modest gains from the technique.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MayfieldM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MayfieldM05,
		author = {James Mayfield and Paul McNamee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{JHU/APL} at {TREC} 2005: {QA} Retrieval and Robust Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MayfieldM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AnswerFinder at TREC 2005

_Diego Mollá, Menno van Zaanen_

- :fontawesome-solid-user-group: **Participant:** [macquarieu.molla](./qa/participants.md#macquarieu.molla)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/macquarieu.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/macquarieu.qa.pdf)
- :material-file-search: **Runs:** [afrun1](./qa/runs.md#afrun1) | [afrun2](./qa/runs.md#afrun2)

??? abstract "Abstract"
	
	AnswerFinder has been completely redesigned for TREC 2005. The new architecture allows a fast development of question-answering systems for their deployment in the TREC tasks and other applications. The AnswerFinder modules use XML to express the services they provide, and they can be queried with XML for their services. The QA method now incorporates graph-based methods to compute the answerhood of a sentence and pin-point the answer. The system uses a set of graph-based rules that are learnt automatically. Unfortunately the system could not be completed and debugged before the TREC deadline and the runs did not fare well. Currently we are debugging and evaluating the system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MollaZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MollaZ05,
		author = {Diego Moll{\'{a}} and Menno van Zaanen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {AnswerFinder at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/macquarieu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MollaZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering Using the DLT System at TREC 2005

_Michael Mulcahy, Kieran White, Igal Gabbay, Aoife O'Gorman, Richard F. E. Sutcliffe_

- :fontawesome-solid-user-group: **Participant:** [ulimerick](./qa/participants.md#ulimerick)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ulimerick.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/ulimerick.qa.pdf)
- :material-file-search: **Runs:** [DLT05QA01](./qa/runs.md#dlt05qa01) | [DLT05QA02](./qa/runs.md#dlt05qa02)

??? abstract "Abstract"
	
	This article summarises our participation in the Question Answering (QA) Track at TREC. Section 2 outlines the architecture of our system. Section 3 describes the changes made for this year. Section 4 summarises the results of our submitted runs while Section 5 presents conclusions and proposes further steps.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MulcahyWGOS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MulcahyWGOS05,
		author = {Michael Mulcahy and Kieran White and Igal Gabbay and Aoife O'Gorman and Richard F. E. Sutcliffe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering Using the {DLT} System at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ulimerick.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MulcahyWGOS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JAVELIN I and II Systems at TREC 2005

_Eric Nyberg, Robert E. Frederking, Teruko Mitamura, Matthew W. Bilotti, Kerry Hannan, Laurie Hiyakumoto, Jeongwoo Ko, Frank Lin, Lucian Vlad Lita, Vasco Pedro, Andrew Hazen Schlaikjer_

- :fontawesome-solid-user-group: **Participant:** [cmu.nyberg](./qa/participants.md#cmu.nyberg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-javelin.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-javelin.qa.pdf)
- :material-file-search: **Runs:** [CMUJAV2005](./qa/runs.md#cmujav2005) | [CMUJAVSEM](./qa/runs.md#cmujavsem) | [CMUJAVSEMMAN](./qa/runs.md#cmujavsemman)

??? abstract "Abstract"
	
	The JAVELIN team at Carnegie Mellon University submitted three question-answering runs for the TREC 2005 evaluation. The JAVELIN I system was used to generate a single submission to the main track, and the JAVELIN II system was used to generate two submissions to the relationship track. In the sections that follow, we separately describe each system and the submission(s) it produced, and conclude with a brief summary.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NybergFMBHHKLLPS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/NybergFMBHHKLLPS05,
		author = {Eric Nyberg and Robert E. Frederking and Teruko Mitamura and Matthew W. Bilotti and Kerry Hannan and Laurie Hiyakumoto and Jeongwoo Ko and Frank Lin and Lucian Vlad Lita and Vasco Pedro and Andrew Hazen Schlaikjer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{JAVELIN} {I} and {II} Systems at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-javelin.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NybergFMBHHKLLPS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Building on Redundancy: Factoid Question Answering, Robust Retrieval  and the "Other"

_Dmitri Roussinov, Elena Filatova, Michael Chau, Jose Antonio Robles-Flores_

- :fontawesome-solid-user-group: **Participant:** [arizonau.roussinov](./qa/participants.md#arizonau.roussinov)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf)
- :material-file-search: **Runs:** [ASUQA01](./qa/runs.md#asuqa01) | [ASUQA02](./qa/runs.md#asuqa02)

??? abstract "Abstract"
	
	We have explored how redundancy based techniques can be used in improving factoid question answering, definitional questions (“other”), and robust retrieval. For the factoids, we explored the meta approach: we submit the questions to the several open domain question answering systems available on the Web and applied our redundancy-based triangulation algorithm to analyze their outputs in order to identify the most promising answers. Our results support the added value of the meta approach: the performance of the combined system surpassed the underlying performances of its components. To answer definitional (“other”) questions, we were looking for the sentences containing re-occurring pairs of noun entities containing the elements of the target. For robust retrieval, we applied our redundancy based Internet mining technique to identify the concepts (single word terms or phrases) that were highly related to the topic (query) and expanded the queries with them. All our results are above the mean performance in the categories in which we have participated, with one of our robust runs being the best in its category among all 24 participants. Overall, our findings support the hypothesis that using as much as possible textual data, specifically such as mined from the World Wide Web, is extre mely promising.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoussinovFCR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoussinovFCR05,
		author = {Dmitri Roussinov and Elena Filatova and Michael Chau and Jose Antonio Robles{-}Flores},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Building on Redundancy: Factoid Question Answering, Robust Retrieval and the "Other"},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoussinovFCR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QACTIS-based Question Answering at TREC 2005

_Patrick Schone, Gary M. Ciany, R. Cutts, Paul McNamee, James Mayfield, Thomas Smith_

- :fontawesome-solid-user-group: **Participant:** [nsa.schone](./qa/participants.md#nsa.schone)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dept-o-defense.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/dept-o-defense.qa.pdf)
- :material-file-search: **Runs:** [QACTIS05v3](./qa/runs.md#qactis05v3) | [QACTIS05v1](./qa/runs.md#qactis05v1) | [QACTIS05v2](./qa/runs.md#qactis05v2)

??? abstract "Abstract"
	
	The QACTIS system is being developed for the eventual purpose of providing a user the capability of multilingual question-answering from multimedia. QACTIS was tested at TREC-2005 as a means of identifying its successes and limitations in answering questions specifically from English newswire text as it moves in the direction of multilingual, multimedia question answering. In this paper, we provide a complete overview of those parts of QACTIS which focus specifically on text question-answering, and we analyze the system's performance at TREC-2005.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchoneCCMMS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchoneCCMMS05,
		author = {Patrick Schone and Gary M. Ciany and R. Cutts and Paul McNamee and James Mayfield and Thomas Smith},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {QACTIS-based Question Answering at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/dept-o-defense.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchoneCCMMS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Syntactic and Semantic Relation Analysis in Question Answering

_Renxu Sun, Jing Jiang, Yee Fan Tan, Hang Cui, Tat-Seng Chua, Min-Yen Kan_

- :fontawesome-solid-user-group: **Participant:** [nus.sun](./qa/participants.md#nus.sun)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/nus.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/nus.qa.pdf)
- :material-file-search: **Runs:** [NUSCHUA1](./qa/runs.md#nuschua1) | [NUSCHUA2](./qa/runs.md#nuschua2) | [NUSCHUA3](./qa/runs.md#nuschua3)

??? abstract "Abstract"
	
	Our participation at TREC this year focuses on integrating dependency and semantic relation analysis of external resources into our existing QA system. In TREC-13, we have proposed the use of dependency relation matching to perform answer extraction for factoid and list questions. The results showed that the technique is effective in answer extraction within the corpus. However, we have also identified some problems and limitations with this technique. First, dependency relation matching does not perform well on short questions, which have only very few key terms. Therefore we need to integrate query expansion and make use of external resources to provide additional contextual information to these short questions. Second, the technique cannot be directly applied to extract answer nuggets from external web pages. As web pages contain much more noise as compared to the corpus, statistical based dependency relation matching tends to make a lot of errors based on our previously trained model on the corpus. Moreover, we do not have sufficient training data to retrain a model on the web. Therefore we propose to use semantic relation analysis to supplement dependency relation analysis to extract answer nuggets for factoid and list questions on the web. Finally, we adopt a soft pattern matching model (Cui et al., 2005) for definition sentence retrieval in the definitional QA task. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SunJTCCK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/SunJTCCK05,
		author = {Renxu Sun and Jing Jiang and Yee Fan Tan and Hang Cui and Tat{-}Seng Chua and Min{-}Yen Kan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Syntactic and Semantic Relation Analysis in Question Answering},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/nus.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SunJTCCK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Enterprise, QA, Robust and Terabyte Experiments with Hummingbird SearchServer  at TREC 2005

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./qa/participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf)
- :material-file-search: **Runs:** [humQ05l](./qa/runs.md#humq05l) | [humQ05xl](./qa/runs.md#humq05xl) | [humQ05xle](./qa/runs.md#humq05xle)

??? abstract "Abstract"
	
	Hummingbird participated in 6 tasks of TREC 2005: the email known-item search task of the Enterprise Track, the document ranking task of the Question Answering Track, the ad hoc topic relevance task of the Robust Retrieval Track, and the adhoc, efficiency and named page finding tasks of the Terabyte Track. In the email known-item task, SearchServer found the desired message in the first 10 rows for more than 80% of the 125 queries. In the document ranking task, SearchServer returned an answering document in the first 10 rows for more than 90% of the 50 questions. In the robustness task, SearchServer found a relevant document in the first 10 rows for 88% of the 50 short (title) topics. In the terabyte adhoc and efficiency tasks, SearchServer found a relevant document in the first 10 rows for more than 90% of the 50 title topics. A new retrieval measure, First Relevant Score, is investigated; it is found to more accurately reflect known-item differences than reciprocal rank and to better reflect robustness across topics than the primary measure of the Robust track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson05,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Enterprise, QA, Robust and Terabyte Experiments with Hummingbird SearchServer at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Question Answering Experiments at Tokyo Institute of Technology

_Edward W. D. Whittaker, Pierre Chatain, Sadaoki Furui, Dietrich Klakow_

- :fontawesome-solid-user-group: **Participant:** [tokyo-it.whittaker](./qa/participants.md#tokyo-it.whittaker)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/tokyo-inst-tech.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/tokyo-inst-tech.qa.pdf)
- :material-file-search: **Runs:** [asked05a](./qa/runs.md#asked05a) | [asked05b](./qa/runs.md#asked05b) | [asked05c](./qa/runs.md#asked05c)

??? abstract "Abstract"
	
	In this paper we describe Tokyo Institute of Technology's speech group's first attempt at the TREC2005 question answering track which placed us eleventh overall among the best systems of the 30 participants in the track. All our evaluation systems were based on novel, non-linguistic, data-driven approaches to question answering. Our main focus was on the factoid task and we describe in detail one of the new models used in this year's evaluation runs. The list task was treated as a simple extension of the factoid task while the other question task was treated as an automatic summarization problem by important sentence selection. Our best system on the factoid task gave 21.3% correct in first place; our best result on the list task was an average F-score of 0.069 and on the other question task a best average F-score of 0.138.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WhittakerCFK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WhittakerCFK05,
		author = {Edward W. D. Whittaker and Pierre Chatain and Sadaoki Furui and Dietrich Klakow},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Question Answering Experiments at Tokyo Institute of Technology},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/tokyo-inst-tech.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WhittakerCFK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ILQUA–An IE-Driven Question Answering System

_Min Wu, Michelle Duan, Samira Shaikh, Sharon G. Small, Tomek Strzalkowski_

- :fontawesome-solid-user-group: **Participant:** [ualbany.min](./qa/participants.md#ualbany.min)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ualbany.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/ualbany.qa.pdf)
- :material-file-search: **Runs:** [ILQUA2](./qa/runs.md#ilqua2) | [ILQUA3](./qa/runs.md#ilqua3) | [ILQUA1](./qa/runs.md#ilqua1)

??? abstract "Abstract"
	
	ILQUA first participated in TREC QA main task in 2003. This year we have made modifications to the system by removing some components with poor performance and enhanced the system with new methods and new components. The newly built ILQUA is an IE-driven QA system. To answer “Factoid” and “List” questions, we apply our answer extraction methods on NE-tagged passages. The answer extraction methods adopted here are surface text pattern matching, n-gram proximity search and syntactic dependency matching. Surface text pattern matching has been applied in some previous TREC QA systems. However, the patterns used in ILQUA are automatically generated by a supervised learning system and represented in a format of regular expressions which can handle up to 4 question terms. N-gram proximity search and syntactic dependency matching are two steps of one component. N-grams of question terms are matched around every named entity in the candidate passages and a list of named entities are generated as answer candidate. These named entities go through a multi-level syntactic dependency matching until a final answer is generated. To answer “Other” questions, we parse the answer sentences of “Other” questions in 2004 main task and built syntactic patterns combined with semantic features. These patterns are applied to the parsed candidate sentences to extract answers of “Other” questions. The evaluation results showed ILQUA has reached an accuracy of 30.9% for factoid questions. ILQUA is an IE-driven QA system without any pre-compiled knowledge base of facts and it doesn't get reference from any other external search engine such as Google. The disadvantage of an IE-driven QA system is that there are some types of questions that can't be answered because the answer in the passages can't be tagged as appropriate NE types. Figure 1 shows the diagram of the ILQUA architecture.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuDSSS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuDSSS05,
		author = {Min Wu and Michelle Duan and Samira Shaikh and Sharon G. Small and Tomek Strzalkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {ILQUA--An IE-Driven Question Answering System},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ualbany.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuDSSS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDUQA on TREC 2005 QA Track

_Lide Wu, Xuanjing Huang, Yaqian Zhou, Zhushuo Zhang, Fen Lin_

- :fontawesome-solid-user-group: **Participant:** [fudan.wu](./qa/participants.md#fudan.wu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/fudanu-wu.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/fudanu-wu.qa.pdf)
- :material-file-search: **Runs:** [FDUQA14B](./qa/runs.md#fduqa14b) | [FDUQA14A](./qa/runs.md#fduqa14a)

??? abstract "Abstract"
	
	In this year's QA Track, we participant in the main and document ranking task and do not take part in the relation task. We put the most effort in factoid and definition questions, and very little on list questions and document ranking task. For factoid questions, we use three QA systems: system 1, system 2 and system 3. System 1 is very similar to our last year's system [Wu et al, 2004] except two main modifications. One is adding an answer validation-feedback scheme. The other is an improved answer projection module. System 2 is a classic QA system that does not use Web. System 3 is a pattern-based system that we used in TREC 2002 evaluation. The main contribution for factoid question is two improvements for Web-based QA system and the system combination. For definition question, we attempt to utilize both the existing definitions in the Web knowledge bases and the automatically generated structured patterns. Effective methods are adopted to make full use of these resources, and they promise high quality response to definition questions. For list questions, we use a pattern-based method to find more answers other than those found in the processing of factoid question. For document ranking task, we only collect the outputs from document searching or answer projection module. In the following, Section 2, 3, 4 will describe our algorithms to factoid, list and definition questions separately. Section 5 will present our results in TREC 2005.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHZZL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHZZL05,
		author = {Lide Wu and Xuanjing Huang and Yaqian Zhou and Zhushuo Zhang and Fen Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDUQA} on {TREC} 2005 {QA} Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/fudanu-wu.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHZZL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Insun05QA on QA Track of TREC 2005

_Yuming Zhao, Zhiming Xu, Yi Guan, Peng Li_

- :fontawesome-solid-user-group: **Participant:** [hit.zhao](./qa/participants.md#hit.zhao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/harbin-it.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/harbin-it.qa.pdf)
- :material-file-search: **Runs:** [Insun05QA1](./qa/runs.md#insun05qa1)

??? abstract "Abstract"
	
	This is the first time that our group takes part in the QA track. At TREC2005, the system we developed, Insun05QA, participated in the Main Task, which submitted answers to three types of questions: factoid questions, list questions and others questions. And we also submitted the document ranking which our answers are generated from. A new sentence similarity calculating method is used in our Insun05QA system. It can be considered as an extension of vector space model. And our QA system incorporates several useful tools. These tools include WordNet, developed by Princeton University, Minipar by Dekang Lin , and GATE, developed by University of Sheffield. Moreover, external knowledge such as knowledge from Internet is also widely used in our system. Since it is the first time that we take part in QA track and the preparing time is limited, we concentrate on the processing of factoid questions. And the methods we developed to process list and others questions are generated from the method used to process factoid questions. The structure of our Insun05QA system will be describe in Section 2, the details of how we process the factoid, list and others questions will be introduced in Section 3, and our results in TREC2005 will be presented in Section 4.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoXGL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoXGL05,
		author = {Yuming Zhao and Zhiming Xu and Yi Guan and Peng Li},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Insun05QA on {QA} Track of {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/harbin-it.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoXGL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Enterprise 

#### Overview of the TREC 2005 Enterprise Track

_Nick Craswell, Arjen P. de Vries, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ENTERPRISE.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/ENTERPRISE.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The goal of the enterprise track is to conduct experiments with enterprise data — intranet pages, email archives, document repositories — that reflect the experiences of users in real organisations, such that for example, an email ranking technique that is effective here would be a good choice for deployment in a real multi-user email search application. This involves both understanding user needs in enterprise search and development of appropriate IR techniques. The enterprise track began this year as the successor to the web track, and this is reflected in the tasks and measures. While the track takes much of its inspiration from the web track, the foci are on search at the enterprise scale, incorporating non-web data and discovering relationships between entities in the organisation. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellVS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellVS05,
		author = {Nick Craswell and Arjen P. de Vries and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2005 Enterprise Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ENTERPRISE.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellVS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melbourne University 2005: Enterprise and Terabyte Tasks

_Vo Ngoc Anh, William Webber, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [umelbourne.anh](./enterprise/participants.md#umelbourne.anh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umelbourne.ent.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/umelbourne.ent.tera.pdf)
- :material-file-search: **Runs:** [MU05ENd1](./enterprise/runs.md#mu05end1) | [MU05ENd2](./enterprise/runs.md#mu05end2) | [MU05ENd3](./enterprise/runs.md#mu05end3) | [MU05ENd4](./enterprise/runs.md#mu05end4) | [MU05ENd5](./enterprise/runs.md#mu05end5)

??? abstract "Abstract"
	
	This report describes the work done at The University of Melbourne for the TREC-2005 Enterprise and Terabyte Tracks. In the Enterprise Track, we participated in the Discussion Task. We tried a number of different methods to make use of special features of mailing lists to improve retrieval effectiveness, and found the use of thread context to be promising. In the Terabyte Track, we continued our work with impact-based ranking and sought to reduce indexing as well as query time. A new retrieval system has been developed for this purpose and has shown several improvements over our system from last year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnhWM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnhWM05,
		author = {Vo Ngoc Anh and William Webber and Alistair Moffat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Melbourne University 2005: Enterprise and Terabyte Tasks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umelbourne.ent.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnhWM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Language Modeling Approaches for Enterprise Tasks

_Leif Azzopardi, Krisztian Balog, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.mueller](./enterprise/participants.md#uamsterdam.mueller)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uamsterdam.ent.balog.pdf](http://trec.nist.gov/pubs/trec14/papers/uamsterdam.ent.balog.pdf)
- :material-file-search: **Runs:** [ToNsBs350](./enterprise/runs.md#tonsbs350) | [ToNsBs350F](./enterprise/runs.md#tonsbs350f) | [ToNsBs350FT5](./enterprise/runs.md#tonsbs350ft5) | [ToNsBs350FT](./enterprise/runs.md#tonsbs350ft) | [qdFlat](./enterprise/runs.md#qdflat) | [qdC](./enterprise/runs.md#qdc) | [OddsC](./enterprise/runs.md#oddsc) | [OddsWcEst](./enterprise/runs.md#oddswcest) | [qdWcEst](./enterprise/runs.md#qdwcest) | [uams05run0](./enterprise/runs.md#uams05run0) | [uams05run1](./enterprise/runs.md#uams05run1) | [uams05run2](./enterprise/runs.md#uams05run2) | [uams05run3](./enterprise/runs.md#uams05run3) | [uams05run4](./enterprise/runs.md#uams05run4)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2005 Enterprise track. We provide a detailed account of the ideas underlying our language modeling approaches to these tasks, report on our results, and give a summary of our findings so far.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AzzopardiBR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AzzopardiBR05,
		author = {Leif Azzopardi and Krisztian Balog and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Language Modeling Approaches for Enterprise Tasks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uamsterdam.ent.balog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AzzopardiBR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Research on Expert Search at Enterprise Track of TREC 2005

_Yunbo Cao, Jingjing Liu, Shenghua Bao, Hang Li_

- :fontawesome-solid-user-group: **Participant:** [microsoft.cao](./enterprise/participants.md#microsoft.cao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/microsoft-asia.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/microsoft-asia.ent.pdf)
- :material-file-search: **Runs:** [MSRA051](./enterprise/runs.md#msra051) | [MSRA052](./enterprise/runs.md#msra052) | [MSRA053](./enterprise/runs.md#msra053) | [MSRA054](./enterprise/runs.md#msra054) | [MSRA055](./enterprise/runs.md#msra055)

??? abstract "Abstract"
	
	We (MSRA team) participated in the Expert Search task at the Enterprise Track of TREC 2005. This document reports our experimental results on expert search. In our research, we have mainly investigated the effectiveness of a new approach to expert search in which we employ what is referred to as two-stage language model. It consists of two parts, relevance model and co-occurrence model. The relevance model represents whether or not a document is relevant to the query. The co-occurrence model represents whether or not the query is associated with a person. Both models are based on statistical language modeling. We have also examined the effectiveness of the use of a number of sub-models in the two-stage model; each sub-model is based on extraction of one type of metadata. In the body-body co-occurrence sub-model, for example, we consider the use of window-based co-occurrence. The co-occurrence is about whether the query and a person appear within the same window of text. In an extreme case the entire document is viewed as a window, and the submodel is referred to as document-based co-occurrence submodel. We also consider using clustering technique in reranking of persons. Persons are clustered according to their co-occurrences with topics and other persons. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaoLBL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaoLBL05,
		author = {Yunbo Cao and Jingjing Liu and Shenghua Bao and Hang Li},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Research on Expert Search at Enterprise Track of {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/microsoft-asia.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CaoLBL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC 14: Enterprise Track

_Nick Craswell, Hugo Zaragoza, Stephen Robertson_

- :fontawesome-solid-user-group: **Participant:** [microsoft.robertson](./enterprise/participants.md#microsoft.robertson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/microsoft-cambridge.enterprise.pdf](http://trec.nist.gov/pubs/trec14/papers/microsoft-cambridge.enterprise.pdf)
- :material-file-search: **Runs:** [MSRCDS1](./enterprise/runs.md#msrcds1) | [MSRCDS2](./enterprise/runs.md#msrcds2) | [MSRCDS3](./enterprise/runs.md#msrcds3) | [MSRCDS4](./enterprise/runs.md#msrcds4) | [MSRCKI1](./enterprise/runs.md#msrcki1) | [MSRCKI2](./enterprise/runs.md#msrcki2) | [MSRCKI3](./enterprise/runs.md#msrcki3) | [MSRCKI4](./enterprise/runs.md#msrcki4) | [MSRCDS5](./enterprise/runs.md#msrcds5) | [MSRCKI5](./enterprise/runs.md#msrcki5)

??? abstract "Abstract"
	
	A major focus of much work of the group (as it has been since the City University Okapi work) is the development and refinement of basic ranking algorithms. The workhorse remains the BM25 algorithm; recently [3, 4] we introduced a field-weighted version of this, allowing differential treatment of different fields in the original documents, such as title, anchor text, body text. We have also recently [2] been working on ways of analysing the possible contributions of static (query-independent) evidence, and of incorporating them into the scoring/ranking algorithm. Finally, we have been working on ways of tuning the resulting ranking functions, since each elaboration tends to introduce one or more new free parameters which have to be set through tuning. We used all these techniques successfully in our contribution to the Web track in TREC 2004 [4]. This year's relatively modest TREC effort is confined to applying essentially the same techniques to rather different data, in the Enterprise Track's known item (KI) and discussion search (DS) experiments. The main interest is whether we can identify some fields and features that lead to an improvement over a flat-text baseline, and as a side effect to verify that our ranking model can deliver the benefit.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellZR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellZR05,
		author = {Nick Craswell and Hugo Zaragoza and Stephen Robertson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Cambridge at {TREC} 14: Enterprise Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/microsoft-cambridge.enterprise.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellZR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Applying the Annotation View on Messages for Discussion Search

_Ingo Frommholz_

- :fontawesome-solid-user-group: **Participant:** [uduisburg.essen.frommholz](./enterprise/participants.md#uduisburg.essen.frommholz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uduisburg-essen.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/uduisburg-essen.ent.pdf)
- :material-file-search: **Runs:** [du05baseline](./enterprise/runs.md#du05baseline) | [du05quotweak](./enterprise/runs.md#du05quotweak) | [du05quotstrg](./enterprise/runs.md#du05quotstrg) | [du05highstrg](./enterprise/runs.md#du05highstrg) | [du05highweak](./enterprise/runs.md#du05highweak)

??? abstract "Abstract"
	
	In this paper we present our runs for the TREC 2005 Enterprise Track discussion search task. Our approaches are based on the view of replies as annotations of the previous message. Quotations in particular play an important role, since they indicate the target of such an annotation. We examine the role of quotations as a context for the unquoted parts as well as the role of quotations as an indicator of which parts of a message were seen as important enough to react to. Results show that retrieval effectiveness w.r.t. the topicality of email messages can be improved by applying this annotation view on email messages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Frommholz05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Frommholz05,
		author = {Ingo Frommholz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Applying the Annotation View on Messages for Discussion Search},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uduisburg-essen.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Frommholz05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2005: Enterprise Track

_Yupeng Fu, Wei Yu, Yize Li, Yiqun Liu, Min Zhang, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghua.ma](./enterprise/participants.md#tsinghua.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.ent.pdf)
- :material-file-search: **Runs:** [THUENT0501](./enterprise/runs.md#thuent0501) | [THUENT0502](./enterprise/runs.md#thuent0502) | [THUENT0503](./enterprise/runs.md#thuent0503) | [THUENT0504](./enterprise/runs.md#thuent0504) | [THUENT0505](./enterprise/runs.md#thuent0505)

??? abstract "Abstract"
	
	IR group of Tsinghua University participated in the expert finding task of TREC2005 enterprise track this year. We developed a novel method which is called document reorganization to solve the problem of locating expert for certain query topics. This method collects and combines related information from different media formats to organize a document which describes an expert candidate. This method proves both effective and efficient for expert finding task. Our submitted run (THUENT0505) obtains the best performance in all participants with evaluation metric MAP. The reorganized documents are also significantly smaller in size than the original corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FuYLLZM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/FuYLLZM05,
		author = {Yupeng Fu and Wei Yu and Yize Li and Yiqun Liu and Min Zhang and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2005: Enterprise Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.ent.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FuYLLZM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSUSM at TREC 2005: Genomics and Enterprise Track

_Rocio Guillén_

- :fontawesome-solid-user-group: **Participant:** [csusm.guillen](./enterprise/participants.md#csusm.guillen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/calstateu-sanmarcos.geo.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/calstateu-sanmarcos.geo.ent.pdf)
- :material-file-search: **Runs:** [csusm1](./enterprise/runs.md#csusm1) | [csusm2](./enterprise/runs.md#csusm2)

??? abstract "Abstract"
	
	In this paper we report on the approach, experiments and results for the Enterprise Track and the Genomics Track. We participated in the adhoc and one of the categorization tasks for the Genomics track. For the enterprise track we participated in the known-item search. We ran experiments using Indri (1], which combines inference networks with language modeling, for the adhoc and the known-item search tasks. For the categorization task we filtered the documents in different stages using decision trees.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Guillen05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Guillen05,
		author = {Rocio Guill{\'{e}}n},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CSUSM} at {TREC} 2005: Genomics and Enterprise Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/calstateu-sanmarcos.geo.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Guillen05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pitt at TREC 2005: HARD and Enterprise

_Daqing He, Jae-wook Ahn_

- :fontawesome-solid-user-group: **Participant:** [upittsburgh.he](./enterprise/participants.md#upittsburgh.he)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/upittsburgh.hard.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/upittsburgh.hard.ent.pdf)
- :material-file-search: **Runs:** [PITTDTA1](./enterprise/runs.md#pittdta1) | [PITTDTA2SML1](./enterprise/runs.md#pittdta2sml1) | [PITTDTA2SML2](./enterprise/runs.md#pittdta2sml2) | [PITTDTA2BIG1](./enterprise/runs.md#pittdta2big1) | [PITTKIA1W7](./enterprise/runs.md#pittkia1w7) | [PITTKIA1W8](./enterprise/runs.md#pittkia1w8) | [PITTKIWB2](./enterprise/runs.md#pittkiwb2) | [PITTKINB1](./enterprise/runs.md#pittkinb1)

??? abstract "Abstract"
	
	The University of Pittsburgh team participated in two tracks for TREC 2005: the High Accuracy Retrieval from Documents (HARD) track and the Enterprise Retrieval track. The goal of Pitt's HARD study in TREC 2005 was to examine the effectiveness of applying Self Organizing Maps (SOM) as a visual presentation tool and as a clustering tool in the context of HARD tasks, especially its role in clarification form generation. Our experiment results demonstrate that SOM can be used as a clustering tool to generate terms for query expansion based on interactive relevance feedback. It produced significant improvement over the baseline when measured by R-Prec. However, its effectiveness of being a visualization tool for users to make relevance feedback still needs careful examination and further studies. Our goal in this year's enterprise search track was to study the effect of query expansion based on an expansion corpus in retrieving emails from an email corpus. The expansion corpus consisted of the WWW, People and ESW sub-collections of the W3C test collection. The results indicate that query expansion based on the expansion corpus can achieve significant improvement over the no expansion baselines. However, there is no significant difference to the simpler query expansion approach using blind relevance feedback. Interestingly the terms used in these two query expansion approaches are different, with averagely only 6 term overlap among 20 possible terms. Further study is needed for examining the effect of combining these two approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeA05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeA05,
		author = {Daqing He and Jae{-}wook Ahn},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pitt at {TREC} 2005: {HARD} and Enterprise},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/upittsburgh.hard.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeA05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Menagerie of Tracks at Maryland: HARD, Enterprise, QA, and Genomics,  Oh My!

_Jimmy Lin, Eileen G. Abels, Dina Demner-Fushman, Douglas W. Oard, Philip Fei Wu, Yejun Wu_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./enterprise/participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf)
- :material-file-search: **Runs:** [THRQUOT](./enterprise/runs.md#thrquot) | [THRNOQNARR](./enterprise/runs.md#thrnoqnarr) | [THRNOQUOT](./enterprise/runs.md#thrnoquot) | [TITLEDEFAULT](./enterprise/runs.md#titledefault) | [TITLETRANS](./enterprise/runs.md#titletrans) | [KITRANS](./enterprise/runs.md#kitrans) | [KITHRQUOT](./enterprise/runs.md#kithrquot) | [KITHRNOQUOT](./enterprise/runs.md#kithrnoquot) | [KIDEFAULT](./enterprise/runs.md#kidefault)

??? abstract "Abstract"
	
	This year, the University of Maryland participated in four separate tracks: HARD, enterprise, question answering, and genomics. Our HARD experiments involved a trained intermediary who searched for documents on behalf of the user, created clarification forms manually, and exploited user responses accordingly. The aim was to better understand the nature of single-iteration clarification dialogs and to develop an “ontology of clarifications” that can be leveraged to guide system development. For the enterprise track, we submitted official runs to the Known Item Search and the Discussion Search tasks. Document transformation to normalize dates and version numbers was found to be helpful, but suppression of text quoted from earlier messages and expansion of the indexed terms for a message based on subject line threading proved to not be. For the QA track, we submitted a manual run of “other” questions in an effort to quantify human performance on the task. Our genomics track participation was in collaboration with the National Library of Medicine, and is primarily reported in NLM's overview paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinADOWW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinADOWW05,
		author = {Jimmy Lin and Eileen G. Abels and Dina Demner{-}Fushman and Douglas W. Oard and Philip Fei Wu and Yejun Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Menagerie of Tracks at Maryland: HARD, Enterprise, QA, and Genomics, Oh My!},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf},
		timestamp = {Sat, 29 Jul 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinADOWW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2005: Experiments in Terabyte and  Enterprise Tracks with Terrier

_Craig Macdonald, Ben He, Vassilis Plachouras, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uglasgow.ounis](./enterprise/participants.md#uglasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uglasgow.tera.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/uglasgow.tera.ent.pdf)
- :material-file-search: **Runs:** [uogEBase](./enterprise/runs.md#uogebase) | [uogEDates1](./enterprise/runs.md#uogedates1) | [uogEDates2](./enterprise/runs.md#uogedates2) | [uogEDates12T](./enterprise/runs.md#uogedates12t) | [uogES05B2](./enterprise/runs.md#uoges05b2) | [uogES05Cbase](./enterprise/runs.md#uoges05cbase) | [uogES05Cbis](./enterprise/runs.md#uoges05cbis) | [uogES05CbaDT](./enterprise/runs.md#uoges05cbadt) | [uogES05CbiH](./enterprise/runs.md#uoges05cbih)

??? abstract "Abstract"
	
	With our participation in TREC 2005, we continue experiments using Terrier, a modular and scalable Information Retrieval (IR) framework, in 4 tasks from the Terabyte and Enterprise tracks. In the Terabyte track, we investigate new Divergence From Randomness weighting models, and a novel query expansion approach that can take into account various document fields, namely content, title and anchor text. In addition, we test a new selective query expansion mechanism which determines the appropriateness of using query expansion on a per-query basis, using statistical information from a low-cost query performance predictor. In the Enterprise track, we investigate combining document fields evidence with other information occurring in an Enterprise setting. In the email known item task, we also investigate temporal and thread priors suitable for email search. In the expert search task, for each candidate, we generate profiles of expertise evidence from the W3C collection. Moreover, we propose a model for ranking these candidate profiles in response to a query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacdonaldHPO05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacdonaldHPO05,
		author = {Craig Macdonald and Ben He and Vassilis Plachouras and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2005: Experiments in Terabyte and Enterprise Tracks with Terrier},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uglasgow.tera.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacdonaldHPO05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIM at TREC 2005

_Junyu Niu, Lin Sun, Luqun Lou, Fang Deng, Chen Lin, Haiqing Zheng, Xuanjing Huang_

- :fontawesome-solid-user-group: **Participant:** [fudan.niu](./enterprise/participants.md#fudan.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/fudanu-sun.geo.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/fudanu-sun.geo.ent.pdf)
- :material-file-search: **Runs:** [WIMent01](./enterprise/runs.md#wiment01)

??? abstract "Abstract"
	
	This paper describes the three TREC tasks we participated in this year, which are, Genomics track's categorization task and ad hoc task, and Enterprise track's known item search task. For the categorization task, we adopt a domain-specific terms extraction method and an ontology-based method for feature selection. A SVM classifier and a Rocchio based two staged classifier were also used in this experiment. For the ad-hoc task, we used BM25 algorithm, probabilistic model and query expansion. For the Enterprise track, language model was adopted, and entity recognition was also implemented in our experiment.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NiuSLDLZH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/NiuSLDLZH05,
		author = {Junyu Niu and Lin Sun and Luqun Lou and Fang Deng and Chen Lin and Haiqing Zheng and Xuanjing Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIM} at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/fudanu-sun.geo.ent.pdf},
		timestamp = {Tue, 20 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NiuSLDLZH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with Language Models for Known-Item Finding of E-mail  Messages

_Paul Ogilvie, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu.dir.callan](./enterprise/participants.md#cmu.dir.callan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-callan.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-callan.ent.pdf)
- :material-file-search: **Runs:** [CMUallon](./enterprise/runs.md#cmuallon) | [CMUnoprior](./enterprise/runs.md#cmunoprior) | [CMUnoPS](./enterprise/runs.md#cmunops) | [CMUnoPSD](./enterprise/runs.md#cmunopsd) | [CMUnoPSDT](./enterprise/runs.md#cmunopsdt)

??? abstract "Abstract"
	
	We present experiments using language models to rank e-mail messages for the Known-Item Finding task of the Enterprise track. We combine evidence from the text of the message, its subject, the text of the thread the in which the message occurs, and the text of messages that are in reply to the message. We find that the only statistically significant differences suggest that in addition to the text of the message, the subject is a very important piece of evidence. We also explore the use of a depth based prior, where emphasis is place on messages near the root of the thread structure, which has mixed results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OgilvieC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/OgilvieC05,
		author = {Paul Ogilvie and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with Language Models for Known-Item Finding of E-mail Messages},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-callan.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OgilvieC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Lowlands' TREC Experiments 2005

_Henning Rode, Djoerd Hiemstra, Georgina Ramírez, Thijs Westerveld, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [lowlands.devries](./enterprise/participants.md#lowlands.devries)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/lowlands-team.hard.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/lowlands-team.hard.ent.pdf)
- :material-file-search: **Runs:** [baseLMlam05](./enterprise/runs.md#baselmlam05) | [LMlam08Thr](./enterprise/runs.md#lmlam08thr) | [baseLMlam08](./enterprise/runs.md#baselmlam08) | [LMMlam05Thr](./enterprise/runs.md#lmmlam05thr) | [LMplaintext](./enterprise/runs.md#lmplaintext) | [LMheaderAND](./enterprise/runs.md#lmheaderand) | [LMheaderOR](./enterprise/runs.md#lmheaderor) | [LMsubjectAND](./enterprise/runs.md#lmsubjectand) | [LMsubjectOR](./enterprise/runs.md#lmsubjector) | [LLEXemails](./enterprise/runs.md#llexemails)

??? abstract "Abstract"
	
	This paper describes our participation to the TREC HARD track (High Accuracy Retrieval of Documents) and the TREC Enterprise track. The main goal of our HARD participation is the development and evaluation of so-called query profiles: Short summaries of the retrieved results that enable the user to perform more focused search, for instance by zooming in on a particular time period. The main goal of our Enterprise track participation is to investigate the potential of the structural information for this type of retrieval task. In particular, we study the use of the thread information and the subject and header fields of the email documents. As a secondary and long standing research goal, we aim at developing an information retrieval framework that supports many diverse retrieval applications by means of one simple yet powerful query language (similar to SQL or relational algebra) that hides the implementation details of retrieval approaches from the application developer, while still giving the application developer control over the ranking process. Both the HARD system and the Enterprise system (as well as our TRECVID video retrieval system [14]) are based on MonetDB, an open source database system developed at CWI [1]. The paper is organised as follows. First, we discusses our participation in the HARD track. We define query profiles and discuss the way we generate them in Section 2. Section 3 describes the clarification forms used and Section 4 explains how we refine the queries and rank the results. We end this part by analysing our experimental results in Section 5 and giving some conclusions for this track in Section 6. The second part of the paper discusses our participation in the enterprise track. We start by describing the system and experimental setup in Section 7. Section 8 discusses the approaches taken for each of the subtasks and Section 9 analyses the results. We end by giving some conclusions and future work for this track in Section 10. The final part of the paper describes our future plans for building a so-called parameterised search engine within the Dutch National project MultimediaN.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RodeHRWV05.bib) "
	```
	@inproceedings{DBLP:conf/trec/RodeHRWV05,
		author = {Henning Rode and Djoerd Hiemstra and Georgina Ram{\'{\i}}rez and Thijs Westerveld and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Lowlands' {TREC} Experiments 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/lowlands-team.hard.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RodeHRWV05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The QMUL Team with Probabilistic SQL at Enterprise Track

_Thomas Roelleke, Elham Ashoori, Hengzhi Wu, Zhen Cai_

- :fontawesome-solid-user-group: **Participant:** [qm-univ-london.roelleke](./enterprise/participants.md#qm-univ-london.roelleke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/queen-mary-ulondon.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/queen-mary-ulondon.ent.pdf)
- :material-file-search: **Runs:** [qmirdtu](./enterprise/runs.md#qmirdtu) | [qmirdts](./enterprise/runs.md#qmirdts) | [qmirdju](./enterprise/runs.md#qmirdju) | [qmirkidju](./enterprise/runs.md#qmirkidju) | [qmirkidtu](./enterprise/runs.md#qmirkidtu) | [qmirex1](./enterprise/runs.md#qmirex1) | [qmirex2](./enterprise/runs.md#qmirex2) | [qmirex3](./enterprise/runs.md#qmirex3) | [qmirex4](./enterprise/runs.md#qmirex4)

??? abstract "Abstract"
	
	The enterprise track caught our attention, since the task is similar to a project we carried our for the BBC. Our motivation for participation has been twofold: On one hand, there is the usual challenge to design and test the quality of retrieval strategies. On the other hand, and for us very important, the TREC participation has been an opportunity to investigate the resource effort it requires to deliver a TREC result. Our main findings from this TREC participation are: 1. Through the consequent usage of our probabilistic variant of SQL, we could describe retrieval strategies within a few lines of code. 2. The processing time proved sufficient to deal with the collection. 3. The abstraction-oriented data modelling layers of our HySpirit framework enable relatively junior researches to explore a TREC collection and submit runs. 4. For the less complex retrieval tasks (discussion search, known-item search), minimal resources lead to acceptable results, whereas for the more complex retrieval tasks (expert search), inclusion and combination of all available evidence appear to significantly improve retrieval quality.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoellekeAWC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoellekeAWC05,
		author = {Thomas Roelleke and Elham Ashoori and Hengzhi Wu and Zhen Cai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {QMUL} Team with Probabilistic {SQL} at Enterprise Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/queen-mary-ulondon.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoellekeAWC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Enterprise Track Experiments at BUPT

_Zhao Ru, Yuehua Chen, Weiran Xu, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [beijingu.guo](./enterprise/participants.md#beijingu.guo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/beijingu-of-pt.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/beijingu-of-pt.ent.pdf)
- :material-file-search: **Runs:** [prisds1](./enterprise/runs.md#prisds1) | [prisds2](./enterprise/runs.md#prisds2) | [prisds3](./enterprise/runs.md#prisds3) | [prisds4](./enterprise/runs.md#prisds4) | [prisds5](./enterprise/runs.md#prisds5) | [priski1](./enterprise/runs.md#priski1) | [priski2](./enterprise/runs.md#priski2) | [priski3](./enterprise/runs.md#priski3) | [priski4](./enterprise/runs.md#priski4) | [priski5](./enterprise/runs.md#priski5) | [PRISEX1](./enterprise/runs.md#prisex1) | [PRISEX2](./enterprise/runs.md#prisex2) | [PRISEX3](./enterprise/runs.md#prisex3) | [PRISEX4](./enterprise/runs.md#prisex4) | [PRISEX5](./enterprise/runs.md#prisex5)

??? abstract "Abstract"
	
	This paper introduces and analyzes some experiments to find valid methods and features in enterprise search. For this purpose, two main experiments have been done. One is to retrieve some emails which contain the required information in all the emails of an enterprise, and the other is to try to find some experts who are helpful in a particular fields. Some features of the intranet dataset, such as the subject, the author, the date and the thread, are proved to be useful when searching an email. A new two-stage rank method which is different from traditional IR is introduced for expert search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuCXG05.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuCXG05,
		author = {Zhao Ru and Yuehua Chen and Weiran Xu and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Enterprise Track Experiments at {BUPT}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/beijingu-of-pt.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuCXG05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments for HARD and Enterprise Tracks

_Olga Vechtomova, Maheedhar Kolla, Murat Karamuftuoglu_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.vechtomova](./enterprise/participants.md#uwaterloo.vechtomova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uwaterloo-vechtomova.hard.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/uwaterloo-vechtomova.hard.ent.pdf)
- :material-file-search: **Runs:** [UwatEntDSq](./enterprise/runs.md#uwatentdsq) | [UwatEntDS](./enterprise/runs.md#uwatentds) | [UwatEntDSth](./enterprise/runs.md#uwatentdsth) | [UWATEntKI](./enterprise/runs.md#uwatentki)

??? abstract "Abstract"
	
	The main theme in our participation in this year's HARD track was experimentation with the effect of lexical cohesion on document retrieval. Lexical cohesion is a major characteristic of natural language texts, which is achieved through semantic connectedness between words in text, and expresses continuity between the parts of text [7]. Segments of text which are about the same or similar subjects (topics) have higher lexical cohesion, i.e. share a larger number of words than unrelated segments. We have experimented with two approaches to the selection of query expansion terms based on lexical cohesion: (1) by selecting query expansion terms that form lexical links between the distinct original query terms in the document (section 1.1); and (2) by identifying lexical chains in the document and selecting query expansion terms from the strongest lexical chains (section 1.2).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VechtomovaKK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/VechtomovaKK05,
		author = {Olga Vechtomova and Maheedhar Kolla and Murat Karamuftuoglu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments for {HARD} and Enterprise Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uwaterloo-vechtomova.hard.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VechtomovaKK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 14 Enterprise Track at CSIRO and ANU

_Mingfang Wu, David Hawking, Paul Thomas_

- :fontawesome-solid-user-group: **Participant:** [csiro.hawking](./enterprise/participants.md#csiro.hawking)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/csiro.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/csiro.ent.pdf)
- :material-file-search: **Runs:** [csiroanuds1](./enterprise/runs.md#csiroanuds1) | [csiroanuds3](./enterprise/runs.md#csiroanuds3) | [csiroanuds5](./enterprise/runs.md#csiroanuds5) | [csiroanuds7](./enterprise/runs.md#csiroanuds7) | [csiroanuds8](./enterprise/runs.md#csiroanuds8) | [csiroanuki1](./enterprise/runs.md#csiroanuki1) | [csiroanuki2](./enterprise/runs.md#csiroanuki2) | [csiroanuki3](./enterprise/runs.md#csiroanuki3) | [csiroanuki5](./enterprise/runs.md#csiroanuki5) | [csiroanuki6](./enterprise/runs.md#csiroanuki6)

??? abstract "Abstract"
	
	The primary goals of the CSIRO and ANU team's participation in the enterprise track were two-fold: 1) to investigate how well our search engine PADRE responds to the new collection and the new tasks, and 2) to explore if document structure specific to an email collection can be used to improve system performance. By the time of submission deadline, we completed two tasks: known-item search and discussion search. For both tasks, we used the PADRE retrieval system [1], in which the Okapi BM25 relevance function was implemented. Each message in the collection was treated as an independent document, so both topic distillation scoring and same site suppression mechanism were turned off (i.e. -nocool and -SSS0 respectively). During the indexing, stemming and stopword elimination were not applied and sequences of letters and/or digits were considered as indexable words. We parsed the HTML pages in the original collection into an XML format (the DTD is shown in the appendix), and removed non-email pages. Our parsed collection includes 174,311 email messages, and we used this collection for our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHT05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHT05,
		author = {Mingfang Wu and David Hawking and Paul Thomas},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 14 Enterprise Track at {CSIRO} and {ANU}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/csiro.ent.pdf},
		timestamp = {Wed, 07 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WuHT05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CNDS Expert Finding System for TREC 2005

_Conglei Yao, Bo Peng, Jing He, Zhifeng Yang_

- :fontawesome-solid-user-group: **Participant:** [pekingu.yan](./enterprise/participants.md#pekingu.yan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/pekingu-he.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/pekingu-he.ent.pdf)
- :material-file-search: **Runs:** [CNDS01](./enterprise/runs.md#cnds01) | [CNDS04LC](./enterprise/runs.md#cnds04lc) | [CNDS03](./enterprise/runs.md#cnds03) | [CNDS02](./enterprise/runs.md#cnds02) | [CNDS06](./enterprise/runs.md#cnds06)

??? abstract "Abstract"
	
	This paper describes our system developed for Expert Finding task of Enterprise Track for TREC2005. This system employs 3 methods, traditional IR method, email clustering method and entry page finding method, to find experts related to a specific topic in W3C corpus. Experiment indicates that traditional IR method is useful to expert finding if the query is well generated, email clustering method is helpful when the mail list is relevant to a unique work group or committee, and entry page finding method is valuable while the topic is the theme of a special group. We use result aggregation methods of linear synthesis to combine the results generated by the three methods,. Of our 5 runs submitted for Expert Finding task, the best run is the one generated by linear synthesis, providing a MAP score of 0.2174(Bpref of 0.4299 and p@10 of 0.3460).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yang05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yang05,
		author = {Conglei Yao and Bo Peng and Jing He and Zhifeng Yang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CNDS} Expert Finding System for {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/pekingu-he.ent.pdf},
		timestamp = {Mon, 15 May 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Yang05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Enterprise Track Results from Drexel

_Weizhong Zhu, Robert B. Allen, Min Song_

- :fontawesome-solid-user-group: **Participant:** [drexelu.allen](./enterprise/participants.md#drexelu.allen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/drexelu.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/drexelu.ent.pdf)
- :material-file-search: **Runs:** [NON](./enterprise/runs.md#non) | [PRO](./enterprise/runs.md#pro) | [CON](./enterprise/runs.md#con) | [KNOWNITEM](./enterprise/runs.md#knownitem) | [UNKNOWN](./enterprise/runs.md#unknown) | [DrexelKI05a](./enterprise/runs.md#drexelki05a) | [DrexelKI05b](./enterprise/runs.md#drexelki05b) | [DrexelKI05c](./enterprise/runs.md#drexelki05c) | [DrexelKI05d](./enterprise/runs.md#drexelki05d) | [DREXEXP1](./enterprise/runs.md#drexexp1) | [DREXEXP2](./enterprise/runs.md#drexexp2)

??? abstract "Abstract"
	
	The primary goal of Discussion Search is to identify a discussion about a topic. A secondary goal is to determine whether a given message expresses pro or con arguments with respect to the discussion. We employed a combination of POS-driven query expansion and a text-classification technique from [6]. The results of those previous experiments indicated that the technique best performed in extracting protein-protein interaction pairs from MEDLINE. The original email corpus was extremely heterogeneous. We first applied the Tidy HTML parser to strip tags and to identify data such as the sender, thread history, and subject of the messages. We then linked messages into threads in two ways. The corpus provides thread index files for email communications. These thread indexes are composed of hieratically structured multiple discussion threads and single thread. For multiple discussion threads, we unified them into a thread document. We also combined single documents when they had the same subject.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuAS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuAS05,
		author = {Weizhong Zhu and Robert B. Allen and Min Song},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Enterprise Track Results from Drexel},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/drexelu.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuAS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Robust 

#### Overview of the TREC 2005 Robust Retrieval Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ROBUST.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/ROBUST.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The robust retrieval track explores methods for improving the consistency of retrieval technology by focusing on poorly performing topics. The retrieval task in the track is a traditional ad hoc retrieval task where the evaluation methodology emphasizes a system's least effective topics. The 2005 edition of the track used 50 topics that had been demonstrated to be difficult on one document collection, and ran those topics on a different document collection. Relevance information from the first collection could be exploited in producing a query for the second collection, if desired. The main measure for evaluating system effectiveness is “gmap”, a variant of the traditional MAP measure that uses a geometric mean rather than an arithmetic mean to average individual topic results. As in previous years, the most effective retrieval strategy was to expand queries using terms derived from additional corpora. The relative difficulty of topics differed across the two document sets. Systems were also required to rank the topics by predicted difficulty. This task is motivated by the hope that systems will eventually be able to use such predictions to do topic-specific processing. This remains a challenging task. Since difficulty depends on more then the topic set alone, prediction methods that train on data from other test collections do not generalize well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees05a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees05a,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2005 Robust Retrieval Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ROBUST.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees05a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fuzzy Proximity Ranking with Boolean Queries

_Michel Beigbeder, Annabelle Mercier_

- :fontawesome-solid-user-group: **Participant:** [emse.mercier](./robust/participants.md#emse.mercier)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ecole-des-mines.pdf](http://trec.nist.gov/pubs/trec14/papers/ecole-des-mines.pdf)
- :material-file-search: **Runs:** [RIMam05t050](./robust/runs.md#rimam05t050) | [RIMam05t200](./robust/runs.md#rimam05t200) | [RIMam05l050](./robust/runs.md#rimam05l050) | [RIMam05l200](./robust/runs.md#rimam05l200) | [RIMam05d200](./robust/runs.md#rimam05d200)

??? abstract "Abstract"
	
	Based on the idea that the closer the query terms are in a document, the more relevant this document is, we experiment an IR method based on a fuzzy proximity degree of the query term occurences in a document to compute its relevance to the query. Our model is able to deal with Boolean queries, but contrary to the traditional extensions of the basic Boolean IR model, it does not explicitly use a proximity operator. The fuzzy term proximity is controlled with an influence function. Given a query term and a document, the influence function associates to each position in the text a value dependant on the distance of the nearest occurence of this query term. To model proximity, this function is decreasing with distance. Different forms of function can be used: triangular, gaussian etc. For practical reasons only functions with finite support were used. The support of the function is limited by a constant called k. The fuzzy term proximity functions are associated to every leaves of the query tree. Then fuzzy proximities are computed for every nodes with a post-order tree traversal. Given the fuzzy proximities of the sons of a node, its fuzzy proximity is computed, like in the fuzzy IR models, with a mimimum (resp. maximum) combination for conjunctives (resp. disjunctives) nodes. Finally, a fuzzy query proximity value is obtained for each position in this document at the root of the query tree. The score of this document is the integration of the function obtained at the tree root. For the experiments, we modified Lucy (version 0.5.2) to implement our IR model. Three query sets are used for our eight runs. One set is manually built with the title words and some description words. Each of these words is OR'ed with its derivatives like plurals for instance. Then the OR nodes obtained are AND'ed at the tree root. The two automatic query sets are built with an AND of automatically extracted terms from either the title field or the description field. These three query sets are submitted to our system with two values of k: 50 and 200. As our method is aimed at high precision, it sometimes give less than one thousand answers. In such cases, the documents retrieved by the BM-25 method implemented in Lucy was concatenated after our result list.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BeigbederM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BeigbederM05,
		author = {Michel Beigbeder and Annabelle Mercier},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Fuzzy Proximity Ranking with Boolean Queries},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ecole-des-mines.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BeigbederM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass Robust 2005: Using Mixtures of Relevance Models for Query Expansion

_Donald Metzler, Fernando Diaz, Trevor Strohman, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./robust/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umass-robust.pdf](http://trec.nist.gov/pubs/trec14/papers/umass-robust.pdf)
- :material-file-search: **Runs:** [indri05RdmT](./robust/runs.md#indri05rdmt) | [indri05RdmD](./robust/runs.md#indri05rdmd) | [indri05RdmeD](./robust/runs.md#indri05rdmed) | [indri05RdmeT](./robust/runs.md#indri05rdmet) | [indri05RdmmT](./robust/runs.md#indri05rdmmt)

??? abstract "Abstract"
	
	This paper describes the UMass TREC 2005 Robust Track experiments. We focus on approaches that use term proximity and pseudo-relevance feedback using external collections. Our results indicate both approaches are highly effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MetzlerDSC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MetzlerDSC05,
		author = {Donald Metzler and Fernando Diaz and Trevor Strohman and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass Robust 2005: Using Mixtures of Relevance Models for Query Expansion},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umass-robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MetzlerDSC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Conceptual Indexing Approach for the TREC Robust Task

_Mustapha Baziz, Mohand Boughanem, Nathalie Aussenac-Gilles_

- :fontawesome-solid-user-group: **Participant:** [irit-sig.boughanem](./robust/participants.md#irit-sig.boughanem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/irit.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/irit.robust.pdf)
- :material-file-search: **Runs:** [CKonT](./robust/runs.md#ckont) | [CKonD](./robust/runs.md#ckond) | [CKonTSE](./robust/runs.md#ckontse) | [CKSEonD](./robust/runs.md#ckseond) | [CKSEonTSE](./robust/runs.md#ckseontse)

??? abstract "Abstract"
	
	This paper describes our participation to the TREC 2005 Robust Task. A method of conceptual indexing based on WordNet is used. Both documents and queries are mapped onto WordNet. Thus concepts belonging to WordNet synsets are identified and extracted whereas those having a single sense are expanded.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BazizBA05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BazizBA05,
		author = {Mustapha Baziz and Mohand Boughanem and Nathalie Aussenac{-}Gilles},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Conceptual Indexing Approach for the {TREC} Robust Task},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/irit.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BazizBA05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2005: Terabyte and Robust Track

_Yaniv Bernstein, Bodo Billerbeck, Steven Garcia, Nicholas Lester, Falk Scholer, Justin Zobel, William Webber_

- :fontawesome-solid-user-group: **Participant:** [rmit.scholer](./robust/participants.md#rmit.scholer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/rmit-falk.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/rmit-falk.tera.robust.pdf)
- :material-file-search: **Runs:** [rmit5t1025](./robust/runs.md#rmit5t1025) | [rmit5t0530N](./robust/runs.md#rmit5t0530n) | [rmit5t1545Td](./robust/runs.md#rmit5t1545td) | [rmit5t0000](./robust/runs.md#rmit5t0000) | [rmit5d1025](./robust/runs.md#rmit5d1025)

??? abstract "Abstract"
	
	RMIT University participated in the terabyte and robust tracks in TREC 2005. The terabyte track consists of the three tasks: adhoc retrieval, efficient retrieval, and named page finding. For the adhoc retrieval task we used a language modelling approach based on query likelihood, as well as a new technique aimed at reducing the amount of memory used for ranking documents. For the efficiency task, we submitted results from both a single-machine system and one that was distrubuted among a number of machines, with promising results. The named page task was organised by RMIT University and as a result we repeated last year's experiments, slightly modified, with this year's data. The robust track has two subtasks: adhoc retrieval, and query difficulty prediction. For adhoc retrieval, we employed a standard local analysis query expansion method, sourcing expansion terms for different runs from the collection supplied, from a side corpus, or a combination of both. In one run, we also tested removing duplicate documents from the list of results; in order to predict topic difficulty, we evaluated different document priors of the documents in the result set, in the hope of supplying a more robust set of answers at the cost of returning a potentially smaller number of relevant documents. The second task was to predict query difficulty. To this end, we compared the order of the documents in the result sets to the ordering as determined by document priors. A high similarity in orderings indicated that the query was poor. Two different priors were used. The first was based on document access counts, where each document is given a score that is derived from how likely it is to be ranked by a randomly generated query. The second was directly related to the document size. In this paper we outline our approaches and experiments in both tracks, and discuss our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BernsteinBGLSZW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BernsteinBGLSZW05,
		author = {Yaniv Bernstein and Bodo Billerbeck and Steven Garcia and Nicholas Lester and Falk Scholer and Justin Zobel and William Webber},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2005: Terabyte and Robust Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/rmit-falk.tera.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BernsteinBGLSZW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Looking at Limits and Tradeoffs: Sabir Research at TREC 2005

_Chris Buckley_

- :fontawesome-solid-user-group: **Participant:** [sabir.buckley](./robust/participants.md#sabir.buckley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf)
- :material-file-search: **Runs:** [sab05rot2](./robust/runs.md#sab05rot2) | [sab05rod1](./robust/runs.md#sab05rod1) | [sab05rod2](./robust/runs.md#sab05rod2) | [sab05roa2](./robust/runs.md#sab05roa2) | [sab05ror1](./robust/runs.md#sab05ror1)

??? abstract "Abstract"
	
	Sabir Research participated in TREC-2005 in the Terabyte, Robust, and document retrieval part of the Question Answering tracks. This writeup focuses on the Robust track, and in particular on a “routing” run that took advantage of relevance judgements for the topics on the old trec V45 collection to construct queries for the new Aquaint collection. The s ¯mart retro tool is described which given a query and the set of relevant documents, constructs an optimally weighted version of the query. s ¯mart retro is also used to examine the differences in difficulty between the V45 and Aquaint collections (the Aquaint collection is considerably easier). The final part of the paper describes the compression algorithms and tradeoffs that were used in both TREC 2004 and 2005. These were presented in the TREC 2004 speaker session, but never formally written up. The hardware used for all runs was a single commodity PC with a total cost of $1600: $540 for a Dell PC, $520 for four 250 GByte disks, and $500 to bring the memory up to 2.5 GBytes. The information retrieval software used was the research version of SMART 15.0. SMART was originally developed in the early 1960's by Gerard Salton and since then has continued to be a leading research information retrieval tool. It continues to use a statistical vector space model, with stemming, stop words, weighting, inner product similarity function, and ranked retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Buckley05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Buckley05,
		author = {Chris Buckley},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Looking at Limits and Tradeoffs: Sabir Research at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Buckley05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CAS-ICT at TREC 2005 Robust Track: Using Query Expansion and RankFusion  to Improve Effectiveness and Robustness of Ad Hoc Information Retrieval

_Guodong Ding, Bin Wang, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [cas-ict.wang](./robust/participants.md#cas-ict.wang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-bin.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-bin.robust.pdf)
- :material-file-search: **Runs:** [ICT05qerfTg](./robust/runs.md#ict05qerftg) | [ICT05qerfT](./robust/runs.md#ict05qerft) | [ICT05qerfD](./robust/runs.md#ict05qerfd) | [ICT05qerfDg](./robust/runs.md#ict05qerfdg)

??? abstract "Abstract"
	
	Our participation in this year's robust track aims to: (1) test how to improve the effectiveness of IR (according to MAP) using different retrieval methods with different local analysis-based query expansion methods; (2) test how to improve the retrieval robustness (according to gMAP) using RankFusion, a novel fusion technique proposed in our experiments. Our results show that although query expansion can improve the effectiveness of IR significantly, it hurts the robustness of IR seriously. However, with appropriate parameters setting, using RankFusion for merging multiple retrieval results can improve the robustness significantly while not harming the average precision too much or even increasing it in some cases.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DingWB05.bib) "
	```
	@inproceedings{DBLP:conf/trec/DingWB05,
		author = {Guodong Ding and Bin Wang and Shuo Bai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CAS-ICT} at {TREC} 2005 Robust Track: Using Query Expansion and RankFusion to Improve Effectiveness and Robustness of Ad Hoc Information Retrieval},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-bin.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DingWB05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Axiomatic Approach to IR–UIUC TREC 2005 Robust Track Experiments

_Hui Fang, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uiuc.zhai](./robust/participants.md#uiuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.robust.pdf)
- :material-file-search: **Runs:** [UIUCrAXd0](./robust/runs.md#uiucraxd0) | [UIUCrAXt1](./robust/runs.md#uiucraxt1) | [UIUCrAXt0](./robust/runs.md#uiucraxt0) | [UIUCrAXt2](./robust/runs.md#uiucraxt2) | [UIUCrAXt3](./robust/runs.md#uiucraxt3)

??? abstract "Abstract"
	
	In this paper, we report our experiments in the TREC 2005 Robust Track. Our focus is to explore the use of a new axiomatic approach to information retrieval. Most existing retrieval models make the assumption that terms are independent of each other. Although such simplifying assumption has facilitated the construction of successful retrieval systems, the assumption is not true; words are related by use, and their similarity of occurrence in documents can reflect underlying semantic relations between terms. Our new method aims at incorporating term dependency relations into the axiomatic retrieval model in a natural way. In this paper, we describe the method and present analysis of our Robust-2005 evaluation results. The results show that the proposed method works equally well as the KL-divergence retrieval model with a mixture model feedback method. The performance can be further improved by using the external resources such as Google.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FangZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/FangZ05,
		author = {Hui Fang and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {An Axiomatic Approach to {IR--UIUC} {TREC} 2005 Robust Track Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FangZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Meiji University HARD and Robust Track Experiments

_Kazuya Kudo, Kenji Imai, Makoto Hashimoto, Tomohiro Takagi_

- :fontawesome-solid-user-group: **Participant:** [meijiu.kakuta](./robust/participants.md#meijiu.kakuta)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf)
- :material-file-search: **Runs:** [MEIJIr2](./robust/runs.md#meijir2)

??? abstract "Abstract"
	
	We participated in HARD Track and Robust Track at TREC2005. Our main challenge is to deal with expansion of a word by recognition of context. In HARD Track, we handled semantic expansion of a word. In Robust Track, we tried a challenge to new approach of “Document expansion” by context recognition. In this paper, the next section presents HARD Track. Section 3 describes Robust Track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KudoIHT05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KudoIHT05,
		author = {Kazuya Kudo and Kenji Imai and Makoto Hashimoto and Tomohiro Takagi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Meiji University {HARD} and Robust Track Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KudoIHT05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Robust Track Experiments Using PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, Norbert Dinstl, Peter Deng_

- :fontawesome-solid-user-group: **Participant:** [queenscollege.kwok](./robust/participants.md#queenscollege.kwok)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/queensc-kwok.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/queensc-kwok.robust.pdf)
- :material-file-search: **Runs:** [pircRB05t3](./robust/runs.md#pircrb05t3) | [pircRB05d1](./robust/runs.md#pircrb05d1) | [pircRB05d3](./robust/runs.md#pircrb05d3) | [pircRB05td3](./robust/runs.md#pircrb05td3) | [pircRB05t2](./robust/runs.md#pircrb05t2)

??? abstract "Abstract"
	
	The two tasks in the TREC2005 Robust track were as follows: given a set of topics, A) predict their ranking according to average precision; and B) improve the effectiveness of their ad hoc retrieval, in particular the weakest topics and if possible with the help of what has been found in task A. The difference from last year is that the test collection (ACQUAINT) is different from the training collection (from TREC2004). The evaluation measures for these tasks have also changed from TREC2004. For task A, it is the difference in area (diff-area) between the observed and the predicted MAP plots when the worst performing topic is successively removed from the set. For task B, it is the GMAP, which is roughly the geometric mean of the average precision of all topics (Voorhees 2005). We do not believe our techniques for predicting topic average precision is sufficiently accurate to be applied to task B, and treat the two tasks independently. For task A, two methods of predicting topic behavior were tried: i) predicting the weakest and strongest n topics by SVM regression; and ii) ranking topics by retrieved document similarity. For task B, we followed the strategy introduced by us before to improve ad-hoc retrieval via the web as an external thesaurus to supplement a given topic's representation, followed with data fusion. A new method of salient term selection from longer description queries based on SVM classification was employed to define web probes for these queries. Five runs were submitted: two for title (pircRB05t2 and -t3), two for description queries (pircRB05d1 and -d3), and one for the combination of the two (pircRB05td3). Section 2 describes our experiments for topic prediction; section 3 describes our weak query effectiveness improvements; and section 4 has our conclusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGDD05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGDD05,
		author = {Kui{-}Lam Kwok and Laszlo Grunfeld and Norbert Dinstl and Peter Deng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Robust Track Experiments Using {PIRCS}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/queensc-kwok.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGDD05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 2005: Robust Track

_Shuang Liu, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [uillinois-chicago.liu](./robust/participants.md#uillinois-chicago.liu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.robust.pdf)
- :material-file-search: **Runs:** [uic0501](./robust/runs.md#uic0501)

??? abstract "Abstract"
	
	This paper presents a new approach to improve retrieval effectiveness by using concepts, examples, and word sense disambiguation. We also employ pseudo-feedback and web-assisted feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuY05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuY05,
		author = {Shuang Liu and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 2005: Robust Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuY05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2005: QA Retrieval and Robust Tracks

_James Mayfield, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [jhu.mayfield](./robust/participants.md#jhu.mayfield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf)
- :material-file-search: **Runs:** [apl05pd](./robust/runs.md#apl05pd) | [apl05cmb](./robust/runs.md#apl05cmb) | [apl05prf](./robust/runs.md#apl05prf) | [apl05pt](./robust/runs.md#apl05pt) | [apl05p50](./robust/runs.md#apl05p50)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) focused on the Robust and Question Answering Information Retrieval (QAIR) Tracks at the 2005 TREC conference. For the Robust Track, we attempted to use the difference in retrieval scores between the top retrieved and the 100th document to predict performance; the result was not competitive. For QAIR, we augmented each query with terms that appeared frequently in documents that contained answers to questions from previous question sets; the results showed modest gains from the technique.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MayfieldM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MayfieldM05,
		author = {James Mayfield and Paul McNamee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{JHU/APL} at {TREC} 2005: {QA} Retrieval and Robust Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MayfieldM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Building on Redundancy: Factoid Question Answering, Robust Retrieval  and the "Other"

_Dmitri Roussinov, Elena Filatova, Michael Chau, Jose Antonio Robles-Flores_

- :fontawesome-solid-user-group: **Participant:** [arizonau.roussinov](./robust/participants.md#arizonau.roussinov)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf)
- :material-file-search: **Runs:** [ASUDIV](./robust/runs.md#asudiv) | [ASUBE](./robust/runs.md#asube) | [ASUDE](./robust/runs.md#asude) | [ASUTI](./robust/runs.md#asuti) | [ASUBE3](./robust/runs.md#asube3)

??? abstract "Abstract"
	
	We have explored how redundancy based techniques can be used in improving factoid question answering, definitional questions (“other”), and robust retrieval. For the factoids, we explored the meta approach: we submit the questions to the several open domain question answering systems available on the Web and applied our redundancy-based triangulation algorithm to analyze their outputs in order to identify the most promising answers. Our results support the added value of the meta approach: the performance of the combined system surpassed the underlying performances of its components. To answer definitional (“other”) questions, we were looking for the sentences containing re-occurring pairs of noun entities containing the elements of the target. For robust retrieval, we applied our redundancy based Internet mining technique to identify the concepts (single word terms or phrases) that were highly related to the topic (query) and expanded the queries with them. All our results are above the mean performance in the categories in which we have participated, with one of our robust runs being the best in its category among all 24 participants. Overall, our findings support the hypothesis that using as much as possible textual data, specifically such as mined from the World Wide Web, is extre mely promising.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoussinovFCR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoussinovFCR05,
		author = {Dmitri Roussinov and Elena Filatova and Michael Chau and Jose Antonio Robles{-}Flores},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Building on Redundancy: Factoid Question Answering, Robust Retrieval and the "Other"},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoussinovFCR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Enterprise, QA, Robust and Terabyte Experiments with Hummingbird SearchServer  at TREC 2005

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./robust/participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf)
- :material-file-search: **Runs:** [humR05tl](./robust/runs.md#humr05tl) | [humR05txl](./robust/runs.md#humr05txl) | [humR05txle](./robust/runs.md#humr05txle) | [humR05dl](./robust/runs.md#humr05dl) | [humR05dle](./robust/runs.md#humr05dle)

??? abstract "Abstract"
	
	Hummingbird participated in 6 tasks of TREC 2005: the email known-item search task of the Enterprise Track, the document ranking task of the Question Answering Track, the ad hoc topic relevance task of the Robust Retrieval Track, and the adhoc, efficiency and named page finding tasks of the Terabyte Track. In the email known-item task, SearchServer found the desired message in the first 10 rows for more than 80% of the 125 queries. In the document ranking task, SearchServer returned an answering document in the first 10 rows for more than 90% of the 50 questions. In the robustness task, SearchServer found a relevant document in the first 10 rows for 88% of the 50 short (title) topics. In the terabyte adhoc and efficiency tasks, SearchServer found a relevant document in the first 10 rows for more than 90% of the 50 title topics. A new retrieval measure, First Relevant Score, is investigated; it is found to more accurately reflect known-item differences than reciprocal rank and to better reflect robustness across topics than the primary measure of the Robust track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson05,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Enterprise, QA, Robust and Terabyte Experiments with Hummingbird SearchServer at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MATRIX at the TREC 2005 Robust Track

_W. S. Wong, Ho Chung Wu, Robert Wing Pong Luk, Hong Va Leong, Kam-Fai Wong, Kui-Lam Kwok_

- :fontawesome-solid-user-group: **Participant:** [hkpu.luk](./robust/participants.md#hkpu.luk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/hkpu.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/hkpu.robust.pdf)
- :material-file-search: **Runs:** [HKPU2CT](./robust/runs.md#hkpu2ct) | [HKPU2CTDN](./robust/runs.md#hkpu2ctdn) | [HKPUVCTDN](./robust/runs.md#hkpuvctdn) | [HKPUCD](./robust/runs.md#hkpucd) | [HKPUVCT](./robust/runs.md#hkpuvct)

??? abstract "Abstract"
	
	In the TREC 2005 robust retrieval track, we tested our adaptive retrieval model that automatically switches between the 2-Poisson model/adaptive vector space model and our initial predictive probabilistic context-based model depending on some query characteristics. Our 2-Poisson model uses the BM11 term weighting scheme with passage retrieval and pseudo-relevance feedback. The context-based model incorporates the term locations in a document for calculating the term weights. By doing this, different term weights are assigned to the same query term depending on its context and location in the document. We also use WordNet in the term selection process when doing pseudo-relevance feedback. The performance of our model is comparable to the median among all participants in the robust track on the whole query set including the title, descriptive and long queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WongWLLWK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WongWLLWK05,
		author = {W. S. Wong and Ho Chung Wu and Robert Wing Pong Luk and Hong Va Leong and Kam{-}Fai Wong and Kui{-}Lam Kwok},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{MATRIX} at the {TREC} 2005 Robust Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/hkpu.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WongWLLWK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Queensland University of Technology at TREC 2005

_Alan Woodley, Chengye Lu, Tony Sahama, John King, Shlomo Geva_

- :fontawesome-solid-user-group: **Participant:** [queenslandu.geva](./robust/participants.md#queenslandu.geva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/queenslandu.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/queenslandu.tera.robust.pdf)
- :material-file-search: **Runs:** [pstitle01](./robust/runs.md#pstitle01) | [pstopic01](./robust/runs.md#pstopic01) | [topic01](./robust/runs.md#topic01) | [title01](./robust/runs.md#title01)

??? abstract "Abstract"
	
	The Information Retrieval and Web Intelligence (IR-WI) research group is a research team at the Faculty of Information Technology, QUT, Brisbane, Australia. The IR-WI group participated in the Terabyte and Robust track at TREC 2005, both for the first time. For the Robust track we applied our existing information retrieval system that was originally designed for use with structured (XML) retrieval to the domain of document retrieval. For the Terabyte track we experimented with an open source IR system, Zettair and performed two types of experiments. First, we compared Zettair's performance on both a high-powered supercomputer and a distributed system across seven midrange personal computers. Second, we compared Zettair's performance when a standard TREC title is used, compared with a natural language query, and a query expanded with synonyms. We compare the systems both in terms of efficiency and retrieval performance. Our results indicate that the distributed system is faster than the supercomputer, while slightly decreasing retrieval performance, and that natural language queries also slightly decrease retrieval performance, while our query expansion technique significantly decreased performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WoodleyLSKG05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WoodleyLSKG05,
		author = {Alan Woodley and Chengye Lu and Tony Sahama and John King and Shlomo Geva},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Queensland University of Technology at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/queenslandu.tera.robust.pdf},
		timestamp = {Wed, 14 Jun 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WoodleyLSKG05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2005 HARD, Robust, and SPAM Tracks

_Kiduk Yang, Ning Yu, Nicholas George, Aaron Loehrlein, David McCaulay, Hui Zhang, Shahrier Akram, Jue Mei, Ivan Record_

- :fontawesome-solid-user-group: **Participant:** [indianau.yang](./robust/participants.md#indianau.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf)
- :material-file-search: **Runs:** [wdf1tbqf](./robust/runs.md#wdf1tbqf) | [wdf1t10q](./robust/runs.md#wdf1t10q) | [wdf1t3qs0](./robust/runs.md#wdf1t3qs0) | [wdf1t3qd](./robust/runs.md#wdf1t3qd) | [wdf1s1wp1sm](./robust/runs.md#wdf1s1wp1sm)

??? abstract "Abstract"
	
	Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science participated in the HARD, Robust, and SPAM tracks in TREC-2005. The basic approach of WIDIT is to combine multiple methods as well as to leverage multiple sources of evidence. Our main strategies for the tracks were: query expansion and fusion optimization for the HARD and Robust tracks; and combination of probabilistic, rule-based, pattern-based, and blacklist email filters for the SPAM track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYGLMZAMR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYGLMZAMR05,
		author = {Kiduk Yang and Ning Yu and Nicholas George and Aaron Loehrlein and David McCaulay and Hui Zhang and Shahrier Akram and Jue Mei and Ivan Record},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2005 HARD, Robust, and {SPAM} Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf},
		timestamp = {Wed, 29 Jun 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangYGLMZAMR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Juru at TREC 2005: Query Prediction in the Terabyte and the Robust  Tracks

_Elad Yom-Tov, David Carmel, Adam Darlow, Dan Pelleg, Shai Errera-Yaakov, Shai Fine_

- :fontawesome-solid-user-group: **Participant:** [ibm-haifa.carmel](./robust/participants.md#ibm-haifa.carmel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm-haifa.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm-haifa.tera.robust.pdf)
- :material-file-search: **Runs:** [juruManTit](./robust/runs.md#jurumantit) | [JuruTDWE](./robust/runs.md#jurutdwe) | [JuruDWE](./robust/runs.md#jurudwe) | [JuruTiWE](./robust/runs.md#jurutiwe)

??? abstract "Abstract"
	
	Our experiments focus this year on the ad-hock tasks of the Terabyte and the Robust tracks. In both tracks we experimented with the query prediction technology we developed recently. In the Terabyte track, we investigated how query prediction can be used to improve federation of search results extracted from several indices. We show that federated search based on query prediction can achieve comparable results to single-index search. In the Robust track we trained a predictor over one collection (TREC-8) for predicting query difficulty over another collection (AQUAINT). The experimental results show that difficult topics on the TREC-8 collection were not found to be consistently difficult on the AQUAINT collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yom-TovCDPEF05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yom-TovCDPEF05,
		author = {Elad Yom{-}Tov and David Carmel and Adam Darlow and Dan Pelleg and Shai Errera{-}Yaakov and Shai Fine},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Juru at {TREC} 2005: Query Prediction in the Terabyte and the Robust Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ibm-haifa.tera.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yom-TovCDPEF05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

