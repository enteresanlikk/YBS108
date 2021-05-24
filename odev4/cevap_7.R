df = data.frame(iris=iris)

new_df = aggregate(df$iris.Petal.Length, list(df$iris.Species), mean)

max_index = apply(new_df, MARGIN = 2, FUN = max)

max_index[c('Group.1')]
