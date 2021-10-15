from collections import Counter
from datetime import datetime
import os
import re


def count_problem_source_code():
    problem_solve_code_list = []

    directory_list = [directory for directory in os.listdir("./") if "DAY" in directory]

    for directory in directory_list:
        code_list = os.listdir(f"./{directory}")

        problem_solve_code_list += code_list

    name_list = [re.findall(r'\[[^)]*\]', code_name) for code_name in problem_solve_code_list]

    name_list = [name[0].replace("[", "").replace("]", "") for name in name_list if len(name) > 0]

    total_code_num = len(name_list)
    
    code_cnt_info = sorted(Counter(name_list).items(), key=lambda x: -x[1])

    return total_code_num, code_cnt_info


def make_count_info(total_code_num, code_cnt_info):
    count_info = f"#### 현재까지 풀어본 총 문제 수 : {total_code_num}개\n"

    for name in code_cnt_info:
        temp = f"- {name[0]} - {name[1]}개\n"
        count_info += temp

    return count_info


def make_read_me(count_info):
    return f"""## 코딩 1일 1문제! ( CODING TEST PRACTICE )
[![SOMJANG LOGO](/images/SOMJANG.png)](https://somjang.tistory.com/category/Programming/%EC%BD%94%EB%94%A9%201%EC%9D%BC%201%EB%AC%B8%EC%A0%9C)
## 하루에 한 문제 씩이라도 코딩문제를 풀어보자! 
### Since 2020.02.07 ~
#### 모든 문제는 Python3 로 해결하였습니다.
{count_info}
#### 아래의 페이지에서 제공하는 문제들로 구성되어 있습니다.
[![BaekJoon](/images/BaekJoon.png)](https://www.acmicpc.net/)
[![Programmers](/images/Programmers.png)](https://programmers.co.kr/)
[![Samsung_SW_Academy](/images/Samsung_SW_Academy.png)](https://swexpertacademy.com/main/main.do)
[![LeetCode](/images/LeetCode.png)](https://leetcode.com/)
[![HackerRank](/images/HackerRank.png)](https://www.hackerrank.com/)
<p align="center"><a href="http://www.jungol.co.kr/"><img src="/images/JUNGOL.png"></a></p>
<p align="center"><a href="https://codeup.kr/"><img src="/images/CodeUp.png"></a></p>"""


def update_readme_md():
    total_code_num, code_cnt_info = count_problem_source_code()

    count_info = make_count_info(total_code_num=total_code_num, code_cnt_info=code_cnt_info)

    readme = make_read_me(count_info=count_info)

    return readme


if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)