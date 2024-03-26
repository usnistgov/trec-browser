# Proceedings 2008 

## Blog 

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

- :fontawesome-solid-user-group: **Participant:** [fub](./blog/participants.md#fub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/fondazione.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/fondazione.blog.pdf)
- :material-file-search: **Runs:** [FIUbaseDFRee](./blog/runs.md#fiubasedfree) | [FIUbasePL2c9](./blog/runs.md#fiubasepl2c9) | [FIUPL2c9DFR](./blog/runs.md#fiupl2c9dfr) | [FIUPL2PL2c9](./blog/runs.md#fiupl2pl2c9) | [FIUDFRDFR](./blog/runs.md#fiudfrdfr) | [FIUDFRPL2c9](./blog/runs.md#fiudfrpl2c9) | [FIUBL1DFR](./blog/runs.md#fiubl1dfr) | [FIUBL1PL2c9](./blog/runs.md#fiubl1pl2c9) | [FIUBL2DFR](./blog/runs.md#fiubl2dfr) | [FIUBL2PL2c9](./blog/runs.md#fiubl2pl2c9) | [FIUBL3DFR](./blog/runs.md#fiubl3dfr) | [FIUBL3PL2c9](./blog/runs.md#fiubl3pl2c9) | [FIUBL4DFR](./blog/runs.md#fiubl4dfr) | [FIUBL4PL2c9](./blog/runs.md#fiubl4pl2c9) | [FIUBL5DFR](./blog/runs.md#fiubl5dfr) | [FIUBL5PL2c9](./blog/runs.md#fiubl5pl2c9) | [FIUpPL2DFR](./blog/runs.md#fiuppl2dfr) | [FIUpDFRDFR](./blog/runs.md#fiupdfrdfr) | [FIUpBL1DFR](./blog/runs.md#fiupbl1dfr) | [FIUpBL2DFR](./blog/runs.md#fiupbl2dfr) | [FIUpBL3DFR](./blog/runs.md#fiupbl3dfr) | [FIUpBL4DFR](./blog/runs.md#fiupbl4dfr) | [FIUpBL5DFR](./blog/runs.md#fiupbl5dfr)

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

- :fontawesome-solid-user-group: **Participant:** [iitkgp](./blog/participants.md#iitkgp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/iit.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/iit.blog.pdf)
- :material-file-search: **Runs:** [IITKGPNOSPAM](./blog/runs.md#iitkgpnospam) | [IITKGPTITLE1](./blog/runs.md#iitkgptitle1) | [KGPPOS1](./blog/runs.md#kgppos1) | [KGPOP](./blog/runs.md#kgpop) | [KGPPOS2](./blog/runs.md#kgppos2) | [KGPFILTER](./blog/runs.md#kgpfilter) | [KGPPOL1](./blog/runs.md#kgppol1) | [KGPPOL2](./blog/runs.md#kgppol2) | [KGPBASE4](./blog/runs.md#kgpbase4) | [FEEDKGP](./blog/runs.md#feedkgp) | [FEEDKGP1](./blog/runs.md#feedkgp1)

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

- :fontawesome-solid-user-group: **Participant:** [CMU-LTI-DIR](./blog/participants.md#cmu-lti-dir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/cmu.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/cmu.blog.rev.pdf)
- :material-file-search: **Runs:** [cmuLDwiki](./blog/runs.md#cmuldwiki) | [cmuLDwikiSP](./blog/runs.md#cmuldwikisp) | [cmuSD](./blog/runs.md#cmusd) | [cmuSDwiki](./blog/runs.md#cmusdwiki)

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

- :fontawesome-solid-user-group: **Participant:** [aic-dcu](./blog/participants.md#aic-dcu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/dublin.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/dublin.blog.pdf)
- :material-file-search: **Runs:** [DCUCDVPtbl](./blog/runs.md#dcucdvptbl) | [DCUCDVPtdbl](./blog/runs.md#dcucdvptdbl) | [DCUCDVPgo](./blog/runs.md#dcucdvpgo) | [DCUCDVPgonc](./blog/runs.md#dcucdvpgonc) | [DCUCDVPgoo](./blog/runs.md#dcucdvpgoo) | [DCUCDVPgoonc](./blog/runs.md#dcucdvpgoonc) | [DCUCDVPgp](./blog/runs.md#dcucdvpgp) | [DCUCDVPgpo](./blog/runs.md#dcucdvpgpo) | [DCUCDVPtdo](./blog/runs.md#dcucdvptdo) | [DCUCDVPtdp](./blog/runs.md#dcucdvptdp) | [DCUCDVPto](./blog/runs.md#dcucdvpto) | [DCUCDVPtol](./blog/runs.md#dcucdvptol) | [DCUCDVPtolnc](./blog/runs.md#dcucdvptolnc) | [DCUCDVPtpl](./blog/runs.md#dcucdvptpl)

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

- :fontawesome-solid-user-group: **Participant:** [UniNE](./blog/participants.md#unine)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uneuchatel.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/uneuchatel.blog.pdf)
- :material-file-search: **Runs:** [UniNEBlog1](./blog/runs.md#unineblog1) | [UniNEBlog2](./blog/runs.md#unineblog2) | [UniNEopZb1](./blog/runs.md#unineopzb1) | [UniNEopZb2](./blog/runs.md#unineopzb2) | [UniNEopZb4](./blog/runs.md#unineopzb4) | [UniNEopZb5](./blog/runs.md#unineopzb5) | [UniNEopLR1](./blog/runs.md#unineoplr1) | [UniNEopLR2](./blog/runs.md#unineoplr2) | [UniNEopLRb1](./blog/runs.md#unineoplrb1) | [UniNEopLRb2](./blog/runs.md#unineoplrb2) | [UniNEopLRb3](./blog/runs.md#unineoplrb3) | [UniNEopLRb4](./blog/runs.md#unineoplrb4) | [UniNEopLRb5](./blog/runs.md#unineoplrb5) | [UniNEopZ1](./blog/runs.md#unineopz1) | [UniNEopZ2](./blog/runs.md#unineopz2) | [UniNEopZb3](./blog/runs.md#unineopzb3) | [UniNEpolLR1](./blog/runs.md#uninepollr1) | [UniNEpolLRb1](./blog/runs.md#uninepollrb1) | [UniNEpolLRb2](./blog/runs.md#uninepollrb2) | [UniNEpolLRb3](./blog/runs.md#uninepollrb3) | [UniNEpolLRb4](./blog/runs.md#uninepollrb4) | [UniNEpolLRb5](./blog/runs.md#uninepollrb5) | [UniNEpolZ1](./blog/runs.md#uninepolz1) | [UniNEpolZb1](./blog/runs.md#uninepolzb1) | [UniNEpolZb2](./blog/runs.md#uninepolzb2) | [UniNEpolZb3](./blog/runs.md#uninepolzb3) | [UniNEpolZb4](./blog/runs.md#uninepolzb4) | [UniNEpolZb5](./blog/runs.md#uninepolzb5)

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

- :fontawesome-solid-user-group: **Participant:** [USI](./blog/participants.md#usi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/ulugano.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/ulugano.blog.rev.pdf)
- :material-file-search: **Runs:** [run0](./blog/runs.md#run0) | [opin0kl](./blog/runs.md#opin0kl) | [opin0svm](./blog/runs.md#opin0svm) | [opin1kl](./blog/runs.md#opin1kl) | [opin1svm](./blog/runs.md#opin1svm) | [BM25LenNorm](./blog/runs.md#bm25lennorm) | [svmMap](./blog/runs.md#svmmap)

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

- :fontawesome-solid-user-group: **Participant:** [BUPT_pris_](./blog/participants.md#bupt_pris_)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/beijingu.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/beijingu.blog.pdf)
- :material-file-search: **Runs:** [prisba](./blog/runs.md#prisba) | [prisbm](./blog/runs.md#prisbm) | [prisoa1](./blog/runs.md#prisoa1) | [prisom1](./blog/runs.md#prisom1)

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

- :fontawesome-solid-user-group: **Participant:** [POSTECH-KLE](./blog/participants.md#postech-kle)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/pohang.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/pohang.blog.rev.pdf)
- :material-file-search: **Runs:** [KLEPsgFeedT](./blog/runs.md#klepsgfeedt) | [KLEPsgFeedTD](./blog/runs.md#klepsgfeedtd) | [KLEPsgRetT](./blog/runs.md#klepsgrett) | [KLEPsgRetTD](./blog/runs.md#klepsgrettd) | [KLEPsgRetTDN](./blog/runs.md#klepsgrettdn) | [KLEDocOpinT](./blog/runs.md#kledocopint) | [KLEPsgOpinT](./blog/runs.md#klepsgopint) | [KLEDocOpinTD](./blog/runs.md#kledocopintd) | [KLEPsgOpinTD](./blog/runs.md#klepsgopintd) | [B1DocOpinAZN](./blog/runs.md#b1docopinazn) | [B1DocOpinSWN](./blog/runs.md#b1docopinswn) | [B1PsgOpinAZN](./blog/runs.md#b1psgopinazn) | [B1PsgOpinSWN](./blog/runs.md#b1psgopinswn) | [B2DocOpinAZN](./blog/runs.md#b2docopinazn) | [B2DocOpinSWN](./blog/runs.md#b2docopinswn) | [B2PsgOpinAZN](./blog/runs.md#b2psgopinazn) | [B2PsgOpinSWN](./blog/runs.md#b2psgopinswn) | [B3DocOpinAZN](./blog/runs.md#b3docopinazn) | [B3DocOpinSWN](./blog/runs.md#b3docopinswn) | [B3PsgOpinAZN](./blog/runs.md#b3psgopinazn) | [B3PsgOpinSWN](./blog/runs.md#b3psgopinswn) | [B4DocOpinAZN](./blog/runs.md#b4docopinazn) | [B4DocOpinSWN](./blog/runs.md#b4docopinswn) | [B4PsgOpinAZN](./blog/runs.md#b4psgopinazn) | [B4PsgOpinSWN](./blog/runs.md#b4psgopinswn) | [B5DocOpinAZN](./blog/runs.md#b5docopinazn) | [B5DocOpinSWN](./blog/runs.md#b5docopinswn) | [B5PsgOpinAZN](./blog/runs.md#b5psgopinazn) | [B5PsgOpinSWN](./blog/runs.md#b5psgopinswn) | [KLEPolarity](./blog/runs.md#klepolarity) | [B4Polarity](./blog/runs.md#b4polarity) | [B1Polarity](./blog/runs.md#b1polarity) | [B2Polarity](./blog/runs.md#b2polarity) | [B3Polarity](./blog/runs.md#b3polarity) | [B5Polarity](./blog/runs.md#b5polarity) | [KLEDistFBT](./blog/runs.md#kledistfbt) | [KLEDistFBB](./blog/runs.md#kledistfbb) | [KLEDistLMT](./blog/runs.md#kledistlmt) | [KLEDistLMB](./blog/runs.md#kledistlmb)

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

- :fontawesome-solid-user-group: **Participant:** [UoGtr](./blog/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf)
- :material-file-search: **Runs:** [uogBLProx](./blog/runs.md#uogblprox) | [uogBLProxCE](./blog/runs.md#uogblproxce) | [uogOP1intL](./blog/runs.md#uogop1intl) | [uogOP1ofL](./blog/runs.md#uogop1ofl) | [uogOP2intL](./blog/runs.md#uogop2intl) | [uogOP2ofL](./blog/runs.md#uogop2ofl) | [uogOP3ofL](./blog/runs.md#uogop3ofl) | [uogOP3intL](./blog/runs.md#uogop3intl) | [uogOP4intL](./blog/runs.md#uogop4intl) | [uogOP4ofL](./blog/runs.md#uogop4ofl) | [uogOP5ofL](./blog/runs.md#uogop5ofl) | [uogOP5extL](./blog/runs.md#uogop5extl) | [uogPL11](./blog/runs.md#uogpl11) | [uogPL21](./blog/runs.md#uogpl21) | [uogPL31](./blog/runs.md#uogpl31) | [uogPL41](./blog/runs.md#uogpl41) | [uogPLb11](./blog/runs.md#uogplb11) | [uogPLb21](./blog/runs.md#uogplb21) | [uogPL51](./blog/runs.md#uogpl51) | [uogOP1Pr](./blog/runs.md#uogop1pr) | [uogOP2Pr](./blog/runs.md#uogop2pr) | [uogOP3Pr](./blog/runs.md#uogop3pr) | [uogOP4Pr](./blog/runs.md#uogop4pr) | [uogOP5Pr](./blog/runs.md#uogop5pr) | [uogOP1PrintL](./blog/runs.md#uogop1printl) | [uogOP3PrintL](./blog/runs.md#uogop3printl) | [uogOP4PrintL](./blog/runs.md#uogop4printl) | [uogOP5PrintL](./blog/runs.md#uogop5printl) | [uogOP2PrintL](./blog/runs.md#uogop2printl) | [uogOPb1intL](./blog/runs.md#uogopb1intl) | [uogOPb2intl](./blog/runs.md#uogopb2intl) | [uogOPb1ofL](./blog/runs.md#uogopb1ofl) | [uogOPb1Pr](./blog/runs.md#uogopb1pr) | [uogOPb1PrinL](./blog/runs.md#uogopb1prinl) | [uogOPb2ofL](./blog/runs.md#uogopb2ofl) | [uogOPb2Pr](./blog/runs.md#uogopb2pr) | [uogOPb2PrinL](./blog/runs.md#uogopb2prinl) | [uogTrBDfe](./blog/runs.md#uogtrbdfe) | [uogTrBDfeNP](./blog/runs.md#uogtrbdfenp) | [uogTrBDfeNPD](./blog/runs.md#uogtrbdfenpd) | [uogTrBDfeNWD](./blog/runs.md#uogtrbdfenwd)

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

- :fontawesome-solid-user-group: **Participant:** [KU](./blog/participants.md#ku)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/koreau.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/koreau.blog.pdf)
- :material-file-search: **Runs:** [kunlpKLtd](./blog/runs.md#kunlpkltd) | [kunlpKLtt](./blog/runs.md#kunlpkltt) | [kunlpKLttOc](./blog/runs.md#kunlpklttoc) | [kunlpKLttOs](./blog/runs.md#kunlpklttos) | [kunlpKLtdOc](./blog/runs.md#kunlpkltdoc) | [kunlpKLtdOs](./blog/runs.md#kunlpkltdos) | [kunlpKLttPs](./blog/runs.md#kunlpklttps) | [kunlpKLtdPs](./blog/runs.md#kunlpkltdps)

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

- :fontawesome-solid-user-group: **Participant:** [UIC_IR_Group](./blog/participants.md#uic_ir_group)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uillinois-chicago.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/uillinois-chicago.blog.pdf)
- :material-file-search: **Runs:** [uicirnoa](./blog/runs.md#uicirnoa) | [uicirwa](./blog/runs.md#uicirwa) | [uicoprun1](./blog/runs.md#uicoprun1) | [uicoprun2](./blog/runs.md#uicoprun2) | [uicop1bl1](./blog/runs.md#uicop1bl1) | [uicop2bl1](./blog/runs.md#uicop2bl1) | [uicop1bl2](./blog/runs.md#uicop1bl2) | [uicop2bl2](./blog/runs.md#uicop2bl2) | [uicop1bl3](./blog/runs.md#uicop1bl3) | [uicop2bl3](./blog/runs.md#uicop2bl3) | [uicop1bl4](./blog/runs.md#uicop1bl4) | [uicop2bl4](./blog/runs.md#uicop2bl4) | [uicop1bl5](./blog/runs.md#uicop1bl5) | [uicop2bl5](./blog/runs.md#uicop2bl5) | [uicpolrun1](./blog/runs.md#uicpolrun1) | [uicpol1bl1](./blog/runs.md#uicpol1bl1) | [uicpol1bl2](./blog/runs.md#uicpol1bl2) | [uicpol2bl2](./blog/runs.md#uicpol2bl2) | [uicpol1bl3](./blog/runs.md#uicpol1bl3) | [uicpol2bl3](./blog/runs.md#uicpol2bl3) | [uicpol1bl4](./blog/runs.md#uicpol1bl4) | [uicpol2bl4](./blog/runs.md#uicpol2bl4) | [uicpol1bl5](./blog/runs.md#uicpol1bl5) | [uicpol2bl5](./blog/runs.md#uicpol2bl5) | [uicop1bl2r](./blog/runs.md#uicop1bl2r) | [uicop2bl2r](./blog/runs.md#uicop2bl2r) | [uicop1bl3r](./blog/runs.md#uicop1bl3r) | [uicop2bl3r](./blog/runs.md#uicop2bl3r) | [uicop1bl4r](./blog/runs.md#uicop1bl4r) | [uicop2bl4r](./blog/runs.md#uicop2bl4r) | [uicop1bl5r](./blog/runs.md#uicop1bl5r) | [uicop2bl5r](./blog/runs.md#uicop2bl5r) | [uicop1bl1r](./blog/runs.md#uicop1bl1r)

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

- :fontawesome-solid-user-group: **Participant:** [york](./blog/participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/yorku.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/yorku.blog.rev.pdf)
- :material-file-search: **Runs:** [york08bb1](./blog/runs.md#york08bb1) | [york08bb2](./blog/runs.md#york08bb2) | [york08bo1a](./blog/runs.md#york08bo1a) | [york08bo3b](./blog/runs.md#york08bo3b)

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

- :fontawesome-solid-user-group: **Participant:** [UTD_SLP_Lab](./blog/participants.md#utd_slp_lab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/utdallas.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/utdallas.blog.rev.pdf)
- :material-file-search: **Runs:** [SplBaseTD](./blog/runs.md#splbasetd) | [SplBaseT](./blog/runs.md#splbaset) | [NOpMM2opi](./blog/runs.md#nopmm2opi) | [NOpMM3opi](./blog/runs.md#nopmm3opi) | [NOpMM4opi](./blog/runs.md#nopmm4opi) | [NOpMM5opi](./blog/runs.md#nopmm5opi) | [NTrMM2opiP](./blog/runs.md#ntrmm2opip) | [NTrMM33P](./blog/runs.md#ntrmm33p) | [NTrMM43P](./blog/runs.md#ntrmm43p) | [NTrMM53P](./blog/runs.md#ntrmm53p) | [NOpMM23](./blog/runs.md#nopmm23) | [NOpMM33](./blog/runs.md#nopmm33) | [NOpMM43](./blog/runs.md#nopmm43) | [NOpMM53](./blog/runs.md#nopmm53) | [NTrMM27P](./blog/runs.md#ntrmm27p) | [NTrMM37P](./blog/runs.md#ntrmm37p) | [NTrMM47P](./blog/runs.md#ntrmm47p) | [NTrMM57P](./blog/runs.md#ntrmm57p) | [NOpMM27](./blog/runs.md#nopmm27) | [NOpMM37](./blog/runs.md#nopmm37) | [NOpMM47](./blog/runs.md#nopmm47) | [NOpMM57](./blog/runs.md#nopmm57) | [NOpMM21](./blog/runs.md#nopmm21) | [NOpMM31](./blog/runs.md#nopmm31) | [NOpMM41](./blog/runs.md#nopmm41) | [NOpMM51](./blog/runs.md#nopmm51) | [NOpMM103](./blog/runs.md#nopmm103) | [NOpMM107](./blog/runs.md#nopmm107) | [NTrMM13P](./blog/runs.md#ntrmm13p) | [NTrMM17P](./blog/runs.md#ntrmm17p) | [NOpMMopi](./blog/runs.md#nopmmopi) | [NOpMM11](./blog/runs.md#nopmm11) | [NOpMMs13](./blog/runs.md#nopmms13) | [NOpMMs23](./blog/runs.md#nopmms23) | [NOpMMs33](./blog/runs.md#nopmms33) | [NOpMMs43](./blog/runs.md#nopmms43) | [NOpMMs53](./blog/runs.md#nopmms53)

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

- :fontawesome-solid-user-group: **Participant:** [feup_irlab](./blog/participants.md#feup_irlab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uporto.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uporto.blog.rev.pdf)
- :material-file-search: **Runs:** [feupB](./blog/runs.md#feupb) | [feupBLMm02](./blog/runs.md#feupblmm02) | [feupbase](./blog/runs.md#feupbase) | [feupfs](./blog/runs.md#feupfs) | [feupne](./blog/runs.md#feupne) | [feupfsne](./blog/runs.md#feupfsne)

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

- :fontawesome-solid-user-group: **Participant:** [tno](./blog/participants.md#tno)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/tno.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/tno.blog.rev.pdf)
- :material-file-search: **Runs:** [tnobase2](./blog/runs.md#tnobase2) | [tnobase3](./blog/runs.md#tnobase3) | [tnobase4](./blog/runs.md#tnobase4) | [tnobase5](./blog/runs.md#tnobase5) | [tnobase1](./blog/runs.md#tnobase1)

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

- :fontawesome-solid-user-group: **Participant:** [uMass](./blog/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/umass.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/umass.blog.pdf)
- :material-file-search: **Runs:** [UMassBlog1](./blog/runs.md#umassblog1) | [UMassBlog2](./blog/runs.md#umassblog2) | [UMassBlog3](./blog/runs.md#umassblog3) | [UMassBlog4](./blog/runs.md#umassblog4)

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

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./blog/participants.md#dutir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/dalianu.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/dalianu.blog.pdf)
- :material-file-search: **Runs:** [DUT08BRun1](./blog/runs.md#dut08brun1) | [DUT08BRun2](./blog/runs.md#dut08brun2) | [DUTIR08Run4](./blog/runs.md#dutir08run4) | [DUTIR08Run3](./blog/runs.md#dutir08run3) | [DUTIR08Run1](./blog/runs.md#dutir08run1) | [DUTIR08Run2](./blog/runs.md#dutir08run2) | [DUTIR08Run6P](./blog/runs.md#dutir08run6p) | [DUTIR08Run5P](./blog/runs.md#dutir08run5p) | [DUTIR08Run2P](./blog/runs.md#dutir08run2p) | [DUTIR08DRun1](./blog/runs.md#dutir08drun1) | [DUTIR08DRun2](./blog/runs.md#dutir08drun2) | [DUTIR08DRun3](./blog/runs.md#dutir08drun3) | [DUTIR08DRun4](./blog/runs.md#dutir08drun4)

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

- :fontawesome-solid-user-group: **Participant:** [UWaterlooEng](./blog/participants.md#uwaterlooeng)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uwaterloo-olga.blog.pdf](http://trec.nist.gov/pubs/trec17/papers/uwaterloo-olga.blog.pdf)
- :material-file-search: **Runs:** [UWBase1](./blog/runs.md#uwbase1) | [UWBase2](./blog/runs.md#uwbase2) | [UWopinion1](./blog/runs.md#uwopinion1) | [UWopinion2](./blog/runs.md#uwopinion2) | [UWnb1Op](./blog/runs.md#uwnb1op) | [UWnb2Op](./blog/runs.md#uwnb2op) | [UWnb3Op](./blog/runs.md#uwnb3op) | [UWnb4Op](./blog/runs.md#uwnb4op) | [UWnb5Op](./blog/runs.md#uwnb5op) | [UWnb1Pol](./blog/runs.md#uwnb1pol) | [UWnb2Pol](./blog/runs.md#uwnb2pol) | [UWnb3Pol](./blog/runs.md#uwnb3pol) | [UWnb4Pol](./blog/runs.md#uwnb4pol) | [UWnb5Pol](./blog/runs.md#uwnb5pol) | [UWpolarity2](./blog/runs.md#uwpolarity2) | [UWpolarity1](./blog/runs.md#uwpolarity1)

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

- :fontawesome-solid-user-group: **Participant:** [SUNY_Buffalo](./blog/participants.md#suny_buffalo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/suny-buffalo.legal.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/suny-buffalo.legal.blog.rev.pdf)
- :material-file-search: **Runs:** [UB](./blog/runs.md#ub) | [UBop1](./blog/runs.md#ubop1) | [UBpol1](./blog/runs.md#ubpol1) | [UBDist1](./blog/runs.md#ubdist1) | [UBDist2](./blog/runs.md#ubdist2) | [UBDist3](./blog/runs.md#ubdist3) | [UBDist4](./blog/runs.md#ubdist4)

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

- :fontawesome-solid-user-group: **Participant:** [UAms_De_Rijke](./blog/participants.md#uams_de_rijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.blog.rev.pdf)
- :material-file-search: **Runs:** [uams08n1o1](./blog/runs.md#uams08n1o1) | [uams08class](./blog/runs.md#uams08class) | [uams08b1pr](./blog/runs.md#uams08b1pr) | [uams08b2pr](./blog/runs.md#uams08b2pr) | [uams08b3pr](./blog/runs.md#uams08b3pr) | [uams08b4pr](./blog/runs.md#uams08b4pr) | [uams08b5pr](./blog/runs.md#uams08b5pr) | [uams08clspr](./blog/runs.md#uams08clspr) | [uams08n1o1sp](./blog/runs.md#uams08n1o1sp) | [uams08qm4it1](./blog/runs.md#uams08qm4it1) | [uams08qm4it2](./blog/runs.md#uams08qm4it2) | [uams08bl](./blog/runs.md#uams08bl) | [uams08nw](./blog/runs.md#uams08nw) | [uams08pnw](./blog/runs.md#uams08pnw) | [uams08nonr](./blog/runs.md#uams08nonr)

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

- :fontawesome-solid-user-group: **Participant:** [IU-SLIS](./blog/participants.md#iu-slis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/indianau.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/indianau.blog.rev.pdf)
- :material-file-search: **Runs:** [wdoqlnvN](./blog/runs.md#wdoqlnvn) | [wdoqsBase](./blog/runs.md#wdoqsbase) | [top3dt1mRd](./blog/runs.md#top3dt1mrd) | [top3wt1mRc](./blog/runs.md#top3wt1mrc) | [b4dt1mRd](./blog/runs.md#b4dt1mrd) | [b4dt1pRd](./blog/runs.md#b4dt1prd) | [wdqbdt1mRd](./blog/runs.md#wdqbdt1mrd) | [wdqbdt1pRd](./blog/runs.md#wdqbdt1prd) | [wdqfdt1pRd](./blog/runs.md#wdqfdt1prd) | [wdqfdt1mRd](./blog/runs.md#wdqfdt1mrd) | [b5dt1mRd](./blog/runs.md#b5dt1mrd) | [b5dt1pRd](./blog/runs.md#b5dt1prd) | [b5wt1pRc](./blog/runs.md#b5wt1prc) | [b5wt1mRc](./blog/runs.md#b5wt1mrc) | [wdqbdt1mP5](./blog/runs.md#wdqbdt1mp5) | [wdqbdt1pP5](./blog/runs.md#wdqbdt1pp5) | [top3dt1pP5](./blog/runs.md#top3dt1pp5) | [top3dt1mP5](./blog/runs.md#top3dt1mp5) | [b4dt1mP5](./blog/runs.md#b4dt1mp5) | [b4dt1pP5](./blog/runs.md#b4dt1pp5)

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

- :fontawesome-solid-user-group: **Participant:** [THUIR](./blog/participants.md#thuir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/tsinghua.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/tsinghua.blog.rev.pdf)
- :material-file-search: **Runs:** [THUrelTwp](./blog/runs.md#thureltwp) | [THUrelTwpmf](./blog/runs.md#thureltwpmf) | [THUopnTmfRmf](./blog/runs.md#thuopntmfrmf) | [THUopnTwpRRM](./blog/runs.md#thuopntwprrm) | [THUopnTwpGen](./blog/runs.md#thuopntwpgen) | [THUpolTmfPNR](./blog/runs.md#thupoltmfpnr) | [THUpolTwpRD](./blog/runs.md#thupoltwprd) | [THUopnTmfRQ](./blog/runs.md#thuopntmfrq)

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

## Million Query 

#### Million Query Track 2008 Overview

_James Allan, Javed A. Aslam, Virgil Pavlu, Evangelos Kanoulas, Ben Carterette_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec17/papers/MQ.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec17/papers/MQ.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Million Query (1MQ) track ran for the second time in TREC 2008. The track is designed to serve two purposes: first, it is an exploration of ad-hoc retrieval over a large set of queries and a large collection of documents; second, it investigates questions of system evaluation, in particular whether it is better to evaluate using many shallow judgments or fewer thorough judgments. As with the 2007 track [ACA+07], participants ran 10,000 queries against a collection of 25 million documents. The 2008 track differed in the following ways: 1. Queries were assigned to one of four categories. 2. Each query was assigned a target of 8, 16, 32, 64, or 128 judgments. 3. Assessors could judge documents “not relevant but reasonable”. Section 1 describes how the corpus and queries were selected, the query classes, details of the submission formats, and a brief description of each submitted run. Section 2 provides an overview of the judging process, including a sketch of how it alternated between two methods for selecting the small set of documents to be judged. Sections 3.1 and 3.2 provide an overview of those two selection methods, developed at UMass and NEU, respectively. In Section 4 we present statistics collected during the judging process, including the total number of queries judged, how many judgments were served by each approach, and so on, along with the overall results of the track. We present additional results and analysis in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanAPKC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanAPKC08,
		author = {James Allan and Javed A. Aslam and Virgil Pavlu and Evangelos Kanoulas and Ben Carterette},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Million Query Track 2008 Overview},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {https://trec.nist.gov/pubs/trec17/papers/MQ.OVERVIEW.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanAPKC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Distributed Multisearch and Resource Selection for the TREC Million  Query Track

_Christopher T. Fallen, Gregory B. Newby, Kylie McCormick_

- :fontawesome-solid-user-group: **Participant:** [ARSC08](./million-query/participants.md#arsc08)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/ualaska.mq.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/ualaska.mq.rev.pdf)
- :material-file-search: **Runs:** [lsi150stat](./million-query/runs.md#lsi150stat) | [vsmstat](./million-query/runs.md#vsmstat) | [vsmstat07](./million-query/runs.md#vsmstat07) | [lsi150dyn](./million-query/runs.md#lsi150dyn) | [vsmdyn](./million-query/runs.md#vsmdyn)

??? abstract "Abstract"
	
	A distributed information retrieval system with resource-selection and result-set merging capability was used to search subsets of the GOV2 document corpus for the 2008 TREC Million Query Track. The GOV2 collection was partitioned into host-name subcollections and distributed to multiple remote machines. The Multisearch demonstration application restricted each search to a fraction of the available sub-collections that was pre-determined by a resource-selection algorithm. Experiment results from topic-by-topic resource selection and aggregate topic resource selection are compared. The sensitivity of Multisearch retrieval performance to variations in the resource selection algorithm is discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FallenNM08.bib) "
	```
	@inproceedings{DBLP:conf/trec/FallenNM08,
		author = {Christopher T. Fallen and Gregory B. Newby and Kylie McCormick},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Distributed Multisearch and Resource Selection for the {TREC} Million Query Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/ualaska.mq.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FallenNM08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Enterprise 

#### Overview of the TREC 2008 Enterprise Track

_Krisztian Balog, Ian Soboroff, Paul Thomas, Peter Bailey, Nick Craswell, Arjen P. de Vries_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec17/papers/ENTERPRISE.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec17/papers/ENTERPRISE.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The goal of the enterprise track is to conduct experiments with enterprise data that reflect the experiences of users in real organizations. This year, we continued with the CERC collection introduced in TREC 2007 (Bailey et al., 2007). Topics were developed in conjunction with CSIRO Enquiries, who field email and telephone questions about CSIRO research from the public.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogS0BCV08.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogS0BCV08,
		author = {Krisztian Balog and Ian Soboroff and Paul Thomas and Peter Bailey and Nick Craswell and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2008 Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {https://trec.nist.gov/pubs/trec17/papers/ENTERPRISE.OVERVIEW.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalogS0BCV08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Candidate and Document Models for Expert Search

_Krisztian Balog, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UAms_De_Rijke](./enterprise/participants.md#uams_de_rijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.ent.rev.pdf)
- :material-file-search: **Runs:** [UvA08DSbl](./enterprise/runs.md#uva08dsbl) | [UvA08DSbfb](./enterprise/runs.md#uva08dsbfb) | [UvA08DSexp](./enterprise/runs.md#uva08dsexp) | [UvA08DSall](./enterprise/runs.md#uva08dsall) | [UvA08EScomb](./enterprise/runs.md#uva08escomb) | [UvA08ESweb](./enterprise/runs.md#uva08esweb) | [UvA08ESm1b](./enterprise/runs.md#uva08esm1b) | [UvA08ESm2all](./enterprise/runs.md#uva08esm2all)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2008 Enterprise track and detail our language modeling-based approaches. For document search, our focus was on query expansion using profiles of top ranked experts and on document priors. We found that these techniques result in small, but noticeable improvements over our baseline method. For expert search, we combine candidate- and document-based models, and also bring in web evidence. We found that the combined models significantly and consistently outperformed our very competitive baseline models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogR08.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogR08,
		author = {Krisztian Balog and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Candidate and Document Models for Expert Search},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalogR08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DERI at TREC 2008 Enterprise Search Track

_Ronan Cummins, Colm O'Riordan_

- :fontawesome-solid-user-group: **Participant:** [DERI_IR_GROUP](./enterprise/participants.md#deri_ir_group)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/natu-ireland.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/natu-ireland.ent.rev.pdf)
- :material-file-search: **Runs:** [DERIrun5](./enterprise/runs.md#derirun5) | [DERIrun6](./enterprise/runs.md#derirun6) | [DERIrun7](./enterprise/runs.md#derirun7) | [DERIrun8](./enterprise/runs.md#derirun8) | [DERIrun1](./enterprise/runs.md#derirun1) | [DERIrun2](./enterprise/runs.md#derirun2) | [DERIrun4](./enterprise/runs.md#derirun4) | [DERIrun3](./enterprise/runs.md#derirun3)

??? abstract "Abstract"
	
	This paper describes the work carried out by DERI for the Enterprise Search track at TREC 2008. We participated in both the expert search task and document search task of the track. For both tasks we made use of novel learned term-weighting schemes. For the expert search task, we used two different approaches (namely a profiling approach and a two-stage document centric approach). We found that the document centric approach outperforms the profiling approach on previous years TREC data. For the document search task we adopted a standard retrieval framework and made use of the learned term-weighting schemes previously developed for the ad hoc retrieval task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CumminsO08.bib) "
	```
	@inproceedings{DBLP:conf/trec/CumminsO08,
		author = {Ronan Cummins and Colm O'Riordan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DERI} at {TREC} 2008 Enterprise Search Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/natu-ireland.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CumminsO08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2008: Experiments in Blog, Enterprise,  and Relevance Feedback Tracks with Terrier

_Ben He, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./enterprise/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf)

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

#### CSIR at TREC 2008 Expert Search Task: Modeling Expert Evidence  in Expertise Retrieval

_Jiepu Jiang, Wei Lu, Haozhen Zhao_

- :fontawesome-solid-user-group: **Participant:** [WHU](./enterprise/participants.md#whu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/wuhanu.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/wuhanu.ent.rev.pdf)
- :material-file-search: **Runs:** [WHU08BASE](./enterprise/runs.md#whu08base) | [WHU08RFCAN](./enterprise/runs.md#whu08rfcan) | [WHU08NOPHR](./enterprise/runs.md#whu08nophr) | [WHU08CAN](./enterprise/runs.md#whu08can)

??? abstract "Abstract"
	
	In this paper, we described our method for the expert search task in TREC 2008. First, we proposed an adaption to the language modeling method for expert search, which considers the probability of query generation separately using each kind of expert evidence (full name, abbreviated name, and email address). Current expert search models can be easily integrated into our method. Our experiments indicated that our method can make use of the ambiguous evidence in expert search (abbreviated name), which often casued a drop in effects in other methods. Besides, we also used a probabilistic measure to detect phrase in query, but it did not make better effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangLZ08.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangLZ08,
		author = {Jiepu Jiang and Wei Lu and Haozhen Zhao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CSIR} at {TREC} 2008 Expert Search Task: Modeling Expert Evidence in Expertise Retrieval},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/wuhanu.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangLZ08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Weighted PageRank: Cluster-Related Weights

_Danil Nemirovsky, Konstantin Avrachenkov_

- :fontawesome-solid-user-group: **Participant:** [inria](./enterprise/participants.md#inria)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/inria.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/inria.ent.rev.pdf)
- :material-file-search: **Runs:** [4FvfI](./enterprise/runs.md#4fvfi) | [Rkylv](./enterprise/runs.md#rkylv) | [TOmUW](./enterprise/runs.md#tomuw) | [ycbLS](./enterprise/runs.md#ycbls)

??? abstract "Abstract"
	
	PageRank is a way to rank Web pages taking into account hyper-link structure of the Web. PageRank provides efficient and simple method to find out ranking of Web pages exploiting hyper-link structure of the Web. However, it produces just an approximation of the ranking since the random surfer model uses just uniform distributions for all situation of choice happening during the surf process. In particular, this implies that the random surfer has no preferences. The assumption is limited by its nature. Personalized PageRank was designed to solve the problem but it is still quite restrictive since it assumes non-uniform preferences just at jumping to arbitrary page on the Web and non-preferring behaviour when following outgoing hyper-links. Taking into account these limitations and restrictions of PageRank and Personalized PageRank we propose Weighted PageRank where we are free to weight hyper-links according any possible preferring behaviour of a user. In particular, cluster-related weights are considered.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NemirovskyA08.bib) "
	```
	@inproceedings{DBLP:conf/trec/NemirovskyA08,
		author = {Danil Nemirovsky and Konstantin Avrachenkov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Weighted PageRank: Cluster-Related Weights},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/inria.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NemirovskyA08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Word Importance Discrimination Using Context Information

_Danil Nemirovsky, Vladimir Dobrynin_

- :fontawesome-solid-user-group: **Participant:** [st.petersburg](./enterprise/participants.md#st.petersburg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/st.petersburg.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/st.petersburg.ent.rev.pdf)
- :material-file-search: **Runs:** [8T0eZ](./enterprise/runs.md#8t0ez) | [Krcy7](./enterprise/runs.md#krcy7) | [U2LwQ](./enterprise/runs.md#u2lwq) | [xLQOW](./enterprise/runs.md#xlqow)

??? abstract "Abstract"
	
	Word importance discrimination is a task deserving attention when one treats a topic from TREC where a topic is quite long. The goal of the process is to estimate importance of words which carry any (additional) information about user information needs. In our experiments we estimated word importance using context information of a word.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NemirovskyD08.bib) "
	```
	@inproceedings{DBLP:conf/trec/NemirovskyD08,
		author = {Danil Nemirovsky and Vladimir Dobrynin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Word Importance Discrimination Using Context Information},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/st.petersburg.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NemirovskyD08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Blind Relevance Feedback with Wikipedia: Enterprise Track

_Yefei Peng, Ming Mao_

- :fontawesome-solid-user-group: **Participant:** [sebir](./enterprise/participants.md#sebir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/yahoo.ent.NEW.pdf](http://trec.nist.gov/pubs/trec17/papers/yahoo.ent.NEW.pdf)
- :material-file-search: **Runs:** [TitExpBrf57](./enterprise/runs.md#titexpbrf57) | [TitExp](./enterprise/runs.md#titexp) | [TitBrf](./enterprise/runs.md#titbrf) | [TitDes](./enterprise/runs.md#titdes)

??? abstract "Abstract"
	
	In this year's Enterprise track experiment, we focused on testing Blind Relevance Feedback, especially using online Wikipedia as query expansion collection. We demonstrated that using Wikipedia as query expansion collection returns better infNDCG than not using it.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PengM08.bib) "
	```
	@inproceedings{DBLP:conf/trec/PengM08,
		author = {Yefei Peng and Ming Mao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Blind Relevance Feedback with Wikipedia: Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/yahoo.ent.NEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PengM08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Universities of Avignon and Lyon III at TREC 2008: Enterprise  Track

_Eric SanJuan, Nicolas Flavier, Patrice Bellot, Fidelia Ibekwe-Sanjuan_

- :fontawesome-solid-user-group: **Participant:** [lia-talne](./enterprise/participants.md#lia-talne)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uavignon.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uavignon.ent.rev.pdf)
- :material-file-search: **Runs:** [LiaIndriMan](./enterprise/runs.md#liaindriman) | [LIAIndriSiac](./enterprise/runs.md#liaindrisiac) | [LiaIcAuto](./enterprise/runs.md#liaicauto) | [LiaIIcAuto](./enterprise/runs.md#liaiicauto) | [LiaExp08](./enterprise/runs.md#liaexp08) | [LiaIcExp08](./enterprise/runs.md#liaicexp08)

??? abstract "Abstract"
	
	The Enterprise track of TREC 2008 comprised of the same two tasks as in the previous years: an ad-hoc document search and an expert search. The document search consisted in retrieving documents that best matched real-life queries submitted by users to the CSIRO corporation. Systems were allowed to retrieve and rank up to a 1000 documents. The expert search consisted in locating the CSIRO staff who is best able to re- spond to the query formulated by the users. This year was our first participation in TREC-ENT. We explored three major approaches to information retrieval using various existing methods and systems. These approaches ranged from domain knowledge mapping [2] to QA [1].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SanJuanFBI08.bib) "
	```
	@inproceedings{DBLP:conf/trec/SanJuanFBI08,
		author = {Eric SanJuan and Nicolas Flavier and Patrice Bellot and Fidelia Ibekwe{-}Sanjuan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Universities of Avignon and Lyon {III} at {TREC} 2008: Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uavignon.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SanJuanFBI08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Twente at the TREC 2008 Enterprise Track: Using the  Global Web as an Expertise Evidence Source

_Pavel Serdyukov, Robin Aly, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [utwentedb](./enterprise/participants.md#utwentedb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/utwente.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/utwente.ent.rev.pdf)

??? abstract "Abstract"
	
	This paper describes the details of our participation in expert search task of the TREC 2007 Enterprise track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SerdyukovAH08.bib) "
	```
	@inproceedings{DBLP:conf/trec/SerdyukovAH08,
		author = {Pavel Serdyukov and Robin Aly and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Twente at the {TREC} 2008 Enterprise Track: Using the Global Web as an Expertise Evidence Source},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/utwente.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SerdyukovAH08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Research on Enterprise Track of TREC 2008

_Huawei Shen, Lei Wang, Wenjing Bi, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [I3S_Group_of_ICT](./enterprise/participants.md#i3s_group_of_ict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/cas-ict.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/cas-ict.ent.rev.pdf)
- :material-file-search: **Runs:** [ICTI3Sdoc01](./enterprise/runs.md#icti3sdoc01) | [ICTI3Sdoc02](./enterprise/runs.md#icti3sdoc02) | [ICTI3Sdoc04](./enterprise/runs.md#icti3sdoc04) | [ICTI3Sdoc03](./enterprise/runs.md#icti3sdoc03) | [ICTI3Sexp01](./enterprise/runs.md#icti3sexp01) | [ICTI3Sexp02](./enterprise/runs.md#icti3sexp02) | [ICTI3Sexp04](./enterprise/runs.md#icti3sexp04) | [ICTI3Sexp03](./enterprise/runs.md#icti3sexp03)

??? abstract "Abstract"
	
	This is the third year that we (ICT-CAS team) participated in the Enterprise Track of TREC. The track of this year includes two tasks, being document search task and expert search task. As to the document search task, we compare two retrieval models, namely BM25 model and language model. As to the expert search task, we focus on the authority of persons by exploring the persons' recommendation network constructed from their associated documents. What's more, we investigate the effectiveness of query expansion on both tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShenWBLC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShenWBLC08,
		author = {Huawei Shen and Lei Wang and Wenjing Bi and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Research on Enterprise Track of {TREC} 2008},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/cas-ict.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShenWBLC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2008: Enterprise Track

_Mingfang Wu, Falk Scholer, Steven Garcia_

- :fontawesome-solid-user-group: **Participant:** [rmit](./enterprise/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/rmit.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/rmit.ent.rev.pdf)
- :material-file-search: **Runs:** [RmitDocQ](./enterprise/runs.md#rmitdocq) | [RmitDQRerank](./enterprise/runs.md#rmitdqrerank) | [RmitDQCombLO](./enterprise/runs.md#rmitdqcomblo) | [RmitDQExp](./enterprise/runs.md#rmitdqexp)

??? abstract "Abstract"
	
	RMIT participated in the 2008 Enterprise Track document search task. Our experiments investigated the use of local outdegree, and whether this can improve the ranking quality of a search result list. Unlike global outdegree, which counts the number of out-links of a page that point to any other pages in a collection, local outdegree only counts the out-links that point to pages contained in a search result list. Intuitively, restricting the outdegree to the result set of a query transforms this source of evidence from something general into a topically-focused source of information, and may help to reduce the problem of topic shift. For our experiments, we used the Zettair search engine1 to index and search the CSIRO collection used for the 2008 Enterprise Track. This collection is a crawl of the the public-facing web of the Australian Commonwealth Scientific and Industrial Research Organization (CSIRO) in 2007 (Bailey et al., 2007). Document weights were calculated using the Okapi BM25 similarity function (Sparck Jones et al., 2000), with query words being terms from the query fields of the track topics. During indexing and search, words are stemmed and stopped.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuSG08.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuSG08,
		author = {Mingfang Wu and Falk Scholer and Steven Garcia},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2008: Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/rmit.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuSG08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2008: Enterprise Track

_Yufei Xue, Tong Zhu, Guichun Hua, Min Zhang, Yiqun Liu, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [THUIR](./enterprise/participants.md#thuir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/tsinghua.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/tsinghua.ent.rev.pdf)
- :material-file-search: **Runs:** [THUFmfS](./enterprise/runs.md#thufmfs) | [THUFS](./enterprise/runs.md#thufs) | [THUFaAS](./enterprise/runs.md#thufaas) | [THUFsimAncL](./enterprise/runs.md#thufsimancl) | [THUPDDSwp](./enterprise/runs.md#thupddswp) | [THUPDDlchrS](./enterprise/runs.md#thupddlchrs) | [THUPDDlcS](./enterprise/runs.md#thupddlcs) | [THUPDDSlL](./enterprise/runs.md#thupddsll)

??? abstract "Abstract"
	
	We participate in document search and expert search of Enterprise Track in TREC2008. The corpus and tasks are same as the year before. Different from TREC 2007, the topics come from CSIRO Enquiries, and the topic statements are richer and more colloquial.. In document search, we look into the key resource page pre-selection, the use of anchor text, query classification, and multi-field search. In expert search, we develop methods to detect expert identifiers and experimented based on our previous PDD (personal description documents) model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XueZHZLM08.bib) "
	```
	@inproceedings{DBLP:conf/trec/XueZHZLM08,
		author = {Yufei Xue and Tong Zhu and Guichun Hua and Min Zhang and Yiqun Liu and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2008: Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/tsinghua.ent.rev.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/XueZHZLM08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Role Determination and Expert Mining in the Enterprise Environment

_Jing Yao, Jun Xu, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [wim-lab.fudan](./enterprise/participants.md#wim-lab.fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/fudanu.ent.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/fudanu.ent.rev.pdf)
- :material-file-search: **Runs:** [FDUBase](./enterprise/runs.md#fdubase) | [FDUExpand](./enterprise/runs.md#fduexpand) | [FDUEmail](./enterprise/runs.md#fduemail) | [FDUUrl](./enterprise/runs.md#fduurl) | [FDUExpBase](./enterprise/runs.md#fduexpbase) | [FDUExpRole](./enterprise/runs.md#fduexprole) | [FDUExpRes](./enterprise/runs.md#fduexpres) | [FDURoleRes](./enterprise/runs.md#fduroleres)

??? abstract "Abstract"
	
	In real world, expert search is not just only name matching. Since each kind of people has their own features, we try two methods to judge whether the person we have found is more likely to be an expert. One method is to determine the role of a person by the context of the pages; the other is to judge the authority of a person by the forms of pages where he appears considering the structure of the Intranet. The evaluation results show these new methodologies have been helpful to improve the performance of the expert search on TREC 08 queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YaoXN08.bib) "
	```
	@inproceedings{DBLP:conf/trec/YaoXN08,
		author = {Jing Yao and Jun Xu and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Role Determination and Expert Mining in the Enterprise Environment},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/fudanu.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YaoXN08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University College London at TREC 2008 Enterprise Track

_Jianhan Zhu_

- :fontawesome-solid-user-group: **Participant:** [UCL](./enterprise/participants.md#ucl)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/ucollege-london.ent.NEW.pdf](http://trec.nist.gov/pubs/trec17/papers/ucollege-london.ent.NEW.pdf)
- :material-file-search: **Runs:** [ucl01](./enterprise/runs.md#ucl01) | [ucl02](./enterprise/runs.md#ucl02) | [ucl03](./enterprise/runs.md#ucl03) | [ucl04](./enterprise/runs.md#ucl04) | [UCLex01](./enterprise/runs.md#uclex01) | [UCLex02](./enterprise/runs.md#uclex02) | [UCLex03](./enterprise/runs.md#uclex03) | [UCLex04](./enterprise/runs.md#uclex04)

??? abstract "Abstract"
	
	The University College London Information Retrieval Group participated in both the Expert Search and Document Search tasks in the TREC2008 Enterprise Track. We used a generic two-stage approach, which consists of a document retrieval stage followed by an expert association discovery stage, for expert finding. Since document search is an integral part of our expert finding approach, we have studied the relationship between document search and expert search. Due to the existence of rich features that can potentially contribute to expert finding, our expert finding approach integrates these features including anchor texts, indegree, and multiple levels of associations between experts and query terms. Our experimental results show that the introduction of features has helped improve the expert finding performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zhu08.bib) "
	```
	@inproceedings{DBLP:conf/trec/Zhu08,
		author = {Jianhan Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University College London at {TREC} 2008 Enterprise Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/ucollege-london.ent.NEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Zhu08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Legal 

#### Overview of the TREC 2008 Legal Track

_Douglas W. Oard, Björn Hedin, Stephen Tomlinson, Jason R. Baron_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/LEGAL.OVERVIEW08.pdf](http://trec.nist.gov/pubs/trec17/papers/LEGAL.OVERVIEW08.pdf)
??? abstract "Abstract"
	
	TREC 2008 was the third year of the Legal Track, which focuses on evaluation of search technology for discovery of electronically stored information in litigation and regulatory settings. The track included three tasks: Ad Hoc (i.e., single-pass automatic search), Relevance Feedback (two-pass search in a controlled setting with some relevant and nonrelevant documents manually marked after the first pass) and Interactive (in which real users could iteratively refine their queries and/or engage in multi-pass relevance feedback). This paper describes the design of the three tasks and presents the official results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardHTB08.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardHTB08,
		author = {Douglas W. Oard and Bj{\"{o}}rn Hedin and Stephen Tomlinson and Jason R. Baron},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2008 Legal Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/LEGAL.OVERVIEW08.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OardHTB08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Iowa at TREC 2008 Legal and Relevance FeedbackTracks

_Brian Almquist, Yelena Mejova, Viet Ha-Thuc, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [UIowa-Srinivasan](./legal/participants.md#uiowa-srinivasan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uiowa.legal.rf.pdf](http://trec.nist.gov/pubs/trec17/papers/uiowa.legal.rf.pdf)
- :material-file-search: **Runs:** [IowaSL08Ref](./legal/runs.md#iowasl08ref) | [IowaSL0804](./legal/runs.md#iowasl0804) | [IowaSL0804b](./legal/runs.md#iowasl0804b) | [IowaSL0805](./legal/runs.md#iowasl0805) | [IowaSL0805b](./legal/runs.md#iowasl0805b) | [IowaSL0808b](./legal/runs.md#iowasl0808b) | [IowaSL0808m2](./legal/runs.md#iowasl0808m2) | [IowaSL0808m3](./legal/runs.md#iowasl0808m3) | [IowaSL08RF1B](./legal/runs.md#iowasl08rf1b) | [IowaSL08RF1A](./legal/runs.md#iowasl08rf1a) | [IowaSL08RF2B](./legal/runs.md#iowasl08rf2b) | [IowaSL08RF2A](./legal/runs.md#iowasl08rf2a) | [IowaSL08RF3B](./legal/runs.md#iowasl08rf3b) | [IowaSL08RF3A](./legal/runs.md#iowasl08rf3a) | [IowaSL08RF2C](./legal/runs.md#iowasl08rf2c) | [IowaSL08RFTr](./legal/runs.md#iowasl08rftr)

??? abstract "Abstract"
	
	The University of Iowa Team, coordinated by Padmini Srinivasan, participated in the legal discovery and relevance feedback tracks of TREC-2008. This is our second year participating in the legal track and the first year in the relevance feedback track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlmquistMHS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlmquistMHS08,
		author = {Brian Almquist and Yelena Mejova and Viet Ha{-}Thuc and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Iowa at {TREC} 2008 Legal and Relevance FeedbackTracks},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uiowa.legal.rf.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlmquistMHS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CNIPA, FUB and University of Rome "Tor Vergata" at TREC 2008 Legal  Track

_Gianni Amati, Marco Bianchi, Mauro Draoli, Alessandro Celi, Giorgio Gambosi, Giovanni Stilo_

- :fontawesome-solid-user-group: **Participant:** [WIR](./legal/participants.md#wir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/cnipa.legal.pdf](http://trec.nist.gov/pubs/trec17/papers/cnipa.legal.pdf)
- :material-file-search: **Runs:** [CTFggeBkBr0](./legal/runs.md#ctfggebkbr0) | [CTFggeSkBr0](./legal/runs.md#ctfggeskbr0) | [CTFrtSk](./legal/runs.md#ctfrtsk) | [CTFrtSkBr0](./legal/runs.md#ctfrtskbr0) | [CTFgge10kBr0](./legal/runs.md#ctfgge10kbr0) | [CTFgge4kBr0](./legal/runs.md#ctfgge4kbr0) | [CTFggeRkBr0](./legal/runs.md#ctfggerkbr0) | [CTFggeBkBr1](./legal/runs.md#ctfggebkbr1)

??? abstract "Abstract"
	
	The TREC Legal track was introduced in TREC 2006 with the claimed purpose of to evaluate the efficacy of automated support for review and production of electronic records in the context of litigation, regulation and legislation. The TREC Legal track 2008 runs three tasks: (1) an automatic ad hoc task, (2) an automatic relevance feedback task, and (3) an interactive task. We have only taken part in the automatic ad hoc task of the TREC Legal track 2008, and focused on the following issues: 1. Indexing. The CDIP test collection is characterized by an large number of unique terms due to OCR mistakes. We have defined a term selection strategy to reduce the number of terms, as described in Section 2. 2. Querying. The analysis of the past TREC results for the Legal track showed that the best retrieval strategy basically returned a ranked list of the boolean retrieved documents. As a consequence, we have defined a strategy aimed to boost the score of documents satisfying the final negotiated boolean query. Furthermore, we defined a method for automatic construction of a weighted query from the request text, as reported in Section 3. 3. Estimation of the K value. We have used a query performance prediction approach to try to estimate K values. The query weighting model that we have adopted is described in Section 4. Submitted runs and their evaluation are reported in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiBDCGS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiBDCGS08,
		author = {Gianni Amati and Marco Bianchi and Mauro Draoli and Alessandro Celi and Giorgio Gambosi and Giovanni Stilo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {CNIPA, {FUB} and University of Rome "Tor Vergata" at {TREC} 2008 Legal Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/cnipa.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiBDCGS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Where to Stop Reading a Ranked List?

_Avi Arampatzis, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./legal/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uamsterdam-kamps.legal.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uamsterdam-kamps.legal.rev.pdf)
- :material-file-search: **Runs:** [xk](./legal/runs.md#xk) | [uvabase](./legal/runs.md#uvabase) | [xconst](./legal/runs.md#xconst) | [xb](./legal/runs.md#xb)

??? abstract "Abstract"
	
	We document our participation in the TREC 2008 Legal Track. This year we focused solely on selecting rank cut-offs for optimizing the given evaluation measure per topic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ArampatzisK08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ArampatzisK08,
		author = {Avi Arampatzis and Jaap Kamps},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Where to Stop Reading a Ranked List?},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uamsterdam-kamps.legal.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ArampatzisK08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### H5 at TREC 2008 Legal Interactive: User Modeling, Assessment &  Measurement

_Christopher Hogan, Dan Brassil, Shana M. Rugani, Jennifer Reinhart, Misti Gerber, Teresa Jade_

- :fontawesome-solid-user-group: **Participant:** [H5_2008](./legal/participants.md#h5_2008)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/h5.legal.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/h5.legal.rev.pdf)
- :material-file-search: **Runs:** [H52008](./legal/runs.md#h52008)

??? abstract "Abstract"
	
	Treating the information retrieval task as one of classification has been shown to be the most effective way to achieve high performance on a particular task. In this paper, we describe a hybrid human-computer system that addresses the problem of achieving high performance on IR tasks by systematically and replicably creating large numbers of document assessments. We demonstrate how User Modeling, Document Assessment and Measurement combine to provide a shared understanding of relevance, a means for representing that understanding to an automated system, and a mechanism for iterating and correcting such a system so as to converge on a desired result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HoganBRRGJ08.bib) "
	```
	@inproceedings{DBLP:conf/trec/HoganBRRGJ08,
		author = {Christopher Hogan and Dan Brassil and Shana M. Rugani and Jennifer Reinhart and Misti Gerber and Teresa Jade},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{H5} at {TREC} 2008 Legal Interactive: User Modeling, Assessment {\&} Measurement},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/h5.legal.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HoganBRRGJ08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Distributed EDLSI, BM25, and Power Norm at TREC 2008

_April Kontostathis, Andrew Lilly, Raymond J. Spiteri_

- :fontawesome-solid-user-group: **Participant:** [Ursinus_College](./legal/participants.md#ursinus_college)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/ursinus-college.legal.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/ursinus-college.legal.rev.pdf)
- :material-file-search: **Runs:** [UrsinusBM25a](./legal/runs.md#ursinusbm25a) | [UrsinusPwrA](./legal/runs.md#ursinuspwra) | [UrsinusPwrB](./legal/runs.md#ursinuspwrb) | [UrsinusBM25b](./legal/runs.md#ursinusbm25b) | [UrsinusPwrC](./legal/runs.md#ursinuspwrc) | [UCRFBM25BL](./legal/runs.md#ucrfbm25bl) | [UCBM25T10Th5](./legal/runs.md#ucbm25t10th5) | [UCBM25T5Th5](./legal/runs.md#ucbm25t5th5) | [UrsinusVa](./legal/runs.md#ursinusva) | [UCEDLSIa](./legal/runs.md#ucedlsia) | [UCRFPwrBL](./legal/runs.md#ucrfpwrbl) | [UCEDLSIb](./legal/runs.md#ucedlsib) | [UCPwrT5Th5](./legal/runs.md#ucpwrt5th5) | [UCPwrT10Th5](./legal/runs.md#ucpwrt10th5)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC Legal competition in 2008. Our first set of experiments involved the use of Latent Semantic Indexing (LSI) with a small number of dimensions, a technique we refer to as Essential Dimensions of Latent Semantic Indexing (EDLSI). Because the experimental dataset is large, we designed a distributed version of EDLSI to use for our submitted runs. We submitted two runs using distributed EDLSI, one with k = 10 and another with k = 41, where k is the dimensionality reduction parameter for LSI. We also submitted a traditional vector space baseline for comparison with the EDLSI results. This article describes our experimental design and the results of these experiments. We find that EDLSI clearly outperforms traditional vector space retrieval using a variety of TREC reporting metrics. We also describe experiments that were designed as a followup to our TREC Legal 2007 submission. These experiments test weighting and normalization schemes as well as techniques for relevance feedback. Our primary intent was to compare the BM25 weighting scheme to our power normalization technique. BM25 outperformed all of our other submissions on the competition metric (F1 at K) for both the ad hoc and relevance feedback tasks, but Power normalization outperformed BM25 in our ad hoc experiments when the 2007 metric (estimated recall at B) was used for comparison.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KontostathisLS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/KontostathisLS08,
		author = {April Kontostathis and Andrew Lilly and Raymond J. Spiteri},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Distributed EDLSI, BM25, and Power Norm at {TREC} 2008},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/ursinus-college.legal.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KontostathisLS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MultiText Legal Experiments at TREC 2008

_Thomas R. Lynam, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [UWIR](./legal/participants.md#uwir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uwaterloo-cormack.legal.pdf](http://trec.nist.gov/pubs/trec17/papers/uwaterloo-cormack.legal.pdf)
- :material-file-search: **Runs:** [wat1fuse](./legal/runs.md#wat1fuse) | [wat2text](./legal/runs.md#wat2text) | [wat3nobool](./legal/runs.md#wat3nobool) | [wat4fuse](./legal/runs.md#wat4fuse) | [wat5fuse](./legal/runs.md#wat5fuse) | [wat6fuse](./legal/runs.md#wat6fuse) | [wat8fuse](./legal/runs.md#wat8fuse) | [wat7fuse](./legal/runs.md#wat7fuse)

??? abstract "Abstract"
	
	Our TREC 2008 effort used fusion IR methods identical to those used for our TREC 2007 effort; in addition we used logistic regression to attempt to learn the optimal K value for the primary F1@K measure introduced at TREC 2008. We used the Wumpus search engine combining several methods that have proven successful, including cover density ranking and Okapi BM25 ranking, and combination methods. Stepwise logistic regression was used to estimate K using TREC 2007 results as training data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LynamC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/LynamC08,
		author = {Thomas R. Lynam and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MultiText Legal Experiments at {TREC} 2008},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uwaterloo-cormack.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LynamC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with the Negotiated Boolean Queries of the TREC 2008  Legal Track

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [ot](./legal/participants.md#ot)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/open-text.legal.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/open-text.legal.rev.pdf)
- :material-file-search: **Runs:** [otL08fb](./legal/runs.md#otl08fb) | [otL08frw](./legal/runs.md#otl08frw) | [otL08fbe](./legal/runs.md#otl08fbe) | [otL08rvl](./legal/runs.md#otl08rvl) | [otL08fv](./legal/runs.md#otl08fv) | [otL08rvlq](./legal/runs.md#otl08rvlq) | [otL08rv](./legal/runs.md#otl08rv) | [otRF08fb](./legal/runs.md#otrf08fb) | [otRF08F](./legal/runs.md#otrf08f) | [otRF08fbF](./legal/runs.md#otrf08fbf) | [otRF08rvl](./legal/runs.md#otrf08rvl) | [otRF08fv](./legal/runs.md#otrf08fv) | [otRF08frw](./legal/runs.md#otrf08frw) | [otL08db](./legal/runs.md#otl08db) | [otRF08FR](./legal/runs.md#otrf08fr) | [otRF08fbFR](./legal/runs.md#otrf08fbfr) | [adhocpool08](./legal/runs.md#adhocpool08)

??? abstract "Abstract"
	
	We analyze the results of several experimental runs submitted for the TREC 2008 Legal Track. In the Ad Hoc task, we found that rank-based merging of vector results with the reference Boolean results produced a statistically significant increase in mean F1@K and Recall@B compared to just using the reference Boolean results. In the Relevance Feedback task, we found that the investigated relevance feedback technique, when merged with the reference Boolean results, produced some substantial increases in Recall@Br without any substantial decreases on individual topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson08.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson08,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with the Negotiated Boolean Queries of the {TREC} 2008 Legal Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/open-text.legal.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion for Noisy Legal Documents

_Lidan Wang, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMCP](./legal/participants.md#umcp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/umd-cp.legal.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/umd-cp.legal.rev.pdf)
- :material-file-search: **Runs:** [UMDSTD](./legal/runs.md#umdstd) | [UMDCRP3](./legal/runs.md#umdcrp3) | [UMDAURCP3](./legal/runs.md#umdaurcp3) | [UMDAURCC40](./legal/runs.md#umdaurcc40) | [UMDCRC40](./legal/runs.md#umdcrc40)

??? abstract "Abstract"
	
	The vocabulary of the TREC Legal OCR collection is noisy and huge. Standard techniques for improving retrieval performance such as content-based query expansion are ineffective for such document collection. In our work, we focused on exploiting metadata using blind relevance feedback, iterative improvement from the reference Boolean run, and the effects of using terms from different topic fields for automatic query formulation. This paper describes our methodologies and results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangO08.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangO08,
		author = {Lidan Wang and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Query Expansion for Noisy Legal Documents},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/umd-cp.legal.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangO08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2008 at the University at Buffalo: Legal and Blog Track

_Jianqiang Wang, Ying Sun, Omar Mukhtar, Rohini K. Srihari_

- :fontawesome-solid-user-group: **Participant:** [SUNY_Buffalo](./legal/participants.md#suny_buffalo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/suny-buffalo.legal.blog.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/suny-buffalo.legal.blog.rev.pdf)
- :material-file-search: **Runs:** [ublegal08](./legal/runs.md#ublegal08)

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

#### Pitt@TREC08: An Initial Study of Collaborative Information Behavior  in E-Discovery

_Zhen Yue, Jon Walker, Yi-Ling Lin, Daqing He_

- :fontawesome-solid-user-group: **Participant:** [Pitt_IR_Team](./legal/participants.md#pitt_ir_team)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/upittsburgh.legal.pdf](http://trec.nist.gov/pubs/trec17/papers/upittsburgh.legal.pdf)
- :material-file-search: **Runs:** [PittSIST1](./legal/runs.md#pittsist1)

??? abstract "Abstract"
	
	The University of Pittsburgh team participated in the interactive task of Legal Track in TREC 2008. We designed an experiment to investigate into the collaborative information behavior (CIB) of the group of people working on e-discovery task provided by Legal Track in TREC 2008. Through the study, we identified three major characteristics of CIB in e-discovery. 1) Frequent communication among participants 2) division of labor is common; and 3) “awareness” is important among participants. Based on these insights, we also propose a set of essential technologies and functions for retrieval systems that support CIB.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YueWLH08.bib) "
	```
	@inproceedings{DBLP:conf/trec/YueWLH08,
		author = {Zhen Yue and Jon Walker and Yi{-}Ling Lin and Daqing He},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pitt@TREC08: An Initial Study of Collaborative Information Behavior in E-Discovery},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/upittsburgh.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YueWLH08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2008: Legal Track

_Ying Zhang, Falk Scholer, Andrew Turpin_

- :fontawesome-solid-user-group: **Participant:** [rmit](./legal/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/rmit.legal.pdf](http://trec.nist.gov/pubs/trec17/papers/rmit.legal.pdf)
- :material-file-search: **Runs:** [RMITrp2](./legal/runs.md#rmitrp2) | [RMITrp3](./legal/runs.md#rmitrp3) | [RMITbp3](./legal/runs.md#rmitbp3) | [RMITbp2](./legal/runs.md#rmitbp2) | [RMITbp1](./legal/runs.md#rmitbp1) | [RMITrp1](./legal/runs.md#rmitrp1)

??? abstract "Abstract"
	
	This paper reports on the participation of RMIT university in the 2008 TREC Legal Track Ad Hoc task. OCR errors can corrupt the document view formed by an information retrieval system, and substantially hinder the successful retrieval of relevant documents for user queries. In previous research, the presence of errors in OCR text was observed to lead to unstable and unpredictable retrieval effectiveness. In this study, we investigate the effects of OCR error minimization — through de-hyphenation of terms, and the removal of corrupted or “noise” terms — on retrieval performance. Our results indicate that removing noise terms can lead to significant savings in terms of index size.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangST08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangST08,
		author = {Ying Zhang and Falk Scholer and Andrew Turpin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2008: Legal Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/rmit.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangST08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Relevance Feedback 

#### Relevance Feedback Track Overview: TREC 2008

_Chris Buckley, Stephen Robertson_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec17/papers/REL.FDBK.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec17/papers/REL.FDBK.OVERVIEW.pdf)
??? abstract "Abstract"
	
	Relevance Feedback has been one of the successes of information retrieval research for the past 30 years. It has been proven to be worthwhile in a wide variety of settings, both when actual user feedback is available, and when the user feedback is implicit. However, while the applications of relevance feedback and type of user input to relevance feedback have changed over the years, the actual algorithms have not changed much. Most algorithms are either pure statistical word based (for example, Rocchio or Language Modeling), or are domain dependent. We should be able to do better now, but there have been surprisingly few advances in the area. In part, that's because relevance feedback is hard to study, evaluate, and compare. It is difficult to separate out the effects of an initial retrieval run, the decision procedure to determine what documents will be looked at, the user dependent relevance judgment procedure (including interface), and the actual relevance feedback reformulation algorithm. Setting up a framework to look at these separate effects for future research is an important goal for this track. Why now? We have a lot more natural language tools than we had 10 or 20 years ago. We're hopeful we can get people to actually use those tools to suggest what makes a document relevant or non-relevant to a particular topic. The question-answering community has been very successful at categorizing questions and taking different approaches for different categories. The success has not transferred over to the IR task, partly because there simply isn't enough syntactic information in a typical IR topic to offer clues as to what is wanted. But given relevant and non-relevant judgments, it should be much easier to form categories for topics (e.g., this topic requires these two aspects to both be present, while this other topic does not), and take different approaches depending on topic. Relevance feedback is an area that's ripe for major advances, and is being held back because there isn't a common methodology for investigating and comparing relevance feedback algorithms. This track establishes that methodology, and offers groups the ability to evaluate and compare their relevance feedback algorithms.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyR08.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyR08,
		author = {Chris Buckley and Stephen Robertson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Relevance Feedback Track Overview: {TREC} 2008},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {https://trec.nist.gov/pubs/trec17/papers/REL.FDBK.OVERVIEW.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyR08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Iowa at TREC 2008 Legal and Relevance FeedbackTracks

_Brian Almquist, Yelena Mejova, Viet Ha-Thuc, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [UIowa-Srinivasan](./relfdbk/participants.md#uiowa-srinivasan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uiowa.legal.rf.pdf](http://trec.nist.gov/pubs/trec17/papers/uiowa.legal.rf.pdf)
- :material-file-search: **Runs:** [IowaSRF08.A1](./relfdbk/runs.md#iowasrf08.a1) | [IowaSRF08.B1](./relfdbk/runs.md#iowasrf08.b1) | [IowaSRF08.C1](./relfdbk/runs.md#iowasrf08.c1) | [IowaSRF08.D1](./relfdbk/runs.md#iowasrf08.d1) | [IowaSRF08.E1](./relfdbk/runs.md#iowasrf08.e1)

??? abstract "Abstract"
	
	The University of Iowa Team, coordinated by Padmini Srinivasan, participated in the legal discovery and relevance feedback tracks of TREC-2008. This is our second year participating in the legal track and the first year in the relevance feedback track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlmquistMHS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlmquistMHS08,
		author = {Brian Almquist and Yelena Mejova and Viet Ha{-}Thuc and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Iowa at {TREC} 2008 Legal and Relevance FeedbackTracks},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uiowa.legal.rf.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlmquistMHS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FUB at TREC 2008 Relevance Feedback Track: Extending Rocchio with  Distributional Term Analysis

_Andrea Bernardini, Claudio Carpineto_

- :fontawesome-solid-user-group: **Participant:** [fub](./relfdbk/participants.md#fub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/fondazione.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/fondazione.rf.rev.pdf)
- :material-file-search: **Runs:** [FubRF08.A1](./relfdbk/runs.md#fubrf08.a1) | [FubRF08.B1](./relfdbk/runs.md#fubrf08.b1) | [FubRF08.D1](./relfdbk/runs.md#fubrf08.d1) | [FubRF08.E1](./relfdbk/runs.md#fubrf08.e1) | [FubRF08.C1](./relfdbk/runs.md#fubrf08.c1) | [FubRF08.A2](./relfdbk/runs.md#fubrf08.a2) | [FubRF08.E2](./relfdbk/runs.md#fubrf08.e2) | [FubRF08.C2](./relfdbk/runs.md#fubrf08.c2) | [FubRF08.D2](./relfdbk/runs.md#fubrf08.d2)

??? abstract "Abstract"
	
	The main goals of our participation in the Relevance feedback track at TREC 2008 were the following. Test the effectiveness of using a combination of Rocchio and distributional term analysis on a relevance feedback task; so far, this approach has usually been used (with good results) in a pseudo-relevance setting.; Test whether and when negative relevance feedback is useful; e.g., is negative relevance feedback most effective when the distribution of terms in the negative documents is different than the distribution in the positive documents?; Study how the performance of relevance feedback varies as the size of the set of feedback documents grows.; Check if /how the performance of relevance feedback is influenced by the size of the expanded query.; Compare relevance feedback to pseudo-relevance feedback; e.g, is relevance feedback not only more effective but also more robust than pseudo-relevance feedback?
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BernardiniC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/BernardiniC08,
		author = {Andrea Bernardini and Claudio Carpineto},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FUB} at {TREC} 2008 Relevance Feedback Track: Extending Rocchio with Distributional Term Analysis},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/fondazione.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BernardiniC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2008 Blog Track

_Jianmei Chen, Wei Guo, Fengming Pan, Fuyang Chang, Rui Song, Hongfei Lin_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./relfdbk/participants.md#dutir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/dalianu.rf.pdf](http://trec.nist.gov/pubs/trec17/papers/dalianu.rf.pdf)
- :material-file-search: **Runs:** [DUTIRRF08.A1](./relfdbk/runs.md#dutirrf08.a1) | [DUTIRRF08.B1](./relfdbk/runs.md#dutirrf08.b1) | [DUTIRRF08.C1](./relfdbk/runs.md#dutirrf08.c1) | [DUTIRRF08.D1](./relfdbk/runs.md#dutirrf08.d1) | [DUTIRRF08.E1](./relfdbk/runs.md#dutirrf08.e1)

??? abstract "Abstract"
	
	For opinion finding task our method of the combination of 5 Windows method and Pseudo Relevance Feedback behaves well, achieving an improvement of over 20% on the baseline adhoc results. For the polarity task we develop two different methods. One is a classification method, and the other uses queries to retrieve positive and negative documents respectively. In Blog Distillation task, Pseudo Relevance Feedback method helps improve the result a little, however, since its dependence on the top 10 retrieval result, the method still need to be improved in order to get better result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenGPCSL08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenGPCSL08,
		author = {Jianmei Chen and Wei Guo and Fengming Pan and Fuyang Chang and Rui Song and Hongfei Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2008 Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/dalianu.rf.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenGPCSL08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2008: Experiments in Blog, Enterprise,  and Relevance Feedback Tracks with Terrier

_Ben He, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [UoGtr](./relfdbk/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf)
- :material-file-search: **Runs:** [uogRF08.A2](./relfdbk/runs.md#uogrf08.a2) | [uogRF08.B2](./relfdbk/runs.md#uogrf08.b2) | [uogRF08.C2](./relfdbk/runs.md#uogrf08.c2) | [uogRF08.B1](./relfdbk/runs.md#uogrf08.b1) | [uogRF08.C1](./relfdbk/runs.md#uogrf08.c1) | [uogRF08.E2](./relfdbk/runs.md#uogrf08.e2) | [uogRF08.D2](./relfdbk/runs.md#uogrf08.d2) | [uogRF08.D1](./relfdbk/runs.md#uogrf08.d1) | [uogRF08.E1](./relfdbk/runs.md#uogrf08.e1) | [uogRF08.A1](./relfdbk/runs.md#uogrf08.a1)

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

#### The Impact of Positive, Negative and Topical Relevance Feedback

_Rianne Kaptein, Jaap Kamps, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./relfdbk/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uamsterdam-kapms.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uamsterdam-kapms.rf.rev.pdf)
- :material-file-search: **Runs:** [UAmsR08PD.A1](./relfdbk/runs.md#uamsr08pd.a1) | [UAmsR08PD.B1](./relfdbk/runs.md#uamsr08pd.b1) | [UAmsR08PD.C1](./relfdbk/runs.md#uamsr08pd.c1) | [UAmsR08PD.D1](./relfdbk/runs.md#uamsr08pd.d1) | [UAmsR08PD.E1](./relfdbk/runs.md#uamsr08pd.e1) | [UAmsR08PD.F1](./relfdbk/runs.md#uamsr08pd.f1) | [UAmsR08CJ.B2](./relfdbk/runs.md#uamsr08cj.b2) | [UAmsR08CJ.C2](./relfdbk/runs.md#uamsr08cj.c2) | [UAmsR08CJ.D2](./relfdbk/runs.md#uamsr08cj.d2) | [UAmsR08CJ.E2](./relfdbk/runs.md#uamsr08cj.e2)

??? abstract "Abstract"
	
	This document contains a description of experiments for the 2008 Relevance Feedback track. We experiment with different amounts of feedback, including negative relevance feedback. Feedback is implemented using massive weighted query expansion. Parsimonious query expansion using only relevant documents and Jelinek-Mercer smoothing performs best on this relevance feedback track dataset. Additional blind feedback gives better results, except when the blind feedback set is of the same size as the explicit feedback set. On a small number of topics topical feedback is applied, which turns out to be mainly beneficial for early precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KapteinKH08.bib) "
	```
	@inproceedings{DBLP:conf/trec/KapteinKH08,
		author = {Rianne Kaptein and Jaap Kamps and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Impact of Positive, Negative and Topical Relevance Feedback},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uamsterdam-kapms.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KapteinKH08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Incorporating Relevance and Pseudo-relevance Feedback in the Markov  Random Field Model

_Matthew Lease_

- :fontawesome-solid-user-group: **Participant:** [Brown_University](./relfdbk/participants.md#brown_university)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/brownu.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/brownu.rf.rev.pdf)
- :material-file-search: **Runs:** [Brown.A1](./relfdbk/runs.md#brown.a1) | [Brown.B1](./relfdbk/runs.md#brown.b1) | [Brown.E1](./relfdbk/runs.md#brown.e1) | [Brown.C1](./relfdbk/runs.md#brown.c1) | [Brown.D1](./relfdbk/runs.md#brown.d1) | [Brown.A2](./relfdbk/runs.md#brown.a2) | [Brown.B2](./relfdbk/runs.md#brown.b2) | [Brown.C2](./relfdbk/runs.md#brown.c2) | [Brown.D2](./relfdbk/runs.md#brown.d2)

??? abstract "Abstract"
	
	We present a new document retrieval approach combining relevance feedback, pseudo-relevance feedback, and Markov random field modeling of term interaction. Overall effectiveness of our combined model and the relative contribution from each component is evaluated on the GOV2 webpage collection. Given 0-5 feedback documents, we find each component contributes unique value to the overall ensemble, achieving significant improvement individually and in combination. Comparative evaluation in the 2008 TREC Relevance Feedback track further shows our complete system typically performs as well or better than peer systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lease08.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lease08,
		author = {Matthew Lease},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Incorporating Relevance and Pseudo-relevance Feedback in the Markov Random Field Model},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/brownu.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lease08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Study of Adaptive Relevance Feedback - UIUC TREC 2008 Relevance  Feedback Experiments

_Yuanhua Lv, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [UIUC](./relfdbk/participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uillinois-uc.rf.rec.pdf](http://trec.nist.gov/pubs/trec17/papers/uillinois-uc.rf.rec.pdf)
- :material-file-search: **Runs:** [UIUC.A1](./relfdbk/runs.md#uiuc.a1) | [UIUC.B2](./relfdbk/runs.md#uiuc.b2) | [UIUC.C2](./relfdbk/runs.md#uiuc.c2) | [UIUC.B1](./relfdbk/runs.md#uiuc.b1) | [UIUC.C1](./relfdbk/runs.md#uiuc.c1) | [UIUC.D1](./relfdbk/runs.md#uiuc.d1) | [UIUC.E1](./relfdbk/runs.md#uiuc.e1) | [UIUC.E2](./relfdbk/runs.md#uiuc.e2) | [UIUC.D2](./relfdbk/runs.md#uiuc.d2)

??? abstract "Abstract"
	
	In this paper, we report our experiments in the TREC 2008 Relevance Feedback Track. Our main goal is to study a novel problem in feedback, i.e., optimization of the balance of the query and feedback information. Intuitively, if we over-trust the feedback information, we may be biased to favor a particular subset of relevant documents, but undertrusting it would not take advantage of feedback. In the cur- rent feedback methods, the balance is usually controlled by some parameter, which is often set to a fixed value across all the queries and collections. However, due to the difference in queries and feedback documents, this balance parameter should be optimized for each query and each set of feedback documents. To address this problem, we present a learning approach to adaptively predict the balance coefficient (i.e., feedback coefficient). First, three heuristics are proposed to characterize the relationships between feedback coefficient and other measures, including discrimination of query, discrimination of feedback documents, and divergence between the query and the feedback documents. Then, taking these three heuristics as a road map, we explore a number of features and combine them using a logistic regression model to predict the feedback coefficient. Experiments show that our adaptive relevance feedback is more robust and effective than the regular fixed-coefficient relevance feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LvZ08.bib) "
	```
	@inproceedings{DBLP:conf/trec/LvZ08,
		author = {Yuanhua Lv and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Study of Adaptive Relevance Feedback - {UIUC} {TREC} 2008 Relevance Feedback Experiments},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uillinois-uc.rf.rec.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LvZ08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Incorporating Non-Relevance Information in the Estimation of Query  Models

_Edgar Meij, Wouter Weerkamp, Jiyin He, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UAms_De_Rijke](./relfdbk/participants.md#uams_de_rijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.rf.rev.pdf)
- :material-file-search: **Runs:** [uams08bl.A1](./relfdbk/runs.md#uams08bl.a1) | [uams08m6.B1](./relfdbk/runs.md#uams08m6.b1) | [uams08m6.C1](./relfdbk/runs.md#uams08m6.c1) | [uams08m6.D1](./relfdbk/runs.md#uams08m6.d1) | [uams08m6.E1](./relfdbk/runs.md#uams08m6.e1) | [uams08m9.B2](./relfdbk/runs.md#uams08m9.b2) | [uams08m9.C2](./relfdbk/runs.md#uams08m9.c2) | [uams08m9.D2](./relfdbk/runs.md#uams08m9.d2) | [uams08m9.E2](./relfdbk/runs.md#uams08m9.e2) | [uams08bl.A2](./relfdbk/runs.md#uams08bl.a2)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the relevance feedback track at TREC 2008. We introduce a new model which incorporates information from relevant and non-relevant documents to improve the estimation of query models. Our main findings are twofold: (i) in terms of statMAP, a larger number of judged non-relevant documents improves retrieval effectiveness and (ii) on the TREC Terabyte topics, we can effectively replace the estimates on the judged non-relevant documents with estimations on the document collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeijWHR08.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeijWHR08,
		author = {Edgar Meij and Wouter Weerkamp and Jiyin He and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Incorporating Non-Relevance Information in the Estimation of Query Models},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MeijWHR08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2008: Relevance Feedback Track

_Yohannes Tsegay, Falk Scholer, Simon J. Puglisi_

- :fontawesome-solid-user-group: **Participant:** [rmit](./relfdbk/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/rmit.rf.pdf](http://trec.nist.gov/pubs/trec17/papers/rmit.rf.pdf)
- :material-file-search: **Runs:** [RMIT08.A1](./relfdbk/runs.md#rmit08.a1) | [RMIT08.B1](./relfdbk/runs.md#rmit08.b1) | [RMIT08.C1](./relfdbk/runs.md#rmit08.c1) | [RMIT08.C2](./relfdbk/runs.md#rmit08.c2) | [RMIT08.D1](./relfdbk/runs.md#rmit08.d1) | [RMIT08.D2](./relfdbk/runs.md#rmit08.d2) | [RMIT08.E1](./relfdbk/runs.md#rmit08.e1) | [RMIT08.E2](./relfdbk/runs.md#rmit08.e2)

??? abstract "Abstract"
	
	This report outlines TREC-2008 Relevance Feedback Track experiments done at RMIT University. Relevance feedback in text retrieval systems is a process where a user gives explicit feedback on an initial set of retrieval results returned by a search system. For example, the user might mark some of the items as being relevant, or not relevant, to their current information need. This feedback can be used in different ways; one approach is query expansion, where terms from the relevant documents are added to the original query, with the aim of improving retrieval effectiveness. This report describes the the query expansion methods that we explored as part of TREC 2008. Our results demonstrate that high weight terms are not always necessarily useful for query expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TsegaySP08.bib) "
	```
	@inproceedings{DBLP:conf/trec/TsegaySP08,
		author = {Yohannes Tsegay and Falk Scholer and Simon J. Puglisi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2008: Relevance Feedback Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/rmit.rf.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TsegaySP08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluating a Novel Kind of Retrieval Models Based on Relevance Decision  Making in a Relevance Feedback Environment

_Ho Chung Wu, Edward K. F. Dang, Robert Wing Pong Luk, G. Ngai, Yinghao Li, James Allan, Kui-Lam Kwok, Kam-Fai Wong_

- :fontawesome-solid-user-group: **Participant:** [HKPU](./relfdbk/participants.md#hkpu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/hong-kong.pu.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/hong-kong.pu.rf.rev.pdf)
- :material-file-search: **Runs:** [HKPU.A1](./relfdbk/runs.md#hkpu.a1) | [HKPU.D1](./relfdbk/runs.md#hkpu.d1) | [HKPU.B1](./relfdbk/runs.md#hkpu.b1) | [HKPU.E1](./relfdbk/runs.md#hkpu.e1) | [HKPU.C1](./relfdbk/runs.md#hkpu.c1) | [HKPU.B2](./relfdbk/runs.md#hkpu.b2) | [HKPU.C2](./relfdbk/runs.md#hkpu.c2)

??? abstract "Abstract"
	
	This paper presents the results of our participation in the relevance feedback track using our novel retrieval models. These models simulate human relevance decision-making. For each document location of a query term, information from its document-context at that location determines the relevance decision outcomes there. The relevance values for all documents locations of all query terms in the same document are combined to form the final relevance value for that document. Two probabilistic models are developed, and one of them is directly related to the TF-IDF term weights. Our initial retrieval is a passage-based retrieval. Passage scores of the same document are combined by the Dombi fuzzy disjunction operator. Later, we found that the Markov random field (MRF) model produces better results than our initial retrieval system (without relevance information). If we apply our novel retrieval models using the initial retrieval list of the MRF model, the retrieval effectiveness of our models will be improved. These informal run results using the MRF model used in conjunction with our novel models are also presented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuDLNLAKW08.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuDLNLAKW08,
		author = {Ho Chung Wu and Edward K. F. Dang and Robert Wing Pong Luk and G. Ngai and Yinghao Li and James Allan and Kui{-}Lam Kwok and Kam{-}Fai Wong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Evaluating a Novel Kind of Retrieval Models Based on Relevance Decision Making in a Relevance Feedback Environment},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/hong-kong.pu.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuDLNLAKW08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Extending Relevance Model for Relevance Feedback

_Le Zhao, Chenmin Liang, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU-LTI-DIR](./relfdbk/participants.md#cmu-lti-dir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/cmu.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/cmu.rf.rev.pdf)
- :material-file-search: **Runs:** [CMURF08.A1](./relfdbk/runs.md#cmurf08.a1) | [CMURF08.B1](./relfdbk/runs.md#cmurf08.b1) | [CMURF08.C1](./relfdbk/runs.md#cmurf08.c1) | [CMURF08.D1](./relfdbk/runs.md#cmurf08.d1) | [CMURF08.D2](./relfdbk/runs.md#cmurf08.d2) | [CMURF08.C2](./relfdbk/runs.md#cmurf08.c2) | [CMURF08.B2](./relfdbk/runs.md#cmurf08.b2) | [CMURF08.E1](./relfdbk/runs.md#cmurf08.e1)

??? abstract "Abstract"
	
	Relevance feedback is the retrieval task where the system is given not only an information need, but also some relevance judgement information, usually from users' feedback for an initial result list by the system. With different amount of feedback information available, the optimal feedback strategy might be very different. In TREC Relevance Feedback task, the system is given different sets of feedback information from 1 relevant document to over 40 judgements with at least 3 relevant. Thus, in this work, we try to develop a feedback algorithm that works well on all levels of feedback by extending the relevance model for pseudo relevance feedback to include judged relevant documents when scoring feedback terms. Within these different levels of feedback, it is more difficult for the feedback algorithm to perform well when given minimal amount of feedback. Experiments show that our algorithm performs robustly in those difficult cases.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoLC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoLC08,
		author = {Le Zhao and Chenmin Liang and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Extending Relevance Model for Relevance Feedback},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/cmu.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoLC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2008: Relevance Feedback Track

_Bo Zhou, Qi Fang, Rongwei Cen, Min Zhang, Yiqun Liu, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [THUIR](./relfdbk/participants.md#thuir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/tsinghua.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/tsinghua.rf.rev.pdf)
- :material-file-search: **Runs:** [THUFB.D1](./relfdbk/runs.md#thufb.d1) | [THUFB.E1](./relfdbk/runs.md#thufb.e1) | [THUFB.A1](./relfdbk/runs.md#thufb.a1) | [THUFB.B1](./relfdbk/runs.md#thufb.b1) | [THUFB.C1](./relfdbk/runs.md#thufb.c1) | [THUFB.B2](./relfdbk/runs.md#thufb.b2) | [THUFB.D2](./relfdbk/runs.md#thufb.d2) | [THUFB.E2](./relfdbk/runs.md#thufb.e2) | [THUFB.C2](./relfdbk/runs.md#thufb.c2)

??? abstract "Abstract"
	
	Our group has participated into Relevance Feedback (RF) Track in TREC2008. In our experiments, two kinds of techniques, query expansion and search result re-ranking based on document relevance model, are adopted to improve the retrieval performance. The TMiner search engine, from IR group of Tsinghua University, is used as our text retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouFCZLM08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouFCZLM08,
		author = {Bo Zhou and Qi Fang and Rongwei Cen and Min Zhang and Yiqun Liu and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2008: Relevance Feedback Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/tsinghua.rf.rev.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhouFCZLM08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

