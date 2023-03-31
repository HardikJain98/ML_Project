---
layout: page
title: Data Pre-processing
permalink: /preprocessing
nav_order: 4
---

# Core Temperature Estimation of Electric Vehicle Battery Packs

## Data Pre-processing
<br/>

### Data Cleaning
The dataset was largely clean initially but required some manual effort to fully clean. Data entry errors (e.g., inconsistent use of delimiting characters) were corrected and special characters (e.g., the degree symbol for temperature) were removed, as their presence produced errors when programmatically reading in data.

<br/>
### Missing Data
During cleaning, two types of missing data were observed. As mentioned earlier, the original dataset was partitioned into 70 data files. It was observed that some features were entirely missing from some data files. Fortunately, features relevant to the prediction task are not impacted by this type of missing data. The dataset contains an overall of ~1.09M data points, of which ~54000 data points were intermittently missing, likely due to sensor failure. Since the percentage of missing data was < 5%, which is below the acceptable limit, we chose to discard those data points, leaving us with an overall of 1.04M data points to train our models. [Table 1](preprocessing#missing-data) lists the measured quantities (features) in the dataset, their units of measure, and describes the nature of missing measurements in the dataset, if any.


 | Number      | Feature                                      | Units        | Notes on Missing Data                           |
 | ----------- | -------------------------------------------- | ------------ | ----------------------------------------------- |
 | 1           | Elapsed Time Since Start of Trip             | s            |                                                 |
 | 2           | Vehicle Velocity                             | km/h         |                                                 |
 | 3           | Vehicle Elevation                            | m            |                                                 |
 | 4           | Throttle Depression                          | %            |                                                 |
 | 5           | Motor Torque                                 | Nm           |                                                 |
 | 6           | Longitudinal Acceleration                    | m/s^2        |                                                 |
 | 7           | Regenerative Braking Signal (On/Off)         |              |                                                 |
 | 8           | Battery Voltage                              | V            |                                                 |
 | 9           | Battery Current                              | A            |                                                 |
 | 10          | Battery Temperature (*)                      | °C           |                                                 |
 | 11          | Max. Battery Temperature                     | °C           |                                                 |
 | 12          | Battery State of Charge (SoC)                | %            | Intermittently missing in < 3% of observations  |
 | 13          | Displayed SoC                                | %            |                                                 |
 | 14          | Min. SoC                                     | %            |                                                 |
 | 15          | Max. SoC                                     | %            |                                                 |
 | 16          | Heating Power CAN                            |              |                                                 |
 | 17          | Heating Power LIN                            |              | Missing in data files 2-21                      |
 | 18          | Requested Heating Power                      | W            |                                                 |
 | 19          | Air Conditioner Power                        | kW           |                                                 |
 | 20          | Heater Signal (On/Off)                       |              |                                                 |
 | 21          | Heater Voltage                               | V            | Missing in data files 2-21                      |
 | 22          | Heater Current                               | A            | Missing in data files 2-21                      |
 | 23          | Ambient Temperature                          | °C           |                                                 |
 | 24          | Coolant Temperature in Heater Core           | °C           | Missing in data files 2-21                      |
 | 25          | Requested Coolant Temperature                | °C           | Missing in data file 20                         |
 | 26          | Coolant Temperature at Inlet                 | °C           | Missing in data files 2-21                      |
 | 27          | Heat Exchanger Temperature                   | °C           |                                                 |
 | 28          | Cabin Temperature Sensor (*)                 | °C           |                                                 |
 | 29          | Ambient Temperature Sensor (*)               | °C           | Missing in data files 1-31                      |
 | 30          | Coolant Volume Flow +500 (*)                 | l/h          | Missing in data files 1-31                      |
 | 31          | Coolant Temperature at Heater Inlet (*)      | °C           | Missing in data files 1-31                      |
 | 32          | Coolant Temperate at Heater Outlet (*)       | °C           | Missing in data files 1-31                      |
 | 33          | Temperature at Heat Exchanger Outlet (*)     | °C           | Missing in data files 1-31                      |
 | 34          | Temperature at Lateral Left Defroster (*)    | °C           | Missing in data files 1-31                      |
 | 35          | Temperature at Lateral Right Defroster (*)   | °C           | Missing in data files 1-31                      |
 | 36          | Temperature at Central Defroster (*)         | °C           | Missing in data files 1-31                      |
 | 37          | Temperature at Central-Left Defroster (*)    | °C           | Missing in data files 1-31                      |
 | 38          | Temperature at Central-Right Defroster (*)   | °C           | Missing in data files 1-31                      |
 | 39          | Temperature in Driver Footwell (*)           | °C           | Missing in data files 1-31                      |
 | 40          | Temperature in Passenger Footwell (*)        | °C           | Missing in data files 1-31                      |
 | 41          | Temperature at Passenger Foot Vent (*)       | °C           | Missing in data files 1-31                      |
 | 42          | Temperature at Driver Foot Vent (*)          | °C           | Missing in data files 1-31                      |
 | 43          | Temperature at Passenger's Head (*)          | °C           | Missing in data files 1-31                      |
 | 44          | Temperature at Driver's Head (*)             | °C           | Missing in data files 1-31                      |
 | 45          | Temperature at Right Vent (*)                | °C           | Missing in data files 1-31                      |
 | 46          | Temperature at Central-Right Vent (*)        | °C           | Missing in data files 1-31                      |
 | 47          | Temperature at Central-Left Vent (*)         | °C           | Missing in data files 1-31                      |
 | 48          | Temperature at Left Vent (*)                 | °C           | Missing in data files 1-31                      |

<center> <b> Table 1: List of Features in Original Dataset, and Characterization of Missing Data </b> </center>
