from operator import add
import pyspark
from pyspark.mllib.feature import HashingTF

myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder\
    .master("local")\
    .appName("myApp")\
    .config(conf=myConf)\
    .getOrCreate()
lines=spark.sparkContext.textFile("ds_spark_wiki.txt")
wc=lines\
    .flatMap(lambda x: x.split(' '))
print type(wc)
print wc.collect()[:]
print "---> Korean:",wc.collect()[10]

wc = spark.sparkContext.textFile("ds_spark_wiki.txt")\
    .flatMap(lambda x: x.split(' '))\
    .map(lambda x: (x.lower().rstrip().lstrip().rstrip(',').rstrip('.'), 1))\
    .reduceByKey(add)

print wc.count()
print wc.first()

wc = spark.sparkContext.textFile("ds_spark_wiki.txt")\
    .map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())\
    .map(lambda x:x.split())\
    .map(lambda x:[(i,1) for i in x])

for e in wc.collect():
    print e

documents = spark.sparkContext.textFile("ds_spark_wiki.txt")\
    .map(lambda line: line.split(" "))
hashingTF = HashingTF()
tf = hashingTF.transform(documents)
tf.collect()