def tree(file1, file2):
    keys = file1.keys() | file2.keys()
    result = []
    for key in sorted(keys):
        child1 = file1.get(key)
        child2 = file2.get(key)
        if key not in file2:
            result.append({
                "key": key,
                "type": "deleted",
                "value": child1,
            })
        elif key not in file1:
            result.append({
                "key": key,
                "type": "added",
                "value": child2,
            })
        elif file1[key] == file2[key]:
            result.append({
                "key": key,
                "type": "unchanged",
                "value": child1,
            })
        elif isinstance(child1, dict) and isinstance(child2, dict):
            result.append({
                "key": key,
                "type": "nested",
                "value": tree(child1, child2),
            })
        else:
            result.append({
                "key": key,
                "type": "changed",
                "value": [child1, child2],
            })
    return result