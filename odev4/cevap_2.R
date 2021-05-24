df = data.frame(mtcars=mtcars)

new_df = subset(df, rownames(df) == "Ferrari Dino")

new_df$mtcars.hp