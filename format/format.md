
## 数据结构

### identifier, 课程唯一 ID
    
### arrangement, 课程安排

 #### start_week, 起始周
    整数，代表行课第一周的周数
 #### end_week, 结束周
    整数，代表行课最后一周的周数
 #### odd_week, 单周安排

  ##### week_day, 课程星期
    整数，从 1 到 7 分别代表星期一到星期日。
  ##### start_from, 开始课程节数
    整数，取值范围从 1 到 14。代表上课在每一天中的时间段。
  ##### end_at, 课程结束节数
    整数，取值范围从 1 到 14。代表上课在每一天中的时间段。
  ##### classroom, 教室
    字符串。代表对应天的授课教室。

 #### even_week, 双周安排

  ##### week_day, 课程星期
    整数，从 1 到 7 分别代表星期一到星期日。
  ##### start_from, 开始课程节数
    整数，取值范围从 1 到 14。代表上课在每一天中的时间段。
  ##### end_at, 课程结束节数
    整数，取值范围从 1 到 14。代表上课在每一天中的时间段。
  ##### classroom, 教室
    字符串，代表对应天的授课教室。
  
### name, 课程名称
    字符串。教务处官方对于此门课程的称呼。包含全角括号的附加说明。

### teacher, 教师
    字符串。授课教师的名字。
    
### teacher_title, 教师职称
    字符串。授课教师的职称。

### year, 起始学年
    整数。官方给出的表示格式为 201x-201(x+1) 学年。简单起见，以秋季学期开始的年份作为起始学年。

### term, 学期
    整数。可取 1、2 和 3。1 代表秋季学期（当年九月至十二月）。2 代表夏季学期（次年三月至六月）。3 代表夏季小学期（次年七月）。

### credit, 学分
    一位小数。小数部分仅可能为 1/2。代表学分。

### student_number, 学生人数
    整数。代表已经选择此门课的人数。




给出 JSON 文件样例：
```
{
	"data": [
		{
			"identifier": "002-(2018-2019-1)NA327(教学班)",
            "start_week": 1,
            "end_week": 17,
            "odd_week": [{
                "week_day": 2,
                "start_from": 9,
                "end_at": 10,
                "classroom": "上院418",
            }],
            "even_week": [{
                "week_day": 2,
                "start_from": 9,
                "end_at": 10,
                "classroom": "上院418",
            }],
            "name": "英美名诗赏析",
            "teacher": "何艳",
            "teacher_title": "大学讲师"
            "year": 2010,
            "term": 2,
            "credit": 2.0,
            "student_number": 37,
		}
	]
}
