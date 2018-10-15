#!/usr/bin/env python3
import subprocess


class GithubConverter:

    def __init__(self):
        pass

    def create_issue(self, title, description, assignees='', milestone='', label='', browser_open=0):

        message = title + '\n\n' + description

        cmd = ['hub', 'issue', 'create', '-m', message]

        if assignees != '':
            cmd.extend(['-a', assignees])

        if milestone != '':
            cmd.extend(['-M', milestone])

        if label != '':
            cmd.extend(['-l', label])

        if browser_open == 1:
            cmd.append('-o')

        try:
            out = subprocess.run(cmd, stdout=subprocess.PIPE)
            print(out.stdout.decode())
        except Exception as e:
            print("Error. {}".format(e.args))

    def create_issue_for_template(self):
        title = 'New Issue'
        description = '<!-- 要望のテンプレート -->\n\n## 概要\n\n## タスク\n\n* [ ] 細かいタスクに分解できているなら書き出す\n\n## 備考'
        self.create_issue(title, description, label='duplicate,good first issue', browser_open=1)


if __name__ == '__main__':
    github_converter = GithubConverter()
    # github_converter.create_issue_for_template()
