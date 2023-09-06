import re

def arithmetic_arranger(problems, display = False):
  if len(problems) > 5:
    return 'Error: Too many problems.'

  arranged_problems = [[],[],[]]

  if display:
    arranged_problems.append([])

  for problem in problems:
    problem = problem.replace(' ','')
    
    match = re.search('[\+\-]', problem)
    
    if not match:
      return "Error: Operator must be '+' or '-'."
      
    operator = match.group()

    numbers = problem.split(operator)

    firstNum, secondNum = numbers[0], numbers[1]

    if len(firstNum) > 4 or len(secondNum) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    if not firstNum.isdigit() or not secondNum.isdigit():
      return 'Error: Numbers must only contain digits.'

    maxLen = max(len(firstNum), len(secondNum))

    arranged_problems[0].append('  ' + ' ' * (maxLen - len(firstNum)) + firstNum)
    arranged_problems[1].append(operator + ' ' + ' ' * (maxLen - len(secondNum)) + secondNum)
    arranged_problems[2].append('-' * (maxLen + 2))

    if display:
      if operator == '+':
        result = int(firstNum) + int(secondNum)
      else:
        result = int(firstNum) - int(secondNum)

      result = str(result)

      arranged_problems[3].append(' ' * (maxLen - len(result) + 2) + result)
        

  arranged_problems[0] = '    '.join(arranged_problems[0])
  arranged_problems[1] = '    '.join(arranged_problems[1])
  arranged_problems[2] = '    '.join(arranged_problems[2])

  if display:
    arranged_problems[3] = '    '.join(arranged_problems[3])

  arranged_problems = '\n'.join(arranged_problems)

  if display:
    print(arranged_problems)
  
  return arranged_problems