git add --all
git status
set /p message= Message commit : 
git commit -m "%message%"
git push