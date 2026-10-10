# Label semantic spot check

Deterministic human-review sample: the first 10 sorted record IDs for every domain/label pair. No LLM or automatic relabeling was used.

Use this report to inspect whether `single_hop` tends toward direct fact lookup, `multi_hop` tends to combine facts, and `summary` tends toward aggregation or summarization. These tendencies do not authorize label rewriting.

## graphragBench_medical

### single_hop

- `graphragBench_medical_0000` — What is the most common type of skin cancer? _(facts: 1; row: 0; source: `<local-path>`)_
- `graphragBench_medical_0001` — From which cell type does basal cell carcinoma arise? _(facts: 1; row: 1; source: `<local-path>`)_
- `graphragBench_medical_0002` — Which anatomical locations are most commonly affected by basal cell carcinoma? _(facts: 1; row: 2; source: `<local-path>`)_
- `graphragBench_medical_0003` — What is the primary risk factor for basal cell carcinoma? _(facts: 1; row: 3; source: `<local-path>`)_
- `graphragBench_medical_0004` — How does fair skin affect the risk of developing BCC? _(facts: 1; row: 4; source: `<local-path>`)_
- `graphragBench_medical_0005` — Does older age influence the risk of basal cell carcinoma? _(facts: 1; row: 5; source: `<local-path>`)_
- `graphragBench_medical_0006` — How does family history impact the risk of basal cell carcinoma? _(facts: 1; row: 6; source: `<local-path>`)_
- `graphragBench_medical_0007` — Is immune suppression a risk factor for BCC? _(facts: 1; row: 7; source: `<local-path>`)_
- `graphragBench_medical_0008` — What are common symptoms of basal cell carcinoma? _(facts: 1; row: 8; source: `<local-path>`)_
- `graphragBench_medical_0009` — Which diagnostic methods are used for BCC? _(facts: 1; row: 9; source: `<local-path>`)_

### multi_hop

- `graphragBench_medical_1098` — Why is a patient with fair skin and a history of organ transplant at particularly high risk for developing basal cell carcinoma? _(facts: 1; row: 1098; source: `<local-path>`)_
- `graphragBench_medical_1099` — If a patient presents with a shiny bump on the face and has a history of tanning bed use, what diagnostic steps should be taken to evaluate for basal cell carcinoma? _(facts: 1; row: 1099; source: `<local-path>`)_
- `graphragBench_medical_1100` — How does the management of recurrent basal cell carcinoma differ from initial treatment, and what factors influence this? _(facts: 1; row: 1100; source: `<local-path>`)_
- `graphragBench_medical_1101` — Which combination of risk factors should prompt earlier and more frequent skin exams for BCC? _(facts: 1; row: 1101; source: `<local-path>`)_
- `graphragBench_medical_1102` — Why might a patient with a shiny bump and a history of radiation therapy require both imaging and biopsy for diagnosis? _(facts: 1; row: 1102; source: `<local-path>`)_
- `graphragBench_medical_1103` — What follow-up strategy is recommended for a patient treated for BCC on the neck, and why? _(facts: 1; row: 1103; source: `<local-path>`)_
- `graphragBench_medical_1104` — How does UV radiation contribute to both the development and recurrence of basal cell carcinoma? _(facts: 1; row: 1104; source: `<local-path>`)_
- `graphragBench_medical_1105` — Why should a patient with a family history of skin cancer and light eye color be particularly vigilant about skin changes? _(facts: 1; row: 1105; source: `<local-path>`)_
- `graphragBench_medical_1106` — What is the rationale for recommending surgery as the most common treatment for BCC lesions on sun-exposed areas? _(facts: 1; row: 1106; source: `<local-path>`)_
- `graphragBench_medical_1107` — Which symptoms and risk factors together would most strongly indicate the need for biopsy to rule out BCC? _(facts: 1; row: 1107; source: `<local-path>`)_

### summary

- `graphragBench_medical_1607` — What are the main risk factors associated with the development of basal cell carcinoma? _(facts: 1; row: 1607; source: `<local-path>`)_
- `graphragBench_medical_1608` — Which anatomical locations and cell types are most commonly involved in basal cell carcinoma? _(facts: 1; row: 1608; source: `<local-path>`)_
- `graphragBench_medical_1609` — What are the typical symptoms and presentations of basal cell carcinoma? _(facts: 1; row: 1609; source: `<local-path>`)_
- `graphragBench_medical_1610` — Which diagnostic methods are used to confirm basal cell carcinoma and what does the process involve? _(facts: 1; row: 1610; source: `<local-path>`)_
- `graphragBench_medical_1611` — What are the standard treatment options for basal cell carcinoma? _(facts: 1; row: 1611; source: `<local-path>`)_
- `graphragBench_medical_1612` — What constitutes recurrence in basal cell carcinoma and how is it managed? _(facts: 1; row: 1612; source: `<local-path>`)_
- `graphragBench_medical_1613` — What follow-up practices are recommended after treatment for basal cell carcinoma? _(facts: 1; row: 1613; source: `<local-path>`)_
- `graphragBench_medical_1614` — How does a patient’s medical and family history contribute to the diagnosis and risk assessment of basal cell carcinoma? _(facts: 1; row: 1614; source: `<local-path>`)_
- `graphragBench_medical_1615` — What are the connections between risk factors, symptoms, and anatomical location in basal cell carcinoma? _(facts: 1; row: 1615; source: `<local-path>`)_
- `graphragBench_medical_1616` — What are the major risk factors and disease locations associated with primary CNS lymphoma? _(facts: 1; row: 1616; source: `<local-path>`)_

## musique

### single_hop

- `musique_2590` — What is the alternative title of the 1919 British silent drama film 'The Soul of Guilda Lois'? _(facts: 1; row: 2590; source: `<local-path>`)_
- `musique_2591` — What is the title of the 14-minute cutout animation film produced by Ishu Patel in 1971? _(facts: 1; row: 2591; source: `<local-path>`)_
- `musique_2592` — What is the population of Los Alamos, California according to the 2010 census? _(facts: 1; row: 2592; source: `<local-path>`)_
- `musique_2593` — What type of celestial feature is Vashakidze? _(facts: 1; row: 2593; source: `<local-path>`)_
- `musique_2594` — Who was the author of the drawings of animals for the game Animal Husbandry? _(facts: 1; row: 2594; source: `<local-path>`)_
- `musique_2595` — What was M. King Hubbert's profession? _(facts: 1; row: 2595; source: `<local-path>`)_
- `musique_2596` — What is the name of the fictional character from the CBS soap opera The Young and the Restless? _(facts: 1; row: 2596; source: `<local-path>`)_
- `musique_2597` — What is the title of the album by Kenny Dorham featuring Ernie Henry that was recorded in 1957? _(facts: 1; row: 2597; source: `<local-path>`)_
- `musique_2598` — What is the objective of Phase III of the Somali Transitional Federal Government's reconstruction plan for Somali Post? _(facts: 1; row: 2598; source: `<local-path>`)_
- `musique_2599` — What did Friedrich Hayek claim about the relationship between unlimited democracy and other forms of unlimited government? _(facts: 1; row: 2599; source: `<local-path>`)_

### multi_hop

- `musique_0000` — Who is the spouse of the Green performer? _(facts: 2; row: 0; source: `<local-path>`)_
- `musique_0001` — Who founded the company that distributed the film UHF? _(facts: 2; row: 1; source: `<local-path>`)_
- `musique_0002` — What administrative territorial entity is the owner of Ciudad Deportiva located? _(facts: 2; row: 2; source: `<local-path>`)_
- `musique_0003` — Where is Ulrich Walter's employer headquartered? _(facts: 2; row: 3; source: `<local-path>`)_
- `musique_0004` — Which company owns the manufacturer of Learjet 60? _(facts: 2; row: 4; source: `<local-path>`)_
- `musique_0005` — Who is the child of Caroline LeRoy's spouse? _(facts: 2; row: 5; source: `<local-path>`)_
- `musique_0006` — Who is the grandmother of Philippe, Duke of Orléans? _(facts: 2; row: 6; source: `<local-path>`)_
- `musique_0007` — What is the goal of the group that European Movement Germany is a member of? _(facts: 2; row: 7; source: `<local-path>`)_
- `musique_0008` — What company succeeded the owner of Empire Sports Network? _(facts: 2; row: 8; source: `<local-path>`)_
- `musique_0009` — What province shares a border with the province where Lago District is located? _(facts: 2; row: 9; source: `<local-path>`)_

### summary

- `musique_2988` — Based on the provided documents, what does the geographic and administrative diversity of the state of Minnesota, within the United States, encompass? _(facts: 5; row: 2988; source: `<local-path>`)_
- `musique_2989` — What does the information reveal about the diversity of geographic and media entities within the province of Quebec, Canada? _(facts: 5; row: 2989; source: `<local-path>`)_
- `musique_2990` — Based on the provided documents, how do the examples of French Polynesia and a French music album illustrate the cultural and administrative reach of France? _(facts: 5; row: 2990; source: `<local-path>`)_
- `musique_2991` — What significant developments occurred in the year 2010 across different sectors such as sports and social issues? _(facts: 5; row: 2991; source: `<local-path>`)_
- `musique_2992` — How does the political structure of Australia, as a federation of states, relate to specific examples of places and individuals within one of its states, such as Victoria? _(facts: 5; row: 2992; source: `<local-path>`)_
- `musique_2993` — How do the provided documents portray India's position both as a participant in global systems and as a nation facing significant domestic challenges? _(facts: 5; row: 2993; source: `<local-path>`)_
- `musique_2994` — Based on the provided documents, what are some of the significant roles or associations of the city of Cologne, Germany? _(facts: 5; row: 2994; source: `<local-path>`)_
- `musique_2995` — Based on the provided documents, what are some of the diverse professional, media, and cultural roles that New York City plays? _(facts: 5; row: 2995; source: `<local-path>`)_
- `musique_2996` — What were some notable events and transitions associated with the year 2006 across different fields? _(facts: 5; row: 2996; source: `<local-path>`)_
- `musique_2997` — How do the provided documents illustrate the multifaceted nature of England across different domains such as culture, sports, and history? _(facts: 5; row: 2997; source: `<local-path>`)_

## quality

### single_hop

- `quality_0461` — What is the name of the man who swung a full bottle at Kregg's head? _(facts: 1; row: 461; source: `<local-path>`)_
- `quality_0462` — Who is the assistant being sent with Nordon to Saarkkad V? _(facts: 1; row: 462; source: `<local-path>`)_
- `quality_0463` — What did the acrobats do after the circle with garlands of flowers bowed out? _(facts: 1; row: 463; source: `<local-path>`)_
- `quality_0464` — What is the name of the Captain mentioned in the passage? _(facts: 1; row: 464; source: `<local-path>`)_
- `quality_0465` — What did people used to call the art-works carved by lonely men in faraway places? _(facts: 1; row: 465; source: `<local-path>`)_
- `quality_0466` — What did O'Reilley say he was going upstairs to get? _(facts: 1; row: 466; source: `<local-path>`)_
- `quality_0467` — What is the name of the Stortulian female that the male Stortulian claims is his spouse? _(facts: 1; row: 467; source: `<local-path>`)_
- `quality_0468` — Who is described as bending over the narrator when they wake up? _(facts: 1; row: 468; source: `<local-path>`)_
- `quality_0469` — What species do the two captive aliens identify themselves as? _(facts: 1; row: 469; source: `<local-path>`)_
- `quality_0470` — What did the narrator ask Skippy to call at the roulette wheel in Jake's spot? _(facts: 1; row: 470; source: `<local-path>`)_

### multi_hop

- `quality_0000` — In the document where Dan is accused of being a crook, what is the budgeting method mentioned in the document that discusses distributed consensus and resistance to state control? _(facts: 2; row: 0; source: `<local-path>`)_
- `quality_0001` — In the story where a boy runs along picturing a wonderland with a rockslide of petrified logs and waves higher than anything, what is the name of the one from the group described in those thrilling tales who was shot? _(facts: 2; row: 1; source: `<local-path>`)_
- `quality_0002` — Who was given the fastest vessel ever made by man to find radium to halt the Plague, according to the person the speaker mentions as being like the listener and whose name makes one think of a Biblical character but is anything but that, referred to as just plain Jake? _(facts: 2; row: 2; source: `<local-path>`)_
- `quality_0003` — What is the name of the character who thought over the idea of being freed by the notable thing for the author about the "Left Behind" series? _(facts: 2; row: 3; source: `<local-path>`)_
- `quality_0004` — In the story where a man uses the instrument used to ray his face and later exchanged for a syringe and razor blade, what is the title of the work? _(facts: 2; row: 4; source: `<local-path>`)_
- `quality_0005` — What field is associated with the OA repository mentioned in the document where Sam Jenkins administers an intravenous flask? _(facts: 2; row: 5; source: `<local-path>`)_
- `quality_0006` — In the first document, a character exclaims 'Arragh! I should have my head examined. I've got a plugged tube somewhere!' What is the name of the self-destructive passion of the actor described in the second document as beautiful, brazenly slim-hipped, who doesn't make his lines sound as if he's thinking them up on the spot? _(facts: 2; row: 6; source: `<local-path>`)_
- `quality_0007` — What is the full name of the apprentice burnerman mentioned in the document that follows the conversation where a character tells another character, whose face flushed and animated and who was called a coward, to smile when saying that, and asks if there are tears in his sweet grey eyes? _(facts: 2; row: 7; source: `<local-path>`)_
- `quality_0008` — What is the waiver rate at Harvard for the group that the Bethesda Statement, Berlin Declaration, and the author's refined BBB definition of Open Access (including terms like green, gold, gratis, libre) are primarily addressed to or concern? _(facts: 2; row: 8; source: `<local-path>`)_
- `quality_0009` — On what planet did the bright, shining object that circled Earth, visible as a bright spot of light during the day and seeming to burn through sunset colors at evening, described as a little piece clipped from the center of a star, have handie-talkies with practically nonexistent range due to the planet being a 'dead spot'? _(facts: 2; row: 9; source: `<local-path>`)_

### summary

- `quality_0915` — Based on the documents, how is the planet Earth characterized in terms of its technological status, political influence, and its relationship with other worlds in the solar system? _(facts: 5; row: 915; source: `<local-path>`)_
- `quality_0916` — In the provided documents, how is the floor used as a setting to establish atmosphere and facilitate conflict? _(facts: 5; row: 916; source: `<local-path>`)_
- `quality_0917` — Based on the documents, how is life aboard a ship in space depicted as a combination of routine operations and sudden, dangerous events? _(facts: 5; row: 917; source: `<local-path>`)_
- `quality_0918` — Based on the documents, what functions and qualities are attributed to the voice in narratives involving communication under tension or between different beings? _(facts: 5; row: 918; source: `<local-path>`)_
- `quality_0919` — Based on the documents, how is the state of the world characterized, particularly in terms of its unity and the threats it faces? _(facts: 5; row: 919; source: `<local-path>`)_
- `quality_0920` — Based on the provided documents, how is the experience and technology of space travel depicted, particularly its challenges and evolution? _(facts: 5; row: 920; source: `<local-path>`)_
- `quality_0921` — Based on the provided documents, how is light portrayed in contrasting technological or magical contexts? _(facts: 5; row: 921; source: `<local-path>`)_
- `quality_0922` — Based on the provided documents, what are the different roles and limitations of money as a motivator and a resource? _(facts: 5; row: 922; source: `<local-path>`)_
- `quality_0923` — Based on the provided documents, how do the described cities or towns exert control or confinement over outsiders or inhabitants? _(facts: 5; row: 923; source: `<local-path>`)_
- `quality_0924` — Based on the provided documents, what role does water play in the various scenarios of confinement, survival, and travel? _(facts: 5; row: 924; source: `<local-path>`)_

## ultraDomain_legal

### single_hop

- `ultraDomain_legal_0526` — What does 'Affected Financial Institution' mean according to the passage? _(facts: 1; row: 526; source: `<local-path>`)_
- `ultraDomain_legal_0527` — What is the name of the limited partnership agreement that was amended and restated as of February 11, 2020? _(facts: 1; row: 527; source: `<local-path>`)_
- `ultraDomain_legal_0528` — What is the name of the entity that is the surviving company in the merger signed on August 10, 2020? _(facts: 1; row: 528; source: `<local-path>`)_
- `ultraDomain_legal_0529` — What is the title of Erik Nelson at MOUNTAIN SHARE TRANSFER LLC? _(facts: 1; row: 529; source: `<local-path>`)_
- `ultraDomain_legal_0530` — What is the title of Richard Kirk von Seelen at PAE GOVERNMENT SERVICES, INC.? _(facts: 1; row: 530; source: `<local-path>`)_
- `ultraDomain_legal_0531` — What is the permit/approval status of the Letter Order Granting Approval for Installation of Structural Steel (Docket No. CP11-72-000)? _(facts: 1; row: 531; source: `<local-path>`)_
- `ultraDomain_legal_0532` — What is the date of the Purchase Agreement mentioned in the passage? _(facts: 1; row: 532; source: `<local-path>`)_
- `ultraDomain_legal_0533` — What is the amount of the Senior Debt Commitment mentioned in the passage? _(facts: 1; row: 533; source: `<local-path>`)_
- `ultraDomain_legal_0534` — What is the status of the Letter Order Granting Approval to Install In-Tank Pumps and Vacuum Relief Valves? _(facts: 1; row: 534; source: `<local-path>`)_
- `ultraDomain_legal_0535` — What is the beneficial ownership of Lincoln Park Capital Fund, LLC in the company's common stock as of the date of the Purchase Agreement? _(facts: 1; row: 535; source: `<local-path>`)_

### multi_hop

- `ultraDomain_legal_0000` — According to the document chain, what entity is described as having legal, valid, and binding obligations enforceable in accordance with their terms, following the entity that prepared the Actuarial Analysis and was provided factual information by the Cedant and its Affiliates? _(facts: 2; row: 0; source: `<local-path>`)_
- `ultraDomain_legal_0001` — What is the entity with the power to issue additional Partnership Interests, as appropriate, in connection with the..., according to the parties who have the right to seek satisfaction when Seller fails to handle taxes or pay wages? _(facts: 2; row: 1; source: `<local-path>`)_
- `ultraDomain_legal_0002` — According to the document chain, what entity, on whose behalf the Purchasers act, to which all Purchased Receivables have been sold, is referenced in relation to the termination event that occurs when the First Additional Prepayment Market Value equals or exceeds the First Additional Maximum Valuation Threshold prior to the Final Delivery Date? _(facts: 2; row: 2; source: `<local-path>`)_
- `ultraDomain_legal_0003` — According to the agreement made as of April 27, 2020, between AltaLink Investments, L.P., as Borrower, and AltaLink Investment Management, what type of claims result in indemnity not being available as determined by a court? _(facts: 2; row: 3; source: `<local-path>`)_
- `ultraDomain_legal_0004` — According to the document detailing the Borrower's policies on Anti-Corruption Laws and Sanctions, what entity requires prior written consent for actions adverse to the party made a third-party beneficiary under Section 9.8 of the agreement referenced in the document discussing waiver provisions? _(facts: 2; row: 4; source: `<local-path>`)_
- `ultraDomain_legal_0005` — According to the document, what term is defined as occurring when the Borrower’s non-credit-enhanced senior unsecured long-term debt is downgraded below Investment Grade by each Rating Agency, based on representations made prior to the date before which litigation must be disclosed to Buyer to avoid a breach of representation? _(facts: 2; row: 5; source: `<local-path>`)_
- `ultraDomain_legal_0006` — According to the document that prohibits entering into any Commodity Hedge Agreement other than the Minimum Required Commodity Hedge Agreements or liquidating them, what is the specific thing that is also prohibited from being established or maintained, as referenced in the form of security or credit support mentioned in the document discussing the Eligibility Reserve Period and due diligence on Accounts and spare parts inventory? _(facts: 2; row: 6; source: `<local-path>`)_
- `ultraDomain_legal_0007` — According to the Agreement involving the Purchaser signing the document with signatories Camilo Alvarado and Natalie Koven, in which courts may legal suits arising from the Agreement be instituted? _(facts: 2; row: 7; source: `<local-path>`)_
- `ultraDomain_legal_0008` — If the document that must be accompanied by invoices from Tenant evidencing expenditure of FF&E Costs and, for work creating lien rights, lien waivers satisfactory to Landlord is not prepared or submitted by the specified date, who may prepare and submit a proposed Program or Budget to the Board for approval? _(facts: 2; row: 8; source: `<local-path>`)_
- `ultraDomain_legal_0009` — According to the Spanish law governing a first-ranking pledge over shares with a COVID-19 related extension clause, what must the Company receive from each Purchaser in order to include such Purchaser's shares of Common Stock in the Registration Statement under the agreement entered into in connection with the Purchase Agreement? _(facts: 2; row: 9; source: `<local-path>`)_

### summary

- `ultraDomain_legal_0896` — Based on the provided legal documents, what are the common characteristics and the legal standing of the Agreement as a formal contract? _(facts: 5; row: 896; source: `<local-path>`)_
- `ultraDomain_legal_0897` — Based on the provided legal documents, what are the key conditions and legal finality events that govern the enforceability, suspension, or termination of a contractual obligation? _(facts: 5; row: 897; source: `<local-path>`)_
- `ultraDomain_legal_0898` — What is the legal framework surrounding 'this Agreement', including its related documents, how it can be amended, and how disputes about its interpretation are resolved? _(facts: 5; row: 898; source: `<local-path>`)_
- `ultraDomain_legal_0899` — What are the key legal and corporate prerequisites for the valid delivery and performance of agreements by an entity? _(facts: 5; row: 899; source: `<local-path>`)_
- `ultraDomain_legal_0900` — Based on the provided documents, what is described about the process and conditions for making an amendment to a formal agreement? _(facts: 5; row: 900; source: `<local-path>`)_
- `ultraDomain_legal_0901` — Based on the provided legal and financial documents, what is the scope of materials relevant to a claim, and how are parties expected to handle the notification and indemnification process for such claims? _(facts: 5; row: 901; source: `<local-path>`)_
- `ultraDomain_legal_0902` — How is the term 'Person' defined and operationally contextualized within the provided legal and financial agreements? _(facts: 5; row: 902; source: `<local-path>`)_
- `ultraDomain_legal_0903` — What are the key legal conditions and restrictions commonly embedded in financial and restructuring documents to govern transactions and ensure compliance? _(facts: 5; row: 903; source: `<local-path>`)_
- `ultraDomain_legal_0904` — What are the key legal principles governing the parties to the agreements described in the documents? _(facts: 5; row: 904; source: `<local-path>`)_
- `ultraDomain_legal_0905` — What are the key legal and financial implications of termination as described in the provided documents on agreements and benefits? _(facts: 5; row: 905; source: `<local-path>`)_
