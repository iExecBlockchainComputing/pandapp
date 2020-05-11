# PANDAPP: PRIVACY PRESERVING DATA CONTRIBUTION 

A voluntary service to allow individuals to share their data to fight the pandemic spread.
Individual keeps the control of its data and its usage by third party. 
The solution leverages blockchain, data encryption and Trusted Execution Environments.

# Slides 
Everything is explained 
[presentation](https://github.com/iExecBlockchainComputing/pandapp/blob/master/Pandapp_hackathon.pdf)

# Requirements:

* iexec SDK 
* Python 3
* pip3 install python-geohash Geohash 

# The Apps in Trust Execution Environment
 
secure_heapmap and secure_socialdistance_calculation directories contain SGX apps source and encrypted datasets.      

Please follow instruction in the chapter "confidential computing" in docs.iex.ec to reproduce. 

 * https://docs.iex.ec/for-developers/quick-start-for-developers
 * https://docs.iex.ec/for-developers/your-first-app
 * https://docs.iex.ec/for-developers/confidential-computing

# Local development
  
If you want to develop or improve existing applications, you can start to work locally  
  
## Dataset generation

```
python3 generatetracks.py
...generates tracks for heatmap app : tracks_heatmap.data
...generates tracks for social distance app : tracks_socialdistance.data
```

## Applications

### Heatmap

The application generates an heatmap, then create the kml files  in a second program 

```
   python3 app_heatmap.py 
   Filename for dataset is tracks_heatmap.data
   heatmap in csv format saved in tempfile.csv
   output file is output_heatmap
   {'u05kngyj3': 24, '......, 'u05kngynf': 20, 'u05kngynd': 20}
   Done loading geohashcode counts.
   generate output_heatmap_simple.kml
   generate output_heatmap.kml
   Total execution time: 0.006757020950317383 seconds
```

Then you can charge the kml file generated in "Google my maps" 

![Heatmap](images/simple_maps.png "heatmap")

Red : hight density of person declared deceased.

Green: low density of person declared deceased.

### Social distance

```
   python3 app_socialdistance.py 2
   Filename for dataset is tracks_socialdistance.data
   [status 1 | [(0, 'u05kngyj3'), (1, 'u05kngyj3'), (2, 'u05kngyj3'), (3, 'u05kngyj3'), (4, 'u05kngyj3'), (5, 'u05kngyj3'), (6, 'u05kngyj3'), (7, 'u05kngyj3'), (8, 'u05kngyj3'), (9, 'u05kngyj3'), (10, 'u05kngyj3'), (11, 'u05kngyj3'), (12, 'u05kngyj3'), (13, 'u05kngyj3'), (14, 'u05kngyj3'), (15, 'u05kngyj3'), (16, 'u05kngyj3'), (17, 'u05kngyj3'), (18, 'u05kngyj3'), (19, 'u05kngyj3')]
   ....
   ....
   ....
   target  18 u05kngvff
   target  19 u05kngvfd
   *************RESULT***************
    you  met  3  person(s) declared deceased
    and  0  person(s) not declared deceased
   Total execution time: 0.0007197856903076172 seconds

```

# Links and references 

* useful github about gephash

    * https://github.com/abeusher/geohash2kml.git
    * https://github.com/ashwin711/proximityhash.git
    * https://github.com/kylebebak/py-geohash-any.git 

* Geohash map

```http://geohash.gofreerange.com/```

* iExec infrastructure

```docs.iex.ec```

* Geohash accuracy
 
| len  | Geohash length  | Cell width heigh  |
|------|-----------------|-------------------|
| 1    | ≤ 5,000km       | ×5,000km          |
| 2    | ≤ 1,250km       | ×	625km        | 
| 3    | ≤ 156km	     | ×	156km        |
| 4    | ≤ 39.1km	     | ×	19.5km       |
| 5    | ≤ 4.89km	     | ×	4.89km       |
| 6    | ≤ 1.22km	     | ×	0.61km       |
| 7    | ≤ 153m	         | ×	153m         |
| 8    | ≤ 38.2m	     | ×	19.1m        |
| 9    | ≤ 4.77m	     | ×	4.77m        |
| 10   | ≤ 1.19m	     | ×	0.596m       |
| 11	 |  149mm	     | ×	149mm        |
| 12   | ≤ 37.2mm	     | ×	18.6mm       |
