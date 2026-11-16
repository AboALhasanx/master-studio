******Created by ebook converter - www.ebook-converter.com****** 

# **Chapter** 13 

# **SOFTWARE MAINTENANCE** 

Many students and practising engineers have a preconceived bias against software maintenanc e work. The mention of the word maintenance brings up the image of a screw driver, wielding mechanic with soiled hands holding onto a bagful of spare parts. It would be the objective of this chapter to clear up this misnomer, provide some intuitive understanding of the software maintenance projects, and to familiarise you with the latest techniques in software maintenance. 

Software maintenance denotes any changes made to a software product after it has been delivered to the customer. Maintenance is inevitable for almost any kind of product. However, most products need maintenance due to the wear and tear caused by use. On the other hand, software products do not need maintenance on this count, but need maintenance to correct errors, enhance features, port to new platforms, etc. 

In Section 13.1, we examine some general issues concerning maintenance projects. In Section 13.2, we discuss some basic ideas about software reverse engineering. In Section 13.3 we discuss two software maintenance process models which attempt to systematise the software development effort and finally we discuss some concepts involved in cost estimation of maintenance efforts. 

## **13.1 CHARACTERISTICS OF SOFTWARE MAINTENANCE** 

In this section, we first classify the different maintenance efforts into a few classes. Next, we discuss some general characteristics of the maintenance projects. We also discuss some special problems associated with maintenance projects. 

Software maintenance is becoming an important activity of a large number of organisations. This is no surprise, given the rate of hardware obsolescence, the immortality of a software product per se, and the demand of the user 

******ebook converter DEMO - www.ebook-converter.com******* 

******Created by ebook converter - www.ebook-converter.com****** 

community to see the existing software products run on newer platforms, run in newer environments, and/or with enhanced features. When the hardware platform changes, and a software product performs some low-level functions, maintenance is necessary. Also, whenever the support environment of a software product changes, the software product requires rework to cope up with the newer interface. For instance, a software product may need to be maintained when the operating system changes. Thus, every software product continues to evolve after its development through maintenance efforts. 

## **Types of Software Maintenance** 

There are three types of software maintenance, which are described as follows: 

**Corrective:** Corrective maintenance of a software product is necessary either to rectify the bugs observed while the system is in use. 

**Adaptive:** A software product might need maintenance when the customers need the product to run on new platforms, on new operating systems, or when they need the product to interface with new hardware or software. 

**Perfective:** A software product needs maintenance to support the new features that users want it to support, to change different functionalities of the system according to customer demands, or to enhance the performance of the system. 

## **13.1.1 Characteristics of Software Evolution** 

Lehman and Belady have studied the characteristics of evolution of several software products [1980]. They have expressed their observations in the form of laws. Their important laws are presented in the following subsection. But a word of caution here is that these are generalisations and may not be applicable to specific cases and also most of these observations concern large software projects and may not be appropriate for the maintenance and evolution of very small products. 

**Lehman’s first law:** A software product must change continually or become progressively less useful. Every software product continues to evolve after its development through maintenance efforts. Larger products stay in operation for longer times because of higher replacement costs and therefore tend to incur higher maintenance efforts. This law clearly shows that every product 

******ebook converter DEMO - www.ebook-converter.com******* 

******Created by ebook converter - www.ebook-converter.com****** 

irrespective of how well designed must undergo maintenance. In fact, when a product does not need any more maintenance, it is a sign that the product is about to be retired/discarded. This is in contrast to the common intuition that only badly designed products need maintenance. In fact, good products are maintained and bad products are thrown away. 

**Lehman’s second law:** The structure of a program tends to degrade as more and more maintenance is carried out on it. The reason for the degraded structure is that when you add a function during maintenance, you build on top of an existing program, often in a way that the existing program was not intended to support. If you do not redesign the system, the additions will be more complex that they should be. Due to quick-fix solutions, in addition to degradation of structure, the documentations become inconsistent and become less helpful as more and more maintenance is carried out. 

**Lehman’s third law:** Over a program’s lifetime, its rate of development is approximately constant. The rate of development can be quantified in terms of the lines of code written or modified. Therefore this law states that the rate at which code is written or modified is approximately the same during development and maintenance. 

## **13.1.2 Special Problems Associated with Software Maintenance** 

Software maintenance work currently is typically much more expensive than what it should be and takes more time than required. The reasons for this situation are the following: 

Software maintenance work in organisations is mostly carried out using ad hoc techniques. The primary reason being that software maintenance is one of the most neglected areas of software engineering. Even though software maintenance is fast becoming an important area of work for many companies as the software products of yester years age, still software maintenance is mostly being carried out as fire-fighting operations, rather than through systematic and planned activities. 

Software maintenance has a very poor image in industry. Therefore, an organisation often cannot employ bright engineers to carry out maintenance work. Even though maintenance suffers from a poor image, the work involved is often more challenging than development work. During maintenance it is necessary to thoroughly understand someone else’s work, and then carry out the required modifications and extensions. 

Another problem associated with maintenance work is that the majority of ******ebook converter DEMO - www.ebook-converter.com******* 

******Created by ebook converter - www.ebook-converter.com****** 

software products needing maintenance are legacy products. Though the word legacy implies “aged” software, but there is no agreement on what exactly is a legacy system. It is prudent to define a legacy system as any software system that is hard to maintain. The typical problems associated with legacy systems are poor documentation, unstructured (spaghetti code with ugly control structure), and lack of personnel knowledgeable in the product. Many of the legacy systems were developed long time back. But, it is possible that a recently developed system having poor design and documentation can be considered to be a legacy system. 

## **13.2 SOFTWARE REVERSE ENGINEERING** 

Software reverse engineering is the process of recovering the design and the requirements specification of a product from an analysis of its code. The purpose of reverse engineering is to facilitate maintenance work by improving the understandability of a system and to produce the necessary documents for a legacy system. Reverse engineering is becoming important, since legacy software products lack proper documentation, and are highly unstructured. Even well-designed products become legacy software as their structure degrades through a series of maintenance efforts. 

The first stage of reverse engineering usually focuses on carrying out cosmetic changes to the code to improve its readability, structure, and understandability, without changing any of its functionalities. A way to carry out these cosmetic changes is shown schematically in Figure 13.1. A program can be reformatted using any of the several available prettyprinter programs which layout the program neatly. Many legacy software products are difficult to comprehend with complex control structure and unthoughtful variable names. Assigning meaningful variable names is important because we had seen in Chapter 9 that meaningful variable names is the most helpful code documentation. All variables, data structures, and functions should be assigned meaningful names wherever possible. Complex nested conditionals in the program can be replaced by simpler conditional statements or whenever appropriate by case statements. 

******ebook converter DEMO - www.ebook-converter.com******* 

******Created by ebook converter - www.ebook-converter.com****** 



<!-- Start of picture text -->
Requirements specification<br>Design<br>Module specification<br>Code<br><!-- End of picture text -->

**Figure 13.1:** A process model for reverse engineering. 

After the cosmetic changes have been carried out on a legacy software, the proces of extracting the code, design, and the requirements specification can begin. These activities are schematically shown in Figure 13.2. In order to extract the design, a full understanding of the code is needed. Some automatic tools can be used to derive the data flow and control flow diagram from the code. The structure chart (module invocation sequence and data interchange among modules) should also be extracted. The SRS document can be written once the full code has been thoroughly understood and the design extracted. 



<!-- Start of picture text -->
Assignmeaningful Simplify<br>Reformatprogram names conditions<br>Simplify RemoveGOTOs<br>processing<br><!-- End of picture text -->

**Figure 13.2:** Cosmetic changes carried out before reverse engineering. 

## **13.3 SOFTWARE MAINTENANCE PROCESS MODELS** 

******ebook converter DEMO - www.ebook-converter.com******* 

******Created by ebook converter - www.ebook-converter.com****** 

Before discussing process models for software maintenance, we need to analyse various activities involved in a typical software maintenance project. The activities involved in a software maintenance project are not unique and depend on several factors such as: (i) the extent of modification to the product required, (ii) the resources available to the maintenance team, (iii) the conditions of the existing product (e.g., how structured it is, how well documented it is, etc.), (iii) the expected project risks, etc. When the changes needed to a software product are minor and straightforward, the code can be directly modified and the changes appropriately reflected in all the documents. 

However, more elaborate activities are required when the required changes are not so trivial. Usually, for complex maintenance projects for legacy systems, the software process can be represented by a reverse engineering cycle followed by a forward engineering cycle with an emphasis on as much reuse as possible from the existing code and other documents. 

Since the scope (activities required) for different maintenance projects vary widely, no single maintenance process model can be developed to suit every kind of maintenance project. However, two broad categories of process models can be proposed. 

## **First model** 

The first model is preferred for projects involving small reworks where the code is changed directly and the changes are reflected in the relevant documents later. This maintenance process is graphically presented in Figure 13.3. In this approach, the project starts by gathering the requirements for changes. The requirements are next analysed to formulate the strategies to be adopted for code change. At this stage, the association of at least a few members of the original development team goes a long way in reducing the cycle time, especially for projects involving unstructured and inadequately documented code. The availability of a working old system to the maintenance engineers at the maintenance site greatly facilitates the task of the maintenance team as they get a good insight into the working of the old system and also can compare the working of their modified system with the old system. Also, debugging of the reengineered system becomes easier as the program traces of both the systems can be compared to localise the bugs. 

******ebook converter DEMO - www.ebook-converter.com******* 

******Created by ebook converter - www.ebook-converter.com****** 



<!-- Start of picture text -->
Gather change<br>requirements<br>Analyse change<br>requirements<br>Devise code change<br>strategies<br>Apply code change<br>strategiesto theoldcode<br>Updatedocuments Integrateandtest<br><!-- End of picture text -->

**Figure 13.3:** Maintenance process model 1. 

## **Second model** 

The second model is preferred for projects where the amount of rework required is significant. This approach can be represented by a reverse engineering cycle followed by a forward engineering cycle. Such an approach is also known as software re-engineering. This process model is depicted in Figure 13.4. 

******ebook converter DEMO - www.ebook-converter.com******* 

******Created by ebook converter - www.ebook-converter.com****** 



<!-- Start of picture text -->
Changerequirements<br>Requirements Newrequirements<br>specification specification Forward<br>Reverse<br>engineering<br>engineering<br>Design Design<br>Module Module<br>specification specification<br>Code Code<br><!-- End of picture text -->

**Figure 13.4:** Maintenance process model 2. 

The reverse engineering cycle is required for legacy products. During the reverse engineering, the old code is analysed (abstracted) to extract the module specifications. The module specifications are then analysed to produce the design. The design is analysed (abstracted) to produce the original requirements specification. The change requests are then applied to this requirements specification to arrive at the new requirements specification. At this point a forward engineering is carried out to produce the new code. At the design, module specification, and coding a substantial reuse is made from the reverse engineered products. An important advantage of this approach is that it produces a more structured design compared to what the original product had, produces good documentation, and very often results in increased efficiency. The efficiency improvements are brought about by a more efficient design. However, this approach is more costly than the first approach. An empirical study indicates that process 1 is preferable when the amount of rework is no more than 15 per cent (see Figure 13.5). 

******ebook converter DEMO - www.ebook-converter.com******* 

******Created by ebook converter - www.ebook-converter.com****** 



<!-- Start of picture text -->
Cost<br>Process1<br>Process2<br>10 20 30 40<br>Percentage ofrework<br><!-- End of picture text -->

**Figure 13.5:** Empirical estimation of maintenance cost versus percentage rework. 

Besides the amount of rework, several other factors might affect the decision regarding using process model 1 over process model 2 as follows: 

- Re-engineering might be preferable for products which exhibit a high failure rate. 

- Re-engineering might also be preferable for legacy products having poor design and code structure. 

## **13.4 ESTIMATION OF MAINTENANCE COST** 

- We had earlier pointed out that maintenance efforts require about 60 per cent of the total life cycle cost for a typical software product. However, maintenance costs vary widely from one application domain to another. For embedded systems, the maintenance cost can be as much as 2 to 4 times the development cost. 

Boehm [1981] proposed a formula for estimating maintenance costs as part of his COCOMO cost estimation model. Boehm’s maintenance cost estimation is made in terms of a quantity called the annual change traffic (ACT). Boehm defined ACT as the fraction of a software product’s source instructions which undergo change during a typical year either through addition or deletion. 

### KLOCadded + KLOCdeleted ACT= KLOCtotal 

- where, KLOCadded is the total kilo lines of source code added during maintenance. KLOCdeleted is the total KLOC deleted during 

******ebook converter DEMO - www.ebook-converter.com******* 

******Created by ebook converter - www.ebook-converter.com****** 

maintenance. Thus, the code that is changed, should be counted in both the code added and code deleted. 

The annual change traffic (ACT) is multiplied with the total development cost to arrive at the maintenance cost: 

Maintenance cost = ACT × Development cost 

Most maintenance cost estimation models, however, give only approximate results because they do not take into account several factors such as experience level of the engineers, and familiarity of the engineers with the product, hardware requirements, software complexity, etc. 

## **SUMMARY** 

- In this chapter, we discussed some fundamental concepts associated with software maintenance activities. 

- Maintenance is the most expensive phase of the software life cycle and therefore it is usually cost-effective to invest in time and effort while developing the product and to emphasise on maintainability of the product to reduce the maintenance costs. 

- We discussed the activities in reverse engineering and then discussed two maintenance process models. We also discussed the applicability of these two process models to maintenance projects. 

- We highlighted the salient points in costing maintenance projects. 

## **EXERCISES** 

1. Choose the correct option: 

   - (a) Which of the following is not a cause for software maintenance for a typical product? 

      - (i) It is not possible to guarantee that a software is defect-free even after thorough testing. 

      - (ii) The deployment platform may change over time. 

      - (iii) The user’s needs may change over time. 

      - (iv) Software undergoes wear and tear after long usage. 

   - (b) A legacy software product refers to a software that is: 

      - (i) Developed at least 50 years ago. (ii) Obsolete software product. 

      - (iii) Software product that has poor design structure and code. 

      - (iv) Software product that could not be tested properly before product 

******ebook converter DEMO - www.ebook-converter.com******* 

******Created by ebook converter - www.ebook-converter.com****** 

delivery. 

   - (c) Which of the following assertions is true? 

      - (i) Legacy products automatically imply very old products. 

      - (ii) The total effort spent in maintaining an average product typically exceeds the effort in developing it. 

      - (iii) Reverse engineering encompasses re-engineering. 

      - (iv) Reeingineering encompasses reverse engineering. 

   - (d) Which of the following types of maintenance consumes the maximum effort for a typical software? 

      - (i) Adaptive 

      - (ii) Corrective 

      - (iii) Preventive 

      - (iv) Perfective 

- 2 . What are the different types of maintenance that a software product might need? Why are these maintenance required? 

- 3 . Explain why every software system must undergo maintenance or progressively become less useful. 

4. Discuss the process models for software maintenance and indicate how you would select an appropriate maintenance model for a maintenance project at hand. 

- 5 . State whether the following statements are **TRUE** or **FALSE** . Give reasons for your answer. 

   - (a) Legacy software products are those products which have been developed long time back. 

   - (b) Corrective maintenance is the type of maintenance that is most frequently carried out on a typical software product. 

6. What do you mean by the term software reverse engineering? Why is it required? Explain the different activites undertaken during reverse engineering. 

7. What do you mean by the term software re-engineering? Why is it required? Explain the different activities undertaken during reverse engineering. 

8. If a software product costed Rs. 10,000,000 for development, compute the annual maintenance cost given that every year approximately 5 per cent of the code needs modification. Identify the factors which render the maintenance cost estimation inaccurate? 

- 9 . What is a legacy software product? Explain the problems one would encounter while maintaining a legacy product. 

******ebook converter DEMO - www.ebook-converter.com******* 

