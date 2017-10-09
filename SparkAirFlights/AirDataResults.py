 
dfall.printSchema()
root
 |-- Year: integer (nullable = true)
 |-- Month: integer (nullable = true)
 |-- DayofMonth: integer (nullable = true)
 |-- DayOfWeek: integer (nullable = true)
 |-- DepTime: string (nullable = true)
 |-- CRSDepTime: integer (nullable = true)
 |-- ArrTime: string (nullable = true)
 |-- CRSArrTime: integer (nullable = true)
 |-- UniqueCarrier: string (nullable = true)
 |-- FlightNum: integer (nullable = true)
 |-- TailNum: string (nullable = true)
 |-- ActualElapsedTime: string (nullable = true)
 |-- CRSElapsedTime: string (nullable = true)
 |-- AirTime: string (nullable = true)
 |-- ArrDelay: integer (nullable = true)
 |-- DepDelay: string (nullable = true)
 |-- Origin: string (nullable = true)
 |-- Dest: string (nullable = true)
 |-- Distance: integer (nullable = true)
 |-- TaxiIn: integer (nullable = true)
 |-- TaxiOut: integer (nullable = true)
 |-- Cancelled: integer (nullable = true)
 |-- CancellationCode: string (nullable = true)
 |-- Diverted: integer (nullable = true)
 |-- CarrierDelay: integer (nullable = true)
 |-- WeatherDelay: integer (nullable = true)
 |-- NASDelay: integer (nullable = true)
 |-- SecurityDelay: integer (nullable = true)
 |-- LateAircraftDelay: integer (nullable = true)

 
 >>> df2007.count()
7453215
>>> df2008.count()
7009728

>>> dfall.count()
14462943

 
 dfall.describe().show()
+-------+-------------------+-----------------+------------------+-----------------+-----------------+------------------+------------------+-----------------+-------------+------------------+--------+------------------+------------------+------------------+-----------------+----------------+--------+--------+-----------------+-----------------+------------------+-------------------+----------------+--------------------+------------------+------------------+-----------------+-------------------+------------------+
|summary|               Year|            Month|        DayofMonth|        DayOfWeek|          DepTime|        CRSDepTime|           ArrTime|       CRSArrTime|UniqueCarrier|         FlightNum| TailNum| ActualElapsedTime|    CRSElapsedTime|           AirTime|         ArrDelay|        DepDelay|  Origin|    Dest|         Distance|           TaxiIn|           TaxiOut|          Cancelled|CancellationCode|            Diverted|      CarrierDelay|      WeatherDelay|         NASDelay|      SecurityDelay| LateAircraftDelay|
+-------+-------------------+-----------------+------------------+-----------------+-----------------+------------------+------------------+-----------------+-------------+------------------+--------+------------------+------------------+------------------+-----------------+----------------+--------+--------+-----------------+-----------------+------------------+-------------------+----------------+--------------------+------------------+------------------+-----------------+-------------------+------------------+
|  count|           14462943|         14462943|          14462943|         14462943|         14462943|          14462943|          14462943|         14462943|     14462943|          14462943|14379556|          14462943|          14462943|          14462943|         14462943|        14462943|14462943|14462943|         14462943|         14462943|          14462943|           14462943|          298183|            14462943|          14462943|          14462943|         14462943|           14462943|          14462943|
|   mean| 2007.4846681619363|6.447145508351931|15.726919203097184|3.929140424600996|1336.605297675433|1328.4101632703662|1481.6940567665158|1495.105587500414|         null|2205.5962054196025|     0.0|126.80747325060011|128.03373732505227|103.39937808896998|9.210410990779613|10.7069527075101|    null|    null|722.9955067236316| 6.77290690834805|   16.373497623358|0.02061696571714346|            null|0.002381534657227094| 5.887385316247028|1.1554270184173447|6.056198464014614|0.03243747180592452| 7.760700828140054|
| stddev|0.49976489673732016|3.416934870784115| 8.788870211900194|1.990331156762789|478.9956073954506|464.49195022971395|506.25527057698486|482.1153081605674|         null|1967.0831873187171|     0.0| 70.70196715010061| 69.90441560101189| 67.85862190138818|38.93204320043179|35.7483837564995|    null|    null|562.2161921259177|5.048903112368827|11.596487983783883|0.14209823305683705|            null|0.048742826284243514|25.567487308675396| 11.92238829308397|20.37778898279596| 1.2455322971387726|25.927525774181525|
|    min|               2007|                1|                 1|                1|                1|                 0|                 1|                0|           9E|                 1|       0|               100|               -10|                 0|               -1|              -1|     ABE|     ABE|               11|                0|                 0|                  0|               A|                   0|                 0|                 0|                0|                  0|                 0|
|    max|               2008|               12|                31|                7|               NA|              2359|                NA|             2400|           YV|              9743|  Unknow|                NA|                NA|                NA|               NA|              NA|     YUM|     YUM|             4962|               NA|                NA|                  1|               D|                   1|                NA|                NA|               NA|                 NA|                NA|
+-------+-------------------+-----------------+------------------+-----------------+-----------------+------------------+------------------+-----------------+-------------+------------------+--------+------------------+------------------+------------------+-----------------+----------------+--------+--------+-----------------+-----------------+------------------+-------------------+----------------+--------------------+------------------+------------------+-----------------+-------------------+------------------+

+-------+------------------+------------------+------------------+-----------------+-----------------+------------------+------------------+-----------------+-------------+------------------+--------+------------------+------------------+------------------+-----------------+-----------------+--------+--------+-----------------+-----------------+-----------------+-------------------+----------------+--------------------+-----------------+------------------+------------------+-------------------+------------------+
|summary|              Year|             Month|        DayofMonth|        DayOfWeek|          DepTime|        CRSDepTime|           ArrTime|       CRSArrTime|UniqueCarrier|         FlightNum| TailNum| ActualElapsedTime|    CRSElapsedTime|           AirTime|         ArrDelay|         DepDelay|  Origin|    Dest|         Distance|           TaxiIn|          TaxiOut|          Cancelled|CancellationCode|            Diverted|     CarrierDelay|      WeatherDelay|          NASDelay|      SecurityDelay| LateAircraftDelay|
+-------+------------------+------------------+------------------+-----------------+-----------------+------------------+------------------+-----------------+-------------+------------------+--------+------------------+------------------+------------------+-----------------+-----------------+--------+--------+-----------------+-----------------+-----------------+-------------------+----------------+--------------------+-----------------+------------------+------------------+-------------------+------------------+
|  count|          14462943|          14462943|          14462943|         14462943|         14462943|          14462943|          14462943|         14462943|     14462943|          14462943|14379556|          14462943|          14462943|          14462943|         14462943|         14462943|14462943|14462943|         14462943|         14462943|         14462943|           14462943|          298183|            14462943|         14462943|          14462943|          14462943|           14462943|          14462943|
|   mean|2007.4846681619363| 6.447145508351931|15.726919203097184|3.929140424600996|1336.605297675433|1328.4101632703662|1481.6940567665158|1495.105587500414|         null|2205.5962054196025|     0.0|126.80747325060011|128.03373732505227|103.39937808896998|9.210410990779613| 10.7069527075101|    null|    null|722.9955067236316| 6.77290690834805|  16.373497623358|0.02061696571714346|            null|0.002381534657227094|5.887385316247028|1.1554270184173447| 6.056198464014614|0.03243747180592452| 7.760700828140054|
| stddev|0.4997648967372985|3.4169348707842295| 8.788870211900155|1.990331156762788|478.9956073954552| 464.4919502297165| 506.2552705769881|482.1153081605677|         null|1967.0831873187221|     0.0| 70.70196715010081| 69.90441560101246| 67.85862190138806|38.93204320043172|35.74838375649943|    null|    null|562.2161921259165|5.048903112368822|11.59648798378389| 0.1420982330568369|            null| 0.04874282628424404|25.56748730867551|11.922388293083939|20.377788982795956| 1.2455322971387826|25.927525774181547|
|    min|              2007|                 1|                 1|                1|                1|                 0|                 1|                0|           9E|                 1|       0|               100|               -10|                 0|               -1|               -1|     ABE|     ABE|               11|                0|                0|                  0|               A|                   0|                0|                 0|                 0|                  0|                 0|
|    max|              2008|                12|                31|                7|               NA|              2359|                NA|             2400|           YV|              9743|  Unknow|                NA|                NA|                NA|               NA|               NA|     YUM|     YUM|             4962|               NA|               NA|                  1|               D|                   1|               NA|                NA|                NA|                 NA|                NA|
+-------+------------------+------------------+------------------+-----------------+-----------------+------------------+------------------+-----------------+-------------+------------------+--------+------------------+------------------+------------------+-----------------+-----------------+--------+--------+-----------------+-----------------+-----------------+-------------------+----------------+--------------------+-----------------+------------------+------------------+-------------------+------------------+


gall.agg( mean("ArrDelay").alias('MeanArrDelay') , max("ArrDelay").alias('MaxArrDelay'),  mean("DepDelay").alias('MeanDepDelay') , max("DepDelay").alias('MaxDepDelay')    ).orderBy(asc('MeanArrDelay'), asc('MeanDepDelay')).show()
+-------------+-------------------+-----------+-------------------+-----------+
|UniqueCarrier|       MeanArrDelay|MaxArrDelay|       MeanDepDelay|MaxDepDelay|
+-------------+-------------------+-----------+-------------------+-----------+
|           AQ|-1.5818131462333826|        623|0.17215657311669127|        624|
|           HA|0.45182667943492005|       1309|  -0.18222726926043|       1317|
|           WN|  5.264350118639599|        702| 10.311338571051937|        672|
|           9E|  5.914205493043974|       1942|  7.700845777541507|       1956|
|           F9|  6.745305443308771|        896|  6.648639431175783|        887|
|           AS|  6.967216748531098|        948|  8.713010822809819|        947|
|           US|  7.191071481817524|       1073|  8.885389910503964|       1003|
|           DL|  7.444714492035093|       1007|   7.81537367161734|       1003|
|           OO|  7.556672254452848|        990|   7.71341523603032|        996|
|           FL|   8.41180505408284|       1175|  9.064476424378338|       1206|
|           XE|  9.997841299026422|        939| 11.355493690093576|        927|
|           NW| 10.014710474456098|       2598|  7.687142635972174|       2601|
|           CO| 10.462609756019086|       1017| 12.325347567430173|       1011|
|           YV|  10.89507220203462|        714| 11.723962846719049|        696|
|           MQ|  11.02325960276846|       1707|  11.52477484685125|       1710|
|           UA| 11.739807794856294|       1351| 13.671641918134531|       1360|
|           B6| 11.983903638582756|       1042|  13.43854714726958|       1048|
|           OH| 12.058512635780748|       1209| 11.686115244996452|        966|
|           AA| 13.115129704167614|       1525| 13.618488757142327|       1521|
|           EV| 13.342191108468638|        969| 15.690412466986233|       1002|
+-------------+-------------------+-----------+-------------------+-----------+

Which carrier performs better?
gall.agg( mean("CarrierDelay").alias('MeanCarrierDelay') , max("CarrierDelay").alias('MaxCarrierDelay') ).orderBy(asc('MeanCarrierDelay')).show()
+-------------+------------------+---------------+
|UniqueCarrier|  MeanCarrierDelay|MaxCarrierDelay|
+-------------+------------------+---------------+
|           AQ|1.5978397341211226|            623|
|           FL|1.8022761092364765|           1175|
|           WN|1.8405589243343001|            668|
|           HA|2.7069177379852714|           1309|
|           F9|2.7399882183937745|            887|
|           CO|3.0604466494853653|           1001|
|           XE|3.0698334204474826|            927|
|           DL|3.1701267487228124|           1003|
|           B6|3.2001104399276463|           1042|
|           US|3.3561290514953632|            854|
|           MQ|3.6006776656416344|           1707|
|           OO|3.7839552427768637|            990|
|           UA| 3.787403527557245|           1351|
|           AS|3.8673153713454145|            947|
|           9E|3.9078127428947584|           1942|
|           AA| 4.457915368979174|           1312|
|           NW| 4.926080259466949|           2580|
|           OH| 5.723053635423765|            955|
|           YV| 6.744735040743357|            649|
|           EV|  7.97659705473978|            969|
+-------------+------------------+---------------+


 When is the best time of day/day of week/time of year to fly to minimise delays?

Best time of day : Morning 7 - 10 
arrudf = UserDefinedFunction(lambda time_str: ( time_str.split(time_str[-2:])[0]  )  , StringType())
garrtime = dfall.where((col("ArrTime") != "NA") ).groupBy( arrudf("ArrTime").alias("ArrTime") )
garrtime.agg( mean("ArrDelay").alias('MeanArrDelay') ).orderBy(asc('MeanArrDelay'), asc('MeanArrDelay')).show()
+-------+-------------------+
|ArrTime|       MeanArrDelay|
+-------+-------------------+
|      7| -4.194172286036355|
|      5| -2.900129963898917|
|      6| -2.523959705030287|
|      8| -1.651424904756972|
|      9|-0.3712623664229298|
|     10| 0.9789158357683616|
|     11| 2.8707159066779124|
|     12| 3.6808479606039866|
|     13|  5.021270186698142|
|     14|  6.243499931273121|
|     15|  6.450804587193484|
|     16|  7.767887482021382|
|     17|  9.727817423689274|
|     18|  11.44955378671402|
|     19|  13.23853107452039|
|     20| 14.339115190944936|
|     21| 17.858989325438703|
|      4| 20.039262380167308|
|     22| 20.341401141516926|
|     23|  27.92943740043494|
+-------+-------------------+
only showing top 20 rows


best DOW  = 6th day of week 
gdow = dfall.groupBy("DayOfWeek")
gdow.agg( mean("ArrDelay").alias('MeanArrDelay') ,  mean("DepDelay").alias('MeanDepDelay')  ).orderBy(asc('MeanArrDelay'), asc('MeanDepDelay')).show()
+---------+------------------+------------------+
|DayOfWeek|      MeanArrDelay|      MeanDepDelay|
+---------+------------------+------------------+
|        6|   5.7101990424787|  8.68195082401107|
|        2| 7.678264256179846| 8.980923059720622|
|        3| 8.077006919821867| 9.305653262849402|
|        1|  9.19519378221462| 10.88929316904604|
|        7| 9.708319888095971|11.551596253277044|
|        4|10.368171357047684|  11.1439297978086|
|        5|11.743698098373544|12.600269087046149|
+---------+------------------+------------------+


garrMonth = dfall.groupBy( col("Month").alias("Month") )
garrMonth.agg( mean("ArrDelay").alias('MeanArrDelay') ).orderBy(asc('MeanArrDelay'), asc('MeanArrDelay')).show()
+-----+------------------+
|Month|      MeanArrDelay|
+-----+------------------+
|    9|  2.27184064429342|
|   11|3.4654858426066157|
|   10|3.6042411167790847|
|    5|6.4377026614384665|
|    4| 7.522809690840997|
|    1| 9.387460035002983|
|    8|  9.62695585662609|
|    3|10.324373714947594|
|    7|11.803986083724837|
|    2|12.722600542807797|
|    6|14.351757953705537|
|   12|15.820482668836172|
+-----+------------------+

 Do older planes suffer more delays?

 Can you detect cascading failures as delays in one airport create delays in others? Are there critical
links in the system?

 Create a model to predict flight delays
 How well does weather predict plane delays?