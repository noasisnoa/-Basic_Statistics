#1주차_2

iris<read.csv("iris.csv")
head(iris)
str(iris)
#head, 와 str 각각의 변수들이 무엇을 의미하는지 알아보기
#품종마다 다른 색까의 산점도 행렬
levels(iris$Species)
iris$Species <- factor(iris$Species)
levels(iris$Species)
# pair산점도를 보여준다.
pairs(iris[, 1:4])
pairs(iris[, 1:4], pch = 21, bg = c('red', 'blue', 'green')[iris$Species] )
par(mfrow=c(1, 2))## 산점도 행렬에서는 사용 안됨

# 꺽은선 그래프 또는 도수분호다각형
plot(iris$Sepal.Length)
plot(iris$Sepal.Length, col='red')
plot(iris$Sepal.Length, col='red', type = 'l')
plot(iris$Sepal.Length, col='red', type = 'b')
plot(iris$Sepal.Length, col='blue', type = 'c')
plot(iris$Sepal.Length, col='blue', type = 'b')
# lwd는 선의 굵기,  pch는 점의 모양
plot(iris$Sepal.Length, col='blue', type = 'o', lwd = 2)
plot(iris$Sepal.Length, col='blue', type = 'b', lwd = 2, pch= 19)
#lty는 선의 모양
plot(iris$Sepal.Length, col='blue', type = 'b', lwd = 2, pch= 19, lty = "dashed")


plot(iris$Sepal.Length[1:20], col='green', type = 'o', lwd = 2, pch= 18)

#삼차원 산점도 그리기
install.packages('scatterplot3d')
library(scatterplot3d)
plot3d(iris[, 1:3], size = 7, col = c(rep('red', 50), rep('blue', 50), rep('green', 50)))

#체르노프 얼굴 표현하기
install.packages("aplpack")
library(aplpack)
iris[1:10, 1:4]
faces(iris[1:10, 1:4], face.type = 3, main = 'Chernoff faces : faces.type = 0')
iris[1:10, 2:5]
faces(iris[1:10, 2:5], face.type = 0, nrow = 3, main = 'Chernoff faces : faces.type = 0')
faces(iris[1:10, 2:5], face.type = 1, nrow = 3, main = 'Chernoff faces : faces.type = 1')
faces(iris[1:10, 2:5], face.type = 2, nrow = 3, main = 'Chernoff faces : faces.type = 2')
