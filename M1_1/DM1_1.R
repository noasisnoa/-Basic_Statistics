#1주차-1교시

getwd()
setwd("C:/Users/user/Desktop/ran/DataMining")
bumpus <-read.csv("Bumpus.csv")
class(bumpus)
attach(bumpus)
str(bumpus)
head(bumpus)
summary(bumpus)
# x축, y축 이름 붙이기
plot(alar~length, xlab = 'Length', ylab='Alar', main = 'Hermon Bumpus')
plot(alar~length, xlab = 'Length', ylab='Alar', main = 'Hermon Bumpus', pch = 15)
plot(alar~length, xlab = 'Length', ylab='Alar', main = 'Hermon Bumpus', pch = 22, bg ='red')
plot(alar~length, xlab = 'Length', ylab='Alar', main = 'Hermon Bumpus', pch = 22, bg ='green')
plot(alar~length, xlab = 'Length', ylab='Alar', main = 'Hermon Bumpus', pch = 8, bg ='green')

#x축 전체 길이(length), y축 날개 길이 (alar), 생존( survive)색깔로 구별

plot(alar~length, col = survive, pch = c(0,15), bg = 'red', xlab = 'Length', ylab = "Alar", main = 'Bumpus')
