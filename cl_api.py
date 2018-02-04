import os

GFW_LIST = '/etc/gfwlist/china-banned'


cl_dict = {
    'ss': {'status': 'ps|grep "ss-redir"|grep -v grep|wc -l',
          'restart': '/etc/init.d/ss-redir.sh restart',
           'stop': '/etc/init.d/ss-redir.sh stop',
           'start': '/etc/init.d/ss-redir.sh start'
          },

}


def run_cmd(cmd):
    os.system(cmd)


def add_file_list(file_, nline):
    with open(file_, 'a') as f:
        f.write(nline + '\n')


def read_file(file_):
    with open(file_, 'r') as f:
        return f.read()


def read_gfwlist():
    return read_file(GFW_LIST)


def add_gfwlist(url):
    return add_file_list(GFW_LIST, url)