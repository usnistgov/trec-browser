# Proceedings - Spam 2006 

#### TREC 2006 Spam Track Overview

_Gordon V. Cormack_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/SPAM06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/SPAM06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	TREC's Spam Track uses a standard testing framework that presents a set of chronologically ordered email messages a spam filter for classification. In the filtering task, the messages are presented one at at time to the filter, which yields a binary judgement (spam or ham [i.e. non-spam]) which is compared to a human-adjudicated gold standard. The filter also yields a spamminess score, intended to reflect the likelihood that the classified message is spam, which is the subject of post-hoc ROC (Receiver Operating Characteristic) analysis. Two forms of user feedback are modeled: with immediate feedback the gold standard for each message is communicated to the filter immediately following classification; with delayed feedback the gold standard is communicated to the filter sometime later, so as to model a user reading email from time to time in batches. A new task - active learning - presents the filter with a large collection of unadjudicated messages, and has the filter request adjudication for a subset of them before classifying a set of future messages. Four test corpora - email messages plus gold standard judgements - were used to evaluate subject filters. Two of the corpora (the public corpora, one English and one Chinese) were distributed to participants, who ran their filters on the corpora using a track-supplied toolkit implementing the framework. Two of the corpora (the private corpora) were not distributed to participants; rather, participants submitted filter implementations that were run, using the toolkit, on the private data. Nine groups participated in the track, each submitting up to four filters for evaluation in each of the three tasks (filtering with immediate feedback; filtering with delayed feedback; active learning).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Cormack06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Cormack06,
		author = {Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 Spam Track Overview},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/SPAM06.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Cormack06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### OSBF-Lua - A Text Classification Module for Lua: The Importance  of the Training Method

_Fidelis Assis_

- :fontawesome-solid-user-group: **Participant:** [fidelis.assis](./participants.md#fidelis.assis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/fidelis-assis.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/fidelis-assis.spam.final.pdf)
- :material-file-search: **Runs:** [oflS1F](./runs.md#ofls1f) | [oflS2F](./runs.md#ofls2f) | [oflS3F](./runs.md#ofls3f) | [oflS4F](./runs.md#ofls4f) | [oflA1F](./runs.md#ofla1f) | [oflS1pei](./runs.md#ofls1pei) | [oflS1pci](./runs.md#ofls1pci) | [oflS1ped](./runs.md#ofls1ped) | [oflS1pcd](./runs.md#ofls1pcd) | [oflS2pei](./runs.md#ofls2pei) | [oflS2pci](./runs.md#ofls2pci) | [oflS2ped](./runs.md#ofls2ped) | [oflS2pcd](./runs.md#ofls2pcd) | [oflS3pei](./runs.md#ofls3pei) | [oflS3pci](./runs.md#ofls3pci) | [oflS3ped](./runs.md#ofls3ped) | [oflS3pcd](./runs.md#ofls3pcd) | [oflS4pei](./runs.md#ofls4pei) | [oflS4pci](./runs.md#ofls4pci) | [oflS4ped](./runs.md#ofls4ped) | [oflS4pcd](./runs.md#ofls4pcd) | [oflA1pei](./runs.md#ofla1pei) | [oflA1pci](./runs.md#ofla1pci) | [oflA2pei](./runs.md#ofla2pei) | [oflA2pci](./runs.md#ofla2pci) | [oflA3pei](./runs.md#ofla3pei) | [oflA3pci](./runs.md#ofla3pci) | [oflA4pei](./runs.md#ofla4pei) | [oflA4pci](./runs.md#ofla4pci)

??? abstract "Abstract"
	
	OSBFL ua is a C module for the Lua language which implements a Bayesian classifier enhanced with Orthogonal Sparse Bigrams OSB for feature extraction and Exponential Differential Document Count EDDC - for feature selection. These two techniques, combined with the new training method introduced for TREC 2006 produce a highly accurate filter, yet very fast and economic in resources. OSBFL ua is an Open Source Software available from http://osbf-lua.luaforge.net/. spamfilter.lua is a productionc lass antis pam filter available in the same package.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Assis06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Assis06,
		author = {Fidelis Assis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {OSBF-Lua - {A} Text Classification Module for Lua: The Importance of the Training Method},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/fidelis-assis.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Assis06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Towards Practical PPM Spam Filtering: Experiments for the TREC  2006 Spam Track

_Andrej Bratko, Bogdan Filipic, Blaz Zupan_

- :fontawesome-solid-user-group: **Participant:** [jozef-stefan-inst.bratko](./participants.md#jozef-stefan-inst.bratko)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/jozef-stefan.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/jozef-stefan.spam.final.pdf)
- :material-file-search: **Runs:** [ijsS1F](./runs.md#ijss1f) | [ijsA1F](./runs.md#ijsa1f) | [ijsS1pei](./runs.md#ijss1pei) | [ijsS1ped](./runs.md#ijss1ped) | [ijsS1pci](./runs.md#ijss1pci) | [ijsS1pcd](./runs.md#ijss1pcd) | [ijsA1pei](./runs.md#ijsa1pei) | [ijsA1pci](./runs.md#ijsa1pci) | [ijsA2pei](./runs.md#ijsa2pei) | [ijsA2pci](./runs.md#ijsa2pci)

??? abstract "Abstract"
	
	This paper summarizes our participation in the TREC 2006 spam track. We submitted a single filter for the evaluation, based on the Prediction by Partial Matching compression scheme, a method that performed well in the previous TREC evaluation. A major focus of our effort was to improve efficiency of the method, particularly in terms of memory consumption, in order to establish whether compression-based filters are in fact a viable solution for practical applications. Our system exhibited fair performance, despite the fact that the filtering techniques remained virtually unchanged from the previous evaluation. We did not investigate methods for tackling delayed user feedback. A very simple strategy of training on most recent examples was used for the active learning task, and found to work surprisingly well given its simplicity.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BratkoFZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BratkoFZ06,
		author = {Andrej Bratko and Bogdan Filipic and Blaz Zupan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Towards Practical {PPM} Spam Filtering: Experiments for the {TREC} 2006 Spam Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/jozef-stefan.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BratkoFZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Highly Scalable Discriminative Spam Filtering

_Michael Brückner, Peter Haider, Tobias Scheffer_

- :fontawesome-solid-user-group: **Participant:** [humboldtu.haider](./participants.md#humboldtu.haider)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/humboldtu.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/humboldtu.spam.final.pdf)
- :material-file-search: **Runs:** [hubA2F](./runs.md#huba2f) | [hubA1F](./runs.md#huba1f) | [hubA3F](./runs.md#huba3f) | [hubA4F](./runs.md#huba4f) | [hubS1F](./runs.md#hubs1f) | [hubS2F](./runs.md#hubs2f) | [hubS3F](./runs.md#hubs3f) | [hubS4F](./runs.md#hubs4f) | [hubS1pcd](./runs.md#hubs1pcd) | [hubS1pci](./runs.md#hubs1pci) | [hubS1ped](./runs.md#hubs1ped) | [hubS1pei](./runs.md#hubs1pei) | [hubS2pcd](./runs.md#hubs2pcd) | [hubS2pci](./runs.md#hubs2pci) | [hubS2ped](./runs.md#hubs2ped) | [hubS2pei](./runs.md#hubs2pei) | [hubS3pcd](./runs.md#hubs3pcd) | [hubS3pci](./runs.md#hubs3pci) | [hubS3ped](./runs.md#hubs3ped) | [hubS3pei](./runs.md#hubs3pei) | [hubS4pcd](./runs.md#hubs4pcd) | [hubS4pci](./runs.md#hubs4pci) | [hubS4ped](./runs.md#hubs4ped) | [hubS4pei](./runs.md#hubs4pei) | [hubA1pci](./runs.md#huba1pci) | [hubA1pei](./runs.md#huba1pei) | [hubA2pci](./runs.md#huba2pci) | [hubA2pei](./runs.md#huba2pei) | [hubA3pci](./runs.md#huba3pci) | [hubA3pei](./runs.md#huba3pei) | [hubA4pci](./runs.md#huba4pci) | [hubA4pei](./runs.md#huba4pei)

??? abstract "Abstract"
	
	This paper discusses several lessons learned from the SpamTREC 2006 challenge. We discuss issues related to decoding, preprocessing, and tokenization of email messages. Using the Winnow algorithm with orthogonal sparse bigram features, we construct an efficient, highly scalable incremental classifier, trained to maximize a discriminative optimization criterion. The algorithm easily scales to millions of training messages and millions of features. We address the composition of training corpora and discuss experiments that guide the construction of our SpamTREC entry. We describe our submission for the filtering tasks with periodical re-training and active learning strategies, and report on the evaluation on the publicly available corpora.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrucknerHS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrucknerHS06,
		author = {Michael Br{\"{u}}ckner and Peter Haider and Tobias Scheffer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Highly Scalable Discriminative Spam Filtering},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/humboldtu.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BrucknerHS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Spam Filtering Using Inexact String Matching in Explicit Feature Space  with On-Line Linear Classifiers

_David Sculley, Gabriel Wachman, Carla E. Brodley_

- :fontawesome-solid-user-group: **Participant:** [tufts.sculley](./participants.md#tufts.sculley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/tuftsu.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/tuftsu.spam.final.pdf)
- :material-file-search: **Runs:** [tufS1F](./runs.md#tufs1f) | [tufS2F](./runs.md#tufs2f) | [tufS3F](./runs.md#tufs3f) | [tufS4F](./runs.md#tufs4f) | [tufS1pcd](./runs.md#tufs1pcd) | [tufS1pci](./runs.md#tufs1pci) | [tufS1ped](./runs.md#tufs1ped) | [tufS1pei](./runs.md#tufs1pei) | [tufS2pcd](./runs.md#tufs2pcd) | [tufS2pci](./runs.md#tufs2pci) | [tufS2ped](./runs.md#tufs2ped) | [tufS2pei](./runs.md#tufs2pei)

??? abstract "Abstract"
	
	Contemporary spammers commonly seek to defeat statistical spam filters through the use of word obfuscation. Such methods include character level substitutions, repetitions, and insertions to reduce the effectiveness of word-based features. We present an efficient method for combating obfuscation through the use of inexact string matching kernels, which were first developed to measure similarity among mutating genes in computational biology. Our system avoids the high classification costs associated with these kernel methods by working in an explicit feature space, and employs the Perceptron Algorithm using Margins for fast on-line training. No prior domain knowledge was incorporated into this system. We report strong experimental results on the TREC 2006 spam data sets and on other publicly available spam data, including near-perfect performance on the TREC 2006 Chinese spam data set. These results invite further exploration of the use of inexact string matching for spam filtering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SculleyWB06.bib) "
	```
	@inproceedings{DBLP:conf/trec/SculleyWB06,
		author = {David Sculley and Gabriel Wachman and Carla E. Brodley},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Spam Filtering Using Inexact String Matching in Explicit Feature Space with On-Line Linear Classifiers},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/tuftsu.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SculleyWB06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SVM-Based Spam Filter with Active and Online Learning

_Qiang Wang, Yi Guan, Xiaolong Wang_

- :fontawesome-solid-user-group: **Participant:** [harbin.zhao](./participants.md#harbin.zhao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/hit.spam.final.final.pdf](http://trec.nist.gov/pubs/trec15/papers/hit.spam.final.final.pdf)
- :material-file-search: **Runs:** [hitS1F](./runs.md#hits1f) | [hitS2F](./runs.md#hits2f) | [hitS3F](./runs.md#hits3f) | [hitA1F](./runs.md#hita1f) | [hitA2F](./runs.md#hita2f) | [hitA1pci](./runs.md#hita1pci) | [hitA1pei](./runs.md#hita1pei) | [hitA2pci](./runs.md#hita2pci) | [hitA2pei](./runs.md#hita2pei) | [hitS1pcd](./runs.md#hits1pcd) | [hitS1pci](./runs.md#hits1pci) | [hitS1ped](./runs.md#hits1ped) | [hitS1pei](./runs.md#hits1pei) | [hitS2pcd](./runs.md#hits2pcd) | [hitS2pci](./runs.md#hits2pci) | [hitS2ped](./runs.md#hits2ped) | [hitS2pei](./runs.md#hits2pei) | [hitS3pcd](./runs.md#hits3pcd) | [hitS3pci](./runs.md#hits3pci) | [hitS3ped](./runs.md#hits3ped) | [hitS3pei](./runs.md#hits3pei)

??? abstract "Abstract"
	
	A realistic classification model for spam filtering should not only take account of the fact that spam evolves over time, but also that labeling a large number of examples for initial training can be expensive in terms of both time and money. This paper address the problem of separating legitimate emails from unsolicited ones with active and online learning algorithm, using a Support Vector Machines (SVM) as the base classifier. We evaluate its effectiveness using a set of goodness criteria on TREC2006 spam filtering benchmark datasets, and promising results are reported.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangGW06.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangGW06,
		author = {Qiang Wang and Yi Guan and Xiaolong Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {SVM-Based Spam Filter with Active and Online Learning},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/hit.spam.final.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangGW06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT at TREC 2006: Spam Track

_Zhen Yang, Wei Xu, Bo Chen, Weiran Xu, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [beijingu-posts-tele.weiran](./participants.md#beijingu-posts-tele.weiran)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/beijing-upt.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/beijing-upt.spam.final.pdf)
- :material-file-search: **Runs:** [BASA2F](./runs.md#basa2f) | [BASS2F](./runs.md#bass2f) | [KB9A3F](./runs.md#kb9a3f) | [B53S3F](./runs.md#b53s3f) | [WEIA4F](./runs.md#weia4f) | [KB9S4F](./runs.md#kb9s4f) | [KB3S1F](./runs.md#kb3s1f) | [KB3A1F](./runs.md#kb3a1f) | [KB9S4pei](./runs.md#kb9s4pei) | [KB9S4ped](./runs.md#kb9s4ped) | [KB9S4pci](./runs.md#kb9s4pci) | [KB9S4pcd](./runs.md#kb9s4pcd) | [B53S3pei](./runs.md#b53s3pei) | [B53S3ped](./runs.md#b53s3ped) | [B53S3pci](./runs.md#b53s3pci) | [B53S3pcd](./runs.md#b53s3pcd) | [KB3S1pei](./runs.md#kb3s1pei) | [KB3S1ped](./runs.md#kb3s1ped) | [KB3S1pci](./runs.md#kb3s1pci) | [KB3S1pcd](./runs.md#kb3s1pcd) | [BASS2pcd](./runs.md#bass2pcd) | [BASS2pci](./runs.md#bass2pci) | [BASS2ped](./runs.md#bass2ped) | [BASS2pei](./runs.md#bass2pei) | [BASA2pci](./runs.md#basa2pci) | [BASA2pei](./runs.md#basa2pei) | [KB3A1pci](./runs.md#kb3a1pci) | [KB3A1pei](./runs.md#kb3a1pei) | [KB9A3pci](./runs.md#kb9a3pci) | [KB9A3pei](./runs.md#kb9a3pei) | [WEIA4pci](./runs.md#weia4pci) | [WEIA4pei](./runs.md#weia4pei)

??? abstract "Abstract"
	
	This report summarizes our participation in the TREC 2006 spam track, in which we consider the use of Bayesian models for the spam filtering task. Firstly, our anti-spam filter, Kidult, is briefly introduced. And then we try to use weighted adjustment of separating hyperplane and selective classifiers ensemble to improve the filtering performance. Finally, we summarize the relevant results from the official evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangXCXG06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangXCXG06,
		author = {Zhen Yang and Wei Xu and Bo Chen and Weiran Xu and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BUPT} at {TREC} 2006: Spam Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/beijing-upt.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangXCXG06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Seven Hypothesis about Spam Filtering

_William S. Yerazunis_

- :fontawesome-solid-user-group: **Participant:** [mitsubhishi.yerazunis](./participants.md#mitsubhishi.yerazunis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/crm.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/crm.spam.final.pdf)
- :material-file-search: **Runs:** [CRMS1F](./runs.md#crms1f) | [CRMS2F](./runs.md#crms2f) | [CRMS3F](./runs.md#crms3f) | [CRMS4F](./runs.md#crms4f) | [CRMS1Ffull](./runs.md#crms1ffull) | [CRMS2Ffull](./runs.md#crms2ffull) | [CRMS3Ffull](./runs.md#crms3ffull) | [CRMS4Ffull](./runs.md#crms4ffull) | [CRMS4Fdelay](./runs.md#crms4fdelay) | [CRMS3Fdelay](./runs.md#crms3fdelay) | [CRMS2Fdelay](./runs.md#crms2fdelay) | [CRMS1Fdelay](./runs.md#crms1fdelay) | [CRMS1Fchi](./runs.md#crms1fchi) | [CRMS2Fchi](./runs.md#crms2fchi) | [CRMS3Fchi](./runs.md#crms3fchi) | [CRMS4Fchi](./runs.md#crms4fchi) | [CRMS4Fchidly](./runs.md#crms4fchidly) | [CRMS3Fchidly](./runs.md#crms3fchidly) | [CRMS2Fchidly](./runs.md#crms2fchidly) | [CRMS1Fchidly](./runs.md#crms1fchidly)

??? abstract "Abstract"
	
	For TREC 2006, the CRM114 team considered several different hypothesis on the topic of spam filtering. The hypothesis were that: 1 Spammers were changing tactics to successfully evade contentba sed spam filters; 2 A pretrained database of known spam and nonspam improves overall accuracy; 3 Repeated training methods are more effective than singlepa ss Train Only Errors training 4 KNN/Hyperspace classifiers are more effective than classical Bayesian or Markovian classifiers 5 Delaying feedback learning results in degraded filter accuracy 6 Bite ntropy filters are as good or better than tokenizing filters and aftert hefa ct: 7 1R OCA% is the best figure of merit for spam filters Of these hypothesis, we found that spammers were not significantly able to evade content based spam filters, that pretraining is probably not helpful, that repeatedpa ss training is not significantly helpful, that KNNs are of roughly equal accuracy to computationally and storagee quivalent Markov classifiers, that delayed feedback is only marginal in impacting filter accuracy, and that despite their highly counterintuitive design, bite ntropic filters are capable of similar or better accuracy to tokenizing filters. We also found a fascinating counterc orrellation between 1R OCA% and the final accuracy of a filter (the accuracy of the filter for the final 10% of the corpus).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yerazunis06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yerazunis06,
		author = {William S. Yerazunis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Seven Hypothesis about Spam Filtering},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/crm.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yerazunis06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

