import glob
import athletemodel
import yate

data_files = glob.glob("data/*.txt") #glob模块可以向操作系统查询一个文件名列表
athletes = athletemodel.put_to_store(data_files)

print(yate.start_respone())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an athlete from the list to work with:"))

for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
print(yate.end_form("Select"))

print(yate.include_footer({"Home":"/index.html"}))