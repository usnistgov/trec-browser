# Proceedings - Spam 2005 

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

- :fontawesome-solid-user-group: **Participant:** [merl.yerazunis](./participants.md#merl.yerazunis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/crm.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/crm.spam.pdf)
- :material-file-search: **Runs:** [crmSPAMp2wi](./runs.md#crmspamp2wi) | [crmSPAMp1of](./runs.md#crmspamp1of) | [crmSPAM2win](./runs.md#crmspam2win) | [crmSPAM4osb](./runs.md#crmspam4osb) | [crmSPAM1osf](./runs.md#crmspam1osf) | [crmSPAM3osu](./runs.md#crmspam3osu) | [crmSPAM2full](./runs.md#crmspam2full) | [crmSPAM2ham2](./runs.md#crmspam2ham2) | [crmSPAM2ham5](./runs.md#crmspam2ham5) | [crmSPAM2spm2](./runs.md#crmspam2spm2) | [crmSPAM2spm5](./runs.md#crmspam2spm5) | [crmSPAM4full](./runs.md#crmspam4full) | [crmSPAM3full](./runs.md#crmspam3full) | [crmSPAM1full](./runs.md#crmspam1full) | [crmSPAM1ham2](./runs.md#crmspam1ham2) | [crmSPAM1ham5](./runs.md#crmspam1ham5) | [crmSPAM1spm5](./runs.md#crmspam1spm5) | [crmSPAM1spm2](./runs.md#crmspam1spm2) | [crmSPAM3ham2](./runs.md#crmspam3ham2) | [crmSPAM3ham5](./runs.md#crmspam3ham5) | [crmSPAM3spm2](./runs.md#crmspam3spm2) | [crmSPAM3spm5](./runs.md#crmspam3spm5) | [crmSPAM4ham2](./runs.md#crmspam4ham2) | [crmSPAM4ham5](./runs.md#crmspam4ham5) | [crmSPAM4spm2](./runs.md#crmspam4spm2) | [crmSPAM4spm5](./runs.md#crmspam4spm5)

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

- :fontawesome-solid-user-group: **Participant:** [breyer.laird](./participants.md#breyer.laird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/breyer.laird-spam.ps](http://trec.nist.gov/pubs/trec14/papers/breyer.laird-spam.ps)
- :material-file-search: **Runs:** [p1cefhuj](./runs.md#p1cefhuj) | [p2adphu](./runs.md#p2adphu) | [p3adphd](./runs.md#p3adphd) | [p4adp](./runs.md#p4adp) | [1cefhuj](./runs.md#1cefhuj) | [2adphu](./runs.md#2adphu) | [3adphd](./runs.md#3adphd) | [4adp](./runs.md#4adp) | [pub1full](./runs.md#pub1full) | [pub1ham50](./runs.md#pub1ham50) | [pub1spam50](./runs.md#pub1spam50) | [pub2full](./runs.md#pub2full) | [pub4full](./runs.md#pub4full) | [pub3full](./runs.md#pub3full)

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

- :fontawesome-solid-user-group: **Participant:** [jozef-stefan-inst.bratko](./participants.md#jozef-stefan-inst.bratko)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/jozef-stefan.bratko.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/jozef-stefan.bratko.spam.pdf)
- :material-file-search: **Runs:** [ijsSPAM1pm1](./runs.md#ijsspam1pm1) | [ijsSPAM2cw1](./runs.md#ijsspam2cw1) | [ijsSPAM3pm2](./runs.md#ijsspam3pm2) | [ijsSPAM3cw2](./runs.md#ijsspam3cw2) | [ijsSPAM4cw2](./runs.md#ijsspam4cw2) | [ijsSPAM1pm8](./runs.md#ijsspam1pm8) | [ijsSPAM2pm6](./runs.md#ijsspam2pm6) | [ijsSPAM3pm4](./runs.md#ijsspam3pm4) | [ijsSPAM4cw8](./runs.md#ijsspam4cw8) | [ijsSPAM1full](./runs.md#ijsspam1full) | [ijsSPAM2full](./runs.md#ijsspam2full) | [ijsSPAM3full](./runs.md#ijsspam3full) | [ijsSPAM4full](./runs.md#ijsspam4full) | [ijsSPAM1h25](./runs.md#ijsspam1h25) | [ijsSPAM2h25](./runs.md#ijsspam2h25) | [ijsSPAM3h25](./runs.md#ijsspam3h25) | [ijsSPAM4h25](./runs.md#ijsspam4h25)

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

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/yorku-huang.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/yorku-huang.spam.pdf)
- :material-file-search: **Runs:** [yorSPAMpknn](./runs.md#yorspampknn) | [yorSPAM1knf](./runs.md#yorspam1knf) | [cao1knf](./runs.md#cao1knf) | [yorSPAM3knf](./runs.md#yorspam3knf) | [cao3knf](./runs.md#cao3knf) | [yorSPAM2ruk](./runs.md#yorspam2ruk) | [cao2ruk](./runs.md#cao2ruk) | [yorSPAM4hyb](./runs.md#yorspam4hyb) | [cao4hyb](./runs.md#cao4hyb) | [yorSPAM1full](./runs.md#yorspam1full) | [yorSPAM1ham2](./runs.md#yorspam1ham2) | [yorSPAM1ham5](./runs.md#yorspam1ham5) | [yorSPAM1spa2](./runs.md#yorspam1spa2) | [yorSPAM1spa5](./runs.md#yorspam1spa5) | [yorSPAM2full](./runs.md#yorspam2full) | [yorSPAM2ham2](./runs.md#yorspam2ham2) | [yorSPAM2ham5](./runs.md#yorspam2ham5) | [yorSPAM2spa2](./runs.md#yorspam2spa2) | [yorSPAM2spa5](./runs.md#yorspam2spa5) | [yorSPAM3full](./runs.md#yorspam3full) | [yorSPAM3ham2](./runs.md#yorspam3ham2) | [yorSPAM3ham5](./runs.md#yorspam3ham5) | [yorSPAM3spa2](./runs.md#yorspam3spa2) | [yorSPAM3spa5](./runs.md#yorspam3spa5) | [yorSPAM4full](./runs.md#yorspam4full) | [yorSPAM4ham2](./runs.md#yorspam4ham2) | [yorSPAM4ham5](./runs.md#yorspam4ham5) | [yorSPAM4spa2](./runs.md#yorspam4spa2) | [yorSPAM4spa5](./runs.md#yorspam4spa5)

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

- :fontawesome-solid-user-group: **Participant:** [dalhousieu.keselj](./participants.md#dalhousieu.keselj)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dalhousieu.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/dalhousieu.spam.pdf)
- :material-file-search: **Runs:** [dalSPAM2vla](./runs.md#dalspam2vla) | [dalSPAM3vla](./runs.md#dalspam3vla) | [dalSPAM4sxw](./runs.md#dalspam4sxw) | [dalSPAM1sxw](./runs.md#dalspam1sxw) | [dalSPAM1fsw](./runs.md#dalspam1fsw) | [dalSPAM4fsw](./runs.md#dalspam4fsw) | [DalSPAM2n4](./runs.md#dalspam2n4) | [DalSPAM3n5](./runs.md#dalspam3n5) | [dalSPAM2h25](./runs.md#dalspam2h25) | [dalSPAM2f](./runs.md#dalspam2f) | [dalSPAM2h50](./runs.md#dalspam2h50) | [dalSPAM2s25](./runs.md#dalspam2s25) | [dalSPAM2s50](./runs.md#dalspam2s50) | [dalSPAM3f](./runs.md#dalspam3f) | [dalSPAM1sw1](./runs.md#dalspam1sw1) | [dalSPAM4sw1](./runs.md#dalspam4sw1) | [dalSPAM3h25](./runs.md#dalspam3h25) | [dalSPAM3s50](./runs.md#dalspam3s50) | [dalSPAM3s25](./runs.md#dalspam3s25) | [dalSPAM3h50](./runs.md#dalspam3h50) | [dalSPAM1sx2](./runs.md#dalspam1sx2) | [dalSPAM4sx2](./runs.md#dalspam4sx2)

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

- :fontawesome-solid-user-group: **Participant:** [masseyu.meyer](./participants.md#masseyu.meyer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/masseyu.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/masseyu.spam.pdf)
- :material-file-search: **Runs:** [tamSPAMpplt](./runs.md#tamspampplt) | [tamSPAM1dte](./runs.md#tamspam1dte) | [tamSPAM2ber](./runs.md#tamspam2ber) | [tamSPAM3bex](./runs.md#tamspam3bex) | [tamSPAM4aex](./runs.md#tamspam4aex) | [tamSPAM1h25](./runs.md#tamspam1h25) | [tamSPAM2h25](./runs.md#tamspam2h25) | [tamSPAM1h50](./runs.md#tamspam1h50) | [tamSPAM2h50](./runs.md#tamspam2h50) | [tamSPAM1s25](./runs.md#tamspam1s25) | [tamSPAM2s25](./runs.md#tamspam2s25) | [tamSPAM3s25](./runs.md#tamspam3s25) | [tamSPAM1s50](./runs.md#tamspam1s50) | [tamSPAM2s50](./runs.md#tamspam2s50) | [tamSPAM1full](./runs.md#tamspam1full) | [tamSPAM2full](./runs.md#tamspam2full) | [tamSPAM3full](./runs.md#tamspam3full)

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

- :fontawesome-solid-user-group: **Participant:** [ibm.segal](./participants.md#ibm.segal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm-segal.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm-segal.spam.pdf)
- :material-file-search: **Runs:** [621SPAM1FT1](./runs.md#621spam1ft1) | [621SPAMFT1](./runs.md#621spamft1) | [621SPAM1FIN](./runs.md#621spam1fin) | [621SPAM1FUL](./runs.md#621spam1ful) | [621SPAM2FUL](./runs.md#621spam2ful) | [621SPAM3FUL](./runs.md#621spam3ful) | [621SPAM1S50](./runs.md#621spam1s50) | [621SPAM2S50](./runs.md#621spam2s50) | [621SPAM3S50](./runs.md#621spam3s50) | [621SPAM1S25](./runs.md#621spam1s25) | [621SPAM2S25](./runs.md#621spam2s25) | [621SPAM3S25](./runs.md#621spam3s25) | [621SPAM1H50](./runs.md#621spam1h50) | [621SPAM2H50](./runs.md#621spam2h50) | [621SPAM3H50](./runs.md#621spam3h50) | [621SPAM1H25](./runs.md#621spam1h25) | [621SPAM2H25](./runs.md#621spam2h25) | [621SPAM3H25](./runs.md#621spam3h25)

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

- :fontawesome-solid-user-group: **Participant:** [puc-rs.terra](./participants.md#puc-rs.terra)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/pontificiau.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/pontificiau.spam.pdf)
- :material-file-search: **Runs:** [PUC](./runs.md#puc) | [pucrs2](./runs.md#pucrs2) | [pucrs1](./runs.md#pucrs1) | [pucrs0](./runs.md#pucrs0) | [pucrs0full](./runs.md#pucrs0full) | [pucrs1full](./runs.md#pucrs1full) | [pucrs2full](./runs.md#pucrs2full) | [pucrs0ham25](./runs.md#pucrs0ham25) | [pucrs0ham50](./runs.md#pucrs0ham50) | [pucrs0spam25](./runs.md#pucrs0spam25) | [pucrs0spam50](./runs.md#pucrs0spam50) | [pucrs1ham25](./runs.md#pucrs1ham25) | [pucrs1ham50](./runs.md#pucrs1ham50) | [pucrs1spam25](./runs.md#pucrs1spam25) | [pucrs1spam50](./runs.md#pucrs1spam50) | [pucrs2ham25](./runs.md#pucrs2ham25) | [pucrs2ham50](./runs.md#pucrs2ham50) | [pucrs2spam25](./runs.md#pucrs2spam25) | [pucrs2spam50](./runs.md#pucrs2spam50)

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

- :fontawesome-solid-user-group: **Participant:** [cas-ict.wang](./participants.md#cas-ict.wang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-bin.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-bin.spam.pdf)
- :material-file-search: **Runs:** [ICTSPAMpWNB](./runs.md#ictspampwnb) | [ICTSPAM1WNB](./runs.md#ictspam1wnb) | [ICTSPAM2WNH](./runs.md#ictspam2wnh) | [ICTSPAM3NBH](./runs.md#ictspam3nbh) | [ICTSPAM4NBB](./runs.md#ictspam4nbb)

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

- :fontawesome-solid-user-group: **Participant:** [beijingu.guo](./participants.md#beijingu.guo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/beijingu-of-pt.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/beijingu-of-pt.spam.pdf)
- :material-file-search: **Runs:** [kidSPAMpBAS](./runs.md#kidspampbas) | [kidSPAM1BAS](./runs.md#kidspam1bas) | [kidSPAM2V2B](./runs.md#kidspam2v2b) | [kidSPAM3V2E](./runs.md#kidspam3v2e) | [kidSPAM4V5B](./runs.md#kidspam4v5b) | [1BASresults](./runs.md#1basresults) | [2V2Bresults](./runs.md#2v2bresults) | [3V2Eresults](./runs.md#3v2eresults) | [4V5Bresults](./runs.md#4v5bresults)

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

- :fontawesome-solid-user-group: **Participant:** [indianau.yang](./participants.md#indianau.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf)
- :material-file-search: **Runs:** [indSPAMpwf4](./runs.md#indspampwf4) | [indSPAM1f4f](./runs.md#indspam1f4f) | [indSPAM2f42](./runs.md#indspam2f42) | [indSPAM3f40](./runs.md#indspam3f40) | [indSPAM4pf4](./runs.md#indspam4pf4)

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

