---
Year: 2022
tags: Source
Authors: Andrew Crooks, Vincent Hess
---

Title:: Mesa-Geo: A GIS Extension for the Mesa Agent-Based Modeling Framework in Python
URL: https://www.academia.edu/89896717/Mesa_Geo_A_GIS_Extension_for_the_Mesa_Agent_Based_Modeling_Framework_in_Python
Zotero Link: 

**1. Introduction**
   - Agent-based modeling (ABM) is a computational method for simulating complex systems of heterogeneous agents.
   - ABM captures dynamics across temporal and spatial scales to reveal macro patterns.
   - Mesa is an open-source ABM framework in Python; Mesa-Geo is its geographical information system (GIS) extension.

**2. Background**
   - ABM has seen growth in applications, and various tools like Repast, GAMA, and Mesa have been developed.
   - Mesa-Geo addresses the lack of direct support for geographical data in Mesa, allowing the importation, analysis, and visualization of georeferenced data.
   - GIS data comes in raster and vector models; Mesa-Geo introduces GeoAgents and Cells to handle both.
  
**3. Framework Architecture**
   - Mesa-Geo builds on Mesa's modular design, introducing GeoAgents, Cells, and GeoSpace to handle geographical data.
   - GeoSpace supports multiple layers of raster and vector data, enhancing the representation of agents and space.
   - Model visualization includes a MapVisualization element using Leaflet.js for displaying GeoSpace in a web browser.
   - Data exportation allows users to export simulation results as raster and vector files for further GIS analysis.

**4. Applications**
   - Example applications demonstrate Mesa-Geo's functionalities, including:
      - Digital Elevation Model (DEM) for rainfall simulation.
      - Overlay of raster and vector data to create a population model.
      - Schelling segregation models using NUTS-2 regions.
      - Agents and Networks model simulating traffic with road network data.

**5. Summary and Outlook**
   - Mesa-Geo addresses the need for integrating geographical data with ABM in Python.
   - The tool is still under active development, and potential improvements include optimizing network communication and linking model outputs to spatial analysis libraries like PySAL.
   - Mesa and Mesa-Geo are open-source, allowing researchers to use and enhance them.

