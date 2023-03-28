def study_schedule(permanence_period, target_time):
    # https://horadecodar.com.br/2020/12/08/if-com-multiplas-condicoes-em-python/
    # https://bit.ly/3JUusaK
    pp = permanence_period
    tt = target_time
    num_students = 0
    for initial_time, final_time in pp:
        if pp is None or tt is None \
                or type(initial_time) != int \
                or type(final_time) != int:
            return None
        if initial_time <= target_time <= final_time:
            num_students += 1
            # Incrementa o contador se estudantes estiveram presentes
            # durante o período de tempo
    return num_students

# Dica para o futuro:
# Na validação de tipos tb poderia usar um isinstance(). Em havendo
# necessidade de herança, seria uma escolha mais flexivel
# Ex.: isinstance(initial_time, int)
# https://bit.ly/3KdbGwB
