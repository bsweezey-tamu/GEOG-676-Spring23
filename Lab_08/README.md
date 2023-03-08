Brett Sweezey GEOG 676 E-Portfolio: Master Well Dataset
======

Industry Problem: There are discrepancies between physical oil well locations which arise from the accumulation of data from various online databases. The manner in which geographical location is collected and recorded can differ between private inudustries and local and federal government organizations. Variation in data may be the result of inaccurate or old data sets and the use of incorect coordinate systems that are projected onto ArcGIS maps. 

Project Proposal and Goal
------
This project will be designed to create a software tool that will combine the location data from various industry oil well databases that may include similar, yet conflicting geographical information. This tool will: 1) Include database information from CAD, Decision Sapce Geographics, Petrel, OpenWells, COMPASS, and state regulatory databases. 2) Calculate the inverses between oil well locations from imported databases and create a new Master Well location database with the most accurate and updated trending position 3) Determine whether the coordinates within each database are in the coordinate systems NAD83 or NAD 27 4) Develop a tool that allows the end user to select the master well location through different aerial images.

Languages, Software, and Database Construction
------
The proposed tool will be developed through the use of the coding language Python, due to its versatility, ease of use, and accessibility compared to other commonly used langauges. The benefit of using Python will allow the end users with limited coding experience to have an increased likelihood of understanding and customizing the proposed software (if they find that necessary). One benefit of using Python for this tool is due to the seemless transition of Python code with ArcGIS through the ArcPy package established by ESRI. In order for the end user to have full access and integration of the proposed tool, it is recommended that they have access to Python, Visual Studio Code, GitHub, Git Extensions, ArcGIS Pro, and ArcPy.

   ### _Visual Studio Code_
Visual Studio Code (VSC) is an open-source code editor designed for writing and debugging modern web and cloud applications. VSC will be useful due to the similarities outline with Python listed above (versatility, ease of use, accessibility) and it is free on all major computing platorms. Python can be easiliy integrated into VSC through installing the 'Python' package which will ease the production of the coding process as well as use a simple user interface (UI) which is easily understandable for the end user. 

### _GitHub_
GitHub allows users to upload and store data through respositories that can be stored online and be made available publicly or to a select group of individuals. The propsed Master Well Dataset will be stored in an online private repository to minimize the likelihood of end users manipulating and changing the final product. The finalized well database can be distributed through trusted users with direct access to this repository. If sucessful, a separate additional repository with the Master Well Database may be created to allow public access for modification and edits to improve the end user's experience within the tool's script. These repositories will include the well location databases from the data sources taken from the various industries used to develop the Master Well Database.

### _Git Extensions_
Git Extensions is a standalone UI tool specifically designed for managing Git respositories which can be access from multiple platform and records the history of files that have been uploaded or removed. This software is designed to overcome the complications for users with limited coding experience pushing their Python code from VSC to their Github repository. Git Extensions can be seamless integrated with VSC, Python, and ArcPy to accurately and rapidly update a repository with the click of a single button.

### _ArcGIS Pro_
ArcGIS Pro is an advanced spatial mapping software developed by ESRI which has the capacity to create, view, and edit maps with the capacity to integrate powerful spatial analysis statistics. ArcGIS Pro is an industry standard when dealing with complex spatial structures and tackling geolocation problems such as proposed by the tool created for this project. ArcGIS can work seamlessly with Python through the ArcPy package which will allow the end user to view the output and results from this tool.

### _ArcPy_
ArcPy is a Python package that allows for seamless integration of Python code within ArcGIS Pro that allows for GIS functions to be written and carried out in the Python language without the requirement of opening ArcGIS software. ArcPy will be necessary for the Python code written in VSC to be interpretted and run without complications with the ArcGIS Pro infrastructure. 

### __Master Well Location Database__
The finalized Master Well Database will be composed of input and output file from the proposed software tool. End users will have access to the original input source well location databases as well as the output data including the steps used to produce the finalized output for our proposed tool. Users will have access to the Python code used to construct the Master Well Database in addition to instructions including a flowchart on how data was gathered, constructed, and analyzed to allow users to replicate these processes.

### __Industry Well Databases__
To streamline the collection of data for the end user, databases used for this project (CAD, Decision Sapce Geographics, Petrel, OpenWells, COMPASS, and state regulatory databases) will be gathered within a local repository with public access. These specific databases were chosen due to their common use within the oil and gas industry. Meta data regarding how information was collected and processed will be included within this repository. Additionally, it is likely that additional databases may be added to our Master Well Database in the future to increase location accuracy and account for the variation in geolocation data across as many databases as possible. 

Project Outline
------
1. The script for the Master Wells Database will be written using the Python coding language integrated with VSC and the ArcPy package. Once this is created, the original code will be uploaded to a private repository on Github which will be accessible to trusted individuals. The software tool will be uploaded to a public repository which can be created and accessed using the examples created in [Lab 1](
