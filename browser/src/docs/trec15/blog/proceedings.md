# Proceedings - Blog 2006 

#### Overview of the TREC 2006 Blog Track

_Iadh Ounis, Craig Macdonald, Maarten de Rijke, Gilad Mishne, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/BLOG06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/BLOG06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The rise on the Internet of blogging, the creation of journal-like web page logs, has created a highly dynamic subset of the World Wide Web that evolves and responds to real-world events. Indeed, blogs (or weblogs) have recently emerged as a new grassroots publishing medium. The so-called blogosphere (the collection of blogs on the Internet) opens up several new interesting research areas. Blogs have many interesting features: entries are added in chronological order, sometimes at a high volume. In addition, many blogs are created by their authors, not intended for any sizable audience, but purely as a mechanism for self-expression. Extremely accessible blog software has facilitated the act of blogging to a wide-ranging audience, their blogs reflecting their opinions, philosophies and emotions. Traditional media tends to focus on “heavy-hitting” blogs devoted to politics, punditry and technology. However, there are many different genres of blogs, some written around a specific topic, some covering several, and others talking about personal daily life [3]. The Blog track began this year, with the aim to explore the information seeking behaviour in the blogosphere. For this purpose, a new large-scale test collection, namely the TREC Blog06 collection, has been created. In the first pilot run of the track in 2006, we had two tasks, a main task (opinion retrieval) and an open task. The opinion retrieval task focuses on a specific aspect of blogs: the opinionated nature of many blogs. The second task was introduced to allow participants the opportunity to influence the determination of a suitable second task (for 2007) on other aspects of blogs, such as the temporal/event-related nature of many blogs, or the severity of spam in the blogosphere. The remainder of this paper is structured as follows. Section 2 provides a short description of the newly created Blog06 test collection. Section 3 describes the opinion task, and provides an overview of the submitted runs of the participants. Section 4 describes the open task and the submitted proposals. We provide concluding remarks in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OunisMRMS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/OunisMRMS06,
		author = {Iadh Ounis and Craig Macdonald and Maarten de Rijke and Gilad Mishne and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2006 Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/BLOG06.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OunisMRMS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Blog Mining Through Opinionated Words

_Giuseppe Attardi, Maria Simi_

- :fontawesome-solid-user-group: **Participant:** [upisa.attardi](./participants.md#upisa.attardi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/upisa.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/upisa.blog.final.pdf)
- :material-file-search: **Runs:** [pisaBlDesOp6](./runs.md#pisabldesop6) | [pisaBlDes](./runs.md#pisabldes) | [pisaBlTit](./runs.md#pisabltit) | [pisaBlTitOp6](./runs.md#pisabltitop6)

??? abstract "Abstract"
	
	Intent mining is a special kind of document analysis whose goal is to assess the attitude of the document author with respect to a given subject. Opinion mining is a kind of intent mining where the attitude is a positive or negative opinion. Most systems tackle the problem with a two step approach, an information retrieval followed by a postprocess or filter phase to identify opinionated blogs. We explored a single stage approach to opinion mining, retrieving opinionated documents ranked with a special ranking function which exploits an index enriched with opinion tags. A set of subjective words are used as tags for identifying opinionated sentences. Subjective words are marked as “opinionated” and are used in the retrieval phase to boost the rank of documents containing them. In indexing the collection, we recovered the relevant content from the blog permalink pages, exploiting HTML metadata about the generator and heuristics to remove irrelevant parts from the body. The index also contains information about the occurrence of opinionated words, extracted from an analysis of WordNet glosses. The experiments compared the precision of normal queries with respect to queries which included as constraint the proximity to an opinionated word. The results show a significant improvement in precision for both topic relevance and opinion relevance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AttardiS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/AttardiS06,
		author = {Giuseppe Attardi and Maria Simi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Blog Mining Through Opinionated Words},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/upisa.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AttardiS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Robert Gordon University

_Malcolm Clark, Ulises Cerviño Beresi, Stuart N. K. Watt, David J. Harper_

- :fontawesome-solid-user-group: **Participant:** [robert-gordonu.harper](./participants.md#robert-gordonu.harper)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/robert-gordonu.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/robert-gordonu.blog.final.pdf)
- :material-file-search: **Runs:** [rguBL](./runs.md#rgubl) | [rguOPN](./runs.md#rguopn) | [rguSBJ](./runs.md#rgusbj) | [Abstract](./runs.md#abstract)

??? abstract "Abstract"
	
	Blogs are highly rich in opinion making their automatic processing appealing to marketing companies, the media, costumer centres, etc. TREC ran a Blog track in 2006 with two tasks: opinion retrieval and an open task. This document reports the experiments conducted at The Robert Gordon University (RGU) where we used Statistical Language Models combined with shallow parsing techniques for the opinion retrieval problem.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkBWH06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkBWH06,
		author = {Malcolm Clark and Ulises Cervi{\~{n}}o Beresi and Stuart N. K. Watt and David J. Harper},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Robert Gordon University},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/robert-gordonu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkBWH06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Opinion Retrieval Experiments Using Generative Models: Experiments  for the TREC 2006 Blog Track

_Koji Eguchi, Chirag Shah_

- :fontawesome-solid-user-group: **Participant:** [nii-eguchi](./participants.md#nii-eguchi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/nii.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/nii.blog.final.pdf)
- :material-file-search: **Runs:** [NII5](./runs.md#nii5) | [NII3](./runs.md#nii3) | [NII1](./runs.md#nii1) | [NII7](./runs.md#nii7) | [NII6](./runs.md#nii6) | [NIIabstract](./runs.md#niiabstract) | [NIIfinal](./runs.md#niifinal)

??? abstract "Abstract"
	
	Ranking blog posts that express opinions regarding a given topic should serve a critical function in helping users. We explored three types of opinion retrieval methods in the framework of probabilistic language models. The first method combines topic-relevance model and opinion-relevance model that captures topic dependence of the opinion expressions. The second method makes use of probability that any of opinion-bearing words appear in each target document as document prior probability in query-likelihood model. The third method makes use of probability that any of adjectives or adverbs appear in each target document as document prior probability, assuming opinionated documents tend to contain more adjectives or adverbs than other documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EguchiS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/EguchiS06,
		author = {Koji Eguchi and Chirag Shah},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Opinion Retrieval Experiments Using Generative Models: Experiments for the {TREC} 2006 Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/nii.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EguchiS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The BlogVox Opinion Retrieval System

_Akshay Java, Pranam Kolari, Timothy W. Finin, Anupam Joshi, Justin Martineau_

- :fontawesome-solid-user-group: **Participant:** [umaryland-bc.finin](./participants.md#umaryland-bc.finin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umbc-jhu.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umbc-jhu.blog.final.pdf)
- :material-file-search: **Runs:** [UABas11](./runs.md#uabas11) | [UAEX13](./runs.md#uaex13) | [UAEX21](./runs.md#uaex21) | [UAEX12](./runs.md#uaex12) | [UAEX11](./runs.md#uaex11) | [uaplabstract](./runs.md#uaplabstract) | [uaplfinal](./runs.md#uaplfinal)

??? abstract "Abstract"
	
	The BlogVox system retrieves opinionated blog posts specified by ad hoc queries. BlogVox was developed for the 2006 TREC blog track by the University of Maryland, Baltimore County and the Johns Hopkins University Applied Physics Laboratory using a novel system to recognize legitimate posts and discriminate against spam blogs. It also processes posts to eliminate extraneous non-content, including blog-rolls, link-rolls, advertisements and sidebars. After retrieving posts relevant to a topic query, the system processes them to produce a set of independent features estimating the likelihood that a post expresses an opinion about the topic. These are combined using an SVM-based system and integrated with the relevancy score to rank the results. We evaluate BlogVox's performance against human assessors. We also evaluate the individual splog filtering and non-content removal components of BlogVox.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JavaKFJM06.bib) "
	```
	@inproceedings{DBLP:conf/trec/JavaKFJM06,
		author = {Akshay Java and Pranam Kolari and Timothy W. Finin and Anupam Joshi and Justin Martineau},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The BlogVox Opinion Retrieval System},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umbc-jhu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JavaKFJM06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UALR at TREC: Blog Track

_Hemant Joshi, Coskun Bayrak, Xiaowei Xu_

- :fontawesome-solid-user-group: **Participant:** [uarkansas-littlerock.joshi](./participants.md#uarkansas-littlerock.joshi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uarkansas.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uarkansas.blog.final.pdf)
- :material-file-search: **Runs:** [UALR06m5Tr1](./runs.md#ualr06m5tr1) | [UALR06a260r2](./runs.md#ualr06a260r2) | [UALR06m260r3](./runs.md#ualr06m260r3) | [UALR06a500r4](./runs.md#ualr06a500r4) | [UALR06m500r5](./runs.md#ualr06m500r5)

??? abstract "Abstract"
	
	We consider Opinion Blog retrieval from classification point of view. We used the active learning method with an integrated feature selection to train the Support Vector Machine algorithm. We wanted to study the effect of different types of features on the classification accuracy of the model generated by the classifier algorithm. We considered mainly three different types of features for 5 runs submitted. Feature types include bag-of-words features, seed-words as features and statistical features. Bag-of-words features are generated from the actual blog data. Seed-words were manually generated specific to the domain of interest. Statistical features studied included the ratio of linguistic features to total number of words. We built models using an iterative process and studied accuracy as well as coverage of each model. Study of different features is important in order to build a better model. Feature selection algorithms can choose the best features among the available ones but different features have costs associated with them. We need features that not only predict class labels or contribute towards prediction but the feature should also be representative of the entire dataset, especially test data. Training the classifier on such features will yield better coverage and training accuracy for the model. We compared the three different models generated by three different feature generation strategies. Our preliminary results indicate that seed-words that are specific to a particular domain or particular type of classification achieve better accuracy and coverage. In general, bag-of-words features are tightly coupled with the data they represent. On the other hand, statistical features are independent of the actual words used. Statistical features are more useful in building robust models that can be used with different languages and for different tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoshiBX06.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoshiBX06,
		author = {Hemant Joshi and Coskun Bayrak and Xiaowei Xu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UALR} at {TREC:} Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uarkansas.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoshiBX06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Language Model with Sentiment Analysis for Opinion Retrieval  of Blog-Post

_Xiangwen Liao, Donglin Cao, Songbo Tan, Yue Liu, Guodong Ding, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-iiis.tan](./participants.md#cas-iiis.tan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cas-ict.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/cas-ict.blog.final.pdf)
- :material-file-search: **Runs:** [ICT](./runs.md#ict) | [IIIS](./runs.md#iiis)

??? abstract "Abstract"
	
	This paper describes our participation in Blog Opinion Retrieval task this year. We conduct experiments on “FirteX” platform that is developed by our lab. Language Model is used to retrieve related blog unit. Interactive Knowledge is adopted to expand query for retrieve blog unit include opinion. Then we introduce a novel extracting technology to extract text from retrieved blog-post. Finally, Lexicon based method is used to rerank the document by opinion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiaoCTLDC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiaoCTLDC06,
		author = {Xiangwen Liao and Donglin Cao and Songbo Tan and Yue Liu and Guodong Ding and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Language Model with Sentiment Analysis for Opinion Retrieval of Blog-Post},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cas-ict.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiaoCTLDC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Splog Detection Task and A Solution Based on Temporal and Link  Properties

_Yu-Ru Lin, Wen-Yen Chen, Xiaolin Shi, Richard Sia, Xiaodan Song, Yun Chi, Koji Hino, Hari Sundaram, Jun'ichi Tatemura, Belle L. Tseng_

- :fontawesome-solid-user-group: **Participant:** [nec-labs.tseng](./participants.md#nec-labs.tseng)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/nec.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/nec.blog.final.pdf)
- :material-file-search: **Runs:** [necabstract](./runs.md#necabstract) | [necnistfinal](./runs.md#necnistfinal)

??? abstract "Abstract"
	
	Spam blogs (splogs) have become a major problem in the increasingly popular blogosphere. Splogs are detrimental in that they corrupt the quality of information retrieved and they waste tremendous network and storage resources. We study several research issues in splog detection. First, in comparison to web spam and email spam, we identify some unique characteristics of splog. Second, we propose a new online task that captures the unique characteristics of splog, in addition to tasks based on the traditional IR evaluation framework. The new task introduces a novel time-sensitive detection evaluation to indicate how quickly a detector can identify splogs. Third, we propose a splog detection algorithm that combines traditional content features with temporal and link regularity features that are unique to blogs. Finally, we develop an annotation tool to generate ground truth on a sampled subset of the TREC-Blog dataset. We conducted experiments on both offline (traditional splog detection) and our proposed online splog detection task. Experiments based on the annotated ground truth set show excellent results on both offline and online splog detection tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinCSSSCHSTT06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinCSSSCHSTT06,
		author = {Yu{-}Ru Lin and Wen{-}Yen Chen and Xiaolin Shi and Richard Sia and Xiaodan Song and Yun Chi and Koji Hino and Hari Sundaram and Jun'ichi Tatemura and Belle L. Tseng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Splog Detection Task and {A} Solution Based on Temporal and Link Properties},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/nec.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinCSSSCHSTT06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Deep Context with a Sense-of-Self

_Robert McArthur_

- :fontawesome-solid-user-group: **Participant:** [csiro-ict.mcarthur](./participants.md#csiro-ict.mcarthur)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/csiro.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/csiro.blog.final.pdf)
- :material-file-search: **Runs:** [csirabstract](./runs.md#csirabstract) | [csirofull](./runs.md#csirofull)

??? abstract "Abstract"
	
	There is a trend in information retrieval to an increased involvement of context. The success of recent workshops at SIGIR [8] and the subsequent 2006 IIiX Symposium 1 , the SIGIR exploratory search workshop 2 , and the outcome of the 2004 SWIRL workshop 3 [21] are indicators that elements of user context are both sort and becoming available. “The provision of tools…can yield great rewards for users, especially when contextual factors such as user emotion, task constraints, and dynamism of information needs are considered” [26]. Recent weblog workshops 4 reflect a strong interest in the discovery of context about the user in the form of the blogger's age [2, 24], gender [23, 24], opinions, sentiments and opinions expressed [9, 19, 22], mood levels [1, 20], happiness [18], residential area [28] and social network(s) [6, 7, 11-13, 25]. The research concentrated on particular forms of identifying or extracting the information, providing fertile ground for TREC-style comparisons of the approaches. Considerable interest has been shown in the analysis of sentiment in weblogs ([1, 4, 18-20, 22]). This broad umbrella encompasses notions of mood, opinion, emotion and happiness. Sentiment is only one aspect of user context. Indeed, many of the published notions of sentiment derive from reflection of authorship. That is, determination of the mood, opinion or emotion comes through analysis of the artefacts of communication, the blog entry, and is deemed a reflection of the sentiment of the author at the time. Of course, the assumption is that a person's writing reflects their inner state of being. Although it is tempting to, repeating history, ignore the author and concentrate on the blog entry itself, the focus should remain on determining more about the user. To this end, more information about the user is required apart from the emphasis on the (usually) explicit manifestations of their selves. Figure 1 presents this difference by separating what we know about the document (e.g. style), what we know about the user from the document at a particular point in time (e.g. sentiment), and the more implicit and meta-information which is derived from the sentiment and which captures deeper context about the user. An example of such information is a computational manifestation of a person's sense-of-self. This has been investigated previously using mailing list records in an online health setting ([15]) and this paper uses it as an exemplar of deeper user context, showing how to apply the ideas and techniques to blog data in a TREC setting
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McArthur06.bib) "
	```
	@inproceedings{DBLP:conf/trec/McArthur06,
		author = {Robert McArthur},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Deep Context with a Sense-of-Self},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/csiro.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McArthur06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multiple Ranking Strategies for Opinion Retrieval in Blogs - The University  of Amsterdam at the 2006 TREC Blog Track

_Gilad Mishne_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.ilps](./participants.md#uamsterdam.ilps)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uamsterdam.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uamsterdam.blog.final.pdf)
- :material-file-search: **Runs:** [UAmsB06Base](./runs.md#uamsb06base) | [UAmsB06L](./runs.md#uamsb06l) | [UAmsB06S](./runs.md#uamsb06s) | [UAmsB06O](./runs.md#uamsb06o) | [UAmsB06All](./runs.md#uamsb06all)

??? abstract "Abstract"
	
	We describe our participation in the Opinion Retrieval task at TREC 2006. Our approach to identifying opinions in blog post consisted of scoring the posts separately on various aspects associated with an expression of opinion about a topic, including shallow sentiment analysis, spam detection, and link-based authority estimation. The separate approaches were combined into a single ranking, yielding significant improvement over a content-only baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Mishne06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Mishne06,
		author = {Gilad Mishne},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Multiple Ranking Strategies for Opinion Retrieval in Blogs - The University of Amsterdam at the 2006 {TREC} Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uamsterdam.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Mishne06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2006 at Maryland: Blog, Enterprise, Legal and QA Tracks

_Douglas W. Oard, Tamer Elsayed, Jianqiang Wang, Yejun Wu, Pengyi Zhang, Eileen G. Abels, Jimmy Lin, Dagobert Soergel_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf)
- :material-file-search: **Runs:** [ParTitDesDef](./runs.md#partitdesdef) | [PasTitDesDef](./runs.md#pastitdesdef) | [ParTiDesDmt2](./runs.md#partidesdmt2) | [ParTiDesDmt3](./runs.md#partidesdmt3) | [ParTitDef](./runs.md#partitdef)

??? abstract "Abstract"
	
	In TREC 2006, teams from the University of Maryland participated in the Blog track, the Expert Search task of the Enterprise track, the Complex Interactive Question Answering task of the Question Answering track, and the Legal track. This paper reports our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardEWWZALS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardEWWZALS06,
		author = {Douglas W. Oard and Tamer Elsayed and Jianqiang Wang and Yejun Wu and Pengyi Zhang and Eileen G. Abels and Jimmy Lin and Dagobert Soergel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 at Maryland: Blog, Enterprise, Legal and {QA} Tracks},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/OardEWWZALS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Knowledge Transfer and Opinion Detection in the TREC 2006 Blog Track

_Hui Yang, Jamie Callan, Luo Si_

- :fontawesome-solid-user-group: **Participant:** [cmu.dir.callan](./participants.md#cmu.dir.callan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cmu.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/cmu.blog.final.pdf)
- :material-file-search: **Runs:** [blog06r1](./runs.md#blog06r1) | [blog06r5](./runs.md#blog06r5) | [blog06r6](./runs.md#blog06r6) | [blog06r2](./runs.md#blog06r2) | [blog06r4](./runs.md#blog06r4) | [blog06r3](./runs.md#blog06r3)

??? abstract "Abstract"
	
	The paper describes the opinion detection system developed in Carnegie Mellon University for TREC 2006 Blog track. The system performed a two-stage process: passage retrieval and opinion detection. Due to lack of training data for the TREC Blog corpus, online opinion reviews provided in other domains, such as movie review and product review, were used as the training data. Knowledge transfer was performed to make the cross-domain learning possible. Logistic regression ranked the sentence-level opinions vs. objective statements. The evaluation shows that the algorithm is effective in the task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangCS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangCS06,
		author = {Hui Yang and Jamie Callan and Luo Si},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Knowledge Transfer and Opinion Detection in the {TREC} 2006 Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cmu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangCS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2006 Blog Track

_Kiduk Yang, Ning Yu, Alejandro Valerio, Hui Zhang_

- :fontawesome-solid-user-group: **Participant:** [indianau.yang](./participants.md#indianau.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/indianau.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/indianau.blog.final.pdf)
- :material-file-search: **Runs:** [woqs2](./runs.md#woqs2) | [wxoqs2](./runs.md#wxoqs2) | [woqln2](./runs.md#woqln2) | [wxoqln2](./runs.md#wxoqln2) | [wxoqf2](./runs.md#wxoqf2)

??? abstract "Abstract"
	
	Web Information Discovery Integrated Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science participated in the Blog track's opinion task in TREC-2006. The goal of opinion task is to 'uncover the public sentiment towards a given entity/target', which involves not only retrieving topically relevant blogs but also identifying those that contain opinions about the target. To further complicate the matter, the blog test collection contains considerable amount of noise, such as blogs with non-English content and non-blog content (e.g., advertisement, navigational text), which may misdirect retrieval systems. Based on our hypothesis that noise reduction (e.g., exclusion of non-English blogs, navigational text) will improve both on-topic and opinion retrieval performances, we explored various noise reduction approaches that can effectively eliminate the noise in blog data without inadvertently excluding valid content. After creating two separate indexes (with and without noise) to assess the noise reduction effect, we tackled the opinion blog retrieval task by breaking it down to two sequential subtasks: on-topic retrieval followed by opinion classification. Our opinion retrieval approach was to first apply traditional IR methods to retrieve on-topic blogs, and then boost the ranks of opinionated blogs based on opinion scores generated by opinion assessment methods. Our opinion module consists of Opinion Term Module, which identify opinions based on the frequency of opinion terms (i.e., terms that only occur frequently in opinion blogs), Rare Term Module, which uses uncommon/rare terms (e.g., “sooo good”) for opinion classification, IU Module, which uses IU (I and you) collocations, and Adjective-Verb Module, which uses computational linguistics' distribution similarity approach to learn the subjective language from training data
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYVZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYVZ06,
		author = {Kiduk Yang and Ning Yu and Alejandro Valerio and Hui Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2006 Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/indianau.blog.final.pdf},
		timestamp = {Wed, 29 Jun 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangYVZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 2006 Blog Track

_Wei Zhang, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [uillinois.chicago.zhang](./participants.md#uillinois.chicago.zhang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.blog.final.pdf)
- :material-file-search: **Runs:** [uicsr](./runs.md#uicsr) | [uicst](./runs.md#uicst)

??? abstract "Abstract"
	
	We developed a two-step approach that finds relevant blog documents containing opinioned content for a given query topic. The first step, retrieval step, is to find documents relevant to the query. The second step, opinion identification step, is to find the documents containing opinions within the scope of the document set from the retrieval step. In the retrieval step, we try to improve the retrieval effectiveness by retrieving based on concepts, and doing query expansion using pseudo feedback, Wikipedia feedback and web feedback. In the opinion identification step, we train a sentence classifier using subjective sentences (opinioned) and objective sentences (non-opinioned), which are relevant to a query topic. This classifier labels each sentence in a given document as either subjective or objective. A document containing subjective sentences relating to the query is finally labeled as an opinioned relevant document (ORD). We tried two strategies to rank the ORDs that became two submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangY06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangY06,
		author = {Wei Zhang and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 2006 Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangY06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCSC on REC 2006 Blog Opinion Mining

_Ethan Zhang, Yi Zhang_

- :fontawesome-solid-user-group: **Participant:** [ucalifornia.sc.zhang](./participants.md#ucalifornia.sc.zhang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ucalifornia-sc.blog.pdf](http://trec.nist.gov/pubs/trec15/papers/ucalifornia-sc.blog.pdf)
- :material-file-search: **Runs:** [ucscauto](./runs.md#ucscauto) | [ucscdesc](./runs.md#ucscdesc) | [ucscrelfb](./runs.md#ucscrelfb)

??? abstract "Abstract"
	
	The University of California Santa Cruz team submitted three runs for the TREC Blog Track opinion mining task. We developed a two stage retrieval system. We started with retrieving relevant documents from the corpus for each topic, and then ran each retrieved document through a classifier to estimate the probability that the document contains opinion expressions. The documents were ranked according to the product of the retrieval score and the estimated probability. The Lemur search engine, which is based on the language modeling approach, was used for retrieval. A Bayesian Logistic Regression classifier was trained using a noisy training data set from other domains, which include news articles, product reviews and movie reviews. All runs are automatic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangZ06,
		author = {Ethan Zhang and Yi Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCSC} on {REC} 2006 Blog Opinion Mining},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ucalifornia-sc.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

