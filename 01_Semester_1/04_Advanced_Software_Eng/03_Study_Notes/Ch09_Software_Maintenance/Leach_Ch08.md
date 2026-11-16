C h a p t e r 8 

# Maintenance and Software Evolution 

n this chapter, we will consider the part of the software engineering process that I takes place after the software is delivered. You may be surprised to learn that for many long-lived systems, maintenance accounts for more than 75 percent of the total cost of the software during its lifetime. For these long-lived products, this tip-of-the-iceberg situation occurs during times of considerable change in supporting technology and changing user expectations, and causes considerable changes that are called _software evolution_ if they are gradual and could be called _disruptive software_ otherwise. 

## 8.1  INTRODUCTION 

At first glance, it seems strange to apply the term _maintenance_ to software. After all, software does not wear out the way that a computer’s on/off switch or other hardware might. The medium on which software is stored may change over time, with magnetic particles worn off the surface of a disk or tape, or even having a compact disk bent. The first situation can occur both on an individual computer and in the cloud. Careful system administrators will keep backup copies of all essential software (and user files), ideally in physically separated locations, in order to avoid problems with fire and flood. 

Note also that software cannot rust nor can it fail because dirt gets in the middle of an electrical connection. Major changes to the power supplied to computers (e.g., 110 volt, 60 cycle alternating current in the United States; 220 volts in the United Kingdom) are not likely. Of course, power spikes or voltage reduction due to overtaxed electrical production facilities may have an effect, but these problems are well known. Prudent computer system administrators use a combination of surge suppressors, conditioned power sources, and uninterruptable power supplies to ensure the proper level of service. These problems are clearly hardware related and pose no particular problem for software engineers. 

The reliability of hardware systems generally follows a pattern such as the one illustrated in Figure 8.1. The relatively high number of failures early in the lifetime of the hardware 

**335** 

**336** ◾  Introduction to Software Engineering 



<!-- Start of picture text -->
Faults<br>Time<br><!-- End of picture text -->

FIGURE 8.1 The typical bathtub curve for malfunctions of electrical and mechanical equipment. 

is due primarily to three factors: faulty components, mistakes in the installation of these components, and improper usage by an inexperienced operator. The increased number of failures at the right-hand side of the graph represents failures that occur near the end of the hardware’s useful lifetime and are due to actual component failures. 

Hardware maintenance is different from hardware testing. For example, you should expect that a new car you recently purchased was assembled by experts using high-quality parts and had certain subsystems (such as those for electrical, steering, and braking operations) tested for safety. The car should also have received other basic checks when it was driven off the assembly line to a waiting cargo carrier and when it was driven from the cargo carrier to the dealer’s showroom. These are all considered testing activities. If a new car needed to have its brakes or steering fixed during the warranty period, you would probably regard the car as being of poor quality and would certainly not recommend that a friend purchase a similar car. 

You might also be very concerned if the plastic on your car dash split or the car rattled when going over bumps. On the other hand, if you had the same (non-safety-related) problems occur after 100,000 miles of operation, then you would probably consider fixing these problems as normal maintenance. You might choose to not fix these problems, because you might think that the remaining life of the car was so short that the maintenance expense was not worth it. 

A personal note is appropriate here. With the average cost of a new car in the United States being well over $30,000, the average monthly payment for a five-year term would be in the neighborhood of $580 per month, assuming little or no down payment and a very low interest rate. My decision is based on an estimate of the value of the repairs and the utility of the car. If repairs mean that a car will be able to run safely for an additional two months, then I expect the repairs to cost no more than $1,160. Beyond that point, I have to ask if the car is worth it. The same would be true for a $7,000 repair, if I expect the car to run for at least a year. Thus, I apply an informal cost-benefit analysis to determine if the car should be maintained, if the car should be donated to a high school automotive repair program (to take a deduction on my income tax), traded to a dealer, or junked. 

Proper maintenance of hardware involves keeping it clean, paying particular attention to moving parts, replacing faulty components, and generally planning to replace components 

Maintenance and Software Evolution   ◾ **337** 

that are old, obsolete, faulty, or at risk for imminent failure. A cost-benefit analysis should also be performed to determine if the maintenance effort is cost efficient, given the goals of the organization. Surprisingly, this approach is also a good way to view software maintenance. 

_Software maintenance_ could be described as the systematic process of changing software that is already in operation in order to prevent system failures and to improve performance. Software maintenance involves keeping software interfaces simple and standard, paying particular attention to troublesome modules, replacing faulty components, and generally planning to replace components that are old, obsolete, faulty, or at risk for imminent failure. The estimated remaining useful lifetime of the software must also be considered to determine if the maintenance effort is worth the added cost. 

After this informal introduction to the reasons for software maintenance, we proceed to a more systematic discussion of the subject. There are several factors that require software to be maintained: 

   1. Hardware platforms change or become obsolete. 

   2. Operating systems change or become obsolete. 

   3. Compilers change or become obsolete. 

   4. Language standards change or become obsolete. 

   5. Communications standards change or become obsolete. 

   6. Graphical user interfaces change or become obsolete. 

   7. Related applications software packages change or become obsolete. 

   8. Relationships with developers of other applications or systems software have changed. 

   9. Software may have defects that become evident only after the customer has used the software. These defects must be corrected. 

10. Customers demand new features. A recent newspaper article describes Workday, a product with about 600 business users that is working on its twenty-third release of a product first sold in 2007 (Hardy, 2014a). That is nearly a new release every four months! 

11. Software needs upgrades to be competitive with new competition. 

12. Existing software errors must be prevented from occurring in new releases of the software. 

These factors may be classified as belonging to several distinct groups. Factors 1 through 8 may be classified as adaptive maintenance, since they are intended to help the software adapt to new technology. Factors 9 through 11 may be classified as corrective maintenance, since they attempt to make the software more correct, in the sense that it has fewer faults. The term _perfective maintenance_ is also used in this case. Factor 12 may be classified as preventive maintenance, since it attempts to reduce the possibility of future software faults. 

**338** ◾  Introduction to Software Engineering 

There is one common thread, however. An essential step in all types of software maintenance is understanding the software system to be maintained. Before a maintainer can change software in order to fix a problem or add a feature, he or she must understand the software as a whole and the particular modules that need to be modified. Many experiments have indicated that program understanding, which includes understanding of software requirements and designs, takes approximately half of all maintenance efforts. Different approaches to software maintenance will be discussed in the remainder of this chapter. Keep in mind, however, that nothing in life is free and that any software maintenance activity must be budgeted for as part of the organization’s software budget. 

We will describe a typical approach to the software maintenance process that will consider the two actions of determining where the problem is and then fixing it. Many software problems can be traced to one or more of the following: 

- Lack of adherence to software development standards. These problems include poor interfaces between modules, such as passing the wrong number or types of arguments to a function. 

- Logical errors within program modules, such as loops, branches, or inconsistent program states. 

- Nonatomic actions. 

- Inconsistency between the requirements, design, code, and documentation for a system. 

Students are often surprised by the amount of difficulty that they have understanding either commercial or government code. I have used actual source code from many software development organizations in my classes and the response is almost identical: the code is poorly documented and hard to understand. In reality, the students are faced with the problem of examining all or portions of systems that are too large to be understood in their entirety. 

## 8.2  CORRECTIVE SOFTWARE MAINTENANCE 

The first step in _corrective software maintenance_ is to determine what needs to be maintained. In corrective software maintenance, all activity begins with the identification of a problem with the existing software. Determining the particular module that is the cause of a problem can be difficult. The basic approach is based on the technique of trial and error, guided by the maintainer’s knowledge of the system, and his or her basic knowledge of computer science and software engineering. 

Once problems have been determined, a decision can be made as to which, how, or when the problem will be fixed. This usually requires several related actions: 

- Observation that a problem exists 

- Documentation of the problem 

- Determination of the importance of the problem 

Maintenance and Software Evolution   ◾ **339** 

- Prioritizing the problems in order of importance of repair 

- Determining which problems will not be repaired, due to insufficient resources 

- Solution of the problem 

- Testing the system to see if the fix to this problem can cause any faults in other portions of the software 

- Documenting the solution as part of the source code 

- Documenting the solution in other forms of the documentation if changes have been made to the original system design 

- Updating a database of information about software errors 

This may seem like a lot of work—it is. Software maintenance must, by its nature, require large amounts of paperwork to update documentation. After all, the developers of software systems in industry or government rarely stay on the same project forever. With high turnover of personnel, written documentation that traces any changes made must be left for future maintainers of a system. 

Observation of a software problem can occur at several levels. In the most ideal situation, the observer is a person who is completely familiar with the system’s requirements. In this case, the documentation of the problem is immediate, and the determination of the source of the problem can generally be easily determined. 

A more common situation is for the persons observing the problem to be completely unfamiliar with the internal structure of the software. Indeed, the person observing the problem may even be unfamiliar with the software’s expected operation. This is typical of the type of problem that is first observed by novice users who then call a toll-free number for technical support of their new word processing or similar application. The technically knowledgeable person working in technical support is responsible for guiding the caller through the steps that led up to this presumed problem, to look for problems in the setup and configuration of the software, and, in short, to determine if the problem is due to an error by the user or an actual fault in the software. There are essentially only two possibilities: the user has misunderstood the installation and operating instructions, or the software is in error. 

Once the technical support person has determined that the user has misunderstood the documentation of either the system’s installation or operation, he or she has two remaining tasks. The user must be led through the correct steps to fix his or her problem. In addition, the technical support person must document the problem so that the documentation and the user interface can be improved. This is often done in a future release of the product. The technical support person should fully describe the documentation problems and turn them over to a person responsible for new releases of the system so that the user community will consider the new releases to be improvements. We note in passing that most computer documentation could be improved by the employment of a technical writer. 

In the case of a software fault, the user is not expected to provide detailed documentation of the details of the problem. The typical user does not have the technical ability and, in any 

**340** ◾  Introduction to Software Engineering 

event, it is not his or her job. The technical support person is responsible for taking the user’s information and organizing it into a format that can be used in the maintenance process. 

The goal of the person documenting a software problem is to be able to fill out a form as detailed as the one shown in Figure 8.2. This form is often called a software maintenance request form or software maintenance report form. Note that the form has places for complete descriptions of the problem and for an assessment of the relative importance of the problem. A sensible software manager generally will prefer to set priorities for the deployment of maintenance personnel based on an assessment of the relative importance of the problems encountered. A realistic estimate of the difficulty of fixing an incorrect module is also useful in assigning priorities. Some minor problems might never be fixed. 

After the problem has been fixed, another form should be filled out. This second form indicates the response to the software maintenance form and, as such, is often called a software maintenance response form. Figure 8.3 illustrates a typical software maintenance 



<!-- Start of picture text -->
Maintenancercquest number<br>System, Version Datc<br>Rclatcd maintenanccrcqucst numbers<br>Environment<br>Computer hardwarc:<br>Operating system Version<br>Relatcd systcm software:GUI<br>Relatcd applicationsoftware<br>Description of problem<br>Severity of problcm<br>Critical, Urgent, Important Routine<br>Classification:Hardware Softwarc._.. Documentation,<br>Person makingreport<br>Person verifying report<br>Datc problcm verificd<br>Organizationresponsiblcforfixingproblem<br><!-- End of picture text -->

FIGURE 8.2 A typical software maintenance request form. 

Maintenance and Software Evolution   ◾ **341** 



<!-- Start of picture text -->
Maintenance repair number<br>In response to maintenance request number<br>Related maintenance request numbers,<br>System Version Date.<br>Environment<br>Computer hardware:<br>Operating system Version<br>Related system software: GUI<br>Related application software<br>Severity of problem<br>Critical Urgent Important Routine,<br>Classification:Hardware Software, Documentation<br>Person making report<br>Person verifying report. Date<br>Person fixing problem<br>Resolution of problem<br>Person verifying solution<br>Modules affected<br>Time needed to fix problem<br><!-- End of picture text -->

FIGURE 8.3 A typical software maintenance response form. 

response form. Many organizations combine these request and response forms into a single form as shown in Figure 8.4. Note that the response form will always indicate a list of affected modules and the time needed to fix the problem. 

Note the importance of the extra documentation on these forms. The ability to attach hard copies of screen dumps is often very helpful to maintainers. If no screen dump facility is available in the software or operating system, a photograph of the screen can suffice. Obviously, a digital image is best. 

**342** ◾  Introduction to Software Engineering 



<!-- Start of picture text -->
Maintenance request number<br>Related maintenance request numbers<br>System Version Date<br>Environment<br>Computer hardware:<br>Operating system Version<br>Related system software: GUI<br>Related application software<br>Description of problem<br>Severity of problem<br>Critical Urgent Important Routine<br>Classification: Hardware Software Documentation<br>Person making report<br>Person verifying report<br>Person fixing problem<br>Person verifying solution<br>Resolution of problem<br>Modules affected<br>Time to fix problem<br><!-- End of picture text -->

FIGURE 8.4 A typical combined software maintenance report and response form. 

Maintenance and Software Evolution   ◾ **343** 

You may be concerned about the proliferation of paperwork required by these forms. Why have all this extra information? Who needs it? An actual example indicates the need for these activities. 

Suppose that you were examining a software system that had to be of highest quality because it was to be used without modification as the core of many other software products in a safety-critical application. Primarily because of its design and adherence to essential interface standards, this software had a much lower defect ratio (faults per 1,000 lines of code [KLOC]) than did most other software in the organization. However, high quality was not enough. Since this reusable core had to be reused in so many applications, it was important to check to determine where software errors tended to occur. 

An examination of a database of maintenance requests and responses indicated that 44 percent of identifiable software faults were traced to a single set of modules used to interface to an old locally developed command language. It was decided to scrap this command language and use a more modern one with a grammar that could be parsed easily using standard grammatical parsing tools such as flex and bison (the successors to the classical tools lex and yacc). The identification of the command language parsing tools as major sources of software maintenance costs certainly influenced this decision. 

Of course, there is no need to have the forms written on paper. The forms themselves can be stored electronically, with automatic entry of data into a database. Ideally, a software package that supports maintenance activities with automatic forms-generation and storage of information into a database would be available to maintainers. In many software environments, the lack of forms-generation capability is the most critical problem. 

The simplest solution is to enter the maintenance data in text format directly into a spreadsheet or database. We prefer to use the lowest level of technology in this book in order to be able to work in nearly all situations. 

## 8.3  ADAPTIVE SOFTWARE MAINTENANCE 

_Adaptive software maintenance_ is the process of changing software to meet new trends in technology or the marketplace. Expected changes in hardware, systems, interoperable application packages, and new features provided by the competition are all important in determining the need for adaptive maintenance of software. 

Consider the case of apps written for smartphones or tablets. An app designer focusing on devices running on a number of phones, each of which is running on multiple versions of the Android operating system, may have to change the apps to accommodate the most current versions or may have to settle for being consistent with the state of a previous operating system version. The layout of apps might have to change to have the proper look and feel for various screen dimensions. 

A designer for the Apple iOS devices may have fewer changes to consider, since there are fewer versions of iOS. However, the change of programming languages to Swift from Objective C may cause many problems if any new features are added to an existing app. 

Here is another example that illustrates the effect of changes in application development environments on software development, Ruby on Rails, especially with the need to have software be installed campuswide by professionals as well as by individual students. 

**344** ◾  Introduction to Software Engineering 

Notice the reference to Git, an open source configuration management system, as well as to Ruby-specific tools. The key concerns are, clearly, the need for the latest version of Rails and a seamless integration package. The information was posted to the SIGCSE (Computer Science Education Special Interest Group) mailing list by Professor Steven Bogaerts of DePauw University on May 2, 2014. 

Hi everyone – I’ll be teaching a course that uses Ruby on Rails in the fall, and I need to decide how to request our IT staff to install everything we need on campus machines. Students will also want to install this on personal machines, so ease of installation is important. 

In the past I’ve used http://railsinstaller.org, which has been very nice. It includes not just Ruby and Rails but also Bundler, Git, SQLite, etc, all integrated properly from the start. 

The problem is it uses Rails 3.2. I’d really like to be using Rails 4.x if possible. I did find http://railsftw.bryanbibat.net/, which looks similar to railsinstaller, only with 4.0.3. But it seems not to include quite as much as railsinstaller (I’m not sure of the consequences of this right now), and it’s also Windows-only. That’s not an insurmountable problem, but it is a slight complication. 

So I’m wondering how others have dealt with this problem: 

- Simplifying student installation procedures 

- Enabling use of Rails 4.x and various tools (as in railsinstaller) with no/minimal configuration required 

Has anyone had success with railsftw? Or a piecemeal manual configuration with the same tools that railsinstaller provides? I appreciate very much any suggestions you could provide, thank you! 

As another example, consider the case of Microsoft Word, which has gone through many versions since its inception. Some of these changes involve the user interface and usability. Other changes provided additional features and common file formats. Frequently, documents opened in one version of later versions of Word either cannot be read or have page formats changed by an earlier version of the same software. (This problem is not unique to Microsoft. The same statement applies to Corel WordPerfect, among others.) 

For some users, the advantage of a common file format in which documents can be read on both PCs and Macs is outweighed by having larger file sizes used for documents. For others, the additional features provided by macros may be less important than the additional security requirements to treat macro viruses, which may migrate from PCs to Macs and vice versa. 

As with corrective maintenance, considerable testing of software is necessary, especially regression testing. 

It is appropriate at this point to indicate some problems that cannot reasonably be expected to be uncovered during even the most exhaustive software testing. 

Unfortunately, standard testing procedures generally cannot detect erroneous events such as race conditions, which will occur very infrequently. The term _race condition_ refers 

Maintenance and Software Evolution   ◾ **345** 

to a situation where the result of a computation (or even the continuation of system operation) depends upon the order in which distinct concurrently executing processes get access to the CPU. 

An example of a race condition is shown in Figure 8.5. The value of the variable X at the end of the asynchronous computation depends on the order in which the concurrently running processes execute. 

There is another equally important problem that can cause problems for maintainers of concurrent systems, especially real-time systems. The maintainer of such systems must pay special attention to functions that make operating system calls but are not themselves atomic. (An “atomic instruction” is one that cannot be interrupted by an external event and, therefore, such instructions will always complete once their execution has started.) 

Scheduling of processes on one or more CPUs cannot be predicted and thus race conditions and nonatomic system calls can be disastrous. 

These two problems can occur in software systems that must execute concurrently with other processes. Both nonatomic function calls and race conditions are extremely dangerous for real-time or safety-critical systems, because the system cannot be guaranteed to operate successfully and because system run-time performance cannot be predicted. Even worse, testing cannot provide guarantees of the necessary system quality. 

In the case of nonatomic functions used to synchronize access to system resources, even the most exhaustive testing of a software system with concurrently executing processes will be inadequate, because the likelihood of a system failure during testing is small. Figure 8.6 illustrates the issue. 

The problem will occur because the synchronization depends on the values of two distinct variables, X and Y, which are tested in two distinct steps. However, if the processes get access to the CPU in such a way that the third instruction of process 2 executes before the third instruction of process 1, the synchronization condition may not hold, and access to the sharable resource may be granted (or denied) incorrectly. 

Another problem is particularly vexing for software maintainers. Many software engineers, especially those whose primary experience is with computers with large amounts of physical memory, do not think of their systems as having any limitations. However, memory can be exhausted, especially if there are commercial off-the-shelf (COTS) products whose memory demands are unknown. 

|Process 1|Process 2|
|---|---|
|X = 1;|X = 1;|
|Y = 7;|Y = 7;|
|X = X + Y;|X = X − Y;|



FIGURE 8.5 A race condition with different results of a computation, depending on the order in which instructions in a process are executed by the CPU. 

**346** ◾  Introduction to Software Engineering 



<!-- Start of picture text -->
Process1 Process2<br>X=1; X=1;<br>Y=7; y=7;<br>IF（X==1）AND （Y==7） X=X- Y<br>ACCESS shared resource; Y=X;<br>+X=X<br>Y=1;<br>SharedResource<br><!-- End of picture text -->

FIGURE 8.6 Access to a shared resource controlled by a nonatomic function. 

An equally difficult problem for maintainers is the use of excessive numbers of other restricted system resources. For example, two different software packages may each write data to the same socket (which may be implemented as a “winsoock” or a “socket descriptor,” depending on the operating system) for network communications, and this may cause unexpected conflicts. 

In another more complex example, the number of files that can be open at any one time for a user’s process can range from eight in programs using older versions of C to twenty for ANSI standard C to sixty-four on some UNIX systems (the “soft limit,” which can be increased by a system administrator) to the maximum allowable (the “hard limit,” often 100 on UNIX and Linux systems). 

You should be aware that the situation is especially complex if the software to be maintained must interact with many COTS products whose internal structure is not known. It is clear that a software maintainer may need many skills beyond simple programming experience. 

## 8.4  HOW TO READ REQUIREMENTS, DESIGNS, AND SOURCE CODE 

Once a maintenance problem has been given to a maintainer, the source code must be modified. However, many software systems consist of millions of lines of source code. Each line of source code has the potential to be the place where a problem occurs. Of course, not all problems in the user interface, for example, need to be checked. But where do we begin? 

A software maintainer will look at all available information: requirements, design, manuals and other documentation and, of course, the source code itself. The goal is to understand the likely effects of any changes in the software before the changes are made. Everyone who has written software is familiar with having a change in one portion of the software affect performance in some other portion. Thus, a systematic approach is necessary. 

Keep in mind the old adage: If the source code and any of the requirements, design, or documentation do not agree, they are all wrong. In this case, the source code is the only certain guide, because it reflects the system as it currently works, not as it was intended to work. The available source code is always read as part of the maintenance process. 

Let us suppose at this point that we are only considering source code. What do we look for first? 

Maintenance and Software Evolution   ◾ **347** 

The answer is composed of several parts. We would start by looking at the maintenance reports for related situations in the software to seek out any suggestions on where to look for problems. We would also make use of any available integrated development environment (IDE) or computer-aided software engineering (CASE) tool to analyze the source code and show the program’s structure. Be aware that, even if the original IDE or CASE tool in which the software was created is no longer available, perhaps due to obsolescence or to expiration of a license, it still may be possible to obtain information on the program’s structure using either newer IDEs or CASE tools available to the maintenance project, or even to freeware or shareware tools to analyze program structure. 

After we had obtained enough information to restrict our attention to a limited number of modules, each of them would be inspected at essentially the same level of detail as it would be in the type of code review discussed in Chapter 5. 

## 8.5  A MANAGER’S PERSPECTIVE ON SOFTWARE MAINTENANCE 

Although it may be surprising to students, software maintenance is one of the most costly items in the software life cycle. One thing that managers like is reducing costs. Senior managers recognize that software maintenance does not usually increase market share and cannot, therefore, aid in improving the organization’s bottom line. You can often help your manager by suggesting some ways that maintenance costs can be reduced. 

A database of maintenance requests and actions can be very helpful. For example, the system described in Section 8.2 had a maintenance database in which a simple query indicated that one particular software module was causing 44 percent of the traceable software failures. The problems were traced to new dialects of a command language, which were created with every new version of the software. Freezing the command language caused little functionality loss in the opinion of the users, but it reduced maintenance costs by a considerable amount. Managers like this type of information. It makes their job easier, especially in times of increased budget pressure, where reducing costs with little or no decrease in functionality or quality is a paramount goal. 

This kind of analysis of maintenance effort is extremely important to managers at all levels. For most commercial organizations, little revenue is brought in during maintenance unless new releases of the software are planned. Thus, maintenance is viewed as a cost to be minimized whenever possible. 

Of course, it is always essential to follow your organization’s standards-and-practices manual (if such a manual exists) for documentation procedures. 

## 8.6  MAINTENANCE COSTS, SOFTWARE EVOLUTION, AND THE DECISION TO BUY VERSUS BUILD VERSUS REUSE VERSUS REENGINEER 

As stated in Chapter 1, many software systems have very long useful lives. Think of the software used in the United States for providing checks for the Social Security Administration. The software originally provided for the printing of checks that were mailed to elderly and disabled people, as well as to the surviving parents or guardians of children under the age of 18, one or both of whose parents had died. Now the dispersal of funds is almost entirely Internet based, with funds transmitted to recipient’s bank accounts. The underlying software, used to 

**348** ◾  Introduction to Software Engineering 

analyze large databases to make this disbursement possible, runs on large mainframe computers, with very old computer languages such as COBOL and Codasyl-enabled databases that allow efficient, batch mode processing that is necessary for delivery of funds without delays. 

It is impossible to buy such software on the open market, so changes (which often occur due to changes in U.S. laws and regulations) are often done by a combination of building, reusing, and reengineering. Reengineering can be very difficult to understand for students and beginning programmers (Leach et al., 2008). 

Another example is Microsoft Word, which was a stand-alone word processor running on 16-bit microcomputers running an operating system with a text-based command-line interface in its first inception. Now, Microsoft Word is part of Microsoft Office, an integrated suite of tools running on an operating system that supports multiple windows, with a mouse as a device for pointing and selecting. Recently, Microsoft Office has been ported to tablet devices, with their own user interfaces depending on the use of a single touch of a finger for selection, sweep actions for selection of text, and pushing two finders together or pulling them apart to indicate changes in size, among other things. Rentals are available through the Office 360 program. This is more a case of reengineer, build, and reuse. 

Clearly, such systems _evolve_ , based on factors such as changing technology, competitive pressures, and the desire to reengineer to make software development more efficient. 

I think the best way to understand the issues is to consider a real-life example from the aerospace industry. (We have previously discussed this example in a simpler form.) Many satellites continued producing useful research data about the earth’s magnetic and atmospheric condition for many years beyond their expected useful life. The Interplanetary Monitoring Platform, hereinafter referred to as IMP-8, was launched on October 26, 1973, and data transmission was stopped on October 7, 2006, a term of 33 years. (The web portal for this project is http://spdf.gsfc.nasa.gov/imp8/project.html.) 

Because of the long lead times for planning, building, and launching many satellites, many of the hardware and software computer systems used to control the satellites and process the data had long been obsolete. Not surprisingly, hardware and software companies were deciding to not support their systems any more. 

In order to focus on its core business, Unisys decided to raise its annual charge for hardware and software maintenance of just its dedicated mainframe to the level of the entire budget for maintenance, operation, ground-based control, data storage, and personnel costs. The decision by Unisys was announced in 1997, nearly nine years before the IMP-8 project finally terminated, so there was a lot of useful data still to be collected. 

The decision was made to use entirely new computer hardware for ground control of the satellite and to simultaneously reengineer the software. The new computer hardware chosen was an HP workstation running HP-UX, a UNIX-variant, which was, essentially, a standard PC far more powerful than a 1970-vintage mainframe. 

The software was another matter, consisting of 33 files, containing a total of 108,161 lines of code. Most files contained both FORTRAN code and Unisys assembly language. The FORTRAN was ported to the most common dialect, FORTRAN 77, and the assembly code was rewritten in FORTRAN. csplit, a standard UNIX utility, was used to separate the 33 files into 584 separate files, each containing a single FORTRAN or Unisys assembly 

Maintenance and Software Evolution   ◾ **349** 

module. Freeware programs such as FORTRAN Source Code Analyzer (fsca) previously developed at Howard University, floppy, and flow, were used to create program control graphs. These metrics were used to identify 2 percent of the modules as having a complex internal structure and, therefore, requiring additional testing effort. By examining the files pairwise using the standard UNIX utility diff, it was determined that naming conventions had not been used but that the same source code was copied into other locations. With proper naming conventions, it was found that 19.4 percent of the files were duplicates, reducing potential maintenance effort by this amount. It was clearly much cheaper to reengineer than to buy or build this software. 

At times, software maintenance also provides an opportunity for code improvement. Here is a simple example. As stated in Chapter 6, the technique of multiple inheritance has fallen into disfavor because of the possibility that a portion of a class may be inherited along different inheritance paths. In some cases, if a portion of the code is newly written, it may be better for the test team to ask the coders to recode any software with multiple inheritance to avoid this problem. If the code has been used without incident for many years, the best choice may be to leave the code alone. 

We briefly turn our attention to software reuse. The most extreme case of software reuse is when an entire software system, such as a COTS product, is reused without change. The question we address is when is the reuse not cost-effective, due to a large number of evolutionary changes in COTS software that cause too many changes to systems, due to the hidden costs of configuration and testing of interfaces to systems for which the internal structure is not known, as is the case with most COTS products. A discussion generated by an important paper of Jeffrey Voas (1999) and followed up by research of Greg Saunders (2003) and myself (Leach, 2005) leads to the following suggestions: 

- Collect data on how your project spent its money. 

- Map this data over time to try to get a graphical image of how costs increased when new releases of COTS products occurred and had to be incorporated into a system. 

- Keep data on how much the process of upfront systems analysis and COTS evaluation costs and how long it takes. Consider the use of some less expensive, junior-level personnel as part of the COTS evaluation team, at least for the second or third iteration of the COTS-based system. 

- Consider ways to reduce the number of senior-level people kept on long-term projects, by phasing in some of the more junior personnel. You will probably have to do it anyway, because talented people want professional growth! 

- Make sure there are at least a few domain experts and senior software engineers always available, even if you have to pay more. Consultants may be of assistance in filling some portion, but not all, of this role. 

- Learn from your mistakes! 

**350** ◾  Introduction to Software Engineering 

## 8.7  MAINTENANCE IN AGILE DEVELOPMENT AND THE TOTAL LIFE CYCLE COSTS 

This is an easy section to write for a very simple reason: Agile development emphasizes rapid development of well-tested software in cooperation with a “customer.” It is highly unlikely that any significant portion of the agile development team will be around the organization, much less be willing to work on what is almost always a much less productive activity such as software maintenance, which requires an enormous effort in program understanding before a system can be maintained. 

Unfortunately, due to the volatility of agile software development teams, there is essentially no data that describes the amount of maintenance time and effort needed for the systems the agile development team has created, at least in the level of detail necessary to guide practitioners and managers. 

## 8.8  MAINTENANCE OF THE MAJOR SOFTWARE PROJECT 

One view of software maintenance would suggest that the system was already under maintenance when the requirements were changed to use the Internet. We will ignore the previous requirements change and instead consider some possible changes after delivery. 

The first type of maintenance to consider is corrective. Does the software behave as it should? After we have considered correctness, we must worry about the user interface and the potential for enhancements. Of course, performance issues can always arise if the response time needs to be improved. 

What about the human–computer interface? The original system has a user interface developed for a Windows-based PC. What changes are necessary for the Microsoft Windows, version 8.1? The maintenance effort might be focused on updating the software to work on later operating systems, with new language versions and application toolkits. 

A system intended for use in a single computer also could be ported to an Apple Mac computer and use the Apple user interface. It could also use the Linux-based operating system underlying the Apple user interface. (This Linux-based system is called Darwin.) What additional maintenance efforts must be required to port from a Windows-based computer to an Apple Mac? 

Could the system be reengineered to become web-based, with the metrics computations performed on servers or, perhaps, a set of individual servers each hosting many source code files? Could the user interface be based primarily on tablets, such as, say, a banking app with its connection to a remote database? Could it be created using only open source software? 

We will leave these issues to the exercises. 

## SUMMARY 

Much of the effort for software projects occurs after the software is delivered and installed. This is called the maintenance phase. 

Maintenance and Software Evolution   ◾ **351** 

There are three major types of software maintenance: 

1. Corrective maintenance 

2. Adaptive maintenance 

3. Preventive maintenance 

The Y2K problem is an example of preventive maintenance until the date changed and the problem occurred. It then became a corrective maintenance problem. 

There is an adage that describes the skepticism a maintainer must have: If the source code and any of the requirements, design, or documentation do not agree, they are all wrong. One of the major issues to consider during software maintenance and evolution is the decision whether to buy versus build versus reuse versus reengineer a complex, existing software system. 

## KEYWORDS AND PHRASES 

Software maintenance, software evolution, reengineering, corrective maintenance, adaptive maintenance, preventive maintenance, COTS 

## FURTHER READING 

Perhaps the best source of information for a beginning software engineer is a company’s software development standards and practices manual. Forms such as the ones given in this text are usually available from these documents. 

There are some general references on software maintenance available. The book _Software Change Impact Analysis_ , edited by Arnold and Bohner (1997), provides an excellent overview of the state of the art in assessing the impact of maintenance decisions. The book by Pigoski (1997) is also useful. 

See the articles by Voas (1999), Saunders (2003), and Leach (2005) for perspectives on COTS products during software evolution. 

There are several important articles on the important subject of software maintenance, and you should check some of the conferences that are more practitioner oriented. There is even a journal related to maintenance issues: the _Journal of Software Maintenance_ , which was renamed to the _Journal of Software Maintenance and Evolution: Research and Practice_ , and now is known as the _Journal of Software: Evolution and Process_ . 

### **EXERCISES** 

1. List at least ten software packages that will have to be changed to accommodate an increase in the number of characters used for Social Security numbers. 

2. List at least ten software packages that will have to be changed to accommodate changes in the number of digits used for phone numbers. 

**352** ◾  Introduction to Software Engineering 

3. List at least ten software packages that will have to be changed to accommodate changes in the UNIX date and time computation. Be sure to discuss the use of the make utility. 

4. Consider a popular application for personal computers. Describe major changes between successive releases. List them in the order of estimated likely costs. 

### **EXERCISES FOR THE MAJOR SOFTWARE PROJECT** 

   1. Examine the dialogue we presented in Chapter 3, when we developed the requirements for the large software project that we have discussed throughout this book. Based on that dialogue, what changes do you expect to be made to the software during its useful lifetime? 

   2. Compare the changes made in the software in the major project with the ones you might have predicted in the previous question. 

   3. Change the major software project to allow the separation of the computational portion from the user interface. Then incorporate a client–server relationship, with the computation done on a server and the user interface on a client machine. 

   4. Change the user interface for the current system in the major software project to run on Windows 8.1. 

   5. Change the user interface for the current system in the major software project to use the Apple user interface. 

   6. Change the user interface for the current system in the major software project to use the Linux-based operating system underlying the Apple user interface. (This Linuxbased system is called Darwin.) 

   7. Change the user interface for the current system in the major software project to become web-based, with the metrics computations performed on servers or, perhaps, a set of individual servers each hosting many source code files. 

   8. Change the user interface for the current system in the major software project to run its user interface based primarily on tablets, such as, say, a banking app with its connection to a remote database. 

   9. The first change is that the customer now wants a web-based user interface instead of one that is PC based. What changes need to be made to the maintenance processes? Is a new maintenance plan needed? 

10. The second change is that the customer now wants to use a cloud for data storage instead of one that is PC based. What changes need to be made to the maintenance process? Is a new maintenance plan needed? 

