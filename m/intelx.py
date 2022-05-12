from intelxapi import intelx
import m.key as KEY
import shutil

intelx = intelx(KEY.intelx)

def get_pastes(target):
    results = intelx.search(target, buckets=['pastes'], maxresults=2000)
    record_count = len(results['records'])
    print(f"|----[INFO][>] Found {record_count} records for {target} in bucket 'pastes'")

    if record_count <= 0:
        return None
    files = []

    for i in range(record_count +1):
        filename = f"../pastes/filepaste-{str(i)}.txt"
        print(f"|----[INFO][>] Downloading paste in{filename}")
        intelx.FILE_READ(results['records'][i]['systemid'], 0, results['records'][i]['bucket'], filename)
        files.append(filename)
    return files

def get_leaks(target):
    results = intelx.search(target, buckets=['leaks.public','leaks.private'], maxresults=2000)
    record_count = len(results['records'])
    print(f"|----[INFO][>] Found {record_count} records for {target} in bucket 'leaks'")

    if record_count <= 0:
        return None
    files = []    

    for i in range(record_count+1):
        filename = f"../pastes/fileleak-{str(i)}.txt"
        print(f"|----[INFO][>] Downloading leak in {filename}")
        intelx.FILE_READ(
            results['records'][i]['systemid'],
            0,
            results['records'][i]['bucket'],
            f"file-{str(i)}.txt",
        )

        files.append(filename)
    return files

def get_darknet(target):
    results = intelx.search(target, buckets=['darknet'], maxresults=2000)
    record_count = len(results['records'])
    print(f"|----[INFO][>] Found {record_count} records for {target} in bucket 'darknet'")

    if record_count <= 0:
        return None
    files = []

    for i in range(record_count+1):
        filename = f"../pastes/filedarknet-{str(i)}.txt"
        print(f"|----[INFO][>] Downloading link in darknet in {filename}")
        intelx.FILE_READ(
            results['records'][i]['systemid'],
            0,
            results['records'][i]['bucket'],
            f"file-{str(i)}.txt",
        )

        files.append(filename)
    return files

def attack(target):

    results = intelx.search(target)
    record_count = len(results['records'])
    files = []
    for i in range(record_count):
        filename = f"{target}-{str(i)}.txt"
        intelx.FILE_READ(results['records'][i]['systemid'], 0, results['records'][i]['bucket'], filename)
        files.append(filename)
    return files