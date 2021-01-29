import numpy as np
import math

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  row1 = list[:3]
  row2 = list[3:6]
  row3 = list[6:]
  col1 = [list[0], list[3], list[6]]
  col2 = [list[1], list[4], list[7]]
  col3 = [list[2], list[5], list[8]]

  meanRows =[
    findMean(row1),
    findMean(row2), 
    findMean(row3)
  ]
  meanCols =[
    findMean(col1), 
    findMean(col2), 
    findMean(col3)
  ]
  varRows = [
    findVariance(row1),
    findVariance(row2),
    findVariance(row3)
  ]
  varCols = [
    findVariance(col1), 
    findVariance(col2), 
    findVariance(col3)
  ]
  sdRows = [
    math.sqrt(findVariance(row1)),
    math.sqrt(findVariance(row2)),
    math.sqrt(findVariance(row3))
  ]
  sdCols = [
    math.sqrt(findVariance(col1)),
    math.sqrt(findVariance(col2)),
    math.sqrt(findVariance(col3))
  ]
  maxRows = [
    max(row1),
    max(row2), 
    max(row3)
  ]
  maxCols = [
    max(col1),
    max(col2), 
    max(col3)
  ]
  minRows =[
    min(row1),
    min(row2), 
    min(row3)
  ]
  minCols=[
    min(col1),
    min(col2), 
    min(col3)
  ]
  sumRows =[
    sum(row1),
    sum(row2),
    sum(row3)
  ]
  sumCols =[
    sum(col1),
    sum(col2),
    sum(col3)
  ]

  mean = [meanCols, meanRows, findMean(list)]
  variance = [varCols, varRows, findVariance(list)]
  stand_dev = [sdCols, sdRows,  math.sqrt(findVariance(list))]
  allMax = [maxCols, maxRows, max(list)]
  allMin = [minCols, minRows, min(list)]
  allSum = [sumCols, sumRows, sum(list)]
  
  calculations = {'mean': mean,'variance' : variance, 'standard deviation': stand_dev, 'max': allMax, 'min': allMin, 'sum': allSum}

  return calculations

def findMean(arr):
  tot = 0
  for i in range(len(arr)):
    tot += arr[i]
  return tot/len(arr)

def findVariance(arr):
  tot = 0
  mean = findMean(arr)
  for i in range(len(arr)):
    tot += (arr[i]-mean)**2
  return tot/len(arr)