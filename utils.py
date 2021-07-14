import csv


def to_list(Ifile_name):
    rsid = []
    alleles = []
    with open(Ifile_name, 'r') as data:
        data = csv.reader(data, delimiter='\t')
        for row in data:
            if len(row) == 4 and row[-1][-1] in ['A', 'T', 'G', 'C', '-', 'D', 'I']:
                rsid.append(row[0])
                alleles.append(row[-1])
    return rsid, alleles


def _to_list(Ifile_name):
    rsid = []
    alleles = []
    with open(Ifile_name, 'r') as data:
        data = csv.reader(data, delimiter='|')
        for row in data:
            rsid.append(row[0])
            alleles.append(row[-1])
    return rsid, alleles


def _zip_data(rsid, alleles):
    l = len(rsid)
    zip_datas = []
    for i in range(l):
        zip_data = f'{rsid[i]}|'
        if alleles[i][0] == alleles[i][-1]:
            zip_data += alleles[i][0]
        else:
            zip_data += alleles[i]
        zip_datas.append(zip_data)
    return '\n'.join(zip_datas)


def _unzip_data(rsid, alleles):
    l = len(rsid)
    unzip_datas = []
    for i in range(l):
        unzip_data = f'{rsid[i]}|'
        if len(alleles[i]) == 1:
            unzip_data += alleles[i] * 2
        else:
            unzip_data += alleles[i]
        unzip_datas.append(unzip_data)
    return '\n'.join(unzip_datas)


def output_txt(zip_datas, Ofile_name):
    with open(Ofile_name, 'w') as f:
        f.write(zip_datas)
