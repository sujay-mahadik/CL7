myData <- read.csv('E:/github/CL7/MLA/Assignment8/pca_gsp.csv')
attach(myData)
names(myData)

myDataPCA <- cbind(Ag, Mining, Constr, Manuf, Transp, Comm, Energy, TradeW, TradeR ,RE, Services, Govt)

myDataPCA

cor(myDataPCA)

pca <- princomp(myDataPCA, cor = TRUE, scores = TRUE)

plot(pca)
plot(pca, type = 'l')
biplot(pca)