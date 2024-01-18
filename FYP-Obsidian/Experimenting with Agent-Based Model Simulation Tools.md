---
Year: 2023
tags: Source
Authors: Alessia Antelmi, Gennaro Cordasco, Giuseppe D’Ambrosio, Daniele De Vinco, Carmine Spagnuolo
---

Title:: Experimenting with Agent-Based Model Simulation Tools
URL: https://www.mdpi.com/2076-3417/13/1/13
Zotero Link: [Full Text PDF](zotero://select/library/items/55SES3VD)

**1. Introduction** 
The introduction provides an overview of simulation models, emphasizing the effectiveness of agent-based models (ABMs) in representing real-world phenomena using a bottom-up approach. ABMs involve modeling autonomous entities (agents) that interact within an environment, leading to emergent behaviors. The applications of ABMs span various fields such as social science, economics, climate change, and epidemiology. Due to the proliferation of ABM tools, the paper addresses the challenge of selecting the right tool for modelers. The introduction reviews previous works that compared ABM software and introduces the motivation for the current paper.

The paper aims to present an overview of open-source general-purpose ABM tools, comparing them based on characteristics, functionalities, and scaling capabilities. It highlights the importance of ease of use and efficiency, providing a unique perspective on the state of ABM tools for newcomers. The contributions of the paper include discussions on ABM developing tools, a description of existing tools, a comparison of intrinsic characteristics and functionalities, and hands-on evaluations of installation, documentation, and model implementation. The outline outlines the structure of the paper, which includes sections on main concepts, existing ABM tools, comparisons, and hands-on experiences.

**2. Agent-Based Models and Simulations** 
This section introduces key concepts related to agent-based models (ABMs) and ABM tools.

**2.1. What Is an ABM?**

- ABMs consist of agents, environment, and rules.
- Agents represent the living population, the environment sets the context, and rules define interactions.
- Agents act autonomously, making decisions based on their environment to achieve internal goals.
- Agent behavior, including movement and communication, is defined by the modeler.
- Environment encompasses spatial grids, continuous spaces, and networks, and may use GIS data.

**2.2. What Is an ABM Tool?**

- ABM tools simplify the complexity of model implementation.
- They come in the form of frameworks and libraries.
- General-purpose tools can model any system, while special-purpose tools are domain-specific.
- Tools may prioritize ease of use or efficiency.
- Ease of use often involves graphical interfaces, while efficiency requires technical skills.

**2.3. What Are the Desiderata of an ABM Tool?**

- Desirable features include efficiency, ease of use, and a balance between them.
- Ready-to-use methods for common patterns in agent behavior, environment, and interactions.
- Support for GIS data, as it is crucial for realistic simulations in various domains.
- Handling multiple types of agents and fields within the same simulation.
- Analysis capabilities, including graphical visualization, statistical tools, real-time monitoring, and data visualization.
- Importance of random number generation for handling stochastic processes.
- Automated validation for reproducibility of results.
- Model exploration and optimization capabilities for parameter space experimentation.

**3. ABM Tools Overview**

In this section, the process of selecting ABM tools and a concise description of each tool are provided.

**3.1. Methodology**
- The selection focuses on open-source general-purpose platforms supported by peer-reviewed academic works.
- Data is gathered from Scopus and GitHub, excluding commercial, proprietary, or domain-specific tools.
- The final selection considers active support and peer-reviewed articles.

**3.2. ABM Tools Description**

1. **ActressMAS:** .NET-based, simple and easy to use, suitable for applications not requiring fast execution or a large number of agents.
2. **AgentPy:** Python library for scientific applications, integrated with IPython and Jupyter Notebooks, supports model exploration and parallel simulation.
3. **Agents.jl:** Julia-based framework for efficiency and ease of use, supports GIS data, model exploration, and parallel computing.
4. **Care HPS:** C++ tool for ABM on high-performance architectures, hides parallel programming complexity, extensible by expert developers.
5. **Cormas:** Smalltalk-based simulation platform, user-friendly for non-computer scientists, limited efficiency and scalability.
6. **CppyABM:** C++ library with Python compatibility, lightweight, relies on third-party packages for additional functionality.
7. **EcoLab:** C++ framework using TCL, supports parallel and distributed processing, manual handling of synchronization and partitioning.
8. **Evoplex:** C++ platform with modular approach, cross-platform, core library for model development, additional components for GUI and web visualization.
9. **FLAME:** Agent-based modeling system with XML language, automatically generates parallel code, suitable for various computing systems.
10. **FLAME GPU:** Extension of FLAME for GPU-based ABMs, uses CUDA for GPU programming, supports visualization without performance loss.
11. **GAMA:** Agent-oriented platform with GAML language, high ease of use, modular architecture, integrated with Eclipse IDE.
12. **Insight Maker:** Web-based modeling and simulation tool with a focus on accessibility, features VPL, web environment-specific functionalities.
13. **JADE:** Java FIPA-compliant framework for multi-agent systems, powerful GUI, scalable, easy to learn, widely used.
14. **JAS-mine:** Java-based toolkit for discrete-event simulations, integrates I/O communication, includes database explorer.
15. **krABMaga:** Rust-based toolkit for fast, reliable, discrete-event multi-agent simulation, re-engineered aspects of MASON architecture.
16. **MaDKit:** Lightweight Java library for designing and simulating agent systems, organization-centered approach.
17. **MASON:** Java-based toolkit for ABM, provides snapshot system, extensions for GIS data, model exploration, and distributed systems.
18. **MASS:** Multi-agent and spatial simulation library in Java, supports parallel ABMs using a coordinator–worker approach.
19. **Mesa:** Python-based ABM framework, extensible, actively supported, provides built-in core components.
20. **NetLogo:** Java-based modeling environment, widely considered standard, features VPL, extensive community support and extensions.
21. **Pandora:** ABM framework for large-scale distributed simulation, supports Python and C++, includes GUI tool Cassandra.
22. **Repast:** Family of ABM platforms available in several languages, e.g., Repast Simphony (Java-based), Repast4Py (Python-based).
23. **RepastHPC:** C++-based modeling system for high-performance computing, designed for large computing clusters and supercomputers.

the diverse set of ABM tools, each with its specific characteristics, programming languages, and focus on ease of use, efficiency, and scalability.

**4. ABM Tools Comparison**
In this section, a comparison of leading open-source general-purpose ABM platforms is presented, focusing on available features and the trade-off between ease of use and efficiency.

**4.1. Available Features**
The table below describes desirable features for ABM platforms, based on Section 2.3, including facilities for writing, running, analyzing, and optimizing ABMs. Tables 3 and 4 compare the tools according to their support for each feature.

| Feature                   | Description                                                                       |
|---------------------------|-----------------------------------------------------------------------------------|
| Programming Language      | Language used for model development.                                              |
| GUI                       | Availability of a Graphical User Interface (GUI) to control simulation execution. |
| Visual programming        | Use of a Visual Programming Language (VSL) for model development.                 |
| Simulation environment     | Fields and topologies available for creating the simulation environment.          |
| Visualization             | Possibility to graphically visualize the model.                                   |
| Snapshot and checkpoint    | Functionalities for pausing, saving, and resuming the simulation state.            |
| Modularity and reusability | Adoption of a modular design supporting code reuse for different simulations.     |
| Inspector                 | Facilities for retrieving the model's information during execution.                |
| Analysis tools            | Presence of tools for statistical and non-statistical analysis, chart creation.    |
| Random number generator   | Support for custom generation of random numbers.                                   |
| Batch runner              | Facilities for automatically performing multiple runs of the same simulation.      |
| Continuous Integration (CI)/Continuous Development (CD) | Facilities for automating code integration and delivery, tracking simulation versions. |
| Model exploration and optimization (MEO) | Facilities for exploring the model's behavior with varying input parameters and optimizing outcomes. |
| HPC                       | Exploitation of parallel, distributed computing, and integration with cloud platforms for in-model execution or optimization. |
Not explicitly reported is the feature "Modularity and reusability" as all frameworks support it to some extent, mainly through their model development language. GAMA is highlighted for introducing modularity by design through the co-modeling mechanism.

This comparison provides a comprehensive overview of the essential features offered by ABM platforms, aiding scientists in choosing a suitable platform based on their specific requirements and preferences.

  ![[Pasted image 20240118083332.png]]
  ![[Pasted image 20240118083404.png]]
  ![[Pasted image 20240118083435.png]]
  **4.2. Declared Ease of Use vs. Efficiency**

Assessing software platforms involves considering two critical and often conflicting criteria: ease of use and efficiency. For ABM tools, ease of use refers to the effort required for installation, setup, and availability of examples and documentation. Efficiency pertains to a tool's capability to handle large and complex models with low execution time.

**Ease of Use Evaluation:**
- **Very Low:** Poor modeling and execution APIs, requiring the developer to handle numerous tasks.
- **Low:** Good modeling but poor execution APIs.
- **Medium:** Comprehensive modeling and execution APIs.
- **High:** Improved by adopting well-known programming languages like Python or Java.
- **Very High:** Offers the previous level with a Domain-specific Language or Visual Programming Language designed for ABM.

**Efficiency Classification:**
- **Very Low to Very High:** Positioning based on the tool's potential to handle large-scale models and execution efficiency. Evaluated using a Likert scale.
![[Pasted image 20240118084035.png]]
**5. ABM Tools Evaluation** 
The evaluation of ABM tools from the developer's perspective focuses on the hands-on experience, considering installation and setup, documentation, examples, effort required, encountered problems, and the overall evaluation process.
**Evaluation Criteria:**

1. **Installation and Setup**
   - **N/A:** No installation guide available.
   - **Easy:** Installation script or installer provided, or the tool can be used as a standard library.
   - **Hard:** Vague installation information or requires technical expertise.

2. **Documentation and Examples**
   - **N/A:** No documentation or tutorials available.
   - **Basic:** Limited documentation; few or no examples.
   - **Good:** Comprehensive documentation; some examples provided.
   - **Extensive:** Detailed documentation covering all functionalities; multiple comprehensive examples.

3. **Effort**
   - Measured in hours, indicating the effort required to implement a single model.

4. **Problems**
   - Identification of errors or issues encountered during installation or usage.

**Hands-on Evaluation Process**
   - Developers with expertise in computer science and ABM independently installed and evaluated each tool.
   - Ratings were provided for installation, documentation, effort, and identified problems.
   - Discrepancies were discussed and resolved to reach a consensus.

Below given Table
   - Displays tools correctly installed and used in the upper part.
   - Lists tools with installation or example-running problems in the lower part, specifying encountered issues.
   - Effort is expressed in hours for developing a single model.
![[Pasted image 20240118084614.png]]
![[Pasted image 20240118084634.png]]
**5.2. Performance Evaluation**

The performance evaluation focused on assessing the efficiency and scalability of each ABM tool using four distinct ABM models: Flockers, Schelling, Wolf, Sheep, and Grass, and ForestFire. To ensure a fair comparison, meta-models were created for each model based on their NetLogo implementations, defining agents' behavior, simulation environment, and interactions. The meta-models served as a basis for consistent behavior across all tested platforms.

**ABM Models:**
1. **Flockers:** Simulates flock flying behavior with agents moving in a toroidal space following simple rules.
2. **Schelling:** A segregation model on a 2D grid where agents decide to move based on neighbor statuses.
3. **Wolf, Sheep, and Grass:** Multi-agent model simulating predator-prey population dynamics in a shared environment.
4. **ForestFire:** A stochastic spreading model using cellular automaton to replicate fire diffusion in a forest.

**Meta-Model Implementation:**
- Created meta-models for each ABM model based on their NetLogo implementations.
- Ensured the same behavior across all tested platforms.
- Verified existing model implementations from platform repositories and made adjustments if needed.

**Code Reusability:**
- Highlighted the ability to reuse code portions (e.g., agent definitions) across models within each platform.

![[Pasted image 20240118084751.png]]

This approach allowed for a standardized comparison of ABM tools, considering their performance in executing common ABM models and the extent to which code could be reused across different simulations.

**Conclusion Summary**

Agent-Based Models (ABMs) provide an effective bottom-up approach for studying complex systems, addressing challenges traditional methods may find difficult. This review aims to assist scientists in selecting appropriate ABM tools based on their needs and skills. The evaluation covers off-the-shelf considerations, hands-on experience in developing ABM models, and performance assessments.

**Key Findings**
1. Most platforms align with their authors' goals, offering a variety of features.
2. GAMA and NetLogo stand out for extreme ease of use, suitable for lay users.
3. MASON and krABMaga strike a good balance between ease of use and efficiency.
4. FLAME GPU, RepastHPC, and MASON (with its distributed extension) excel in performance but require extensive training.
5. Agents.jl and Mesa are ideal for modelers seeking deep insights and data analysis capabilities.

**Considerations for Modelers**
1. Choice depends on technical skills, application requirements, and specific features needed.
2. Evaluation factors include programming language comfort, functionality requirements, and model scale/complexity.
3. No perfect ABM platform exists; the right tool depends on the user's priorities.

**Future Perspectives**
Exploring ABM tools in distributed computing domains like federated learning and blockchain systems could be a promising avenue for future research, informing feature development in these contexts.