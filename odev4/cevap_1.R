df = data.frame(mtcars=mtcars)

max_index = apply(df[c('mtcars.mpg')], MARGIN = 2, FUN = max)

max_mpg_car = subset(df, mtcars.mpg == max_index[1])

print(max_mpg_car[1])