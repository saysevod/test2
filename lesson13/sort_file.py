dicts = []

if __name__ == '__main__':
    with open('src_14.txt', 'r') as f:
        list_one = f.readlines()
        for line in list_one:
            line = line.split()
            mark = [int(i) for i in line[2:]]
            dicts.append({'name': line[0], 'family': line[1], 'mark': sum(mark) / len(mark)})

    list_two = list(filter(lambda person: person['mark'] < 5, dicts))
    for i in list_two:
        print("{:<20} {:.3}".format(' '.join([i['family'], i['name'][0]]) + '.', i['mark']))

    print("Middle score {:.3}".format(sum(i['mark'] for i in dicts) / len(dicts)))

    with open('out_14.txt', 'w') as f:
        for i in dicts:
            f.write("{:<20} {:.3} \n".format(' '.join([i['family'], i['name'][0]]) + '.', i['mark']))



