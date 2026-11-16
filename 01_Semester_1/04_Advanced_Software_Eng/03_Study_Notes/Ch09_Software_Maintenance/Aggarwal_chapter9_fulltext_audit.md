

## PDF page 206

Chapter 9
SOFTWARE MAINTENANCE AND 
PROJECT MANAGEMENT
9.1 
SOFTWARE AS AN EVOLUTION ENTITY
 L
ehman and Belady have studied the characteristics of the evolution of 
several software products [1980]. They have expressed their observations in 
the form of laws. Their important laws are given below.
 
1. Lehman’s first law: A software product must change continually or become 
progressively less useful. 
 
2. Lehman’s second law: The structure of a program tends to degrade as more 
and more maintenance is carried out on it. 
 
3. Lehman’s third law: Over a program’s lifetime, its rate of development is 
approximately constant.
9.2 
SOFTWARE-CONFIGURATION MANAGEMENT ACTIVITIES 
 
Configuration management is carried out through three principal activities:
193


## PDF page 207

194 
SOF TWARE ENGINEERING AND TESTING
 
1. Configuration identification,
 
2. Configuration control, and
 
3. Configuration accounting.
 
 
Briefly, these three activities can be described as:
 
 Configuration Identification: Which parts of the system must be kept track 
of?
 
 Configuration Control: Ensures that changes to a component happen 
smoothly.
 
 Configuration Accounting: Keeps track of what has been changed, when, 
and why. 
 
1. Configuration Identification. The project manager normally classifies 
the objects associated with a software’s development into three main 
categories: controlled, pre-controlled, and uncontrolled. Controlled objects 
are those that are already put under configuration control. You must 
follow some formal procedures to change them. Pre-controlled objects 
are not yet under configuration control, but will eventually be under 
configuration control. Uncontrolled objects are not and will not be subject 
to configuration control. Controllable objects include both controlled and 
pre-controlled objects. Typical controllable objects include:
 
 Requirement specifications documents
 
 Designing documents
 
 Tools used to build the system, such as compliers, linkers, lexical 
analyzers, parsers, etc.
 
 Source code for each module
 
 Test cases
 
 Problem reports
 
 The configuration-management plan written during the project-planning 
phase lists all controlled objects. 
 
2. Configuration Control. Configuration control is the process of managing 
changes to controlled objects. The configuration control system prevents 
unauthorized changes to any controlled object. In order to change a 
controlled object, such as a module, a developer can get a private copy 
of the module from a reserve operation (see Figure 9.1). Configuration-
management tools allow only one person to reserve a module at any time. 
Once an object is reserved it does not allow anyone else to reserve this 
module until the reserved module is restored. Thus, by preventing more 


## PDF page 208

 
SOFTWARE MAINTENANCE AND PROJECT MANAGEMENT 
195
than one engineer to simultaneously reserve a module, the problems 
associated with concurrent access are solved. 
 
 The CCB is a group of people responsible for configuration management. 
The CCB evaluates the request based on its effect on the project, and the 
benefit due to change.
 
 An important reason for configuration control is people need a stable 
environment to develop a software product. 
 
 Suppose you are trying to integrate module A, with modules B and C. 
You cannot make progress if the developer of module C keeps changing 
it; this is especially frustrating if a change to module C forces you to 
recompile A. 
 
 As soon as a document under configuration control is updated, the 
updated version is frozen and is called a baseline, as shown in Figure 9.1.
FIGURE 9.1 Configuration Control
 
3. Configuration Accounting. Configuration accounting can be explained 
with two concepts:
 
(i) Status Accounting. Once the changes in the baselines occur, some 
mechanisms must be used to record how the system evolves and what 
its current state is. This task is accomplished by status accounting. 
Its basic function is to record the activities related to the other SCM 
functions. 


## PDF page 209

196 
SOF TWARE ENGINEERING AND TESTING
 
 Configuration status reporting (sometimes called status accounting) 
is an SCM task that answers the following questions:
 
(a) What happened? 
(b) Who did it?
 
(c) When did it happen? 
(d) What else will be affected?
 
 The flow of information for configuration status reporting (CSR) is 
illustrated in Figure 9.1. Each time an SCI is assigned new or updated 
identification, a CSR entry is made. Each time a change is approved 
by the CCA (i.e., an ECO is issued), a CSR entry is made. Each time 
a configuration audit is conducted, the results are reported as part of 
the CSR task. The key elements under status accounting are shown in 
Figure 9.2.
FIGURE 9.2 Status Accounting
 
(ii) Configuration Audit. A software-configuration audit complements 
the formal technical review by assessing a configuration object for 
characteristics that are generally not considered during review. The 
audit asks and answers the following questions:
 
(a) Has the change specified in the ECO been made? Have any 
additional modifications been incorporated?
 
(b) Has a formal technical review been conducted to assess technical 
correctness?
 
(c) Has the software process been followed and have software-
engineering standards been properly applied?
 
(d) Has the change been “highlighted” in the SCI? Have the change 
date and change author been specified? Do the attributes of the 
configuration object reflect the change?


## PDF page 210

 
SOFTWARE MAINTENANCE AND PROJECT MANAGEMENT 
197
 
(e) Have SCM procedures for noting the change, recording it, and 
reporting it been followed?
 
(f) Have all related SCIs been properly updated?
 
 The SCM audit revolves around software-configuration items, change 
requests, and the software quality-assurance plan. 
FIGURE 9.3 Configuration Accounting
9.3 
CHANGE-CONTROL PROCESS
 
At any moment, the configuration-management team must know the state of any 
component or document in the system. Consequently, configuration management 
should emphasize communication among those whose actions affect the system. 
Cashman and Holt (1980) suggest that we should always know the answers to the 
following questions:
 
 Synchronization: When was the change made?
 
 Identification: Who made the change?
 
 Naming: What components of the system were changed?
 
 Authentication: Was the change made correctly?
 
 Authorization: Who authorized that the change be made?
 
 Routing: Who was notified of the change?
 
 Cancellation: Who can cancel the request for a change?
 
 Delegation: Who is responsible for the change?
 
 Valuation: What is the priority of the change?
 
 
Notice that these questions are management questions, not technical ones. We 
must use procedures to manage change carefully. 
 
 
Change control combines human procedures and automated tools to provide 
a mechanism for the control of change. The change-control process is illustrated 
schematically in Figure 9.4.


## PDF page 211

198 
SOF TWARE ENGINEERING AND TESTING
FIGURE 9.4 Change-Control Process


## PDF page 212

 
SOFTWARE MAINTENANCE AND PROJECT MANAGEMENT 
199
9.4 
SOFTWARE-VERSION CONTROL
 
During the process of software evolution, many objects are produced; for example, 
files, electronic documents, paper documents, source code, executable code, and 
bitmap graphics. A version control tool is the first stage towards being able to 
manage multiple versions. Once it is in place, a detailed record of every version of 
the software must be kept. This report includes:
 
 The name of each source-code component, including the variations and 
revisions.
 
 The versions of the various compliers and linkers used.
 
 The name of the software staff who constructed the component.
 
 The date and the time at which it was constructed.
FIGURE 9.5 An Evolutionary Graph for a Different Versions of an Item
 
 
The above evolutionary graph (Figure 9.5) depicts the evolution of a 
configuration item during the development life-cycle. The initial version of the 
item is given version number Ver 1.0. Subsequent changes to the item which could 
be mostly fixing bugs or adding minor functionality is given as Ver 1.1 and Ver 
1.2. After that, a major modification to Ver 1.2 is given a number Ver 2.0, and at the 
same time, a parallel version of the same item without the major modification is 
maintained and given a version number 1.3.
 
 
Commercial tools are available for version control, which perform one or more 
of the  following tasks:
 
 Source-code control
 
 Revision control
 
 Concurrent-version control


## PDF page 213

200 
SOF TWARE ENGINEERING AND TESTING
 
 
There are many commercial tools, such as Rational Clear Case, Microsoft 
Visual Source Safe, and a number of other tools to help version control. 
9.5 
SOFTWARE-CONFIGURATION MANAGEMENT
 
Software-configuration management deals with effectively tracking and controlling 
the configuration of a software product during its life-cycle.
 
 
Before we discuss configuration management, we must be clear about what 
exactly is meant by a version and a revision of a software product. A new version 
of software is created when there is significant change in functionality, technology, 
or the hardware it runs on, etc. On the other hand, a new release is created if there 
is only a bug fix, minor enhancements to the functionality, usability, etc.
 
 
The configuration-management team is responsible for assuring that each 
version or release is correct and stable before it is released for use, and that changes 
are made accurately and promptly. Accuracy is critical, because we want to avoid 
generating new faults while correcting existing ones. Similarly, promptness is 
important, because fault detection and correction are proceeding at the same time 
that the test team searches for additional faults. Thus, those who are trying to 
repair system faults should work with components and documentation that reflect 
the current state of the system.
 
 
Thus, configuration management is the art of identifying, organizing, and controlling 
modifications to the software being built by a programming team. The goal is to maximize 
productivity by minimizing mistakes.
OR
 
 
Software-configuration management (SCM) is a set of activities designed to control 
change by identifying the work products that are likely to change, establishing relationships 
among them, defining mechanisms different versions of these work products, controlling 
the changes imposed, and auditing and reporting on the changes made.
 
 
Configuration-management procedures define how to record and process 
proposed system changes, how to relate these to system components, and 
the methods used to identify different versions of the system. Configuration-
management tools are used to store versions of system components, build systems 
from these components, and track the release of system versions to customers. 
 
 
The IEEE defines SCM as the process of identifying and defining the items in the 
system, controlling the change of these items throughout their life-cycle, recording and 
reporting the status of items and change requests, and verifying the completeness and 
correctness of items.


## PDF page 214

 
SOFTWARE MAINTENANCE AND PROJECT MANAGEMENT 
201
 
 
Figure 9.6 shows a simple configuration-management procedure based on the 
rebuilding and deployment process.
FIGURE 9.6 Simple Configuration-Management Environment
9.5.1 
Versions and Releases 
 
A configuration for a particular system is sometimes called a version. Thus, the 
initial delivery of a software package may consist of several versions, one for each 
platform or situation in which the software will be used. For example, aircraft 
software may be built so that version 1 runs on Navy planes, version 2 runs on Air 
Force planes, and version 3 runs on commercial airliners.
 
 
A new release of the software is an improved system intended to replace 
the old one. Often, software systems are described as version n, release m, or 
as version n.m, where the number reflects the system’s position as it grows and 
matures. Version n is sometimes intended to replace version n-1, and release m 
supersedes m-1.
 
Version and Release Management
 
Version and release management are the processes of identifying and keeping track 
of different versions and releases of a system. New system versions should always 
be created by the CM team rather than the system developers, even when they are 
not intended for external release. This makes it easier to maintain consistency in 
the configuration database as only the CM team can change version information.
 
 
A system version is an instance of a system that differs, in some way, from 
other instances. New versions of the system may have different functionality, 
performance, or may repair system faults. Some versions may be functionally 
equivalent but designed for different hardware or software configurations. If there 
are only small differences between versions, one of these is sometimes called a 
variant of the other. 


## PDF page 215

202 
SOF TWARE ENGINEERING AND TESTING
 
 
A system release is a version that is distributed to customers. Each system 
release should either include new functionality or be intended for a different 
hardware platform. There are always many more versions of a system than releases 
as versions are created within an organization for internal development or testing 
that are never released to customers.
9.6 
NEED FOR MAINTENANCE 
 
Software maintenance is the activity associated with keeping an operational 
computer system continuously in tune with the requirements of users and data-
processing operations. The software maintenance process is expensive and risky 
and is very challenging. There is a need for software maintenance due to the 
following reasons:
 
 Changes in user requirements with time
 
 Program/System problems
 
 Changing hardware/Software environment 
 
 To improve system efficiency and throughout
 
 To modify the components
 
 To test the resulting product to verify the correctness of changes
 
 To eliminate any unwanted side effects resulting from modifications
 
 To augment or fine-tune the software
 
 To optimize the code to run faster 
 
 To review standards and efficiency 
 
 To make the code easier to understand and work with 
 
 To eliminate any deviations from specifications 
9.6.1 
Maintenance To-Do List
 
 Correct errors 
 
 Correct requirements and design flaws 
 
 Improve the design 
 
 Make enhancements 
 
 Interface with other systems 
 
 Convert for use with other hardware
 
 Migrate legacy systems 
 
 Retire systems 


## PDF page 216

 
SOFTWARE MAINTENANCE AND PROJECT MANAGEMENT 
203
 
 Major aspects 
 
 Maintain control over the system’s day-to-day functions 
 
 Maintain control over system modification 
 
 Perfect existing acceptable functions 
 
 Prevent system performance from degrading to unacceptable levels
9.7 
CATEGORIES OF MAINTENANCE
 
Maintenance may be classified into the four categories as follows:  
 
 Corrective - reactive modifications to correct discovered problems. 
 
 Adaptive - modifications to keep it usable in a changed or changing 
environment.
 
 Perfective - improve performance or maintainability. 
 
 Preventive - modifications to detect and correct latent faults.
 
(i) Corrective Maintenance. Corrective maintenance means repairing processing 
or performance failures or making changes because of previously uncorrected 
problems. 
 
(ii) Adaptive Maintenance. Adaptive maintenance means changing the program 
functions. This is done to adapt to external environment changes. For example, 
the current system was designed so that it calculates taxes on profits after 
deducting the dividend on equity shares. The government has issued orders 
now to include the dividend in the company profit for tax calculation. This 
function needs to be changed to adapt to the new system.
 
(iii) Perfective Maintenance. Perfective maintenance means enhancing the 
performance or modifying the programs to respond to the user’s additional or 
changing needs. For example, earlier data was sent from stores to headquarters 
on magnetic media but after stores were electronically linked via leased lines, 
the software was enhanced to send data via leased lines. 
 
 As maintenance is very costly and very essential, efforts have been done 
to reduce its costs. One way to reduce the costs is through a maintenance 
management and software-modification audit. Software modification consists 
of program rewriting and system level-upgradation.
 
(iv) Preventive Maintenance. Preventive maintenance is the process by which we 
prevent our system from being obsolete. Preventive maintenance involves the 
concept of re-engineering and reverse engineering in which an old system with 
an old technology is re-engineered using new technology. This maintenance 
prevents the system from dying out.


## PDF page 217

204 
SOF TWARE ENGINEERING AND TESTING
9.8 
MAINTENANCE COSTS
 
In the 1970s, most of a software system’s budget was spent on development. The 
ratio of development money to maintenance money was reversed in the 1980s, 
and various estimates place maintenance at 40 to 60% of the full life-cycle cost of 
a system (i.e., from development through maintenance to eventual retirement or 
replacement). However, this cost may vary widely from one application domain to 
another.
 
 
It is advisable to invest more effort in early phases of the software life-cycle 
to reduce maintenance costs. The defect repair ratio increases heavily from the 
analysis phase to the implementation phase as shown in Table 9.1.
TABLE 9.1 Defect Repair Ratio
Phase
Ratio
Analysis
1
Design
10
Implementation
100
 
 
Therefore, more effort during development will certainly reduce the cost of 
maintenance.
9.8.1 
Factors Affecting Effort 
 
There are many other factors that contribute to the effort needed to maintain a 
system. These factors include the following: 
 
 Application type
 
 System novelty
 
 Turnover and maintenance staff availability
 
 System life-span
 
 Dependence on a changing environment
 
 Hardware characteristics
 
 Design quality
 
 Code quality
 
 Documentation quality
 
 Testing quality


## PDF page 218

 
SOFTWARE MAINTENANCE AND PROJECT MANAGEMENT 
205
9.8.2 Modeling Maintenance Effort
 
As with development, we want to estimate the effort required to maintain a 
software system. 
 
1. Belady and Lehman Model. Belady and Lehman (1972) were among the 
first researchers to try to capture maintenance effort in a predictive model. 
This model indicates that effort and costs can increase exponentially if a poor 
software development approach is used, and the person or group that used 
the approach is no longer available to perform maintenance.
 
 Belady and Lehman capture these effects in an equation: 
 
 
M = P + Ke(c – d).
 
 M is the total maintenance effort expanded for a system, and p represents 
wholly productive efforts: analysis, evaluation, design, coding, and testing. 
c is the complexity caused by the lack of structured design and documentation; 
it is reduced by d, the degree to which the maintenance team is familiar with 
the software. Finally, K is a constant determined by comparing this model with 
the effort relationships on actual projects; it is called an empirical constant 
because its value depends on the environment.
 
 The Belady-Lehman equation expresses a very important relationship among 
the factors determining maintenance effort. In this relation, the value of ‘c’ 
is increased if the software system is developed without use of a software-
engineering process. Of course, ‘c’ will be higher for a large software product 
with a high degree of systematic structure than a small one with the same 
degree. If the software is maintained without an understanding of the structure, 
the function and purpose of the software, then the value of ‘d’ will be low.
 
 The result is that the cost for maintenance increases exponentially. Thus, to 
economize on maintenance, the best approach is to build the system using 
good software-engineering practices and to give the maintainers time to 
become familiar with the software.
 
 Example 9.1. The development effort for a software project is 500 person-months. The 
empirically determined constant (K) is 0.3. The complexity of the code is quite high 
and is equal to 8. Calculate the total effort expended (M) if
 
(i) The maintenance team has good level of understanding of the project (d = 0.9).
 
(ii) The maintenance team has poor understanding of project (d = 0.1).
 
 Solution.
 
 
Development effort (P) = 500 PM
 
 
K = 0.3
 
 
C = 8.


## PDF page 219

206 
SOF TWARE ENGINEERING AND TESTING
 
(i) The maintenance team has good level of understanding (d = 0.9)
 
 
M = P + Ke(c – d)
 
 
 = 500 + 0.3e(8 – 0.9)
 
 
 = 500 + 363.59 = 863.59 PM.
 
(ii) The maintenance team has poor level of understanding (d = 0.1)
 
 
M = P + Ke(c – d)
 
  
 = 500 + 0.3e(8 – 0.1)
 
 
 = 500 + 809.18 = 1309.18 PM.
 
 Hence, it is clear that effort increases exponentially if poor software-engineering 
approaches are used and understandability of the project is poor.
 
2. Boehm Model. Boehm proposed a formula for estimating maintenance costs 
as part of his COCOMO model. Using data gathered from several projects, 
this formula was established in terms of effort. Boehm used a quantity called 
Annual Change Traffic (ACT), which is defined as:
 
 The fraction of a software product’s source instructions which undergo change during 
a year either through addition, deletion, or modification.
 
 The ACT is clearly related to the number of change requests.
 
 
ACT = 
+
added
deleted
total
KLOC
KLOC
KLOC
,
 
 where KLOCadded is the total kilo lines of source code added during 
maintenance. KLOCdeleted is the total KLOCdeleted during maintenance. Thus, 
the code that is changed should be counted in both the code added and the 
code deleted.
 
 The annual change traffic is multiplied with the total development cost to 
arrive at the maintenance cost. 
 
 
Maintenance cost = ACT × development cost
 
 Most maintenance-cost estimation models, however, give only approximate 
results because they do not take into account several factors, such as the 
experience level of engineers and the familiarity of engineers with the product, 
hardware requirements, software complexity, etc.
 
 Example 9.2. The Annual change traffic for a software system is 15% per year. The 
development effort is 600 PMs. Compute an estimate for the Annual maintenance 
effort (AME). If the lifetime of the project is 10 years, what is the total effort of the 
project?


## PDF page 220

 
SOFTWARE MAINTENANCE AND PROJECT MANAGEMENT 
207
 
 Solution.
 
 
 
The development effort = 600 PM.
 
 
 
ACT = 15%.
 
 Total duration for which effort is to be calculated = 10 years.
 
 The maintenance effort is a fraction of the development effort and is assumed 
to be constant.
 
 
 
AME = ACT × SDE
 
 
 
 = 0.15 × 600 = 90 PM
 
 
 
The maintenance effort for 10 years = 10 × 90 = 900 PM
 
 
 
Total effort = 600 + 900 = 1500 PM.
9.9 
SOFTWARE-PROJECT ESTIMATION
 
Software-project estimation is the process of estimating various resources required 
for the completion of a project. Effective software-project estimation is an important 
activity in any software-development project. Underestimating software projects 
and understaffing it often leads to low-quality deliverables, and the project misses 
the target deadline leading to customer dissatisfaction and loss of credibility to the 
company. On the other hand, overstaffing a project without proper control will 
increase the cost of the project and reduce the competitiveness of the company. 
 
 
Software-project estimation mainly encompasses the following steps:
 
1. Estimating the Size of the Project. There are many procedures available 
for estimating the size of a project, which are based on quantitative 
approaches, such as estimating lines of code or estimating the functionality 
requirements of the project called function points.
 
2. Estimating Efforts Based on Person-months or Person-hours. Person-
month is an estimate of the personal resources required for the project.
 
3. Estimating Schedule in Calendar Days/Month/Year Based on Total 
Person-months Required and Manpower Allocated to the Project. The 
duration in calendar month = Total person-months/Total manpower 
allocated.
 
4. Estimating Total Cost of the Project Depending on the Above and 
Other Resources. In a commercial and competitive environment, 
software-project estimation is crucial for managerial decision-making. 
Table 9.2 gives the relationship between various management functions 
and software metrics/indicators. Project estimation and tracking help to 
