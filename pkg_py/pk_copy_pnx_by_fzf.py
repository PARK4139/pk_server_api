from pkg_py.pk_core import cmd_to_os

# fail
# cmd_to_os(cmd='fzf | xclip -selection clipboard') 




# success
import subprocess

# 예시: 리스트를 fzf에 넘기고, 선택 결과를 받아오기
items = "\n".join(["apple", "banana", "cherry"])
proc = subprocess.Popen(
    f"echo {items!r} | fzf",
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)
selection, _ = proc.communicate()
print("선택한 항목:", selection.strip())
                          