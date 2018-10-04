mydb<- read.csv('pca_gsp.csv')
attach(mydb)
names(mydb)

X <- cbind(Ag, Mining, Constr, Manuf, Manuf_nd, Transp, Comm, Energy, TradeW, TradeR, RE, Services, Govt) 

cor(X) 

pcal<-princomp(X, scores=TRUE, cor=TRUE) 
summary(pcal) 

loadings(pcal) 
plot(pcal)
screeplot(pcal,type="line",main="Screen Plot") 
biplot(pcal) 

pcal$scores[1:10,] 
