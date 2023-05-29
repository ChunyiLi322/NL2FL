import difflib
import Levenshtein

def similar_lvst_jaro(str1, str2):
     return Levenshtein.jaro(str1, str2)
 
def similar_lvst_hamming(str1, str2):
     return Levenshtein.hamming(str1, str2)
 
def similar_lvst_distance(str1, str2):
     return Levenshtein.distance(str1, str2)

def get_file_textlist(file_path):
     file_textlist = []
     with open(file_path, "r", encoding='utf-8') as file:
         for line in file:
             line = line.strip('\n')
             file_textlist.append(line)
         file.close()
     return  " ".join(file_textlist)

def record_sim(result_list, file_path):
     with open(file_path, 'a') as f:
          for i in result_list:
                 f.write(i + ',')
          f.write('\n')
          f.close()


str_file_1 = get_file_textlist("dataset_ltl_2.txt")
str_file_2 = get_file_textlist("our_method.txt")


result_list = []
result_list.append(str(difflib.SequenceMatcher(None, str_file_1, str_file_2).quick_ratio()))
result_list.append(str(Levenshtein.ratio(str_file_1, str_file_2)))
result_list.append(str(similar_lvst_jaro(str_file_1, str_file_2)))
result_list.append(str(similar_lvst_distance(str_file_1, str_file_2)))

sim_result_file_path = "sim_result.txt"
record_sim(result_list, sim_result_file_path)



