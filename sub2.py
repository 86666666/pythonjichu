def xieru():  #创建文件的函数
    with open('~/.vimrc','w')as pd:
        pd.write('filetype plugin on\n')
        pd.write("'let g:pydiction_location = '~/.vim/tools/pydiction/complete-dict\n'")