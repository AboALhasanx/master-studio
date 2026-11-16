# Chapter 7 — Source Report for the Four Examiner Notes

**Scope and verification.** This report checks the four notes against `ch7_part1.md` and the source inventory named in the handoff. DOI links below were opened through `doi.org` and cross-checked against publisher or Crossref records. A DOI error in the earlier draft has been corrected: `10.1145/1005959.1005965` is John D. Musa's 1983 article “Stimulating software engineering progress,” not the Musa–Okumoto ICSE model paper. The corrected DOI list below contains only identifiers matched to the cited publication. No Chapter 7 source or deliverable was edited.

## Note 1 — Name the Goel–Okumoto model explicitly

**Status in our chapter:** Missing by name. `ch7_part1.md` discusses NHPP reliability growth but contains no “Goel” or “Okumoto” mention. The handoff’s scan of the book OCR and course sources found “Okumoto” only in a bibliography entry, not as a named model.

**Candidate sources:**

- Amrit L. Goel and Kazu Okumoto, “Time-Dependent Error-Detection Rate Model for Software Reliability and Other Performance Measures,” *IEEE Transactions on Reliability*, R-28(3), 206–211 (1979). DOI: [10.1109/TR.1979.5220566](https://doi.org/10.1109/TR.1979.5220566). The resolver lands on IEEE Xplore document 5220566; the IEEE record confirms the title.
- National Research Council, “Software Reliability Growth,” in *Reliability Growth: Enhancing Defense System Reliability*, Chapter 9, pp. 117–124 (2015). DOI: [10.17226/18987](https://doi.org/10.17226/18987). The National Academies Press identifies the model as an NHPP and gives its mean value function.
- Daniel R. Jeske and Qi Zhang, “Assessing the Validity of One-Part Software Reliability Models Using Likelihood Ratio and Early Detection Tests,” *Journal of Systems and Software*, 80(6), 805–816 (2007). DOI: [10.1016/j.jss.2006.10.016](https://doi.org/10.1016/j.jss.2006.10.016). The publisher page names the model and states the mean value function.

**Evidence:** The National Academies chapter explicitly labels the section “Goel-Okumoto Model” and gives its mean value function. The ScienceDirect record for Jeske and Zhang includes an indexed excerpt naming it “A widely used NHPP model” and showing `M(t; θ) = a(1 − e^(−bt))`; the article's full text was not independently inspected, so that excerpt is not treated here as a verified quotation from the complete paper. Differentiating the National Academies mean value function gives `λ(t) = ab e^(−bt)`.

**What we would add to the chapter:**

> **Goel–Okumoto NHPP model.** A widely used non-homogeneous Poisson process model for software reliability growth is the Goel–Okumoto model. Its mean value function is `m(t) = a(1 − e^(−bt))`, where `a` is the expected eventual number of detected failures and `b` is the detection-rate parameter; therefore, its failure intensity is `λ(t) = dm(t)/dt = ab e^(−bt)`. The parameters are estimated from observed failure data.

**Risk:** The name and equations are absent from the five course sources surveyed, so this is an external addition. The original article’s DOI and metadata are verified. The National Academies is the full-text-checked secondary source for the model name and mean-value equation; Jeske–Zhang is a useful supporting record, but its cited wording should not be presented as a full-text-verified quotation until the article itself is read. Avoid calling it “the most famous” or “canonical” unless the instructor wants that stronger wording; the sources establish that it is widely used, not a ranked claim.

## Note 2 — Place the hardware bathtub curve beside the software failure-rate curve

**Status in our chapter:** Present but split. The handoff reports Figure 7.1 on PDF page 5 and Figure 7.2 on page 6. In `ch7_part1.md`, the hardware bathtub curve and software failure-rate curve appear consecutively, with separate captions.

**Candidate sources:**

- Inder M. Soi and Krishna Gopal, “Hardware vs Software Reliability—A Comparative Study,” *Microelectronics Reliability*, 20(6), 881–885 (1980). DOI: [10.1016/0026-2714(80)90012-8](https://doi.org/10.1016/0026-2714(80)90012-8). The publisher describes the article as a comparison of hardware and software reliability definitions, theories, and trends.
- National Institute of Standards and Technology, [“‘Bathtub’ Curve,” NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/apr/section1/apr124.htm). This is an authoritative reference for the hardware curve and its life-cycle phases.
- Philip Koopman, Carnegie Mellon University, [“Software Reliability”](https://users.ece.cmu.edu/~koopman/des_s99/sw_reliability/index.html). This teaching resource shows the hardware bathtub curve and a possible software failure-rate curve in its figures, making the conceptual comparison explicit.

**Evidence (verbatim quote):** Soi and Gopal write that their paper “presents a comparative study between hardware reliability and software reliability.” Koopman’s page labels the hardware figure the “bathtub curve” and follows it with a software curve.

**What we would add to the chapter:** Place the existing `fig7_1_bathtub.png` and `fig7_2_sw_reliability.png` beside one another on the same page, retaining their separate captions and axes. No external diagram needs to be downloaded for this layout change. Keep the hardware bathtub curve and software curve visually distinct; do not imply that software physically wears out like hardware or that both curves share an identical failure mechanism.

**Risk:** The DOI article supports the hardware–software comparison, while NIST supports the hardware curve; the Carnegie Mellon page provides an accessible visual comparator. The request to put the figures on one page is an editorial layout decision, not a scientific claim that a particular layout improves learning. The existing chapter assets are sufficient. The NIST and Carnegie Mellon pages are free to view; no explicit reuse license for the Carnegie Mellon figure was verified, so use it as a reference rather than copying it into the chapter.

## Note 3 — One-page comparison of the Basic and Logarithmic Poisson models

**Status in our chapter:** Partially present. Sections 7.3.1 and 7.3.2 define both models and give their equations and cumulative-mean behavior. Table 7.13 compares five models using four different headings. The requested two-row table organized by assumption, `λ(μ)` shape, finite asymptote, and use is not present.

**Candidate sources:**

- John D. Musa, “Software Reliability Measurement,” *Journal of Systems and Software*, 1, 223–241 (1979). DOI: [10.1016/0164-1212(79)90023-2](https://doi.org/10.1016/0164-1212(79)90023-2). The publisher record describes an execution-time reliability theory and the associated testing/debugging model.
- John D. Musa and Kazuhira Okumoto, “A Comparison of Time Domains for Software Reliability Models,” *Journal of Systems and Software*, 4(4), 277–287 (1984). DOI: [10.1016/0164-1212(84)90027-X](https://doi.org/10.1016/0164-1212(84)90027-X). Crossref and the publisher record match this title and these authors. This is a related time-domain comparison paper; it is not the ICSE paper and should not be cited as its replacement.
- John D. Musa and Kazuhira Okumoto, “Application of Basic and Logarithmic Poisson Execution Time Models in Software Reliability Measurement,” in *Software Reliability Modelling and Identification*, Lecture Notes in Computer Science 341, 68–100 (1988). Chapter DOI: [10.1007/BFb0034287](https://doi.org/10.1007/BFb0034287). Springer’s chapter record identifies both authors, both models, and the comparison; its abstract says “Two software reliability models” are compared using project failure data.

**DOI correction:** The bibliographic record for the ICSE 1984 paper “A Logarithmic Poisson Execution Time Model for Software Reliability Measurement,” pp. 230–238, is independently identifiable, but no correct DOI for that conference paper was verified in this check. Do not attach `10.1145/1005959.1005965`: Crossref resolves it to John D. Musa, “Stimulating software engineering progress,” *ACM SIGSOFT Software Engineering Notes*, 8(2), 29–54 (1983). The Springer chapter above is the verified DOI-backed source that directly compares the basic and logarithmic models.

**Evidence (verbatim quote):** Springer’s chapter title names both models and its abstract confirms that the authors compare them. The local chapter’s equations in Sections 7.3.1–7.3.2 give the relationships below.

**What we would add to the chapter:**

| Assumption | Shape of failure intensity `λ(μ)` | Finite cumulative-mean asymptote? | When to use |
|:--|:--|:--|:--|
| **Basic execution-time model:** NHPP; intensity is proportional to the remaining failures in a finite population `V₀`. | Linear decrease: `λ(μ) = λ₀(1 − μ/V₀)`. | **Yes.** `μ(τ) = V₀[1 − exp(−λ₀τ/V₀)] → V₀` as `τ → ∞`. | Use when a finite eventual failure count is a reasonable modeling assumption and the observed failure data support it. |
| **Logarithmic Poisson model:** NHPP; intensity decreases exponentially with failures experienced, with no finite cap on the cumulative mean. | Exponential decrease: `λ(μ) = λ₀ exp(−θμ)`. | **No.** `μ(τ) = (1/θ) ln(1 + λ₀θτ) → ∞` as `τ → ∞`. | Use when the data support this unbounded-mean form and a finite `V₀` is not assumed; compare model fit before selecting it. |

**Risk:** The formulas and limits are mathematical consequences of the two model definitions and are consistent with the chapter’s equations. “When to use” is deliberately stated as a data- and assumption-based selection rule, not a universal empirical ranking. “No finite asymptote” is a property of the model’s cumulative mean, not a literal claim that real software contains infinitely many faults.

## Note 4 — Make reliability’s dependence on the operational profile explicit

**Status in our chapter:** Conceptually present; explicit generalized statement missing. Section 7.1.10’s library example says librarians and members can have different views of the same product because they execute different functions. Section 7.3.9 explains that statistical testing and its reliability estimate are tied to an operational profile. Neither section states in one direct sentence that the same software system may have different reliability values under different profiles.

**Candidate sources:**

- National Research Council, “Software Reliability Growth,” in *Reliability Growth: Enhancing Defense System Reliability*, Chapter 9 (2015). DOI: [10.17226/18987](https://doi.org/10.17226/18987). The chapter states that the same software system can have different reliability values for different operational use profiles.
- John D. Musa, “Operational Profiles in Software-Reliability Engineering,” *IEEE Software*, 10(2), 14–32 (1993). DOI: [10.1109/52.199724](https://doi.org/10.1109/52.199724). The article defines the operational profile as a quantitative description of system use and explains how it guides test allocation.
- Süleyman Özekici and Refik Soyer, “Reliability of Software with an Operational Profile,” *European Journal of Operational Research*, 149(2), 459–474 (2003). DOI: [10.1016/S0377-2217(02)00461-7](https://doi.org/10.1016/S0377-2217(02)00461-7). The publisher’s abstract says failure characteristics depend on the operation being performed and that reliability assessment is made for a specific operational profile.

**Evidence (verbatim quotes):** The National Academies chapter says the same system can have “different reliability values in relation to different software operational use profiles.” Özekici and Soyer state that “the failure characteristics depend on the specific operation performed.” Musa describes an operational profile as a “quantitative characterization of how a system will be used.”

**What we would add to the chapter:**

> Software reliability is conditional on the operational profile used to define or measure its operation. Therefore, the same program version can have different operational reliability under two profiles when those profiles assign different probabilities to operations with different conditional failure probabilities. Reliability estimates should be reported together with the operational profile to which they apply.

**Risk:** The central claim is directly supported by the National Academies and by the peer-reviewed operational-profile model of Özekici and Soyer. The condition matters: changing profile weights does not necessarily change reliability if the operations have identical conditional failure probabilities. Keep the same program version, environment, and observation period fixed when explaining the comparison.

## DOI verification record

| DOI | Resolver destination checked | Result |
|:--|:--|:--|
| `10.1109/TR.1979.5220566` | IEEE Xplore, document 5220566 | Resolved to the matching IEEE article record |
| `10.17226/18987` | National Academies Press, publication 18987 | Resolved to the cited book and chapter |
| `10.1016/j.jss.2006.10.016` | Elsevier/ScienceDirect, article PII S0164121206002792 | Resolved to the matching article record |
| `10.1016/0026-2714(80)90012-8` | Elsevier/ScienceDirect, article PII 0026271480900128 | Resolved to the matching article record |
| `10.1016/0164-1212(79)90023-2` | Elsevier, article PII 0164121279900232 | Resolved to the matching article record |
| `10.1016/0164-1212(84)90027-X` | Elsevier / *Journal of Systems and Software* | Resolved and matched to “A Comparison of Time Domains for Software Reliability Models,” Musa and Okumoto, 1984, pp. 277–287 |
| `10.1007/BFb0034287` | SpringerLink chapter page | Resolved to the matching Musa–Okumoto chapter |
| `10.1109/52.199724` | IEEE Xplore, document 199724 | Resolved to the matching IEEE article record |
| `10.1016/S0377-2217(02)00461-7` | Elsevier, article PII S0377221702004617 | Resolved to the matching article record |

**Rejected DOI from the earlier draft:** `10.1145/1005959.1005965` resolves to “Stimulating software engineering progress,” John D. Musa, *ACM SIGSOFT Software Engineering Notes*, 8(2), 29–54 (1983). It is not cited as evidence for Note 3. Crossref's `created` timestamp is a metadata deposit date, not the publication year; the bibliographic years above follow the publisher publication records.

## Full-text and download access

| Source | Access checked | What this means for the chapter work |
|:--|:--|:--|
| National Research Council, *Reliability Growth* (2015) | The National Academies provides a free PDF download as a guest; an email and acceptance of its terms are required. The book can also be read online. | Download is optional for the layout task. It is a useful full-text source for the model and operational-profile statements. |
| NIST/SEMATECH e-Handbook | Public web page and its bathtub-curve figure are freely viewable. | No download is needed; cite the page if its definition is used. |
| Koopman, Carnegie Mellon University, “Software Reliability” | Public lecture web page with separate hardware and software curve figures. | No download is needed. Use as a visual reference only; reuse permission for its images was not established. |
| IEEE, ACM, Elsevier, and Springer publications listed above | DOI pages and bibliographic records are resolvable, but full-text access varies by article and subscription. A resolvable DOI does not mean the PDF is open access. | Do not download all papers by default. Obtain a full text only when an exact quotation or a claim unavailable in the abstract/record must be checked. The Jeske–Zhang phrase currently comes from a publisher-indexed excerpt, not a full-text inspection. |

**Figure decision:** The chapter already has both required local image assets (`fig7_1_bathtub.png` and `fig7_2_sw_reliability.png`). A paired same-page layout can use them directly; no outside figure download is necessary. Do not treat free viewing as permission to reproduce a third-party figure.

**Chapter-file boundary:** This task wrote only this report. The final Git status shows modified and untracked files in the Reliability Seminar folder; none were edited during this research task. I did not capture a pre-task Git status, so I cannot establish when those existing working-tree changes were made.

