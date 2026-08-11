# DPS Analytics Dashboard
The code in this repository is used to create the DPS Analytics Dashboard and uses Dash, Plotly and Pandas.

## Prerequisites
The scripts developed for format work were developed using `miniforge`, and `conda-forge`. This dashboard is developed with python.

## Installation
* Navigate to the [conda-forge](https://conda-forge.org/download/) website to download the installer.
* Download the installer and run (Be sure to be in the directory that contains the installer you just downloaded.)
  ```
  bash Miniforge3-$(uname)-$(uname -m).sh
  ``` 
### Installing Packages
Install packages and create an environment with the [environment.yml](https://drive.google.com/file/d/1qa0S5UXKgzFx4F6LTPugD58Dar33baQ7/view?usp=drive_link) file

1. Download `yml` file
2. Run the follow
  
```
conda env create -n <my_env_name> -f /path/to/environment.yml 
```

## Build the Environment
* Activate the environment 
  ```
  conda activate <my_env_name>
  ```
* Deactivate the environment 
  ```
  conda deactivate
  ```
## Removing an Environment
* To remove an environment 
  ```
  conda remove --name <my_env_name> --all
  ```
## Structure and Use
These scripts require the setup of a `.env` file for the filepaths. This will hold the sheet identifier.

To launch the app, ensure that the environment is active, then use 
```
python3 app.py
```
The app will launch in the terminal. When launched, navigate to `http://127.0.0.1:8050/` to see the site.

![Dashboard Home Page](./assets/Screenshot%202026-08-10%20at%2020.12.05.png)

---
## License
This work is licensed under [The MIT License](https://opensource.org/license/mit).

## Contact Information
```
Digital Preservation Services - preservation@frdr-dfdr.ca
```

## Resources
* [`conda_forge` documentation](https://docs.conda.io/en/latest/)
* [`miniforge3` documentation](https://conda-forge.org/download/)
* [Conda Cheat Sheet](https://media.datacamp.com/legacy/image/upload/v1681474450/Marketing/Blog/Conda_Cheat_Sheet_1.pdf)

