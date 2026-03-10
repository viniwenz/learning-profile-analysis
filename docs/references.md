# References & Variable Definitions

## 1. Theoretical Foundation

### 1.1 Theory of Multiple Intelligences (Gardner, 1983)

Howard Gardner proposed in *Frames of Mind* (1983) that human intelligence is not a single, fixed capacity, but rather a set of independent dimensions, each representing a distinct way of processing information. Gardner initially identified seven intelligences, later expanding to eight with the inclusion of Naturalist Intelligence (1995).

Each intelligence dimension is characterized by:
- Independent neurological basis
- Presence in individuals with exceptional abilities or specific deficits
- Identifiable core operations and developmental trajectory

Gardner's framework is recognized by Brazil's Ministry of Education (MEC) and is present in the pedagogical training of Brazilian educators, making it a defensible and contextually appropriate theoretical reference for this project.

**Core dimensions used in this project:**

| Intelligence | Description |
|---|---|
| Linguistic | Sensitivity to spoken and written language; ability to use language to accomplish goals |
| Logical-Mathematical | Capacity to analyze problems logically, carry out mathematical operations, and investigate issues scientifically |
| Spatial | Potential to recognize and manipulate the patterns of wide space as well as confined areas |
| Bodily-Kinesthetic | Potential of using one's whole body or parts of the body to solve problems or create products |
| Interpersonal | Capacity to understand the intentions, motivations, and desires of other people |
| Intrapersonal | Capacity to understand oneself, including feelings, fears and motivations |

> **Note:** Musical and Naturalist intelligences were intentionally excluded from this model's scope. Their measurement in a standard classroom setting requires observational instruments not available in the synthetic dataset context and also in a regular classroom.

---

### 1.2 Socioemotional Indicators

The Instituto Criativo explicitly mentions socioemotional competencies as a relevant dimension in the challenge statement. Socioemotional learning (SEL) refers to the process through which children develop essential skills for managing emotions, building relationships, and making responsible decisions.

For this project, two socioemotional indicators complement Gardner's dimensions:

**Emotional Regulation:** The ability to manage one's emotional responses in learning contexts — including frustration tolerance, focus maintenance, and behavioral self-control in the classroom.

**Engagement & Frequency:** A composite indicator reflecting the student's participation rate, task completion behavior, and active involvement in classroom activities. This variable captures behavioral patterns that cut across all intelligence dimensions.

---

## 2. Variable Definitions

The model uses **8 variables**, each mapped to a theoretical source and operationalized as a numeric score on a scale of **0 to 10**.

| # | Variable | Type | Scale | Theoretical Source | Description |
|---|---|---|---|---|---|
| 1 | `linguistic_score` | Numeric | 0–10 | Gardner (1983) — Linguistic | Performance in reading, writing, and verbal expression activities |
| 2 | `logical_math_score` | Numeric | 0–10 | Gardner (1983) — Logical-Mathematical | Performance in mathematical reasoning and logical problem-solving tasks |
| 3 | `spatial_score` | Numeric | 0–10 | Gardner (1983) — Spatial | Performance in visual, drawing, and spatial reasoning activities |
| 4 | `bodily_kinesthetic_score` | Numeric | 0–10 | Gardner (1983) — Bodily-Kinesthetic | Engagement and performance in physical, hands-on, and craft activities |
| 5 | `interpersonal_score` | Numeric | 0–10 | Gardner (1983) — Interpersonal | Quality of social interaction, collaboration and peer relationship skills |
| 6 | `intrapersonal_score` | Numeric | 0–10 | Gardner (1983) — Intrapersonal | Self-awareness, goal-setting behavior and capacity to reflect on own learning |
| 7 | `emotional_regulation` | Numeric | 0–10 | CASEL (2020) — Self-Management | Ability to manage frustration, maintain focus and regulate behavior in class |
| 8 | `engagement_frequency` | Numeric | 0–10 | Fredricks, Blumenfeld & Paris (2004) — Behavioral Engagement | Composite of attendance rate, task completion, and active classroom participation |

---

## 3. Variable Design Rationale

**Why 8 variables?**  
The chosen set provides broad coverage of the child's profile without introducing redundancy. Variables 1–6 capture intelligence dimensions directly derived from Gardner. Variables 7–8 address the socioemotional layer required by the Instituto Criativo's challenge statement.

**Why numeric scores (0–10)?**  
Continuous numerical variables allow direct application of K-Means clustering without requiring categorical encoding. They also facilitate normalization in the preprocessing step and produce interpretable cluster centroids.

**Why exclude musical and naturalist intelligence?**  
These dimensions require specialized observational instruments (music performance assessment, nature-based activities) that are not realistically available in the synthetic dataset context and would introduce poorly grounded synthetic values. Besides, it would also be difficult to replicate in regular classrooms in Brazil.

---

## 4. References

ARMSTRONG, T. *Inteligências Múltiplas na sala de aula*. Porto Alegre: Artmed, 2001.

ANTUNES, C. *As inteligências múltiplas e seus estímulos*. Campinas: Papirus, 1998.

BRASIL. Ministério da Educação. *Altas Habilidades/Superdotação: encorajando potenciais*. Brasília: MEC/SEESP, 2006.

BRASIL. Ministério da Educação. *Política Nacional de Educação Especial na Perspectiva da Educação Inclusiva*. Brasília: MEC/SEESP, 2008.

GARDNER, H. *Frames of Mind: The Theory of Multiple Intelligences*. New York: Basic Books, 1983.

GARDNER, H. *Inteligências Múltiplas: a teoria na prática*. Porto Alegre: Artmed, 1995.

MOISSA, B.; GASPARINI, I.; KEMCZINSKI, A. Educational Data Mining versus Learning Analytics: estamos reinventando a roda? *Anais do XXVI Simpósio Brasileiro de Informática na Educação (SBIE)*, 2015.

ALBUQUERQUE, J. G. M.; ABREU, M. T. C.; LIMA, I. N. O impacto da Inteligência Artificial na personalização do ensino. *Revista Brasileira de Ensino, Neurociência e Aprendizagem (Rebena)*, v. 9, 2024.

SANTOS, F. A. et al. Mapeamento sistemático da literatura brasileira sobre EDM e Learning Analytics. *Brazilian Journal of Development*, 2020.

CASEL. *CASEL's SEL Framework: What Are the Core Competence Areas and Where Are They Promoted?* Chicago: Collaborative for Academic, Social, and Emotional Learning, 2020.

FREDRICKS, J. A.; BLUMENFELD, P. C.; PARIS, A. H. School engagement: potential of the concept, state of the evidence. *Review of Educational Research*, v. 74, n. 1, p. 59–109, 2004.