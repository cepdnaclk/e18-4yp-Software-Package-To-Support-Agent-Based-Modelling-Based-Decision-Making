---
Year: 2015
tags: Source
Authors: David Masad, Jacqueline Kazil
---

Title:: Mesa: An Agent-Based Modeling Framework
URL: https://conference.scipy.org/proceedings/scipy2015/jacqueline_kazil.html
Zotero Link: [Full Text](zotero://select/library/items/XKNVAT9U)

**Mesa: An Agent-Based Modeling Framework**” Green Highlight [Page 1](zotero://open-pdf/library/items/XKNVAT9U?page=1&annotation=MARVZKFZ)

https://www.youtube.com/watch?v=lcySLoprPMc” Yellow Highlight [Page 1](zotero://open-pdf/library/items/XKNVAT9U?page=1&annotation=GPLCJSVH)
This is a presentation by Jackie Kazil and David Masad on Agent Based Modelling in Python With Mesa.

What is agent Based modeling?
	computer simulation that consists of agents interacting with one another in order to study an overall system

Conway's Game of Life models' simulation was shown in the video

What is Mesa?
	python package
	Open-Source, Apache-licensed, and on Github.
	Modular
	Browser-based visualization (none of the ABM tools don't have)
	
Future Work
	Networks
	Checking and fixed seeds
	More and More better visualizations
	Optimization
	Scaling
	Geospatial tools
		

	
Introduction[Page 1](zotero://open-pdf/library/items/XKNVAT9U?page=1&annotation=ZGAJCSUU)

The introduction of the research paper discusses agent-based modeling, a simulation method involving autonomous entities or agents with defined rules and states. It highlights advantages of agent-based modeling, such as capturing dynamic system histories, incorporating spatial attributes, and establishing sufficiency theorems. The example of Thomas Schelling's model on neighborhood segregation is presented to demonstrate the emergence of higher-order phenomena from agent interactions.

The paper introduces Mesa, an open-source Python package for agent-based modeling, addressing perceived weaknesses in existing frameworks by leveraging Python's popularity and versatility. Mesa allows quick creation of models, visualization through a browser-based interface, and analysis using Python's data tools. The design choices of Mesa, such as multiple agent schedulers and tools for efficient model analysis, are discussed. The importance of interactive data analysis and live visualization in agent-based modeling is emphasized, with Mesa utilizing the browser as a front-end for visualization.


Architecture
Overview
The architecture of Mesa follows a guiding principle of modularity, allowing flexibility in modeling different scenarios. It is designed to make minimal assumptions about the structure of models, accommodating variations such as spatial components or the necessity of visualizations. Mesa's architecture is divided into three main categories: modeling, analysis, and visualization.

1. **Modeling Components:** These form the core elements needed to build a model. This includes:
    - **Model Class:** Stores model-level parameters and serves as a container for other components.
    - **Agent Classes:** Describe the characteristics of model agents.
    - **Scheduler:** Controls agent activation and manages time in the model.
    - **Space/Network Components:** Describe the spatial or network context in which agents are situated.
2. **Analysis Components:** These components focus on data collection and model analysis:
    - **Data Collectors:** Record data from each model run.
    - **Batch Runners:** Automate multiple runs and parameter sweeps.
3. **Visualization Components:** These are responsible for mapping a model object to visual representations:
    - Utilizes a server interface to display visualizations in a browser window.

The architecture promotes modularity by providing a set of components that can be easily combined and extended to build diverse models. The UML diagram in Figure 2 illustrates the relationships between these components. The example model of wealth distribution is used to demonstrate the practical implementation of Mesa's architecture, involving the creation of classes for the model object and agents, along with initializations for parameters such as the number of agents and their initial wealth.

Schedular
In Mesa's agent-based modeling framework, the scheduler is like the director of a play, managing the flow of events in simulations. Mesa makes it easy for modelers to choose how agents get activated and try out different ways of scheduling. The scheduler is like a flexible tool, separated into a special class, that guides when agents do their actions, influencing what happens in the simulation. The text explains different scheduling styles, like everyone acting together or in a specific order. It shows how Mesa's scheduler works by using an example of a model about how wealth is distributed. This example demonstrates how easy it is to make agents do things and move the simulation forward. In simple terms, Mesa's scheduler is like a handy tool that gives modelers lots of options to experiment and be flexible when creating agent-based models.

Space
Mesa provides two broad classes of space: grid and continuous. Grids are discrete spaces with rectangular cells, and agents may occupy specific cells. The concept of toroidal grids, where edges wrap around, is introduced to prevent artifacts at the edges. Mesa's grid classes include SingleGrid and MultiGrid, enforcing different cell occupancy rules. Cell neighborhoods, such as Moore and Von Neumann neighborhoods, are explained, offering flexibility based on model specifics. ContinuousSpace, inheriting from Grid, allows agents to have arbitrary coordinates, defining neighbors based on distances. The implementation of space in the example model involves agents moving around a MultiGrid. The `MoneyAgent` class is updated to include movement and wealth exchange behaviors based on spatial considerations. The `MoneyModel` class incorporates MultiGrid to place agents and defines methods for agent movement and wealth exchange.

Data Collection
highlights the two main approaches: visualization for qualitative examination and quantitative data collection. Mesa provides a generic DataCollector class that facilitates the extraction and storage of model and agent-level variables, as well as custom tables for event logging. Model- and agent-level variables are added to the data collector with collection functions, and the collect method stores the results in a dictionary associated with the current step of the model. Tables allow logging by the model or agents for specific events and associated data.

The data collector can be placed within the model class or used externally, providing flexibility in data collection frequency. Mesa's data collector stores variables and tables internally, allowing easy export to JSON or CSV. Integration with Python's scientific and data-analysis ecosystems is emphasized, with methods for exporting data to pandas data frames. An example using the MoneyModel demonstrates how to use a data collector to collect wealth data at each step, run the model, and analyze the results. The resulting wealth distribution illustrates the potential insights gained from agent-based modeling and data collection.

Batch Runner
BatchRunner in Mesa is a vital tool for exploring stochastic agent-based models (ABMs), allowing multiple runs with different parameter values to comprehensively understand their impact on system behavior. Instantiated with a model class and parameter dictionaries, BatchRunner systematically tests all parameter combinations using Python's itertools library. It orchestrates model execution, collects data, and, akin to DataCollector, efficiently stores results in pandas data frames for further analysis. An example demonstrates its versatility by adapting a model for variable starting wealth and employing BatchRunner to test diverse values, visualized in a scatter plot. In summary, BatchRunner is a robust Mesa feature facilitating systematic parameter exploration and efficient data collection for in-depth model analysis.

Visualization
Mesa's visualization system facilitates model observation through a server-client setup. Divided into server and client components, it employs a WebSocket connection to send model data from the server to the client for visualization. Mesa provides pre-built visualization elements, such as the ChartModule, which can be easily deployed. The server-side of a visualization module is a Python object with a render method, while the client-side is a JavaScript class. The ModularServer class manages visualization modules, and a Tornado server launches the visualization. The client includes a GUI controller for model control. Mesa's visualization capabilities allow for interactive and dynamic exploration of agent-based model behavior. An example of creating a live chart of the Gini coefficient is demonstrated using the ChartModule. Additionally, the creation of a custom histogram visualization module is outlined, illustrating the integration of Python and JavaScript components for model visualization.

Conclusion
Mesa presents a dynamic and comprehensive framework for constructing, analyzing, and visualizing agent-based models (ABMs). Addressing a gap in the scientific Python ecosystem, Mesa incorporates unique features like its schedule architecture and in-browser visualization. While currently a work in progress, Mesa aims to introduce enhancements such as inter-agent networks, improved random seed management, and video-style scrubbing through model runs. Future plans include geospatial simulation tools, enhanced efficiency, and collaborative contributions from researchers to enrich the framework. Mesa's open-source nature fosters ongoing development and community collaboration, marking the beginning of a collaborative effort to enhance Python's scientific ecosystem.