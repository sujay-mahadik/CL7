library(arules)
library(arulesViz)
library(datasets)

data("Groceries")
itemFrequencyPlot(Groceries, topN=20, type="absolute")

rules <- (apriori(Groceries, parameter = list(supp=0.001, conf=0.8)))
options(digits = 2)
inspect(rules[1:5])

summary(rules)

rules<-sort(rules, by="confidence", decreasing=TRUE) 

rules <- apriori(Groceries, parameter = list(supp = 0.001, conf = 0.8,maxlen=3)) 

#redundancies -to do

# subset.matrix <- is.subset(rules, rules)
# subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA 

#before whole milk

rules<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.08), 
               appearance = list(default="lhs",rhs="whole milk"),
               control = list(verbose=F))
rules<-sort(rules, decreasing=TRUE,by="confidence")
inspect(rules[1:5]) 

#plot antecedants only prints top 100
plot(rules,method="graph",engine = 'interactive',shading=NA)

#after whole milk, confidence = 0.10 
rules<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.10), 
               appearance = list(default="rhs",lhs="whole milk"),
               control = list(verbose=F))
rules<-sort(rules, decreasing=TRUE,by="confidence")
inspect(rules[1:5])

#plot decendents
plot(rules,method="graph",engine = 'interactive',shading=NA)

