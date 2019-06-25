# finda-studyroom

![GitHub](https://img.shields.io/github/license/yuetsin/finda-studyroom.svg)
![GitHub release](https://img.shields.io/github/release/yuetsin/finda-studyroom.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/yuetsin/finda-studyroom.svg)

## Data Source Status

| Data Branch  | Status |
| ------------- | ------------- |
| Master (Default)  | [![Build Status](https://travis-ci.org/yuetsin/finda-studyroom.svg?branch=master)](https://travis-ci.org/yuetsin/finda-studyroom)  |
| Beta  | [![Build Status](https://travis-ci.org/yuetsin/finda-studyroom.svg?branch=be-ta)](https://travis-ci.org/yuetsin/finda-studyroom)  |

## 能做什么？

- [x] 从 electsys.sjtu.edu.cn 抓取到指定学期 XML、CSV 或 HTML 等格式的上课教室数据
  > 抓取本科生数据功能坏了（小声）得手动存一下文件

- [x] 解析 CSV 格式文件，转码输出为可读的 [JSON](https://github.com/yuxiqian/finda-studyroom/tree/master/json_output)

- [x] 将得到的数据可视化

  macOS 版
  > [electsys-utility](https://github.com/yuxiqian/electsys-utility)
  
  Web 版
  > [finda-studyroom](https://yuxiqian.github.io/index.html)
  
  Python 命令行版
  > [electsys-utility-cli](https://github.com/yuxiqian/electsys-utility-cli)

- [ ] 智能提供自习教室选择推荐

## 已知问题

- [ ] 无法获取医学院本科生课程数据。

- [ ] 2017 年秋季学期门牌号改动之后，新旧教室无法对应。

- [ ] 研究生课程教师无法显示职称。

## 支持的教学楼

### 闵行校区
上院、中院、下院、东上院、东中院、东下院、木兰楼、陈瑞球楼、杨咏曼楼

### 徐汇校区
徐汇中院、教一楼、新上院、工程馆

 > 由于数据源质量问题，以下校区教室信息不完善，仅供参考
### 卢湾校区
### 法华（长宁）校区
### 七宝校区
### 临港校区
### SMHC（上海市精神卫生中心）
