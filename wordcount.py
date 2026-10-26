import sys
from pyspark.sql import SparkSession
def main():
    # 1. Initialize SparkSession
    spark = SparkSession.builder \
        .appName("WordCountSpark") \
        .getOrCreate()
    sc = spark.sparkContext
    input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "spark_output"
    # 2. Read lines from text file
    lines = sc.textFile(input_path)
    # 3. FlatMap: Split lines into individual words
    words = lines.flatMap(lambda line: line.strip().split())
    # 4. Map: Pair each word with count 1
    word_pairs = words.map(lambda word: (word.lower(), 1))
    # 5. ReduceByKey: Aggregate counts by word
    counts = word_pairs.reduceByKey(lambda a, b: a + b)
    # 6. Save or print results
    counts.saveAsTextFile(output_path)
    # Print directly to console for verification
    for word, count in counts.collect():
        print(f"{word}: {count}")
    spark.stop()
if __name__ == "__main__":
    main()