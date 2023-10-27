from mrjob.job import MRJob
import string
class CharCount(MRJob):
     def mapper(self, _, line):
          counts = {}
          for char in line:
               if char.isalpha():
                    char = char.lower()
                    if char in counts:
                         counts[char] += 1
                    else:
                         counts[char] = 1
          for char, count in counts.items():
                                   yield char, count
     def reducer(self, char, counts):
         yield char, sum(counts)
if __name__ == '__main__':
              CharCount.run()
