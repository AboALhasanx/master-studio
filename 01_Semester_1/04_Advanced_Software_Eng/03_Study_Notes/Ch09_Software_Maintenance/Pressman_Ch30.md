# C H A P T E R **REENGINEERING** 30 

K E Y C O N C E P T S **abstraction level** . . . . . . . . . 809 **BPR principles** . . 801 **BPR process** . . . . 802 **c/s architectures** 816 **data structure** . . 811 

**document restructuring** . . . . 807 

**economics** . . . . . . 819 **forward engineering** . . . . . 814 

**inventory analysis** . . . . . . . . 806 **OO architectures** 817 **restructuring** . . . 813 **reverse engineering** . . . . 809 **reengineering** . . . 804 

n a seminal article written for the _Harvard Business Review,_ Michael Hammer [HAM90] laid the foundation for a revolution in management thinking about business processes and computing: 

## I 

It is time to stop paving the cow paths. Instead of embedding outdated processes in silicon and software, we should obliterate them and start over. We should “reengineer” our businesses: use the power of modern information technology to radically redesign our business processes in order to achieve dramatic improvements in their performance. 

Every company operates according to a great many unarticulated rules . . . Reengineering strives to break away from the old rules about how we organize and conduct our business. 

Like all revolutions, Hammer’s call to arms resulted in both positive and negative changes. During the 1990s, some companies made a legitimate effort to reengineer, and the results led to improved competitiveness. Others relied solely on downsizing and outsourcing (instead of reengineering) to improve their bottom line. “Mean” organizations with little potential for future growth often resulted [DEM95]. 

During this first decade of the twenty-first century, the hype associated with reengineering has waned, but the process itself continues in companies large 

### Q U I C K L O O K 

What is it? Consider any technology product that has served you well. You use it regularly, but 

it’s getting old. It breaks too often, takes longer to repair than you’d like, and no longer represents the newest technology. What to do? If the product is hardware, you’ll likely throw it away and buy a newer model. But if it’s custom-built software, that option may not be available. You’ll need to rebuild it. You’ll create a product with added functionality, better performance and reliability, and improved maintainability. That’s what we call reengineering. 

Who does it? At a business level, reengineering is performed by business specialists (often consult- 

ing companies). At the software level, reengineering is performed by software engineers. Why is it important? We live in a rapidly changing world. The demands on business functions and the information technology that supports them are changing at a pace that puts enormous competitive pressure on every commercial organization. Both the business and the software that supports (or is) the business must be reengineered to keep pace. 

- What are the steps? Business process reengineering (BPR) defines business goals, identifies and evaluates existing business processes, and creates revised business processes that better meet current goals. The software reengineering process 

799 

800 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

Q U I C K encompasses inventory analysis, L O O K document restructuring, reverse engineering, program and data restructuring, and forward engineering. The intent of these activities is to create versions of existing programs that exhibit higher quality and better maintainability. 

What is the work product? A variety of reengineering work products (e.g., analysis models, design models, test procedures) are produced. The final output is the reengineered business 

process and/or the reengineered software that supports it. 

- How do I ensure that I’ve done it right? Use the same SQA practices that are applied in every software engineering process—formal technical reviews assess the analysis and design models, specialized reviews consider business applicability and compatibility, testing is applied to uncover errors in content, functionality, and interoperability. 

and small. The nexus between business reengineering and software engineering lies in a “system view.” 

Software is often the realization of the business rules that Hammer discusses. As these rules change, software must also change. Today, major companies have tens of thousands of computer programs that support the “old business rules.” As managers work to modify the rules to achieve greater effectiveness and competitiveness, software must keep pace. In some cases, this means the creation of major new computer-based systems.<sup>1</sup> But in many others, it means the modification or rebuilding of existing applications. 

In this chapter, we examine reengineering in a top-down manner, beginning with a brief overview of business process reengineering and proceeding to a more detailed discussion of the technical activities that occur when software is reengineered. 

### <u>30.1 BUSINESS PROCESS REENGINEERING</u> 

“To face tomorrow with the thought of using the methods of yesterday is to envision life at a standstill.” 

**James Bell** 

_Business process reengineering_ (BPR) extends far beyond the scope of information technologies and software engineering. Among the many definitions (most somewhat abstract) that have been suggested for BPR is one published in Fortune magazine [STE93]: “the search for, and the implementation of, radical change in business process to achieve breakthrough results.” But how is the search conducted, and how is the implementation achieved? More important, how can we ensure that the “radical change” suggested will in fact lead to “breakthrough results” instead of organizational chaos? 

#### 30.1.1 Business Processes 

A _business process_ is “a set of logically related tasks performed to achieve a defined business outcome” [DAV90]. Within the business process, people, equipment, mate- 

- 1 The Web-based systems and applications discussed in Chapter 29 are contemporary examples. 

801 

CHAPTER 30 

REENGINEERING 

rial resources, and business procedures are combined to produce a specified result. Examples of business processes include designing a new product, purchasing services and supplies, hiring a new employee, and paying suppliers. Each demands a set of tasks and each draws on diverse resources within the business. 

Every business process has a defined customer—a person or group that receives the outcome (e.g., an idea, a report, a design, a product). In addition, business processes cross organizational boundaries. They require that different organizational groups participate in the “logically related tasks” that define the process. 

_As a software engineer, your reengineering work occurs at the bottom of this hierarchy. Be sure, however, that someone has given serious thought to the level above. If this hasn’t been done, your work is at risk._ 

In Chapter 10, we noted that every system is actually a hierarchy of subsystems. A business is no exception. The overall business is segmented in the following manner: 

The business 

business systems 

business process 

business subprocesses 

Each business system (also called _business function_ ) is composed of one or more business processes, and each business process is defined by a set of subprocesses. 

BPR can be applied at any level of the hierarchy, but as the scope of BPR broadens (i.e., as we move upward in the hierarchy), the risks associated with BPR grow dramatically. For this reason, most BPR efforts focus on individual processes or subprocesses. 

#### 30.1.2 Principles of Business Process Reengineering 

In many ways, BPR is identical in focus and scope to business process engineering (Chapter 10). In an ideal setting, BPR should occur in a top-down manner, beginning with the identification of major business objectives and goals and culminating with a much more detailed specification of the tasks that define a specific business process. 

#### **_WebRef_** 

Extensive information on business process reengineering can be found at **www.brint.com/ BPR.htm** 

Hammer [HAM90] suggests a number of principles that guide BPR activities when they begin at the top (business) level: 

**Organize around outcomes, not tasks.** Many companies have compartmentalized business activities so that no single person (or organization) has responsibility (or control) of a business outcome. It such cases, it is difficult to determine the status of work and even more difficult to debug process problems if they do occur. BPR should design processes that avoid this problem. 

**Have those who use the output of the process perform the process.** 

The intent of this recommendation is to allow those who need business output to control all of the variables that allow them to get the output in a timely manner. The fewer separate constituencies involved in a process, the smoother is the road to a rapid outcome. 

802 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

**Incorporate information processing work into the real work that produces the raw information.** As IT becomes more distributed, it is possible to locate most information processing within the organization that produces the raw data. This localizes control, reduces communication time, and puts computing power in the hands of those that have a vested interest in the information that is produced. 

“As soon as we are shown the existence of something old in a new thing, we are pacified.” **Friedrich Wilhelm Nietzsche** 

**Treat geographically dispersed resources as though they were centralized.** Computer-based communications have become so sophisticated that geographically diverse groups can be placed in the same “virtual office.” For example, instead of running three engineering shifts at a single location, a global company can run one shift in Europe, a second shift in North America, and a third shift in Asia. In each case, engineers will work during daylight hours and communicate via high-bandwidth networks. 

**Link parallel activities instead of integrating their results.** When different constituencies perform work in parallel, it is essential to design a process that demands continuing communication and coordination. Otherwise, integration problems are sure to result. 

**Put the decision point where the work is performed, and build control into the process.** Using software design jargon, this principle suggests a flatter organizational architecture with reduced factoring. 

**Capture data once, at its source.** Data should be stored on-line so that once collected it need never be re-entered. 

Each of these principles represents a “big picture” view of BPR. Guided by these principles, business planners and process designers must begin process redesign. In the next section, we examine the process of BPR in a bit more detail. 

#### 30.1.3 A BPR Model 

Like most engineering activities, business process reengineering is iterative. Business goals and the processes that achieve them must be adapted to a changing business environment. For this reason, there is no start and end to BPR—it is an evolutionary process. A model for business process reengineering is depicted in Figure 30.1. The model defines six activities: 

**Business definition.** Business goals are identified within the context of four key drivers: _cost reduction, time reduction, quality improvement,_ and _personnel development and empowerment._ Goals may be defined at the business level or for a specific component of the business. 

**Process identification.** Processes that are critical to achieving the goals defined in the business definition are identified. They may then be ranked by importance, by need for change, or in any other way that is appropriate for the reengineering activity. 

803 

CHAPTER 30 REENGINEERING 

##### **FIGURE 30.1** 

A BPR model 



<!-- Start of picture text -->
Business<br>definition<br>Refinement &<br>instantiation<br>Process<br>Prototyping identification<br>Process<br>specification Process<br>evaluation<br>and design<br><!-- End of picture text -->

**Process evaluation.** The existing process is thoroughly analyzed and measured. Process tasks are identified; the costs and time consumed by process tasks are noted; and quality/performance problems are isolated. 

**Process specification and design.** Based on information obtained during the first three BPR activities, use-cases (Chapter 11) are prepared for each process that is to be redesigned. Within the context of BPR, use-cases identify a scenario that delivers some outcome to a customer. With the use-case as the specification of the process, a new set of tasks (which conform to the principles noted in Section 30.2.1) are designed for the process. 

**Prototyping** .  A redesigned business process must be prototyped before it is fully integrated into the business. This activity “tests” the process so that refinements can be made. 

**Refinement and instantiation.** Based on feedback from the prototype, the business process is refined and then instantiated within a business system. 

These BPR activities are sometimes used in conjunction with workflow analysis tools. The intent of these tools is to build a model of existing workflow in an effort to better analyze existing processes. In addition, the modeling techniques commonly associated with business process engineering activities such as information strategy planning and business area analysis (Chapter 10) can be used to implement the first four activities described in the process model. 

804 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

#### 30.1.4 Words of Warning 

It is not uncommon that a new business approach—in this case, BPR—is at first hyped as a panacea, and then criticized so severely that it becomes a pariah. Over the years, debate has raged about the efficacy of BPR (e.g., [BLE93], [DIC95]). In an excellent discussion of the case for and against BPR, Weisz [WEI95] summarizes the argument in the following way: 

It is tempting to bash BPR as another silver-bullet fad. From several points of view—systems thinking, peopleware, simple history—you’d have to predict high failure rates for the concept, rates which seem to be borne out by empirical evidence. For many companies, the silver bullet has apparently missed. For others, though, the reengineering effort has evidently been fruitful. 

BPR can work, if it is applied by motivated, trained people who recognize that process reengineering is a continuous activity. If BPR is conducted effectively, information systems are better integrated into the business process. Reengineering older applications can be examined in the context of a broad-based business strategy, and priorities for software reengineering can be established intelligently. 

But even if business reengineering is a strategy that is rejected by a company, software reengineering is something that _must_ be done. Tens of thousands of legacy systems—applications that are crucial to the success of businesses large and small—are in dire need of refurbishing or rebuilding. 

### <u>30.2</u> 

#### **_WebRef_** 

The SEI offers a variety of software reengineering resources at **www.sei.cmu.edu/ reengineering/** 

### <u>SOFTWARE REENGINEERING</u> 

The scenario is all too common: An application has served the business needs of a company for 10 or 15 years. During that time it has been corrected, adapted, and enhanced many times. People approached this work with the best intentions, but good software engineering practices were always shunted to the side (the press of other matters). Now the application is unstable. It still works, but every time a change is attempted, unexpected and serious side effects occur. Yet the application must continue to evolve. What to do? 

Unmaintainable software is not a new problem. In fact, the broadening emphasis on software reengineering has been spawned by a software maintenance “iceberg” that has been building for more than three decades. 

#### 30.2.1 Software Maintenance 

Thirty years ago, software maintenance was characterized [CAN72] as an "iceberg." We hope that what was immediately visible is all there is to it, but we know that an enormous mass of potential problems and cost lies under the surface. In the early 1970s, the maintenance iceberg was big enough to sink an aircraft carrier. Today, it could easily sink the entire navy! 

805 

CHAPTER 30 REENGINEERING 

The maintenance of existing software can account for over 60 percent of all effort expended by a development organization, and the percentage continues to rise as more software is produced [HAN93]. Uninitiated readers may ask why so much maintenance is required and why so much effort is expended. Osborne and Chikofsky [OSB90] provide a partial answer: 

Much of the software we depend on today is on average 10 to 15 years old. Even when these programs were created using the best design and coding techniques known at the time [and most were not], they were created when program size and storage space were principle concerns. They were then migrated to new platforms, adjusted for changes in machine and operating system technology and enhanced to meet new user needs—all without enough regard to overall architecture. 

The result is the poorly designed structures, poor coding, poor logic, and poor documentation of the software systems we are now called on to keep running . . . 

The ubiquitous nature of change underlies all software work. Change is inevitable when computer-based systems are built; therefore, we must develop mechanisms for evaluating, controlling, and making modifications. 

“Program maintainability and program understandability are parallel concepts: the more difficult a program is to understand, the more difficult it is to maintain.” **Gerald Berns** 

Upon reading the preceding paragraphs, a reader may protest: "but I don't spend 60 percent of my time fixing mistakes in the programs I develop." Software maintenance is, of course, far more than "fixing mistakes." We may define maintenance by describing four activities [SWA76] that are undertaken after a program is released for use. In Chapter 2, we defined four different maintenance activities: _corrective maintenance, adaptive maintenance, perfective maintenance_ or _enhancement,_ and _preventive maintenance_ or _reengineering._ Only about 20 percent of all maintenance work is spent “fixing mistakes.” The remaining 80 percent is spent adapting existing systems to changes in their external environment, making enhancements requested by users, and reengineering an application for future use. When maintenance is considered to encompass all of these activities, it is relatively easy to see why it absorbs so much effort. 

#### 30.2.2 A Software Reengineering Process Model 

Reengineering takes time; it costs significant amounts of money; and it absorbs resources that might be otherwise occupied on immediate concerns. For all of these reasons, reengineering is not accomplished in a few months or even a few years. Reengineering of information systems is an activity that will absorb information technology resources for many years.  That’s why every organization needs a pragmatic strategy for software reengineering. 

A workable strategy is encompassed in a reengineering process model. We’ll discuss the model later in this section, but first, some basic principles. 

Reengineering is a rebuilding activity, and we can better understand the reengineering of information systems if we consider an analogous activity: the rebuilding of a house. Consider the following situation. 

806 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

You have purchased a house in another state. You’ve never actually seen the property, but you acquired it at an amazingly low price, with the warning that it might have to be completely rebuilt. How would you proceed? 

- Before you can start rebuilding, it would seem reasonable to inspect the house. To determine whether it is in need of rebuilding, you (or a professional inspector) would create a list of criteria so that your inspection would be systematic. 

_The steps noted here for a house are “obvious.” Be sure that your consideration of legacy software applies steps that are just as obvious. Think about it. A lot more money is at stake._ 

- Before you tear down and rebuild the entire house, be sure that the structure is weak. If the house is structurally sound, it may be possible to “remodel” without rebuilding (at much lower cost and in much less time). 

- Before you start rebuilding be sure you understand how the original was built. Take a peek behind the walls. Understand the wiring, the plumbing, and the structural internals. Even if you trash them all, the insight you’ll gain will serve you well when you start construction. 

- If you begin to rebuild, use only the most modern, long-lasting materials. This may cost a bit more now, but it will help you to avoid expensive and time-consuming maintenance later. 

- If you decide to rebuild, be disciplined about it. Use practices that will result in high quality—today and in the future. 

Although these principles focus on the rebuilding of a house, they apply equally well to the reengineering of computer-based systems and applications. 

To implement these principles, we apply a software reengineering process model that defines six activities, shown in Figure 30.2.  In some cases, these activities occur in a linear sequence, but this is not always the case. For example, it may be that reverse engineering (understanding the internal workings of a program) may have to occur before document restructuring can commence. 

The reengineering paradigm shown in the figure is a cyclical model. This means that each of the activities presented as a part of the paradigm may be revisited. For any particular cycle, the process can terminate after any one of these activities. 



Inventory Analysis 

**Inventory analysis.** Every software organization should have an inventory of all applications. The inventory can be nothing more than a spreadsheet model containing information that provides a detailed description (e.g., size, age, business criticality) of every active application. By sorting this information according to business criticality, longevity, current maintainability, and other locally important criteria, candidates for reengineering appear. Resources can then be allocated to candidate applications for reengineering work. 

It is important to note that the inventory should be revisited on a regular cycle. The status of applications (e.g., business criticality) can change as a function of time, and as a result, priorities for reengineering will shift. 

807 

CHAPTER 30 REENGINEERING 

##### **FIGURE 30.2** 

A software reengineering process model 



<!-- Start of picture text -->
Forward Inventory<br>engineering analysis<br>Data Document<br>restructuring restructuring<br>Code<br>Reverse<br>restructuring<br>engineering<br><!-- End of picture text -->

**Document restructuring.** Weak documentation is the trademark of many legacy systems. But what do we do about it? What are our options? 

_Create only as much documentation as is required to enhance understanding of the software, not one page more._ 

**1.** _Creating documentation is far too time consuming. If the system works, we’ll live with what we have._ In some cases, this is the correct approach. It is not possible to re-create documentation for hundreds of computer programs. If a program is relatively static, is coming to the end of its useful life, and is unlikely to undergo significant change, let it be! 

**2.** _Documentation must be updated, but we have limited resources. We’ll use a “document when touched” approach._ It may not be necessary to fully redocument an application. Rather, those portions of the system that are currently undergoing change are fully documented. Over time, a collection of useful and relevant documentation will evolve. 

**3.** _The system is business critical and must be fully redocumented._ Even in this case, an intelligent approach is to pare documentation to an essential minimum. 

Each of these options is viable. A software organization must choose the one that is most appropriate for each case. 

**Reverse engineering.** The term _reverse engineering_ has its origins in the hardware world. A company disassembles a competitive hardware product in an effort to understand its competitor's design and manufacturing "secrets." These secrets could be easily understood if the competitor's design and manufacturing specifications were obtained. But these documents are proprietary and unavailable to the company doing 

808 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

the reverse engineering. In essence, successful reverse engineering derives one or more design and manufacturing specifications for a product by examining actual specimens of the product. 

Reverse engineering for software is quite similar. In most cases, however, the program to be reverse engineered is not a competitor's. Rather, it is the company's own work (often done many years earlier). The "secrets" to be understood are obscure because no specification was ever developed. Therefore, reverse engineering for software is the process of analyzing a program in an effort to create a representation of the program at a higher level of abstraction than source code. Reverse engineering is a process of design recovery. Reverse engineering tools extract data, architectural, and procedural design information from an existing program. 

**Code restructuring.** The most common type of reengineering (actually, the use of the term _reengineering_ is questionable in this case) is code restructuring. Some legacy systems have a relatively solid program architecture, but individual modules were coded in a way that makes them difficult to understand, test, and maintain. In such cases, the code within the suspect modules can be restructured. 

To accomplish this activity, the source code is analyzed using a restructuring tool. Violations of structured programming constructs are noted and code is then restructured (this can be done automatically). The resultant restructured code is reviewed and tested to ensure that no anomalies have been introduced. Internal code documentation is updated. 

#### **_WebRef_** 

A vast array of resources for the reengineering community can be obtained at **www.comp.lancs.ac. uk/projects/ RenaissanceWeb/** 

**Data restructuring.** A program with weak data architecture will be difficult to adapt and enhance. In fact, for many applications, data architecture has more to do with the long-term viability of a program that the source code itself. 

Unlike code restructuring, which occurs at a relatively low level of abstraction, data structuring is a full-scale reengineering activity. In most cases, data restructuring begins with a reverse engineering activity. Current data architecture is dissected and necessary data models are defined (Chapter 12). Data objects and attributes are identified, and existing data structures are reviewed for quality. 

When data structure is weak (e.g., flat files are currently implemented, when a relational approach would greatly simplify processing), the data are reengineered. 

Because data architecture has a strong influence on program architecture and the algorithms that populate it, changes to the data will invariably result in either architectural or code-level changes. 

**Forward engineering.** In an ideal world, applications would be rebuilt using a automated “reengineering engine.” The old program would be fed into the engine, analyzed, restructured, and then regenerated in a form that exhibited the best aspects of software quality. In the short term, it is unlikely that such an “engine” will appear, but CASE vendors have introduced tools that provide a limited subset of these capabili- 

809 

CHAPTER 30 REENGINEERING 

ties that addresses specific application domains (e.g., applications that are implemented using a specific database system). More important, these reengineering tools are becoming increasingly more sophisticated. 

Forward engineering, also called _renovation_ or _reclamation_ [CHI90], not only recovers design information from existing software, but uses this information to alter or reconstitute the existing system in an effort to improve its overall quality. In most cases, reengineered software reimplements the function of the existing system and also adds new functions and/or improves overall performance. 

### <u>30.3 REVERSE ENGINEERING</u> 

Reverse engineering conjures an image of the "magic slot." We feed an unstructured, undocumented source listing into the slot and out the other end comes full documentation for the computer program. Unfortunately, the magic slot doesn't exist. Reverse engineering can extract design information from source code, but the abstraction level, the completeness of the documentation, the degree to which tools and a human analyst work together, and the directionality of the process are highly variable [CAS88]. 

##### **XRef** 

The notation discussed here is explained in detail in Chapter 12. 

Three reverse engineering issues must be addressed: abstraction level, completeness, and directionality. 

The _abstraction level_ of a reverse engineering process and the tools used to effect it refers to the sophistication of the design information that can be extracted from source code. Ideally, the abstraction level should be as high as possible. That is, the reverse engineering process should be capable of deriving procedural design representations (a low-level abstraction), program and data structure information (a somewhat higher level of abstraction), data and control flow models (a relatively high level of abstraction), and entity relationship models (a high level of abstraction). As the abstraction level increases, the software engineer is provided with information that will allow easier understanding of the program. 

The _completeness_ of a reverse engineering process refers to the level of detail that is provided at an abstraction level. In most cases, the completeness decreases as the abstraction level increases. For example, given a source code listing, it is relatively easy to develop a complete procedural design representation. Simple data flow representations may also be derived, but it is far more difficult to develop a complete set of data flow diagrams or entity-relationship models. 

Completeness improves in direct proportion to the amount of analysis performed by the person doing reverse engineering. _Interactivity_ refers to the degree to which the human is "integrated" with automated tools to create an effective reverse engineering process. In most cases, as the abstraction level increases, interactivity must increase or completeness will suffer. 

If the _directionality_ of the reverse engineering process is one way, all information extracted from the source code is provided to the software engineer who can then use it during any maintenance activity. If directionality is two way, the information is 

810 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

##### **FIGURE 30.3** 

The reverse engineering process 



<!-- Start of picture text -->
Dirty source code<br>Restructure<br>code<br>Processing<br>Clean source code<br>Extract<br>Interface<br>abstractions<br>Initial specification Database<br>Refine &<br>simplify<br>Final specification<br><!-- End of picture text -->

fed to a reengineering tool that attempts to restructure or regenerate the old program. 

#### **_WebRef_** 

The Design Recovery and Program Understanding page provides useful resources for reengineering work: **wwwsel.iit.nrc.ca/ projects/dr/dr.html** 

The reverse engineering process is represented in Figure 30.3. Before reverse engineering activities can commence, unstructured (“dirty”) source code is _restructured_ (Section 30.4.1) so that it contains only the structured programming constructs.<sup>2</sup> This makes the source code easier to read and provides the basis for all the subsequent reverse engineering activities. 

The core of reverse engineering is an activity called _extract abstractions._ The engineer must evaluate the old program and from the (often undocumented) source code, extract a meaningful specification of the processing that is performed, the user interface that is applied, and the program data structures or database that is used. 

#### 30.3.1 Reverse Engineering to Understand Processing 

The first real reverse engineering activity begins with an attempt to understand and then extract procedural abstractions represented by the source code. To understand procedural abstractions, the code is analyzed at varying levels of abstraction: system, program, component, pattern, and statement. 

> 2 Code can be restructured automatically using a “restructuring engine”—a CASE tool that restructures source code. 

811 

CHAPTER 30 

REENGINEERING 

“There exists a passion for comprehension, just as there exists a passion for music. That passion is rather common in children, but gets lost in most people later on.” 

**Albert Einstein** 

The overall functionality of the entire application system must be understood before more detailed reverse engineering work occurs. This establishes a context for further analysis and provides insight into interoperability issues among applications within the system. Each of the programs that make up the application system represents a functional abstraction at a high level of detail. A block diagram, representing the interaction between these functional abstractions, is created. Each component performs some subfunction and represents a defined procedural abstraction. A processing narrative for each component is created. In some situations, system, program and component specifications already exist. When this is the case, the specifications are reviewed for conformance to existing code.<sup>3</sup> 

Things become more complex when the code inside a component is considered. The engineer looks for sections of code that represent generic procedural patterns. In almost every component, a section of code prepares data for processing (within the module), a different section of code does the processing, and another section of code prepares the results of processing for export from the component. Within each of these sections, we can encounter smaller patterns; for example, data validation and bounds checking often occur within the section of code that prepares data for processing. 

For large systems, reverse engineering is generally accomplished using a semiautomated approach. CASE tools are used to “parse” the semantics of existing code. The output of this process is then passed to restructuring and forward engineering tools to complete the reengineering process. 

#### 30.3.2 Reverse Engineering to Understand Data 

Reverse engineering of data occurs at different levels of abstraction. At the program level, internal program data structures must often be reverse engineered as part of an overall reengineering effort. At the system level, global data structures (e.g., files, databases) are often reengineered to accommodate new database management paradigms (e.g., the move from flat file to relational or object-oriented database systems). Reverse engineering of the current global data structures sets the stage for the introduction of a new systemwide database. 

**Internal data structures.** Reverse engineering techniques for internal program data focus on the definition of classes of objects.<sup>4</sup> This is accomplished by examining the program code with the intent of grouping related program variables. In many cases, the data organization within the code identifies abstract data types. For example, record structures, files, lists, and other data structures often provide an initial indicator of classes. 

> 3 Often, specifications written early in the life history of a program are never updated. As changes are made, the code no longer conforms to the specification. 

> 4 For a complete discussion of these object-oriented concepts, see Part Four of this book. 

812 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

Breuer and Lano [BRE91] suggest the following approach for reverse engineering of classes: 

_Relatively insignificant compromises in data structures can lead to potentially catastrophic problems in future years. Consider the Y2K problem as an example._ 

**1.** Identify flags and local data structures within the program that record important information about global data structures (e.g., a file or database). 

**2.** Define the relationship between flags and local data structures and the global data structures. For example, a flag may be set when a file is empty; a local data structure may serve as a buffer that contains the last 100 records acquired from a central database. 

**3.** For every variable (within the program) that represents an array or file, list all other variables that have a logical connection to it. 

These steps enable a software engineer to identify classes within the program that interact with the global data structures. 

**Database structure.** Regardless of its logical organization and physical structure, a database allows the definition of data objects and supports some method for establishing relationships among the objects. Therefore, reengineering one database schema into another requires an understanding of existing objects and their relationships. 

The following steps [PRE94] may be used to define the existing data model as a precursor to reengineering a new database model: 

**? What stepscan be applied to reverse engineer an existing database structure?** 

**1. Build an initial object model.** The classes defined as part of the model may be acquired by reviewing records in a flat file database or tables in a relational schema. The items contained in records or tables become attributes of a class. 

**2. Determine candidate keys.** The attributes are examined to determine whether they are used to point to another record or table. Those that serve as pointers become candidate keys. 

**3. Refine the tentative classes.** Determine whether similar classes can be combined into a single class. 

**4. Define generalizations.** Examine classes that have many similar attributes to determine whether a class hierarchy should be constructed with a generalization class at its head. 

**5. Discover associations.** Use techniques that are analogous to the CRC approach (Chapter 21) to establish associations among classes. 

Once information defined in the preceding steps is known, a series of transformations [PRE94] can be applied to map the old database structure into a new database structure. 

#### 30.3.3 Reverse Engineering User Interfaces 

Sophisticated GUIs have become de rigueur for computer-based products and systems of every type. Therefore, the redevelopment of user interfaces has become one 

813 

CHAPTER 30 REENGINEERING 

of the most common types of reengineering activity. But before a user interface can be rebuilt, reverse engineering should occur. 

To fully understand an existing user interface (UI), the structure and behavior of the interface must be specified. Merlo and his colleagues [MER93] suggest three basic questions that must be answered as reverse engineering of the UI commences: 

**? How do Iunderstand the workings of an existing user interface?** 

- What are the basic actions (e.g., keystrokes and mouse clicks) that the interface must process? 

- What is a compact description of the behavioral response of the system to these actions? 

- What is meant by a “replacement,” or more precisely, what concept of equivalence of interfaces is relevant here? 

Behavioral modeling notation (Chapter 12) can provide a means for developing answers to the first two questions. Much of the information necessary to create a behavioral model can be obtained by observing the external manifestation of the existing interface. But additional information necessary to create the behavioral model must extracted from the code. 

It is important to note that a replacement GUI may not mirror the old interface exactly (in fact, it may be radically different). It is often worthwhile to develop new interaction metaphors. For example, an old UI requests that a user provide a scale factor (ranging from 1 to 10) to shrink or magnify a graphical image. A reengineered GUI might use a slide-bar and mouse to accomplish the same function. 

### <u>30.4 RESTRUCTURING</u> 

Software restructuring modifies source code and/or data in an effort to make it amenable to future changes. In general, restructuring does not modify the overall program architecture. It tends to focus on the design details of individual modules and on local data structures defined within modules. If the restructuring effort extends beyond module boundaries and encompasses the software architecture, restructuring becomes forward engineering (Section 30.5). 

Arnold [ARN89] defines a number of benefits that can be achieved when software is restructured: 

**? What benefits are derived from restructuring?** 

- Programs have higher quality—better documentation, less complexity, and conformance to modern software engineering practices and standards. 

- Frustration among software engineers who must work on the program is reduced, thereby improving productivity and making learning easier. 

- Effort required to perform maintenance activities is reduced. 

- Software is easier to test and debug. 

Restructuring occurs when the basic architecture of an application is solid, even though technical internals need work. It is initiated when major parts of the 

814 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

software are serviceable and only a subset of all modules and data need extensive modification.<sup>5</sup> 

#### 30.4.1 Code Restructuring 

_Although code restructuring can alleviate immediate problems associated with debugging or small changes, it is not reengineering. Real benefit is achieved only when data and architecture are restructured._ 

_Code restructuring_ is performed to yield a design that produces the same function but with higher quality than the original program. In general, code restructuring techniques (e.g., Warnier's logical simplification techniques [WAR74]) model program logic using Boolean algebra and then apply a series of transformation rules that yield restructured logic. The objective is to take "spaghetti-bowl" code and derive a procedural design that conforms to the structured programming philosophy (Chapter 16). 

Other restructuring techniques have also been proposed for use with reengineering tools. A _resource exchange diagram_ maps each program module and the resources (data types, procedures and variables) that are exchanged between it and other modules. By creating representations of resource flow, the program architecture can be restructured to achieve minimum coupling among modules. 

#### 30.4.2 Data Restructuring 

Before data restructuring can begin, a reverse engineering activity called _analysis of source code_ must be conducted. All programming language statements that contain data definitions, file descriptions, I/O, and interface descriptions are evaluated. The intent is to extract data items and objects, to get information on data flow, and to understand the existing data structures that have been implemented. This activity is sometimes called _data analysis_ [RIC89]. 

Once data analysis has been completed, _data redesign_ commences. In its simplest form, a _data record standardization_ step clarifies data definitions to achieve consistency among data item names or physical record formats within an existing data structure or file format. Another form of redesign, called _data name rationalization,_ ensures that all data naming conventions conform to local standards and that aliases are eliminated as data flow through the system. 

When restructuring moves beyond standardization and rationalization, physical modifications to existing data structures are made to make the data design more effective. This may mean a translation from one file format to another, or in some cases, translation from one type of database to another. 

### <u>30.5 FORWARD ENGINEERING</u> 

A program with control flow that is the graphic equivalent of a bowl of spaghetti, with "modules" that are 2,000 statements long, with few meaningful comment lines in 

> 5 It is sometimes difficult to make a distinction between extensive restructuring and redevelopment. Both are reengineering. 

815 

CHAPTER 30 REENGINEERING 

290,000 source statements and no other documentation must be modified to accommodate changing user requirements. We have the following options: 

**? What options exist when we’re faced with a poorly designed and implemented program?** 

**1.** We can struggle through modification after modification, fighting the implicit design and source code to implement the necessary changes. 

**2.** We can attempt to understand the broader inner workings of the program in an effort to make modifications more effectively. 

**3.** We can redesign, recode, and test those portions of the software that require modification, applying a software engineering approach to all revised segments. 

**4.** We can completely redesign, recode, and test the program, using CASE (reengineering) tools to assist us in understanding the current design. 

There is no single "correct" option. Circumstances may dictate the first option even if the others are more desirable. 

Rather than waiting until a maintenance request is received, the development or support organization uses the results of inventory analysis to select a program that (1) will remain in use for a preselected number of years, (2) is currently being used successfully, and (3) is likely to undergo major modification or enhancement in the near future. Then, option 2, 3, or 4 is applied. 

This preventative maintenance approach was pioneered by Miller [MIL81] under the title _structured retrofit._ This concept is defined as "the application of today's methodologies to yesterday's systems to support tomorrow's requirements." 

At first glance, the suggestion that we redevelop a large program when a working version already exists may seem quite extravagant. Before passing judgment, consider the following points: 

_Reengineering is a lot like getting your teeth cleaned. You can think of a thousand reasons to delay it, and you’ll get away with procrastinating for quite a while. But eventually, your delaying tactics will come back to haunt you._ 

**1.** The cost to maintain one line of source code may be 20 to 40 times the cost of initial development of that line. 

**2.** Redesign of the software architecture (program and/or data structure), using modern design concepts, can greatly facilitate future maintenance. 

**3.** Because a prototype of the software already exists, development productivity should be much higher than average. 

**4.** The user now has experience with the software. Therefore, new requirements and the direction of change can be ascertained with greater ease. 

**5.** CASE tools for reengineering will automate some parts of the job. 

**6.** A complete software configuration (documents, programs, and data) will exist upon completion of preventive maintenance. 

When a software development organization sells software as a product, preventive maintenance is seen in "new releases" of a program. A large in-house software developer (e.g., a business systems software development group for a large consumer 

816 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

products company) may have 500–2000 production programs within its domain of responsibility. These programs can be ranked by importance and then reviewed as candidates for preventive maintenance. 

The forward engineering process applies software engineering principles, concepts, and methods to re-create an existing application. In most cases, forward engineering does not simply create a modern equivalent of an older program. Rather, new user and technology requirements are integrated into the reengineering effort. The redeveloped program extends the capabilities of the older application. 

#### 30.5.1 Forward Engineering for Client/Server Architectures 

##### **XRef** 

Client/server software engineering is discussed in Chapter 28. 

Over the past decade many mainframe applications have been reengineered to accommodate client/server architectures. In essence, centralized computing resources (including software) are distributed among many client platforms. Although a variety of different distributed environments can be designed, the typical mainframe application that is reengineered into a client/server architecture has the following features: 

- Application functionality migrates to each client computer. 

- New GUI interfaces are implemented at the client sites. 

- Database functions are allocated to the server. 

- Specialized functionality (e.g., compute-intensive analysis) may remain at the server site. 

- New communications, security, archiving, and control requirements must be established at both the client and server sites. 

_In some cases, c/s or OO systems designed to replace a legacy application should be approached as a new development project. Reengineering enters the picture only when elements of an old system are to be integrated with the new architecture. In some cases, you may be better off rejecting the old and creating identical new functionality._ 

It is important to note that the migration from mainframe to c/s computing requires both business and software reengineering. In addition, an “enterprise network infrastructure” [JAY94] should be established. 

Reengineering for c/s applications begins with a thorough analysis of the business environment that encompasses the existing mainframe. Three layers of abstraction (Figure 30.4) can be identified. The database sits at the foundation of a client/server architecture and manages transactions and queries from server applications. Yet these transactions and queries must be controlled within the context of a set of business rules (defined by an existing or reengineered business process). Client applications provide targeted functionality to the user community. 

The functions of the existing database management system and the data architecture of the existing database must be reverse engineered as a precursor to the redesign of the database foundation layer. In some cases a new data model (Chapter 12) is created. In every case, the c/s database is reengineered to ensure that transactions are executed in a consistent manner, that all updates are performed only by authorized users, that core business rules are enforced (e.g., before a vendor record is deleted, the server ensures that no related accounts payable, contracts, or com- 

817 

CHAPTER 30 REENGINEERING 

##### **FIGURE 30.4** 

Reengineering mainframe applications to client/server 



<!-- Start of picture text -->
Interface: GUI<br>Client applications<br>Interface: process requests<br>Business rules<br>Interface: transactions and queries<br>Database<br><!-- End of picture text -->

munications exist for that vendor), that queries can be accommodated efficiently, and that full archiving capability has been established. 

The business rules layer represents software resident at both the client and the server. This software performs control and coordination tasks to ensure that transactions and queries between the client application and the database conform to the the established business process. 

The client applications layer implements business functions that are required by specific groups of end-users. In many instances, a mainframe application is segmented into a number of smaller, reengineered desktop applications. Communication among the desktop applications (when necessary) is controlled by the business rules layer. 

A comprehensive discussion of client/server software design and reengineering is best left to books dedicated to the subject. The interested reader should see [VAS93], [INM93], and [BER92]. 

#### 30.5.2 Forward Engineering for Object-Oriented Architectures 

Object-oriented software engineering has become the development paradigm of choice for many software organizations. But what about existing applications that were developed using conventional methods? In some cases, the answer is to leave such applications “as is.” In others, older applications must be reengineered so that they can be easily integrated into large, object-oriented systems. 

818 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

Reengineering conventional software into an object-oriented implementation uses many of the same techniques discussed in Part Four of this book. First, the existing software is reverse engineered so that appropriate data, functional, and behavioral models can be created. If the reengineered system extends the functionality or behavior of the original application, use-cases (Chapters 11 and 21) are created. The data models created during reverse engineering are then used in conjunction with CRC modeling (Chapter 21) to establish the basis for the definition of classes. Class hierarchies, object-relationship models, object-behavior models, and subsystems are defined, and object-oriented design commences. 

As object-oriented forward engineering progresses from analysis to design, a CBSE process model (Chapter 27) can be invoked. If the existing application exists within a domain that is already populated by many object-oriented applications, it is likely that a robust component library exists and can be used during forward engineering. 

For those classes that must be engineered from scratch, it may be possible to reuse algorithms and data structures from the existing conventional application. However, these must be redesigned to conform to the object-oriented architecture. 

#### 30.5.3 Forward Engineering User Interfaces 

As applications migrate from the mainframe to the desktop, users are no longer willing to tolerate arcane, character-based user interfaces. In fact, a significant portion of all effort expended in the transition from mainframe to client/server computing can be spent in the reengineering of client application user interfaces. 

Merlo and his colleagues [MER95] suggest the following model for reengineering user interfaces: 

**? What stepsshould we follow to reengineer a user interface?** 

**1. Understand the original interface and the data that move between it and the remainder of the application.** The intent is to understand how other elements of a program interact with existing code that implements the interface. If a new GUI is to be developed, the data that flow between the GUI and the remaining program must be consistent with the data that currently flow between the character-based interface and the program. 

**2. Remodel the behavior implied by the existing interface into a series of abstractions that have meaning in the context of a GUI.** Although the mode of interaction may be radically different, the business behavior exhibited by users of the old and new interfaces (when considered in terms of a usage scenario) must remain the same. A redesigned interface must still allow a user to exhibit the appropriate business behavior. For example, when a database query is to be made, the old interface may require a long series of text-based commands to specify the query. The reengineered GUI may streamline the query to a small sequence of mouse picks, but the intent and content of the query remain unchanged. 

819 

CHAPTER 30 REENGINEERING 

**3. Introduce improvements that make the mode of interaction more efficient.** The ergonomic failings of the existing interface are studied and corrected in the design of the new GUI. 

**4. Build and integrate the new GUI.** The existence of class libraries and fourth generation tools can reduce the effort required to build the GUI significantly. However, integration with existing application software can be more time consuming. Care must be taken to ensure that the GUI does not propagate adverse side effects into the remainder of the application. 

### <u>30.6 THE ECONOMICS OF REENGINEERING</u> 

In a perfect world, every unmaintainable program would be retired immediately, to be replaced by high-quality, reengineered applications developed using modern software engineering practices. But we live in a world of limited resources. Reengineering drains resources that can be used for other business purposes. Therefore, before an organization attempts to reengineer an existing application, it should perform a cost/benefit analysis. 

A cost/benefit analysis model for reengineering has been proposed by Sneed [SNE95]. Nine parameters are defined: 

“You can pay us a little now, or pay us a lot more later.” **Sign in auto dealership suggesting a tune-up** 

- _P_ 1 = current annual maintenance cost for an application. _P_ 2 = current annual operation cost for an application. _P_ 3 = current annual business value of an application. _P_ 4 = predicted annual maintenance cost after reengineering. _P_ 5 = predicted annual operations cost after reengineering. _P_ 6 = predicted annual business value after reengineering. _P_ 7 = estimated reengineering costs. _P_ 8 = estimated reengineering calendar time. _P_ 9 = reengineering risk factor ( _P_ 9 = 1.0 is nominal). _L_ = expected life of the system. 

The cost associated with continuing maintenance of a candidate application (i.e., reengineering is not performed) can be defined as 



The costs associated with reengineering are defined using the following relationship: 



Using the costs presented in equations (30-1) and (30-2), the overall benefit of reengineering can be computed as 



820 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

The cost/benefit analysis presented in the equations can be performed for all highpriority applications identified during inventory analysis (Section 30.2.2). Those applications that show the highest cost/benefit can be targeted for reengineering, while work on others can be postponed until resources are available. 

### <u>30.7 SUMMARY</u> 

Reengineering occurs at two different levels of abstraction. At the business level, reengineering focuses on the business process with the intent of making changes to improve competitiveness in some area of the business. At the software level, reengineering examines information systems and applications with the intent of restructuring or reconstructing them so that they exhibit higher quality. 

Business process reengineering defines business goals, identifies and evaluates existing business processes (in the context of defined goals), specifies and designs revised processes, and prototypes, refines, and instantiates them within a business. BPR has a focus that extends beyond software. The result of BPR is often the definition of ways in which information technologies can better support the business. 

Software reengineering encompasses a series of activities that include inventory analysis, document restructuring, reverse engineering, program and data restructuring, and forward engineering. The intent of these activities is to create versions of existing programs that exhibit higher quality and better maintainability—programs that will be viable well into the twenty-first century. 

Inventory analysis enables an organization to assess each application systematically, with the intent of determining which are candidates for reengineering. Document restructuring creates a framework of documentation that is necessary for the long-term support of an application. Reverse engineering is the process of analyzing a program in an effort to extract data, architectural, and procedural design information. Finally, forward engineering reconstructs a program using modern software engineering practices and information learned during reverse engineering. 

The cost/benefit of reengineering can be determined quantitatively. The cost of the status quo, that is, the cost associated with ongoing support and maintenance of an existing application, is compared to the projected costs of reengineering and the resultant reduction in maintenance costs. In almost every case in which a program has a long life and currently exhibits poor maintainability, reengineering represents a cost-effective business strategy. 

### <u>REFERENCES</u> 

- [ARN89] Arnold, R.S., “Software Restructuring,” _Proc. IEEE,_ vol. 77, no. 4, April 1989, pp. 607–617. 

[BER92] Berson, A., _Client/Server Architecture,_ McGraw-Hill, 1992. 

821 

CHAPTER 30 REENGINEERING 

[BLE93] Bleakley, F.R., “The Best Laid Plans: Many Companies Try Management Fads, Only to See Them Flop,” _The Wall Street Journal,_ July 6, 1993, p. 1. 

[BRE91] Breuer, P.T. and K. Lano, “Creating Specification From Code: Reverse-Engineering Techniques,” _Journal of Software Maintenance: Research and Practice,_ vol. 3, 1991, pp. 145–162. 

[CAN72]  Canning, R., "The Maintenance 'Iceberg'," _EDP Analyzer,_ vol. 10, no. 10, October 1972. 

[CAS88] "Case Tools for Reverse Engineering," _CASE Outlook,_ CASE Consulting Group, vol. 2, no. 2, 1988, pp. 1–15. 

[CHI90] Chikofsky, E.J., and J.H. Cross, II, "Reverse Engineering and Design Recovery: A Taxonomy," _IEEE Software,_ January 1990, pp. 13–17. 

[DAV90] Davenport, T.H. and J.E. Young, “The New Industrial Engineering: Information Technology and Business Process Redesign,” _Sloan Management Review,_ Summer 1990, pp. 11–27. 

[DEM95] DeMarco, T., “Lean and Mean,” _IEEE Software,_ November 1995, pp. 101–102. [DIC95] Dickinson, B., _Strategic Business Reengineering,_ LCI Press, 1995. [HAM90] Hammer, M., “Reengineer Work: Don’t Automate, Obliterate,” _Harvard Business Review,_ July–August 1990, pp. 104–112. 

[HAN93] Manna, M., “Maintenance Burden Begging for a Remedy,” _Datamation,_ April 1993, pp. 53–63. 

[INM93] Inmon, W.H., _Developing Client Server Applications,_ QED Publishing, 1993. 

[JAY94] Jaychandra, Y., _Re-engineering the Networked Enterprise,_ McGraw-Hill, 1994. [MER93] Merlo, E., et al., “Reverse Engineering of User Interfaces,” _Proc. Working Conference on Reverse Engineering,_ IEEE, Baltimore, May 1993, pp. 171–178. 

[MER95] Merlo, E., et al., “Reengineering User Interfaces,” _IEEE Software,_ January 1995, pp. 64–73. 

[MIL81] Miller, J., in _Techniques of Program and System Maintenance,_ (G. Parikh, ed.) Winthrop Publishers, 1981. 

[OSB90] Osborne, W.M. and E.J. Chikofsky, "Fitting Pieces to the Maintenance Puzzle," _IEEE Software,_ January 1990, pp. 10–11. 

[PRE94] Premerlani,W.J., and M.R. Blaha, “An Approach for Reverse Engineering of Relational Databases,” _CACM,_ vol. 37, no. 5, May 1994, pp. 42–49. 

[RIC89] Ricketts, J.A., J.C. DelMonaco, and M.W. Weeks, “Data Reengineering for Application Systems,” _Proc. Conf. Software Maintenance—1989,_ IEEE, 1989, pp. 174–179. [SNE95] Sneed, H., "Planning the Reengineering of Legacy Systems," _IEEE Software,_ January 1995, pp. 24–25. 

[STE93] Stewart, T.A., “Reengineering: The Hot New Managing Tool,” _Fortune,_ August 23, 1993, pp. 41–48. 

[SWA76] Swanson, E.B., "The Dimensions of Maintenance," _Proc. Second Intl. Conf. Software Engineering,_ IEEE, October 1976, pp. 492–497. [VAS93] Vaskevitch, D., _Client/Server Strategies,_ IDG Books, 1993. 

822 

PART FIVE ADVANCED TOPICS IN SOFTWARE ENGINEERING 

[WAR74] Warnier, J.D., _Logical Construction of Programs,_ Van Nostrand-Reinhold, 1974. 

[WEI95] Weisz, M., “BPR Is Like Teenage Sex,” _American Programmer,_ vol. 8, no. 6, June 1995, pp. 9–15. 

### <u>PROBLEMS AND POINTS TO PONDER</u> 

**30.1.** Consider any job that you’ve held in the last five years. Describe the business process in which you played a part. Use the BPR model described in Section 30.1.3 to recommend changes to the process in an effort to make it more efficient. 

**30.2.** Do some research on the efficacy of business process reengineering. Present pro and con arguments for this approach. 

**30.3.** Your instructor will select one of the programs that everyone in the class has developed during this course. Exchange your program randomly with someone else in the class. Do not explain or walk through the program. Now, implement an enhancement (specified by your instructor) in the program you have received. 

- a. Perform all software engineering tasks including a brief walkthrough (but not with the author of the program). 

- b. Keep careful track of all errors encountered during testing. 

- c. Discuss your experiences in class. 

**30.4.** Explore the inventory analysis checklist presented at the SEPA Web site and attempt to develop a quantitative software rating system that could be applied to existing programs in an effort to pick candidate programs for reengineering. Your system should extend beyond economic analysis presented in Section 30.6. 

**30.5.** Suggest alternatives to paper and ink or conventional electronic documentation that could serve as the basis for document restructuring. (Hint: Think of new descriptive technologies that could be used to communicate the intent of the software.) 

**30.6.** Some people believe that artificial intelligence technology will increase the abstraction level of the reverse engineering process. Do some research on this subject (i.e., the use of AI for reverse engineering) and write a brief paper that takes a stand on this point. 

**30.7.** Why is completeness difficult to achieve as abstraction level increases? 

**30.8.** Why must interactivity increase if completeness is to increase? 

**30.9.** Get product literature on three reverse engineering tools and present their characteristics in class. 

**30.10.** There is a subtle difference between restructuring and forward engineering. What is it? 

