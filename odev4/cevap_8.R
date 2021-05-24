df = data.frame(iris=iris)

new_df = aggregate(df[c('iris.Sepal.Length', 'iris.Sepal.Width', 'iris.Petal.Length', 'iris.Petal.Width')], list(Species = df$iris.Species), mean)

new_df