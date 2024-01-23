# Runs - Legal 2007 

#### catchup0701p 
[**`Results`**](./results.md#catchup0701p), [**`Participants`**](./participants.md#uamsterdamderijke), [**`Proceedings`**](./proceedings.md#access-to-legal-documents-exact-match-best-match-and-combinations), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.catchup0701p.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.catchup0701p.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/catchup0701p.main.pdf) 

- :material-rename: **Run ID:** catchup0701p 
- :fontawesome-solid-user-group: **Participant:** uamsterdam.deRijke 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/4/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** For the basic run, we index for each document the WHOLE text, including the XML tags. They should not have much effect, since they are usually the same for each document. We just take the request as is and retrieve it from that (quite huge) index. 

---
#### CMU07RBase 
[**`Results`**](./results.md#cmu07rbase), [**`Participants`**](./participants.md#cmudircallan), [**`Proceedings`**](./proceedings.md#stuctured-queries-for-legal-search), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.CMU07RBase.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.CMU07RBase.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/CMU07RBase.routing.pdf) 

- :material-rename: **Run ID:** CMU07RBase 
- :fontawesome-solid-user-group: **Participant:** cmu.dir.callan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/6/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** routing 
- :material-text: **Run description:** baseline run with ranking of final boolean query filtered results first, and then appending with results from bag of word boolean query terms. 

---
#### CMU07RFBSVME 
[**`Results`**](./results.md#cmu07rfbsvme), [**`Participants`**](./participants.md#cmudircallan), [**`Proceedings`**](./proceedings.md#stuctured-queries-for-legal-search), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.CMU07RFBSVME.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.CMU07RFBSVME.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/CMU07RFBSVME.routing.pdf) 

- :material-rename: **Run ID:** CMU07RFBSVME 
- :fontawesome-solid-user-group: **Participant:** cmu.dir.callan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** routing 
- :material-text: **Run description:** expanding the query with terms extracted from highest weight SVM features learned from training documents.  40 terms are selected for expansion for each topic.  This new query is used to rerank the documents matching the final negotiated Boolean query.  To make up for 26000 documents, results from the expanded queries are used to patch up the Boolean result lists. 

---
#### CMU07RSVMNP 
[**`Results`**](./results.md#cmu07rsvmnp), [**`Participants`**](./participants.md#cmudircallan), [**`Proceedings`**](./proceedings.md#stuctured-queries-for-legal-search), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.CMU07RSVMNP.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.CMU07RSVMNP.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/CMU07RSVMNP.routing.pdf) 

- :material-rename: **Run ID:** CMU07RSVMNP 
- :fontawesome-solid-user-group: **Participant:** cmu.dir.callan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/6/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** routing 
- :material-text: **Run description:** Queries with positive and negative term weights that approximates SVM classifiers learned from training documents. Top 100 weighted terms (with positive and negative weights) are selected for each topic. This new query is used to rerank the documents matching the final negotiated Boolean query. Those documents that do not match the boolean query are ranked and used to append the Boolean result lists. 

---
#### CMUL07ibp 
[**`Results`**](./results.md#cmul07ibp), [**`Participants`**](./participants.md#cmudircallan), [**`Proceedings`**](./proceedings.md#stuctured-queries-for-legal-search), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.CMUL07ibp.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.CMUL07ibp.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/CMUL07ibp.main.pdf) 

- :material-rename: **Run ID:** CMUL07ibp 
- :fontawesome-solid-user-group: **Participant:** cmu.dir.callan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/4/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Convert final boolean queries to Indri structured queries with boolean constraints. The ranking function treats each phrase as a query term. 

---
#### CMUL07ibs 
[**`Results`**](./results.md#cmul07ibs), [**`Participants`**](./participants.md#cmudircallan), [**`Proceedings`**](./proceedings.md#stuctured-queries-for-legal-search), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.CMUL07ibs.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.CMUL07ibs.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/CMUL07ibs.main.pdf) 

- :material-rename: **Run ID:** CMUL07ibs 
- :fontawesome-solid-user-group: **Participant:** cmu.dir.callan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/4/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Convert final boolean queries to Indri structured queries with boolean constraints. The ranking function treats terms connected by 'OR' as synonyms. 

---
#### CMUL07ibt 
[**`Results`**](./results.md#cmul07ibt), [**`Participants`**](./participants.md#cmudircallan), [**`Proceedings`**](./proceedings.md#stuctured-queries-for-legal-search), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.CMUL07ibt.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.CMUL07ibt.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/CMUL07ibt.main.pdf) 

- :material-rename: **Run ID:** CMUL07ibt 
- :fontawesome-solid-user-group: **Participant:** cmu.dir.callan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/4/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Convert final boolean queries to Indri structured queries with boolean constraints. The ranking is based on bag-of-words representation without any operators. 

---
#### CMUL07irs 
[**`Results`**](./results.md#cmul07irs), [**`Participants`**](./participants.md#cmudircallan), [**`Proceedings`**](./proceedings.md#stuctured-queries-for-legal-search), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.CMUL07irs.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.CMUL07irs.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/CMUL07irs.main.pdf) 

- :material-rename: **Run ID:** CMUL07irs 
- :fontawesome-solid-user-group: **Participant:** cmu.dir.callan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/4/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Convert final boolean queries to Indri structured queries without boolean constraints. The ranking function treats terms connected by 'OR' as synonyms. 

---
#### CMUL07irt 
[**`Results`**](./results.md#cmul07irt), [**`Participants`**](./participants.md#cmudircallan), [**`Proceedings`**](./proceedings.md#stuctured-queries-for-legal-search), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.CMUL07irt.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.CMUL07irt.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/CMUL07irt.main.pdf) 

- :material-rename: **Run ID:** CMUL07irt 
- :fontawesome-solid-user-group: **Participant:** cmu.dir.callan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/4/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Convert final boolean queries to Indri structured queries without boolean constraints. The ranking is based on bag-of-words representation of the query without any operators. 

---
#### CMUL07o1 
[**`Results`**](./results.md#cmul07o1), [**`Participants`**](./participants.md#cmudircallan), [**`Proceedings`**](./proceedings.md#stuctured-queries-for-legal-search), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.CMUL07o1.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.CMUL07o1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/CMUL07o1.main.pdf) 

- :material-rename: **Run ID:** CMUL07o1 
- :fontawesome-solid-user-group: **Participant:** cmu.dir.callan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/4/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Okapi ranking based on bag-of-words representation of the final boolean query. Ignore boolean constraints. 

---
#### CMUL07o3 
[**`Results`**](./results.md#cmul07o3), [**`Participants`**](./participants.md#cmudircallan), [**`Proceedings`**](./proceedings.md#stuctured-queries-for-legal-search), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.CMUL07o3.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.CMUL07o3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/CMUL07o3.main.pdf) 

- :material-rename: **Run ID:** CMUL07o3 
- :fontawesome-solid-user-group: **Participant:** cmu.dir.callan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/4/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Okapi ranking based on bag-of-words representation of the final boolean query, initial proposal by defendant and rejoinder by plaintiff. Ignore boolean constraints. 

---
#### CMUL07std 
[**`Results`**](./results.md#cmul07std), [**`Participants`**](./participants.md#cmudircallan), [**`Proceedings`**](./proceedings.md#stuctured-queries-for-legal-search), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.CMUL07std.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.CMUL07std.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/CMUL07std.main.pdf) 

- :material-rename: **Run ID:** CMUL07std 
- :fontawesome-solid-user-group: **Participant:** cmu.dir.callan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/3/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** This is the standard condition run. It uses terms in request text, excluding some headers that are not meaningful for the query (e.g. "Please produce any and all documents that discuss ..."). 

---
#### Dartmouth1 
[**`Results`**](./results.md#dartmouth1), [**`Participants`**](./participants.md#dartmouththompson), [**`Proceedings`**](./proceedings.md#dartmouth-college-at-trec-2007-legal-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.Dartmouth1.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.Dartmouth1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/Dartmouth1.main.pdf) 

- :material-rename: **Run ID:** Dartmouth1 
- :fontawesome-solid-user-group: **Participant:** dartmouth.thompson 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/30/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** It is a automatic run that only use request text as the query sentence. It is the result returned by Indri. 

---
#### fdwim7rs 
[**`Results`**](./results.md#fdwim7rs), [**`Participants`**](./participants.md#fudanuniu), [**`Proceedings`**](./proceedings.md#wim-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.fdwim7rs.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.fdwim7rs.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/fdwim7rs.main.pdf) 

- :material-rename: **Run ID:** fdwim7rs 
- :fontawesome-solid-user-group: **Participant:** fudanu.niu 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/2/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** On the base of run fdwim7ts, we write a program to remove meaningless words from <RequestText> as indri's input 

---
#### fdwim7sl 
[**`Results`**](./results.md#fdwim7sl), [**`Participants`**](./participants.md#fudanuniu), [**`Proceedings`**](./proceedings.md#wim-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.fdwim7sl.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.fdwim7sl.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/fdwim7sl.main.pdf) 

- :material-rename: **Run ID:** fdwim7sl 
- :fontawesome-solid-user-group: **Participant:** fudanu.niu 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/2/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** It is mostly same as fdwim7ss despite that we run the retrieval on an non-preprocessed index  

---
#### fdwim7ss 
[**`Results`**](./results.md#fdwim7ss), [**`Participants`**](./participants.md#fudanuniu), [**`Proceedings`**](./proceedings.md#wim-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.fdwim7ss.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.fdwim7ss.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/fdwim7ss.main.pdf) 

- :material-rename: **Run ID:** fdwim7ss 
- :fontawesome-solid-user-group: **Participant:** fudanu.niu 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/2/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** On the base of run fdwim7rs, we try a new method to extract representative words from fields "instruction" "definition" , "background" adding to the input of retrieval 

---
#### fdwim7ts 
[**`Results`**](./results.md#fdwim7ts), [**`Participants`**](./participants.md#fudanuniu), [**`Proceedings`**](./proceedings.md#wim-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.fdwim7ts.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.fdwim7ts.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/fdwim7ts.main.pdf) 

- :material-rename: **Run ID:** fdwim7ts 
- :fontawesome-solid-user-group: **Participant:** fudanu.niu 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/2/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** In spite of removing prepositions and "the", "a" (such meaningless words), run of fdwim7ts does not take any optimizing steps. 

---
#### fdwim7xj 
[**`Results`**](./results.md#fdwim7xj), [**`Participants`**](./participants.md#fudanuniu), [**`Proceedings`**](./proceedings.md#wim-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.fdwim7xj.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.fdwim7xj.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/fdwim7xj.main.pdf) 

- :material-rename: **Run ID:** fdwim7xj 
- :fontawesome-solid-user-group: **Participant:** fudanu.niu 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/1/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** As the baseline, fdwim7xj does not make lots of pre-process. All steps mainly rely on indri search engine. 

---
#### IowaSL0702 
[**`Results`**](./results.md#iowasl0702), [**`Participants`**](./participants.md#uiowasrinivasan), [**`Proceedings`**](./proceedings.md#exploring-the-legal-discovery-and-enterprise-tracks-at-the-university-of-iowa), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.IowaSL0702.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.IowaSL0702.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/IowaSL0702.main.pdf) 

- :material-rename: **Run ID:** IowaSL0702 
- :fontawesome-solid-user-group: **Participant:** uiowa.srinivasan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/2/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** This run is processed the same as IowaSL07Ref, except that all three boolean queries are converted to term vectors, and added to the query. 

---
#### IowaSL0703 
[**`Results`**](./results.md#iowasl0703), [**`Participants`**](./participants.md#uiowasrinivasan), [**`Proceedings`**](./proceedings.md#exploring-the-legal-discovery-and-enterprise-tracks-at-the-university-of-iowa), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.IowaSL0703.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.IowaSL0703.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/IowaSL0703.main.pdf) 

- :material-rename: **Run ID:** IowaSL0703 
- :fontawesome-solid-user-group: **Participant:** uiowa.srinivasan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/3/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** This run is processed in the same manner as IowaSL0702, except that the wildcards in the Boolean queries, previously stripped, are evaluated, and the two candidates with the greatest document frequencies are added to the query. I should note that all scoring/reranking for the IowaSL07* runs are based on Okapi term weights. 

---
#### IowaSL0704 
[**`Results`**](./results.md#iowasl0704), [**`Participants`**](./participants.md#uiowasrinivasan), [**`Proceedings`**](./proceedings.md#exploring-the-legal-discovery-and-enterprise-tracks-at-the-university-of-iowa), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.IowaSL0704.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.IowaSL0704.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/IowaSL0704.main.pdf) 

- :material-rename: **Run ID:** IowaSL0704 
- :fontawesome-solid-user-group: **Participant:** uiowa.srinivasan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/3/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** This run is processed in the same manner as IowaSL0703, except that the top three documents from IowaSL0703 are scanned for terms that have a high local frequency relative to the rest of the corpus. The best five candidates are added to the query term vector, provided they are not already in the query, not on the SMART list of stop words, do not contain any punctuation or numeric characters, and that they have a valid entry in WordNet.  

---
#### IowaSL0705 
[**`Results`**](./results.md#iowasl0705), [**`Participants`**](./participants.md#uiowasrinivasan), [**`Proceedings`**](./proceedings.md#exploring-the-legal-discovery-and-enterprise-tracks-at-the-university-of-iowa), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.IowaSL0705.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.IowaSL0705.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/IowaSL0705.main.pdf) 

- :material-rename: **Run ID:** IowaSL0705 
- :fontawesome-solid-user-group: **Participant:** uiowa.srinivasan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/3/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** This run is processed in the same manner as IowaSL0704, except that the top three documents from a prior run with this configuration provide the basis for the query expansion terms. For this run, the system has filtered our terms from the RequestText topic field that exist in that field for more than 10 of the topics.  

---
#### IowaSL0706 
[**`Results`**](./results.md#iowasl0706), [**`Participants`**](./participants.md#uiowasrinivasan), [**`Proceedings`**](./proceedings.md#exploring-the-legal-discovery-and-enterprise-tracks-at-the-university-of-iowa), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.IowaSL0706.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.IowaSL0706.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/IowaSL0706.main.pdf) 

- :material-rename: **Run ID:** IowaSL0706 
- :fontawesome-solid-user-group: **Participant:** uiowa.srinivasan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/3/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** This run was conducted in the same manner as IowaSL0705, except that the two indicated Boolean query fields were dropped from the query term vector for the initial feedback retrieval and the final retrieval. 

---
#### IowaSL0707 
[**`Results`**](./results.md#iowasl0707), [**`Participants`**](./participants.md#uiowasrinivasan), [**`Proceedings`**](./proceedings.md#exploring-the-legal-discovery-and-enterprise-tracks-at-the-university-of-iowa), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.IowaSL0707.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.IowaSL0707.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/IowaSL0707.main.pdf) 

- :material-rename: **Run ID:** IowaSL0707 
- :fontawesome-solid-user-group: **Participant:** uiowa.srinivasan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Same as IowaSL0706 except that the Request Text was edited manually instead of automatically. 

---
#### IowaSL07Ref 
[**`Results`**](./results.md#iowasl07ref), [**`Participants`**](./participants.md#uiowasrinivasan), [**`Proceedings`**](./proceedings.md#exploring-the-legal-discovery-and-enterprise-tracks-at-the-university-of-iowa), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.IowaSL07Ref.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.IowaSL07Ref.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/IowaSL07Ref.main.pdf) 

- :material-rename: **Run ID:** IowaSL07Ref 
- :fontawesome-solid-user-group: **Participant:** uiowa.srinivasan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/2/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** The reference run. The index consists of the document title and ocr data indexed as one field, generated using Lucene's StandardAnalyzer. Lucene is used to retrieve max(25000, B) * 1.5 documents. We post-process, automatically assigning a new score to the documents (the submitted score) and reranking. 

---
#### LIU 
[**`Results`**](./results.md#liu), [**`Participants`**](./participants.md#liuchu), [**`Proceedings`**](./proceedings.md#trec-2007-legal-track-interactive-task-a-report-from-the-liu-team), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.LIU.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.LIU.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/interactive.pdf) 

- :material-rename: **Run ID:** LIU 
- :fontawesome-solid-user-group: **Participant:** liu.chu 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/15/2007 
- :material-text-search: **Task:** interactive 

---
#### otL07db 
[**`Results`**](./results.md#otl07db), [**`Participants`**](./participants.md#open-texttomlinson), [**`Proceedings`**](./proceedings.md#experiments-with-the-negotiated-boolean-queries-of-the-trec-2007-legal-discovery-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.otL07db.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.otL07db.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/otL07db.main.pdf) 

- :material-rename: **Run ID:** otL07db 
- :fontawesome-solid-user-group: **Participant:** open-text.tomlinson 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/28/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** boolean run based on initial proposal by defendant (same as otL07fb except that the defendant boolean query was used instead of the final query) 

---
#### otL07fb 
[**`Results`**](./results.md#otl07fb), [**`Participants`**](./participants.md#open-texttomlinson), [**`Proceedings`**](./proceedings.md#experiments-with-the-negotiated-boolean-queries-of-the-trec-2007-legal-discovery-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.otL07fb.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.otL07fb.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/otL07fb.main.pdf) 

- :material-rename: **Run ID:** otL07fb 
- :fontawesome-solid-user-group: **Participant:** open-text.tomlinson 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/14/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** boolean run based on final negotiated query (same as reference boolean run refL07B except re-ordered by relevance) 

---
#### otL07fb2x 
[**`Results`**](./results.md#otl07fb2x), [**`Participants`**](./participants.md#open-texttomlinson), [**`Proceedings`**](./proceedings.md#experiments-with-the-negotiated-boolean-queries-of-the-trec-2007-legal-discovery-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.otL07fb2x.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.otL07fb2x.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/otL07fb2x.main.pdf) 

- :material-rename: **Run ID:** otL07fb2x 
- :fontawesome-solid-user-group: **Participant:** open-text.tomlinson 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/28/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** boolean run based on doubling the word distances in the final negotiated query (same as otL07fb except that the word proximity distances were doubled, e.g. w/20 was changed to w/40) 

---
#### otL07fbe 
[**`Results`**](./results.md#otl07fbe), [**`Participants`**](./participants.md#open-texttomlinson), [**`Proceedings`**](./proceedings.md#experiments-with-the-negotiated-boolean-queries-of-the-trec-2007-legal-discovery-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.otL07fbe.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.otL07fbe.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/otL07fbe.main.pdf) 

- :material-rename: **Run ID:** otL07fbe 
- :fontawesome-solid-user-group: **Participant:** open-text.tomlinson 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/28/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** blind feedback expansion of the final boolean query, based 50% on queries from first 2 retrieved rows of otL07fb and 50% on original otL07fb query 

---
#### otL07frw 
[**`Results`**](./results.md#otl07frw), [**`Participants`**](./participants.md#open-texttomlinson), [**`Proceedings`**](./proceedings.md#experiments-with-the-negotiated-boolean-queries-of-the-trec-2007-legal-discovery-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.otL07frw.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.otL07frw.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/otL07frw.main.pdf) 

- :material-rename: **Run ID:** otL07frw 
- :fontawesome-solid-user-group: **Participant:** open-text.tomlinson 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/28/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** weighted fusion of boolean and vector runs, weight 3 on otL07fb, weight 2 on otL07rvl, weight 1 on otL07fv 

---
#### otL07fv 
[**`Results`**](./results.md#otl07fv), [**`Participants`**](./participants.md#open-texttomlinson), [**`Proceedings`**](./proceedings.md#experiments-with-the-negotiated-boolean-queries-of-the-trec-2007-legal-discovery-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.otL07fv.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.otL07fv.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/otL07fv.main.pdf) 

- :material-rename: **Run ID:** otL07fv 
- :fontawesome-solid-user-group: **Participant:** open-text.tomlinson 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/14/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** vector run based on final negotiated query (same as otL07fb except that all boolean, phrase and proximity operators were changed to the OR operator) 

---
#### otL07pb 
[**`Results`**](./results.md#otl07pb), [**`Participants`**](./participants.md#open-texttomlinson), [**`Proceedings`**](./proceedings.md#experiments-with-the-negotiated-boolean-queries-of-the-trec-2007-legal-discovery-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.otL07pb.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.otL07pb.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/otL07pb.main.pdf) 

- :material-rename: **Run ID:** otL07pb 
- :fontawesome-solid-user-group: **Participant:** open-text.tomlinson 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/31/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** boolean run based on rejoinder by plaintiff (same as otL07fb except that the plaintiff boolean query was used instead of the final query); note, for some topics, the depth-25000 limit prevented some lower-ranking matches from being included 

---
#### otL07rvl 
[**`Results`**](./results.md#otl07rvl), [**`Participants`**](./participants.md#open-texttomlinson), [**`Proceedings`**](./proceedings.md#experiments-with-the-negotiated-boolean-queries-of-the-trec-2007-legal-discovery-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.otL07rvl.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.otL07rvl.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/otL07rvl.main.pdf) 

- :material-rename: **Run ID:** otL07rvl 
- :fontawesome-solid-user-group: **Participant:** open-text.tomlinson 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/28/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** vector run based on request text terms (same as otL07fv except (1) the terms were taken from the request text field instead of the final boolean field, (2) English inflections were matched, (3) common instruction words (e.g. "please", "produce", "documents") were manually removed) 

---
#### otRF07fb 
[**`Results`**](./results.md#otrf07fb), [**`Participants`**](./participants.md#open-texttomlinson), [**`Proceedings`**](./proceedings.md#experiments-with-the-negotiated-boolean-queries-of-the-trec-2007-legal-discovery-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.otRF07fb.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.otRF07fb.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/otRF07fb.routing.pdf) 

- :material-rename: **Run ID:** otRF07fb 
- :fontawesome-solid-user-group: **Participant:** open-text.tomlinson 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/3/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** routing 
- :material-text: **Run description:** boolean run based on final negotiated query (same as reference boolean run refL06B except re-ordered by relevance, and for some non-interactive topics, the depth-26000 limit prevented some lower-ranking matches from being included) 

---
#### otRF07fv 
[**`Results`**](./results.md#otrf07fv), [**`Participants`**](./participants.md#open-texttomlinson), [**`Proceedings`**](./proceedings.md#experiments-with-the-negotiated-boolean-queries-of-the-trec-2007-legal-discovery-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.otRF07fv.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.otRF07fv.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/otRF07fv.routing.pdf) 

- :material-rename: **Run ID:** otRF07fv 
- :fontawesome-solid-user-group: **Participant:** open-text.tomlinson 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/3/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** routing 
- :material-text: **Run description:** vector run based on final negotiated query (same approach as otL07fv) 

---
#### sab07legrf1 
[**`Results`**](./results.md#sab07legrf1), [**`Participants`**](./participants.md#sabirbuckley), [**`Proceedings`**](./proceedings.md#examining-overfitting-in-relevance-feedback-sabir-research-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.sab07legrf1.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.sab07legrf1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/sab07legrf1.routing.pdf) 

- :material-rename: **Run ID:** sab07legrf1 
- :fontawesome-solid-user-group: **Participant:** sabir.buckley 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/18/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** routing 
- :material-text: **Run description:** Optimize weights using up to top 50 Rocchio weighted terms.  Limit number of expansion terms to avoid overfitting by automatic determination from split collection. 

---
#### sab07legrf2 
[**`Results`**](./results.md#sab07legrf2), [**`Participants`**](./participants.md#sabirbuckley), [**`Proceedings`**](./proceedings.md#examining-overfitting-in-relevance-feedback-sabir-research-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.sab07legrf2.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.sab07legrf2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/sab07legrf2.routing.pdf) 

- :material-rename: **Run ID:** sab07legrf2 
- :fontawesome-solid-user-group: **Participant:** sabir.buckley 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** routing 
- :material-text: **Run description:** Optimized weights from legal 06 judgements, using all top 100 Rocchio terms for all topics (no attempt to avoid overfitting). 

---
#### sab07legrf3 
[**`Results`**](./results.md#sab07legrf3), [**`Participants`**](./participants.md#sabirbuckley), [**`Proceedings`**](./proceedings.md#examining-overfitting-in-relevance-feedback-sabir-research-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.sab07legrf3.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.sab07legrf3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/sab07legrf3.routing.pdf) 

- :material-rename: **Run ID:** sab07legrf3 
- :fontawesome-solid-user-group: **Participant:** sabir.buckley 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** routing 
- :material-text: **Run description:** Same as run rf1, except rf1 inadvertantly used only judgments on odd-numbered docs from legal06, this uses all judgements, and is to be preferred in judging if possible. 

---
#### SabL07ab1 
[**`Results`**](./results.md#sabl07ab1), [**`Participants`**](./participants.md#sabirbuckley), [**`Proceedings`**](./proceedings.md#examining-overfitting-in-relevance-feedback-sabir-research-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.SabL07ab1.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.SabL07ab1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/SabL07ab1.main.pdf) 

- :material-rename: **Run ID:** SabL07ab1 
- :fontawesome-solid-user-group: **Participant:** sabir.buckley 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** blind feedback, expansion by 20 terms from top 30 docs 

---
#### SabL07ar1 
[**`Results`**](./results.md#sabl07ar1), [**`Participants`**](./participants.md#sabirbuckley), [**`Proceedings`**](./proceedings.md#examining-overfitting-in-relevance-feedback-sabir-research-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.SabL07ar1.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.SabL07ar1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/SabL07ar1.main.pdf) 

- :material-rename: **Run ID:** SabL07ar1 
- :fontawesome-solid-user-group: **Participant:** sabir.buckley 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Basic tfidf vector run on request field only.  Run on full OCR collection. 

---
#### SabL07ar2 
[**`Results`**](./results.md#sabl07ar2), [**`Participants`**](./participants.md#sabirbuckley), [**`Proceedings`**](./proceedings.md#examining-overfitting-in-relevance-feedback-sabir-research-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.SabL07ar2.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.SabL07ar2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/SabL07ar2.main.pdf) 

- :material-rename: **Run ID:** SabL07ar2 
- :fontawesome-solid-user-group: **Participant:** sabir.buckley 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Basic tfidf vector run on request field only.  Same as ar1 except run on collection with most OCR terms deleted. 

---
#### SabL07arbn 
[**`Results`**](./results.md#sabl07arbn), [**`Participants`**](./participants.md#sabirbuckley), [**`Proceedings`**](./proceedings.md#examining-overfitting-in-relevance-feedback-sabir-research-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.SabL07arbn.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.SabL07arbn.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/SabL07arbn.main.pdf) 

- :material-rename: **Run ID:** SabL07arbn 
- :fontawesome-solid-user-group: **Participant:** sabir.buckley 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Simple vector run using request plus boolean queries.  Initial search corresponding to blind feedback run bf1 

---
#### sableg07i1 
[**`Results`**](./results.md#sableg07i1), [**`Participants`**](./participants.md#sabirbuckley), [**`Proceedings`**](./proceedings.md#examining-overfitting-in-relevance-feedback-sabir-research-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.sableg07i1.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.sableg07i1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/interactive.pdf) 

- :material-rename: **Run ID:** sableg07i1 
- :fontawesome-solid-user-group: **Participant:** sabir.buckley 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/15/2007 
- :material-text-search: **Task:** interactive 

---
#### UIowa07LegE0 
[**`Results`**](./results.md#uiowa07lege0), [**`Participants`**](./participants.md#uiowaeichman), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UIowa07LegE0.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UIowa07LegE0.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UIowa07LegE0.main.pdf) 

- :material-rename: **Run ID:** UIowa07LegE0 
- :fontawesome-solid-user-group: **Participant:** uiowa.eichman 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** baseline run - standard analysis of OCR and request text 

---
#### UIowa07LegE1 
[**`Results`**](./results.md#uiowa07lege1), [**`Participants`**](./participants.md#uiowaeichman), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UIowa07LegE1.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UIowa07LegE1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UIowa07LegE1.main.pdf) 

- :material-rename: **Run ID:** UIowa07LegE1 
- :fontawesome-solid-user-group: **Participant:** uiowa.eichman 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/6/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** 3-4 ngram analysis on OCR and request text 

---
#### UIowa07LegE2 
[**`Results`**](./results.md#uiowa07lege2), [**`Participants`**](./participants.md#uiowaeichman), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UIowa07LegE2.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UIowa07LegE2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UIowa07LegE2.main.pdf) 

- :material-rename: **Run ID:** UIowa07LegE2 
- :fontawesome-solid-user-group: **Participant:** uiowa.eichman 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** standard analysis on OCR, translation of boolean query 

---
#### UIowa07LegE3 
[**`Results`**](./results.md#uiowa07lege3), [**`Participants`**](./participants.md#uiowaeichman), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UIowa07LegE3.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UIowa07LegE3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UIowa07LegE3.main.pdf) 

- :material-rename: **Run ID:** UIowa07LegE3 
- :fontawesome-solid-user-group: **Participant:** uiowa.eichman 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** 3-4 ngram analysis of OCR w/ boolean query 

---
#### UIowa07LegE4 
[**`Results`**](./results.md#uiowa07lege4), [**`Participants`**](./participants.md#uiowaeichman), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UIowa07LegE4.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UIowa07LegE4.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UIowa07LegE4.main.pdf) 

- :material-rename: **Run ID:** UIowa07LegE4 
- :fontawesome-solid-user-group: **Participant:** uiowa.eichman 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** standard analysis on OCR with pseudo-relevance feedback on persons (authors, recipients and mentions) and production boxes 

---
#### UIowa07LegE5 
[**`Results`**](./results.md#uiowa07lege5), [**`Participants`**](./participants.md#uiowaeichman), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UIowa07LegE5.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UIowa07LegE5.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UIowa07LegE5.main.pdf) 

- :material-rename: **Run ID:** UIowa07LegE5 
- :fontawesome-solid-user-group: **Participant:** uiowa.eichman 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/6/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** ngram analysis on OCR with pseudo-relevance feedback on persons (authors, recipients and mentions) and production boxes 

---
#### UMass10 
[**`Results`**](./results.md#umass10), [**`Participants`**](./participants.md#umassallan), [**`Proceedings`**](./proceedings.md#ciir-experiments-for-trec-legal-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMass10.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMass10.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMass10.main.pdf) 

- :material-rename: **Run ID:** UMass10 
- :fontawesome-solid-user-group: **Participant:** umass.allan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/16/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** This is a hand edited version of the automatic queries generated for UMass11.  It uses only the request text field. 

---
#### UMass11 
[**`Results`**](./results.md#umass11), [**`Participants`**](./participants.md#umassallan), [**`Proceedings`**](./proceedings.md#ciir-experiments-for-trec-legal-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMass11.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMass11.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMass11.main.pdf) 

- :material-rename: **Run ID:** UMass11 
- :fontawesome-solid-user-group: **Participant:** umass.allan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/16/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** This run is automatically generated from the RequestText field only.  The only metadata field used is date.  

---
#### UMass12 
[**`Results`**](./results.md#umass12), [**`Participants`**](./participants.md#umassallan), [**`Proceedings`**](./proceedings.md#ciir-experiments-for-trec-legal-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMass12.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMass12.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMass12.main.pdf) 

- :material-rename: **Run ID:** UMass12 
- :fontawesome-solid-user-group: **Participant:** umass.allan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/16/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** This run is automatically generated from the final BooleanQuery field only.  The only metadata field used is date.  

---
#### UMass13 
[**`Results`**](./results.md#umass13), [**`Participants`**](./participants.md#umassallan), [**`Proceedings`**](./proceedings.md#ciir-experiments-for-trec-legal-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMass13.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMass13.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMass13.main.pdf) 

- :material-rename: **Run ID:** UMass13 
- :fontawesome-solid-user-group: **Participant:** umass.allan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/16/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** This run combines the queries generated from the requestText field (UMass11) and the final booleanQuery (UMass12).  The only metadata field used is date.  

---
#### UMass14 
[**`Results`**](./results.md#umass14), [**`Participants`**](./participants.md#umassallan), [**`Proceedings`**](./proceedings.md#ciir-experiments-for-trec-legal-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMass14.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMass14.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMass14.main.pdf) 

- :material-rename: **Run ID:** UMass14 
- :fontawesome-solid-user-group: **Participant:** umass.allan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/29/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** A term dependence model that makes use of phrases and term proximity was used on request text. 

---
#### UMass15 
[**`Results`**](./results.md#umass15), [**`Participants`**](./participants.md#umassallan), [**`Proceedings`**](./proceedings.md#ciir-experiments-for-trec-legal-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMass15.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMass15.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMass15.main.pdf) 

- :material-rename: **Run ID:** UMass15 
- :fontawesome-solid-user-group: **Participant:** umass.allan 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/29/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** A term dependence model that makes use of phrases and term proximity was used on request text. In addition, a standard pseudo-relevance feedback technique was employed. 

---
#### UMKC1 
[**`Results`**](./results.md#umkc1), [**`Participants`**](./participants.md#umkczhao), [**`Proceedings`**](./proceedings.md#evaluation-of-query-formulations-in-the-negotiated-query-refinement-process-of-legal-e-discovery-umkc-at-trec-2007-legal-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMKC1.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMKC1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMKC1.main.pdf) 

- :material-rename: **Run ID:** UMKC1 
- :fontawesome-solid-user-group: **Participant:** umkc.zhao 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/30/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** PBDf9E80LMa8b9.run  --> UMKC1.run 

---
#### UMKC2 
[**`Results`**](./results.md#umkc2), [**`Participants`**](./participants.md#umkczhao), [**`Proceedings`**](./proceedings.md#evaluation-of-query-formulations-in-the-negotiated-query-refinement-process-of-legal-e-discovery-umkc-at-trec-2007-legal-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMKC2.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMKC2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMKC2.main.pdf) 

- :material-rename: **Run ID:** UMKC2 
- :fontawesome-solid-user-group: **Participant:** umkc.zhao 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/30/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** RTf9E80LMa8b9.run  --> UMKC2 

---
#### UMKC3 
[**`Results`**](./results.md#umkc3), [**`Participants`**](./participants.md#umkczhao), [**`Proceedings`**](./proceedings.md#evaluation-of-query-formulations-in-the-negotiated-query-refinement-process-of-legal-e-discovery-umkc-at-trec-2007-legal-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMKC3.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMKC3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMKC3.main.pdf) 

- :material-rename: **Run ID:** UMKC3 
- :fontawesome-solid-user-group: **Participant:** umkc.zhao 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/30/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** FQf9E80LMa8b9.run  --> UMKC3 

---
#### UMKC4 
[**`Results`**](./results.md#umkc4), [**`Participants`**](./participants.md#umkczhao), [**`Proceedings`**](./proceedings.md#evaluation-of-query-formulations-in-the-negotiated-query-refinement-process-of-legal-e-discovery-umkc-at-trec-2007-legal-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMKC4.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMKC4.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMKC4.main.pdf) 

- :material-rename: **Run ID:** UMKC4 
- :fontawesome-solid-user-group: **Participant:** umkc.zhao 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/30/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** PBDf9E80.run --> UMKC4 

---
#### UMKC5 
[**`Results`**](./results.md#umkc5), [**`Participants`**](./participants.md#umkczhao), [**`Proceedings`**](./proceedings.md#evaluation-of-query-formulations-in-the-negotiated-query-refinement-process-of-legal-e-discovery-umkc-at-trec-2007-legal-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMKC5.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMKC5.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMKC5.main.pdf) 

- :material-rename: **Run ID:** UMKC5 
- :fontawesome-solid-user-group: **Participant:** umkc.zhao 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/30/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** RTf9E80.run --> UMKC5 

---
#### UMKC6 
[**`Results`**](./results.md#umkc6), [**`Participants`**](./participants.md#umkczhao), [**`Proceedings`**](./proceedings.md#evaluation-of-query-formulations-in-the-negotiated-query-refinement-process-of-legal-e-discovery-umkc-at-trec-2007-legal-track), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.UMKC6.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.UMKC6.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/UMKC6.main.pdf) 

- :material-rename: **Run ID:** UMKC6 
- :fontawesome-solid-user-group: **Participant:** umkc.zhao 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/30/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** FQf9E80.run --> UMKC6 

---
#### ursinus1 
[**`Results`**](./results.md#ursinus1), [**`Participants`**](./participants.md#ursinus-collegekontostathis), [**`Proceedings`**](./proceedings.md#on-retrieving-legal-files-shortening-documents-and-weeding-out-garbage), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.ursinus1.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.ursinus1.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/ursinus1.main.pdf) 

- :material-rename: **Run ID:** ursinus1 
- :fontawesome-solid-user-group: **Participant:** ursinus-college.kontostathis 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/22/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** request text, fourth root norm, no ocr, query pruning w/ old query file 

---
#### ursinus2 
[**`Results`**](./results.md#ursinus2), [**`Participants`**](./participants.md#ursinus-collegekontostathis), [**`Proceedings`**](./proceedings.md#on-retrieving-legal-files-shortening-documents-and-weeding-out-garbage), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.ursinus2.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.ursinus2.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/ursinus2.main.pdf) 

- :material-rename: **Run ID:** ursinus2 
- :fontawesome-solid-user-group: **Participant:** ursinus-college.kontostathis 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/23/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** request text, cube root norm, no ocr, query pruning w/ old query file 

---
#### ursinus3 
[**`Results`**](./results.md#ursinus3), [**`Participants`**](./participants.md#ursinus-collegekontostathis), [**`Proceedings`**](./proceedings.md#on-retrieving-legal-files-shortening-documents-and-weeding-out-garbage), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.ursinus3.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.ursinus3.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/ursinus3.main.pdf) 

- :material-rename: **Run ID:** ursinus3 
- :fontawesome-solid-user-group: **Participant:** ursinus-college.kontostathis 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/24/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** sqrt norm, no ocr, query pruning 

---
#### ursinus4 
[**`Results`**](./results.md#ursinus4), [**`Participants`**](./participants.md#ursinus-collegekontostathis), [**`Proceedings`**](./proceedings.md#on-retrieving-legal-files-shortening-documents-and-weeding-out-garbage), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.ursinus4.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.ursinus4.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/ursinus4.main.pdf) 

- :material-rename: **Run ID:** ursinus4 
- :fontawesome-solid-user-group: **Participant:** ursinus-college.kontostathis 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/24/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** log norm, no ocr, query pruning 

---
#### ursinus5 
[**`Results`**](./results.md#ursinus5), [**`Participants`**](./participants.md#ursinus-collegekontostathis), [**`Proceedings`**](./proceedings.md#on-retrieving-legal-files-shortening-documents-and-weeding-out-garbage), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.ursinus5.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.ursinus5.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/ursinus5.main.pdf) 

- :material-rename: **Run ID:** ursinus5 
- :fontawesome-solid-user-group: **Participant:** ursinus-college.kontostathis 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/24/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** cos norm, no ocr, query pruning 

---
#### ursinus6 
[**`Results`**](./results.md#ursinus6), [**`Participants`**](./participants.md#ursinus-collegekontostathis), [**`Proceedings`**](./proceedings.md#on-retrieving-legal-files-shortening-documents-and-weeding-out-garbage), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.ursinus6.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.ursinus6.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/ursinus6.main.pdf) 

- :material-rename: **Run ID:** ursinus6 
- :fontawesome-solid-user-group: **Participant:** ursinus-college.kontostathis 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/24/2007 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** cube rt norm, ocr on, query pruning 

---
#### ursinus7 
[**`Results`**](./results.md#ursinus7), [**`Participants`**](./participants.md#ursinus-collegekontostathis), [**`Proceedings`**](./proceedings.md#on-retrieving-legal-files-shortening-documents-and-weeding-out-garbage), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.ursinus7.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.ursinus7.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/ursinus7.main.pdf) 

- :material-rename: **Run ID:** ursinus7 
- :fontawesome-solid-user-group: **Participant:** ursinus-college.kontostathis 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/25/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** cube rt norm, ocr off, query pruning, manual (played with boolean query) 

---
#### ursinus8 
[**`Results`**](./results.md#ursinus8), [**`Participants`**](./participants.md#ursinus-collegekontostathis), [**`Proceedings`**](./proceedings.md#on-retrieving-legal-files-shortening-documents-and-weeding-out-garbage), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.ursinus8.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.ursinus8.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/ursinus8.main.pdf) 

- :material-rename: **Run ID:** ursinus8 
- :fontawesome-solid-user-group: **Participant:** ursinus-college.kontostathis 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 7/25/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** cos norm, ocr off, query pruning, manual (played with boolean query) 

---
#### Washington 
[**`Results`**](./results.md#washington), [**`Participants`**](./participants.md#uwashefthimiadis), [**`Proceedings`**](./proceedings.md#university-of-washington-uw-at-legal-trec-interactive-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.Washington.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.Washington.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/interactive.pdf) 

- :material-rename: **Run ID:** Washington 
- :fontawesome-solid-user-group: **Participant:** uwash.efthimiadis 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/15/2007 
- :material-text-search: **Task:** interactive 

---
#### wat1fuse 
[**`Results`**](./results.md#wat1fuse), [**`Participants`**](./participants.md#uwaterlooclarke), [**`Proceedings`**](./proceedings.md#multitext-legal-experiments-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.wat1fuse.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.wat1fuse.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/wat1fuse.main.pdf) 

- :material-rename: **Run ID:** wat1fuse 
- :fontawesome-solid-user-group: **Participant:** uwaterloo.clarke 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Fusion of 6 runs. 

---
#### wat2nobool 
[**`Results`**](./results.md#wat2nobool), [**`Participants`**](./participants.md#uwaterlooclarke), [**`Proceedings`**](./proceedings.md#multitext-legal-experiments-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.wat2nobool.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.wat2nobool.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/wat2nobool.main.pdf) 

- :material-rename: **Run ID:** wat2nobool 
- :fontawesome-solid-user-group: **Participant:** uwaterloo.clarke 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Same as wat1fuse, but with boolean results excluded. 

---
#### wat3desc 
[**`Results`**](./results.md#wat3desc), [**`Participants`**](./participants.md#uwaterlooclarke), [**`Proceedings`**](./proceedings.md#multitext-legal-experiments-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.wat3desc.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.wat3desc.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/wat3desc.main.pdf) 

- :material-rename: **Run ID:** wat3desc 
- :fontawesome-solid-user-group: **Participant:** uwaterloo.clarke 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Description only field. 

---
#### wat4feed 
[**`Results`**](./results.md#wat4feed), [**`Participants`**](./participants.md#uwaterlooclarke), [**`Proceedings`**](./proceedings.md#multitext-legal-experiments-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.wat4feed.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.wat4feed.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/wat4feed.main.pdf) 

- :material-rename: **Run ID:** wat4feed 
- :fontawesome-solid-user-group: **Participant:** uwaterloo.clarke 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Pseudo-relevance feedback (only feedback terms - character 4grams) 

---
#### wat5nofeed 
[**`Results`**](./results.md#wat5nofeed), [**`Participants`**](./participants.md#uwaterlooclarke), [**`Proceedings`**](./proceedings.md#multitext-legal-experiments-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.wat5nofeed.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.wat5nofeed.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/wat5nofeed.main.pdf) 

- :material-rename: **Run ID:** wat5nofeed 
- :fontawesome-solid-user-group: **Participant:** uwaterloo.clarke 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Fusion, no pseudo-relevance feedback. 

---
#### wat6qap 
[**`Results`**](./results.md#wat6qap), [**`Participants`**](./participants.md#uwaterlooclarke), [**`Proceedings`**](./proceedings.md#multitext-legal-experiments-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.wat6qap.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.wat6qap.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/wat6qap.main.pdf) 

- :material-rename: **Run ID:** wat6qap 
- :fontawesome-solid-user-group: **Participant:** uwaterloo.clarke 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** term proximity ranking 

---
#### wat7bool 
[**`Results`**](./results.md#wat7bool), [**`Participants`**](./participants.md#uwaterlooclarke), [**`Proceedings`**](./proceedings.md#multitext-legal-experiments-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.wat7bool.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.wat7bool.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/wat7bool.main.pdf) 

- :material-rename: **Run ID:** wat7bool 
- :fontawesome-solid-user-group: **Participant:** uwaterloo.clarke 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** ranked boolean 

---
#### wat8gram 
[**`Results`**](./results.md#wat8gram), [**`Participants`**](./participants.md#uwaterlooclarke), [**`Proceedings`**](./proceedings.md#multitext-legal-experiments-at-trec-2007), [**`Input`**](https://trec.nist.gov/results/trec16/legal/input.wat8gram.gz), [**`Summary`**](https://trec.nist.gov/results/trec16/legal/summary.wat8gram.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec16/appendices/legal/wat8gram.main.pdf) 

- :material-rename: **Run ID:** wat8gram 
- :fontawesome-solid-user-group: **Participant:** uwaterloo.clarke 
- :material-format-text: **Track:** Legal 
- :material-calendar: **Year:** 2007 
- :material-upload: **Submission:** 8/5/2007 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** character 4-grams 

---
