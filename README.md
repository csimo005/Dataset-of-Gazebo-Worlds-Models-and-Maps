# Dataset-of-Gazebo-Worlds-Models-and-Maps
- A set of Gazebo worlds models and maps that I use for testing Navigation2
- These models are tested using Gazebo 9 and Gazebo 11.

## How to use the models
1- Copy the model you want to use in .gazebo/models directory.

or

- Set Gazebo model path for the worlds with models directory

2- Gazebo -> Insert -> <World_Model_Name>

or

- go to gazebo word directory and type `gazebo example.world`

Most models come with maps.

### AWS Small House
 - `export GAZEBO_MODEL_PATH=/home/<user_name>/.gazebo/models/small_house/models/`
 - `gazebo small_house.world`
 ![Small_House](https://github.com/mlherd/gazebo_worlds_models_for_testing_navigation/blob/master/worlds/small_house/small_house.jpg?raw=true)

### AWS Office
 - `export GAZEBO_MODEL_PATH=/home/<user_name>/.gazebo/models/office/models/`
 - `gazebo office.world`
 ![Office](https://github.com/mlherd/gazebo_worlds_models_for_testing_navigation/blob/master/worlds/office/office.jpg?raw=true)
 
### AWS Bookstore
 - `export GAZEBO_MODEL_PATH=/home/<user_name>/.gazebo/models/bookstore/models/`
 - `gazebo bookstore.world`
 ![Bookstore](https://github.com/mlherd/gazebo_worlds_models_for_testing_navigation/blob/master/worlds/bookstore/bookstore.jpg?raw=true)

### AWS Hospital
 - unzip the models_part# into a dicrectory called models
 - `export GAZEBO_MODEL_PATH=/home/<user_name>/.gazebo/models/hospital/models/`
 - `gazebo hospital.world`
 - `gazebo hospital_two_floors.world`
 ![Hospital](https://github.com/mlherd/gazebo_worlds_models_maps_for_testing_navigation/blob/master/worlds/hospital/hospital.png?raw=true)
 
 #### Hospital with Two Floors
 
 ![Hospital_Two_Floors](https://github.com/mlherd/gazebo_worlds_models_maps_for_testing_navigation/blob/master/worlds/hospital/two_floor.png?raw=true)

### Custom Factory
 - `export GAZEBO_MODEL_PATH=/home/<user_name>/.gazebo/models/factory/models/`
 - `gazebo factory.world`
 ![Factory](https://github.com/mlherd/gazebo_worlds_models_maps_for_testing_navigation/blob/master/worlds/factory/factory.jpg?raw=true)

### To Do
 - [ ] Hospital: Move photos into corresponding model directories
 - [ ] Small House: Move photos into corresponding model directories
 - [ ] Office: Some tables are not rendering in the office environment, shows floating computers
 - [ ] Office: Move media into corresponding models folders 
 - [ ] Factory: Gazebo complains about repeated names inside factory.world
 - [ ] Combine all models folders into one large folder 
