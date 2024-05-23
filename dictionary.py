student = {
"name":"Mark",
"Student_id": 15163,
"avg_grades": 2.6,
"ubytován": True,
"známky": [4,2,3,1,5],
"profesoři": {"matematika":"novotný","fyzika":"karel"}
}

print(student)
print(student["Student_id"])
student["ubytován"] = False
print(student)

student["lorem"] = "impsum"
print(student)

student["známky"].sort()
print(student["známky"])
student["známky"].append(5)
print(student["známky"])

print(student["profesoři"]["matematika"])

print(student["známky"][-1])
print(student["známky"][-1])

seznam_studentu = [{
"name":"Mark",
"Student_id": 15163,
"avg_grades": 2.6,
"ubytován": True,
"známky": [4,2,3,1,5],
"profesoři": {"matematika":"novotný","fyzika":"karel"}
},{
"name":"Mark",
"Student_id": 15163,
"avg_grades": 2.6,
"ubytován": True,
"známky": [4,2,3,1,5],
"profesoři": {"matematika":"novotný","fyzika":"karel"}
},{
"name":"Mark",
"Student_id": 15163,
"avg_grades": 2.6,
"ubytován": True,
"známky": [4,2,3,1,5],
"profesoři": {"matematika":"novotný","fyzika":"karel"}
}]
seznam_studentu[0]["name"] = "franta"
seznam_studentu[1]["name"] = "karel"
seznam_studentu[2]["name"] = "karolína"
print(seznam_studentu)