# Proceedings - Blog 2008 

#### Overview of the TREC 2008 Blog Track

_Iadh Ounis, Craig MacDonald, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec17/papers/BLOG.OVERVIEW08.pdf](https://trec.nist.gov/pubs/trec17/papers/BLOG.OVERVIEW08.pdf)
??? abstract "Abstract"
	
	The Blog track explores the information seeking behaviour in the blogosphere. The track was introduced in 2006 [1], with a main pi- lot search task, namely the opinion-finding task. In TREC 2007 [2], the track investigated two main tasks inspired by the analysis of a commercial blog-search query log: the opinion-finding task (i.e. “What do people think about X?”) and the blog distillation task (i.e. “Find me a blog with a principal, recurring interest in X.”). In addition, the Blog 2007 track investigated a natural extension to the opinion-finding task, namely the polarity task (i.e. “Find me positive or negative opinionated posts about X.”). All tasks thus far investigated in the Blog track have used the so-called Blogs06 collection, which was created by the University of Glasgow [3]. The Blogs06 collection was crawled over an 11-week period from 6th December 2005 until the 21st February 2006. The collection is 148GB in size, consisting of 38.6GB of feeds, 88.8GB of permalink documents, and 28.8GB of homepages. For TREC 2008, the track continued using the Blogs06 collection. It also continued investigating the opinion-finding, polarity, and blog distillation tasks. In addition, the Blog track 2008 introduced a baseline blog post retrieval task (i.e. “Find me blog posts about X.”), to encourage participants to study the impact of their opinion-finding techniques across different underlying topic-relevance baselines. As a consequence, following our conclusions from both the TREC 2006 and the Blog 2007 tracks, we structured the Blog track 2008 around four tasks: (1) Baseline adhoc (blog post) retrieval task; (2) Opinion-finding (blog post) retrieval task; (3) Polarity opinion-finding (blog post) retrieval task; and (4) Blog (feed) distillation task. The track has seen an increased level of participation over the years from 17 groups in 2006, to 24 groups in 2007 (20 participants in the opinion-finding task, 11 in the polarity task, and 9 in the blog distillation task). In TREC 2008, 20 groups submitted runs to the baseline task, 19 groups submitted runs to the opinion-finding task, 16 groups submitted runs to the polarity task, and 12 groups submitted runs to the blog distillation task. The remainder of this paper is structured as follows. Section 2 describes the baseline and opinion-finding tasks, providing an overview of the submitted runs, as well as a summary of the main effective techniques used by the participating groups. Section 3 describes the polarity task, and the main obtained results by the participating groups. Section 4 describes the blog search (blog distillation) task, and summarises the results of the runs and the main effective approaches deployed by the participating groups. We provide concluding remarks in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OunisMS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/OunisMS08,
		author = {Iadh Ounis and Craig MacDonald and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2008 Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {https://trec.nist.gov/pubs/trec17/papers/BLOG.OVERVIEW08.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OunisMS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FUB, IASI-CNR and University of Tor Vergata at TREC 2008 Blog  Track

_Giambattista Amati, Giuseppe Amodeo, Marco Bianchi, Carlo Gaibisso, Giorgio Gambosi_

- :fontawesome-solid-user-group: **Participant:** [fub](./participants.md#fub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/fondazione.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/fondazione.blog.pdf)
- :material-file-search: **Runs:** [FIUbaseDFRee](./runs.md#fiubasedfree) | [FIUbasePL2c9](./runs.md#fiubasepl2c9) | [FIUPL2c9DFR](./runs.md#fiupl2c9dfr) | [FIUPL2PL2c9](./runs.md#fiupl2pl2c9) | [FIUDFRDFR](./runs.md#fiudfrdfr) | [FIUDFRPL2c9](./runs.md#fiudfrpl2c9) | [FIUBL1DFR](./runs.md#fiubl1dfr) | [FIUBL1PL2c9](./runs.md#fiubl1pl2c9) | [FIUBL2DFR](./runs.md#fiubl2dfr) | [FIUBL2PL2c9](./runs.md#fiubl2pl2c9) | [FIUBL3DFR](./runs.md#fiubl3dfr) | [FIUBL3PL2c9](./runs.md#fiubl3pl2c9) | [FIUBL4DFR](./runs.md#fiubl4dfr) | [FIUBL4PL2c9](./runs.md#fiubl4pl2c9) | [FIUBL5DFR](./runs.md#fiubl5dfr) | [FIUBL5PL2c9](./runs.md#fiubl5pl2c9) | [FIUpPL2DFR](./runs.md#fiuppl2dfr) | [FIUpDFRDFR](./runs.md#fiupdfrdfr) | [FIUpBL1DFR](./runs.md#fiupbl1dfr) | [FIUpBL2DFR](./runs.md#fiupbl2dfr) | [FIUpBL3DFR](./runs.md#fiupbl3dfr) | [FIUpBL4DFR](./runs.md#fiupbl4dfr) | [FIUpBL5DFR](./runs.md#fiupbl5dfr)

??? abstract "Abstract"
	
	We take part in the opinion and polarity retrieval tasks of the blog track. A test collection, called Blog06, was created for the blog track in 2006 [4] with three main different components: feeds, permalinks and home-pages. The collection contains spam as well as possibly no blogs and no english pages. For our experimentation only permalinks have been taken into consideration, consisting of 3.2 million of Web pages for a total of 88.8GB, each one containing a post and its related comments. The evaluation metrics are precision/recall based [4], the Mean Average Precision (MAP) and R-Precision (RPrec), but we also focused on Precision at 10 (P@10), due to its relevance in evaluating the effectiveness of Web search engines [5] [3]. As in 2007, we based our approch on the costruction of ad-hoc weighted dictionaries, containing terms assumed to be used to express a sentiment. The weight is a measure of how much sentiment the term expresses. To automatically construct our dictionaries, we assumed that “opinion-bearing” words distribute more randomly in the set of opinionated documents than semantic-bearing terms, but less randomly than not-informative terms. As a consequence, we relyed on two theoretic measures. The first of them was based on a Divergence From Randomness (DFR) model and defined the weight of each term within an opinionated document, conseguently identifing the set of terms candidate to appear in the vocabularies. The other one, was based on entropy maximization in the set of all relevant and opinionated documents and defined the final content of the dictionaries and the weights of their terms. By these dictionaries, we first reranked the set of documents relevant to a topic on the basis of the quantity of opinion they express, and then extract two new rankings according to the polarity of the expressed sentiment. All these phases are detailed described in Sections 2, 3, 4, 5 and 6. Finally, in Section 7 we report and discuss on the experimentation activity and results. Finally, a brief analysis of our results is present in 8.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiABGG08.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiABGG08,
		author = {Giambattista Amati and Giuseppe Amodeo and Marco Bianchi and Carlo Gaibisso and Giorgio Gambosi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {FUB, {IASI-CNR} and University of Tor Vergata at {TREC} 2008 Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/fondazione.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiABGG08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT Kharagpur at TREC 2008 Blog Track

_Robin Anil, Sudeshna Sarkar_

- :fontawesome-solid-user-group: **Participant:** [iitkgp](./participants.md#iitkgp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/iit.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/iit.blog.pdf)
- :material-file-search: **Runs:** [IITKGPNOSPAM](./runs.md#iitkgpnospam) | [IITKGPTITLE1](./runs.md#iitkgptitle1) | [KGPPOS1](./runs.md#kgppos1) | [KGPOP](./runs.md#kgpop) | [KGPPOS2](./runs.md#kgppos2) | [KGPFILTER](./runs.md#kgpfilter) | [KGPPOL1](./runs.md#kgppol1) | [KGPPOL2](./runs.md#kgppol2) | [KGPBASE4](./runs.md#kgpbase4) | [FEEDKGP](./runs.md#feedkgp) | [FEEDKGP1](./runs.md#feedkgp1)

??? abstract "Abstract"
	
	This paper describes our opinion retrieval system for TREC 2008 blog track. We focused on five different aspects of the system. The first module is focussed on extracting the blog content out from junk html and thereby decreasing the noise in the indexed content. The second module aims at removing various kind of spam content from real blogs. The third module aimed at retrieving the relevant documents. The fourth module filters out opinionated documents and the fifth one calculated the polarity of the sentiments in the document. The final ranked retrieval runs were based on various combination of settings in each module so as to study the effect of each. For classification of subjectivity and polarity, the predictions we done using a complementary naive bayes classifier
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnilS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnilS08,
		author = {Robin Anil and Sudeshna Sarkar},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} Kharagpur at {TREC} 2008 Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/iit.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnilS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Document and Query Expansion Models for Blog Distillation

_Jaime Arguello, Jonathan L. Elsas, Changkuk Yoo, Jamie Callan, Jaime G. Carbonell_

- :fontawesome-solid-user-group: **Participant:** [CMU-LTI-DIR](./participants.md#cmu-lti-dir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/cmu.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/cmu.blog.rev.pdf)
- :material-file-search: **Runs:** [cmuLDwiki](./runs.md#cmuldwiki) | [cmuLDwikiSP](./runs.md#cmuldwikisp) | [cmuSD](./runs.md#cmusd) | [cmuSDwiki](./runs.md#cmusdwiki)

??? abstract "Abstract"
	
	This paper presents the CMU submission to the 2008 TREC blog distillation track. Similar to last year's experiments, we evaluate different retrieval models and apply a query expansion method that leverages the link structure in Wikipedia. We also explore using a corpus that combines several different representations of the documents, using both the feed XML and permalink HTML, and apply initial experiments with spam filtering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ArguelloEYCC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ArguelloEYCC08,
		author = {Jaime Arguello and Jonathan L. Elsas and Changkuk Yoo and Jamie Callan and Jaime G. Carbonell},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Document and Query Expansion Models for Blog Distillation},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/cmu.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ArguelloEYCC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DCU at the TREC 2008 Blog Track

_Adam Bermingham, Alan F. Smeaton, Jennifer Foster, Deirdre Hogan_

- :fontawesome-solid-user-group: **Participant:** [aic-dcu](./participants.md#aic-dcu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/dublin.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/dublin.blog.pdf)
- :material-file-search: **Runs:** [DCUCDVPtbl](./runs.md#dcucdvptbl) | [DCUCDVPtdbl](./runs.md#dcucdvptdbl) | [DCUCDVPgo](./runs.md#dcucdvpgo) | [DCUCDVPgonc](./runs.md#dcucdvpgonc) | [DCUCDVPgoo](./runs.md#dcucdvpgoo) | [DCUCDVPgoonc](./runs.md#dcucdvpgoonc) | [DCUCDVPgp](./runs.md#dcucdvpgp) | [DCUCDVPgpo](./runs.md#dcucdvpgpo) | [DCUCDVPtdo](./runs.md#dcucdvptdo) | [DCUCDVPtdp](./runs.md#dcucdvptdp) | [DCUCDVPto](./runs.md#dcucdvpto) | [DCUCDVPtol](./runs.md#dcucdvptol) | [DCUCDVPtolnc](./runs.md#dcucdvptolnc) | [DCUCDVPtpl](./runs.md#dcucdvptpl)

??? abstract "Abstract"
	
	In this paper we describe our system, experiments and results from our participation in the Blog Track at TREC 2008. Dublin City University participated in the adhoc retrieval, opinion finding and polarised opinion finding tasks. For opinion finding, we used a fusion of approaches based on lexicon features, surface features and syntactic features. Our experiments evaluated the relative usefulness of each of the feature sets and achieved a significant improvement on the baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BerminghamSFH08.bib) "
	```
	@inproceedings{DBLP:conf/trec/BerminghamSFH08,
		author = {Adam Bermingham and Alan F. Smeaton and Jennifer Foster and Deirdre Hogan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DCU} at the {TREC} 2008 Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/dublin.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BerminghamSFH08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UniNE at TREC 2008: Fact and Opinion Retrieval in the Blogsphere

_Claire Fautsch, Jacques Savoy_

- :fontawesome-solid-user-group: **Participant:** [UniNE](./participants.md#unine)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uneuchatel.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/uneuchatel.blog.pdf)
- :material-file-search: **Runs:** [UniNEBlog1](./runs.md#unineblog1) | [UniNEBlog2](./runs.md#unineblog2) | [UniNEopZb1](./runs.md#unineopzb1) | [UniNEopZb2](./runs.md#unineopzb2) | [UniNEopZb4](./runs.md#unineopzb4) | [UniNEopZb5](./runs.md#unineopzb5) | [UniNEopLR1](./runs.md#unineoplr1) | [UniNEopLR2](./runs.md#unineoplr2) | [UniNEopLRb1](./runs.md#unineoplrb1) | [UniNEopLRb2](./runs.md#unineoplrb2) | [UniNEopLRb3](./runs.md#unineoplrb3) | [UniNEopLRb4](./runs.md#unineoplrb4) | [UniNEopLRb5](./runs.md#unineoplrb5) | [UniNEopZ1](./runs.md#unineopz1) | [UniNEopZ2](./runs.md#unineopz2) | [UniNEopZb3](./runs.md#unineopzb3) | [UniNEpolLR1](./runs.md#uninepollr1) | [UniNEpolLRb1](./runs.md#uninepollrb1) | [UniNEpolLRb2](./runs.md#uninepollrb2) | [UniNEpolLRb3](./runs.md#uninepollrb3) | [UniNEpolLRb4](./runs.md#uninepollrb4) | [UniNEpolLRb5](./runs.md#uninepollrb5) | [UniNEpolZ1](./runs.md#uninepolz1) | [UniNEpolZb1](./runs.md#uninepolzb1) | [UniNEpolZb2](./runs.md#uninepolzb2) | [UniNEpolZb3](./runs.md#uninepolzb3) | [UniNEpolZb4](./runs.md#uninepolzb4) | [UniNEpolZb5](./runs.md#uninepolzb5)

??? abstract "Abstract"
	
	This paper describes our participation in the Blog track at the TREC 2008 evaluation campaign. The Blog track goes beyond simple document retrieval, its main goal is to identify opinionated blog posts and assign a polarity measure (positive, negative or mixed) to these information items. Available topics cover various target entities, such as people, location or product for example. This year's Blog task may be subdivided into three parts: First, retrieve relevant information (facts & opinionated documents), second extract only opinionated documents (either positive, negative or mixed) and third classify opinionated documents as having a positive or negative polarity. For the first part of our participation we evaluate different indexing strategies as well as various retrieval models such as Okapi (BM25) and two models derived from the Divergence from Randomness (DFR) paradigm. For the opinion and polarity detection part, we use two different approaches, an additive and a logistic-based model using characteristic terms to discriminate between various opinion classes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FautschS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/FautschS08,
		author = {Claire Fautsch and Jacques Savoy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UniNE at {TREC} 2008: Fact and Opinion Retrieval in the Blogsphere},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uneuchatel.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FautschS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lugano at TREC 2008 Blog Track

_Shima Gerani, Mostafa Keikha, Mark James Carman, Robert Gwadera, Davide Taibi, Fabio Crestani_

- :fontawesome-solid-user-group: **Participant:** [USI](./participants.md#usi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/ulugano.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/ulugano.blog.rev.pdf)
- :material-file-search: **Runs:** [run0](./runs.md#run0) | [opin0kl](./runs.md#opin0kl) | [opin0svm](./runs.md#opin0svm) | [opin1kl](./runs.md#opin1kl) | [opin1svm](./runs.md#opin1svm) | [BM25LenNorm](./runs.md#bm25lennorm) | [svmMap](./runs.md#svmmap)

??? abstract "Abstract"
	
	We report on the University of Lugano's participation in the Blog track of TREC 2008. In particular we describe our system for performing opinion retrieval and blog distillation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeraniKCGTC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeraniKCGTC08,
		author = {Shima Gerani and Mostafa Keikha and Mark James Carman and Robert Gwadera and Davide Taibi and Fabio Crestani},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Lugano at {TREC} 2008 Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/ulugano.blog.rev.pdf},
		timestamp = {Mon, 29 Jun 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GeraniKCGTC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS in TREC 2008 Blog Track

_Hui He, Bo Chen, Lei Du, Si Li, Huiji Gao, Weiran Xu, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [BUPT_pris_](./participants.md#bupt_pris_)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/beijingu.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/beijingu.blog.pdf)
- :material-file-search: **Runs:** [prisba](./runs.md#prisba) | [prisbm](./runs.md#prisbm) | [prisoa1](./runs.md#prisoa1) | [prisom1](./runs.md#prisom1)

??? abstract "Abstract"
	
	This paper describes BUPT (pris) participation in baseline adhoc retrieval task and the opinion retrieval task at Blog Track 2008. The system adopts a two-stage strategy in the opinion retrieval task. In the first stage, the system carries out a basic topic relevance retrieval to get the top 1,000 documents for each query. In the second stage, our system combines several Maximum Entropy based classifiers to implement opinion judging and ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeCDLGXG08.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeCDLGXG08,
		author = {Hui He and Bo Chen and Lei Du and Si Li and Huiji Gao and Weiran Xu and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} in {TREC} 2008 Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/beijingu.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeCDLGXG08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### KLE at TREC 2008 Blog Track: Blog Post and Feed Retrieval

_Yeha Lee, Seung-Hoon Na, Jungi Kim, Sang-Hyob Nam, Hun-Young Jung, Jong-Hyeok Lee_

- :fontawesome-solid-user-group: **Participant:** [POSTECH-KLE](./participants.md#postech-kle)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/pohang.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/pohang.blog.rev.pdf)
- :material-file-search: **Runs:** [KLEPsgFeedT](./runs.md#klepsgfeedt) | [KLEPsgFeedTD](./runs.md#klepsgfeedtd) | [KLEPsgRetT](./runs.md#klepsgrett) | [KLEPsgRetTD](./runs.md#klepsgrettd) | [KLEPsgRetTDN](./runs.md#klepsgrettdn) | [KLEDocOpinT](./runs.md#kledocopint) | [KLEPsgOpinT](./runs.md#klepsgopint) | [KLEDocOpinTD](./runs.md#kledocopintd) | [KLEPsgOpinTD](./runs.md#klepsgopintd) | [B1DocOpinAZN](./runs.md#b1docopinazn) | [B1DocOpinSWN](./runs.md#b1docopinswn) | [B1PsgOpinAZN](./runs.md#b1psgopinazn) | [B1PsgOpinSWN](./runs.md#b1psgopinswn) | [B2DocOpinAZN](./runs.md#b2docopinazn) | [B2DocOpinSWN](./runs.md#b2docopinswn) | [B2PsgOpinAZN](./runs.md#b2psgopinazn) | [B2PsgOpinSWN](./runs.md#b2psgopinswn) | [B3DocOpinAZN](./runs.md#b3docopinazn) | [B3DocOpinSWN](./runs.md#b3docopinswn) | [B3PsgOpinAZN](./runs.md#b3psgopinazn) | [B3PsgOpinSWN](./runs.md#b3psgopinswn) | [B4DocOpinAZN](./runs.md#b4docopinazn) | [B4DocOpinSWN](./runs.md#b4docopinswn) | [B4PsgOpinAZN](./runs.md#b4psgopinazn) | [B4PsgOpinSWN](./runs.md#b4psgopinswn) | [B5DocOpinAZN](./runs.md#b5docopinazn) | [B5DocOpinSWN](./runs.md#b5docopinswn) | [B5PsgOpinAZN](./runs.md#b5psgopinazn) | [B5PsgOpinSWN](./runs.md#b5psgopinswn) | [KLEPolarity](./runs.md#klepolarity) | [B4Polarity](./runs.md#b4polarity) | [B1Polarity](./runs.md#b1polarity) | [B2Polarity](./runs.md#b2polarity) | [B3Polarity](./runs.md#b3polarity) | [B5Polarity](./runs.md#b5polarity) | [KLEDistFBT](./runs.md#kledistfbt) | [KLEDistFBB](./runs.md#kledistfbb) | [KLEDistLMT](./runs.md#kledistlmt) | [KLEDistLMB](./runs.md#kledistlmb)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2008 Blog Track. For the opinion task, we made an opinion retrieval model that consists of preprocessing, topic retrieval, opinion finding, and sentiment classification parts. For topic retrieval, our system is based on the passage-based retrieval model and feedback. For the opinion analysis, we created a pseudo opinionated word (POW), O, which is representative of all opinion words, and expanded the original query with O. For the blog distillation task, we integrated the average score of all posts within a feed, and the average score of the most relevant N post scores. We also examined the pseudo-relevance feedback for the distillation task by focusing on various document selection schemes to expand the query terms. The experimental results show a significant improvement over previous results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeNKNJL08.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeNKNJL08,
		author = {Yeha Lee and Seung{-}Hoon Na and Jungi Kim and Sang{-}Hyob Nam and Hun{-}Young Jung and Jong{-}Hyeok Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{KLE} at {TREC} 2008 Blog Track: Blog Post and Feed Retrieval},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/pohang.blog.rev.pdf},
		timestamp = {Sat, 30 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LeeNKNJL08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2008: Experiments in Blog, Enterprise,  and Relevance Feedback Tracks with Terrier

_Ben He, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [UoGtr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf)
- :material-file-search: **Runs:** [uogBLProx](./runs.md#uogblprox) | [uogBLProxCE](./runs.md#uogblproxce) | [uogOP1intL](./runs.md#uogop1intl) | [uogOP1ofL](./runs.md#uogop1ofl) | [uogOP2intL](./runs.md#uogop2intl) | [uogOP2ofL](./runs.md#uogop2ofl) | [uogOP3ofL](./runs.md#uogop3ofl) | [uogOP3intL](./runs.md#uogop3intl) | [uogOP4intL](./runs.md#uogop4intl) | [uogOP4ofL](./runs.md#uogop4ofl) | [uogOP5ofL](./runs.md#uogop5ofl) | [uogOP5extL](./runs.md#uogop5extl) | [uogPL11](./runs.md#uogpl11) | [uogPL21](./runs.md#uogpl21) | [uogPL31](./runs.md#uogpl31) | [uogPL41](./runs.md#uogpl41) | [uogPLb11](./runs.md#uogplb11) | [uogPLb21](./runs.md#uogplb21) | [uogPL51](./runs.md#uogpl51) | [uogOP1Pr](./runs.md#uogop1pr) | [uogOP2Pr](./runs.md#uogop2pr) | [uogOP3Pr](./runs.md#uogop3pr) | [uogOP4Pr](./runs.md#uogop4pr) | [uogOP5Pr](./runs.md#uogop5pr) | [uogOP1PrintL](./runs.md#uogop1printl) | [uogOP3PrintL](./runs.md#uogop3printl) | [uogOP4PrintL](./runs.md#uogop4printl) | [uogOP5PrintL](./runs.md#uogop5printl) | [uogOP2PrintL](./runs.md#uogop2printl) | [uogOPb1intL](./runs.md#uogopb1intl) | [uogOPb2intl](./runs.md#uogopb2intl) | [uogOPb1ofL](./runs.md#uogopb1ofl) | [uogOPb1Pr](./runs.md#uogopb1pr) | [uogOPb1PrinL](./runs.md#uogopb1prinl) | [uogOPb2ofL](./runs.md#uogopb2ofl) | [uogOPb2Pr](./runs.md#uogopb2pr) | [uogOPb2PrinL](./runs.md#uogopb2prinl) | [uogTrBDfe](./runs.md#uogtrbdfe) | [uogTrBDfeNP](./runs.md#uogtrbdfenp) | [uogTrBDfeNPD](./runs.md#uogtrbdfenpd) | [uogTrBDfeNWD](./runs.md#uogtrbdfenwd)

??? abstract "Abstract"
	
	In TREC 2008, we participate in the Blog, Enterprise, and Relevance Feedback tracks. In all tracks, we continue the research and development of the Terrier platform1 centred around extending state-of-the-art weighting models based on the Divergence From Randomness (DFR) framework [26]. In particular, we investigate two main themes, namely, proximity-based models, and collection and profile enrichment techniques based on several resources. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeMOPS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeMOPS08,
		author = {Ben He and Craig Macdonald and Iadh Ounis and Jie Peng and Rodrygo L. T. Santos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2008: Experiments in Blog, Enterprise, and Relevance Feedback Tracks with Terrier},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeMOPS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Hybrid Method for Opinion finding Task (KUNLP at TREC 2008 Blog  Track)

_Linh Hoang, Seung-Wook Lee, Gumwon Hong, Joo-Young Lee, Hae-Chang Rim_

- :fontawesome-solid-user-group: **Participant:** [KU](./participants.md#ku)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/koreau.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/koreau.blog.pdf)
- :material-file-search: **Runs:** [kunlpKLtd](./runs.md#kunlpkltd) | [kunlpKLtt](./runs.md#kunlpkltt) | [kunlpKLttOc](./runs.md#kunlpklttoc) | [kunlpKLttOs](./runs.md#kunlpklttos) | [kunlpKLtdOc](./runs.md#kunlpkltdoc) | [kunlpKLtdOs](./runs.md#kunlpkltdos) | [kunlpKLttPs](./runs.md#kunlpklttps) | [kunlpKLtdPs](./runs.md#kunlpkltdps)

??? abstract "Abstract"
	
	This paper presents an approach for the Opinion Finding task at TREC 2008 Blog Track. For the Ad-hoc Retrieval subtask, we adopt language model to retrieve relevant documents. For the Opinion Retrieval subtask, we propose a hybrid model of lexicon-based approach and machine learning approach for estimating and ranking the opinionated documents. For the Polarized Opinion Retrieval subtask, we employ machine learning for predicting the polarity and linear combination technique for ranking polar documents. The hybrid model which utilize both lexicon-based approach and machine learning approach to predict and rank opinionated documents are the focuses of our participation this year. Regarding the hybrid method for opinion retrieval subtask, our submitted runs yield 15% improvement over baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HoangLHLR08.bib) "
	```
	@inproceedings{DBLP:conf/trec/HoangLHLR08,
		author = {Linh Hoang and Seung{-}Wook Lee and Gumwon Hong and Joo{-}Young Lee and Hae{-}Chang Rim},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Hybrid Method for Opinion finding Task {(KUNLP} at {TREC} 2008 Blog Track)},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/koreau.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HoangLHLR08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 208 Blog Track

_Lifeng Jia, Clement T. Yu, Wei Zhang_

- :fontawesome-solid-user-group: **Participant:** [UIC_IR_Group](./participants.md#uic_ir_group)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uillinois-chicago.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/uillinois-chicago.blog.pdf)
- :material-file-search: **Runs:** [uicirnoa](./runs.md#uicirnoa) | [uicirwa](./runs.md#uicirwa) | [uicoprun1](./runs.md#uicoprun1) | [uicoprun2](./runs.md#uicoprun2) | [uicop1bl1](./runs.md#uicop1bl1) | [uicop2bl1](./runs.md#uicop2bl1) | [uicop1bl2](./runs.md#uicop1bl2) | [uicop2bl2](./runs.md#uicop2bl2) | [uicop1bl3](./runs.md#uicop1bl3) | [uicop2bl3](./runs.md#uicop2bl3) | [uicop1bl4](./runs.md#uicop1bl4) | [uicop2bl4](./runs.md#uicop2bl4) | [uicop1bl5](./runs.md#uicop1bl5) | [uicop2bl5](./runs.md#uicop2bl5) | [uicpolrun1](./runs.md#uicpolrun1) | [uicpol1bl1](./runs.md#uicpol1bl1) | [uicpol1bl2](./runs.md#uicpol1bl2) | [uicpol2bl2](./runs.md#uicpol2bl2) | [uicpol1bl3](./runs.md#uicpol1bl3) | [uicpol2bl3](./runs.md#uicpol2bl3) | [uicpol1bl4](./runs.md#uicpol1bl4) | [uicpol2bl4](./runs.md#uicpol2bl4) | [uicpol1bl5](./runs.md#uicpol1bl5) | [uicpol2bl5](./runs.md#uicpol2bl5) | [uicop1bl2r](./runs.md#uicop1bl2r) | [uicop2bl2r](./runs.md#uicop2bl2r) | [uicop1bl3r](./runs.md#uicop1bl3r) | [uicop2bl3r](./runs.md#uicop2bl3r) | [uicop1bl4r](./runs.md#uicop1bl4r) | [uicop2bl4r](./runs.md#uicop2bl4r) | [uicop1bl5r](./runs.md#uicop1bl5r) | [uicop2bl5r](./runs.md#uicop2bl5r) | [uicop1bl1r](./runs.md#uicop1bl1r)

??? abstract "Abstract"
	
	Our opinion retrieval system has four steps. In the first step, documents which are deemed relevant by the system with respect to the query are retrieved, without taking into consideration whether the documents are opinionative or not. In the second step, the abbreviations of query concepts in documents are recognized. This helps in identifying whether an opinion is in the vicinity of a query concept (which can be an abbreviation) in a document. The third step of opinion identification is designed for recognizing query-relevant opinions within the documents. In the forth step, for each query, all retrieved opinionated documents are ranked by various methods which take into account IR scores, opinion scores and the number of concepts in query. For the polarity subtask, the opinionative documents are classified into positive, negative and mixed types by two classifiers. Since TREC 2008 does not require mixed documents, all documents which are deemed mixed by our system are discarded.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiaYZ08.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiaYZ08,
		author = {Lifeng Jia and Clement T. Yu and Wei Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 208 Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uillinois-chicago.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiaYZ08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2008: Blog Track

_Mladen Kovacevic, Xiangji Huang_

- :fontawesome-solid-user-group: **Participant:** [york](./participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/yorku.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/yorku.blog.rev.pdf)
- :material-file-search: **Runs:** [york08bb1](./runs.md#york08bb1) | [york08bb2](./runs.md#york08bb2) | [york08bo1a](./runs.md#york08bo1a) | [york08bo3b](./runs.md#york08bo3b)

??? abstract "Abstract"
	
	York University participated in the TREC 2008 Blog track, by introducing two opinion finding features. By initially focusing solely on the sentiment terms found in a document, using two different methods, and not considering the topic relevance, we saw an overall negative impact in the final evaluations. Post-TREC improvements show the necessity of combining opinion weights with the topic relevance scores. A tunable combination function is used, which revealed some interesting findings about the opinion finding features noting the strengths and weaknesses. We also introduce the Compass Information Retrieval system, which is based on Okapi, as the driver by which these experiments were conducted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KovacevicH08.bib) "
	```
	@inproceedings{DBLP:conf/trec/KovacevicH08,
		author = {Mladen Kovacevic and Xiangji Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2008: Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/yorku.blog.rev.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KovacevicH08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UTDallas at TREC 2008 Blog Track

_Bin Li, Feifan Liu, Yang Liu_

- :fontawesome-solid-user-group: **Participant:** [UTD_SLP_Lab](./participants.md#utd_slp_lab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/utdallas.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/utdallas.blog.rev.pdf)
- :material-file-search: **Runs:** [SplBaseTD](./runs.md#splbasetd) | [SplBaseT](./runs.md#splbaset) | [NOpMM2opi](./runs.md#nopmm2opi) | [NOpMM3opi](./runs.md#nopmm3opi) | [NOpMM4opi](./runs.md#nopmm4opi) | [NOpMM5opi](./runs.md#nopmm5opi) | [NTrMM2opiP](./runs.md#ntrmm2opip) | [NTrMM33P](./runs.md#ntrmm33p) | [NTrMM43P](./runs.md#ntrmm43p) | [NTrMM53P](./runs.md#ntrmm53p) | [NOpMM23](./runs.md#nopmm23) | [NOpMM33](./runs.md#nopmm33) | [NOpMM43](./runs.md#nopmm43) | [NOpMM53](./runs.md#nopmm53) | [NTrMM27P](./runs.md#ntrmm27p) | [NTrMM37P](./runs.md#ntrmm37p) | [NTrMM47P](./runs.md#ntrmm47p) | [NTrMM57P](./runs.md#ntrmm57p) | [NOpMM27](./runs.md#nopmm27) | [NOpMM37](./runs.md#nopmm37) | [NOpMM47](./runs.md#nopmm47) | [NOpMM57](./runs.md#nopmm57) | [NOpMM21](./runs.md#nopmm21) | [NOpMM31](./runs.md#nopmm31) | [NOpMM41](./runs.md#nopmm41) | [NOpMM51](./runs.md#nopmm51) | [NOpMM103](./runs.md#nopmm103) | [NOpMM107](./runs.md#nopmm107) | [NTrMM13P](./runs.md#ntrmm13p) | [NTrMM17P](./runs.md#ntrmm17p) | [NOpMMopi](./runs.md#nopmmopi) | [NOpMM11](./runs.md#nopmm11) | [NOpMMs13](./runs.md#nopmms13) | [NOpMMs23](./runs.md#nopmms23) | [NOpMMs33](./runs.md#nopmms33) | [NOpMMs43](./runs.md#nopmms43) | [NOpMMs53](./runs.md#nopmms53)

??? abstract "Abstract"
	
	This paper describes our participation in the 2008 TREC Blog track. Our system consists of 3 components: data preprocessing, topic retrieval, and opinion finding. In the topic retrieval task, we applied Lemur IR toolkit and used various techniques for query expansion. In the opinion finding and polarization task, we employed a feature-based classification approach. Then re-ranking was performed using a linear combination of the opinionated score and the topic relevance score. Our system achieved reasonable performance in this evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiLL08.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiLL08,
		author = {Bin Li and Feifan Liu and Yang Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UTDallas at {TREC} 2008 Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/utdallas.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiLL08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FEUP at TREC 2008 Blog Track: Using Temporal Evidence for Ranking  and Feed Distillation

_Sérgio Nunes, Cristina Ribeiro, Gabriel David_

- :fontawesome-solid-user-group: **Participant:** [feup_irlab](./participants.md#feup_irlab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uporto.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uporto.blog.rev.pdf)
- :material-file-search: **Runs:** [feupB](./runs.md#feupb) | [feupBLMm02](./runs.md#feupblmm02) | [feupbase](./runs.md#feupbase) | [feupfs](./runs.md#feupfs) | [feupne](./runs.md#feupne) | [feupfsne](./runs.md#feupfsne)

??? abstract "Abstract"
	
	This paper presents the participation of FEUP, from University of Porto, in the TREC 2008 Blog Track. FEUP participated in two tasks, the baseline adhoc retrieval task and the blog finding distillation task. Our approach was focused on the use of the temporal information available in the TREC Blog06 collection. For the baseline adhoc retrieval task a simple temporal sort was evaluated. In the blog finding distillation task we tested three alternative scoring functions based on temporal evidence. All features were combined with a BM25 baseline run using a standard rank aggregation approach. We observed small, but statistically significant, improvements in several evaluation measures when temporal information is used.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NunesRD08.bib) "
	```
	@inproceedings{DBLP:conf/trec/NunesRD08,
		author = {S{\'{e}}rgio Nunes and Cristina Ribeiro and Gabriel David},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FEUP} at {TREC} 2008 Blog Track: Using Temporal Evidence for Ranking and Feed Distillation},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uporto.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NunesRD08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Polarity Classification of Blog TREC 2008 Data with a Geodesic Kernel

_Stephan Raaijmakers, Wessel Kraaij_

- :fontawesome-solid-user-group: **Participant:** [tno](./participants.md#tno)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/tno.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/tno.blog.rev.pdf)
- :material-file-search: **Runs:** [tnobase2](./runs.md#tnobase2) | [tnobase3](./runs.md#tnobase3) | [tnobase4](./runs.md#tnobase4) | [tnobase5](./runs.md#tnobase5) | [tnobase1](./runs.md#tnobase1)

??? abstract "Abstract"
	
	In this paper we describe the TNO approach to large-scale polarity classification of the Blog TREC 2008 dataset. Our participation consists of the submission of the 5 baseline runs provided by NIST, for which we applied a multinomial kernel machine operating on character n-gram representations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RaaijmakersK08.bib) "
	```
	@inproceedings{DBLP:conf/trec/RaaijmakersK08,
		author = {Stephan Raaijmakers and Wessel Kraaij},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Polarity Classification of Blog {TREC} 2008 Data with a Geodesic Kernel},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/tno.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RaaijmakersK08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2008 Blog Distillation Task

_Jangwon Seo, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [uMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/umass.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/umass.blog.pdf)
- :material-file-search: **Runs:** [UMassBlog1](./runs.md#umassblog1) | [UMassBlog2](./runs.md#umassblog2) | [UMassBlog3](./runs.md#umassblog3) | [UMassBlog4](./runs.md#umassblog4)

??? abstract "Abstract"
	
	This paper presents the work done for the TREC 2008 blog distillation task. We introduce two new methods based on blog site search using resource selection which was the framework we used for the TREC 2007 blog distillation task. One is a new factor that penalizes the topical diversity of a blog. The other is a query expansion technique. We compare the methods to strong baselines.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SeoC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/SeoC08,
		author = {Jangwon Seo and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2008 Blog Distillation Task},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/umass.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SeoC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2008 Relevance Feedback Track

_Xiaoling Sun, Yuan Lin, Hongfei Lin, Zhihao Yang_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./participants.md#dutir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/dalianu.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/dalianu.blog.pdf)
- :material-file-search: **Runs:** [DUT08BRun1](./runs.md#dut08brun1) | [DUT08BRun2](./runs.md#dut08brun2) | [DUTIR08Run4](./runs.md#dutir08run4) | [DUTIR08Run3](./runs.md#dutir08run3) | [DUTIR08Run1](./runs.md#dutir08run1) | [DUTIR08Run2](./runs.md#dutir08run2) | [DUTIR08Run6P](./runs.md#dutir08run6p) | [DUTIR08Run5P](./runs.md#dutir08run5p) | [DUTIR08Run2P](./runs.md#dutir08run2p) | [DUTIR08DRun1](./runs.md#dutir08drun1) | [DUTIR08DRun2](./runs.md#dutir08drun2) | [DUTIR08DRun3](./runs.md#dutir08drun3) | [DUTIR08DRun4](./runs.md#dutir08drun4)

??? abstract "Abstract"
	
	This paper details our experiments carried out at TREC 2008 Relevance Feedback Track. We focused on the analysis of feedback documents, both relevant and non-relevant, to explore more useful information to improve retrieval performance. In our experiments, local co-occurrence model and a Rocchio formula were used to select good expansion terms. Five runs were submitted. These runs used different amount of relevance info for analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SunLLY08.bib) "
	```
	@inproceedings{DBLP:conf/trec/SunLLY08,
		author = {Xiaoling Sun and Yuan Lin and Hongfei Lin and Zhihao Yang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2008 Relevance Feedback Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/dalianu.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SunLLY08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at TREC 2008 Blog Track

_Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooEng](./participants.md#uwaterlooeng)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uwaterloo-olga.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/uwaterloo-olga.blog.pdf)
- :material-file-search: **Runs:** [UWBase1](./runs.md#uwbase1) | [UWBase2](./runs.md#uwbase2) | [UWopinion1](./runs.md#uwopinion1) | [UWopinion2](./runs.md#uwopinion2) | [UWnb1Op](./runs.md#uwnb1op) | [UWnb2Op](./runs.md#uwnb2op) | [UWnb3Op](./runs.md#uwnb3op) | [UWnb4Op](./runs.md#uwnb4op) | [UWnb5Op](./runs.md#uwnb5op) | [UWnb1Pol](./runs.md#uwnb1pol) | [UWnb2Pol](./runs.md#uwnb2pol) | [UWnb3Pol](./runs.md#uwnb3pol) | [UWnb4Pol](./runs.md#uwnb4pol) | [UWnb5Pol](./runs.md#uwnb5pol) | [UWpolarity2](./runs.md#uwpolarity2) | [UWpolarity1](./runs.md#uwpolarity1)

??? abstract "Abstract"
	
	The paper reports the University of Waterloo participation in the opinion and polarity tasks of the Blog track. The proposed method uses a lexicon built from several linguistic resources. The opinion discriminating ability of each subjective lexical unit was estimated using the Kullback-Leibler divergence. The KLD scores of subjective words occurring within fixed-size windows around instances of query terms were used in calculating document scores. The described system also used a method of identifying phrases in topic titles by matching them to Wikipedia titles. The results show that both KLD-based scores of subjective lexical units and Wikipedia-matched phrases are useful techniques that help improve opinion retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Vechtomova08.bib) "
	```
	@inproceedings{DBLP:conf/trec/Vechtomova08,
		author = {Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Waterloo at {TREC} 2008 Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uwaterloo-olga.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Vechtomova08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2008 at the University at Buffalo: Legal and Blog Track

_Jianqiang Wang, Ying Sun, Omar Mukhtar, Rohini K. Srihari_

- :fontawesome-solid-user-group: **Participant:** [SUNY_Buffalo](./participants.md#suny_buffalo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/suny-buffalo.legal.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/suny-buffalo.legal.blog.rev.pdf)
- :material-file-search: **Runs:** [UB](./runs.md#ub) | [UBop1](./runs.md#ubop1) | [UBpol1](./runs.md#ubpol1) | [UBDist1](./runs.md#ubdist1) | [UBDist2](./runs.md#ubdist2) | [UBDist3](./runs.md#ubdist3) | [UBDist4](./runs.md#ubdist4)

??? abstract "Abstract"
	
	In the TREC 2008, the team from the State University of New York at Buffalo participated in the Legal track and the Blog track. For the Legal track, we worked on the interactive search task using the Web-based Legacy Tobacco Document Library Boolean search system. Our experiment achieved reasonable precision but suffered significantly from low recall. These results, together with the appealing and adjudication results, suggest that the concept of document relevance in legal e-discovery deserve further investigation. For the Blog distillation task, our official runs were based on a reduced document model in which only text from several most content-bearing fields were indexed. This approach indeed yielded encouraging retrieval effectiveness while significantly decreasing the index size. We also studied query independence/dependence and link-based features for finding relevant feeds. For the Blog opinion and polarity tasks, we mainly investigated the usefulness of opinionated words contained in the SentiGI lexicon. Our experiment results showed that the effectiveness of the technique is quite limited, indicating other more sophisticated techniques are needed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangSMS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangSMS08,
		author = {Jianqiang Wang and Ying Sun and Omar Mukhtar and Rohini K. Srihari},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2008 at the University at Buffalo: Legal and Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/suny-buffalo.legal.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangSMS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### External Query Expansion in the Blogosphere

_Wouter Weerkamp, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UAms_De_Rijke](./participants.md#uams_de_rijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.blog.rev.pdf)
- :material-file-search: **Runs:** [uams08n1o1](./runs.md#uams08n1o1) | [uams08class](./runs.md#uams08class) | [uams08b1pr](./runs.md#uams08b1pr) | [uams08b2pr](./runs.md#uams08b2pr) | [uams08b3pr](./runs.md#uams08b3pr) | [uams08b4pr](./runs.md#uams08b4pr) | [uams08b5pr](./runs.md#uams08b5pr) | [uams08clspr](./runs.md#uams08clspr) | [uams08n1o1sp](./runs.md#uams08n1o1sp) | [uams08qm4it1](./runs.md#uams08qm4it1) | [uams08qm4it2](./runs.md#uams08qm4it2) | [uams08bl](./runs.md#uams08bl) | [uams08nw](./runs.md#uams08nw) | [uams08pnw](./runs.md#uams08pnw) | [uams08nonr](./runs.md#uams08nonr)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the blog track at TREC 2008. We mainly explored different ways of using external corpora to expand the original query. In the blog post retrieval task we did not succeed in improving over a simple baseline (equal weights for both the expanded and original query). Obtaining optimal weights for the original and the expanded query remains a subject of investigation. In the blog distillation task we tried to improve over our (strong) baseline using external expansion, but due to differences in the run setup, comparing these runs is hard. Compared to a simpler baseline, we see an improvement for the run using external expansion on the combination of news, Wikipedia and blog posts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WeerkampR08.bib) "
	```
	@inproceedings{DBLP:conf/trec/WeerkampR08,
		author = {Wouter Weerkamp and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {External Query Expansion in the Blogosphere},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WeerkampR08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2008 Blog Track: Leveraging Multiple Sources of  Opinion Evidence

_Kiduk Yang_

- :fontawesome-solid-user-group: **Participant:** [IU-SLIS](./participants.md#iu-slis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/indianau.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/indianau.blog.rev.pdf)
- :material-file-search: **Runs:** [wdoqlnvN](./runs.md#wdoqlnvn) | [wdoqsBase](./runs.md#wdoqsbase) | [top3dt1mRd](./runs.md#top3dt1mrd) | [top3wt1mRc](./runs.md#top3wt1mrc) | [b4dt1mRd](./runs.md#b4dt1mrd) | [b4dt1pRd](./runs.md#b4dt1prd) | [wdqbdt1mRd](./runs.md#wdqbdt1mrd) | [wdqbdt1pRd](./runs.md#wdqbdt1prd) | [wdqfdt1pRd](./runs.md#wdqfdt1prd) | [wdqfdt1mRd](./runs.md#wdqfdt1mrd) | [b5dt1mRd](./runs.md#b5dt1mrd) | [b5dt1pRd](./runs.md#b5dt1prd) | [b5wt1pRc](./runs.md#b5wt1prc) | [b5wt1mRc](./runs.md#b5wt1mrc) | [wdqbdt1mP5](./runs.md#wdqbdt1mp5) | [wdqbdt1pP5](./runs.md#wdqbdt1pp5) | [top3dt1pP5](./runs.md#top3dt1pp5) | [top3dt1mP5](./runs.md#top3dt1mp5) | [b4dt1mP5](./runs.md#b4dt1mp5) | [b4dt1pP5](./runs.md#b4dt1pp5)

??? abstract "Abstract"
	
	Indiana University‟s WIDIT Lab1 participated in the Blog track‟s opinion task and the polarity subtask, where we combined multiple opinion detection methods to leverage a variety of complementary evidences rather than trying to optimize the utilization of a single source of evidence. To address the weakness of our past topical retrieval strategy, which generated mediocre baseline results with short queries (i.e., title only queries), we explored Web-based query expansion (WebX) methods to increase the initial retrieval performance for the short query. Our WebX methods consisted of the Google module, which harvests expansion terms from Google search results using various term selection methods, and Wikipedia module, which extracts noun phrases and related terms from Wikipedia articles and Wikipedia thesaurus. Web-expanded queries were combined using ad-hoc heuristics based on observation, trial and error, and some basic assumptions regarding quality of individual WebX methods. For opinion detection, we leveraged the complementary opinion evidences of Opinion Lexicon (e.g., suck, cool), Opinion Collocation (e.g., I believe, to me), and Opinion Morphology (e.g., sooooo, metacool) in the form of semi-automatically constructed opinion lexicons. In creating the opinion lexicons, we extracted terms from external sources (e.g., IMDb movie reviews and plot summaries) as well as the blog collection. Opinion lexicons were utilized by opinion scoring modules to compute opinion scores of documents, and the combined opinion score in conjunction with the on-topic retrieval score was used to boost the ranks of opinionated documents. To optimize the fusion formula for combining opinion and polarity scores, WIDIT used the “Dynamic Tuning Interface”, an interactive system optimization mechanism that displays the effects of tuning parameter changes in real time so as to guide its user towards the discovery of a system optimization state.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yang08.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yang08,
		author = {Kiduk Yang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2008 Blog Track: Leveraging Multiple Sources of Opinion Evidence},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/indianau.blog.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yang08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2008: Blog Track

_Tong Zhu, Min Zhang, Yiqun Liu, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [THUIR](./participants.md#thuir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/tsinghua.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/tsinghua.blog.rev.pdf)
- :material-file-search: **Runs:** [THUrelTwp](./runs.md#thureltwp) | [THUrelTwpmf](./runs.md#thureltwpmf) | [THUopnTmfRmf](./runs.md#thuopntmfrmf) | [THUopnTwpRRM](./runs.md#thuopntwprrm) | [THUopnTwpGen](./runs.md#thuopntwpgen) | [THUpolTmfPNR](./runs.md#thupoltmfpnr) | [THUpolTwpRD](./runs.md#thupoltwprd) | [THUopnTmfRQ](./runs.md#thuopntmfrq)

??? abstract "Abstract"
	
	This is the second time we participate in TREC Blog Track. There are three main tasks in the track, relevant finding task, opinion finding task and polarity task. In this year, we use multi-field relevance ranking in relevant finding task; and in opinion finding task, we focused on the combination of relevance score and opinionate score use a unified generation model; in polarity task, we develop two new methods to find out positive and negative blogs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuZLM08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuZLM08,
		author = {Tong Zhu and Min Zhang and Yiqun Liu and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2008: Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/tsinghua.blog.rev.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhuZLM08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

