
def file_name(name_of_file):
    l = []
    name = []
    priority = []
    with open(name_of_file) as f:
        for line in  f :
            if line.startswith('Customer_') :
                s = line
                new_s = s.strip('Customer_')
                ns = new_s.lstrip('0123456789_')
                st = ns.strip('Priority:')
                stf = st.strip()
                l.append(stf)

    for i in range(0,len(l),2):
        name.append(l[i])

    for i in range(1,len(l),2):
        priority.append(l[i])


    return name, priority
