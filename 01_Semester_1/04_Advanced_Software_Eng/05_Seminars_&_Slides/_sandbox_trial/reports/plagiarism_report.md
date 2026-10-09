# Local Plagiarism & Style Report

- Document: `Ch5_Software_Design.md` (3291 words, 136 sentences)
- Corpus: 8 sources, 45428 words
- Note: similarity != plagiarism; this shows overlap with THIS local corpus only.

## 1. Verbatim overlap (k-gram shingles)

| k | doc shingles | matched in corpus | overlap |
|:--|--:|--:|--:|
| 6 | 3284 | 237 | 7.2% |
| 8 | 3284 | 160 | 4.9% |
| 10 | 3282 | 115 | 3.5% |

**Longest verbatim-matched phrases (>= 8 words): 25 found**

- (28 words) `is complete the problem should have been decomposed into many small functionally independent modules that are cohesive have low coupling among themselves and ar`
- (25 words) `once the high level design is complete detailed design is undertaken during detailed design each module is examined carefully to design its data structures and`
- (22 words) `modules are identified the outcome of high level design is called the program structure or the software architecture high level design is`
- (19 words) `reviewed by the members of the development team to ensure that the design solution conforms to the requirements specification`
- (17 words) `problem is decomposed into a set of modules the control relationships among the modules are identified and`
- (15 words) `levels of procedural detail a hierarchy is developed by decomposing a macroscopic statement of function`
- (21 words) `data in the system how will the system look to users what choices will be offered to users what is the`
- (18 words) `per cent of the total effort in the life cycle of a typical product is spent on maintenance`
- (13 words) `abstraction is the elimination of the irrelevant and the amplification of the essentials`
- (10 words) `the relevant data structures modules external interfaces and module interconnections`
- (14 words) `the design document the design document produced at the end of the design phase`
- (11 words) `be implementable using a programming language in the subsequent coding phase`
- (11 words) `algorithms the outcome of the detailed design stage is usually documented`
- (11 words) `the following items are designed and documented during the design phase`
- (10 words) `in a stepwise fashion until programming language statements are reached`

## 2. TF-IDF cosine similarity (document vs each source)

| Source | Cosine |
|:--|--:|
| pressman_ch13_design | 0.416 |
| agarwal2010_systemdesign | 0.407 |
| pressman_coupling_cohesion | 0.400 |
| mall_ch5_design | 0.349 |
| agarwal2010_design | 0.313 |
| kkaggarwal_slides_ch5 | 0.263 |
| sommerville_ch6 | 0.218 |
| agarwal2010_lowlevel | 0.185 |

## 3. Sentence-level near-match (rapidfuzz, best match >= 80)

Sentences with a >=80 token-set match: **27 / 136**

- **100**  doc: `The design process transforms the SRS document into the design document.`
   — closest source: `5.1 OVERVIEW OF THE DESIGN PROCESS
The design process essentially transforms the SRS document into a
design do`
- **100**  doc: `The following items are designed and documented during the design phase.`
   — closest source: `5.1.1 Outcome of the Design Process
The following items are designed and documented during the design
phase.`
- **100**  doc: `Once the high-level design is complete, detailed design is undertaken.`
   — closest source: `Once the high-level design is complete, detailed design is undertaken.`
- **100**  doc: `During detailed design each module is examined carefully to design its data structures and its algorithms.`
   — closest source: `During detailed design each module is examined carefully to design its data structures
and the algorithms.`
- **100**  doc: `Abstraction is the elimination of the irrelevant and the amplification of the essentials.`
   — closest source: `Abstraction is the elimination of the irrelevant and the amplification of 
the essentials.`
- **100**  doc: `What will happen to the data in the system?`
   — closest source: `
What will happen to data in the system?`
- **100**  doc: `How will the system look to users?`
   — closest source: `
How will the system look to users?`
- **100**  doc: `What choices will be offered to users?`
   — closest source: `
What choices will be offered to users?`
- **99**  doc: `The outcome of high-level design is called the program structure, or the software architecture.`
   — closest source: `The outcome of high-level design is called the program structure or the
software architecture.`
- **98**  doc: `The reason is that a design technique requires the designer to make many subjective decisions and to work out `
   — closest source: `The reason is that a
design technique often requires the designer to make many subjective
decisions and work o`
- **96**  doc: `First, the different modules required by the solution are identified; each module is a collection of functions`
   — closest source: `Each
module should be named according to the task it performs.`
- **95**  doc: `A large number of methodologies exist, but they can be roughly classified into two approaches — the procedural`
   — closest source: `These
two approaches are two fundamentally different design paradigms.`
- **95**  doc: `How will the reports and screens look like?`
   — closest source: `
How will the reports & screens look like?`
- **95**  doc: `What is the timing of events?`
   — closest source: `
What is the timings of events?`
- **94**  doc: `High-level design is the crucial step of the whole design: when it is complete, the problem should have been d`
   — closest source: `When the high-level design is complete, the problem should
have been decomposed into many small functionally i`

## 4. Style metrics

- Sentence length: mean 23.9, std 11.3, **burstiness (std/mean) 0.47**
- Type-Token Ratio: 0.280
- MTLD/MSTTR: 0.838
- Flesch-Kincaid grade: 14.2 | Flesch reading ease: 34.3
- AI/slop phrase hits: 2  `it is worth noting`×1, `leverage`×1
