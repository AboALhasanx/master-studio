
## 7.2 Software Quality

Our objective of software engineering is to produce good quality maintainable software in time and within budget. Here quality is very important. But what do we understand with the term "quality"? It is not easy to define quality. People understand quality, appreciate quality but the term may not be able to clearly express the same. It is like beauty which is very much in the eyes of the beholder.

Different people understand different meanings of quality like:

- conformance to requirements
- fitness for the purpose
- level of satisfaction

If a product is meeting its requirements, we may say it is a good quality product. We are assured with respect to requirements are clearly stated and cannot be misunderstood. Everything is measured and designed to requirements and if it matches, product is a quality product. If a car is product with a maximum speed of 150 km/hour and if it fails to achieve in the field, then it is not meeting the requirements. If two cars are designed with different style, performance and economy and both are up-to standards set for them, then both are quality cars.

When user uses the product and finds the product fit for its purpose, he/she feels that product is of good quality. If product is meeting user requirements, a feeling of satisfaction may emerge and this satisfaction is nothing but the satisfaction for quality.

In a broad sense, the users views of quality must deal with the product's ease of installation, operational efficiency, and convenience. If the product is easy to handle and we comfortably remember how to use it, then customer satisfaction level may increases.

Quality has many characteristics and some are related to each other. In software, the quality is commonly recognised as "lack of bugs" in the program. If a software has too many functional defects, then, it is not meeting its basic requirement of functionality. This is usually expressed in two ways:

1. Defect rate: number of defects per million lines of source code, per function point or any other unit.
2. Reliability: generally measured as number of failures per 't' hours of operation, mean time to failure or probability of failure free operation in a specified time under specified environment.

When we deal with software quality, a list of attributes is required to be defined that are appropriate for software. There are four attribute domains [DUNN90], which should be defined. These are usually the ones most trusted by the customer:

- Reliability
- Usability
- Maintainability
- Adaptability

These four attribute-domains can be divided into attributes that are more commonly understood by the software community and are given in Fig. 7.8. The details of software quality attributes are given in Table 7.4.

![fig7_8_quality_attributes.png|4.6]
*Figure 7.8. Software quality attributes.*

**Table 7.4: Software quality attributes**

| Sr. No. | Attribute | Definition |
|:--:|:--|:--|
| 1 | Reliability | The extent to which a software performs its intended functions without failure. |
| 2 | Correctness | The extent to which a software meets its specifications. |
| 3 | Consistency and precision | The extent to which a software is consistent and give results with precision. |
| 4 | Robustness | The extent to which a software tolerates the unexpected problems. |
| 5 | Simplicity | The extent to which a software is simple in its operations. |
| 6 | Traceability | The extent to which an error is traceable in order to fix it. |
| 7 | Usability | The extent of effort required to learn, operate and understand the functions of the software. |
| 8 | Accuracy | Meeting specifications with precision. |
| 9 | Clarity and accuracy of documentation | The extent to which documents are clearly and accurately written. |
| 10 | Conformity of operational environment | The extent to which a software is in conformity of operational environment. |
| 11 | Completeness | The extent to which a software has specified functions. |
| 12 | Efficiency | The amount of computing resources and code required by software to perform a function. |
| 13 | Testability | The effort required to test a software to ensure that it performs its intended functions. |
| 14 | Maintainability | The effort required to locate and fix an error during maintenance phase. |
| 15 | Modularity | It is the extent of ease to implement, test, debug and maintain the software. |
| 16 | Readability | The extent to which a software is readable in order to understand. |
| 17 | Adaptability | The extent to which a software is adaptable to new platforms and technologies. |
| 18 | Modifiability | The effort required to modify a software during maintenance phase. |
| 19 | Expandability | The extent to which a software is expandable without undesirable side effects. |
| 20 | Portability | The effort required to transfer a program from one platform to another platform. |

The attribute domain and attributes are also named as the factor and criteria. There are many models of software quality and some are discussed here.

### 7.2.1 McCall Software Quality Model

McCall et al. [MCCA77] model of software quality was introduced in 1977 and many quality factors were incorporated. The model distinguishes between two levels of quality attributes. Higher level quality attributes are known as quality factors. These are external attributes and can be measured directly. The second level of quality attributes is named as quality criteria. Quality criteria can be measured either subjectively or objectively. The software quality factors are organised in three product quality factors as shown in Fig. 7.9.

![fig7_9_quality_factors.png|3.5]
*Figure 7.9. Software quality factors.*

**(i) Product Operation:** Here, factors which are related to the operation of a product are combined. The factors are:

- Correctness
- Efficiency
- Integrity
- Reliability
- Usability

These five factors are related to operational performance, convenience, ease of usage and its correctness. These factors play a very significant role in building customer's satisfaction.

**(ii) Product Revision:** The factors which are required for testing and maintenance are combined and are given below:

- Maintainability
- Flexibility
- Testability

These factors pertain to the testing and maintainability of software. They give us idea about ease of maintenance, flexibility and testing effort. Hence, they are combined under the umbrella of product revision.

**(iii) Product Transition:** We may have to transfer a product from one platform to another platform or from one technology to another technology. The factors related to such a transfer are combined and are given below:

- Portability
- Reusability
- Interoperability

Most of the quality factors are explained in Table 7.4. The remaining factors are given in Table 7.5.

**Table 7.5: Remaining quality factors**

| Sr. No. | Quality factor | Purpose |
|:--:|:--|:--|
| 1 | Integrity | The extent to which access to software or data by the unauthorised persons can be controlled. |
| 2 | Flexibility | The effort required to modify an operational program. |
| 3 | Reusability | The extent to which a program can be reused in other applications. |
| 4 | Interoperability | The effort required to couple one system with another. |

**Quality criteria**

The second level of quality attributes are termed as quality criteria. We have eleven quality factors and each quality factor has many second level of quality attributes which are shown in Fig. 7.10. Second level quality attributes are internal attributes. However, users and managers are interested in the higher level external quality attributes. For example, we may not directly measure the reliability of a software system. We may however, directly measure the number of defects encountered so far. This direct measure can be used to obtain insight into the reliability of the system. This involves a theory of how the number of defects encountered relates to reliability, which can be ascertained on good grounds. For most other aspects of quality though, the relation between the attributes that can be measured directly and the external attributes we are interested in is less obvious, to say the least [VLIE 02]. The relationship between quality factors and quality criteria are given in Table 7.5(a). The definitions and details of these quality criteria are discussed in Table 7.5(b).

![fig7_10_mccall_model.png|3.3]
*Figure 7.10. McCall's quality model.*

**Table 7.5(b): Software quality criteria**

| Sr. No. | Quality criteria | Definition / Purpose |
|:--:|:--|:--|
| 1 | Operability | The ease of operation of the software. |
| 2 | Training | The ease with which new users can use the system. |
| 3 | Communicativeness | The ease with which inputs and outputs can be assimilated. |
| 4 | I/O volume | It is related to the I/O volume. |
| 5 | I/O rate | It is the indication of I/O rate. |
| 6 | Access control | The provisions for control and protection of the software and data. |
| 7 | Access audit | The ease with which software and data can be checked for compliance with standards or other requirements. |
| 8 | Storage efficiency | The run-time storage requirements of the software. |
| 9 | Execution efficiency | The run-time efficiency of the software. |
| 10 | Traceability | The ability to link software components to requirements. |
| 11 | Completeness | The degree to which a full implementation of the required functionality has been achieved. |
| 12 | Accuracy | The precision of computations and output. |
| 13 | Error tolerance | The degree to which continuity of operation is ensured under adverse conditions. |
| 14 | Consistency | The use of uniform design and implementation techniques and notations throughout a project. |
| 15 | Simplicity | The ease with which the software can be understood. |
| 16 | Conciseness | The compactness of the source code, in terms of lines of code. |
| 17 | Instrumentation | The degree to which the software provides for measurements of its use or identification of errors. |
| 18 | Expandability | The degree to which storage requirements or software functions can be expanded. |
| 19 | Generality | The breadth of the potential application of software components. |
| 20 | Self-descriptiveness | The degree to which the documents are self-explanatory. |
| 21 | Modularity | The provision of highly independent modules. |
| 22 | Machine independence | The degree to which software is dependent on its associated hardware. |
| 23 | Software system independence | The degree to which software is independent of its environment. |
| 24 | Communication commonality | The degree to which standard protocols and interfaces are used. |
| 25 | Data commonality | The use of standard data representations. |

It is not easy to measure many quality factors. We may have to apply software metrics, if possible, to measure such factors. The quality factors are not independent, but may overlap. Some factors may impact others in a positive sense, while others may do so negatively. We may have to study and understand such relationships very carefully. A subjective assessment of some criteria can be obtained by giving a rating on a scale from, say, 0 (extremely bad) to 10 (extremely good). Such a subjective metric is difficult to use. Different people assessing the same criterion are likely to give different ratings. This renders a proper quality assessment almost impossible.

There are other methods to assessing quality like decomposing criterion into objectively measurable properties of the system. It is also difficult to measure every property objectively but aim is to define correctly and measure effectively.

### 7.2.2 Boehm Software Quality Model

Boehm introduced his quality model in 1978 [BOEH78]. He has defined three levels for quality attributes which are given in Fig. 7.11. These levels are primary uses, intermediate constructs and primitive constructs. Intermediate constructs are similar to McCall's quality factors and primitive constructs are similar to quality criteria. Hence Boehm's model is similar to McCall's model in that it presents a hierarchy of characteristics, each of which contributes to overall quality. Boehm's notion of successful software includes the needs and expectations of users, as does McCall's, however, it also includes characteristics of hardware performance that are missing in McCall's model [PFLE 02].

![fig7_11_boehm_model.png|5.4]
*Figure 7.11. The Boehm software quality model.*

The users must find the system easy to use. Thus human engineering aspect can sometime be the most critical. A system may be very good from performance point of view, but if user cannot understand how to use it, the system is a failure. The Boehm's model asserts that quality software is software that satisfies the needs of the users. It reflects an understanding of quality where the software:

- does what the user wants it to do
- uses resources correctly and efficiently
- is easy for the user to learn and use
- is well designed, well coded, easily tested and maintained.

### 7.2.3 ISO 9126

The software engineering community was in the search of a single model to standardise the quality factors since 1980. The advantage of such a universal model is quite obvious; it makes easier to compare one product with another product. The result was ISO 9126 in 1992 as a hierarchical model with six major attributes contributing to quality. These attributes are:

- Functionality
- Reliability
- Usability
- Efficiency
- Maintainability
- Portability

The standard claims that these six factors are comprehensive; that is, any component of software quality can be described in terms of some aspect of one or more of the six factors.

**Table 7.6: Software quality characteristics and attributes — The ISO 9126 view**

| Characteristic / Attribute | Short description of the characteristics and the concerns addressed by attributes |
|:--|:--|
| **Functionality** | Characteristics relating to achievement of the basic purpose for which the software is being engineered |
| Suitability | The presence and appropriateness of a set of functions for specified tasks |
| Accuracy | The provision of right or agreed results or effects |
| Interoperability | Software's ability to interact with specified systems |
| Security | Ability to prevent unauthorized access, whether accidental or deliberate, to programs and data |
| **Reliability** | Characteristics relating to capability of software to maintain its level of performance under stated conditions for a stated period of time |
| Maturity | Attributes of software that bear on the frequency of failure by faults in the software |
| Fault tolerance | Ability to maintain a specified level of performance in cases of software faults or unexpected inputs |
| Recoverability | Capability and effort needed to reestablish level of performance and recover affected data after possible failure |
| **Usability** | Characteristics relating to the effort needed for use, and on the individual assessment of such use, by a stated implied set of users |
| Understandability | The effort required for a user to recognize the logical concept and its applicability |
| Learnability | The effort required for a user to learn its application, operation, input, and output |
| Operability | The ease of operation and control by users |
| **Efficiency** | Characteristic related to the relationship between the level of performance of the software and the amount of resources used, under stated conditions |
| Time behaviour | The speed of response and processing times and throughput rates in performing its function |
| Resource behaviour | The amount of resources used and the duration of such use in performing its function |
| **Maintainability** | Characteristics related to the effort needed to make modifications, including corrections, improvements or adaptation of software to changes in environment, requirements and functional specifications |
| Analyzability | The effort needed for diagnosis of deficiencies or causes of failures, or for identification of parts to be modified |
| Changeability | The effort needed for modification, fault removal or for environmental change |
| Stability | The risk of unexpected effect of modifications |
| Testability | The effort needed for validating the modified software |
| **Portability** | Characteristics related to the ability to transfer the software from one organization or hardware or software environment to another |
| Adaptability | The opportunity for its adaptation to different specified environments |
| Installability | The effort needed to install the software in a specified environment |
| Conformance | The extent to which it adheres to standards or conventions relating to portability |
| Replaceability | The opportunity and effort of using it in the place of other software in a particular environment |

The hierarchical model is given in Fig. 7.12. The software quality attributes are explained in Table 7.6.

![fig7_12_iso9126.png|3.5]
*Figure 7.12. ISO 9126 quality model.*
