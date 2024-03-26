# Proceedings - Spam 2007 

#### TREC 2007 Spam Track Overview

_Gordon V. Cormack_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/SPAM.OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/SPAM.OVERVIEW16.pdf)
??? abstract "Abstract"
	
	TREC's Spam Track uses a standard testing framework that presents a set of chronologically ordered email messages a spam filter for classification. In the filtering task, the messages are presented one at at time to the filter, which yields a binary judgment (spam or ham [i.e. non-spam]) which is compared to a human-adjudicated gold standard. The filter also yields a spamminess score, intended to reflect the likelihood that the classified message is spam, which is the subject of post-hoc ROC (Receiver Operating Characteristic) analysis. Four different forms of user feedback are modeled: with immediate feedback the gold standard for each message is communicated to the filter immediately following classification; with delayed feedback the gold standard is communicated to the filter sometime later (or potentially never), so as to model a user reading email from time to time and perhaps not diligently reporting the filter's errors; with partial feedback the gold standard for only a subset of email recipients is transmitted to the filter, so as to model the case of some users never reporting filter errors; with active on-line learning (suggested by D. Sculley from Tufts University [11]) the filter is allowed to request immediate feedback for a certain quota of messages which is considerably smaller than the total number. Two test corpora - email messages plus gold standard judgments - were used to evaluate subject filters. One public corpus (trec07p) was distributed to participants, who ran their filters on the corpora using a track-supplied toolkit implementing the framework and the four kinds of feedback. One private corpus (MrX 3) was not distributed to participants; rather, participants submitted filter implementations that were run, using the toolkit, on the private data. Twelve groups participated in the track, each submitting up to four filters for evaluation in each of the four feedback modes (immediate; delayed; partial; active). Task guidelines and tools may be found on the web at http://plg.uwaterloo.ca/~gvcormac/spam/.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Cormack07.bib) "
	```
	@inproceedings{DBLP:conf/trec/Cormack07,
		author = {Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 Spam Track Overview},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/SPAM.OVERVIEW16.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Cormack07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo Participation in the TREC 2007 Spam Track

_Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.clarke](./participants.md#uwaterloo.clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uwaterloo.spam.pdf](http://trec.nist.gov/pubs/trec16/papers/uwaterloo.spam.pdf)
- :material-file-search: **Runs:** [wat1](./runs.md#wat1) | [wat2](./runs.md#wat2) | [wat3](./runs.md#wat3) | [wat4](./runs.md#wat4) | [wat3p1000](./runs.md#wat3p1000) | [wat4p1000](./runs.md#wat4p1000) | [wat1p1000](./runs.md#wat1p1000) | [wat2p1000](./runs.md#wat2p1000) | [wat3pd](./runs.md#wat3pd) | [wat4pd](./runs.md#wat4pd) | [wat1pd](./runs.md#wat1pd) | [wat2pd](./runs.md#wat2pd) | [wat3pf](./runs.md#wat3pf) | [wat4pf](./runs.md#wat4pf) | [wat1pf](./runs.md#wat1pf) | [wat2pf](./runs.md#wat2pf) | [wat2pp](./runs.md#wat2pp) | [wat3pp](./runs.md#wat3pp) | [wat4pp](./runs.md#wat4pp) | [wat1pp](./runs.md#wat1pp)

??? abstract "Abstract"
	
	This is the first year that we have submitted participant runs to TREC (Cormack is track coordinator). In parallel with running the track, we have investigated two new filtering methods, inspired by the excellent results that others have shown in the task. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Cormack07a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Cormack07a,
		author = {Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Waterloo Participation in the {TREC} 2007 Spam Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uwaterloo.spam.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Cormack07a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Three Non-Bayesian Methods of Spam Filtration: CRM114 at TREC  2007

_Mamoru Kato, Joseph Langeway, Yimin Wu, William S. Yerazunis_

- :fontawesome-solid-user-group: **Participant:** [mitsubhishi.yerazunis](./participants.md#mitsubhishi.yerazunis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/crm114.spam.final.pdf](http://trec.nist.gov/pubs/trec16/papers/crm114.spam.final.pdf)
- :material-file-search: **Runs:** [crm4p1000](./runs.md#crm4p1000) | [crm1p1000](./runs.md#crm1p1000) | [crm2p1000](./runs.md#crm2p1000) | [crm1pd](./runs.md#crm1pd) | [crm2pd](./runs.md#crm2pd) | [crm3pd](./runs.md#crm3pd) | [crm4pd](./runs.md#crm4pd) | [crm1pf](./runs.md#crm1pf) | [crm2pf](./runs.md#crm2pf) | [crm3pf](./runs.md#crm3pf) | [crm4pf](./runs.md#crm4pf) | [crm4pp](./runs.md#crm4pp) | [crm1pp](./runs.md#crm1pp) | [crm2pp](./runs.md#crm2pp) | [crm3pp](./runs.md#crm3pp)

??? abstract "Abstract"
	
	For the TREC 2007 conference, the CRM114 team considered three non Bayesian methods of spam filtration in the CRM114 framework - an SVM based on the “hyperspace” feature==document paradigm, a bit entropy matcher, and substring compression based on LZ77. As a calibration yardstick, we used the well tested and widely used CRM114 OSB markov random field system (basically unchanged since 2003). The results show that the SVM has a spam filtering accuracy of about a factor of two to three better accuracy than the OSB system, that substring compression is somewhat more accurate than OSB, and that bit entropy is somewhat less accurate for the TREC 2007 test sets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KatoLWY07.bib) "
	```
	@inproceedings{DBLP:conf/trec/KatoLWY07,
		author = {Mamoru Kato and Joseph Langeway and Yimin Wu and William S. Yerazunis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Three Non-Bayesian Methods of Spam Filtration: {CRM114} at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/crm114.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KatoLWY07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Relaxed Online SVMs in the TREC Spam Filtering Track

_David Sculley, Gabriel Wachman_

- :fontawesome-solid-user-group: **Participant:** [tufts.sculley](./participants.md#tufts.sculley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/tuftsu.spam.final.pdf](http://trec.nist.gov/pubs/trec16/papers/tuftsu.spam.final.pdf)
- :material-file-search: **Runs:** [tftS1F](./runs.md#tfts1f) | [tftS2F](./runs.md#tfts2f) | [tftS3F](./runs.md#tfts3f) | [tftS4F](./runs.md#tfts4f) | [tftS2Fp1000](./runs.md#tfts2fp1000) | [tftS1Fp1000](./runs.md#tfts1fp1000) | [tftS3Fp1000](./runs.md#tfts3fp1000) | [tftS1Fpd](./runs.md#tfts1fpd) | [tftS2Fpd](./runs.md#tfts2fpd) | [tftS3Fpd](./runs.md#tfts3fpd) | [tftS1Fpf](./runs.md#tfts1fpf) | [tftS2Fpf](./runs.md#tfts2fpf) | [tftS3Fpf](./runs.md#tfts3fpf) | [tftS1Fpp](./runs.md#tfts1fpp) | [tftS2Fpp](./runs.md#tfts2fpp) | [tftS3Fpp](./runs.md#tfts3fpp)

??? abstract "Abstract"
	
	Relaxed Online Support Vector Machines (ROSVMs) have recently been proposed as an efficient methodology for attaining an approximate SVM solution for streaming data such as the online spam filtering task. Here, we apply ROSVMs in the TREC 2007 Spam filtering track and report results. In particular, we explore the effect of various sliding-window sizes, trading off computation cost against classification performance with good results. We also test a variant of fixed-uncertainty sampling for Online Active Learning. The best results with this approach give classification performance near to that of the fully supervised approach while requiring only a small fraction of the examples to be labeled.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SculleyW07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SculleyW07,
		author = {David Sculley and Gabriel Wachman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Relaxed Online SVMs in the {TREC} Spam Filtering Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/tuftsu.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SculleyW07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIM at TREC 2007

_Jun Xu, Jing Yao, Jiaqian Zheng, Qi Sun, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [fudanu.niu](./participants.md#fudanu.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fudan-niu.spam.ent.legal.geo.final.pdf)
- :material-file-search: **Runs:** [fdw1](./runs.md#fdw1) | [fdw2](./runs.md#fdw2) | [fdw3](./runs.md#fdw3) | [fdw4](./runs.md#fdw4) | [fdw4pf](./runs.md#fdw4pf) | [fdw4pd](./runs.md#fdw4pd) | [fdw4pp](./runs.md#fdw4pp) | [fdw4p1000](./runs.md#fdw4p1000) | [fdw3pf](./runs.md#fdw3pf) | [fdw3pd](./runs.md#fdw3pd) | [fdw3pp](./runs.md#fdw3pp) | [fdw3p1000](./runs.md#fdw3p1000) | [fdw2pf](./runs.md#fdw2pf) | [fdw2pd](./runs.md#fdw2pd) | [fdw2pp](./runs.md#fdw2pp) | [fdw2p1000](./runs.md#fdw2p1000) | [fdw1pf](./runs.md#fdw1pf) | [fdw1pd](./runs.md#fdw1pd) | [fdw1pp](./runs.md#fdw1pp) | [fdw1p1000](./runs.md#fdw1p1000)

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

