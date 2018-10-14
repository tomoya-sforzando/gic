#!/usr/bin/env python3
import subprocess


class GithubConverter:

    def __init__(self):
        pass

    def create_issue(self):

        cmd = ['hub', 'issue', 'create',  # create issue
               '-o',  # open browser
               '-m', 'Title\n\n<!-- 要望のテンプレート -->\n\n## 概要\n\n## タスク\n\n* [ ] 細かいタスクに分解できているなら書き出す\n\n## 備考',  # title + description
               '-a', 'tomoya-sforzando',  # assignee: username
               '-M', '1',  # milestone: number
               '-l', 'enhancement,good first issue'  # label: label name
               ]

        try:
            out = subprocess.run(cmd, stdout=subprocess.PIPE)
            print(out.stdout.decode())
        except Exception as e:
            print("Error. {}".format(e.args))


if __name__ == '__main__':
    github_converter = GithubConverter()
