import os
import subprocess
## directories
user_path = os.path.expanduser('~')
exe_dir = os.path.join(user_path, 'Box/NU-malaria-team/projects/binaries/compartments/')
if "mrung" in user_path : git_dir = os.path.join(user_path, 'gitrepos/covid-chicago/')

initial_infect = [1,5,10]
#Ki = 0.319 # [0.319, 0.319]
#incubation_pd = 6.63 # [4,5,6]
#recovery_rate = 16 # [4,5,6]

for i in enumerate(initial_infect) :
    initial_infect_i = i[1]
    fin = open("simplemodel_covid.emodl", "rt")
    data = fin.read()
    data = data.replace('(species I 10)', '(species I ' + str(i[1]) +')')
    data = data.replace('(param Ki 0.319)', '(param Ki ' + str(Ki) +')')
    data = data.replace('(param incubation_pd 6.63)', '(param incubation_pd ' + str(incubation_pd) +')')
    data = data.replace('(param recovery_rate 16)', '(param recovery_rate ' + str(recovery_rate) +')')
    fin.close()

    fin = open("simplemodel_covid_i.emodl", "wt")
    fin.write(data)
    fin.close()

    # adjust simplemodel.cfg file as well
    fin = open("simplemodel.cfg", "rt")
    data_cfg = fin.read()
    data_cfg = data_cfg.replace('trajectories', 'trajectories_' + str(i[1]) )
    fin.close()

    fin = open("simplemodel_i.cfg", "wt")
    fin.write(data_cfg)
    fin.close()

    file = open('runModel_i.bat', 'w')
    file.write('\n"' + os.path.join(exe_dir, "compartments.exe") + '"' + ' -c ' + '"' + os.path.join(git_dir, "simplemodel_i.cfg") +
               '"' + ' -m ' + '"' + os.path.join( git_dir, "simplemodel_covid_i.emodl", ) + '"')
    file.close()

    subprocess.call([r'runModel_i.bat'])

