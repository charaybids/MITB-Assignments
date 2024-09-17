
'''
class Q5:
    def eval(self, n):
        return ['   \n o \n   ', '  o\n   \no  ', '  o\n o \no  ', 'o o\n   \no o', 'o o\n o \no o', 'o o\no o\no o'][n-1]

for i in range(1,7):
    print("i =", str(i))
    print(Q5().eval(i))
    print("----------")
'''

'''
from datetime import datetime, timedelta

class Q4:
    def eval(self, date_range):
        # Split the input string to get the start and end dates
        start_date, end_date = date_range.split()
        
        # Parse the input dates
        start = datetime.strptime(start_date, "%d/%m/%Y")
        end = datetime.strptime(end_date, "%d/%m/%Y")
        
        # Initialize result string
        palindromic_times = ""
        
        # Iterate through each day in the date range
        current_date = start
        while current_date <= end:
            # Iterate through each minute of the day
            for hour in range(24):
                for minute in range(60):
                    # Format the date and time
                    formatted_time = "{:02d}:{:02d}:{:02d}:{:02d}".format(
                        current_date.month, current_date.day, hour, minute)
                    # Check if the formatted string is a palindrome
                    if formatted_time == formatted_time[::-1]:
                        palindromic_times += formatted_time + "\n"
            # Move to the next day
            current_date += timedelta(days=1)
        
        return palindromic_times


# Example usage
q4 = Q4()
q4.eval("10/12/2024 07/01/2025")

'''


class Q3:
    
    def order(self, words):
        # Write a one-line lambda expression to do step 1.
       return sorted(words, key=lambda word: (word[1], len(word)))
    
    def to_int(self, words):
        # Write a one-line list comprehension to do step 2 to 4 (inclusively).
        return [(len(word) - 2) * (-1 if word.startswith('s') else 1) for word in words]

    def eval(self, words):
        words = self.order(words)
        scores = self.to_int(words)
        result = ''
        
        max_score = max(abs(score) for score in scores)
        for i, score in enumerate(scores):
            if score == 0:
                result += f'{i} =|\n'
            elif score < 0:
                result += f'{i} {"=" * abs(score)}|\n'
            else:
                result += f'{i} {" " * (max_score + 1)}|{"=" * score}\n'
        
        return result.strip()
    
print(Q3().eval(['it', 'set', 'seek', 'grade']))


'''
class Q2:
    
    def sort_the_integer(self, input_ls):
        
        flat_ls = []
       
        for element in input_ls:
            if isinstance(element, list):
                flat_ls.extend(self.sort_the_integer(element))
            else:
                if element is not None:
                    flat_ls.append(element)
        
        flat_ls.sort()         
                 
        return flat_ls

       
    def eval(self, input_ls):
        
        if not input_ls or len(input_ls) == 1: return input_ls
        
        if input_ls[1] == None: return input_ls
        
        flat_ls = []
        sorted_ls = []
        
        def flatten_list(nested_list):
            for element in nested_list:
                if isinstance(element, list):
                    flatten_list(element)
                else:
                    flat_ls.append(element)
        
        flatten_list(input_ls)
              
        flat_ls.sort(key=lambda x: (x is None, x))
        
        firstlist = [flat_ls[-2],flat_ls[-1]]
        templist = []
   
        for value in reversed(flat_ls):
                                   
            if len(sorted_ls) < 2:
                sorted_ls.insert(0,value)
                
            elif sorted_ls == firstlist:
                
                for index, item in enumerate(sorted_ls):
                    templist.append(sorted_ls[index])
                    
                sorted_ls.clear()
                sorted_ls.insert(0,templist)
                sorted_ls.insert(0, value)
                
            else:
                recurTempList = []
                
                for index, item in enumerate(sorted_ls):
                    recurTempList.append(sorted_ls[index])
                
                sorted_ls.clear()    
                sorted_ls.insert(0,recurTempList)
                sorted_ls.insert(0, value)
                            
        return sorted_ls
        

input_ls = [3, [2, [1, None]]] 

print("Sort the Integer: ", Q2().sort_the_integer(input_ls))
print("Eval Function: ", Q2().eval(input_ls))
print('\n')
'''  

'''
Class Q1:

    def eval(x, va, vb):
        #x = hours
        #va, vb = speed of a and b
            
        count = 0
        posA = x
        posB = 0
                    
        while not (posA == posB):
            posB += vb
            posA += va
            count += 1    

        return count

print(Q1().eval (2,1,2))s
'''
    