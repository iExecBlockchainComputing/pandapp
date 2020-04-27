# Objective:



We started from

* https://github.com/abeusher/geohash2kml.git
* https://github.com/ashwin711/proximityhash.git

## usefful link
* Geohash map
```http://geohash.gofreerange.com/```


## Command to execute the script


python3 backend.py tracks ; python3 geohash2kml.py tracks heatmap

* Backend.py create generate geohash samples and creates dataset

   * output : geohash dict
* Geohask2kml creates kml file from dataset.

   * input : geohash dict
   * output : heatmap in kml file    

## Précision geohash


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
