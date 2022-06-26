Lepto Classifier Frontend Project
---
**The goal**

The goal of the frontend project is to provide an easy method for doctors around the world to utilize UC Davis data to diagnose leptospirosis. 

**What will it look like?**

The result will be a simple and easy to use front-end webpage that anyone in the world can use to easily input required patient data and blood work in order to be run by the algorithm. 

**What does it need to do?**
- Allow the user to easily upload bloodwork data and patient data
- Parse incoming patient data from the PDF file
- Run the [lepto-classifier](https://github.com/sf-deng/lepto-classifier) machine learning model on the data
- Return the result to the user
- Save the data to a database for further analysis and for iteration on the ML model
- Provide an easy method for retrieving data from the database in the future (Similar to [cardinal](https://github.com/JakeRoggenbuck/cardinal)

Please take a look at the full document outlining this project [here](https://docs.google.com/document/d/1_JbwD9eq7wKAGS854u0sA33uxKoX0pj0M-58mrS5z4s/edit?usp=sharing)
