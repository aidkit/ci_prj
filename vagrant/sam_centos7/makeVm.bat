
vagrant halt


set FILE_PATH=shareDir

mkdir shareDir > NUL 2>&1
if ERRORLEVEL 1 goto MKDIR_FAILED else goto MKDIR_TRUE

:MKDIR_TRUE
rem copy playbook.yml.org %FILE_PATH%\playbook.yml


:MKDIR_FAILED

vagrant up

vagrant provision

rem vagrant ssh
