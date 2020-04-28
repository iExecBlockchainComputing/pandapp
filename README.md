# User centric data sharing service to fight pandemic spread 

We build a voluntary service to allow individuals to share their status and contact traces,
Individuals will allow the processing of the data under their control, their datas will be shared 
to white listed applications running in SGX enclaves, where data cant be leaked and the processing cannot be tampered.


## usefful link
* Geohash map
```http://geohash.gofreerange.com/```
*iExec infrastructure
```docs.iex.ec```

## Command to execute the script

* Backend.py create generate geohash samples and creates dataset
   * output : geohash dict in a file

```python3 backend.py tracks```


* Geohask2kml creates kml file from dataset.
   * input : geohash dict file
   * output : heatmap in kml file    

```python3 geohash2kml.py tracks heatmap```



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
