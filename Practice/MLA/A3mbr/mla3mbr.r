library(arules)
library(arulesViz)
library(datasets)

data("Groceries")

itemFrequencyPlot(Groceries, topN = 5, type = "absolute")

rules <- (apriori(Groceries, parameter = list(supp = 0.001, conf = 0.8)))
inspect(rules[1: 5])

summary(rules)

rules <- sort(rules, by = "confidence", decreasing = TRUE)
rules <- apriori(Groceries, parameter = list(supp = 0.001, conf = 0.8,maxlen=7))

rules <- apriori(Groceries,
                 parameter = list(supp  = 0.001, conf = 0.8),
                 appearance = list(default = "lhs", rhs = "whole milk"),
                 control = list(verbose = F))
                 
rules <- sort(rules, by = "confidence", decreasing = TRUE)

plot(rules, method = "paracoord")

plotly_arules(rules)

top10subRules <- head(rules, n = 10, by = "confidence")
plot(top10subRules, method = "graph", engine = "htmlwidget")

plot(top10subRules, method = "paracoord")
