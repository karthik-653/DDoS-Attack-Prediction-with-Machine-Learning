import pandas as pd
import pickle
import ipaddress
import sys
new_x = pd.read_csv(sys.argv[1])

drop_cols = [
             'flow',
             'src',
             'total_fpackets',
             'total_bpackets',
             'total_bpktl',
             'flowBytesPerSecond',
             'flowPktsPerSecond',
             'max_flowiat',
             'min_flowiat',
             'total_biat',
             'max_biat',
             'std_biat',
             'total_fhlen',
             'min_biat',
             'bPktsPerSecond',
             'total_bhlen',
             'total_fhlen',
             'flow_syn',
             'downUpRatio',
             'total_fhlen',
             'fSubFlowAvgPkts',
             'bSubFlowAvgPkts',
             'fAvgSegmentSize',
             'std_active_s',
             'max_active_s',
             'min_active_s',
             'max_idle_s',
             'min_idle_s',
             'std_flowpktl',
             'bpsh_cnt',
             'furg_cnt',
             'burg_cnt',
             'flow_fin',
             'flow_psh',
             'flow_ece',
             'fAvgBytesPerBulk',
             'fAvgPacketsPerBulk',
             'fAvgBulkRate',
             'bAvgBytesPerBulk',
             'bAvgPacketsPerBulk',
             'bAvgBulkRate',
             'timestamp',
             'label']

new_x = new_x.drop(drop_cols, axis=1)

ips = new_x['dst']
converted=[]
for ip in ips:
    ip = int(ipaddress.IPv4Address(ip))
    converted.append(ip)

new_x['dst'] = converted
new_x['protocol']=new_x['protocol'].replace(['TCP'],6)

loaded_model = pickle.load(open('/Users/karthikeyan/Downloads/keyan/172.22.10.28:3000/github_upload/pcaps/final_knn.dat', 'rb'))
print(list(loaded_model.predict(new_x)))
