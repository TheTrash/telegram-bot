def shutdown(updater):
    updater.stop()
    updater.is_idle = False

lists = {'po':[], 'all':[]}

message = 'po'
if message in lists:
    print("true")