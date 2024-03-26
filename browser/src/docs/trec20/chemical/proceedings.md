# Proceedings - Chemical 2011 

#### Overview of the TREC 2011 Chemical IR Track

_Mihai Lupu, Jiashu Zhao, Jimmy X. Huang, Harsha Gurulingappa, Juliane Fluck, Marc Zimmermann, Igor V. Filippov, John Tait_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/CHEM.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec20/papers/CHEM.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The third year of the Chemical IR evaluation track benefitted from the support of many more people interested in the domain, as shown by the number of co-authors of this overview paper. We continued the two tasks we had before, and introduced a new task focused on chemical image recognition. The objective is to gradually move towards systems really useful to the practitioners, and in chemistry, this involves both text and images. The track had a total of 9 groups participating, submitting a total of 36 runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LupuZHGFZFT11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LupuZHGFZFT11,
		author = {Mihai Lupu and Jiashu Zhao and Jimmy X. Huang and Harsha Gurulingappa and Juliane Fluck and Marc Zimmermann and Igor V. Filippov and John Tait},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2011 Chemical {IR} Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/CHEM.OVERVIEW.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LupuZHGFZFT11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Optical Structure Recognition Application Entry in Image2Structure  Task

_Igor V. Filippov, Dmitry Katsubo, Marc C. Nicklaus_

- :fontawesome-solid-user-group: **Participant:** [SAIC_Frederick](./participants.md#saic_frederick)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/saic-frederick.chem.pdf](http://trec.nist.gov/pubs/trec20/papers/saic-frederick.chem.pdf)
- :material-file-search: **Runs:** [osra_1.3.8_r300](./runs.md#osra_1.3.8_r300) | [osra_1.3.8_def](./runs.md#osra_1.3.8_def)

??? abstract "Abstract"
	
	We present Optical Structure Recognition Application (OSRA) as an entry into Image2Structure task of TREC-CHEM. OSRA is an open source utility to convert images of chemical structures to connection tables in an established computerized molecular format. There exists a large body of chemical information which has remained largely inaccessible to machine data mining techniques so far. One of the most common ways of describing a chemical structure in a journal publication or a patent document is by drawing a two-dimensional structure diagram which represents atoms and bonds of the molecule in a human-recognizable form. While easily interpreted by a human expert, such drawings are by themselves unsuitable for use in a computer database for applications such as virtual screening and computer aided drug development. OSRA allows recognition and conversion of such drawings into computer formats widely used by the chemoinformatics community.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FilippovKN11.bib) "
	```
	@inproceedings{DBLP:conf/trec/FilippovKN11,
		author = {Igor V. Filippov and Dmitry Katsubo and Marc C. Nicklaus},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Optical Structure Recognition Application Entry in Image2Structure Task},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/saic-frederick.chem.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FilippovKN11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BiTeM Group Report for TREC Chemical IR Track 2011

_Julien Gobeill, Arnaud Gaudinat, Patrick Ruch, Emilie Pasche, Douglas Teodoro, Dina Vishnyakova_

- :fontawesome-solid-user-group: **Participant:** [BiTeM](./participants.md#bitem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/BiTeM.chem.pdf](http://trec.nist.gov/pubs/trec20/papers/BiTeM.chem.pdf)
- :material-file-search: **Runs:** [BiTeMtext](./runs.md#bitemtext) | [BiTeMmesh](./runs.md#bitemmesh) | [BiTeMboth](./runs.md#bitemboth) | [BiTeMPAmesh](./runs.md#bitempamesh) | [BiTeMPAtext](./runs.md#bitempatext) | [BiTeMPAcomb](./runs.md#bitempacomb) | [BiTeMPAcitFB](./runs.md#bitempacitfb)

??? abstract "Abstract"
	
	For the third year, the BiTeM group participated in the TREC Chemical IR Track. For this campaign, we applied strategies that already showed their effectiveness, as the Citations Feedback, which takes benefit from the citations of the retrieved documents in order to re-arrange the ranking. But we also investigated a new inter-lingua model built with chemical annotations with concepts that we automatically mapped into documents. We used the MeSH controlled vocabulary for this purpose. For the Technology Survey task, the fusion of the MeSH and Text models led to a remarkable improvement (+71% for MAP) compared to the Text model alone. The most interesting aspect is that both models are highly complementary as the MeSH model brings 70% of new relevant documents that were not retrieved by the Text model. For the Prior Art task, we showed that there exist patterns of chemical patents that are interconnected (i.e. linked together with direct citations) and that are more likely to be present together in a prior art. Such patterns are efficiently retrieved with our Citations Feedback strategy. On the other hand, we pointed out that the less the prior art of a given topic is interconnected, the less efficient is the Information Retrieval. We hypothesize that such patents have a larger technical focus, maybe represented by a larger set of IPC codes, and then have a lower textual similarity with their prior art documents. These topics should gain to be recognized in order to be treated with complementary techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GobeillGRPTV11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GobeillGRPTV11,
		author = {Julien Gobeill and Arnaud Gaudinat and Patrick Ruch and Emilie Pasche and Douglas Teodoro and Dina Vishnyakova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BiTeM Group Report for {TREC} Chemical {IR} Track 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/BiTeM.chem.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GobeillGRPTV11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Retrieval Framework for Technology Survey in Biomedical  and Chemistry Literature

_Harsha Gurulingappa, Bernd Müller, Martin Hofmann-Apitius, Juliane Fluck_

- :fontawesome-solid-user-group: **Participant:** [fraunhofer.scai](./participants.md#fraunhofer.scai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Fraunhofer-SCAI.chem.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Fraunhofer-SCAI.chem.update.pdf)
- :material-file-search: **Runs:** [SCAIRUN1](./runs.md#scairun1) | [SCAIRUN2](./runs.md#scairun2) | [SCAIRUN3](./runs.md#scairun3) | [SCAIRUN4](./runs.md#scairun4)

??? abstract "Abstract"
	
	The Technology survey task deals with the retrieval of information that can best answer a scientific question. This task is more challenging in biomedical and chemistry domains due to diverse conventions applied for naming the entities. In order to address this challenge, the work reported here presents an ad-hoc retrieval task that has been evaluated during the TRECCHEM-2011 for its ability to support retrieval from the biomedical and chemistry literature. The core of the framework contains nearly 1.3 million patents and full-text articles that were indexed with pre-selected biomedical concepts. Altogether, four runs were submitted based on different query formulation strategies and they exhibited competitive results
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GurulingappaMHFGH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GurulingappaMHFGH11,
		author = {Harsha Gurulingappa and Bernd M{\"{u}}ller and Martin Hofmann{-}Apitius and Juliane Fluck},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Information Retrieval Framework for Technology Survey in Biomedical and Chemistry Literature},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Fraunhofer-SCAI.chem.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GurulingappaMHFGH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Image-to-Structure Task by ChemReader

_Jungkap Park, Ye Li, Gus R. Rosania, Kazuhiro Saitou_

- :fontawesome-solid-user-group: **Participant:** [ChemReader](./participants.md#chemreader)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/chemreader.chem.update.pdf](http://trec.nist.gov/pubs/trec20/papers/chemreader.chem.update.pdf)
- :material-file-search: **Runs:** [ChemReader_Run1](./runs.md#chemreader_run1) | [ChemReader_Run2](./runs.md#chemreader_run2)

??? abstract "Abstract"
	
	Chemical structure recognition software aims to extract raster images of 2D chemical structure diagrams and convert them into a standard, machineͲreadable chemical file format. Such software, so called chemical OCR can be used for mining chemical entities appeared in scientific literature. Since traditional textͲbased mining methods haven't attempt to utilize image data in documents yet, chemical OCR software will pave a new way for the development of chemical literature mining [1, 2]. This year, the TREC Chemical IR campaign has launched a new topic called “ImageͲtoͲStructure (I2S) task” where participants are asked to process given images and recognize chemical structures in the images. While the immediate objective of this task would be to evaluate the existing chemical OCR software, it ultimately aims to create a platform to see how information in image data can be incorporated with existing textͲmining approach to facilitate further development of chemical IR techniques. We developed a chemical OCR software, ChemReader which specifically tailored to a chemical database annotation scheme [3, 4]. The recognition algorithms are optimized to achieve high accuracy and robust performance sufficient for fully automated processing of scientific articles. In our previous reports, ChemReader was able to outperform other chemical OCR software on several sets of sample images from diverse sources in terms of the rate of correct outputs and the accuracy on extracting molecular substructure patterns. Since then, other existing tools have been continuously updated, and new chemical OCR tools also have been released. Thus this task is a good opportunity for chemical OCR developers to evaluate their algorithms against common image set, and see strengths and weaknesses of their own comparing them to others. Here we report how we performed the I2S task during MayͲJuly, 2011. We first briefly present the recognition algorithms in ChemReader, followed by the updates during the training. Then, we will show the results of its evaluation on test set and discuss major errors of ChemReader on the test. Most importantly, on the basis of the lessons learned from this task, we will discuss issues and insights in the chemical OCR development.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ParkLRS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ParkLRS11,
		author = {Jungkap Park and Ye Li and Gus R. Rosania and Kazuhiro Saitou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Image-to-Structure Task by ChemReader},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/chemreader.chem.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ParkLRS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Performance of MolRec at TREC 2011 Overview and Analysis of Results

_Noureddin M. Sadawi, Alan P. Sexton, Volker Sorge_

- :fontawesome-solid-user-group: **Participant:** [UoB](./participants.md#uob)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UoB.chem.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UoB.chem.update.pdf)
- :material-file-search: **Runs:** [Run1](./runs.md#run1) | [Run2](./runs.md#run2)

??? abstract "Abstract"
	
	Chemical molecular diagrams are commonly found in documents from the chemical and life science disciplines. We present an overview of the elements of these diagrams and of MolRec, our system for analysing and recognising them. MolRec uses a number of techniques to refine the scanned images and precisely detect line segments and line junctions, structural elements and the atomic formulae that commonly appear in such diagrams. The output of our system is a chemical formula and associated MOL file, a standard representation of molecular structures used in cheminformatics that records precise molecular spatial and connectivity information. When applied to the TREC 2011 test set of 1000 molecular diagrams, MolRec returned in two separate runs 949 and 950 correctly recalled structures, respectively. We discuss these results and present an analysis of MolRec's performance on the test set.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SadawiSS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/SadawiSS11,
		author = {Noureddin M. Sadawi and Alan P. Sexton and Volker Sorge},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Performance of MolRec at {TREC} 2011 Overview and Analysis of Results},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UoB.chem.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SadawiSS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Imago: Open-Source Toolkit for 2D Chemical Structure Image Recognition

_Viktor Smolov, Fedor Zentsev, Mikhail Rybalkin_

- :fontawesome-solid-user-group: **Participant:** [GGA](./participants.md#gga)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/GGA.chemical.pdf](http://trec.nist.gov/pubs/trec20/papers/GGA.chemical.pdf)
- :material-file-search: **Runs:** [GGA_Imago_2011](./runs.md#gga_imago_2011) | [GGA_Imago2011a](./runs.md#gga_imago2011a)

??? abstract "Abstract"
	
	Different chemical databases contain molecule structures with links to articles and patents, where such molecules are presented as images. Keeping such a database in a consistent state is a challenging problem, and, thus, efficient and accurate molecule image recognition algorithms are very important for solving this task. We present an open-source toolkit for 2D chemical structure image recognition, called Imago. The main aim of this paper is to describe the algorithm approach implemented in Imago, and to share our ideas of possible improvements in the algorithm after we have summarized the results from the participation in the Image2Structure task at TREC-CHEM 2011.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmolovZR11.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmolovZR11,
		author = {Viktor Smolov and Fedor Zentsev and Mikhail Rybalkin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Imago: Open-Source Toolkit for 2D Chemical Structure Image Recognition},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/GGA.chemical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmolovZR11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2011 Chemistry Track

_Ping Zhang, Hongfei Lin, Jiajin Wu, Yuan Lin_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./participants.md#dutir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/DUTIR.chem.update.pdf](http://trec.nist.gov/pubs/trec20/papers/DUTIR.chem.update.pdf)
- :material-file-search: **Runs:** [DUT11TSRun1](./runs.md#dut11tsrun1) | [DUT11TSRun2](./runs.md#dut11tsrun2) | [DUT11TSRun3](./runs.md#dut11tsrun3) | [DUT11TSRun4](./runs.md#dut11tsrun4) | [DUT11PARun1](./runs.md#dut11parun1) | [DUT11PARun5](./runs.md#dut11parun5) | [DUT11PARun2](./runs.md#dut11parun2) | [DUT11PARun3](./runs.md#dut11parun3) | [DUT11PARun4](./runs.md#dut11parun4) | [DUT11PARun6](./runs.md#dut11parun6) | [DUT11PARun7](./runs.md#dut11parun7) | [DUT11PARun8](./runs.md#dut11parun8) | [DUT11PARun9](./runs.md#dut11parun9)

??? abstract "Abstract"
	
	This paper presents the DUTIR submission to TREC 2011 Chemical IR Track. Several experiments are done mainly with two retrieval models i.e. Language Model for IR and DFR model. In addition, query expansion technology is also applied to enhance retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangLWL11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangLWL11,
		author = {Ping Zhang and Hongfei Lin and Jiajin Wu and Yuan Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2011 Chemistry Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/DUTIR.chem.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangLWL11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### How to Make Manual Conjunctive Normal Form Queries Work in Patents  Search

_Le Zhao, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU.LIRA](./participants.md#cmu.lira)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/CMU-LIRA.chemistry.pdf](http://trec.nist.gov/pubs/trec20/papers/CMU-LIRA.chemistry.pdf)
- :material-file-search: **Runs:** [CMUTSmans](./runs.md#cmutsmans) | [CMUTStncs](./runs.md#cmutstncs) | [CMUTStncws](./runs.md#cmutstncws)

??? abstract "Abstract"
	
	This year we focused on the Technology Survey (TS) task: Given a natural language description of the topic, look for related patents about that topic. The task is close to an ad hoc retrieval task, except for the additional information of the specific chemicals or chemical reactions that the user cares about. Since there are only 6 topics for the TS task, this notebook paper is more of a case study report, than the ordinary TREC report with significance tests. We found that on average, with the infAP measure, manually created conjunctive normal form queries performed similarly as automatic keyword search with some tuning of term weights. Manual queries do not seem to always help, especially when initial keyword performance is high, but can give large improvements on difficult queries. We also used the same querying strategy in the Patent Olympics 2011 ChemAthlon task, and also include some of the ChemAthlon cases in this report. Since CNF queries are strictly more expressive than keyword queries, we try to identify problems that may have caused the manual CNF queries to be seen sometimes performing worse than the automatic keyword queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoC11,
		author = {Le Zhao and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {How to Make Manual Conjunctive Normal Form Queries Work in Patents Search},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/CMU-LIRA.chemistry.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Chemical Structure Reconstruction with chemoCR

_Marc Zimmermann_

- :fontawesome-solid-user-group: **Participant:** [chemoCR](./participants.md#chemocr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/chemoCR.chem.update.pdf](http://trec.nist.gov/pubs/trec20/papers/chemoCR.chem.update.pdf)
- :material-file-search: **Runs:** [chemoCR_v93_p10](./runs.md#chemocr_v93_p10)

??? abstract "Abstract"
	
	chemoCR makes chemical information contained in depictions of chemical structures accessible as connection table for computer programs. In order to solve the problem of recognizing and translating chemical structures in image documents, our chemoCR system combines pattern recognition techniques with supervised machine learning concepts. The method is based on the idea of identifying from structural formulas the most significant semantic entities. Semantic entities are for example chiral bonds, superatoms and reaction arrows. The workflow consists of three phases: image preprocessing, semantic entity recognition, and molecule reconstruction plus validation of the result. All steps of the process make use of chemical knowledge in order to detect and fix errors. The system can be trained and adapted to different sources of input images. The reconstructed connection table can be used by all chemical software.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zimmermann11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Zimmermann11,
		author = {Marc Zimmermann},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Chemical Structure Reconstruction with chemoCR},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/chemoCR.chem.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Zimmermann11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

