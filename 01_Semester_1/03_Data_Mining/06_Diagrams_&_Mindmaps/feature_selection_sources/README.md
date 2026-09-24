# Feature Selection — Source Figures

Figures extracted **verbatim** from the two Data-Mining textbooks, cropped at 300 DPI.
Used in the Feature-Selection ملزمة and seminar. Kept here (not copied wholesale) because the repository is public.

| File | Figure | Source |
|:--|:--|:--|
| `fig_HK_3-6_greedy_methods.png` | Figure 3.6 — Greedy (heuristic) methods for attribute subset selection | **Han, Kamber & Pei, *Data Mining: Concepts and Techniques*, 3rd ed., Morgan Kaufmann, 2011**, p. 104 |
| `fig_AG_10-1_gini_entropy.png` | Figure 10.1 — Variation of two feature selection criteria with class distribution skew | **Aggarwal, *Data Mining: The Textbook*, Springer, 2015**, p. 289 |
| `fig_AG_10-2_fisher_direction.png` | Figure 10.2 — Impact of class distribution on Fisher's discriminating direction | **Aggarwal, *Data Mining: The Textbook*, Springer, 2015**, p. 291 |
| `fig_AG_6-1_distance_entropy.png` | Figure 6.1 — Impact of clustered data on distance distribution entropy | **Aggarwal, *Data Mining: The Textbook*, Springer, 2015**, p. 156 |
| `fig_AG_2-2_correlated_axis.png` | Figure 2.2 — Highly correlated data represented in a small number of dimensions in a rotated axis system | **Aggarwal, *Data Mining: The Textbook*, Springer, 2015**, p. 41 |

**Provenance:** cropped with PyMuPDF (300 DPI) directly from the local PDFs in `../../02_Raw_Materials/`.
**Note:** Fig. 2.2 is about *dimensionality reduction (PCA)* and is included only to illustrate the *redundancy* idea — the seminar itself stays scoped to Feature Selection.

---

## Web-sourced explanatory diagrams (Wikimedia Commons, **CC BY-SA 4.0**)

| File | What it shows | Source & credit |
|:--|:--|:--|
| `web_decision_tree_depth2.png` | a decision tree: internal tests, branches, class leaves | "Decision Tree Depth 2" — **CollaborativeGeneticist**, CC BY-SA 4.0, via Wikimedia Commons |
| `web_fs_filter.png` | the **filter** pipeline: all features → best subset → learning algorithm → performance | "Filter Methode" — **Lucien Mousin**, CC BY-SA 4.0, via Wikimedia Commons |
| `web_fs_wrapper.png` | the **wrapper** loop: generate subset ⇄ learning algorithm → performance | "Feature selection Wrapper Method" — **Lastdreamer7591**, CC BY-SA 4.0, via Wikimedia Commons |
| `web_fs_embedded.png` | the **embedded** model: selection folded into the learning algorithm | "Feature selection Embedded Method" — **Lastdreamer7591**, CC BY-SA 4.0, via Wikimedia Commons |
| `web_fs_three_models.png` | **composite** (stacked + labelled) of the three above — used on one seminar slide | assembled locally with Pillow from the three CC BY-SA files above |

> **Attribution is mandatory** for the CC BY-SA 4.0 images (the repository is public). They are credited on the deck's final "References and image credits" slide and here.
> **Downloaded via** the Wikimedia Commons API (search → imageinfo → direct fetch), verified as real PNGs, and visually inspected before use.
