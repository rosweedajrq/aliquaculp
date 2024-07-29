def f(x):
    return (x + 1)

max_udf = udf(lambda x, y: max(x, y), IntegerType())
f_udf = udf(f, IntegerType())

df2 = df.withColumn("result", max_udf(f_udf(df.col1), f_udf(df.col2)))
