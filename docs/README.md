---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e18-4yp-Software-Package-To-Support-Agent-Based-Modelling-Based-Decision-Making
title:
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Software Package To Support Agent Based Modelling Based Decision Making

#### Team

-  E/18/017, Aarah J.F., [e18017@eng.pdn.ac.lk](mailto:e18017@eng.pdn.ac.lk)
-  E/18/177, Khan A.K.M.S., [e18177@eng.pdn.ac.lk](mailto:e18177@eng.pdn.ac.lk)
-  E/18/304, Rishad N.M., [e18304@eng.pdn.ac.lk](mailto:e18304@eng.pdn.ac.lk)

#### Supervisors

- Dr. Damayanthi Herath, [damayanthiherath@eng.pdn.ac.lk](mailto:damayanthiherath@eng.pdn.ac.lk)
- Dr. Rajith Vidanaarachchi, [rajith.v@unimelb.edu.au](mailto:rajith.v@unimelb.edu.au)

#### Table of content

1. [Abstract](#abstract)
2. [Introduction](#introduction)
3. [Related works](#related-works)
4. [Methodology](#methodology)
5. [Experiment Setup and Implementation](#experiment-setup-and-implementation)
6. [Results and Analysis](#results-and-analysis)
7. [Conclusion](#conclusion)
8. [Publications](#publications)
9. [Links](#links)

---

<!-- 
DELETE THIS SAMPLE before publishing to GitHub Pages !!!
This is a sample image, to show how to add images to your page. To learn more options, please refer [this](https://projects.ce.pdn.ac.lk/docs/faq/how-to-add-an-image/)
![Sample Image](./images/sample.png) 
-->


## Abstract
Agent-based modeling (ABM) is a powerful tool for studying complex systems and decision-making processes. This research contributes to the advancement of Agent-Based Modeling by proposing a transformative extension to the Mesa Python framework, specifically designed to enhance decision-making in ABM environments. Acknowledging the framework's current limitation of not supporting three-dimensional (3D) environments, our study focuses on smoothly integrating Triangular Meshes into Mesa. This integration aims to boost the framework's spatial simulation capabilities, which are essential for accurately representing complex surfaces and terrains in decision-making scenarios. Our objectives include exploring integration strategies, validating through case studies, implementing Triangular Mesh integration, evaluating performance, and extending the solution for scalability and generalization. The proposed software package targets decision-makers using ABM, providing an enhanced representation of spatial dynamics applicable in environmental simulations, structural engineering, and astronomy. Subsequent sections offer a thorough overview of our methodology, results, and implications, illustrating our efforts to empower the Mesa Python framework for more effective decision support in Agent-Based Modeling.

## Introduction
Agent-Based Modeling (ABM) stands as a powerful methodology for comprehending the intricacies of complex systems and decision-making processes. ABMs simulate how individual entities, or agents, interact and behave in a given environment, offering valuable insights for informed decision-making. However, the effectiveness of ABMs relies on how accurately the environment is represented. Mesa Python framework, historically limited to two-dimensional (2D) spaces, faces challenges in handling the complexities of three-dimensional (3D) scenarios.

This research aims to overcome Mesa's 2D limitations by proposing a significant upgrade for spatial simulations in 3D environments, with a particular emphasis on the implementation of Triangular Mesh. Despite Mesa's essential role in ABM, contributing significantly to simulation studies[1], its inherent lack of native 3D support poses constraints in scenarios requiring detailed 3D representation.

The motivation for this upgrade stems from a recognized gap in the existing literature, highlighted by Patel's influential work in 2019 [2]. Patel emphasizes the need to expand Mesa's class structure to include (x, y, z) positions for agents, addressing the current limitation of Mesa's HexGrid grid, which only accommodates (x, y) positions. This extension proves crucial for achieving more realistic simulations, introducing a 3D-like modeling grid.

<img src="images/table1.PNG"/>

According to the insights derived from the comparative table based on [3][4], our choice of Mesa as the preferred Agent-Based Modeling (ABM) framework is underpinned by careful considerations. Table1 compares various ABM tools based on factors like proprietary languages, non-proprietary languages, and 3D visualization capabilities, serves as a valuable guide in understanding the strengths of different frameworks.

Informed by this comparison, we specifically opted for Mesa due to several key factors. Notably, Mesa stands out for utilizing the Python language, a widely adopted and user-friendly programming language within the scientific community. Python's popularity is not only attributed to its ease of use but also to its extensive libraries that facilitate data processing and analysis, making it a favored choice for scientific research and modeling.

Additionally, Mesa's compatibility with Python aligns with the growing trend in the scientific community, where Python has become the language of choice. The gentle learning curve and the availability of a rich ecosystem of data analysis and visualization tools in Python make it an attractive option for researchers and developers. This aligns with our goal of creating a user-friendly and accessible ABM framework that caters to the diverse needs of decision-makers.

Furthermore, the table reflects that Mesa, despite its 2D limitation, outshines other frameworks in terms of its language choice and non-proprietary nature. While other frameworks might utilize proprietary languages or lack the flexibility to import a variety of toolkits and libraries, Mesa's use of Python ensures a more open and adaptable environment.

The heart of our research lies in the implementation of Triangular Mesh within Mesa. Triangular Meshes offer a sophisticated solution for representing complex surfaces and terrains in 3D. This implementation enhances Mesa's spatial simulation capabilities, providing a detailed and accurate representation of the environment. Triangular Meshes excel in capturing irregularities, making them indispensable for scenarios where precision matters, such as environmental simulations, structural engineering, and astronomy.

This paper outlines our approach to upgrading Mesa, emphasizing the exploration of integration strategies, validation through case studies, the pivotal implementation of Triangular Mesh, performance metric evaluation, and considerations for scalability and generalization. The envisaged software package aims to meet the diverse needs of decision-makers using ABM, offering an advanced representation of spatial dynamics applicable in various fields such as environmental simulations, structural engineering, and astronomy. Subsequent sections delve into the intricacies of our methodology, present results, and illuminate the implications of our efforts, showcasing the potential for more effective decision support in Agent-Based Modeling.

In conclusion, our research aims to elevate the Mesa Python framework, both metaphorically and literally, by introducing 3D support through the integration of Triangular Meshes. This enhancement, especially the implementation of Triangular Mesh, is poised to substantially improve the realism and accuracy of spatial simulations within ABM, contributing significantly to the broader landscape of computational modeling and decision-making.

## Related works
The literature review delves into four key papers on Agent-Based Modeling (ABM) tools, each offering unique insights. Reference [4] extensively compare various ABM tools, assessing features such as Available Features, Ease of Use, and Performance, aiding researchers in tool selection. From this, researchers can glean an understanding of the strengths and weaknesses of individual tools, facilitating an informed decision-making process. Reference [5] focus on MASON, Swarm, Repast, and NetLogo, emphasizing Programming Experience and Execution Speed, providing valuable practical and performance considerations. This offers insights into the user experience and computational efficiency, guiding researchers on the practical aspects of working with different ABM tools. 

<img src="images/table2.PNG"/>

Reference [6] survey presents a comprehensive list of ABM tools, offering a broad overview without direct comparison but serving as a valuable resource for understanding the diverse landscape. Researchers can extract a wealth of information regarding the range of available ABM tools, expanding their awareness of potential options. Refernce [7] conduct a thorough review, evaluating ABM tools on multiple criteria, providing a comprehensive understanding for decision-makers with diverse research requirements. This enables decision-makers to consider various aspects, such as language, model scalability, and development effort, when selecting tools aligned with their specific needs. Together, these papers contribute to a holistic understanding of ABM tools, covering features, user experience, programming, and overall suitability for varied applications, guiding researchers in selecting tools aligned with their specific needs. The Table2 gives an over all idea of the tools and the criteria used to make comparative analysis in those 4 papers.

## Methodology

## Experiment Setup and Implementation

## Results and Analysis

## Conclusion

## Publications
[//]: # "Note: Uncomment each once you uploaded the files to the repository"

<!-- 1. [Semester 7 report](./) -->
<!-- 2. [Semester 7 slides](./) -->
<!-- 3. [Semester 8 report](./) -->
<!-- 4. [Semester 8 slides](./) -->
<!-- 5. Author 1, Author 2 and Author 3 "Research paper title" (2021). [PDF](./). -->

## Links

[//]: # ( NOTE: EDIT THIS LINKS WITH YOUR REPO DETAILS )

- [Project Repository](https://github.com/cepdnaclk/repository-name)
- [Project Page](https://cepdnaclk.github.io/repository-name)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

[//]: # "Please refer this to learn more about Markdown syntax"
[//]: # "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"
