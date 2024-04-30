#Mean Function
def mean(numbers):
  return sum(numbers) / len(numbers)

#Mode Function
def mode(numbers):
  frequency = {}
  for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
  max_freq = max(frequency.values())
  modes = [num for num, freq in frequency.items() if freq == max_freq]
  return modes[0] if len(modes) == 1 else modes

