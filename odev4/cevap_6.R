df = data.frame(Puromycin=Puromycin)

treated_list = subset(df, Puromycin.state == "treated")
untreated_list = subset(df, Puromycin.state == "untreated")

nrow(untreated_list) / nrow(treated_list) * 100