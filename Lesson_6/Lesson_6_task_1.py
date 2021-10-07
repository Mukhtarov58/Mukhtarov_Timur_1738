def prsing_log(log):
    log_name = log.split(' ')
    return tuple([log_name[0], log_name[5].replace('"', ''), log_name[6]])


log_list = []
with open('nginx_logs.txt', encoding='utf-8') as f:
    log = f.readline().replace('/n', '')
    while log:
        log_list.append(prsing_log(log))
        log = f.readline().replace('/n', '')

for i in range(5):
    print(log_list[i])

