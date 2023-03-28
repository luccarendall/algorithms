def study_schedule(permanence_period, target_time):
    # https://horadecodar.com.br/2020/12/08/if-com-multiplas-condicoes-em-python/
    pp = permanence_period
    tt = target_time
    if pp is None or tt is None or type(pp) != int or type(tt) != int:
        return None

# 1.1 - Retorne a quantidade de estudantes presentes
# para uma entrada específica;

# 1.2 - Retorne None se em permanence_period houver alguma entrada inválida;

# 1.3 - Retorne None se target_time recebe um valor vazio;

# 1.4 - A função deverá, por meio de análise empírica, se comportar (no
# avaliador remoto em sua Pull Request) como no máximo O(n), ou seja,
# com complexidade assintótica linear.
