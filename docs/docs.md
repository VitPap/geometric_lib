# Geometric Lib 
Данная библиотека разработана для решения простых геометрических задач: подсчет площади, периметра простейших геометрических фигур

### circle.py

1. _Нахождение площади окружности_

Пример: circle.area(4) = 50,26
```python
def area(r): 
    '''принимает радиус r(float), возвращает площадь окружности(float)'''
    return math.pi * r * r
```

2. _Нахождение периметра окружности_

Пример: circle.perimeter(4) = 25,13
```python
def perimeter(r):
    '''принимает радиус r(float), возвращает периметр окружности(float)'''
    return 2 * math.pi * r
```

### rectangle.py

1. _Нахождение площади прямоугольника_

Пример: rectangle.area(4, 3) = 12
```python
def area(a, b):
    '''принимает числа a и b - длины сторон прямоугольника, возвращает площадь прямоугольника'''
    return a * b 
```

2. _Нахождение периметра прямоугольника_

Пример: rectangle.perimeter(4, 3) = 14
```python
def perimeter(a, b): 
    '''принимает числа a и b - длины сторон прямоугольника, возвращает периметр прямоугольника'''
    return (a + b) * 2 
```

### square.py

1. _Нахождение площади квадрата_

Пример: square.area(4) = 16
```python
def area(a):
    '''принимает число a - длина стороны квадрата, возвращает площадь квадрата'''
    return a * a
```

2. _Нахождение периметра квадрата_

Пример: square.perimeter(4) = 16
```python
def perimeter(a):
    '''принимает число a - длина стороны квадрата, возвращает периметр квадрата'''
    return 4 * a
```

### triangle.py
1. _Нахождение площади треугольника_

Пример: triangle.area(4, 3) = 6
```python
def area(a, h): 
    '''принимает числа a и h - длина стороны и высоты треугольника, возвращает площадь треугольника'''
    return a * h / 2 
```

2. _Нахождение периметра треугольника_

Пример: triangle.perimeter(4, 5, 3) = 12
```python
def perimeter(a, b, c): 
    '''принимает числа a,b,c - длины сторон треугольника, возвращает периметр треугольника'''
    return a + b + c
```
## История изменений библиотеки 
* ad5851a Create docs.md
* c984e76 [docs]: adding function description
* 403114c Editing report(readMe.pdf)
* f05c90d [add] ReadMe.pdf
* 4d446c2 fix rectangle calculation
* 883732b add file for triangle
* b6c44a1 addding new file
* c5860c4 addding new file
* d078c8d L-03: Docs added
* 8ba9aeb L-03: Circle and square added