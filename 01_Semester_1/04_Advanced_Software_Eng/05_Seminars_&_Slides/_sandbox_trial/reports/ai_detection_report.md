# AI-text detection report v2 (calibrated)

- Document: `Ch5_Software_Design.md` (8168 words, 340 sentences)
- Models: observer `gpt2`, performer `gpt2`
- Human baseline: `sommerville_ch6.txt`
- CAUTION: an indicator for editing, not proof of authorship.

## Detectors (document vs known-human baseline)

| Metric | Document | Human baseline | Reference |
|:--|--:|--:|:--|
| Fast-DetectGPT curvature (mean) | **0.07** | 0.14 | machine~3, human~0 |
| Binoculars score | **0.913** | 0.929 | AI<0.85, human>0.9 |

**Verdict (curvature): human-like** : document curvature is close to the human baseline.

## Per-sentence curvature (most AI-like first)

- +0.83  `What will happen to the data in the system?`
- +0.71  `A good design is the key to a successful product.`
- +0.60  `The relationship between the two parts is best understood as a contract.`
- +0.60  `The two documents describe the same system, but in different ways, because they are written for different audiences.`
- +0.58  `Once the high-level design is complete, detailed design is undertaken.`
- +0.58  `Each module has a single, well-defined purpose.`
- +0.52  `X and Y are part of a single functional task, which is a very good reason for them to be in the same procedure.`
- +0.51  `How will the system look to users?`
- +0.50  `Because the operations are linked by a real data flow, this is a strong reason to keep them together.`
- +0.50  `Each module is a well-defined subsystem that is potentially useful in other applications.`

## Stylometric signals

- Sentence-length burstiness: 0.53 (higher = more human)
- Sentence-curvature burstiness: nan
- Em-dashes: 0 | Rule-of-three triads: 57
- TTR 0.192 | Flesch-Kincaid 13.5