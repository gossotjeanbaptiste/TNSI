git add --all
git status
set /p input= Message commit : 
git commit -m "%input%"
git push